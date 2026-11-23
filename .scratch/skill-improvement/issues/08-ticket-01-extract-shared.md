# 01: Extract Shared References

**What to build:** Move the AI context shielding instructions (the Tiered Archival strategy) and the list of banned technical implementations (APIs, SQL, Redis, cron jobs) out of the `.gemini/config` skills and into the `Product-Owner` workspace at `system-projects/_templates/reference/`. Delete the old duplicate clumps from `config`.

**Blocked by:** None (can start immediately)

**Status:** resolved

- [ ] Create `system-projects/_templates/reference/archival-strategy.md`
- [ ] Create `system-projects/_templates/reference/technical-boundaries.md`
- [ ] Delete `archival-strategy.md` from `config/skills/stakeholder-docs/`
- [ ] Strip the banned technical terms from `developer-rules.md` and `stakeholder-rules.md` in preparation for the router.
