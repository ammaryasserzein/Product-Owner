# 03: Implement the Checkpoint Gate

**What to build:** Add the explicit execution logic to the `/po-raw-to-spec` router so that it guarantees the Narrow Waist lossless protocol.

**Blocked by:** 09-ticket-02-build-router.md

**Status:** ready-for-agent

- [ ] Add the execution instruction to write the `01-prd` to disk.
- [ ] Add the explicit "Human-in-the-Loop Checkpoint" step where the agent must stop and ask the user for approval.
- [ ] Add the formulation instruction dictating that the tech spec subagent must read the approved PRD from disk rather than relying on conversation history.
- [ ] Ensure the Adjustment Mode auto-infers feedback targets.
