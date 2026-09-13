#!/usr/bin/env python3
"""Assemble per-page markdown into one document per label plus an index.

Takes md/<label>/p*.md in page order and emits md/<label>.md and md/INDEX.json.
Idempotent: unchanged input produces byte-identical output.
"""

import json
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "md"
MANIFEST = ROOT / "work" / "manifest.jsonl"
BANNED_MARKERS = ("example.com", "](http", "https://")
DASHES = ("\u2014", "\u2013")
PAGE_RE = re.compile(r"^p(\d+)\.md$")


def fix_dashes(text):
    count = 0
    for dash in DASHES:
        count += text.count(dash)
        text = text.replace(dash, "-")
    return text, count


def write_text_atomic(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "w", encoding="utf-8") as handle:
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(tmp, path)


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
        latest[(record.get("label"), record.get("page"))] = record
    return latest


def page_files(label_dir):
    found = []
    for path in label_dir.glob("p*.md"):
        match = PAGE_RE.match(path.name)
        if match:
            found.append((int(match.group(1)), path))
    found.sort(key=lambda item: item[0])
    return found


def assemble_label(label, latest):
    label_dir = OUT / label
    bodies = []
    pages = 0
    done = 0
    chars = 0
    dashes_fixed = 0
    flagged = set()
    for number, path in page_files(label_dir):
        pages += 1
        raw = path.read_text(encoding="utf-8", errors="replace")
        body = raw.strip()
        body, fixed = fix_dashes(body)
        dashes_fixed += fixed
        if body:
            done += 1
            chars += len(body)
            bodies.append(body)
        if any(marker in raw for marker in BANNED_MARKERS):
            flagged.add(number)
        record = latest.get((label, number)) or {}
        if record.get("status") == "truncated":
            flagged.add(number)

    if bodies:
        document = "# %s\n\n%s\n" % (label, "\n\n---\n\n".join(bodies))
    else:
        document = "# %s\n" % label
    write_text_atomic(OUT / (label + ".md"), document)
    return {"pages": pages, "chars": chars, "done": done, "flagged": len(flagged), "dashes_fixed": dashes_fixed}


def main(argv):
    labels = sorted(path.name for path in OUT.iterdir() if path.is_dir()) if OUT.is_dir() else []
    latest = read_manifest_latest()
    index = {}
    for label in labels:
        index[label] = assemble_label(label, latest)
        stats = index[label]
        print(
            "%s: %d pages, %d done, %d chars, %d flagged, %d dashes fixed"
            % (label, stats["pages"], stats["done"], stats["chars"], stats["flagged"], stats["dashes_fixed"])
        )
    write_text_atomic(OUT / "INDEX.json", json.dumps(index, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
