#!/usr/bin/env python3
"""Build illustrated PDF editions of every MAS2001 deck and note file."""

from __future__ import annotations

import argparse
import csv
import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Circle, Drawing, Line, Polygon, Rect, String
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)
from svglib.svglib import svg2rlg


REPO = Path(__file__).resolve().parents[2]
DECK = REPO / "deck"
NOTES = REPO / "deck" / "notes"
VISUALS = REPO / "deck" / "visuals-gpt56" / "assets"
NOTES_OUTPUT = REPO / "output" / "pdf" / "visual-notes"
DECK_OUTPUT = REPO / "output" / "pdf" / "visual-deck"
CONVERSION_LEDGER = REPO / "deck" / "visuals-gpt56" / "source-notes" / "pdf-block-conversion.csv"
TMP = REPO / "tmp" / "pdfs"

PAGE_W, PAGE_H = A4
LEFT = 18 * mm
RIGHT = 18 * mm
TOP = 21 * mm
BOTTOM = 18 * mm
CONTENT_W = PAGE_W - LEFT - RIGHT

INK = colors.HexColor("#172033")
MUTED = colors.HexColor("#64748b")
BLUE = colors.HexColor("#2563eb")
CYAN = colors.HexColor("#0891b2")
PURPLE = colors.HexColor("#7c3aed")
SOFT = colors.HexColor("#f4f7fb")
GRID = colors.HexColor("#dbe3ee")

STRUCTURAL_MARKERS = set("│├┤└┌┐┘┬┴┼─▶◀█║╔╗╚╝═╠╣╦╩╬▓▃▁╱╲‾▲▼●")
BOX_MARKERS = set("│├┤└┌┐┘┬┴┼─║╔╗╚╝═╠╣╦╩╬")


