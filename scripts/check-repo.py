#!/usr/bin/env python3
"""Pre-commit mechanical guardrails for Product-Owner repo.

Checks staged files (or all tracked files with --all):
1. Zero .docx binaries committed into the repository.
2. Obsidian `![[assets/...]]` embeds resolve to existing files, and indented
   bullet-attached embeds are preceded by two trailing spaces (`  `) for
   Obsidian Strict Line Breaks.
3. Non-Wayfinding tickets under `.scratch/*/issues/*.md` use canonical triage
   roles for `**Status:**` and omit Windows drive paths / `%TEMP%` above
   `## Comments`.
4. Schoolvoice specs, presenter notes, and active `.scratch/` spec/ticket docs
   avoid `_Avoid_` synonyms declared in `Schoolvoice/GLOSSARY.md`.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHOOLVOICE_GLOSSARY = ROOT / "Schoolvoice" / "GLOSSARY.md"
VALID_TRIAGE_STATUSES = {
    "needs-triage",
    "needs-info",
    "ready-for-agent",
    "ready-for-human",
    "wontfix",
}
EMBED_RE = re.compile(r"!\[\[(assets/[^|\]]+)(?:\|[^\]]+)?\]\]")
STATUS_RE = re.compile(r"^\*{0,2}Status:\*{0,2}\s*([a-zA-Z0-9_-]+)\s*$", re.MULTILINE)
WINDOWS_PATH_RE = re.compile(r"(?:[A-Za-z]:\\|%TEMP%)")
AVOID_LINE_RE = re.compile(r"^_Avoid_:\s*(.+)$", re.MULTILINE)


def get_target_files(check_all: bool) -> list[Path]:
    cmd = (
        ["git", "ls-files", "-z"]
        if check_all
        else ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM", "-z"]
    )
    out = subprocess.check_output(cmd, cwd=ROOT)
    paths = [p for p in out.decode("utf-8", errors="replace").split("\0") if p]
    return [ROOT / p for p in paths if (ROOT / p).is_file()]


CANONICAL_TERM_RE = re.compile(r"^\*\*([^*]+)\*\*:", re.MULTILINE)


def load_schoolvoice_avoided_terms() -> list[str]:
    if not SCHOOLVOICE_GLOSSARY.is_file():
        return []
    text = SCHOOLVOICE_GLOSSARY.read_text(encoding="utf-8", errors="replace")
    canonical: set[str] = set()
    for m in CANONICAL_TERM_RE.finditer(text):
        base = re.sub(r"\([^)]*\)", "", m.group(1)).strip().lower()
        if base:
            canonical.add(base)

    terms: list[str] = []
    for m in AVOID_LINE_RE.finditer(text):
        for raw_term in m.group(1).split(","):
            term = re.sub(r"\([^)]*\)", "", raw_term).strip()
            if not term or term.lower().startswith(("conflating ", "which ")):
                continue
            # Never ban a term that is itself a canonical glossary entry
            if term.lower() in canonical:
                continue
            terms.append(term)
    return sorted(set(terms), key=len, reverse=True)


def check_docx_quarantine(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        if path.suffix.lower() == ".docx":
            rel = path.relative_to(ROOT).as_posix()
            errors.append(f"[docx-quarantine] Staged .docx binary forbidden in repo: {rel}")
    return errors


def check_obsidian_embeds(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        if path.suffix.lower() != ".md":
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(".scratch/"):
            continue
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        for idx, line in enumerate(lines, start=1):
            for match in EMBED_RE.finditer(line):
                asset_rel = match.group(1)
                target = path.parent / asset_rel
                if not target.is_file():
                    errors.append(f"[obsidian-embed] {rel}:{idx} missing asset: {asset_rel}")
                stripped = line.lstrip(" ")
                if stripped.startswith("![[assets/") and len(line) > len(stripped):
                    if idx > 1 and lines[idx - 2].strip() and not lines[idx - 2].endswith("  "):
                        errors.append(
                            f"[obsidian-hard-break] {rel}:{idx - 1} missing trailing two spaces before bullet embed on line {idx}"
                        )
    return errors


def check_ticket_hygiene(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        if not re.match(r"^\.scratch/[^/]+/issues/[^/]+\.md$", rel):
            continue
        feature_dir = path.parent.parent
        is_wayfinding = (feature_dir / "map.md").is_file()
        text = path.read_text(encoding="utf-8", errors="replace")
        body = text.split("\n## Comments", 1)[0]

        if not is_wayfinding:
            m = STATUS_RE.search(body)
            if m and m.group(1) not in VALID_TRIAGE_STATUSES:
                errors.append(
                    f"[ticket-status] {rel}: invalid Status '{m.group(1)}' (expected one of {sorted(VALID_TRIAGE_STATUSES)})"
                )
            if WINDOWS_PATH_RE.search(body):
                errors.append(
                    f"[ticket-path] {rel}: Windows drive path or %TEMP% found in ticket body (keep implementation logs under ## Comments)"
                )
    return errors


def is_glossary_checked_doc(rel: str) -> bool:
    if not rel.endswith(".md"):
        return False
    if rel.endswith("GLOSSARY.md") or "(Visual).md" in rel:
        return False
    return (
        rel.startswith(".scratch/message-translation-visual-spec/")
        or "Presenter Notes.md" in rel
        or rel.startswith("Schoolvoice/docs/01-prd/")
    )


def check_glossary_avoided_terms(files: list[Path]) -> list[str]:
    avoided = load_schoolvoice_avoided_terms()
    if not avoided:
        return []
    patterns = [(t, re.compile(rf"\b{re.escape(t)}\b", re.IGNORECASE)) for t in avoided]
    errors: list[str] = []
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        if not is_glossary_checked_doc(rel):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        body = text.split("\n## Comments", 1)[0]
        for idx, line in enumerate(body.splitlines(), start=1):
            # Allow explicit negation quotes documenting the glossary boundary itself
            if "_Avoid_" in line or "excluding" in line.lower():
                continue
            for term, pat in patterns:
                if pat.search(line):
                    errors.append(
                        f"[glossary-avoid] {rel}:{idx} uses avoided Schoolvoice term '{term}' (see Schoolvoice/GLOSSARY.md)"
                    )
    return errors


def main() -> int:
    check_all = "--all" in sys.argv[1:]
    files = get_target_files(check_all)
    errors = (
        check_docx_quarantine(files)
        + check_obsidian_embeds(files)
        + check_ticket_hygiene(files)
        + check_glossary_avoided_terms(files)
    )
    if errors:
        print("Repo pre-commit check FAILED:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1
    print(f"Repo pre-commit check PASSED ({len(files)} file(s) checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
