#!/usr/bin/env python3
"""Audit the PDF to markdown conversion and run a fidelity gate.

Two modes:

* default: coverage audit. For every page of every source, compare the page
  markdown against the page PDF text layer and bucket the page.
* --fidelity N: pick N converted pages across labels, transcribe them again
  with a second vision model, and compare the two readings.

Standard library only. See BRIEF-003-audit-and-fidelity.md.
"""

import argparse
import json
import os
import pathlib
import random
import re
import subprocess
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
VISION = pathlib.Path.home() / ".local" / "bin" / "vision"

MD_ROOT = ROOT / "md"
WORK_ROOT = ROOT / "work"
AUDIT_JSONL = WORK_ROOT / "audit.jsonl"
AUDIT_MD = WORK_ROOT / "AUDIT.md"
FIDELITY_ROOT = WORK_ROOT / "fidelity"
FIDELITY_MD = WORK_ROOT / "FIDELITY.md"

DEFAULT_FIDELITY_MODEL = "xiaomi/mimo-v2.5-pro"
DEFAULT_SEED = 20260913

BANNED_MARKERS = ("example.com", "](http", "https://")
DASHES = ("\u2014", "\u2013")
GREEK_RE = re.compile("[\u0370-\u03ff\u1f00-\u1fff]")
PAGE_RE = re.compile(r"^p(\d+)\.md$")
NUM_RE = re.compile(r"\d[\d,]*(?:\.\d+)?")

VISION_TIMEOUT_S = 900
PDFTOTEXT_TIMEOUT_S = 120


def log(message):
    print(message, file=sys.stderr, flush=True)


def page_name(page):
    return "p%03d" % page


def write_text_atomic(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "w", encoding="utf-8") as handle:
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(tmp, path)


def read_text(path):
    if not path.is_file():
        return ""
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


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
        "page_dir": scalars.get("page_dir") or "work/pages",
        "out_dir": scalars.get("out_dir") or "md",
    }
    return config, sources


def page_numbers_for_source(src, present):
    """Expected pages from the manifest unioned with pages found in md."""
    try:
        expected = int(src.get("pages") or 0)
    except (TypeError, ValueError):
        expected = 0
    numbers = set(range(1, expected + 1))
    numbers.update(present)
    return sorted(numbers)


def collect_converted(md_root):
    """Map label to sorted page numbers that have a per page markdown file."""
    converted = {}
    if not md_root.is_dir():
        return converted
    for label_dir in sorted(md_root.iterdir()):
        if not label_dir.is_dir():
            continue
        pages = []
        for path in label_dir.glob("p*.md"):
            match = PAGE_RE.match(path.name)
            if match:
                pages.append(int(match.group(1)))
        if pages:
            converted[label_dir.name] = sorted(set(pages))
    return converted


def pdf_text_layer(pdf, page):
    """Extract one page with pdftotext -layout. Returns text, never raises."""
    cmd = [
        "pdftotext",
        "-layout",
        "-f", str(page),
        "-l", str(page),
        str(pdf),
        "-",
    ]
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            timeout=PDFTOTEXT_TIMEOUT_S,
        )
    except Exception as exc:
        log("pdftotext failed for page %d: %s" % (page, exc))
        return ""
    if proc.returncode != 0:
        return ""
    return proc.stdout.decode("utf-8", "replace")


def count_figure_lines(text):
    return sum(1 for line in text.splitlines() if line.startswith("Figure:"))


def bucket_for(record):
    if record["empty"]:
        return "EMPTY"
    ratio = record["ratio"]
    if record["textlayer_chars"] > 250 and ratio is not None and ratio < 0.5:
        return "MISSING_TEXT"
    text_layer = record["_textlayer"]
    has_math = ("=" in text_layer) or bool(GREEK_RE.search(text_layer))
    if has_math and record["latex_inline"] == 0:
        return "NO_MATH"
    if record["banned_url"]:
        return "BANNED_URL"
    if record["dashes"]:
        return "DASH"
    return "OK"