VISUAL_INSERTS = {
    "README.md": [
        ("Read this first", "course-map.svg", "Course concept map"),
    ],
    "00-INDEX.md": [
        ("THE COURSE AS A TREE", "course-map.svg", "Course prerequisite map"),
        ("THE ORDER", "study-roadmap.svg", "Study order and dependency gates"),
    ],
    "01-CHEATSHEET.md": [
        ("WHOLE PAPER AS ONE FLOWCHART", "formula-landscape.svg", "Formula landscape and final checks"),
        ("FIVE DISTRIBUTIONS", "distribution-gallery.svg", "Five parameterized distribution shapes"),
    ],
    "02-TERMS.md": [
        ("MASTER TERM MAP", "course-map.svg", "Concept relationships across the course"),
    ],
    "03-LINGUISTICS.md": [
        ("MASTER WORDING", "method-decision-tree.svg", "Question-solving decision path"),
        ("CONDITIONAL", "probability-tree.svg", "Conditional probability tree"),
    ],
    "04-METHODS.md": [
        ("MASTER DECISION TREE", "method-decision-tree.svg", "Question-solving decision path"),
    ],
    "05-DISTRIBUTIONS.md": [
        ("FIVE-DISTRIBUTION MAP", "distribution-gallery.svg", "Five parameterized distribution shapes"),
        ("NORMAL", "normal-table-conventions.svg", "Two normal-table conventions"),
    ],
    "06-NUMBERS.md": [
        ("NORMAL-TABLE", "normal-table-conventions.svg", "Cumulative and centre-area normal tables"),
    ],
    "07-PATTERNS.md": [
        ("MUTATION TREE", "mutation-operators.svg", "Question mutation operators"),
    ],
    "08-TRAPS.md": [
        ("MASTER TRAP", "method-decision-tree.svg", "Solve and check before committing to an answer"),
    ],
    "09-QUESTIONS.md": [
        ("QUESTION UNIVERSE", "mutation-operators.svg", "Question families and structural mutations"),
    ],
    "10-SLIDE-MAP.md": [
        ("COURSE PAGE MAP", "course-map.svg", "Course concept map"),
    ],
    "11-BEYOND-SLIDES.md": [
        ("VISIBLE COURSE", "study-roadmap.svg", "Visible topics and hidden dependency gates"),
    ],
    "12-DRILL.md": [
        ("50-QUESTION LADDER", "study-roadmap.svg", "Drill sequence and dependency gates"),
    ],
    "13-EXAM-MECHANICS.md": [
        ("time budget", "exam-timeline.svg", "Proportional ninety-minute practice budget"),
    ],
    "14-MASTER-STUDY-ORDER.md": [
        ("MASTER ORDER, ONE PICTURE", "study-roadmap.svg", "Study order and dependency gates"),
        ("DEPENDENCY MAP", "course-map.svg", "Course prerequisite map"),
    ],
    "00-NOTES-INDEX.md": [
        ("The map", "course-map.svg", "Course concept map"),
        ("one picture to hold", "study-roadmap.svg", "Study order and dependency gates"),
    ],
    "01-probability-foundations.md": [
        ("Sample space", "dice-sum.svg", "The 36 ordered outcomes for two dice"),
        ("Conditional probability", "probability-tree.svg", "Conditional probability tree"),
    ],
    "02-random-variables.md": [
        ("dice sum", "dice-sum.svg", "Ordered outcomes and the distribution of their sum"),
    ],
    "03-pmf-and-cdf.md": [
        ("cumulative distribution", "pmf-to-cdf.svg", "How a PMF accumulates into a CDF"),
    ],
    "04-expectation-and-variance.md": [
        ("three parameters", "expectation-variance.svg", "Mean as balance point and variance as spread"),
    ],
    "05-continuous-rv.md": [
        ("probability density function", "continuous-pdf-cdf.svg", "PDF, probability area, and CDF relationships"),
    ],
    "06-binomial-poisson.md": [
        ("DISCRETE DISTRIBUTIONS SIDE BY SIDE", "distribution-gallery.svg", "Distribution shapes, with the discrete models on the left"),
    ],
    "07-uniform-normal-exponential.md": [
        ("family tree first", "distribution-gallery.svg", "Five distribution shapes for comparison"),
        ("THE TWO TABLES", "normal-table-conventions.svg", "Cumulative and centre-area normal tables"),
    ],
    "08-sampling-and-clt.md": [
        ("Standard error", "sampling-clt.svg", "Sampling distributions narrow at the exact square-root rate"),
    ],
    "09-estimation.md": [
        ("WORKED COMPARISON SET 2", "estimator-comparison.svg", "Unbiased estimators compared by variance"),
    ],
    "10-chebyshev-and-hidden.md": [
        ("geometry, drawn", "chebyshev-bound.svg", "Chebyshev central-mass guarantee without a shape assumption"),
        ("hidden-layer study order", "study-roadmap.svg", "Study order and dependency gates"),
    ],
}


DECK_BLOCK_TYPES = {
    "00-INDEX.md": ["flow", "flow", "flow", "table", "table", "table", "table", "timeline", "table", "table"],
    "01-CHEATSHEET.md": ["flow", "plot", "plot", "formula", "formula", "formula", "formula", "formula", "formula", "formula", "table", "table", "table"],
    "02-TERMS.md": ["flow", "table", "table", "table", "table", "table", "table", "table", "table", "table", "table", "table", "table"],
    "03-LINGUISTICS.md": ["flow", "plot", "flow", "table", "table", "table", "table", "table", "table", "table"],
    "04-METHODS.md": ["flow", "flow"] + ["table"] * 17,
    "05-DISTRIBUTIONS.md": ["plot", "flow"] + ["table"] * 12,
    "06-NUMBERS.md": ["plot", "plot", "plot", "table", "table", "table", "formula", "table", "table", "formula", "table", "table"],
    "07-PATTERNS.md": ["flow", "callout", "table", "flow"] + ["table"] * 8,
    "08-TRAPS.md": ["flow", "table", "callout", "table", "table", "table"],
    "09-QUESTIONS.md": ["table", "table", "plot"] + ["table"] * 6,
    "10-SLIDE-MAP.md": ["timeline"] + ["table"] * 9,
    "11-BEYOND-SLIDES.md": ["flow", "plot"] + ["table"] * 10,
    "12-DRILL.md": ["timeline"] + ["table"] * 10 + ["callout"],
    "13-EXAM-MECHANICS.md": ["callout", "timeline", "table", "flow", "callout", "plot", "table", "callout"],
    "14-MASTER-STUDY-ORDER.md": ["table", "flow", "table", "table", "table", "table", "table", "table", "table", "table", "table", "flow", "table", "timeline", "table", "timeline"],
    "README.md": ["table", "timeline", "table"],
}


