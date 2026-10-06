"""One-page binder sheet for the CED interview. Usage: python3 build_sheet.py out.pdf"""
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pathlib
src = pathlib.Path(__file__).with_name("build_pdf.py").read_text()
FONT_DIR = [l.split("=",1)[1].strip().strip('"\'') for l in src.splitlines() if l.startswith("FONT_DIR")][0]
for n, f in [("B", "LiberationSans-Regular.ttf"), ("BB", "LiberationSans-Bold.ttf"), ("BI", "LiberationSans-Italic.ttf")]:
    pdfmetrics.registerFont(TTFont(n, f"{FONT_DIR}/{f}"))
pdfmetrics.registerFontFamily("B", normal="B", bold="BB", italic="BI", boldItalic="BB")
H = ParagraphStyle("h", fontName="BB", fontSize=15, leading=19, spaceAfter=4)
S = ParagraphStyle("s", fontName="BB", fontSize=11.5, leading=15, spaceBefore=8, spaceAfter=3)
Q = ParagraphStyle("q", fontName="B", fontSize=11.5, leading=15, leftIndent=16, firstLineIndent=-16, spaceAfter=5)
T = ParagraphStyle("t", fontName="B", fontSize=10, leading=13, spaceAfter=2)
I = ParagraphStyle("i", fontName="BI", fontSize=9.5, leading=12, leftIndent=16, spaceAfter=5, textColor="#444444")
story = [
 Paragraph("CED Management Trainee: questions for Chris", H),
 Paragraph("Tue 6 Oct, 12:00 · 3838 Imperial Way, Ste 600A, Stockton", T),
 Paragraph("My 5 questions", S),
 Paragraph("1.&nbsp;&nbsp;“How did you get to where you are, running this branch? Did you start in the trainee program?”", Q),
 Paragraph("Listen. Ask a follow-up about his path. This is the chair you want.", I),
 Paragraph("2.&nbsp;&nbsp;“What’s the biggest opportunity, or the biggest challenge, for this branch right now?”", Q),
 Paragraph("Owner mindset. Connect your experience to whatever he says.", I),
 Paragraph("3.&nbsp;&nbsp;“What separates the trainees who earn their own branch from the ones who don’t?”", Q),
 Paragraph("Then: “That’s what I want to be,” plus one real example.", I),
 Paragraph("4.&nbsp;&nbsp;“If you hire me, what would I have done in my first year that makes you say it was a great decision?”", Q),
 Paragraph("Write his answer down. That’s your scorecard.", I),
 Paragraph("5.&nbsp;&nbsp;“Is there anything about my background that would make you hesitate to recommend me?”", Q),
 Paragraph("Answer calmly (below). Then: “What’s the next step?”", I),
 Paragraph("Backups: Stockton or Fresno during training? · Which rotation do trainees start in?", T),
 Paragraph("If he names a concern", S),
 Paragraph("<b>No electrical experience:</b> “The program says none is needed, and I’ve already done warehouse, inventory, and counter-style selling. I’ll outwork anyone learning the product.”", T),
 Paragraph("<b>Will you stay?</b> “I’m looking for a career, not a stepping stone. The reason I want this program is to run a branch.”", T),
 Paragraph("<b>Relocation:</b> “I’m ready to move wherever CED needs me.”", T),
 Paragraph("<b>No management experience:</b> “That’s what the program is for. I’ve captained two varsity teams, trained new hires, and ran a committee.”", T),
 Paragraph("My 3 points", S),
 Paragraph("1) I want to run a branch: entrepreneurship degree, minor in management. 2) I’ve done the hands-on parts: warehouse, inventory, quotes, trucks, face-to-face selling. 3) Competitive, coachable, will relocate.", T),
 Paragraph("My numbers", S),
 Paragraph("500–2,000 people/day · 30+ conversations/hour · 116% growth · 8 seasons · 120-acre yard · 8M+ views · 252 sales, no ad budget", T),
 Paragraph("Notes", S),
]
for _ in range(5):
    story += [Spacer(1, 18), HRFlowable(width="100%", thickness=0.6, color="#888888")]
SimpleDocTemplate(sys.argv[1], pagesize=letter, leftMargin=0.7*inch, rightMargin=0.7*inch, topMargin=0.55*inch, bottomMargin=0.5*inch).build(story)
