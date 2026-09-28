"""Render the same resume / cover-letter markdown dialect as build_resume.js
straight to a text-based PDF (LibreOffice can't open files in this sandbox).

Usage: python3 build_pdf.py in.md out.pdf [--letter]
"""
import html
import re
import sys
from pathlib import Path

from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import HRFlowable, ListFlowable, ListItem, Paragraph, SimpleDocTemplate, Spacer

FONT_DIR = "/usr/share/fonts/truetype/liberation"
for name, file in [("Body", "LiberationSans-Regular.ttf"), ("Body-Bold", "LiberationSans-Bold.ttf"),
                   ("Body-Italic", "LiberationSans-Italic.ttf"), ("Body-BoldItalic", "LiberationSans-BoldItalic.ttf")]:
    pdfmetrics.registerFont(TTFont(name, f"{FONT_DIR}/{file}"))
pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold", italic="Body-Italic", boldItalic="Body-BoldItalic")

in_path, out_path = sys.argv[1], sys.argv[2]
is_letter = "--letter" in sys.argv
root = Path(__file__).resolve().parent.parent

src = re.sub(r"<!--.*?-->", "", Path(in_path).read_text(), flags=re.S)
private = root / "profile" / "private.local.md"
if private.exists():
    m = re.search(r"- Phone:\s*(.+)", private.read_text())
    if m:
        src = src.replace("{{PHONE}}", m.group(1).strip())
leftover = re.search(r"\{\{[A-Z]+\}\}|\[CONFIRM[^\]]*\]", src)
if leftover:
    sys.exit(f"Unresolved placeholder in {in_path}: {leftover.group(0)}")

size = 10
base = ParagraphStyle("base", fontName="Body", fontSize=size, leading=size * 1.18, alignment=TA_LEFT)
name_style = ParagraphStyle("name", parent=base, fontName="Body-Bold", fontSize=16, leading=20,
                            alignment=TA_LEFT if is_letter else TA_CENTER, spaceAfter=2)
contact = ParagraphStyle("contact", parent=base, alignment=TA_CENTER, spaceAfter=1)
heading = ParagraphStyle("heading", parent=base, fontName="Body-Bold", fontSize=11, leading=13, spaceBefore=5, spaceAfter=1)
org = ParagraphStyle("org", parent=base, fontName="Body-Bold", spaceBefore=3)
title = ParagraphStyle("title", parent=base, fontName="Body-Italic", spaceAfter=1)
para = ParagraphStyle("para", parent=base, spaceAfter=3 if not is_letter else 8)


def inline(text):
    text = html.escape(text, quote=False)
    return re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)


story, bullets, seen_section = [], [], False


def flush():
    global bullets
    if bullets:
        story.append(ListFlowable(
            [ListItem(Paragraph(inline(b), base), leftIndent=12) for b in bullets],
            bulletType="bullet", start="•", leftIndent=12, bulletFontName="Body", bulletFontSize=size))
        bullets = []


for raw in src.splitlines():
    line = raw.rstrip()
    if not line.strip():
        continue
    if line.startswith("- "):
        bullets.append(line[2:])
        continue
    flush()
    if line.startswith("# "):
        story.append(Paragraph(inline(line[2:]), name_style))
    elif line.startswith("## "):
        seen_section = True
        story.append(Paragraph(inline(line[3:].upper()), heading))
        story.append(HRFlowable(width="100%", thickness=0.6, color="#444444", spaceBefore=0, spaceAfter=3))
    elif not seen_section and not is_letter:
        story.append(Paragraph(inline(line), contact))
    elif line.startswith("### "):
        story.append(Paragraph(inline(line[4:]), org))
    elif re.fullmatch(r"\*\*[^*]+\*\*", line):
        story.append(Paragraph(inline(line[2:-2]), title))
    else:
        story.append(Paragraph(inline(line), para))
flush()

margins = dict(topMargin=0.75 * inch, bottomMargin=0.75 * inch, leftMargin=0.875 * inch, rightMargin=0.875 * inch) \
    if is_letter else dict(topMargin=0.45 * inch, bottomMargin=0.45 * inch, leftMargin=0.6 * inch, rightMargin=0.6 * inch)
doc = SimpleDocTemplate(out_path, pagesize=LETTER, title=Path(out_path).stem, author="Ethan Santillan", **margins)
doc.build(story)
print(f"wrote {out_path}")
