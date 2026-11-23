---
name: export-doc
description: Export Product-Owner Markdown PRDs/BRDs/user stories into audited Word (.docx) deliverables saved to OneDrive (EN/AR) or uploaded directly to Google Drive as native Google Docs.
---

# Export Product-Owner Documents

Compile any Markdown (`.md`) or JSON document model in `Product-Owner` into an audited `.docx` deliverable for OneDrive or direct Google Docs conversion.

## Storage Quarantine

- **Repo quarantine**: Write `.docx` files strictly to `%TEMP%` (for Google Drive upload, deleting after verification) or `C:\Users\L\OneDrive\3. Product-Owner\<Project-Name>\`. `build_docx.py` enforces this boundary and refuses repo-internal targets.
- **No temporary files left in repo**: Save intermediate JSON models and temp `.docx` files strictly in `[System.IO.Path]::GetTempPath()`.

## Delivery Modes

1. **Google Docs Direct Upload (`--en-only` / single Markdown)**:
   - Build in `%TEMP%` directly from Markdown via `build_docx.py --markdown`, audit with `audit_docx.py --source-md`, upload with `gdrive mutate upload <temp.docx> --mime-type "application/vnd.google-apps.document"`, verify live metadata + round-trip export, then delete `<temp.docx>`.
2. **OneDrive Executive Pair (EN + AR Hybrid)**:
   - **English (`<Name>-EN.docx`)**: LTR, Aptos, `#17365D` / `#1F4E78` / `#2F5597` palette.
   - **Arabic Hybrid (`<Name>-AR.docx`)**: Translated prose with explicit RTL (`direction: "rtl"`), mirrored palette, bilingual glossary table (`المصطلح العربي | English System Term`), saved to `C:\Users\L\OneDrive\3. Product-Owner\<Project-Name>\`.

## Pipeline

```powershell
$SCRIPTS = "c:/Users/L/Documents/Product-Owner/.gemini/skills/export-doc/scripts"
$TEMP_DIR = [System.IO.Path]::GetTempPath()

# 1. Verify environment
py -3 "$SCRIPTS/check_environment.py"

# 2a. Markdown -> Google Docs fast path
$TARGET = "$TEMP_DIR/My-Doc.docx"
py -3 "$SCRIPTS/build_docx.py" --markdown "<source.md>" $TARGET
py -3 "$SCRIPTS/audit_docx.py" $TARGET --source-md "<source.md>"
# Upload via gdrive mutate upload $TARGET --parent <FOLDER_ID> --mime-type "application/vnd.google-apps.document"
# Remove-Item $TARGET after verifying live Google Doc

# 2b. JSON model -> OneDrive executive pair
py -3 "$SCRIPTS/build_docx.py" "$TEMP_DIR/<Name>-EN.json" "C:/Users/L/OneDrive/3. Product-Owner/<Project>/<Name>-EN.docx"
py -3 "$SCRIPTS/audit_docx.py" "C:/Users/L/OneDrive/3. Product-Owner/<Project>/<Name>-EN.docx"
```

## Completion Criteria

- `audit_docx.py` returns `"passed": true` with `0` findings.
- For Google Drive mode: `gdrive readonly info` confirms `mimeType: application/vnd.google-apps.document` and temp `.docx` is deleted.
- Zero `.docx` files exist inside `c:\Users\L\Documents\Product-Owner\`.
