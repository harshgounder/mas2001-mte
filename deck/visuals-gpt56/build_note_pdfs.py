#!/usr/bin/env python3
"""Build illustrated PDF editions of every MAS2001 note Markdown file."""

from __future__ import annotations

import argparse
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
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)
from svglib.svglib import svg2rlg


REPO = Path(__file__).resolve().parents[2]
NOTES = REPO / "deck" / "notes"
VISUALS = REPO / "deck" / "visuals-gpt56" / "assets"
OUTPUT = REPO / "output" / "pdf" / "visual-notes"
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


VISUAL_INSERTS = {
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
            spaceBefore=4, spaceAfter=16,
        ),
        "h2": ParagraphStyle(
            "H2", parent=base["Heading2"], fontName="DejaVu-Bold", fontSize=14,
            leading=18, textColor=INK, borderColor=CYAN, borderWidth=0,
            borderPadding=(0, 0, 5, 0), spaceBefore=14, spaceAfter=7,
        ),
        "h3": ParagraphStyle(
            "H3", parent=base["Heading3"], fontName="DejaVu-Bold", fontSize=11.5,
            leading=15, textColor=PURPLE, spaceBefore=10, spaceAfter=5,
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


def code_flowable(lines: list[str]):
    text_value = "\n".join(lines).rstrip()
    longest = max((len(line) for line in lines), default=1)
    font_size = max(4.5, min(7.2, (CONTENT_W - 12) / (longest * 0.62)))
    style = ParagraphStyle(
        "CodeBlock", fontName="DejaVuMono", fontSize=font_size,
        leading=font_size * 1.35, textColor=INK, backColor=SOFT,
        borderColor=GRID, borderWidth=0.6, borderPadding=7,
        leftIndent=0, rightIndent=0, spaceBefore=4, spaceAfter=8,
    )
    return Preformatted(text_value, style, maxLineLength=180)


def markdown_story(path: Path, st):
    lines = path.read_text(encoding="utf-8").splitlines()
    story = []
    paragraph = []
    in_code = False
    code_lines = []
    inserted = set()
    insert_specs = VISUAL_INSERTS.get(path.name, [])

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

    for line in lines:
        if line.strip() == "---" or re.match(r"^(Next:|End of the notes)", line):
            flush_paragraph()
            continue
        if line.startswith("```"):
            flush_paragraph()
            if in_code:
                story.append(code_flowable(code_lines))
                code_lines = []
                in_code = False
            else:
                in_code = True
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
    return story


def page_decorator(source_label: str):
    def draw(canvas, doc):
        canvas.saveState()
        canvas.setFont("DejaVu", 7.5)
        canvas.setFillColor(MUTED)
        canvas.drawString(LEFT, PAGE_H - 11 * mm, "MAS2001 visual notes")
        canvas.drawRightString(PAGE_W - RIGHT, PAGE_H - 11 * mm, source_label)
        canvas.setStrokeColor(GRID)
        canvas.line(LEFT, PAGE_H - 13 * mm, PAGE_W - RIGHT, PAGE_H - 13 * mm)
        canvas.line(LEFT, 12 * mm, PAGE_W - RIGHT, 12 * mm)
        canvas.drawString(LEFT, 8 * mm, "generated from the audited Markdown notes")
        canvas.drawRightString(PAGE_W - RIGHT, 8 * mm, f"page {doc.page}")
        canvas.restoreState()
    return draw


def make_doc(path: Path, source_label: str):
    return SimpleDocTemplate(
        str(path), pagesize=A4, rightMargin=RIGHT, leftMargin=LEFT,
        topMargin=TOP, bottomMargin=BOTTOM, title=source_label,
        author="MAS2001 visual notes", subject="Probability and statistics study notes",
    )


def individual_pdf(note: Path, st):
    out = OUTPUT / f"{note.stem}-visual.pdf"
    story = markdown_story(note, st)
    doc = make_doc(out, note.name)
    decorate = page_decorator(note.name)
    doc.build(story, onFirstPage=decorate, onLaterPages=decorate)
    return out


def combined_pdf(notes: list[Path], st):
    out = OUTPUT / "MAS2001-visual-notes-complete.pdf"
    story = [
        Spacer(1, 45 * mm),
        Paragraph("MAS2001 Probability and Statistics", st["cover"]),
        Paragraph("Illustrated study notes", st["cover"]),
        Spacer(1, 8 * mm),
        Paragraph("Eleven audited Markdown notes with topic diagrams, exact formulas, worked examples, and source-preserving code panels.", st["cover_sub"]),
        Spacer(1, 12 * mm),
        Paragraph("Contents", st["h2"]),
    ]
    for index, note in enumerate(notes):
        first = note.read_text(encoding="utf-8").splitlines()[0].lstrip("# ")
        story.append(Paragraph(f"{index:02d}. {inline_markup(first)}", st["body"]))
    story.append(PageBreak())
    for index, note in enumerate(notes):
        if index:
            story.append(PageBreak())
        story.extend(markdown_story(note, st))
    doc = make_doc(out, "complete visual notes")
    decorate = page_decorator("complete visual notes")
    doc.build(story, onFirstPage=decorate, onLaterPages=decorate)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--individual-only", action="store_true")
    args = parser.parse_args()
    register_fonts()
    st = styles()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(parents=True, exist_ok=True)
    notes = sorted(NOTES.glob("*.md"))
    outputs = [individual_pdf(note, st) for note in notes]
    if not args.individual_only:
        outputs.append(combined_pdf(notes, st))
    for output in outputs:
        print(output)


if __name__ == "__main__":
    main()
