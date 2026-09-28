#!/usr/bin/env bash
# Build .docx and text-based .pdf for resume.md / cover-letter.md in a folder,
# then check each PDF by extracting its text.
# Usage: tools/build.sh jobs/<packet-folder> [more folders...]
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
status=0
for dir in "$@"; do
  for md in "$dir"/resume.md "$dir"/cover-letter.md; do
    [ -f "$md" ] || continue
    base="${md%.md}"
    flag=""; [[ "$md" == *cover-letter.md ]] && flag="--letter"
    node "$here/build_resume.js" "$md" "$base.docx" $flag >/dev/null
    python3 "$here/build_pdf.py" "$md" "$base.pdf" $flag >/dev/null
    python3 "$here/check_pdf.py" "$base.pdf" $flag || status=1
  done
done
exit $status
