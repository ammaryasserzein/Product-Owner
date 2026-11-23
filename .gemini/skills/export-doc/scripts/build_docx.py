#!/usr/bin/env python3
"""Build executive-ready .docx files from Obsidian Markdown or JSON doc models.

Features:
- Strict ECMA-376 CT_PPr child-element ordering (zero Word/Google Docs schema glitches).
- Supports Obsidian width-constrained PNG embeds (`![[assets/img.png|width]]`),
  standard Markdown images, clickable external hyperlinks, bold/italic/code spans,
  nested bullet lists, tables, callouts, horizontal rules, and RTL/LTR modes.
- Refuses to write .docx files inside the Product-Owner git repository by default.

Usage:
  py -3 build_docx.py --markdown <input.md> <output.docx>
  py -3 build_docx.py <model.json> <output.docx>
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from PIL import Image

REPO_ROOT = Path(__file__).resolve().parents[4]

# Official ECMA-376 CT_PPr child sequence order
PPR_ORDER = [
    "pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr",
    "widowControl", "numPr", "suppressLineNumbers", "pBdr", "shd", "tabs",
    "suppressAutoHyphens", "kinsoku", "wordWrap", "overflowPunct",
    "topLinePunct", "autoSpaceDE", "autoSpaceDN", "bidi", "adjustRightInd",
    "snapToGrid", "spacing", "ind", "contextualSpacing", "mirrorIndents",
    "suppressOverlap", "jc", "textDirection", "textAlignment",
    "textboxTightWrap", "outlineLvl", "divId", "cnfStyle", "rPr", "sectPr",
    "pPrChange",
]
PPR_INDEX = {tag: idx for idx, tag in enumerate(PPR_ORDER)}

NAVY_DARK = RGBColor(0x17, 0x36, 0x5D)
NAVY_MID = RGBColor(0x1F, 0x4E, 0x78)
ACCENT_BLUE = RGBColor(0x2F, 0x55, 0x97)
BODY_INK = RGBColor(0x1F, 0x29, 0x37)
LINK_BLUE = RGBColor(0x11, 0x55, 0xCC)

INLINE_TOKEN_RE = re.compile(
    r"\[([^\]]+)\]\((https?://[^)\s]+)\)"
    r"|\*\*([^*]+)\*\*"
    r"|\*([^*]+)\*"
    r"|`([^`]+)`"
)
OBSIDIAN_EMBED_RE = re.compile(r"^\s*!\[\[([^|\]]+)(?:\|(\d+))?\]\]\s*$")
MD_IMAGE_RE = re.compile(r"^\s*!\[([^\]]*)\]\(([^)]+)\)\s*$")
BULLET_RE = re.compile(r"^(\s*)[*-]\s+(.*)$")


def insert_ppr_child(ppr: Any, elem: Any) -> None:
    local = elem.tag.split("}")[-1]
    target_idx = PPR_INDEX.get(local, len(PPR_ORDER))
    for existing in list(ppr):
        ex_local = existing.tag.split("}")[-1]
        if ex_local == local:
            ppr.remove(existing)
    for idx, child in enumerate(list(ppr)):
        child_local = child.tag.split("}")[-1]
        if PPR_INDEX.get(child_local, len(PPR_ORDER)) > target_idx:
            ppr.insert(idx, elem)
            return
    ppr.append(elem)


def set_paragraph_border_bottom(paragraph: Any, color: str = "D0D7DE", sz: str = "6") -> None:
    ppr = paragraph._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), sz)
    bottom.set(qn("w:space"), "4")
    bottom.set(qn("w:color"), color)
    pbdr.append(bottom)
    insert_ppr_child(ppr, pbdr)


def set_paragraph_shading(paragraph: Any, fill: str) -> None:
    ppr = paragraph._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    insert_ppr_child(ppr, shd)


def set_rtl(paragraph: Any) -> None:
    ppr = paragraph._p.get_or_add_pPr()
    bidi = OxmlElement("w:bidi")
    bidi.set(qn("w:val"), "1")
    insert_ppr_child(ppr, bidi)


def unescape_md(text: str) -> str:
    return re.sub(r"\\([<>\\`*_{}\[\]()#+\-.!|])", r"\1", text)


def style_run(
    run: Any,
    *,
    bold: bool = False,
    italic: bool = False,
    code: bool = False,
    color: RGBColor = BODY_INK,
    size_pt: float = 10.5,
) -> None:
    run.bold = bold
    run.italic = italic
    run.font.name = "Consolas" if code else "Aptos"
    run.font.size = Pt(size_pt - 0.5 if code else size_pt)
    run.font.color.rgb = color


def add_hyperlink(paragraph: Any, label: str, url: str, *, bold: bool = False, size_pt: float = 10.5) -> None:
    part = paragraph.part
    r_id = part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)

    new_run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    rfonts = OxmlElement("w:rFonts")
    rfonts.set(qn("w:ascii"), "Aptos")
    rfonts.set(qn("w:hAnsi"), "Aptos")
    rpr.append(rfonts)
    if bold:
        rpr.append(OxmlElement("w:b"))
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "1155CC")
    rpr.append(color)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rpr.append(u)
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), str(int(size_pt * 2)))
    rpr.append(sz)
    new_run.append(rpr)

    t = OxmlElement("w:t")
    t.set(qn("xml:space"), "preserve")
    t.text = unescape_md(label)
    new_run.append(t)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)


def add_inline_formatted_text(
    paragraph: Any,
    raw_text: str,
    *,
    base_bold: bool = False,
    base_color: RGBColor = BODY_INK,
    size_pt: float = 10.5,
) -> None:
    pos = 0
    for m in INLINE_TOKEN_RE.finditer(raw_text):
        if m.start() > pos:
            run = paragraph.add_run(unescape_md(raw_text[pos : m.start()]))
            style_run(run, bold=base_bold, color=base_color, size_pt=size_pt)
        if m.group(1) is not None and m.group(2) is not None:
            add_hyperlink(paragraph, m.group(1), m.group(2), bold=base_bold, size_pt=size_pt)
        elif m.group(3) is not None:
            inner = m.group(3)
            if "[" in inner and "](" in inner:
                add_inline_formatted_text(
                    paragraph, inner, base_bold=True, base_color=base_color, size_pt=size_pt
                )
            else:
                run = paragraph.add_run(unescape_md(inner))
                style_run(run, bold=True, color=base_color, size_pt=size_pt)
        elif m.group(4) is not None:
            run = paragraph.add_run(unescape_md(m.group(4)))
            style_run(run, bold=base_bold, italic=True, color=base_color, size_pt=size_pt)
        elif m.group(5) is not None:
            run = paragraph.add_run(unescape_md(m.group(5)))
            style_run(run, bold=base_bold, code=True, color=NAVY_MID, size_pt=size_pt)
        pos = m.end()

    if pos < len(raw_text):
        run = paragraph.add_run(unescape_md(raw_text[pos:]))
        style_run(run, bold=base_bold, color=base_color, size_pt=size_pt)


def compute_image_width_inches(img_path: Path, hint_px: int | None) -> float:
    with Image.open(img_path) as im:
        w, h = im.size
    if w >= 1200 or (hint_px is not None and hint_px >= 600):
        return 6.2
    if h >= 900 and w <= 500:
        return 2.35
    return 3.2


def add_image_block(
    doc: Document,
    img_path: Path,
    *,
    width_inches: float | None = None,
    hint_px: int | None = None,
    indent_inches: float = 0.0,
) -> None:
    if not img_path.is_file():
        raise FileNotFoundError(f"Embedded image not found: {img_path}")
    width = width_inches if width_inches is not None else compute_image_width_inches(img_path, hint_px)
    if doc.paragraphs:
        doc.paragraphs[-1].paragraph_format.keep_with_next = True
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(8)
    if indent_inches > 0:
        p.paragraph_format.left_indent = Inches(indent_inches)
    run = p.add_run()
    run.add_picture(str(img_path), width=Inches(width))


def configure_document(direction: str = "ltr") -> Document:
    doc = Document()
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.85)
        section.right_margin = Inches(0.85)
    normal = doc.styles["Normal"]
    normal.font.name = "Aptos"
    normal.font.size = Pt(10.5)
    normal.font.color.rgb = BODY_INK
    if direction == "rtl":
        normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    return doc


def build_from_markdown(md_path: Path, out_path: Path) -> None:
    doc = configure_document("ltr")
    base_dir = md_path.parent
    lines = md_path.read_text(encoding="utf-8").splitlines()
    last_indent_in = 0.0

    i = 0
    while i < len(lines):
        raw = lines[i].rstrip()
        if not raw.strip():
            i += 1
            continue

        if raw.strip() in {"---", "***", "___"}:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(8)
            set_paragraph_border_bottom(p, color="CBD5E1", sz="6")
            last_indent_in = 0.0
            i += 1
            continue

        obs_m = OBSIDIAN_EMBED_RE.match(raw)
        if obs_m:
            rel_img = obs_m.group(1).strip()
            hint = int(obs_m.group(2)) if obs_m.group(2) else None
            img_indent = last_indent_in if raw.startswith(" ") else 0.0
            add_image_block(doc, base_dir / rel_img, hint_px=hint, indent_inches=img_indent)
            i += 1
            continue

        md_img_m = MD_IMAGE_RE.match(raw)
        if md_img_m:
            rel_img = md_img_m.group(2).strip()
            img_indent = last_indent_in if raw.startswith(" ") else 0.0
            add_image_block(doc, base_dir / rel_img, indent_inches=img_indent)
            i += 1
            continue

        if raw.startswith("# "):
            heading_text = raw[2:].strip()
            if heading_text.startswith("**") and heading_text.endswith("**"):
                heading_text = heading_text[2:-2]
            p = doc.add_heading(level=1)
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(8)
            p.paragraph_format.keep_with_next = True
            add_inline_formatted_text(p, heading_text, base_bold=True, base_color=NAVY_DARK, size_pt=18.0)
            last_indent_in = 0.0
            i += 1
            continue

        if raw.startswith("## "):
            heading_text = raw[3:].strip()
            if heading_text.startswith("**") and heading_text.endswith("**"):
                heading_text = heading_text[2:-2]
            p = doc.add_heading(level=2)
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.keep_with_next = True
            add_inline_formatted_text(p, heading_text, base_bold=True, base_color=NAVY_MID, size_pt=13.5)
            last_indent_in = 0.0
            i += 1
            continue

        if raw.startswith("### "):
            heading_text = raw[4:].strip()
            p = doc.add_heading(level=3)
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_with_next = True
            add_inline_formatted_text(p, heading_text, base_bold=True, base_color=ACCENT_BLUE, size_pt=11.5)
            last_indent_in = 0.0
            i += 1
            continue

        bullet_m = BULLET_RE.match(raw)
        if bullet_m:
            lead_spaces = len(bullet_m.group(1))
            level = min(lead_spaces // 2, 3)
            text = bullet_m.group(2).strip()
            style_name = "List Bullet" if level == 0 else f"List Bullet {level + 1}"
            try:
                p = doc.add_paragraph(style=style_name)
            except KeyError:
                p = doc.add_paragraph(style="List Bullet")
                p.paragraph_format.left_indent = Inches(0.25 * (level + 1))
            p.paragraph_format.space_before = Pt(1.5)
            p.paragraph_format.space_after = Pt(3)
            add_inline_formatted_text(p, text, size_pt=10.5)
            last_indent_in = 0.25 * (level + 1)
            i += 1
            continue

        # Plain paragraph
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        add_inline_formatted_text(p, raw.strip(), size_pt=10.5)
        last_indent_in = 0.0
        i += 1

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(out_path))


def build_from_json(model_path: Path, out_path: Path) -> None:
    model = json.loads(model_path.read_text(encoding="utf-8"))
    direction = str(model.get("direction", "ltr")).lower()
    doc = configure_document(direction)

    title = model.get("title")
    if title:
        p = doc.add_heading(level=1)
        if direction == "rtl":
            set_rtl(p)
        add_inline_formatted_text(p, str(title), base_bold=True, base_color=NAVY_DARK, size_pt=18.0)

    for block in model.get("blocks", []):
        btype = block.get("type")
        if btype == "heading":
            lvl = int(block.get("level", 2))
            p = doc.add_heading(level=max(1, min(lvl, 3)))
            if direction == "rtl":
                set_rtl(p)
            p.paragraph_format.keep_with_next = True
            add_inline_formatted_text(
                p,
                str(block.get("text", "")),
                base_bold=True,
                base_color=NAVY_DARK if lvl == 1 else NAVY_MID,
                size_pt=16.0 if lvl == 1 else 13.0,
            )
        elif btype == "paragraph":
            p = doc.add_paragraph()
            if direction == "rtl":
                set_rtl(p)
            add_inline_formatted_text(p, str(block.get("text", "")))
        elif btype == "list":
            for item in block.get("items", []):
                p = doc.add_paragraph(style="List Bullet")
                if direction == "rtl":
                    set_rtl(p)
                add_inline_formatted_text(p, str(item))
        elif btype == "table":
            headers = block.get("headers", [])
            rows = block.get("rows", [])
            cols = len(headers) if headers else (len(rows[0]) if rows else 0)
            if cols:
                table = doc.add_table(rows=(1 if headers else 0) + len(rows), cols=cols)
                table.style = "Table Grid"
                r_offset = 0
                if headers:
                    for c, val in enumerate(headers):
                        cell_p = table.cell(0, c).paragraphs[0]
                        if direction == "rtl":
                            set_rtl(cell_p)
                        add_inline_formatted_text(cell_p, str(val), base_bold=True, base_color=NAVY_DARK)
                    r_offset = 1
                for r, row in enumerate(rows):
                    for c, val in enumerate(row):
                        cell_p = table.cell(r + r_offset, c).paragraphs[0]
                        if direction == "rtl":
                            set_rtl(cell_p)
                        add_inline_formatted_text(cell_p, str(val))
        elif btype == "callout":
            p = doc.add_paragraph()
            if direction == "rtl":
                set_rtl(p)
            fill = "FEF3C7" if block.get("style") == "warning" else "EFF6FF"
            set_paragraph_shading(p, fill)
            add_inline_formatted_text(p, str(block.get("text", "")))
        elif btype == "page_break":
            doc.add_page_break()
        elif btype == "image":
            img_path = Path(block["path"])
            width = float(block["width_inches"]) if "width_inches" in block else None
            add_image_block(doc, img_path, width_inches=width)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(out_path))


def guard_output_path(out_path: Path, allow_in_repo: bool) -> None:
    if allow_in_repo:
        return
    resolved_out = out_path.resolve()
    try:
        resolved_out.relative_to(REPO_ROOT.resolve())
    except ValueError:
        return
    raise SystemExit(
        f"Refusing to write .docx inside git repository ({resolved_out}). "
        "Target %TEMP% (for Google Drive upload) or OneDrive instead."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build an executive .docx from Markdown or JSON model.")
    parser.add_argument("--markdown", action="store_true", help="Treat input file as Obsidian/Markdown.")
    parser.add_argument("--allow-in-repo", action="store_true", help="Override repo .docx quarantine guard.")
    parser.add_argument("input_path", type=Path)
    parser.add_argument("output_path", type=Path)
    args = parser.parse_args()

    guard_output_path(args.output_path, args.allow_in_repo)
    if args.markdown or args.input_path.suffix.lower() == ".md":
        build_from_markdown(args.input_path, args.output_path)
    else:
        build_from_json(args.input_path, args.output_path)
    print(f"Built {args.output_path} ({args.output_path.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
