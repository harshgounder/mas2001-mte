#!/usr/bin/env python3
"""Build the deterministic gross question-instance ledger (383 exact instances).

This ledger enumerates every question instance the corpus accounting report counts,
without deduplicating content families. It is a GROSS ledger: the same underlying
problem may appear in more than one row, exactly as reports/18-CORPUS-ACCOUNTING.md
counts it. The total is fixed at 383 across seven groups:

    teaching          60
    chebyshev          3
    assignments-2025  52
    mte               16
    ete               97
    assignments-2024 125
    four-decks        30
    total            383

Structured data is reused where it is reliable:

  * 97 ETE rows parsed from reports/17-ETE-INTAKE.md tables (scope carried, provenance
    deliberately left unsearched).
  * 16 MTE rows parsed from the block-by-block table in reports/16-SOURCE-PROVENANCE.md
    (provenance verdict and source text carried verbatim, never upgraded).
  * 30 four-decks rows parsed from reports/evidence/deck-block-ledger-20260916.csv
    (ledger fields and provenance carried).
  * 30 teaching Deck 01 items parsed from the numbered manifest in
    reports/11-QUESTION-ATLAS/00-COUNT-REGISTER.md when present.

Everything that has no reliable row description is seeded as an ordered placeholder:
the remaining teaching sources (ppt3 6, ppt4 7, lms-standard-error-clt 5, ppt5 5,
lms-theory 7), Chebyshev Q1 to Q3, the 52 assignment-2025-26 instances, and the six
2024-25 assignment labels with Q1..Qn counts 15, 20, 25, 25, 16, 24. Every seeded
placeholder carries description_state=pending and an empty summary. Placeholders are
never marked resolved and are not claimed to be fully described.

description_state is one of:
    resolved   a reliable row summary exists in a structured source
    pending    a seeded placeholder; no reliable row description exists

status is "gross" for every row: this ledger does not resolve content families. The
content_family_id column is intentionally left blank until a separate content-family
pass assigns families with evidence.

Usage:
    python3 scripts/build_question_instance_ledger.py [--output PATH]
    python3 scripts/build_question_instance_ledger.py --check [--output PATH]

--check rebuilds the ledger in memory and exits nonzero on a wrong header, a wrong
row count, duplicate or missing ids, an ordering change, or stale generated content.
Standard library only.
"""

import argparse
import csv
import io
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

ETE_REL = pathlib.Path("reports") / "17-ETE-INTAKE.md"
MTE_REL = pathlib.Path("reports") / "16-SOURCE-PROVENANCE.md"
DECK_REL = pathlib.Path("reports") / "evidence" / "deck-block-ledger-20260916.csv"
REGISTER_REL = pathlib.Path("reports") / "11-QUESTION-ATLAS" / "00-COUNT-REGISTER.md"
LEDGER_REL = pathlib.Path("reports") / "evidence" / "question-instance-ledger.csv"

FIELDS = [
    "instance_id",
    "corpus_group",
    "source_label",
    "block_order",
    "page_start",
    "page_end",
    "summary",
    "scope",
    "description_state",
    "provenance_verdict",
    "provenance_source",
    "evidence_locator",
    "content_family_id",
    "status",
]

GROUP_ORDER = [
    "teaching",
    "chebyshev",
    "assignments-2025",
    "mte",
    "ete",
    "assignments-2024",
    "four-decks",
]

GROUP_TOTALS = {
    "teaching": 60,
    "chebyshev": 3,
    "assignments-2025": 52,
    "mte": 16,
    "ete": 97,
    "assignments-2024": 125,
    "four-decks": 30,
}
TOTAL_INSTANCES = 383

SOURCE_ORDER = {
    "teaching": [
        "notes-lecture-series-01-09",
        "ppt3-discrete-prob-dist",
        "ppt4-continuous-prob-dist",
        "lms-standard-error-clt",
        "ppt5-estimation-summary",
        "lms-theory-of-estimation",
    ],
    "chebyshev": ["L10-11-chebyshev-deck"],
    "assignments-2025": ["assignment-2025-26-1", "assignment-2025-26-2"],
    "mte": ["paper-mte-2024-25", "paper-mte-2025-26"],
    "ete": ["E24S3", "E25S3", "E24S4", "E25S4", "E25SUM", "R25S3", "R25S4"],
    "assignments-2024": [
        "assignment-2024-25-1",
        "assignment-2024-25-2",
        "assignment-2024-25-3",
        "assignment-2024-25-3-ep2",
        "assignment-2024-25-4",
        "assignment-2024-25-5",
    ],
    "four-decks": [
        "sp-l1-7",
        "sp-l8-9",
        "sp-l12-13-discrete",
        "sp-l14-15-continuous",
    ],
}

