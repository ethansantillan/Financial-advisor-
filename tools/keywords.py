"""Keyword coverage of a resume against the job's keyword list.

Reads the "## Exact keywords and phrases" line in jd.md (items split on " · "),
then reports which appear in the master resume (before) and the tailored
resume (after). Matching is case-insensitive and ignores hyphens.
Usage: python3 keywords.py jobs/<packet>
"""
import re
import sys
from pathlib import Path

packet = Path(sys.argv[1])
root = Path(__file__).resolve().parent.parent
jd = (packet / "jd.md").read_text()
m = re.search(r"## Exact keywords and phrases\n+(.+)", jd)
keywords = [k.strip() for k in m.group(1).split("·") if k.strip()]


def norm(s):
    return re.sub(r"[-–]", " ", s.lower())


def covered(text):
    t = norm(re.sub(r"<!--.*?-->", "", text, flags=re.S))
    return [k for k in keywords if norm(k) in t]


before = covered((root / "profile" / "master-resume.md").read_text())
after = covered((packet / "resume.md").read_text())
pct = lambda xs: round(100 * len(xs) / len(keywords))
print(f"before {pct(before)}% ({len(before)}/{len(keywords)})  after {pct(after)}% ({len(after)}/{len(keywords)})")
print("still missing:", ", ".join(k for k in keywords if k not in after) or "none")
