# Visual Message Translation User Stories & Presentation Deliverables

Status: ready-for-agent

## Problem Statement

As a Product Owner intern presenting the Message Translation user stories to teammates in a live meeting, reading a text-only specification full of raw Figma links forces constant tab-switching and loses co-workers' attention. The source export also bundles three overlapping tabs in one raw file, omits several inline wireframe links in the latest five-story draft, and needs a shareable Google Docs copy alongside the working Obsidian note—while staying within a Figma View-seat monthly read-call cap.

## Solution

Produce a clean, presentation-ready visual version of the five-story Message Translation specification (Section 3 only) in Obsidian, enriched with crisp, focus-cropped Figma wireframe screenshots embedded directly beneath every relevant story header, inline wireframe link, and unlinked UI behavior bullet—captured efficiently via a reusable two-call full-board download and local coordinate slicing pipeline. Pair the visual Obsidian note with a separate Presenter Notes sheet summarizing open technical validation items, and upload a cleanly formatted English Google Doc copy directly to the Product Owner's Schoolvoice Google Drive without leaving any binary Word documents inside the repository or OneDrive.

## User Stories

1. As a Product Owner presenter, I want only the five-story specification (Section 3) extracted as the single source of truth, so that outdated two-story drafts never confuse teammates during the walkthrough.
2. As a Product Owner presenter, I want the original raw user-story file preserved untouched, so that I always have an unmodified backup of the source export.
3. As a Product Owner presenter, I want every sentence, heading, bullet, and acceptance criterion from Section 3 preserved verbatim in the exact same order, so that engineering and design review the exact approved wording.
4. As a Product Owner presenter, I want mechanical Google-Docs-export artifacts cleaned up (missing character typo, stray backtick, blank duplicate headings, redundant Markdown backslash escapes) without altering any word or meaning, so that the presentation looks polished on screen.
5. As a Product Owner presenter, I want the full Message Translation Figma board metadata and composite image downloaded once and cached locally, so that extracting every linked and unlinked frame stays within my monthly Figma View-seat read quota.
6. As a Product Owner presenter, I want an automatic sharpness check on locally sliced frames with fallback to direct per-node Figma screenshots if the full board is downscaled, so that mobile UI text remains crystal-clear during screen-sharing.
7. As a Product Owner presenter, I want every Story-level design link (Stories 2, 3, and 5) to display its full mobile screen wireframe directly beneath the link, so that co-workers immediately orient to the full screen context for each story.
8. As a Product Owner presenter, I want inline wireframe links and unlinked UI behavior bullets (Feed Entry Points, Message Details Recipient/Sender, Long-Press Bottom Sheet, Translating Loading Spinner, Translated State, Show Original, Daily Translation Quota toast if present on the board, and Language Picker states) to display tightly cropped screenshots focused on the relevant card, menu, or modal, so that attendees' eyes stay locked on the exact UI detail being discussed.
9. As a Product Owner presenter, I want the top-level overview board link skipped as an inline embed in the document body, so that an unreadable zoomed-out canvas never clutters the top of the specification.
10. As a Product Owner presenter, I want repeated node references to reuse the same locally stored PNG asset, so that storage stays clean and zero redundant Figma calls are spent.
11. As a Product Owner presenter, I want the visual Obsidian Markdown document and its wireframe assets stored neatly inside the Schoolvoice working vault under the Message Translation feature folder, so that all feature artifacts live in one place.
12. As a Product Owner presenter, I want Obsidian image embeds width-constrained for clean Reading View proportions, so that phone screenshots never blow up vertically and force excessive scrolling during a presentation.
13. As a Product Owner presenter, I want a separate Presenter Notes companion file listing all `[tech validate]` items and key clarifying talking points without modifying the user-story document, so that I can guide technical Q&A smoothly during the meeting.
14. As a Product Owner presenter, I want the exact same visual English specification compiled to a temporary Word document and uploaded directly to my Schoolvoice Google Drive as a native Google Doc, so that co-workers can open, follow along, and comment in the team's native Google Docs workflow.
15. As a Product Owner presenter, I want no `.docx` binaries saved in the git repository or OneDrive, so that repository hygiene is maintained and unnecessary duplicates are avoided.
16. As a Product Owner maintaining domain knowledge, I want the five settled Message Translation concepts (`Message Translation Scope`, `Translation Language`, `Daily Translation Quota`, `Device Translation Cache`, `Show Original`) maintained in the single canonical Schoolvoice glossary linked from the root glossary map, so that future PO and agent sessions share one unified domain vocabulary.

## Implementation Decisions

