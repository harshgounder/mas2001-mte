#!/usr/bin/env python3
"""Build the exact 119-item ledger for the 2025-26 assignment bundle (assignments 1 to 5).

The source PDF is /home/liebert511/PS/2025-2026-S&P_assignments_1-5.pdf (17 pages). The
ledger is built from the text layer at
/home/liebert511/mas2001-devore/corpus-text/asgn-2025-26-bundle.txt. That text layer keeps
the 17 form-feed page breaks, so every item can be attributed to a page without re-reading
the PDF.

Counts, one row per numbered occurrence (multi-part counts once):

    assignment 1   19   Q1..Q19
    assignment 2   36   Q1..Q36
    assignment 3   25   A1..A10, B1..B5, C1..C5, D1..D5
    assignment 4   21   1..21
    assignment 5   18   A1..A6, B1..B4, C1..C4, D1..D4
    total         119

Assignment 5 prints its fourth section-A item as "45.". That is a PDF typo for A4; the
row keeps the canonical label A4 and records the printed token in its evidence locator.

Page spans are taken from the form-feed delimited pages of the text layer and clipped to
the declared assignment ranges:

    assignment 1 pages 1-4    assignment 2 pages 5-8    assignment 3 pages 9-11
    assignment 4 pages 12-14  assignment 5 pages 15-17

extraction_state is one of:

    text_extracted          the item's statement follows its label in normal text order
    text_layout_recovered   the label sat alone on its line (or after a line break) so the
                            statement was recovered from the surrounding lines
    text_layout_reviewed    the item was manually reviewed and supplied with a canonical
                            summary via REVIEWED_SUMMARIES

REVIEWED_SUMMARIES maps the 17 full item ids that are currently recovered to faithful
one-line summaries. After automatic parsing, any row whose item_id appears in
REVIEWED_SUMMARIES uses the override summary and its extraction_state is set to
text_layout_reviewed. Retain text_layout_recovered as an allowed parser state, but
generated output must have zero recovered rows and exactly 17 reviewed rows.

structural_family_candidate is filled only when a section heading states the type in words
(memory, concept, analytical, application). Assignments 3, 4 and 5 print bare "SECTION A"
style headings, so their candidate is left blank; no structural or 2024 family match is
claimed without explicit evidence.

match_status is "not_assessed" for every row and matched_2024_locator is blank. The 2024-25
assignments are not in this run, so no 2024 match is asserted.

scope is one of:

    in-scope      assignments 1 and 2, plus seven lecture 19 to 21 items in assignment 3
    boundary      seven confidence-interval construction items in assignment 3
    out-of-scope  MLE, method of moments, Bayesian, and other post-MTE items in
                  assignment 3, plus assignments 4 and 5

Counts:

    in-scope      62
    boundary       7
    out-of-scope  50
    total         119

Usage:
    python3 scripts/build_assignment_bundle_ledger.py [--bundle PATH] [--output PATH]
    python3 scripts/build_assignment_bundle_ledger.py --check [--bundle PATH] [--output PATH]

--check rebuilds the ledger in memory and exits nonzero on a wrong header, a wrong count,
duplicate or missing ids, a page outside the declared range, a changed order, or stale
generated content. Standard library only.
"""

import argparse
import bisect
import csv
import io
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

DEFAULT_BUNDLE = pathlib.Path(
    "/home/liebert511/mas2001-devore/corpus-text/asgn-2025-26-bundle.txt"
)
LEDGER_REL = pathlib.Path("reports") / "evidence" / "assignment-bundle-ledger-20260916.csv"

FIELDS = [
    "item_id",
    "source_label",
    "assignment",
    "section",
    "item_label",
    "order",
    "page_start",
    "page_end",
    "summary",
    "extraction_state",
    "structural_family_candidate",
    "match_status",
    "matched_2024_locator",
    "evidence_locator",
    "scope",
]

WATERMARK = "MSV17HMFJTVMF6IE7MQ6"

EXPECTED_TOTAL = 119
EXPECTED_PAGES = 17

ASSIGNMENT_PAGES = {
    1: (1, 4),
    2: (5, 8),
    3: (9, 11),
    4: (12, 14),
    5: (15, 17),
}

ASSIGNMENT_COUNTS = {1: 19, 2: 36, 3: 25, 4: 21, 5: 18}

SOURCE_LABEL = {
    1: "assignment-2025-26-bundle-1",
    2: "assignment-2025-26-bundle-2",
    3: "assignment-2025-26-bundle-3",
    4: "assignment-2025-26-bundle-4",
    5: "assignment-2025-26-bundle-5",
}

