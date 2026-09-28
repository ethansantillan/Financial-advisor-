"""Extract a PDF's text the way an ATS would and flag problems.

Usage: python3 check_pdf.py file.pdf [--letter]
Fails if the resume runs past one page, if a standard heading is missing,
or if the text comes out letter-spaced (e.g. "E T H A N").
"""
import re
import sys

import pypdf

path = sys.argv[1]
is_letter = "--letter" in sys.argv
reader = pypdf.PdfReader(path)
text = "\n".join(p.extract_text() or "" for p in reader.pages)
problems = []
if not is_letter and len(reader.pages) != 1:
    problems.append(f"{len(reader.pages)} pages (want 1)")
if re.search(r"\b(?:[A-Z] ){4,}[A-Z]\b", text):
    problems.append("letter-spaced text (ATS will not read it as words)")
if not is_letter:
    for h in ("SUMMARY", "EXPERIENCE", "EDUCATION", "SKILLS"):
        if h not in text:
            problems.append(f"missing heading {h}")
if "santill" not in text.lower():
    problems.append("name not found in extracted text")
words = len(text.split())
status = "OK" if not problems else "PROBLEMS: " + "; ".join(problems)
print(f"{path}: {len(reader.pages)} page(s), {words} words, {status}")
sys.exit(1 if problems else 0)
