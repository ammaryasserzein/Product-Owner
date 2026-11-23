# 02: Build Router Skeleton

**What to build:** Create the new `/po-raw-to-spec` deep module, merge the old rules into a single file, and delete the legacy `/stakeholder-docs` and `/developer-docs` skills.

**Blocked by:** 08-ticket-01-extract-shared.md

**Status:** resolved

- [ ] Create `skills/po-raw-to-spec/SKILL.md` with `disable-model-invocation: true`. It must act as a Pipeline Orchestrator (not a router).
- [ ] Move `stakeholder-rules.md` and `developer-rules.md` into `skills/po-raw-to-spec/` to preserve Single Responsibility (avoiding Divergent Change).
- [ ] Ensure the new skill correctly references the external `archival-strategy.md` from the `Product-Owner` workspace.
- [ ] Implement the checkpoint gate logic explicitly to prevent sequence rushing (absorbing Ticket 03).
- [ ] Delete the legacy `stakeholder-docs` and `developer-docs` folders completely.
