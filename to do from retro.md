# To-Do From Retro (2026-11-23)

Deferred environment and tooling improvements from the Message Translation visual user-stories retrospective.

## High Priority
- [ ] **Restore / relocate `export-doc` build & audit scripts (Retro #1)**
  - `.gemini/skills/export-doc/SKILL.md` currently points to missing `C:/Users/L/.gemini/config/skills/arabic-word-production/scripts/{check_environment,build_docx,audit_docx}.py`.
  - Relocate or rebuild reusable `build_docx.py` + `audit_docx.py` inside `.gemini/skills/export-doc/scripts/` (with strict ECMA-376 `CT_PPr` ordering, image/hyperlink checks, and verbatim word-diff validation).
  - Extend `export-doc/SKILL.md` to support `--en-only` and direct Google Drive upload (`application/vnd.google-apps.document`) alongside OneDrive dual-copy export.

- [ ] **Codify 2-call Figma View-seat section-slice guide (Retro #2)**
  - Create `docs/agents/figma-capture.md` and add a 1-line context pointer in root `AGENTS.md`.
  - Document the quota-safe workflow for Figma View seats (`20` MCP read calls/month): check `whoami` seat → `get_metadata` to find the tightest feature `<section>` inside large canvases → single `get_screenshot(maxDimension=16384)` → local PIL slicing → ignore raw `board-*.xml` / `board-*.png` dumps.

## Medium Priority
- [ ] **Install official Google Docs plugin (Retro #6)**
  - Add `antigravity-plugins-official/plugin/gdocs` from the Marketplace card so future sessions can read/edit team Google Docs directly without `.docx` conversion round-trips.

- [ ] **Review & commit global config repo (`C:\Users\L\.gemini\config`)**
  - Review uncommitted diffs from the Matt Pocock skills `v1.3.2` (`main@abeeaf9`) upgrade and the `AGENTS.md` / `GEMINI.md` / `english-feedback/RULE.md` consolidation, then commit when satisfied.

## Low Priority (Minor Code-Review Leftovers)
- [ ] **Empty `US Notes.md`**: Decide whether to delete the now-empty `Schoolvoice-PO/AI translated messages/US Notes.md` or reuse it for future notes.
- [ ] **Deduplicate `assets/manifest.json`**: Only if reused as a template for future features, stop repeating file-level dimensions (`width`, `height`) inside both `mappings[]` and `files[]`.
