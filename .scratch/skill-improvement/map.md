# Skill Improvement: Product Owner Documentation Pipeline

## Destination

Two improved skills — `/stakeholder-docs` and `/developer-docs` — that form a professional Product Owner documentation pipeline. `/stakeholder-docs` runs stakeholder discovery and directly authors BRD/PRD files. `/developer-docs` translates PRDs into behavior-level developer handoffs with clear PO authority boundaries. Both integrate cleanly with the Product-Owner repo layout (`docs/01-prd/`, `docs/02-tech/`, `docs/adr/`, `CONTEXT.md`) and hand off downstream to `/export-doc` and `/to-tickets`.

## Notes

- Domain: Product Owner documentation for e-commerce operational systems.
- Skills to consult every session: `/writing-for-agents`, `/domain-modeling`.
- The current baseline is tagged `skills-baseline-v1` in `ammaryasserzein/ai-gemini-config.git`.
- Future research note (out of current scope): "What format and tools do professional Product Owners use for technical handoff documents?"
- Future research note (out of current scope): Deep dive into the 4 PO-Owned Business Categories (Rule Violations, User Errors, Domain Validation, Alternate Journeys) and industry examples of each.

## Decisions so far

- [Grilling: Skill Architecture (Round 1 & 2)](../../../.gemini/antigravity/brain/978e7671-c7c3-49e6-a7e9-f5e1d9386e8f): Q1 (direct authoring), Q2 (linear pipeline), Q3a (behavior-level only), Q3b (Actor+Outcome+Gherkin, research needed), Q3c (business-constraint ADRs only), Q3d (PO authority boundary research first), Q3e (wayfinder for both skills), Q4 (fixed checklist, no dynamic append). See conversation transcript for full detail.
- [PO Authority Boundary Research](issues/01-po-authority-boundary-research.md): PO owns What/Why, Developer owns How. Two-tier edge cases (business vs. technical). Declarative BRIEF Gherkin only. Five anti-patterns to ban. Full report at [research/po-authority-boundaries.md](research/po-authority-boundaries.md).
- [Grill Developer-Docs Design](issues/03-grill-developer-docs-design.md): Adopt 4 PO-Owned Business Categories (no technical infrastructure edge cases). Ban HTTP/SQL codes from Gherkin (BRIEF only). PO ADRs are business constraints only. Renamed output to `Developer-Spec.md`.
- [Write Stakeholder-Docs Skill](issues/02-write-stakeholder-docs-skill.md): Wrote improved `stakeholder-docs/SKILL.md` and `stakeholder-rules.md` strictly enforcing business-logic focus and direct authoring into `docs/01-prd/`.
- [Write Developer-Docs Skill](issues/04-write-developer-docs-skill.md): Wrote improved `developer-docs/SKILL.md` and `developer-rules.md` enforcing the Black-Box rule, BRIEF Gherkin, and traceability to `docs/01-prd/`.
- [Grill Feedback Loop](issues/06-grill-feedback-loop.md): Added "Adjustment Mode" to both skills. Enforces Tiered Archival strategy (copy to `docs/archive/`, tag superseded, add to `.geminiignore`), inline Revision History, contradiction halting, and `/to-questionnaire` handoffs.
- [Validate Against Luster](issues/05-validate-against-luster.md): Successfully generated `Luster-EG-System-Developer-Spec.md` under the new rules. Validated Archival ignore rules. Tagged git config repo as `skills-v2-product-owner`.

## Not yet specified

- How the improved `/stakeholder-docs` grilling probes should differ from generic `/grilling` probes (PO-specific angles: ROI framing, stakeholder power/interest, regulatory constraints).
- Whether `/developer-docs` should enforce a fixed number of edge-case categories or let the categories emerge from the PRD content.
- How the two skills share the `CONTEXT.md` vocabulary consistently (both invoke `/domain-modeling`, but sequencing and conflict resolution are unspecified).
- How to validate the improved skills against the existing Luster-EG-System deliverables as a regression test.

## Out of scope

- Improving other skills in the pipeline (`/to-tickets`, `/to-spec`, `/export-doc`).
- Changing the Product-Owner repo directory structure.
- Format/tools research for PO handoff documents (noted for future effort).