DESCRIPTION_PENDING = "pending"
DESCRIPTION_RESOLVED = "resolved"
STATUS_GROSS = "gross"
PROVENANCE_UNSEARCHED = "unsearched"

ASSIGNMENT_2025_MANIFEST = [
    ("assignment-2025-26-1", [("MCQ", 10), ("SHORT", 6), ("LONG", 4), ("APP", 4)]),
    ("assignment-2025-26-2", [("A", 12), ("B", 8), ("C", 4), ("D", 4)]),
]

ASSIGNMENT_2024_COUNTS = [
    ("assignment-2024-25-1", 15),
    ("assignment-2024-25-2", 20),
    ("assignment-2024-25-3", 25),
    ("assignment-2024-25-3-ep2", 25),
    ("assignment-2024-25-4", 16),
    ("assignment-2024-25-5", 24),
]

TEACHING_PLACEHOLDERS = [
    ("ppt3-discrete-prob-dist", "teach-ppt3", 6),
    ("ppt4-continuous-prob-dist", "teach-ppt4", 7),
    ("lms-standard-error-clt", "teach-lms-se-clt", 5),
    ("ppt5-estimation-summary", "teach-ppt5", 5),
    ("lms-theory-of-estimation", "teach-lms-theory", 7),
]

ETE_ID_RE = re.compile(r"^[ER]\d{2}[A-Z0-9]*-[A-Z0-9]+$")
MTE_ID_RE = re.compile(r"^M\d{2}-[A-Z]\d+$")

MTE_SOURCE_LABELS = {
    "24": "paper-mte-2024-25",
    "25": "paper-mte-2025-26",
}

COUNT_REGISTER_LOCATOR = "reports/11-QUESTION-ATLAS/00-COUNT-REGISTER.md"
ETE_LOCATOR = "reports/17-ETE-INTAKE.md"
MTE_LOCATOR = "reports/16-SOURCE-PROVENANCE.md#mte-block-by-block-provenance"
DECK_LEDGER_LOCATOR = "reports/evidence/deck-block-ledger-20260916.csv"
ACCOUNTING_LOCATOR = "reports/18-CORPUS-ACCOUNTING.md"


def log(message):
    print(message, file=sys.stderr, flush=True)


def read_text(path):
    return pathlib.Path(path).read_text(encoding="utf-8")


def split_pipe_row(line):
    """Return stripped cells for a markdown pipe row, or None when not a row."""
    stripped = line.strip()
    if not stripped.startswith("|"):
        return None
    return [cell.strip() for cell in stripped.strip("|").split("|")]


def make_row(
    instance_id,
    corpus_group,
    source_label,
    block_order,
    page_start="",
    page_end="",
    summary="",
    scope="",
    description_state=DESCRIPTION_PENDING,
    provenance_verdict=PROVENANCE_UNSEARCHED,
    provenance_source="",
    evidence_locator="",
    content_family_id="",
):
    return {
        "instance_id": instance_id,
        "corpus_group": corpus_group,
        "source_label": source_label,
        "block_order": block_order,
        "page_start": page_start,
        "page_end": page_end,
        "summary": summary,
        "scope": scope,
        "description_state": description_state,
        "provenance_verdict": provenance_verdict,
        "provenance_source": provenance_source,
        "evidence_locator": evidence_locator,
        "content_family_id": content_family_id,
        "status": STATUS_GROSS,
    }


