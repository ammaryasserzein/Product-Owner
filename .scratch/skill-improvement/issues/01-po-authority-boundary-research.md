Type: research
Status: resolved
Blocked by:

## Question

What are the industry best practices for Product Owners writing developer-ready user stories with edge cases? Specifically:

1. **Authority boundary**: Where does PO specification authority end and developer implementation authority begin? What should a PO prescribe (observable behavior, acceptance criteria) versus what the developer decides (architecture, data structures, algorithms)?
2. **Edge case coverage**: How do professional POs document edge cases without prescribing implementation? What categories of edge cases are the PO's responsibility (business rule violations, user-facing error states, data validation) versus the developer's (concurrency, infrastructure resilience, performance)?
3. **Gherkin at PO level**: Is Gherkin (Given/When/Then) the right format for PO-level behavioral specs, or is there a more appropriate format? What level of Gherkin detail is appropriate for a PO versus a QA engineer?
4. **User story anti-patterns**: What are the most common mistakes POs make when writing technical handoff documents (e.g., prescribing implementation, "As a system..." stories, mixing behavior with architecture)?

Target sources: Agile Alliance, Scrum.org, Mike Cohn's writing, INVEST criteria literature, BDD/Gherkin best practices from Cucumber docs.

## Answer

Full report: [po-authority-boundaries.md](../research/po-authority-boundaries.md)

Key findings:
1. **Authority boundary**: PO owns What/Why (observable behavior, business rules, SLA targets). Developer owns How (architecture, data structures, algorithms, lock strategies). Scrum Guide 2020: implementation is "at the sole discretion of the Developers."
2. **Edge cases split into two tiers**: Business edge cases (PO-owned: rule violations, user-facing errors, domain validation, unhappy paths) vs. Technical edge cases (Developer-owned: concurrency mechanisms, infrastructure resilience, performance implementation, data persistence strategies). PO specifies the business invariant; developer picks the mechanism.
3. **Gherkin format confirmed, but must be declarative BRIEF**: Business language, Real data, Intent-focused, Essential (no HTTP codes/SQL/CSS), Focused (one rule per scenario, 3-5 lines). PO writes ~1-3 scenarios per business rule. QA/Dev writes exhaustive automated test suites.
4. **Five anti-patterns identified**: Solutioneering (prescribing implementation), "As a system..." persona, mixing behavior with architecture, over-specifying (>5 AC per story), story-as-handoff mentality.
5. **The current Luster Tech-Handoff.md violates multiple anti-patterns**: "As a system..." stories, prescribing pessimistic locks and atomic SQL operations, naming database columns in acceptance criteria.