EXTRACTION_TEXT = "text_extracted"
EXTRACTION_RECOVERED = "text_layout_recovered"
EXTRACTION_REVIEWED = "text_layout_reviewed"
MATCH_STATUS = "not_assessed"

SCOPE_IN_SCOPE = "in-scope"
SCOPE_BOUNDARY = "boundary"
SCOPE_OUT_OF_SCOPE = "out-of-scope"

ASSIGNMENT_3_IN_SCOPE = {
    "A5",
    "A6",
    "A7",
    "A9",
    "B3",
    "C2",
    "D5",
}

ASSIGNMENT_3_BOUNDARY = {
    "A10",
    "B4",
    "B5",
    "C3",
    "C4",
    "D2",
    "D4",
}

EXPECTED_IN_SCOPE_TOTAL = 62
EXPECTED_BOUNDARY_TOTAL = 7
EXPECTED_OUT_OF_SCOPE_TOTAL = 50

REVIEWED_SUMMARIES = {
    "asgnbundle-3-A05": "True or false: if sample statistic t is an unbiased estimator of population parameter theta, then t squared is also an unbiased estimator of theta squared.",
    "asgnbundle-3-A06": "Write a short note on efficiency of the best estimator.",
    "asgnbundle-3-A09": "Explain the properties of unbiasedness and consistency for an estimator.",
    "asgnbundle-3-B01": "Find the method of moments estimators for the mean and variance of normal random variables.",
    "asgnbundle-3-B02": "Find the maximum likelihood estimator of theta from a sample drawn from a specified density function.",
    "asgnbundle-3-B03": "Prove that the sample mean is a sufficient estimator of the population mean for a Poisson distribution.",
    "asgnbundle-3-B04": "A quality control expert estimates the mean thickness of aluminum sheets for airframes from n=100 sheets with mean 0.048 inches and sd 0.01 inches; construct a 99% confidence interval.",
    "asgnbundle-3-C01": "Find the maximum likelihood estimate of the mean survival time from exponential data of ten rats in a cancer drug study.",
    "asgnbundle-3-C02": "Verify that the sample mean is an unbiased estimator of the population mean using all samples of size two drawn with replacement from 2, 4, 6, 8.",
    "asgnbundle-3-C03": "Obtain a 95% confidence interval for the population mean from a random sample of size 10 with variance 44.1 inch squared.",
    "asgnbundle-3-C04": "Construct a 95% confidence interval for the mean number of automobile accidents per crossing per year from a random sample of 50 of 600 Jaipur road crossings with mean 3.8 and sd 0.8.",
    "asgnbundle-3-C05": "Find the maximum likelihood estimators for the population mean when variance is known and the population variance when mean is known from a normal population.",
    "asgnbundle-3-D01": "Find a 95% Bayesian interval to estimate the mean life of light bulbs with known standard deviation 100 hours, prior mean 800 and prior sd 10, from a sample of 25 bulbs with mean 780 hours.",
    "asgnbundle-3-D02": "Find a 90% confidence interval for the true mean value of sales from a random sample of 50 invoices with mean Rs 2000 and sd Rs 540.",
    "asgnbundle-3-D03": "For a random sample from a two-parameter density function, find the likelihood function and the equations for the maximum likelihood estimators of alpha and beta.",
    "asgnbundle-3-D05": "Find sufficient estimators for the mean and variance of a normal population from a random sample.",
    "asgnbundle-5-C03": "Test whether income and type of schooling are independent for 1000 families selected at random.",
}

ASSIGNMENT_HEADER_RE = re.compile(
    r"(?m)^[ \t]*Assignment\s*(?:#\s*|[-]\s*|\u2013\s*|\u2014\s*)?([1-5])\s*$"
)
SECTION_HEADER_RE = re.compile(
    r"(?m)^[ \t]*(?:SECTION[ \t]*-?[ \t]*([A-D])|Section[ \t]+([A-D]))\b"
)
COVER_RE = re.compile(
    r"(?m)^[ \t]*(?:"
    r"Statistical Methods and Probability Theory"
    r"|MANIPAL UNIVERSITY JAIPUR"
    r"|Department of Mathematics"
    r"|B\.Tech\."
    r"|MAS2001-Statistical"
    r"|Session:"
    r"|Topics\b"
    r"|Topics Covered:"
    r"|Assignment\s*(?:#\s*|[-]\s*|\u2013\s*|\u2014\s*)?[1-5]\s*$"
    r")"
)