def parse_ete_rows(text):
    """Parse the 97 ETE / summer / re-sess block rows from report 17.

    Each row keeps its own id, its block text as summary, and its verdict as scope.
    Provenance is not searched here and is set to unsearched by the builder.
    """
    rows = []
    order_by_source = {}
    for line in text.splitlines():
        cells = split_pipe_row(line)
        if not cells or len(cells) < 3:
            continue
        block_id = cells[0]
        if not ETE_ID_RE.match(block_id):
            continue
        source_label = block_id.split("-", 1)[0]
        order_by_source[source_label] = order_by_source.get(source_label, 0) + 1
        rows.append(
            {
                "instance_id": "ete-" + block_id,
                "source_label": source_label,
                "block_order": order_by_source[source_label],
                "summary": "|".join(cells[1:-1]).strip(),
                "scope": cells[-1],
                "evidence_locator": ETE_LOCATOR,
            }
        )
    return rows


def parse_mte_rows(text):
    """Parse the 16 MTE block rows from the report 16 block-by-block table.

    Verdict and origin/evidence are carried verbatim. The builder never rewrites
    them into a stronger claim.
    """
    rows = []
    order_by_source = {}
    for line in text.splitlines():
        cells = split_pipe_row(line)
        if not cells or len(cells) < 4:
            continue
        block_id = cells[0]
        if not MTE_ID_RE.match(block_id):
            continue
        source_label = MTE_SOURCE_LABELS.get(
            block_id[1:3], "paper-mte-20" + block_id[1:3]
        )
        order_by_source[source_label] = order_by_source.get(source_label, 0) + 1
        rows.append(
            {
                "instance_id": "mte-" + block_id,
                "source_label": source_label,
                "block_order": order_by_source[source_label],
                "summary": "|".join(cells[1:-2]).strip(),
                "scope": "in-scope",
                "provenance_verdict": cells[-2],
                "provenance_source": cells[-1],
                "evidence_locator": MTE_LOCATOR,
            }
        )
    return rows


def parse_deck_rows(csv_text):
    """Parse the 30 four-decks ledger rows, carrying all fields and provenance."""
    rows = []
    order_by_source = {}
    reader = csv.DictReader(io.StringIO(csv_text, newline=""))
    for record in reader:
        block_id = (record.get("block_id") or "").strip()
        if not block_id:
            continue
        source_label = (record.get("label") or "").strip()
        order_by_source[source_label] = order_by_source.get(source_label, 0) + 1
        rows.append(
            {
                "instance_id": "deck-" + block_id,
                "source_label": source_label,
                "block_order": order_by_source[source_label],
                "page_start": (record.get("page_start") or "").strip(),
                "page_end": (record.get("page_end") or "").strip(),
                "summary": (record.get("summary") or "").strip(),
                "scope": (record.get("mte_scope") or "").strip(),
                "provenance_verdict": (record.get("provenance_status") or "").strip(),
                "provenance_source": (record.get("source_candidate") or "").strip(),
                "evidence_locator": (record.get("evidence") or "").strip(),
            }
        )
    return rows


def parse_deck01_manifest(text):
    """Parse the numbered 30-item Deck 01 manifest in the count register.

    Returns an empty list when the section or the 30 items are not present, so the
    caller can fall back to pending placeholders.
    """
    heading = "## Deck 01 manifest (30 items)"
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if line.strip() == heading:
            start = index + 1
            break
    if start is None:
        return []
    items = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        match = re.match(r"^\s*(\d+)\.\s+(.*)$", line)
        if not match:
            continue
        content = match.group(2).strip()
        page_match = re.match(r"^p(\d+)(?:\s*-\s*p?(\d+))?\b\s*(.*)$", content)
        if page_match:
            page_start = str(int(page_match.group(1)))
            page_end = str(int(page_match.group(2) or page_match.group(1)))
            detail = page_match.group(3).strip()
        else:
            page_start = ""
            page_end = ""
            detail = content
        items.append(
            {
                "block_order": len(items) + 1,
                "page_start": page_start,
                "page_end": page_end,
                "summary": detail,
            }
        )
    return items


