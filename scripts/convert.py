#!/usr/bin/env python3
"""Convert PDF slide decks into per-page markdown with a vision model.

Resumable, parallel, standard library only. See process/BRIEF-001-conversion-pipeline.md.

The pipeline reads sources.yaml and PROMPT.txt at runtime, renders each page to
a PNG with pdftoppm, and shells out to the existing vision CLI for transcription.
It never talks HTTP directly.
"""

import argparse
import concurrent.futures
import datetime
import hashlib
import json
import os
import pathlib
import subprocess
import sys
import threading
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
VISION = pathlib.Path.home() / ".local" / "bin" / "vision"
# user directive 2026-09-15: glm-5.3-flash on ollama-cloud
DEFAULT_MODEL = "glm-5.3-flash"

BACKOFF_S = (2, 6, 18)
MAX_ATTEMPTS = 4
BANNED_MARKERS = ("example.com", "](http", "https://")
TRUNCATED_MARKER = "[truncated"

VISION_TIMEOUT_S = 900
RENDER_TIMEOUT_S = 300
PDFINFO_TIMEOUT_S = 60

_MANIFEST_LOCK = threading.Lock()


def log(message):
    print(message, file=sys.stderr, flush=True)


def page_filename(page):
    return "p%03d" % page


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def utc_now():
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()


def write_text_atomic(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "w", encoding="utf-8") as handle:
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(tmp, path)


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


def parse_sources_yaml(text):
    """Tiny targeted parser for sources.yaml. Returns (scalars, sources)."""
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


def load_config():
    config_path = ROOT / "sources.yaml"
    scalars, sources = parse_sources_yaml(config_path.read_text(encoding="utf-8"))
    config = {
        "dpi": int(scalars.get("dpi") or 110),
        "max_tokens": int(scalars.get("max_tokens") or 6000),
        "workers": int(scalars.get("workers") or 6),
        "page_dir": scalars.get("page_dir") or "work/pages",
        "out_dir": scalars.get("out_dir") or "md",
    }
    return config, sources


def pdfinfo_pages(pdf):
    try:
        proc = subprocess.run(
            ["pdfinfo", str(pdf)],
            capture_output=True,
            text=True,
            timeout=PDFINFO_TIMEOUT_S,
        )
    except Exception:
        return 0
    if proc.returncode != 0:
        return 0
    for line in proc.stdout.splitlines():
        if line.startswith("Pages:"):
            try:
                return int(line.split(":", 1)[1].strip())
            except ValueError:
                return 0
    return 0


def source_page_count(src):
    fallback = int(src.get("pages") or 0)
    pdf = pathlib.Path(src["path"])
    if pdf.is_file():
        found = pdfinfo_pages(pdf)
        if found:
            return found
    return fallback


def verify_source(src):
    pdf = pathlib.Path(src["path"])
    if not pdf.is_absolute():
        return "path is not absolute"
    if not pdf.is_file():
        return "missing file: %s" % pdf
    wanted = (src.get("sha256") or "").strip().lower()
    if wanted:
        found = sha256_file(pdf).lower()
        if found != wanted:
            return "sha256 mismatch: wanted %s got %s" % (wanted, found)
    return None


def render_page(pdf, page, dpi, png_path):
    png_path.parent.mkdir(parents=True, exist_ok=True)
    prefix = png_path.with_suffix("")
    for stale in prefix.parent.glob(prefix.name + "-*.png"):
        try:
            stale.unlink()
        except OSError:
            pass
    cmd = [
        "pdftoppm",
        "-r", str(dpi),
        "-png",
        "-f", str(page),
        "-l", str(page),
        str(pdf),
        str(prefix),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=RENDER_TIMEOUT_S)
    produced = sorted(prefix.parent.glob(prefix.name + "-*.png"))
    if produced:
        os.replace(produced[0], png_path)
        for extra in produced[1:]:
            try:
                extra.unlink()
            except OSError:
                pass
    if not png_path.is_file():
        note = (proc.stderr or proc.stdout or "").strip()
        raise RuntimeError("pdftoppm failed for page %d: %s" % (page, note or "no output"))