SECTION_FAMILY = [
    ("memory", "memory_based"),
    ("concept", "concept_based"),
    ("analytical", "analytical_based"),
    ("application", "application_based"),
]

# The literal token printed for the fourth section-A item of assignment 5.
PRINTED_TYPO_LABEL = "45"
TYPO_CANONICAL = "A4"


def log(message):
    print(message, file=sys.stderr, flush=True)


def read_text(path):
    return pathlib.Path(path).read_text(encoding="utf-8")


def expected_labels(assignment):
    if assignment == 1:
        return ["Q%d" % number for number in range(1, 20)]
    if assignment == 2:
        return ["Q%d" % number for number in range(1, 37)]
    if assignment == 3:
        return (
            ["A%d" % number for number in range(1, 11)]
            + ["B%d" % number for number in range(1, 6)]
            + ["C%d" % number for number in range(1, 6)]
            + ["D%d" % number for number in range(1, 6)]
        )
    if assignment == 4:
        return [str(number) for number in range(1, 22)]
    if assignment == 5:
        return (
            ["A1", "A2", "A3", PRINTED_TYPO_LABEL, "A5", "A6"]
            + ["B%d" % number for number in range(1, 5)]
            + ["C%d" % number for number in range(1, 5)]
            + ["D%d" % number for number in range(1, 5)]
        )
    raise ValueError("unknown assignment %r" % (assignment,))


def canonical_label(assignment, printed):
    if assignment == 5 and printed == PRINTED_TYPO_LABEL:
        return TYPO_CANONICAL
    return printed


def scope_for(assignment, item_label):
    """Return the item-level MTE scope from the official lecture boundary."""
    if assignment in (1, 2):
        return SCOPE_IN_SCOPE
    if assignment == 3 and item_label in ASSIGNMENT_3_IN_SCOPE:
        return SCOPE_IN_SCOPE
    if assignment == 3 and item_label in ASSIGNMENT_3_BOUNDARY:
        return SCOPE_BOUNDARY
    return SCOPE_OUT_OF_SCOPE


def label_id_part(assignment, printed):
    canonical = canonical_label(assignment, printed)
    match = re.match(r"^([A-Za-z]?)(\d+)$", canonical)
    if not match:
        raise ValueError("unexpected label %r" % (canonical,))
    return "%s%02d" % (match.group(1), int(match.group(2)))


def label_regex(assignment, label):
    """Return a line-anchored regex matching one item label in its assignment."""
    if assignment in (1, 2):
        return re.compile(r"(?m)^[ \t]*(Q\s?%s\s?[\.\)])" % label[1:])
    if assignment == 3:
        return re.compile(r"(?m)^[ \t]*(%s)(?=\s)" % re.escape(label))
    if assignment == 5:
        return re.compile(r"(?m)^[ \t]*(%s)\s?[\.\)]" % re.escape(label))
    return re.compile(r"(?m)^[ \t]*(%s\.)\s" % re.escape(label))


def strip_watermark(text):
    return text.replace(WATERMARK, " ")


def is_blank(line):
    return strip_watermark(line).strip() == ""


def split_lines(text, base):
    """Yield (line_text, absolute_offset) for every line of text."""
    lines = []
    offset = 0
    for line in text.split("\n"):
        lines.append((line, base + offset))
        offset += len(line) + 1
    return lines


def split_gap(text, base):
    """Split the gap before a label into (belongs_before, belongs_after).

    Only blank lines separate the two runs. A trailing run of blank lines is ignored so
    the page's final newline does not hide the recovery. The after run is the text that
    sits directly above the coming label and belongs to it.
    """
    lines = split_lines(text, base)
    while lines and is_blank(lines[-1][0]):
        lines.pop()
    last_blank = -1
    for index, (line, _) in enumerate(lines):
        if is_blank(line):
            last_blank = index
    head = [(line, off) for line, off in lines[:last_blank] if not is_blank(line)]
    tail = [
        (line, off)
        for line, off in lines[last_blank + 1 :]
        if not is_blank(line) and strip_watermark(line).strip()
    ]
    return head, tail


def needs_prefix(item):
    """True when a label's statement may sit on the lines above the label.

    Bare labels always need recovery. Labels whose visible remainder starts with a
    bracket, a digit or a lower-case letter are continuations of the line above.
    """
    if item["bare"]:
        return True
    text = normalize(item["inline"])
    if not text:
        return True
    first = text[0]
    return first in "([0123456789" or first.islower()


