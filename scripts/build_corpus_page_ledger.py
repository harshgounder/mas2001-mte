#!/usr/bin/env python3
"""Build a per-page corpus ledger from sources.yaml and the conversion manifest.

The ledger has exactly one row for every page declared in sources.yaml. A page is
declared when its source carries `pages: N`; the rows for that source are numbered
1..N in file order, regardless of how many pages the PDF text layer turns out to
hold. That keeps the row set a pure function of the declaration, so the CSV can be
diffed across runs and validated by --check.

Each PDF's text layer is extracted exactly once with `pdftotext -layout`, split on
the form feed character that pdftotext writes between pages, and the resulting
pieces are mapped page N -> parts[N - 1]. pdftotext normally writes a trailing form
feed after the final page; that single trailing empty piece is dropped, so the
mapping stays exact and no phantom page is created.

`block_marker_count` is a machine hint only: it counts question-shaped lines such
as Q1, Example, Exercise, and Problem in the extracted page text. It is NOT a final
question count and must not be cited as one.

`record_state` is one of:
  converted                    the per-page markdown file exists and is non-empty
  pending                      the page is declared but has no usable markdown
  missing_source               the source PDF path does not point at a file
  source_page_count_mismatch   the text layer page count differs from `pages:`,
                               or pdftotext failed for an existing file

Usage:
  python3 scripts/build_corpus_page_ledger.py [--output PATH]
  python3 scripts/build_corpus_page_ledger.py --check [--output PATH]

--check rebuilds the ledger in memory from the current sources and exits nonzero
when the ledger on disk has a wrong header, missing or extra rows, colliding or
missing keys, per-source page gaps, or stale generated content. Standard library
only.
"""

import argparse
import csv
import hashlib
import io
import json
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCES_NAME = "sources.yaml"
MANIFEST_REL = pathlib.Path("work") / "manifest.jsonl"
MD_DIR_NAME = "md"
PAGE_DIR_REL = pathlib.Path("work") / "pages"
LEDGER_REL = pathlib.Path("reports") / "evidence" / "corpus-page-ledger.csv"

PDTOTEXT_TIMEOUT_S = 300

FIELDS = [
    "source_index",
    "label",
    "page",
    "declared_pages",
    "source_path",
    "source_sha256",
    "topic",
    "latest_manifest_status",
    "latest_model",
    "md_path",
    "md_exists",
    "md_chars",
    "png_exists",
    "raw_text_chars",
    "raw_text_sha256",
    "block_marker_count",
    "record_state",
]

BLOCK_MARKER_RE = re.compile(
    r"(?im)^[ \t]*(?:"
    r"Q(?:uestion)?[ \t]*\d+"
    r"|Example[ \t]*\d*"
    r"|Exercise[ \t]*\d*"
    r"|Problem[ \t]*\d*"
    r")\b"
)

_PARSE_SOURCES_YAML = None
_PARSE_LOOKUP_DONE = False


def log(message):
    print(message, file=sys.stderr, flush=True)


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _strip_comment(raw):
    out = []
    quote = None
    for char in raw:
        if quote is not None:
            out.append(char)
            if char == quote:
                quote = None
        elif char in "\"'":
            quote = char
            out.append(char)
        elif char == "#":
            break
        else:
            out.append(char)
    return "".join(out)


