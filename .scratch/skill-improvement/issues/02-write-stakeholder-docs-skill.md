Type: task
Status: resolved
Blocked by:

## Question

Write the improved `/stakeholder-docs` SKILL.md and `stakeholder-rules.md` applying all settled decisions:

- Direct authoring: the skill writes `docs/01-prd/<project>-BRD(Business-needs).md` and `docs/01-prd/<project>-PRD.md` as its completion criteria.
- Linear handoff: upon completion, recommends `/developer-docs` for technical edge cases or `/export-doc` for executive deliverables.
- Fixed checklist rules: no dynamic "golden reference" append. `stakeholder-rules.md` is an immutable checklist updated only via intentional refactoring.
- Runs `/grilling` and `/domain-modeling` primitives internally.
- Grilling probes focused on PO concerns: Outcome Alignment, Trade-offs, Assumptions, Constraints, Failure Scenarios.
- Apply `/writing-for-agents` principles: sharp completion criteria, leading words, no-op pruning, progressive disclosure.
