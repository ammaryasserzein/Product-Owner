# 03: Assemble & Verify Visual Obsidian User Stories

**What to build:** The presentation-ready Obsidian Markdown document for the five-story Message Translation specification (Section 3 only), preserving every word, sentence, heading, and bullet verbatim in its exact original order while fixing strictly the four approved mechanical export glitches, embedding width-constrained local PNG wireframes directly beneath every Story header link, inline wireframe link, and unlinked UI behavior bullet (omitting the top-level overview board), and verifying verbatim fidelity and asset integrity via an automated check. See the parent feature spec, asset manifest from Ticket 01, and canonical Schoolvoice glossary.

**Blocked by:** 01: Acquire & Slice Cached Figma Wireframe Assets

**Status:** ready-for-agent

- [x] New visual Obsidian Markdown note created inside the Message Translation feature folder; original raw user-story export remains completely untouched.
- [x] Strictly Section 3 (five stories: Translation Engine, Translate a Message, Revert to Original Message, Daily Translation Quota, Change Translation Language) is included; Sections 1 and 2 are excluded.
- [x] Only the four approved mechanical export cleanups are applied: Story 5 entry point broken word ending fixed to `row.`, stray backtick in Story 2 removed, two empty duplicate headings before Story 3 removed, and redundant Markdown backslash escapes normalized.
- [x] Top-level feature overview board link has no inline screenshot embedded beneath it; every Story header link (Stories 2, 3, 5) has its full mobile-frame PNG embedded directly beneath it; every inline wireframe link and unlinked UI behavior bullet (with an available board asset) has its focus-cropped PNG embedded directly beneath it using Obsidian width-constrained embeds.
- [x] Automated verbatim text-diff check passes with zero unexpected word, sentence, or ordering deviations against Section 3 of the untouched source file.
- [x] Automated asset-link check confirms 100% of embedded PNG references resolve to existing non-empty files in the wireframe assets folder.

## Comments

- **Completed**: Assembled Section 3 verbatim with strictly the 4 approved mechanical export cleanups and 20 width-constrained Obsidian image embeds across 18 unique PNG assets (including consistent trailing two-space hard line breaks for all 16 bullet-attached embeds). Automated verification confirmed 0 word/line diffs against Section 3 of the untouched source export and 20/20 valid non-empty asset references.
