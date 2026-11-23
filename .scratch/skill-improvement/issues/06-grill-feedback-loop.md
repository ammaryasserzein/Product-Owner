Type: grilling
Status: resolved
Blocked by:

## Question

Design the "Feedback Loop" workflow for the Product Owner pipeline. 

The PO (user) does not write code. Their pipeline is strictly:
1. Generate BRD/PRD (`/stakeholder-docs`) and Developer Spec (`/developer-docs`).
2. Deliver documents to human stakeholders and developers.
3. Receive notes/feedback.
4. Adjust documents.
5. Repeat.

How should the skills/workflow handle step 4 (Adjusting based on feedback)?
- Do we need a new skill (e.g., `/refine-docs`)?
- Should the existing skills be updated to handle an "adjustment" mode?
- How do we track what changed so stakeholders/developers know their feedback was incorporated?

## Answer

- **Skill Boundary**: Added an "Adjustment Mode (Feedback Loop)" directly into `/stakeholder-docs` and `/developer-docs`. No new skills needed.
- **Contradictions**: The AI is programmed to halt and grill the PO if new feedback contradicts an existing constraint or ADR.
- **Tracking/Versioning**: Implemented the "Tiered Archival Strategy" from research. The active file stays canonical (e.g., `Developer-Spec.md`), the old file is copied to `docs/archive/`, tagged with `> ⛔ SUPERSEDED`, and added to `.geminiignore` so AI won't read it. A `## Revision History` table is updated inline in the active spec.
- **Roadblocks**: Added explicit handoffs to `/to-questionnaire` if the PO hits a wall needing human expert knowledge.
