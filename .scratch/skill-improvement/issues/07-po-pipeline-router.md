## Problem Statement

The Product Owner documentation pipeline currently exposes two shallow modules (`/stakeholder-docs` and `/developer-docs`) which forces the user to manually trigger handoffs. Furthermore, the pipeline suffers from architectural friction: shared logic (the Tiered Archival strategy) is inappropriately coupled inside sibling skill folders, and banned technical implementations (APIs, SQL, Redis) are duplicated as data clumps across multiple rule files.

## Solution

We will collapse the pipeline into a single, deep router module named `/po-raw-to-spec`. This router will orchestrate the entire workflow using an industry-standard "Internal Checkpoint" (a Lossless "Narrow Waist" protocol) to prevent hallucination cascades. Simultaneously, we will decouple the shared logic by extracting it into the `Product-Owner` workspace to serve as a clean global reference.

## User Stories

1. As a Product Owner, I want a single `/po-raw-to-spec` command to trigger the entire documentation pipeline, so that I don't have to manage manual handoffs or memorize multiple AI commands.
2. As a Product Owner, I want the AI to generate the business PRD and then *pause* for my approval, so that I can ensure the business outcomes are correct before the AI generates detailed Gherkin edge cases.
3. As an AI Agent, I want to read the approved PRD from the filesystem before generating the Tech Spec, so that I guarantee lossless context transfer (the Narrow Waist protocol) instead of relying on bloated conversation history.
4. As a Product Owner, I want the agent to automatically infer whether my feedback applies to the BRD or the Tech Spec, so that I can seamlessly update requirements without explicitly dictating routing instructions.
5. As an AI Agent maintainer, I want the Tiered Archival strategy to live in the `Product-Owner` workspace (`system-projects/_templates/reference/archival-strategy.md`), so that it can be cleanly referenced by any skill without cross-folder coupling.
6. As an AI Agent maintainer, I want the list of banned technical implementations (APIs, SQL, Redis, cron jobs) extracted into `technical-boundaries.md`, so that I can update them in a single source of truth without shotgun surgery across multiple rule files.

## Implementation Decisions

- **The Router Module**: A new skill `skills/po-raw-to-spec/SKILL.md` will be created. It will have `disable-model-invocation: true`.
- **Legacy Cleanup**: The old `stakeholder-docs` and `developer-docs` skills will be deleted, and their unique rule files will be absorbed by the new router.
- **Shared References**: We will create `archival-strategy.md` and `technical-boundaries.md` inside the user's `Product-Owner` workspace (at `system-projects/_templates/reference/`).
- **The Checkpoint Gate**: The router's workflow will explicitly mandate that it must wait for the user to confirm the `01-prd` documents before it starts the Example Mapping/Gherkin generation for `02-tech`.

## Testing Decisions

- **Tests only check external behavior**: We will verify the architectural refactor by ensuring the new `/po-raw-to-spec` command successfully executes both the BRD and Tech Spec phases seamlessly.
- **The Global Reference Seam**: We will test that the router correctly locates and obeys `archival-strategy.md` and `technical-boundaries.md` from the external `Product-Owner` workspace.
- **The Internal Checkpoint Seam**: We will trigger the router with a dummy feature. We will verify that it writes the PRD and then *hard pauses*, waiting for user confirmation before proceeding to the Tech Spec.

## Out of Scope

- Modifying the underlying structure of the Gherkin rules or the 4 PO Edge Case Categories (these were already validated in v2.1).
- Building an automated Google Docs exporter (this will be handled by a separate `/browser` prompt in the future).

## Further Notes

- The research subagent definitively proved that simultaneous generation of PRDs and Tech Specs is a BDD anti-pattern ("Premature Formulation"). The Internal Checkpoint is a load-bearing architectural requirement for this pipeline.