def audit_page(label, page, pdf_path):
    md_path = MD_ROOT / label / (page_name(page) + ".md")
    md = read_text(md_path)
    if md_path.is_file():
        empty = md_path.stat().st_size == 0
    else:
        empty = True
    md_chars = len(md)

    text_layer = ""
    if pdf_path.is_file():
        text_layer = pdf_text_layer(pdf_path, page)
    textlayer_chars = len(text_layer)

    if textlayer_chars > 0:
        ratio = round(md_chars / textlayer_chars, 4)
    else:
        ratio = None

    banned_url = any(marker in md for marker in BANNED_MARKERS)
    dashes = any(dash in md for dash in DASHES)

    record = {
        "label": label,
        "page": page,
        "md_chars": md_chars,
        "textlayer_chars": textlayer_chars,
        "ratio": ratio,
        "latex_inline": md.count("$"),
        "display_math": md.count("$$"),
        "figure_lines": count_figure_lines(md),
        "banned_url": bool(banned_url),
        "dashes": bool(dashes),
        "empty": bool(empty),
        "_textlayer": text_layer,
    }
    record["bucket"] = bucket_for(record)
    return record


def run_audit():
    config, sources = load_config()
    converted = collect_converted(MD_ROOT)
    records = []
    for src in sources:
        label = src.get("label") or ""
        pdf_path = pathlib.Path(src.get("path") or "")
        present = converted.get(label, [])
        for page in page_numbers_for_source(src, present):
            try:
                record = audit_page(label, page, pdf_path)
            except Exception as exc:
                log("%s p%03d: audit error: %s" % (label, page, exc))
                record = {
                    "label": label,
                    "page": page,
                    "md_chars": 0,
                    "textlayer_chars": 0,
                    "ratio": None,
                    "latex_inline": 0,
                    "display_math": 0,
                    "figure_lines": 0,
                    "banned_url": False,
                    "dashes": False,
                    "empty": True,
                    "_textlayer": "",
                }
                record["bucket"] = "EMPTY"
            records.append(record)

    lines = []
    for record in records:
        payload = {key: value for key, value in record.items() if key != "_textlayer"}
        lines.append(json.dumps(payload, ensure_ascii=False))
    write_text_atomic(AUDIT_JSONL, "\n".join(lines) + ("\n" if lines else ""))

    write_audit_markdown(records)

    total = len(records)
    empty = sum(1 for record in records if record["bucket"] == "EMPTY")
    flagged = sum(1 for record in records if record["bucket"] != "OK")
    print("audit: %d pages, %d flagged, %d empty" % (total, flagged, empty))
    return 0 if empty == 0 else 1


def bucket_totals(records):
    keys = ("OK", "EMPTY", "MISSING_TEXT", "NO_MATH", "BANNED_URL", "DASH")
    totals = {key: 0 for key in keys}
    for record in records:
        totals[record["bucket"]] = totals.get(record["bucket"], 0) + 1
    return totals


def write_audit_markdown(records):
    labels = []
    grouped = {}
    for record in records:
        label = record["label"]
        if label not in grouped:
            grouped[label] = []
            labels.append(label)
        grouped[label].append(record)

    total = len(records)
    flagged = sum(1 for record in records if record["bucket"] != "OK")
    percent = (flagged * 100.0 / total) if total else 0.0

    keys = ("OK", "EMPTY", "MISSING_TEXT", "NO_MATH", "BANNED_URL", "DASH")
    out = []
    out.append("# Conversion coverage audit")
    out.append("")
    out.append(
        "Headline: total pages %d, flagged %d, percentage flagged %.2f."
        % (total, flagged, percent)
    )
    out.append("")
    out.append("## Per label")
    out.append("")
    out.append("| label | pages | " + " | ".join(keys) + " |")
    out.append("|---|" + "---|" * (len(keys) + 1))
    for label in labels:
        group = grouped[label]
        totals = bucket_totals(group)
        cells = " | ".join(str(totals[key]) for key in keys)
        out.append("| %s | %d | %s |" % (label, len(group), cells))
    out.append("")
    out.append("## Non OK pages")
    out.append("")
    out.append("| label | page | bucket | md_chars | textlayer_chars |")
    out.append("|---|---|---|---|---|")
    any_flagged = False
    for record in records:
        if record["bucket"] == "OK":
            continue
        any_flagged = True
        out.append(
            "| %s | %d | %s | %d | %d |"
            % (
                record["label"],
                record["page"],
                record["bucket"],
                record["md_chars"],
                record["textlayer_chars"],
            )
        )
    if not any_flagged:
        out.append("| (none) | | | | |")
    out.append("")
    write_text_atomic(AUDIT_MD, "\n".join(out))


def numeric_tokens(text):
    tokens = []
    for match in NUM_RE.finditer(text):
        tokens.append(match.group(0).replace(",", ""))
    return tokens


def numeric_agreement(primary, second):
    primary_counts = Counter(numeric_tokens(primary))
    second_counts = Counter(numeric_tokens(second))
    total = sum(primary_counts.values())
    if total == 0:
        return 1.0
    matched = 0
    for token, count in primary_counts.items():
        matched += min(count, second_counts.get(token, 0))
    return matched / total