def register_fonts():
    font_dir = Path("/usr/share/fonts/TTF")
    pdfmetrics.registerFont(TTFont("DejaVu", font_dir / "DejaVuSans.ttf"))
    pdfmetrics.registerFont(TTFont("DejaVu-Bold", font_dir / "DejaVuSans-Bold.ttf"))
    pdfmetrics.registerFont(TTFont("DejaVuMono", font_dir / "DejaVuSansMono.ttf"))
    pdfmetrics.registerFont(TTFont("DejaVuMono-Bold", font_dir / "DejaVuSansMono-Bold.ttf"))


def styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "VisualTitle", parent=base["Title"], fontName="DejaVu-Bold", fontSize=24,
            leading=29, textColor=INK, spaceAfter=12, alignment=TA_LEFT,
        ),
        "h1": ParagraphStyle(
            "H1", parent=base["Heading1"], fontName="DejaVu-Bold", fontSize=20,
            leading=25, textColor=colors.white, backColor=BLUE, borderPadding=12,
            spaceBefore=4, spaceAfter=16, keepWithNext=1,
        ),
        "h2": ParagraphStyle(
            "H2", parent=base["Heading2"], fontName="DejaVu-Bold", fontSize=14,
            leading=18, textColor=INK, borderColor=CYAN, borderWidth=0,
            borderPadding=(0, 0, 5, 0), spaceBefore=14, spaceAfter=7,
            keepWithNext=1,
        ),
        "h3": ParagraphStyle(
            "H3", parent=base["Heading3"], fontName="DejaVu-Bold", fontSize=11.5,
            leading=15, textColor=PURPLE, spaceBefore=10, spaceAfter=5,
            keepWithNext=1,
        ),
        "body": ParagraphStyle(
            "Body", parent=base["BodyText"], fontName="DejaVu", fontSize=9.2,
            leading=13.2, textColor=INK, spaceAfter=6,
        ),
        "bullet": ParagraphStyle(
            "Bullet", parent=base["BodyText"], fontName="DejaVu", fontSize=9.1,
            leading=13, textColor=INK, leftIndent=15, firstLineIndent=-8, spaceAfter=3,
        ),
        "caption": ParagraphStyle(
            "Caption", parent=base["BodyText"], fontName="DejaVu", fontSize=8,
            leading=10.5, textColor=MUTED, alignment=TA_CENTER, spaceBefore=4, spaceAfter=11,
        ),
        "cover": ParagraphStyle(
            "Cover", parent=base["Title"], fontName="DejaVu-Bold", fontSize=30,
            leading=37, textColor=INK, alignment=TA_CENTER, spaceAfter=14,
        ),
        "cover_sub": ParagraphStyle(
            "CoverSub", parent=base["BodyText"], fontName="DejaVu", fontSize=13,
            leading=19, textColor=MUTED, alignment=TA_CENTER, spaceAfter=10,
        ),
    }


def inline_markup(value: str) -> str:
    value = html.escape(value, quote=False)
    value = re.sub(r"`([^`]+)`", r'<font name="DejaVuMono" color="#4338ca">\1</font>', value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    return value


def visual_flowables(asset_name: str, caption: str, st):
    path = VISUALS / asset_name
    drawing = svg2rlg(str(path))
    if drawing is None:
        raise ValueError(f"could not parse SVG: {path}")
    scale = min(CONTENT_W / drawing.width, 88 * mm / drawing.height)
    drawing.width *= scale
    drawing.height *= scale
    drawing.scale(scale, scale)
    frame = Table([[drawing]], colWidths=[CONTENT_W], hAlign="CENTER")
    frame.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),
        ("BOX", (0, 0), (-1, -1), 0.7, GRID),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return [Spacer(1, 4), frame, Paragraph(inline_markup(caption), st["caption"])]


def is_border_line(line: str) -> bool:
    compact = "".join(line.split())
    return bool(compact) and all(char in BOX_MARKERS or char in "+-=_" for char in compact)