def call_vision(png_path, prompt, model, max_tokens):
    env = os.environ.copy()
    env["VISION_MAX_TOKENS"] = str(max_tokens)
    cmd = [str(VISION), "--model", model, str(png_path), prompt]
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        env=env,
        timeout=VISION_TIMEOUT_S,
    )
    return proc.returncode, proc.stdout, proc.stderr


def _read_status(returncode, err):
    """Status for a non-empty read: truncated beats exit code beats ok."""
    if TRUNCATED_MARKER in err:
        return "truncated"
    if returncode != 0:
        return "exit_%d" % returncode
    return "ok"


def transcribe(png_path, prompt, model, base_tokens):
    text = ""
    status = "empty"
    note = ""
    tokens = base_tokens
    trunc_retried = False
    attempts = 0
    index = 0
    while index < MAX_ATTEMPTS:
        index += 1
        attempts = index
        try:
            returncode, out, err = call_vision(png_path, prompt, model, tokens)
            out = (out or "").strip()
            err = (err or "").strip()
        except Exception as exc:
            returncode, out, err = -1, "", "exception: %s" % exc

        if out:
            if TRUNCATED_MARKER in err and not trunc_retried:
                trunc_retried = True
                first_text = out
                first_note = err
                try:
                    _, out2, err2 = call_vision(png_path, prompt, model, tokens * 2)
                    out2 = (out2 or "").strip()
                    err2 = (err2 or "").strip()
                except Exception as exc:
                    out2, err2 = "", "exception: %s" % exc
                if len(out2) > len(first_text):
                    text = out2
                    status = _read_status(returncode, err2)
                    note = err2
                else:
                    text = first_text
                    status = "truncated"
                    note = first_note
                break
            text = out
            status = _read_status(returncode, err)
            note = err
            break

        if index >= MAX_ATTEMPTS:
            text = ""
            status = "error" if returncode != 0 else "empty"
            note = err
            break
        time.sleep(BACKOFF_S[index - 1])
    return text, status, attempts, note


def is_banned(text):
    return any(marker in text for marker in BANNED_MARKERS)


def has_dash(text):
    return "\u2014" in text or "\u2013" in text


