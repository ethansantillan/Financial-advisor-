// Build an ATS-safe, single-column resume or cover letter .docx from a small
// markdown dialect:
//   # Name                 -> name line
//   (lines until first ##) -> contact lines
//   ## Heading             -> section heading
//   ### Org — Place        -> bold line
//   **Title | Dates**      -> italic line
//   - text                 -> bullet
//   anything else          -> paragraph
// {{PHONE}} is filled from profile/private.local.md so the number never lands in git.
// Usage: node build_resume.js in.md out.docx [--letter]
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, LevelFormat, BorderStyle,
} = require("docx");

const [, , inPath, outPath, ...flags] = process.argv;
const isLetter = flags.includes("--letter");
const root = path.resolve(__dirname, "..");

function privateValue(key) {
  const p = path.join(root, "profile", "private.local.md");
  if (!fs.existsSync(p)) return null;
  const m = fs.readFileSync(p, "utf8").match(new RegExp(`- ${key}:\\s*(.+)`));
  return m ? m[1].trim() : null;
}

let src = fs.readFileSync(inPath, "utf8").replace(/<!--[\s\S]*?-->/g, "");
const phone = privateValue("Phone");
if (phone) src = src.replace(/\{\{PHONE\}\}/g, phone);
const leftover = src.match(/\{\{[A-Z]+\}\}|\[CONFIRM[^\]]*\]/);
if (leftover) {
  console.error(`Unresolved placeholder in ${inPath}: ${leftover[0]}`);
  process.exit(1);
}

const FONT = "Arial";
const BODY = 20; // half-points: 10pt
const run = (text, opts = {}) => new TextRun({ text, font: FONT, size: BODY, ...opts });

// Inline **bold** inside a line.
function inline(text, base = {}) {
  return text.split(/(\*\*[^*]+\*\*)/).filter(Boolean).map((t) =>
    t.startsWith("**") ? run(t.slice(2, -2), { ...base, bold: true }) : run(t, base));
}

const children = [];
let seenSection = false;
let lastWasName = false;
for (const raw of src.split("\n")) {
  const line = raw.trimEnd();
  if (!line.trim()) continue;
  if (line.startsWith("# ")) {
    children.push(new Paragraph({
      alignment: isLetter ? AlignmentType.LEFT : AlignmentType.CENTER,
      spacing: { after: 40 },
      children: [run(line.slice(2), { bold: true, size: 32 })],
    }));
    lastWasName = true;
    continue;
  }
  if (line.startsWith("## ")) {
    seenSection = true;
    children.push(new Paragraph({
      spacing: { before: 100, after: 40 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "444444", space: 1 } },
      children: [run(line.slice(3).toUpperCase(), { bold: true, size: 22 })],
    }));
    continue;
  }
  if (!seenSection && !isLetter) {
    // contact lines
    children.push(new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { after: 20 }, children: inline(line),
    }));
    continue;
  }
  if (line.startsWith("### ")) {
    children.push(new Paragraph({
      spacing: { before: 60, after: 0 }, keepNext: true,
      children: [run(line.slice(4), { bold: true })],
    }));
    continue;
  }
  if (/^\*\*[^*]+\*\*$/.test(line)) {
    children.push(new Paragraph({
      spacing: { before: 0, after: 30 }, keepNext: true,
      children: [run(line.slice(2, -2), { italics: true })],
    }));
    continue;
  }
  if (line.startsWith("- ")) {
    children.push(new Paragraph({
      numbering: { reference: "bullets", level: 0 },
      spacing: { after: 20 },
      children: inline(line.slice(2)),
    }));
    continue;
  }
  children.push(new Paragraph({
    spacing: { after: isLetter ? 160 : 40 },
    alignment: AlignmentType.LEFT,
    children: inline(line),
  }));
  lastWasName = false;
}

const doc = new Document({
  creator: "Ethan Santillan",
  title: path.basename(outPath, ".docx"),
  styles: { default: { document: { run: { font: FONT, size: BODY } } } },
  numbering: {
    config: [{
      reference: "bullets",
      levels: [{
        level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 300, hanging: 200 } } },
      }],
    }],
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 }, // US Letter
        margin: isLetter
          ? { top: 1080, bottom: 1080, left: 1260, right: 1260 }
          : { top: 650, bottom: 650, left: 860, right: 860 },
      },
    },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(outPath, buf);
  console.log(`wrote ${outPath}`);
});
