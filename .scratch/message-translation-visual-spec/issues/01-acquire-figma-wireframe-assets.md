# 01: Acquire & Slice Cached Figma Wireframe Assets

**What to build:** A complete, locally cached library of crisp PNG wireframes for the five-story Message Translation specification (Stories 2, 3, 4 if a Daily Translation Quota toast exists on the board, and 5), captured within the Figma View-seat read budget by downloading the board metadata and composite image once and slicing target frames locally—with automatic fallback to direct per-node screenshots only when full-board downscaling makes mobile text illegible. Produce full mobile frames for Story-level design links and tightly focus-cropped UI regions (card, overflow menu, long-press bottom sheet, loading spinner, translated body, Show Original state, quota toast, and language picker modal states) for inline links and unlinked UI behavior bullets, plus a concise asset-mapping manifest so downstream assembly reuses every PNG without extra Figma reads. See the parent feature spec and canonical Schoolvoice glossary.

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [x] Figma session opened against the SV-Wireframes file and board metadata + high-resolution composite image fetched once for the Message Translation board node (2 read calls) and cached locally inside the wireframe assets folder.
- [x] Every linked Figma node in Section 3 (Story 2, Story 3, Story 5) and every unlinked UI state present on the board (Feed Entry Point, Message Details Recipient/Sender, Translated State, Show Original action, Daily Translation Quota toast if present, Language Picker checkmark/saved states) mapped to a cleanly named local PNG.
- [x] Every sliced mobile frame visually inspected for sharp, readable UI text; any frame degraded by board downscaling re-fetched directly by node ID while staying within the monthly View-seat quota.
- [x] Story-level design headers have full mobile-frame PNGs; inline wireframe links and unlinked UI behavior bullets have tight focus-cropped PNGs isolating the relevant card, menu, toast, or modal.
- [x] Duplicate node references share a single local PNG asset and a concise asset manifest lists each target story/bullet, Figma node ID, framing type (full or crop), and PNG filename.
- [x] Every PNG file exists, has non-zero size and readable dimensions, and visually matches its mapped UI state.

## Comments

- **Completed**: Acquired board metadata (`427:3015`) and composite PNG (`2102:36435`, `8039×4672`) in 2 Figma read calls; sliced 18 unique crisp PNGs (3 full mobile/flow frames + 15 focus crops) with zero fallback reads required. Exhaustive XML inspection confirmed no Story 4 Daily Translation Quota toast exists on the board. All 18 PNGs visually verified and indexed in the asset manifest.