def choose_pages(converted, count, seed):
    if count <= 0:
        return []
    labels = sorted(converted)
    rng = random.Random(seed)
    rng.shuffle(labels)
    pools = {}
    for label in labels:
        pages = list(converted[label])
        rng.shuffle(pages)
        pools[label] = pages
    chosen = []
    index = 0
    while len(chosen) < count:
        added = False
        for label in labels:
            if index < len(pools[label]):
                chosen.append((label, pools[label][index]))
                added = True
                if len(chosen) >= count:
                    break
        if not added:
            break
        index += 1
    return chosen


def call_vision(png_path, prompt, model, max_tokens):
    if not png_path.is_file():
        log("missing png: %s" % png_path)
        return ""
    env = os.environ.copy()
    env["VISION_MAX_TOKENS"] = str(max_tokens)
    cmd = [str(VISION), "--model", model, str(png_path), prompt]
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            env=env,
            timeout=VISION_TIMEOUT_S,
        )
    except Exception as exc:
        log("vision failed for %s: %s" % (png_path, exc))
        return ""
    if proc.returncode != 0:
        note = (proc.stderr or "").strip().replace("\n", " ")[:200]
        log("vision exit %d for %s: %s" % (proc.returncode, png_path, note))
    return (proc.stdout or "").strip()


def run_fidelity(args):
    config, _sources = load_config()
    pages_root = ROOT / config["page_dir"]
    prompt_path = ROOT / "PROMPT.txt"
    prompt = prompt_path.read_text(encoding="utf-8").strip()
    converted = collect_converted(MD_ROOT)
    chosen = choose_pages(converted, args.fidelity, args.seed)

    rows = []
    for label, page in chosen:
        primary_path = MD_ROOT / label / (page_name(page) + ".md")
        second_path = FIDELITY_ROOT / label / (page_name(page) + ".md")
        primary = read_text(primary_path)
        if second_path.is_file():
            second = read_text(second_path)
        else:
            png_path = pages_root / label / (page_name(page) + ".png")
            second = call_vision(png_path, prompt, args.fidelity_model, config["max_tokens"])
            if second:
                write_text_atomic(second_path, second + "\n")

        agreement = numeric_agreement(primary, second)
        primary_figures = count_figure_lines(primary)
        second_figures = count_figure_lines(second)
        second_title = any(line.startswith("## ") for line in second.splitlines())
        verdict = "PASS" if agreement >= 0.8 else "REVIEW"
        rows.append(
            {
                "label": label,
                "page": page,
                "agreement": agreement,
                "primary_figures": primary_figures,
                "second_figures": second_figures,
                "second_title": second_title,
                "verdict": verdict,
            }
        )
        print(
            "fidelity %s p%03d: agreement %.3f, figures %d/%d, title %s, %s"
            % (
                label,
                page,
                agreement,
                primary_figures,
                second_figures,
                "yes" if second_title else "no",
                verdict,
            )
        )

    write_fidelity_markdown(rows)
    return 0


def write_fidelity_markdown(rows):
    out = []
    out.append("# Fidelity gate")
    out.append("")
    out.append("| label | page | numeric agreement | figures primary | figures second | second title | verdict |")
    out.append("|---|---|---|---|---|---|---|")
    for row in rows:
        out.append(
            "| %s | %d | %.3f | %d | %d | %s | %s |"
            % (
                row["label"],
                row["page"],
                row["agreement"],
                row["primary_figures"],
                row["second_figures"],
                "yes" if row["second_title"] else "no",
                row["verdict"],
            )
        )
    out.append("")
    write_text_atomic(FIDELITY_MD, "\n".join(out))


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="Audit the PDF to markdown conversion and run a fidelity gate."
    )
    parser.add_argument(
        "--fidelity",
        type=int,
        default=None,
        metavar="N",
        help="run the fidelity gate on N converted pages instead of the coverage audit",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=DEFAULT_SEED,
        help="random seed for fidelity page selection (default %d)" % DEFAULT_SEED,
    )
    parser.add_argument(
        "--fidelity-model",
        default=DEFAULT_FIDELITY_MODEL,
        help="second reader model (default %s)" % DEFAULT_FIDELITY_MODEL,
    )
    return parser.parse_args(argv)


def main(argv):
    args = parse_args(argv)
    if args.fidelity is not None:
        return run_fidelity(args)
    return run_audit()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