def normalize(text):
    text = text.replace("\u2014", "-").replace("\u2013", "-")
    return re.sub(r"\s+", " ", text).strip()


def summarize(body):
    """Join body lines, drop answers, normalize dashes and cap the length."""
    kept = []
    for line, _ in body:
        text = strip_watermark(line)
        match = re.search(r"\bAns\b", text)
        if match:
            text = text[: match.start()]
        if text.strip():
            kept.append(text)
    text = normalize(" ".join(kept))
    if len(text) > 200:
        text = text[:200].rsplit(" ", 1)[0] + " ..."
    return text


def page_starts(text):
    starts = []
    offset = 0
    for part in text.split("\f"):
        starts.append(offset)
        offset += len(part) + 1
    return starts


def build_rows(text):
    """Build the 119 rows from the bundle text layer."""
    pages = text.split("\f")
    if pages and pages[-1] == "":
        pages.pop()
    if len(pages) != EXPECTED_PAGES:
        raise ValueError(
            "expected %d bundle pages, found %d" % (EXPECTED_PAGES, len(pages))
        )
    starts = page_starts(text)

    def page_of(offset):
        return bisect.bisect_right(starts, offset)

    def line_end(offset):
        found = text.find("\n", offset)
        return found if found != -1 else len(text)

    headers = [
        (int(match.group(1)), match.start(), match.end())
        for match in ASSIGNMENT_HEADER_RE.finditer(text)
    ]
    if [number for number, _, _ in headers] != [1, 2, 3, 4, 5]:
        raise ValueError("assignment headers not found in order 1..5")

    regions = []
    for index, (number, start, end) in enumerate(headers):
        region_end = headers[index + 1][1] if index + 1 < len(headers) else len(text)
        regions.append((number, start, end, region_end))

    rows = []
    for assignment, _header_start, header_end, region_end in regions:
        sections = [
            (match.start(), match.end(), (match.group(1) or match.group(2)))
            for match in SECTION_HEADER_RE.finditer(text, header_end, region_end)
        ]
        if sections:
            spans = []
            for index, (start, end, letter) in enumerate(sections):
                span_end = (
                    sections[index + 1][0] if index + 1 < len(sections) else region_end
                )
                spans.append((start, end, letter, span_end))
        else:
            spans = [(header_end, header_end, None, region_end)]

        items = []
        cursor = header_end
        for printed in expected_labels(assignment):
            match = label_regex(assignment, printed).search(text, cursor, region_end)
            if not match:
                raise ValueError(
                    "assignment %d missing label %r" % (assignment, printed)
                )
            end_of_line = line_end(match.end())
            inline = text[match.end() : end_of_line]
            items.append(
                {
                    "printed": printed,
                    "canonical": canonical_label(assignment, printed),
                    "start": match.start(),
                    "end": match.end(),
                    "line_end": end_of_line,
                    "inline": inline,
                    "bare": normalize(inline) == "",
                    "order": len(items) + 1,
                    "pre": [],
                    "gap": [],
                    "section": "",
                    "family": "",
                    "recovered": False,
                }
            )
            cursor = match.end()

        for section_start, section_end, letter, span_end in spans:
            section_items = [
                item
                for item in items
                if section_start <= item["start"] < span_end
            ]
            if not section_items:
                continue
            if letter:
                family = section_family(
                    text[section_start : line_end(section_start)]
                )
            else:
                family = ""
            for item in section_items:
                if letter:
                    item["section"] = letter
                elif assignment == 5:
                    item["section"] = (
                        "A" if item["printed"] == PRINTED_TYPO_LABEL else item["printed"][0]
                    )
                item["family"] = family

            if letter:
                prefix_start = line_end(section_end)
                prefix = [
                    (line, offset)
                    for line, offset in split_lines(
                        text[prefix_start : section_items[0]["start"]], prefix_start
                    )
                    if not is_blank(line)
                ]
            else:
                prefix = []

            for index, item in enumerate(section_items):
                item["pre"] = prefix
                gap_start = item["line_end"]
                gap_end = (
                    section_items[index + 1]["start"]
                    if index + 1 < len(section_items)
                    else span_end
                )
                gap_text = text[gap_start:gap_end]
                if index + 1 < len(section_items) and needs_prefix(
                    section_items[index + 1]
                ):
                    head, prefix = split_gap(gap_text, gap_start)
                    gap = head
                else:
                    prefix = []
                    gap = [
                        (line, offset)
                        for line, offset in split_lines(gap_text, gap_start)
                        if not is_blank(line) and strip_watermark(line).strip()
                    ]
                cleaned = []
                for line, offset in gap:
                    if COVER_RE.match(line):
                        break
                    cleaned.append((line, offset))
                item["gap"] = cleaned

        for item in items:
            body = item["pre"] + [(item["inline"], item["end"])] + item["gap"]
            body = [
                (line, offset)
                for line, offset in body
                if strip_watermark(line).strip()
            ]
            summary = summarize(body)
            page_start = page_of(item["start"])
            page_end = page_start
            if body:
                page_end = max(page_end, page_of(max(offset for _, offset in body)))
            low, high = ASSIGNMENT_PAGES[assignment]
            page_start = min(max(page_start, low), high)
            page_end = min(max(page_end, low), high)
            if page_end < page_start:
                page_end = page_start
            recovered = item["bare"] or bool(item["pre"])
            line_number = text.count("\n", 0, item["start"]) + 1
            locator = "asgn-2025-26-bundle.txt:L%d; PDF p%d" % (
                line_number,
                page_start,
            )
            if page_end != page_start:
                locator = "asgn-2025-26-bundle.txt:L%d; PDF p%d-%d" % (
                    line_number,
                    page_start,
                    page_end,
                )
            if item["printed"] == PRINTED_TYPO_LABEL:
                locator += " (printed label 45 read as A4)"
            item_id = "asgnbundle-%d-%s" % (
                assignment, label_id_part(assignment, item["printed"])
            )
            if item_id in REVIEWED_SUMMARIES:
                summary = REVIEWED_SUMMARIES[item_id]
                extraction_state = EXTRACTION_REVIEWED
            else:
                extraction_state = (
                    EXTRACTION_RECOVERED if recovered else EXTRACTION_TEXT
                )
            rows.append(
                {
                    "item_id": item_id,
                    "source_label": SOURCE_LABEL[assignment],
                    "assignment": assignment,
                    "section": item["section"],
                    "item_label": item["canonical"],
                    "order": item["order"],
                    "page_start": page_start,
                    "page_end": page_end,
                    "summary": summary,
                    "extraction_state": extraction_state,
                    "structural_family_candidate": item["family"],
                    "match_status": MATCH_STATUS,
                    "matched_2024_locator": "",
                    "evidence_locator": locator,
                    "scope": scope_for(assignment, item["canonical"]),
                }
            )
    return rows


