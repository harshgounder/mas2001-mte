#!/usr/bin/env python3
"""Inventory every fenced block in the 27 original deck Markdown files."""

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent / "source-notes" / "fenced-block-inventory.csv"
STRUCTURAL_MARKERS = set("│├└┌┐┘┬┴┼─▶◀█║╔╗╚╝═╠╣╦╩╬")


def source_files():
    return sorted(ROOT.glob("*.md")) + sorted((ROOT / "notes").glob("*.md"))


def blocks(path):
    inside = False
    start = None
    content = []
    index = 0
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("```"):
            if not inside:
                inside = True
                start = line_number
                content = []
            else:
                index += 1
                joined = "\n".join(content)
                markers = "".join(sorted(set(joined) & STRUCTURAL_MARKERS))
                classification = "structural-candidate" if markers else "text-or-formula"
                yield index, start, line_number, classification, markers
                inside = False
        elif inside:
            content.append(line)
    if inside:
        raise ValueError(f"unclosed fence in {path}")


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for path in source_files():
        source = path.relative_to(ROOT.parent).as_posix()
        for index, start, end, classification, markers in blocks(path):
            rows.append(
                {
                    "source_file": source,
                    "block_index": index,
                    "start_line": start,
                    "end_line": end,
                    "classification": classification,
                    "structural_markers": markers,
                }
            )
    with OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    candidates = sum(row["classification"] == "structural-candidate" for row in rows)
    print(f"wrote {len(rows)} blocks, including {candidates} structural candidates, to {OUT}")


if __name__ == "__main__":
    main()