def _unquote(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def _fallback_parse_sources_yaml(text):
    """Same targeted parser as scripts/convert.py, used only if reuse is unsafe."""
    scalars = {}
    sources = []
    current = None
    for raw in text.splitlines():
        line = _strip_comment(raw).rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        content = line.strip()
        if indent == 0:
            current = None
            key, sep, value = content.partition(":")
            if not sep:
                continue
            key = key.strip()
            value = value.strip()
            if key == "sources" and value == "":
                continue
            scalars[key] = _unquote(value)
            continue
        if content.startswith("- "):
            current = {}
            sources.append(current)
            content = content[2:].strip()
        if current is None:
            continue
        key, sep, value = content.partition(":")
        if not sep:
            continue
        current[key.strip()] = _unquote(value.strip())
    return scalars, sources


def _reuse_parse_sources_yaml():
    """Return scripts.convert.parse_sources_yaml when importing it is safe."""
    global _PARSE_SOURCES_YAML, _PARSE_LOOKUP_DONE
    if _PARSE_LOOKUP_DONE:
        return _PARSE_SOURCES_YAML
    _PARSE_LOOKUP_DONE = True
    here = pathlib.Path(__file__).resolve().parent
    if str(here) not in sys.path:
        sys.path.insert(0, str(here))
    try:
        import convert as _convert
    except Exception:
        _convert = None
    parser = getattr(_convert, "parse_sources_yaml", None)
    if callable(parser):
        _PARSE_SOURCES_YAML = parser
    return _PARSE_SOURCES_YAML


def parse_sources(text):
    parser = _reuse_parse_sources_yaml()
    if parser is not None:
        return parser(text)
    return _fallback_parse_sources_yaml(text)


def parse_manifest_latest(path):
    """Map (label, page) to its last manifest record; last row wins."""
    latest = {}
    path = pathlib.Path(path)
    if not path.is_file():
        return latest
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(record, dict):
            continue
        try:
            page = int(record.get("page"))
        except (TypeError, ValueError):
            continue
        latest[(record.get("label"), page)] = record
    return latest


def extract_pdf_pages(pdf_path):
    """Run pdftotext once and return the list of page texts, or None on failure."""
    cmd = ["pdftotext", "-layout", str(pdf_path), "-"]
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            timeout=PDTOTEXT_TIMEOUT_S,
        )
    except Exception as exc:
        log("pdftotext failed for %s: %s" % (pdf_path, exc))
        return None
    if proc.returncode != 0:
        return None
    stdout = proc.stdout
    if isinstance(stdout, bytes):
        text = stdout.decode("utf-8", "replace")
    elif stdout is None:
        text = ""
    else:
        text = str(stdout)
    parts = text.split("\f")
    if parts and parts[-1] == "":
        parts.pop()
    return parts


def count_block_markers(text):
    """Machine hint only; never a final question count."""
    if not text:
        return 0
    return sum(1 for _ in BLOCK_MARKER_RE.finditer(text))


def read_text_chars(path):
    try:
        return len(path.read_text(encoding="utf-8", errors="replace"))
    except OSError:
        return 0


def _relative(path, root):
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except (ValueError, OSError):
        return path.as_posix()


def build_rows(sources, manifest_latest, repo_root):
    """Build one row per declared source page. No filesystem writes."""
    repo_root = pathlib.Path(repo_root)
    md_root = repo_root / MD_DIR_NAME
    page_root = repo_root / PAGE_DIR_REL
    rows = []
    for source_index, src in enumerate(sources, start=1):
        label = src.get("label") or ""
        try:
            declared = int(src.get("pages") or 0)
        except (TypeError, ValueError):
            declared = 0
        source_path = src.get("path") or ""
        source_sha256 = src.get("sha256") or ""
        topic = src.get("topic") or ""

        page_texts = None
        state_reason = None
        pdf = pathlib.Path(source_path)
        if not pdf.is_file():
            state_reason = "missing_source"
        else:
            page_texts = extract_pdf_pages(pdf)
            if page_texts is None or len(page_texts) != declared:
                state_reason = "source_page_count_mismatch"

        for page in range(1, declared + 1):
            text = ""
            if page_texts is not None and 1 <= page <= len(page_texts):
                text = page_texts[page - 1]

            md_path = md_root / label / ("p%03d.md" % page)
            md_exists = md_path.is_file()
            md_chars = read_text_chars(md_path) if md_exists else 0
            png_exists = (page_root / label / ("p%03d.png" % page)).is_file()

            record = manifest_latest.get((label, page)) or {}
            if state_reason == "missing_source":
                state = "missing_source"
            elif state_reason == "source_page_count_mismatch":
                state = "source_page_count_mismatch"
            elif md_exists and md_chars > 0:
                state = "converted"
            else:
                state = "pending"

            rows.append(
                {
                    "source_index": source_index,
                    "label": label,
                    "page": page,
                    "declared_pages": declared,
                    "source_path": source_path,
                    "source_sha256": source_sha256,
                    "topic": topic,
                    "latest_manifest_status": record.get("status") or "",
                    "latest_model": record.get("model") or "",
                    "md_path": _relative(md_path, repo_root),
                    "md_exists": md_exists,
                    "md_chars": md_chars,
                    "png_exists": png_exists,
                    "raw_text_chars": len(text),
                    "raw_text_sha256": sha256_text(text) if text else "",
                    "block_marker_count": count_block_markers(text),
                    "record_state": state,
                }
            )
    return rows