def section_family(header_line):
    """Return a structural candidate only when the heading states it in words."""
    lowered = header_line.lower()
    for keyword, family in SECTION_FAMILY:
        if keyword in lowered:
            return family
    return ""


def validate_rows(rows):
    """Return a list of invariant problems; empty means the ledger is well formed."""
    problems = []
    for item_id, summary in REVIEWED_SUMMARIES.items():
        if not summary:
            problems.append("empty reviewed summary for %s" % item_id)
        if "\n" in summary:
            problems.append("multiline reviewed summary for %s" % item_id)
        if len(summary) > 200:
            problems.append("reviewed summary exceeds 200 chars for %s" % item_id)
        if "\u2014" in summary or "\u2013" in summary:
            problems.append("forbidden dash in reviewed summary for %s" % item_id)
    if len(rows) != EXPECTED_TOTAL:
        problems.append(
            "total item count: expected %d got %d" % (EXPECTED_TOTAL, len(rows))
        )
    counts = {}
    ids = []
    orders = {}
    for row in rows:
        counts[row["assignment"]] = counts.get(row["assignment"], 0) + 1
        ids.append(row["item_id"])
        orders.setdefault(row["assignment"], []).append(row["order"])
    for assignment, expected in ASSIGNMENT_COUNTS.items():
        actual = counts.get(assignment, 0)
        if actual != expected:
            problems.append(
                "assignment %d: expected %d got %d" % (assignment, expected, actual)
            )
    unknown = sorted(set(counts) - set(ASSIGNMENT_COUNTS))
    if unknown:
        problems.append("unknown assignment(s): %s" % unknown)
    if len(ids) != len(set(ids)):
        duplicates = sorted({value for value in ids if ids.count(value) > 1})
        problems.append("duplicate item_id(s): %s" % duplicates)
    for assignment, values in orders.items():
        if values != list(range(1, len(values) + 1)):
            problems.append("assignment %d has non-dense order" % assignment)

    for row in rows:
        low, high = ASSIGNMENT_PAGES[row["assignment"]]
        if not (low <= row["page_start"] <= high):
            problems.append(
                "page_start out of range on %s" % row["item_id"]
            )
        if not (low <= row["page_end"] <= high):
            problems.append("page_end out of range on %s" % row["item_id"])
        if row["page_end"] < row["page_start"]:
            problems.append("page_end before page_start on %s" % row["item_id"])
        if row["extraction_state"] not in (
            EXTRACTION_TEXT,
            EXTRACTION_RECOVERED,
            EXTRACTION_REVIEWED,
        ):
            problems.append(
                "unknown extraction_state %r on %s"
                % (row["extraction_state"], row["item_id"])
            )
        if not row["summary"]:
            problems.append("empty summary on %s" % row["item_id"])
        if row["item_id"] in REVIEWED_SUMMARIES:
            if row["extraction_state"] != EXTRACTION_REVIEWED:
                problems.append(
                    "reviewed item %s not marked text_layout_reviewed"
                    % row["item_id"]
                )
            if row["summary"] != REVIEWED_SUMMARIES[row["item_id"]]:
                problems.append(
                    "reviewed item %s has wrong summary" % row["item_id"]
                )
        elif row["extraction_state"] == EXTRACTION_REVIEWED:
            problems.append(
                "unearned text_layout_reviewed state on %s" % row["item_id"]
            )
        if row["assignment"] in (3, 4, 5) and row["structural_family_candidate"]:
            problems.append(
                "unearned structural candidate on %s" % row["item_id"]
            )
        if row["match_status"] != MATCH_STATUS:
            problems.append("non-honest match_status on %s" % row["item_id"])
        if row["matched_2024_locator"]:
            problems.append(
                "unearned 2024 locator on %s" % row["item_id"]
            )
        expected_scope = scope_for(row["assignment"], row["item_label"])
        if row["scope"] != expected_scope:
            problems.append(
                "wrong scope %r on %s" % (row["scope"], row["item_id"])
            )
    in_scope_count = sum(1 for row in rows if row["scope"] == SCOPE_IN_SCOPE)
    boundary_count = sum(1 for row in rows if row["scope"] == SCOPE_BOUNDARY)
    out_of_scope_count = sum(1 for row in rows if row["scope"] == SCOPE_OUT_OF_SCOPE)
    if in_scope_count != EXPECTED_IN_SCOPE_TOTAL:
        problems.append(
            "in-scope count: expected %d got %d"
            % (EXPECTED_IN_SCOPE_TOTAL, in_scope_count)
        )
    if boundary_count != EXPECTED_BOUNDARY_TOTAL:
        problems.append(
            "boundary count: expected %d got %d"
            % (EXPECTED_BOUNDARY_TOTAL, boundary_count)
        )
    if out_of_scope_count != EXPECTED_OUT_OF_SCOPE_TOTAL:
        problems.append(
            "out-of-scope count: expected %d got %d"
            % (EXPECTED_OUT_OF_SCOPE_TOTAL, out_of_scope_count)
        )
    reviewed_ids = {
        row["item_id"]
        for row in rows
        if row["extraction_state"] == EXTRACTION_REVIEWED
    }
    if reviewed_ids != set(REVIEWED_SUMMARIES):
        problems.append("reviewed item manifest does not match generated rows")
    recovered_count = sum(
        1 for row in rows if row["extraction_state"] == EXTRACTION_RECOVERED
    )
    if recovered_count:
        problems.append(
            "recovered row count: expected 0 got %d" % recovered_count
        )
    return problems


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
    for item_id in actual_ids:
        if item_id in seen:
            problems.append("duplicate item_id: %s" % item_id)
        seen.add(item_id)
    missing_ids = sorted(set(expected_ids) - set(actual_ids))
    extra_ids = sorted(set(actual_ids) - set(expected_ids))
    if missing_ids:
        problems.append("missing item_id(s): %d" % len(missing_ids))
    if extra_ids:
        problems.append("unexpected item_id(s): %d" % len(extra_ids))
    if actual_ids != expected_ids:
        problems.append("row order mismatch")
    if actual_text != expected_text:
        problems.append("stale generated content")
    return problems


def generate_rows(bundle_path):
    text = read_text(bundle_path)
    rows = build_rows(text)
    problems = validate_rows(rows)
    if problems:
        raise ValueError("; ".join(problems))
    return rows


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="Build or check the 2025-26 assignment bundle ledger."
    )
    parser.add_argument(
        "--bundle", default=str(DEFAULT_BUNDLE), help="bundle text layer path"
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
    rows = generate_rows(args.bundle)

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