def append_manifest(record):
    with _MANIFEST_LOCK:
        with open(MANIFEST, "a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
            handle.flush()
            os.fsync(handle.fileno())


def make_record(label, page, status, attempts, latency_s, chars, note, model, banned, png_path):
    png_sha = ""
    if png_path is not None and png_path.is_file():
        png_sha = sha256_file(png_path)
    return {
        "label": label,
        "page": page,
        "png_sha256": png_sha,
        "status": status,
        "attempts": attempts,
        "latency_s": round(latency_s, 3),
        "chars": chars,
        "stderr_note": note,
        "model": model,
        "banned_url": bool(banned),
        "ts": utc_now(),
    }


def is_done(md_path, record=None):
    """Done means non-empty markdown AND the latest manifest record says ok."""
    if not (md_path.is_file() and md_path.stat().st_size > 0):
        return False
    if record is None:
        return False
    return record.get("status") == "ok"


def page_done(label, page, latest, md_root):
    return is_done(md_root / label / (page_filename(page) + ".md"), latest.get((label, page)))


def process_page(label, page, pdf, dpi, prompt, model, max_tokens, force, latest=None):
    png_path = PAGEROOT / label / (page_filename(page) + ".png")
    md_path = OUT / label / (page_filename(page) + ".md")
    if latest is None:
        latest = read_manifest_latest()
    if not force and page_done(label, page, latest, OUT):
        return {"page": page, "ran": False, "done": True, "banned": False, "truncated": False}

    started = time.monotonic()
    try:
        if force or not png_path.is_file():
            render_page(pdf, page, dpi, png_path)
    except Exception as exc:
        latency = time.monotonic() - started
        record = make_record(label, page, "error", 0, latency, 0, "render: %s" % exc, model, False, png_path)
        append_manifest(record)
        log("%s p%03d: render error: %s" % (label, page, exc))
        return {"page": page, "ran": True, "done": False, "banned": False, "truncated": False}

    text, status, attempts, note = transcribe(png_path, prompt, model, max_tokens)
    latency = time.monotonic() - started
    banned = bool(text) and is_banned(text)
    if text:
        write_text_atomic(md_path, text + "\n")
    record = make_record(label, page, status, attempts, latency, len(text), note, model, banned, png_path)
    append_manifest(record)
    return {"page": page, "ran": True, "done": bool(text), "banned": banned, "truncated": status == "truncated"}


def read_manifest_latest():
    latest = {}
    if not MANIFEST.is_file():
        return latest
    for line in MANIFEST.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        key = (record.get("label"), record.get("page"))
        latest[key] = record
    return latest


def label_summary(label, total, latest):
    done = 0
    banned = 0
    dashes = 0
    truncated = 0
    for page in range(1, total + 1):
        if page_done(label, page, latest, OUT):
            done += 1
            md_path = OUT / label / (page_filename(page) + ".md")
            try:
                if has_dash(md_path.read_text(encoding="utf-8", errors="replace")):
                    dashes += 1
            except OSError:
                pass
        record = latest.get((label, page)) or {}
        if record.get("banned_url"):
            banned += 1
        if record.get("status") == "truncated":
            truncated += 1
    return {
        "pages": total,
        "done": done,
        "failed": total - done,
        "banned": banned,
        "dashes": dashes,
        "truncated": truncated,
    }


def print_table(rows):
    headers = ("label", "pages", "done", "failed", "banned", "dashes", "truncated")
    widths = [len(header) for header in headers]
    for row in rows:
        widths[0] = max(widths[0], len(row["label"]))
        for index, key in enumerate(headers[1:], start=1):
            widths[index] = max(widths[index], len(str(row[key])))
    header_line = "  ".join(header.ljust(widths[index]) for index, header in enumerate(headers))
    print(header_line)
    for row in rows:
        cells = [row["label"].ljust(widths[0])]
        for index, key in enumerate(headers[1:], start=1):
            cells.append(str(row[key]).rjust(widths[index]))
        print("  ".join(cells))


def write_summary(rows, wall_s):
    lines = ["# Conversion summary", "", "Wall time: %.1fs" % wall_s, ""]
    lines.append("| label | pages | done | failed | banned | dashes | truncated |")
    lines.append("|---|---|---|---|---|---|---|")
    for row in rows:
        lines.append(
            "| %s | %d | %d | %d | %d | %d | %d |"
            % (
                row["label"],
                row["pages"],
                row["done"],
                row["failed"],
                row["banned"],
                row["dashes"],
                row["truncated"],
            )
        )
    lines.append("")
    write_text_atomic(WORK_ROOT / "SUMMARY.md", "\n".join(lines))


def parse_args(argv):
    parser = argparse.ArgumentParser(description="PDF slide to markdown conversion pipeline.")
    parser.add_argument("--label", action="append", default=None, help="label to process, repeatable")
    parser.add_argument("--limit", type=int, default=None, help="first N pages per label")
    parser.add_argument("--force", action="store_true", help="redo pages even if markdown exists")
    parser.add_argument("--workers", type=int, default=None, help="parallel workers")
    parser.add_argument("--dpi", type=int, default=None, help="render resolution")
    parser.add_argument("--dry-run", action="store_true", help="list pending pages and exit")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="vision model id")
    return parser.parse_args(argv)


def selected_pages(total, limit):
    pages = list(range(1, total + 1))
    if limit is not None and limit >= 0:
        pages = pages[:limit]
    return pages


class convert_test_harness:
    """Test hook: tests set _root to redirect every repo write."""

    _root = None


