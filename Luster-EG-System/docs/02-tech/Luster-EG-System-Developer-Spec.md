# Luster-EG-System Developer Specification

*Traceability: Maps to [Luster-EG-System-PRD.md](../01-prd/Luster-EG-System-PRD.md)*
*Domain Vocabulary: See `CONTEXT.md`*

## 1. Business Rule Violations (PO Category 1)
**Feature**: Quarantine Enforcement
**Business Constraint**: Returned or disputed items must never be allocated to new orders until physically verified and cleared.

```gherkin
Rule: Quarantined goods cannot be allocated to new sales

  Scenario: Seller attempts to sell a quarantined item
    Given a product is physically returned and marked as "Pending Inspection"
    When a Seller attempts to manually create a new Meta order for that product
    Then the system rejects the allocation
    And the Seller is informed that the item is quarantined and unavailable for sale
```

## 2. Domain Data Validation (PO Category 3)
**Feature**: External Catalog Sync
**Business Constraint**: If Shopify sends an order containing a product not registered in Luster, the order must not be dropped.

```gherkin
Rule: Unrecognized products must generate financial stubs

  Scenario: Order arrives with missing product definition
    Given Shopify sends an order containing a product missing from the local catalog
    When the system processes the import
    Then the order is successfully created in Luster
    And a stub product record is generated
    And the Accountant receives an alert to update the missing Purchase Price
```

## 3. User-Facing Error States (PO Category 2)
**Feature**: Real-time Inventory Depletion (Concurrency SLA)
**Business Constraint**: Negative inventory is strictly disallowed. Only one user can claim the final unit of stock. (Implementation mechanism: Developer discretion).

```gherkin
Rule: Inventory cannot drop below zero during concurrent packaging

  Scenario: Concurrent packaging of the last available unit
    Given a product has exactly 1 unit of Available Inventory
    When two Sellers simultaneously attempt to package separate orders containing this product
    Then one order successfully transitions to "Packaged"
    And the other order is rejected with an "Out of Stock" UI error message
```

## 4. Alternate User Journeys (PO Category 4)
**Feature**: Role-Based Authorization
**Business Constraint**: Financial metrics are strictly confidential to Accountants and Admins. Sellers navigating directly to restricted URLs must be blocked.

```gherkin
Rule: Sellers cannot view financial reports

  Scenario: Seller navigates to a restricted financial URL
    Given a user is authenticated with the "Seller" role
    When they attempt to view the net profit reports
    Then the system denies access
    And the Seller is redirected to their authorized dashboard
```

## 5. Non-Functional Requirements & SLAs (Developer Domain)
*These represent technical edge cases. Implementation architecture (retries, lock types, DB constraints) is left to the engineering team.*

* **Shopify Sync Resilience**: Orders created during third-party webhook outages must not be lost. The system must synchronize all missing orders within 1 hour of recovery.
* **API Rate Limiting**: Background sync jobs must handle third-party API rate limits gracefully without dropping batches or crashing.

---

### Revision History
| Version | Date | Author | Description of Change |
| :--- | :--- | :--- | :--- |
| 1.0 | 2026-09-27 | Product Owner | Initial validation of new developer-docs skill rules. Replaced old Tech-Handoff. |