- **Source & Scope Isolation**: Extract strictly Section 3 (the five-story specification: Translation Engine, Translate a Message, Revert to Original Message, Daily Translation Quota, Change Translation Language) into a new visual Markdown note inside the Schoolvoice working vault's Message Translation folder; leave the original root export untouched.
- **Verbatim Text Hygiene**: Preserve all wording, structure, and ordering identically. Clean only mechanical export defects: fix the broken word ending on the Story 5 entry point row, remove the stray backtick in Story 2, drop the two empty duplicate headings before Story 3, and normalize redundant Markdown escape backslashes.
- **Two-Stage Figma Acquisition Pipeline (Quota-Aware)**:
  - Start a Figma session against the target wireframes file, then run a single metadata fetch on the Message Translation board node to obtain exact bounding boxes for every child frame and component, followed by a single high-resolution screenshot fetch of the board (two read calls total).
  - Slice each target node locally from the cached board PNG using proportional coordinate mapping and evaluate effective pixel width/text legibility on sliced mobile frames.
  - If Figma's backend rasterizer clamps the full-board image such that sliced phone UI text is blurry, automatically fall back to direct per-node screenshot fetches for the needed frames (caching every downloaded PNG locally so repeated references cost zero extra calls).
- **Framing & Crop Strategy**:
  - Skip embedding the top-level multi-screen overview board in the document body.
  - Use full mobile screen renders for story-level design headers.
  - Apply deterministic smart crops focused on the relevant UI region (message card, overflow menu, long-press bottom sheet, loading card, translated body, toast banner, or language modal) for inline acceptance-criteria links and unlinked UI behavior bullets across Stories 2, 3, 4 (if a quota toast frame exists on the board), and 5.
  - Embed images in Obsidian using width-constrained local asset references so Reading View stays compact and scannable.
- **Companion Presenter Notes**: Generate a separate Presenter Notes Markdown file collecting every `[tech validate]` callout from Stories 1–5 (system prompt caching, failed-call quota debit, same-language bypass, plus quick reference notes for the meeting) without injecting any extra prose into the verbatim story document.
- **Direct Google Docs Delivery (No Repo/OneDrive `.docx`)**:
  - Build a clean English-only `.docx` in the OS temporary directory from the exact same verbatim Section 3 text and cropped/sized PNG assets (matching executive typography and clear image sizing so each screenshot sits cleanly under its link/bullet).
  - Validate the temporary `.docx` with the existing document audit script before upload.
  - Upload the temporary `.docx` into a folder named `"user story enhancments"` in the authenticated Schoolvoice Google Drive account (creating the folder if it does not yet exist), converting it into a native Google Doc, capture the returned Drive file ID and shareable URL, then remove the temporary `.docx` so zero `.docx` files remain in the repository or OneDrive.
- **Canonical Domain Glossary Unification** *(completed inline during grilling)*: Legacy context files are unified onto the multi-context root glossary map pointing to one canonical Schoolvoice glossary containing the five Message Translation terms, and the obsolete scope-doubt note was cleared.

## Testing Decisions

Verification operates through two high-level external deliverable seams rather than testing internal helper details:

1. **Verbatim & Visual Integrity Seam**:
   - Programmatically normalize and diff the extracted textual content of the new visual Markdown document against Section 3 of the untouched source file (ignoring only inserted image embed lines and the four explicitly approved export-glitch cleanups) to guarantee zero unintended word drift, missing bullets, or reordering.
   - Verify every image reference resolves to an existing local PNG asset with non-zero dimensions, crisp text readability (visual inspection of rendered crops), and exact UI-state alignment with its parent bullet.
2. **Google Docs Export & Repo Hygiene Seam**:
   - Run the existing Word document audit script (`audit_docx.py`, prior art from the workspace export skill) against the temporary `.docx` prior to upload and require zero audit findings.
   - Verify the uploaded native Google Doc via read-only Google Drive inspection (confirming native Google Docs MIME type and accessible URL) and confirm via repository status check that zero `.docx` binaries were created in the repository or OneDrive.

## Out of Scope

- Translating the user stories into Arabic or generating an Arabic hybrid `.docx`.
- Editing or modifying the original root Markdown export file.
- Keeping or enriching Sections 1 and 2 (the older two-story drafts).
- Writing `.docx` copies to OneDrive.
- Creating an interactive HTML deck or PowerPoint slide deck (deferred unless requested later).
- Altering Figma designs or creating new wireframes for states not present on the Figma board.
- Committing or pushing git changes automatically without user review.

## Further Notes

- Figma View-seat read quota is capped at 20 MCP read calls per month (1 call already used during verification). Caching the board/assets locally guarantees future presentation tweaks or re-exports require zero additional Figma calls.
- Because the Google Doc is uploaded to the root of the authenticated Schoolvoice Drive by default, the user can move it into any team shared folder in Drive immediately via the returned link (or specify a Drive folder ID before implementation).
- Matt Pocock's skills were updated to `v1.3.2` (`main@abeeaf9`) in parallel during grilling; diffs in the global config repo and project workspace remain uncommitted for user review.
