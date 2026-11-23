# Figma Wireframe Capture (View-Seat Quota Workflow)

Use this workflow whenever extracting multiple wireframes from a Figma file (`figma_figma` MCP) to stay within the **20 read calls/month** Figma View-seat cap.

## Steps

1. **Check seat type (0 quota)**: Call `whoami` to confirm whether the active Figma seat is `View` (`20` read calls/month) or `Full`/`Dev`.
2. **Open a session (0 quota)**: Call `create_session` once with the target `fileKey` and reuse `sessionId` across all calls.
3. **Locate the tightest feature `<section>` (1 read call)**: Call `get_metadata` on the linked canvas/board node. Save the XML locally to `assets/board-<nodeId>-metadata.xml` and inspect it to locate the specific `<section>` containing the feature's frames (avoid rendering huge multi-feature canvases).
4. **Render the section once at native resolution (1 read call)**: Call `get_screenshot` on that `<section>` node with `maxDimension: 16384`. Verify `width / original_width >= 0.85` (1:1 native scale for crisp mobile UI text) and save to `assets/board-<sectionId>.png`.
5. **Slice and crop locally (0 quota)**:
   - Use Python `Pillow` (`PIL`) and exact `(x, y, width, height)` coordinates from the cached metadata XML to slice every target frame locally.
   - Save full mobile frames (`*-full.png`) for Story-level design links and focus-cropped UI regions (`*-crop.png`) for inline AC links and unlinked UI bullets.
   - Visually inspect every final PNG via `read_file` to verify crisp text, clean margins, and exact UI-state alignment.
   - Fall back to direct per-node `get_screenshot` calls **only** if Figma downscales the section and sliced text is blurry.
6. **Cache hygiene**: Keep `board-*.xml` and `board-*.png` ignored in `.gitignore`, `.geminiignore`, and `.cursorignore` so cached boards remain locally reusable (0 future Figma reads) without bloating git or AI context indexing.
