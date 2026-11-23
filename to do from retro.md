# To-Do From Retro (2026-11-23)

Retrospective follow-ups from the Message Translation visual user-stories session.

## Completed
- [x] **Restore / relocate `export-doc` build & audit scripts (Retro #1)** — Built reusable `check_environment.py`, `build_docx.py`, and `audit_docx.py` inside `.gemini/skills/export-doc/scripts/` and updated `.gemini/skills/export-doc/SKILL.md`.
- [x] **Codify 2-call Figma View-seat section-slice guide (Retro #2)** — Added `docs/agents/figma-capture.md` with a 1-line pointer in root `AGENTS.md`.
- [x] **Add `Schoolvoice/GLOSSARY.md` avoided-terms lint to `scripts/check-repo.py` (Retro #1)**.

## Remaining (Medium Priority)
- [ ] **Install official Google Docs plugin (Retro #6)**
  - Add `antigravity-plugins-official/plugin/gdocs` from the Marketplace card so future sessions can read/edit team Google Docs directly without `.docx` conversion round-trips.

- [ ] **Review & commit global config repo (`C:\Users\L\.gemini\config`)**
  - Review uncommitted diffs from the Matt Pocock skills `v1.3.2` (`main@abeeaf9`) upgrade and the `AGENTS.md` / `GEMINI.md` / `english-feedback/RULE.md` consolidation, then commit when satisfied.

## Remaining (Low Priority)
- [ ] **Empty `US Notes.md`**: Decide whether to delete the now-empty `Schoolvoice-PO/AI translated messages/US Notes.md` or reuse it for future notes.
- [ ] **Deduplicate `assets/manifest.json`**: Only if reused as a template for future features, stop repeating file-level dimensions (`width`, `height`) inside both `mappings[]` and `files[]`.