def seed_teaching(time_manifest):
    """Build the 60 teaching rows: parsed Deck 01 items then ordered placeholders."""
    rows = []
    if len(time_manifest) == 30:
        for item in time_manifest:
            rows.append(
                make_row(
                    "teach-deck01-%02d" % item["block_order"],
                    "teaching",
                    "notes-lecture-series-01-09",
                    item["block_order"],
                    page_start=item["page_start"],
                    page_end=item["page_end"],
                    summary=item["summary"],
                    scope="in-scope",
                    description_state=DESCRIPTION_RESOLVED,
                    evidence_locator=COUNT_REGISTER_LOCATOR,
                )
            )
    else:
        for number in range(1, 31):
            rows.append(
                make_row(
                    "teach-deck01-%02d" % number,
                    "teaching",
                    "notes-lecture-series-01-09",
                    number,
                    scope="in-scope",
                    description_state=DESCRIPTION_PENDING,
                    evidence_locator=COUNT_REGISTER_LOCATOR,
                )
            )
    for source_label, id_stem, count in TEACHING_PLACEHOLDERS:
        for number in range(1, count + 1):
            rows.append(
                make_row(
                    "%s-%02d" % (id_stem, number),
                    "teaching",
                    source_label,
                    number,
                    scope="in-scope",
                    description_state=DESCRIPTION_PENDING,
                    evidence_locator=COUNT_REGISTER_LOCATOR,
                )
            )
    return rows


def seed_chebyshev():
    rows = []
    for number in range(1, 4):
        rows.append(
            make_row(
                "cheb-Q%d" % number,
                "chebyshev",
                "L10-11-chebyshev-deck",
                number,
                scope="in-scope",
                description_state=DESCRIPTION_PENDING,
                evidence_locator=ACCOUNTING_LOCATOR,
            )
        )
    return rows


def seed_assignment_2025():
    rows = []
    for source_label, sections in ASSIGNMENT_2025_MANIFEST:
        order = 0
        for section, count in sections:
            for number in range(1, count + 1):
                order += 1
                rows.append(
                    make_row(
                        "asn2025-%s-%s-%02d"
                        % (source_label.rsplit("-", 1)[-1], section, number),
                        "assignments-2025",
                        source_label,
                        order,
                        scope="in-scope",
                        description_state=DESCRIPTION_PENDING,
                        evidence_locator=COUNT_REGISTER_LOCATOR,
                    )
                )
    return rows


def seed_assignment_2024():
    rows = []
    for source_label, count in ASSIGNMENT_2024_COUNTS:
        suffix = source_label.rsplit("-", 1)[-1]
        for number in range(1, count + 1):
            rows.append(
                make_row(
                    "asn2024-%s-Q%02d" % (suffix, number),
                    "assignments-2024",
                    source_label,
                    number,
                    scope="pending",
                    description_state=DESCRIPTION_PENDING,
                    evidence_locator=ACCOUNTING_LOCATOR,
                )
            )
    return rows


def build_rows(ete_text, mte_text, deck_csv_text, register_text):
    """Assemble all 383 rows in the fixed group and source order."""
    rows = []
    rows.extend(seed_teaching(parse_deck01_manifest(register_text)))

    rows.extend(seed_chebyshev())
    rows.extend(seed_assignment_2025())

    for parsed in parse_mte_rows(mte_text):
        rows.append(
            make_row(
                parsed["instance_id"],
                "mte",
                parsed["source_label"],
                parsed["block_order"],
                summary=parsed["summary"],
                scope=parsed["scope"],
                description_state=DESCRIPTION_RESOLVED,
                provenance_verdict=parsed["provenance_verdict"],
                provenance_source=parsed["provenance_source"],
                evidence_locator=parsed["evidence_locator"],
            )
        )

    for parsed in parse_ete_rows(ete_text):
        rows.append(
            make_row(
                parsed["instance_id"],
                "ete",
                parsed["source_label"],
                parsed["block_order"],
                summary=parsed["summary"],
                scope=parsed["scope"],
                description_state=DESCRIPTION_RESOLVED,
                provenance_verdict=PROVENANCE_UNSEARCHED,
                evidence_locator=parsed["evidence_locator"],
            )
        )

    rows.extend(seed_assignment_2024())

    for parsed in parse_deck_rows(deck_csv_text):
        rows.append(
            make_row(
                parsed["instance_id"],
                "four-decks",
                parsed["source_label"],
                parsed["block_order"],
                page_start=parsed["page_start"],
                page_end=parsed["page_end"],
                summary=parsed["summary"],
                scope=parsed["scope"],
                description_state=DESCRIPTION_RESOLVED,
                provenance_verdict=parsed["provenance_verdict"],
                provenance_source=parsed["provenance_source"],
                evidence_locator=parsed["evidence_locator"],
            )
        )
    return rows