def table_rows(lines: list[str]):
    content = []
    meaningful = [line for line in lines if line.strip() and not is_border_line(line)]
    for raw in lines:
        if is_border_line(raw):
            continue
        normalized = raw.replace("║", "│").strip()
        if "│" not in normalized:
            continue
        cells = [cell.strip() for cell in normalized.strip("│").split("│")]
        if len(cells) >= 2 and any(cells):
            content.append(cells)
    if len(content) < 2:
        return None
    if len(content) / max(1, len(meaningful)) < 0.8:
        return None
    counts = [len(row) for row in content]
    width = max(set(counts), key=counts.count)
    stable = [row for row in content if len(row) == width]
    if width < 2 or len(stable) != len(content):
        return None
    return stable


def semantic_table_flowable(rows: list[list[str]], st):
    columns = len(rows[0])
    lengths = [max(4, max(len(row[i]) for row in rows)) for i in range(columns)]
    total = sum(lengths)
    widths = [CONTENT_W * length / total for length in lengths]
    cell_style = ParagraphStyle(
        "VisualTableCell", parent=st["body"], fontSize=7.4, leading=9.6,
        spaceAfter=0, textColor=INK,
    )
    data = [[Paragraph(inline_markup(cell), cell_style) for cell in row] for row in rows]
    table = Table(data, colWidths=widths, repeatRows=1, hAlign="CENTER")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8eefc")),
        ("TEXTCOLOR", (0, 0), (-1, 0), INK),
        ("FONTNAME", (0, 0), (-1, 0), "DejaVu-Bold"),
        ("GRID", (0, 0), (-1, -1), 0.45, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, SOFT]),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return table


def aligned_table_rows(lines: list[str]):
    parsed = []
    for raw in lines:
        if is_border_line(raw):
            continue
        value = raw.strip().strip("│║").strip()
        if not value:
            continue
        cells = [cell.strip() for cell in re.split(r"\s{2,}", value) if cell.strip()]
        parsed.append(cells or [value])
    if not parsed:
        return [[""]]
    counts = [len(row) for row in parsed if len(row) > 1]
    columns = min(6, max(counts, default=2))
    normalized = []
    for row in parsed:
        if len(row) > columns:
            row = row[: columns - 1] + ["  ".join(row[columns - 1:])]
        if len(row) == 1:
            row = [row[0]] + [""] * (columns - 1)
        else:
            row = row + [""] * (columns - len(row))
        normalized.append(row)
    return normalized


def looks_like_aligned_table(lines: list[str]) -> bool:
    meaningful = [line for line in lines if line.strip() and not is_border_line(line)]
    if len(meaningful) < 3:
        return False
    aligned = [line for line in meaningful if re.search(r"\S\s{2,}\S", line)]
    return len(aligned) >= 2 and len(aligned) / len(meaningful) >= 0.5


def formula_flowable(lines: list[str], st):
    body = "<br/>".join(inline_markup(line.strip()) for line in lines if line.strip())
    paragraph = Paragraph(body or " ", ParagraphStyle(
        "FormulaPanel", parent=st["body"], fontName="DejaVu",
        fontSize=8.6, leading=12.2, textColor=INK, spaceAfter=0,
    ))
    table = Table([[paragraph]], colWidths=[CONTENT_W], hAlign="CENTER")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), SOFT),
        ("LINEBEFORE", (0, 0), (0, -1), 2.2, PURPLE),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return table


def callout_flowable(lines: list[str], st):
    cleaned = []
    for raw in lines:
        if is_border_line(raw):
            continue
        value = raw.strip().strip("│║").strip()
        if value:
            cleaned.append(value)
    body = "<br/>".join(inline_markup(line) for line in cleaned)
    paragraph = Paragraph(body or " ", ParagraphStyle(
        "VisualCallout", parent=st["body"], fontName="DejaVu",
        fontSize=8.5, leading=12, textColor=INK, spaceAfter=0,
    ))
    table = Table([[paragraph]], colWidths=[CONTENT_W], hAlign="CENTER")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#eef5ff")),
        ("BOX", (0, 0), (-1, -1), 1.1, BLUE),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return table