def row_values(row):
    values = []
    for key in FIELDS:
        value = row.get(key, "")
        if isinstance(value, bool):
            value = "true" if value else "false"
        elif value is None:
            value = ""
        values.append(str(value))
    return values


def render_csv(rows):
    """Deterministic CSV text: fixed field order, LF line endings, no timestamps."""
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(FIELDS)
    for row in rows:
        writer.writerow(row_values(row))
    return buffer.getvalue()


def write_csv(path, rows):
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "w", encoding="utf-8", newline="") as handle:
        handle.write(render_csv(rows))
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(tmp, path)


def check_ledger(actual_text, expected_rows):
    """Return a list of problems; empty means the ledger matches current reality."""
    problems = []
    expected_text = render_csv(expected_rows)
    try:
        actual = list(csv.reader(io.StringIO(actual_text, newline="")))
    except csv.Error as exc:
        return ["unreadable ledger: %s" % exc]
    if not actual:
        return ["ledger is empty"]

    header = actual[0]
    if header != FIELDS:
        missing = [field for field in FIELDS if field not in header]
        extra = [field for field in header if field not in FIELDS]
        problems.append(
            "header mismatch: missing=%s extra=%s" % (missing, extra)
        )

    body = actual[1:]
    expected_pairs = [row_values(row) for row in expected_rows]
    if len(body) != len(expected_pairs):
        problems.append(
            "row count mismatch: expected %d got %d" % (len(expected_pairs), len(body))
        )

    expected_keys = {}
    for values in expected_pairs:
        expected_keys[(values[0], values[1], values[2])] = values
    actual_keys = {}
    for values in body:
        if len(values) < 3:
            problems.append("short row: %r" % (values,))
            continue
        key = (values[0], values[1], values[2])
        if key in actual_keys:
            problems.append("duplicate key: %s" % (key,))
        actual_keys[key] = values

    missing_keys = sorted(set(expected_keys) - set(actual_keys))
    extra_keys = sorted(set(actual_keys) - set(expected_keys))
    if missing_keys:
        problems.append(
            "missing key(s): %d, first=%s" % (len(missing_keys), missing_keys[0])
        )
    if extra_keys:
        problems.append(
            "unexpected key(s): %d, first=%s" % (len(extra_keys), extra_keys[0])
        )

    expected_pages = {}
    for values in expected_pairs:
        expected_pages.setdefault((values[0], values[1]), set()).add(values[2])
    actual_pages = {}
    for values in body:
        if len(values) >= 3:
            actual_pages.setdefault((values[0], values[1]), set()).add(values[2])
    for source_key in sorted(expected_pages):
        wanted = expected_pages[source_key]
        found = actual_pages.get(source_key, set())
        if wanted != found:
            gaps = sorted(wanted - found)
            problems.append(
                "page gap for source %s: missing=%s" % (source_key, gaps)
            )

    if actual_text != expected_text:
        changed = [
            key
            for key in sorted(set(expected_keys) & set(actual_keys))
            if expected_keys[key] != actual_keys[key]
        ]
        note = ""
        if changed:
            note = " (%d changed row(s), first=%s)" % (len(changed), changed[0])
        problems.append("stale generated content%s" % note)

    return problems


def generate_rows(repo_root):
    repo_root = pathlib.Path(repo_root)
    sources_path = repo_root / SOURCES_NAME
    _, sources = parse_sources(sources_path.read_text(encoding="utf-8"))
    manifest = parse_manifest_latest(repo_root / MANIFEST_REL)
    return build_rows(sources, manifest, repo_root)


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Build or check the corpus page ledger.")
    parser.add_argument("--output", default=None, help="ledger CSV path")
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate an existing ledger and exit nonzero on drift",
    )
    return parser.parse_args(argv)


def main(argv):
    args = parse_args(argv)
    output = pathlib.Path(args.output) if args.output else (ROOT / LEDGER_REL)
    rows = generate_rows(ROOT)

    if args.check:
        if not output.is_file():
            log("check: missing ledger: %s" % output)
            return 1
        problems = check_ledger(output.read_text(encoding="utf-8"), rows)
        if problems:
            for problem in problems:
                log("check: %s" % problem)
            return 1
        print("check: ledger ok, %d row(s)" % len(rows))
        return 0

    write_csv(output, rows)
    print("wrote %d row(s) to %s" % (len(rows), output))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
