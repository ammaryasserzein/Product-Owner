# Product Owner Authority Boundaries: Writing Developer-Ready User Stories and Edge Cases

## Executive Summary

A critical failure mode in agile product development occurs when Product Owners (POs) conflate **business specifications** with **technical implementation**. When a PO dictates database schemas, concurrency locking mechanisms, or infrastructure retry patterns, they violate developer autonomy, degrade system architecture, and destroy the foundational principle of user stories as tokens for collaboration. Conversely, when a PO omits business-level edge cases, developers are forced to make unguided business assumptions in code.

This report establishes the industry consensus across foundational authorities—the Scrum Guide, INVEST criteria (Bill Wake), Mike Cohn (Mountain Goat Software), Roman Pichler, Martin Fowler, Dan North, and Cucumber/BDD documentation—defining exactly where PO specification authority ends and Developer implementation authority begins.

---

## 1. Authority Boundary: Specification vs. Implementation

### 1.1 The Scrum Guide Definition
*   **The Product Owner owns the "What" and "Why"**: The Product Owner is accountable for maximizing the value of the product resulting from the work of the Scrum Team and for effective Product Backlog management. This includes developing and explicitly communicating the Product Goal, creating and clearly communicating Product Backlog items (PBIs), and ordering them ([Scrum Guide 2020](https://scrumguides.org/scrum-guide.html)).
*   **The Developers own the "How"**: Developers are accountable for creating a plan for the Sprint (the Sprint Backlog), instilling quality by adhering to a Definition of Done, and adapting their plan toward the Sprint Goal ([Scrum Guide 2020](https://scrumguides.org/scrum-guide.html)).
*   **The "Sole Discretion" Clause**: The Scrum Guide 2020 explicitly demarcates implementation authority in Sprint Planning Topic 3 (*"How will the chosen work get done?"*):
    > *"For each selected Product Backlog item, the Developers plan the work necessary to create an Increment that meets the Definition of Done... How this is done is at the sole discretion of the Developers. No one else tells them how to turn Product Backlog items into Increments of value."* ([Scrum Guide 2020](https://scrumguides.org/scrum-guide.html))

### 1.2 The INVEST Criteria (Bill Wake)
In 2003, Bill Wake formulated the INVEST mnemonic to define what makes a high-quality Product Backlog Item ([Bill Wake, XP123](https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/)):
*   **Independent**: Stories should be self-contained and deliverable without tight coupling to sibling stories.
*   **Negotiable**: A user story is **not a formal contract or rigid specification**. It is a placeholder for a conversation between the PO and the development team. If a PO prescribes architecture, data structures, or algorithms, the story ceases to be negotiable and degenerates into a mini-waterfall requirement.
*   **Valuable**: The story must deliver observable value to an end user or the business.
*   **Estimable**: Developers must understand the requirement well enough to size the work.
*   **Small**: Sized to fit comfortably within a single iteration.
*   **Testable**: Verifiable through objective acceptance criteria. Bill Wake stresses that testability refers to verifying observable outcomes, not validating internal code implementation.

### 1.3 Mike Cohn (Mountain Goat Software)
*   **Conditions of Satisfaction (CoS)**: Mike Cohn defines Acceptance Criteria as the PO's "Conditions of Satisfaction"—the criteria used to confirm that a user story meets the business intent ([Mountain Goat Software: Acceptance Criteria](https://www.mountaingoatsoftware.com/agile/user-stories)).
*   **The Card, Conversation, Confirmation (3 C's) Model**: Originally articulated by Ron Jeffries and championed by Cohn, user stories are not comprehensive technical documents:
    *   *Card*: A reminder to have a conversation.
    *   *Conversation*: The dialogue between PO and Developers where the implementation "how" is debated and decided.
    *   *Confirmation*: The acceptance criteria verifying that the problem was solved.
*   **Respecting the Seam**: Cohn notes that POs frequently overstep when they prescribe UI mechanics or technical solutions. A PO should describe the user's intent and business problem; Developers decide the best architectural means to achieve it ([Mountain Goat Software Blog](https://www.mountaingoatsoftware.com/blog/)).

### 1.4 Martin Fowler: Domain-Oriented Specifications
*   Martin Fowler notes that business-facing specifications and story tests must *"describe the system in domain-oriented terms while intentionally ignoring the component architecture of the system"* ([Martin Fowler: BusinessFacingTest](https://martinfowler.com/bliki/BusinessFacingTest.html)).
*   Conflating acceptance criteria with architectural layers makes tests brittle and deprives developers of the ability to refactor underlying schemas without breaking specifications.

### Summary Table: Division of Authority

| Dimension | Product Owner Authority (Prescribed) | Developer Authority (Autonomous) |
| :--- | :--- | :--- |
| **Goal & Context** | Business problem, user motivation, ROI, Product Goal | Engineering strategy, technical debt reduction, refactoring plan |
| **Behavior** | Observable user inputs, business outputs, system domain responses | Internal method calls, service boundaries, component design |
| **Acceptance Criteria** | Conditions of satisfaction, business validation rules, SLA targets | Unit/integration test design, CI/CD pipeline, code architecture |
| **Data** | Domain entities, business attributes, data retention policies | Table schema, normalization, indexes, column types, DB engines |
| **Execution** | Prioritization of features and business constraints | Algorithms, concurrency handling, caching, design patterns |

---

## 2. Edge Case Coverage at PO Level: What to Specify vs. What to Defer

### 2.1 Edge Cases That ARE the PO's Responsibility
The PO is accountable for any scenario that alters the **business outcome**, **domain rule**, or **user experience**:
1.  **Business Rule Violations**: Expired promotions, credit limit exceedance, invalid state transitions.
2.  **User-Facing Error States & Recovery Paths**: Out-of-stock messaging, partial fulfillment communication, form validation guidance.
3.  **Domain Data Validation**: Permitted formats (tax IDs, phone numbers), business quantity limits, duplicate detection.
4.  **Alternate User Journeys / Unhappy Paths**: Permission revocation mid-checkout, address changes after order placement.

### 2.2 Edge Cases That ARE the Developer's Responsibility
The PO specifies the **business requirement**, but Developers determine the **technical mechanism**:
1.  **Concurrency & Race Conditions**: PO specifies *"negative inventory is strictly disallowed"*; Developer decides lock strategy.
2.  **Infrastructure Resilience**: PO specifies *"orders must not be lost during API downtime, sync within 1 hour"*; Developer designs webhooks, queues, backoff.
3.  **Performance & Scaling**: PO defines SLA thresholds; Developer implements caching, indexing, pagination.
4.  **Data Integrity & Persistence**: PO defines retention policies; Developer chooses soft deletes, cascading, partitions.

### 2.3 The "Black-Box" Rule
As Roman Pichler emphasizes: *"Acceptance criteria should specify the system as a black box. Describe what the system should do from the user's perspective, not how the software should do it internally."* ([Roman Pichler](https://www.romanpichler.com/blog/acceptance-criteria/))

---

## 3. Gherkin at the PO Level: Declarative vs. Imperative

### 3.1 Declarative Gherkin (Best Practice)
```gherkin
# GOOD: Clear business intent, technology-agnostic
Rule: Inventory cannot become negative

  Scenario: Concurrent purchase of the final inventory unit
    Given a product has exactly 1 unit available in stock
    When two customers attempt to purchase this item simultaneously
    Then one customer's order is successfully placed
    And the other customer is informed that the item is out of stock
    And the remaining stock level is 0
```

### 3.2 Imperative Gherkin (Anti-Pattern)
```gherkin
# BAD: Dictates UI mechanics and technical implementation
Scenario: Purchase last item
  Given the product table has row id 42 with count 1
  When I click the button with id "#buy-now-btn"
  And the API sends POST to "/api/v1/orders"
  Then the backend middleware executes a pessimistic lock
  And the response status code is 200
```

### 3.3 The BRIEF Principle (Seb Rose & Gáspár Nagy)
*   **B - Business language**: Terms from the domain ubiquitous language.
*   **R - Real data**: Realistic examples, not dummy data.
*   **I - Intent-focused**: What the user accomplishes, not how the system does it.
*   **E - Essential**: No CSS selectors, HTTP codes, database columns.
*   **F - Focused**: One business rule per scenario; rarely exceed 3–5 lines.

### 3.4 Level of Detail: PO vs. QA Engineer

| Attribute | PO Level Gherkin | QA Engineer / Developer Gherkin |
| :--- | :--- | :--- |
| **Primary Goal** | Define business rules, communicate acceptance criteria | Executable automated regression test suites |
| **Syntax Style** | High-level declarative, business domain events | Step definitions, parameter tables, test fixture hooks |
| **Scope** | Core happy path + critical business edge cases (1–3 per rule) | Exhaustive boundary permutations, performance tests |
| **Technical Exposure** | Zero implementation details | Automated test harnesses |

---

## 4. User Story Anti-Patterns

### 4.1 Prescribing Implementation ("Solutioneering")
PO dictates architecture instead of specifying behavior. Example: *"the system uses a pessimistic lock (or atomic UPDATE ... WHERE count >= 1)"*. Correction: Specify the behavioral invariant.

### 4.2 The "As a system..." Persona
Systems do not have desires or business motivations. Reframe with real human actors or capture as NFR/SLA.

### 4.3 Mixing Behavior with Architecture
Merging functional acceptance criteria with architectural specifications. Maintain a strict seam.

### 4.4 Over-Specifying ("Monster Stories")
Violates Negotiable and Small in INVEST. Aim for ~5 acceptance criteria per story (Roman Pichler).

### 4.5 The "Story Handoff / Scribe" Mentality
Treating stories as one-way documents. Stories are co-created in "Three Amigos" discovery sessions.

---

## Primary Sources & Citations

1.  **Scrum Guide (2020)**: [https://scrumguides.org/scrum-guide.html](https://scrumguides.org/scrum-guide.html)
2.  **INVEST Criteria (Bill Wake)**: [https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/](https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/)
3.  **Mountain Goat Software (Mike Cohn)**: [https://www.mountaingoatsoftware.com/agile/user-stories](https://www.mountaingoatsoftware.com/agile/user-stories)
4.  **Roman Pichler**: [https://www.romanpichler.com/blog/acceptance-criteria/](https://www.romanpichler.com/blog/acceptance-criteria/)
5.  **Martin Fowler**: [https://martinfowler.com/bliki/BusinessFacingTest.html](https://martinfowler.com/bliki/BusinessFacingTest.html)
6.  **Dan North**: [https://dannorth.net/introducing-bdd/](https://dannorth.net/introducing-bdd/)
7.  **Cucumber Documentation**: [https://cucumber.io/docs/bdd/](https://cucumber.io/docs/bdd/)
8.  **The BDD Books (Seb Rose & Gáspár Nagy)**: [https://bddbooks.com/](https://bddbooks.com/)
9.  **Scrum.org (Stefan Wolpers)**: [https://www.scrum.org/resources/blog/product-owner-anti-patterns-31-2-ways-improve-po](https://www.scrum.org/resources/blog/product-owner-anti-patterns-31-2-ways-improve-po)
