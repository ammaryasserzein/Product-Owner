#!/usr/bin/env python3
"""Deterministic OOXML & content auditor for generated .docx deliverables.

Returns JSON to stdout (`passed`, `findings`, `stats`) and exits 0 on pass, 1 on fail.

Usage:
  py -3 audit_docx.py <file.docx> [--source-md <source.md>]
"""

from __future__ import annotations

import argparse
import json
import re
import zipfile
from pathlib import Path
from lxml import etree

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"

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

LEAKED_MD_RE = re.compile(r"(!\[\[|\*\*|\\<|\\>)")
WORD_RE = re.compile(r"[\w\u0600-\u06FF\u0900-\u097F]+", re.UNICODE)


def normalize_md_words(md_path: Path) -> list[str]:
    lines = md_path.read_text(encoding="utf-8").splitlines()
    kept: list[str] = []
    for line in lines:
        s = line.strip()
        if not s or s in {"---", "***", "___"}:
            continue
        if re.match(r"^!\[\[.*\]\]$", s) or re.match(r"^!\[.*\]\(.*\)$", s):
            continue
        s = re.sub(r"^#{1,6}\s+", "", s)
        s = re.sub(r"^[*-]\s+", "", s)
        s = re.sub(r"\[([^\]]+)\]\(https?://[^)\s]+\)", r"\1", s)
        s = re.sub(r"\\([<>\\`*_{}\[\]()#+\-.!|])", r"\1", s)
        s = s.replace("**", "").replace("*", "").replace("`", "")
        kept.append(s)
    return WORD_RE.findall(" ".join(kept).lower())


def audit(docx_path: Path, source_md: Path | None = None) -> dict:
    findings: list[str] = []
    stats: dict[str, int | bool] = {}

    if not docx_path.is_file():
        return {"passed": False, "findings": [f"File not found: {docx_path}"], "stats": stats}

    try:
        zf = zipfile.ZipFile(docx_path, "r")
    except zipfile.BadZipFile:
        return {"passed": False, "findings": ["Invalid ZIP archive"], "stats": stats}

    with zf:
        names = zf.namelist()
        xml_parts = [n for n in names if n.endswith(".xml") or n.endswith(".rels")]
        parsed_parts: dict[str, etree._Element] = {}
        for part in xml_parts:
            try:
                parsed_parts[part] = etree.fromstring(zf.read(part))
            except etree.XMLSyntaxError as exc:
                findings.append(f"XML syntax error in {part}: {exc}")
        stats["xml_parts_parsed"] = len(parsed_parts)

        doc_xml = parsed_parts.get("word/document.xml")
        rels_xml = parsed_parts.get("word/_rels/document.xml.rels")
        if doc_xml is None:
            findings.append("Missing word/document.xml")
            return {"passed": False, "findings": findings, "stats": stats}

        # 1. ECMA-376 CT_PPr child ordering check
        ppr_violations = 0
        for ppr in doc_xml.findall(f".//{{{W_NS}}}pPr"):
            prev_idx = -1
            for child in ppr:
                local = child.tag.split("}")[-1]
                idx = PPR_INDEX.get(local, -1)
                if idx == -1:
                    continue
                if idx < prev_idx:
                    ppr_violations += 1
                    break
                prev_idx = idx
        stats["ppr_order_violations"] = ppr_violations
        if ppr_violations:
            findings.append(f"{ppr_violations} CT_PPr child-element ordering violation(s)")

        # 2. Relationships map (images + hyperlinks)
        rels: dict[str, tuple[str, str]] = {}
        if rels_xml is not None:
            for rel in rels_xml.findall(f"{{{REL_NS}}}Relationship"):
                rels[rel.get("Id", "")] = (rel.get("Type", ""), rel.get("Target", ""))

        blips = doc_xml.findall(f".//{{{A_NS}}}blip")
        stats["inline_images"] = len(blips)
        media_files = {n for n in names if n.startswith("word/media/")}
        stats["unique_media_files"] = len(media_files)
        for blip in blips:
            embed_id = blip.get(f"{{{R_NS}}}embed")
            if not embed_id or embed_id not in rels:
                findings.append(f"Broken image relationship: {embed_id}")
                continue
            target = "word/" + rels[embed_id][1].lstrip("/")
            if target not in media_files:
                findings.append(f"Missing media payload in archive: {target}")
            elif zf.getinfo(target).file_size == 0:
                findings.append(f"Zero-byte media payload: {target}")

        hyperlinks = doc_xml.findall(f".//{{{W_NS}}}hyperlink")
        stats["hyperlinks"] = len(hyperlinks)
        for hl in hyperlinks:
            rid = hl.get(f"{{{R_NS}}}id")
            if rid and rid not in rels:
                findings.append(f"Broken hyperlink relationship: {rid}")

        # 3. Extract visible text & check leaked Markdown tokens
        all_text = " ".join(
            t.text for t in doc_xml.findall(f".//{{{W_NS}}}t") if t.text
        )
        leaked = LEAKED_MD_RE.findall(all_text)
        stats["leaked_markdown_tokens"] = len(leaked)
        if leaked:
            findings.append(f"Leaked raw Markdown token(s) in document text: {leaked[:5]}")

        doc_words = WORD_RE.findall(all_text.lower())
        stats["word_count"] = len(doc_words)

        if source_md is not None:
            src_words = normalize_md_words(source_md)
            stats["source_word_count"] = len(src_words)
            if doc_words != src_words:
                findings.append(
                    f"Verbatim word mismatch vs {source_md.name}: docx={len(doc_words)}, source={len(src_words)}"
                )

    return {"passed": len(findings) == 0, "findings": findings, "stats": stats}


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit generated .docx for OOXML integrity and verbatim fidelity.")
    parser.add_argument("docx_path", type=Path)
    parser.add_argument("--source-md", type=Path, default=None, help="Optional source Markdown for verbatim word diff.")
    args = parser.parse_args()

    result = audit(args.docx_path, args.source_md)
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
