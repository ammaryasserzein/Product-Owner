# 04: Export & Upload Native Google Doc Deliverable

**What to build:** A cleanly formatted, English-only native Google Doc uploaded directly into a `"user story enhancments"` folder in the authenticated Schoolvoice Google Drive account, generated from the verified visual Obsidian Markdown specification and its cached PNG assets via an audited temporary Word build that leaves zero Word binaries in the git repository or OneDrive. See the parent feature spec and verified output from Ticket 03.

**Blocked by:** 03: Assemble & Verify Visual Obsidian User Stories

**Status:** ready-for-agent

- [x] English-only temporary Word document generated strictly inside the OS temporary directory containing the exact verbatim five-story text from Ticket 03 with every embedded PNG wireframe rendered cleanly inline directly under its corresponding link or bullet at presentation-friendly scale.
- [x] Existing Word audit check and OOXML schema validation pass with zero findings, verifying package integrity, schema ordering, SHA-256-matched wireframe assets, external hyperlinks, zero leaked Markdown syntax, and exact verbatim word parity.
- [x] Target folder named `"user story enhancments"` created (or reused) in the authenticated Schoolvoice Google Drive account.
- [x] Temporary Word document uploaded into `"user story enhancments"` and converted to a native Google Doc, verified via read-only Drive inspection and round-trip export for native MIME type, parent folder placement, verbatim five-story text, embedded wireframe images, and clickable links.
- [x] Temporary Word document, build/audit scripts, and export verification files deleted from the OS temporary directory; repository and OneDrive confirmed completely free of generated Word binaries.

## Comments

- **Completed — Build & OOXML Audit**:
  - Generated temporary Word document in the OS temporary directory at presentation scale (`6.2 in` four-phone flow, `2.35 in` single-phone screens, `3.2 in` focus crops; 20 inline drawings, 18 unique PNGs, 9 OOXML hyperlinks, 3-level native bullets, orphan guards).
  - Standalone Word audit script was absent locally, so an equivalent full Python OOXML audit ran and passed (`"passed": true`, `0` findings): verified valid ZIP / 16 XML parts, strict ECMA-376 OOXML schema ordering, 20 inline drawings & 18 SHA-256-matched PNGs from the wireframe assets folder at target widths, 9 external hyperlinks, zero leaked Markdown syntax, and exact `2002/2002` verbatim word match.
- **Completed — Google Drive Upload & Round-Trip Verification**:
  - Account: `ammar.zein@schoolvoice.com`
  - Drive Folder: `"user story enhancments"` — ID: `1d9LzT-gr9-bqCm-0gVsYUe3vBtUZd2fk`, URL: `https://drive.google.com/drive/folders/1d9LzT-gr9-bqCm-0gVsYUe3vBtUZd2fk`
  - Native Google Doc: `Message Translation - User Stories` (`application/vnd.google-apps.document`) — ID: `1jT1lDhhsjpiGehrOOasRHmF07a4Wu47ZBGHWsUD7d9w`, URL: `https://docs.google.com/document/d/1jT1lDhhsjpiGehrOOasRHmF07a4Wu47ZBGHWsUD7d9w/edit?usp=drivesdk`
  - Live read-only Drive metadata and exported text/HTML round-trip verified native Google Docs MIME type, parent folder `1d9LzT-gr9-bqCm-0gVsYUe3vBtUZd2fk`, all 5 stories verbatim (`2002/2002` visible words), `20/20` embedded images with alt text, and `9/9` clickable external links.
- **Completed — Cleanup**: Deleted all temporary Word, script, and export verification files from the OS temporary directory; confirmed `0` `.docx` files in repository and `0` new `.docx` files in OneDrive.