def main(argv):
    global WORK_ROOT, MANIFEST, PAGEROOT, OUT

    args = parse_args(argv)
    config, sources = load_config()

    WORK_ROOT = ROOT / "work"
    MANIFEST = WORK_ROOT / "manifest.jsonl"
    PAGEROOT = ROOT / config["page_dir"]
    OUT = ROOT / config["out_dir"]
    if convert_test_harness._root is not None:
        base = convert_test_harness._root
        WORK_ROOT = base / "work"
        MANIFEST = WORK_ROOT / "manifest.jsonl"
        PAGEROOT = base / config["page_dir"]
        OUT = base / config["out_dir"]

    dpi = args.dpi if args.dpi is not None else config["dpi"]
    workers = args.workers if args.workers is not None else config["workers"]
    if workers < 1:
        workers = 1

    wanted = args.label
    if wanted:
        known = {src.get("label") for src in sources}
        unknown = [label for label in wanted if label not in known]
        if unknown:
            log("unknown label(s): %s" % ", ".join(unknown))
            return 2
        sources = [src for src in sources if src.get("label") in set(wanted)]

    prompt_path = ROOT / "PROMPT.txt"
    if not prompt_path.is_file():
        log("missing prompt file: %s" % prompt_path)
        return 2
    prompt = prompt_path.read_text(encoding="utf-8").strip()

    if not args.dry_run:
        PAGEROOT.mkdir(parents=True, exist_ok=True)
        OUT.mkdir(parents=True, exist_ok=True)
        WORK_ROOT.mkdir(parents=True, exist_ok=True)

    runnable = []
    skipped = []
    for src in sources:
        reason = verify_source(src)
        if reason is not None:
            log("%s: SKIPPED, %s" % (src.get("label"), reason))
            skipped.append((src.get("label"), reason))
            continue
        runnable.append(src)

    # One manifest read per run, shared by the dry-run branch, the processing
    # loop, and process_page. The re-read after the loop (below) picks up
    # records this run appended, for the per-label summary.
    latest = read_manifest_latest()

    if args.dry_run:
        if skipped:
            for label, reason in skipped:
                print("%s: SKIPPED, %s" % (label, reason))
            print("dry run: %d skipped source(s)" % len(skipped))
            return 1
        total_pending = 0
        for src in runnable:
            label = src["label"]
            total = source_page_count(src)
            pages = selected_pages(total, args.limit)
            pending = [p for p in pages if not page_done(label, p, latest, OUT)]
            total_pending += len(pending)
            done = len(pages) - len(pending)
            if pending:
                names = " ".join(page_filename(p) for p in pending)
                print("%s: %d pages, %d done, %d pending: %s" % (label, len(pages), done, len(pending), names))
            else:
                print("%s: %d pages, %d done, 0 pending" % (label, len(pages), done))
        print("dry run: %d pending page(s)" % total_pending)
        return 0

    started_wall = time.monotonic()
    rows = []
    for src in runnable:
        label = src["label"]
        total = source_page_count(src)
        pages = selected_pages(total, args.limit)
        pending = [
            page
            for page in pages
            if args.force or not page_done(label, page, latest, OUT)
        ]
        if pending:
            pdf = pathlib.Path(src["path"])
            with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
                futures = {
                    executor.submit(
                        process_page,
                        label,
                        page,
                        pdf,
                        dpi,
                        prompt,
                        args.model,
                        config["max_tokens"],
                        args.force,
                        latest,
                    ): page
                    for page in pending
                }
                for future in concurrent.futures.as_completed(futures):
                    page = futures[future]
                    try:
                        future.result()
                    except Exception as exc:
                        log("%s p%03d: unexpected error: %s" % (label, page, exc))
                        record = make_record(
                            label, page, "error", 0, 0.0, 0, str(exc), args.model, False, None
                        )
                        append_manifest(record)

        latest = read_manifest_latest()  # re-read: sees rows this run wrote
        stats = label_summary(label, len(pages), latest)
        rows.append(dict(label=label, **stats))
        print(
            "%s: %d pages, %d done, %d failed, %d banned, %d truncated"
            % (label, stats["pages"], stats["done"], stats["failed"], stats["banned"], stats["truncated"])
        )

    wall_s = time.monotonic() - started_wall
    print("")
    print_table(rows)
    print("wall time: %.1fs" % wall_s)
    write_summary(rows, wall_s)
    if skipped:
        for label, reason in skipped:
            print("%s: SKIPPED, %s" % (label, reason))
        print("%d skipped source(s)" % len(skipped))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