def vector_diagram_flowable(lines: list[str]):
    rows = max(1, len(lines))
    cols = max((len(line) for line in lines), default=1)
    cell_w, cell_h = 5.6, 9.0
    raw_w, raw_h = cols * cell_w + 12, rows * cell_h + 12
    scale = min(CONTENT_W / raw_w, (165 * mm) / raw_h, 1.0)
    width, height = raw_w * scale, raw_h * scale
    drawing = Drawing(width, height)
    line_color = colors.HexColor("#52657e")
    mark_color = CYAN
    font_size = max(3.8, 6.6 * scale)

    connections = {
        "─": (1, 0, 1, 0), "═": (1, 0, 1, 0),
        "│": (0, 1, 0, 1), "║": (0, 1, 0, 1),
        "┌": (0, 0, 1, 1), "╔": (0, 0, 1, 1),
        "┐": (1, 0, 0, 1), "╗": (1, 0, 0, 1),
        "└": (0, 1, 1, 0), "╚": (0, 1, 1, 0),
        "┘": (1, 1, 0, 0), "╝": (1, 1, 0, 0),
        "├": (0, 1, 1, 1), "╠": (0, 1, 1, 1),
        "┤": (1, 1, 0, 1), "╣": (1, 1, 0, 1),
        "┬": (1, 0, 1, 1), "╦": (1, 0, 1, 1),
        "┴": (1, 1, 1, 0), "╩": (1, 1, 1, 0),
        "┼": (1, 1, 1, 1), "╬": (1, 1, 1, 1),
    }

    for row_index, raw in enumerate(lines):
        y = height - (row_index + 1) * cell_h * scale - 6 * scale
        col = 0
        while col < len(raw):
            char = raw[col]
            x = 6 * scale + col * cell_w * scale
            if char in connections:
                left, up, right, down = connections[char]
                cx, cy = x + cell_w * scale / 2, y + cell_h * scale / 2
                stroke = 1.0 if char in "═║╔╗╚╝╠╣╦╩╬" else 0.65
                if left:
                    drawing.add(Line(x, cy, cx, cy, strokeColor=line_color, strokeWidth=stroke))
                if right:
                    drawing.add(Line(cx, cy, x + cell_w * scale, cy, strokeColor=line_color, strokeWidth=stroke))
                if up:
                    drawing.add(Line(cx, cy, cx, y + cell_h * scale, strokeColor=line_color, strokeWidth=stroke))
                if down:
                    drawing.add(Line(cx, y, cx, cy, strokeColor=line_color, strokeWidth=stroke))
                col += 1
                continue
            if char in "/╱\\╲":
                if char in "/╱":
                    drawing.add(Line(x, y, x + cell_w * scale, y + cell_h * scale, strokeColor=line_color, strokeWidth=0.9))
                else:
                    drawing.add(Line(x, y + cell_h * scale, x + cell_w * scale, y, strokeColor=line_color, strokeWidth=0.9))
                col += 1
                continue
            if char in "_‾":
                yy = y + (2 if char == "_" else cell_h - 2) * scale
                drawing.add(Line(x, yy, x + cell_w * scale, yy, strokeColor=line_color, strokeWidth=0.8))
                col += 1
                continue
            if char in "█▓▃▁":
                fraction = {"█": 1.0, "▓": .78, "▃": .42, "▁": .2}[char]
                drawing.add(Rect(x + .5, y, cell_w * scale - 1, cell_h * scale * fraction, fillColor=mark_color, strokeColor=None))
                col += 1
                continue
            if char == "●":
                drawing.add(Circle(x + cell_w * scale / 2, y + cell_h * scale / 2, 2.2 * scale, fillColor=BLUE, strokeColor=None))
                col += 1
                continue
            if char in "▲▼▶◀":
                cx, cy = x + cell_w * scale / 2, y + cell_h * scale / 2
                r = 3 * scale
                points = {
                    "▲": [cx-r, cy-r, cx+r, cy-r, cx, cy+r],
                    "▼": [cx-r, cy+r, cx+r, cy+r, cx, cy-r],
                    "▶": [cx-r, cy-r, cx-r, cy+r, cx+r, cy],
                    "◀": [cx+r, cy-r, cx+r, cy+r, cx-r, cy],
                }[char]
                drawing.add(Polygon(points, fillColor=BLUE, strokeColor=None))
                col += 1
                continue
            if char.isspace():
                col += 1
                continue
            end = col + 1
            while end < len(raw) and raw[end] not in STRUCTURAL_MARKERS and raw[end] not in "/\\_" and not raw[end].isspace():
                end += 1
            label = raw[col:end]
            drawing.add(String(x, y + 1.5 * scale, label, fontName="DejaVuMono", fontSize=font_size, fillColor=INK))
            col = end
    frame = Table([[drawing]], colWidths=[CONTENT_W], hAlign="CENTER")
    frame.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),
        ("BOX", (0, 0), (-1, -1), 0.55, GRID),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return frame