def validate_rows(rows):
    """Return a list of invariant problems; empty means the ledger is well formed."""
    problems = []
    if len(rows) != TOTAL_INSTANCES:
        problems.append(
            "total instance count: expected %d got %d" % (TOTAL_INSTANCES, len(rows))
        )
    group_counts = {}
    source_counts = {}
    ids = []
    for row in rows:
        group_counts[row["corpus_group"]] = group_counts.get(row["corpus_group"], 0) + 1
        source_counts[row["source_label"]] = (
            source_counts.get(row["source_label"], 0) + 1
        )
        ids.append(row["instance_id"])
    for group in GROUP_ORDER:
        expected = GROUP_TOTALS[group]
        actual = group_counts.get(group, 0)
        if actual != expected:
            problems.append(
                "group %s: expected %d got %d" % (group, expected, actual)
            )
    unknown_groups = sorted(set(group_counts) - set(GROUP_ORDER))
    if unknown_groups:
        problems.append("unknown group(s): %s" % unknown_groups)
    if len(ids) != len(set(ids)):
        duplicates = sorted(
            {value for value in ids if ids.count(value) > 1}
        )
        problems.append("duplicate instance_id(s): %s" % duplicates)

    for row in rows:
        if row["description_state"] == DESCRIPTION_PENDING:
            if row["summary"] != "":
                problems.append(
                    "pending row has a summary: %s" % row["instance_id"]
                )
        elif row["description_state"] == DESCRIPTION_RESOLVED:
            if not row["summary"]:
                problems.append(
                    "resolved row has no summary: %s" % row["instance_id"]
                )
        else:
            problems.append(
                "unknown description_state %r on %s"
                % (row["description_state"], row["instance_id"])
            )
        if row["status"] != STATUS_GROSS:
            problems.append("non-gross status on %s" % row["instance_id"])
    return problems


def ordering_key(row):
    return (
        GROUP_ORDER.index(row["corpus_group"]),
        SOURCE_ORDER[row["corpus_group"]].index(row["source_label"]),
        row["block_order"],
    )


def row_values(row):
    values = []
    for key in FIELDS:
        value = row.get(key, "")
        if value is None:
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
    """Return a list of problems; empty means the on-disk ledger matches reality."""
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
        problems.append("header mismatch: missing=%s extra=%s" % (missing, extra))

    body = actual[1:]
    expected_pairs = [row_values(row) for row in expected_rows]
    if len(body) != len(expected_pairs):
        problems.append(
            "row count mismatch: expected %d got %d"
            % (len(expected_pairs), len(body))
        )

    expected_ids = [values[0] for values in expected_pairs]
    actual_ids = [values[0] for values in body if values]
    seen = set()
    for instance_id in actual_ids:
        if instance_id in seen:
            problems.append("duplicate instance_id: %s" % instance_id)
        seen.add(instance_id)
    missing_ids = sorted(set(expected_ids) - set(actual_ids))
    extra_ids = sorted(set(actual_ids) - set(expected_ids))
    if missing_ids:
        problems.append("missing instance_id(s): %d" % len(missing_ids))
    if extra_ids:
        problems.append("unexpected instance_id(s): %d" % len(extra_ids))

    if actual_ids != expected_ids:
        problems.append("row order mismatch")

    if actual_text != expected_text:
        problems.append("stale generated content")
    return problems


def load_texts(root):
    root = pathlib.Path(root)
    return {
        "ete": read_text(root / ETE_REL),
        "mte": read_text(root / MTE_REL),
        "deck": read_text(root / DECK_REL),
        "register": read_text(root / REGISTER_REL),
    }


def generate_rows(root):
    texts = load_texts(root)
    rows = build_rows(texts["ete"], texts["mte"], texts["deck"], texts["register"])
    problems = validate_rows(rows)
    if problems:
        raise ValueError("; ".join(problems))
    return rows


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="Build or check the gross question-instance ledger."
    )
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
