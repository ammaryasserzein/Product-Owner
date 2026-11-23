# Tiered Archival Strategy

When a Product Owner triggers "Adjustment Mode" by bringing notes back to update an existing PRD, BRD, or Developer Spec, use this exact archival workflow to prevent AI context poisoning:

1. **Move, Do Not Copy**: Move the existing active document from its current location to the corresponding archive folder (`docs/archive/01-prd/` or `docs/archive/02-tech/`). Append a `-v<timestamp>` to the filename to prevent overwriting.
2. **Metadata Tombstoning**: Prepend the following `> ⛔ SUPERSEDED` markdown block to the very top of the newly archived file:
   ```markdown
   > ⛔ **SUPERSEDED / ARCHIVED SPECIFICATION**  
   > **Status**: INACTIVE / OBSOLETE  
   > **Effective Replacement**: `[Path to the new active file]`  
   > **Notice**: Do NOT implement requirements or test cases from this document. It is preserved strictly for historical auditing and violates current PO guidelines.
   ```
3. **AI Context Shielding**: Explicitly instruct the user to ensure that the `docs/archive/` path is added to `.geminiignore` and `.cursorignore`. Wait for their confirmation or run the command yourself if permitted.
4. **Active Document Update**: Generate the new, updated document in the active directory (`docs/01-prd/` or `docs/02-tech/`) incorporating the feedback.
5. **Inline Changelog**: Append a new row to the `## Revision History` table at the bottom of the active document detailing what changed and why.
