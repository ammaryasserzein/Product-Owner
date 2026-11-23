# 02: Author Presenter Notes Cheat-Sheet

**What to build:** A standalone Presenter Notes companion Markdown document inside the Message Translation feature folder that equips the Product Owner presenter for live meeting walkthroughs and technical Q&A—synthesizing every `[tech validate]` item across Stories 1–5 and concise story-by-story clarification cues using canonical Schoolvoice glossary terminology (`Actionable Message`, `Message Translation Scope`, `Translation Language`, `App UI Language`, `Daily Translation Quota`, `Device Translation Cache`, `Show Original`) while leaving the source user-story export untouched. See the parent feature spec and canonical Schoolvoice glossary.

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [x] Standalone Presenter Notes note created inside the Message Translation feature folder without altering the raw user-story export or duplicating the full user-story body.
- [x] Every `[tech validate]` callout from Section 3 across Stories 1–5 is captured with its story reference, concrete question to resolve with engineering, and recommended default/decision prompt (system prompt caching, same-language bypass to save tokens, failed-call quota debit in Story 1 and Story 4).
- [x] Concise story-by-story presenter cues included for Stories 1–5 highlighting key boundaries (Actionable Messages excluding Emergency Alert, body-only translation, pinned `gpt-4o-mini` at temperature 0, 10/day UAE GMT+4 quota with Device Translation Cache exemption, RTL/LTR body-vs-UI direction rules, and own-script vs UI-localized language labels).
- [x] All terminology strictly matches the canonical Schoolvoice glossary (zero avoided synonyms).
- [x] Structured with scannable Markdown tables and checklists suitable for quick glancing during a live presentation.

## Comments

- **Completed**: Authored the standalone Presenter Notes companion cheat-sheet covering all 4 `[tech validate]` engineering decisions, Stories 1–5 presenter cues, directionality and action-impact matrices, and the live meeting sign-off checklist. Post-review cleanup removed unrequested UI polish/parking-lot notes and confirmed zero avoided glossary terms.