def render_code_block(lines: list[str], st, declared_type=None):
    joined = "\n".join(lines)
    if declared_type == "table":
        rows = table_rows(lines) or aligned_table_rows(lines)
        return "semantic-table", semantic_table_flowable(rows, st)
    if declared_type == "callout":
        return "styled-callout", callout_flowable(lines, st)
    if declared_type == "formula":
        return "typeset-formula", formula_flowable(lines, st)
    if declared_type in {"flow", "plot", "timeline"}:
        return f"vector-{declared_type}", vector_diagram_flowable(lines)
    rows = table_rows(lines)
    if rows is not None and any(char in joined for char in "┼╬"):
        return "semantic-table", semantic_table_flowable(rows, st)
    if any(char in joined for char in STRUCTURAL_MARKERS):
        outer_box = any(char in joined for char in "┌╔") and any(char in joined for char in "┘╝")
        if outer_box and rows is None and not any(char in joined for char in "▶◀▲▼█▓▃▁╱╲"):
            return "styled-callout", callout_flowable(lines, st)
        return "vector-diagram", vector_diagram_flowable(lines)
    if looks_like_aligned_table(lines):
        return "semantic-table", semantic_table_flowable(aligned_table_rows(lines), st)
    return "typeset-formula", formula_flowable(lines, st)


def markdown_story(path: Path, st, audit_rows=None):
    lines = path.read_text(encoding="utf-8").splitlines()
    story = []
    paragraph = []
    in_code = False
    code_lines = []
    code_index = 0
    code_start = None
    inserted = set()
    insert_specs = VISUAL_INSERTS.get(path.name, [])
    declared_types = DECK_BLOCK_TYPES.get(path.name) if path.parent == DECK else None

    def flush_paragraph():
        if paragraph:
            value = " ".join(part.strip() for part in paragraph)
            value = value.replace(
                "Diagrams are ASCII so they render anywhere.",
                "Original ASCII diagrams are retained as source evidence, with vector figures inserted beside the relevant explanations.",
            )
            story.append(Paragraph(inline_markup(value), st["body"]))
            paragraph.clear()

    def maybe_insert(heading: str):
        for needle, asset, caption in insert_specs:
            key = (needle, asset)
            if key not in inserted and needle.lower() in heading.lower():
                story.extend(visual_flowables(asset, caption, st))
                inserted.add(key)

    for line_number, line in enumerate(lines, 1):
        if line.strip() == "---" or re.match(r"^(Next:|End of the notes)", line):
            flush_paragraph()
            continue
        if line.startswith("```"):
            flush_paragraph()
            if in_code:
                code_index += 1
                declared_type = None
                if declared_types is not None:
                    declared_type = declared_types[code_index - 1]
                renderer, flowable = render_code_block(code_lines, st, declared_type)
                story.append(flowable)
                if audit_rows is not None:
                    audit_rows.append({
                        "source_file": path.relative_to(REPO).as_posix(),
                        "block_index": code_index,
                        "start_line": code_start,
                        "end_line": line_number,
                        "declared_type": declared_type or "heuristic",
                        "renderer": renderer,
                        "ascii_structural_replaced": "yes",
                    })
                code_lines = []
                in_code = False
            else:
                in_code = True
                code_start = line_number
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line.strip():
            flush_paragraph()
            continue
        heading = re.match(r"^(#{1,3})\s+(.*)$", line)
        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            value = heading.group(2)
            story.append(Paragraph(inline_markup(value), st[f"h{level}"]))
            maybe_insert(value)
            continue
        bullet = re.match(r"^\s*[-*]\s+(.*)$", line)
        if bullet:
            flush_paragraph()
            story.append(Paragraph("• " + inline_markup(bullet.group(1)), st["bullet"]))
            continue
        paragraph.append(line)
    flush_paragraph()
    if in_code:
        raise ValueError(f"unclosed code fence in {path}")
    if declared_types is not None and code_index != len(declared_types):
        raise ValueError(
            f"classification count mismatch for {path}: "
            f"found {code_index}, mapped {len(declared_types)}"
        )
    return story


def page_decorator(source_label: str):
    def draw(canvas, doc):
        canvas.saveState()
        canvas.setFont("DejaVu", 7.5)
        canvas.setFillColor(MUTED)
        canvas.drawString(LEFT, PAGE_H - 11 * mm, "MAS2001 visual edition")
        canvas.drawRightString(PAGE_W - RIGHT, PAGE_H - 11 * mm, source_label)
        canvas.setStrokeColor(GRID)
        canvas.line(LEFT, PAGE_H - 13 * mm, PAGE_W - RIGHT, PAGE_H - 13 * mm)
        canvas.line(LEFT, 12 * mm, PAGE_W - RIGHT, 12 * mm)
        canvas.drawString(LEFT, 8 * mm, "generated from the audited Markdown source")
        canvas.drawRightString(PAGE_W - RIGHT, 8 * mm, f"page {doc.page}")
        canvas.restoreState()
    return draw


def make_doc(path: Path, source_label: str):
    return SimpleDocTemplate(
        str(path), pagesize=A4, rightMargin=RIGHT, leftMargin=LEFT,
        topMargin=TOP, bottomMargin=BOTTOM, title=source_label,
        author="MAS2001 visual notes", subject="Probability and statistics study notes",
    )


def individual_pdf(source: Path, output_dir: Path, st, audit_rows):
    out = output_dir / f"{source.stem}-visual.pdf"
    story = markdown_story(source, st, audit_rows)
    doc = make_doc(out, source.name)
    decorate = page_decorator(source.name)
    doc.build(story, onFirstPage=decorate, onLaterPages=decorate)
    return out


def combined_pdf(sources: list[Path], output_dir: Path, filename: str, edition_title: str, st):
    out = output_dir / filename
    story = [
        Spacer(1, 45 * mm),
        Paragraph("MAS2001 Probability and Statistics", st["cover"]),
        Paragraph(edition_title, st["cover"]),
        Spacer(1, 8 * mm),
        Paragraph("Audited Markdown content with topic diagrams, semantic tables, vectorized source drawings, exact formulas, and worked examples.", st["cover_sub"]),
        Spacer(1, 12 * mm),
        Paragraph("Contents", st["h2"]),
    ]
    for index, source in enumerate(sources):
        first = source.read_text(encoding="utf-8").splitlines()[0].lstrip("# ")
        story.append(Paragraph(f"{index:02d}. {inline_markup(first)}", st["body"]))
    story.append(PageBreak())
    for index, source in enumerate(sources):
        if index:
            story.append(PageBreak())
        story.extend(markdown_story(source, st))
    doc = make_doc(out, edition_title.lower())
    decorate = page_decorator(edition_title.lower())
    doc.build(story, onFirstPage=decorate, onLaterPages=decorate)
    return out


def write_conversion_ledger(rows):
    CONVERSION_LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with CONVERSION_LEDGER.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--individual-only", action="store_true")
    args = parser.parse_args()
    register_fonts()
    st = styles()
    NOTES_OUTPUT.mkdir(parents=True, exist_ok=True)
    DECK_OUTPUT.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(parents=True, exist_ok=True)
    notes = sorted(NOTES.glob("*.md"))
    deck_files = sorted(DECK.glob("*.md"))
    audit_rows = []
    outputs = [individual_pdf(note, NOTES_OUTPUT, st, audit_rows) for note in notes]
    outputs.extend(individual_pdf(source, DECK_OUTPUT, st, audit_rows) for source in deck_files)
    if not args.individual_only:
        outputs.append(combined_pdf(notes, NOTES_OUTPUT, "MAS2001-visual-notes-complete.pdf", "Illustrated study notes", st))
        outputs.append(combined_pdf(deck_files, DECK_OUTPUT, "MAS2001-visual-deck-complete.pdf", "Illustrated reference deck", st))
    write_conversion_ledger(audit_rows)
    for output in outputs:
        print(output)


if __name__ == "__main__":
    main()
