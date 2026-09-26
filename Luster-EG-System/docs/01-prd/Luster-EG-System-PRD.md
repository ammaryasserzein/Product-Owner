## Problem Statement

The current manual or scattered operations of managing Luster's inventory, orders, and accounting lack precision. Relying purely on Shopify's high-level order statuses (like "Canceled") loses critical operational granularity (e.g., damaged items vs. fraud). There is a need for a unified, central system to track granular order statuses, precise inventory levels, and accurate profit/loss calculations.

## Solution

Luster-EG-System is a centralized hub acting as the absolute Source of Truth for operations. It imports basic order and product data from Shopify, but entirely handles order fulfillment, detailed status tracking, granular accounting (including losses and supplier compensations), and inventory audits internally.

## User Stories

### Orders & Shopify Sync
1. As an Admin, I want the system to automatically import new products and orders from Shopify, so that I don't have to enter them manually.
2. As a Seller/Admin, I want to manually create orders for other platforms (e.g., Meta), so that all sales are tracked in one place.
3. As a Seller, I want the system to autofill province codes matching Shopify, so that location data remains consistent for analytics.

### Inventory & Audits
4. As an Accountant, I want to add internal "Purchase Price" and "Running Low Thresholds" to imported products, so that the system can calculate profits and alert me when stock is low.
5. As an Admin, I want to filter products by their "Running Low" status, so that I know what to reorder.
6. As a Warehouse Worker, I want returned items to automatically go into a "Pending Inspection" quarantine, so that damaged goods aren't accidentally sold to new customers.
7. As an Admin, I want to perform periodic inventory audits and mark missing/damaged items, so that the system deducts them from available inventory and records the loss.
8. As an Admin, I want to mark damaged goods as "Awaiting Supplier Compensation" or "Awaiting Courier Compensation", so that I can track who owes us money.
9. As an Admin, I want to mark an item as "Compensated", so that the system reverses the recorded loss and balances the accounts.

### Order Status & Shipping
10. As a Seller, I want to transition orders through granular states (Packaged, Shipped, Delivered), so that I know exactly where the inventory is.
11. As an Admin, I want to mark fake orders as "Fraud", so that the items are restocked but the shipping penalty is accurately logged as a company loss.
12. As an Admin, I want to manually deduct orders fulfilled by the shipping company's warehouse from our system, so that our inventory stays accurate before API integration is built.

### Accounts & Financials
13. As an Accountant, I want the system to automatically calculate the profit of a sold order (Sale Price - Purchase Price) and add it to realized profits, so that I don't have to do manual math.
14. As an Accountant, I want to record lump-sum expenses (like Marketing or Salaries & Bonuses), so that they are deducted from the total company profit.
15. As an Admin, I want cart-level discounts to be tracked as generic marketing expenses, while BOGO offers record the second item at $0, so that product-specific margins remain accurate.
16. As an Accountant, I want failed shipping deliveries to automatically log the shipping penalty as a "Failed Delivery Penalty" loss, so that I can monitor how much money is lost to returns.
17. As an Accountant, I want delivered orders to sit in an "Awaiting Collection from Courier" bucket, so that I know how much cash the shipping company holds.
18. As an Admin, I want a "Delayed Collection" counter to flag orders that have passed specific weekly payout days, so that I can chase the courier for my money.
19. As an Accountant, I want to mark batches of orders as "Collected", so that the cash is moved into realized company profit.

### Analytics & Roles
20. As an Admin, I want graphs showing profit and units sold per product over various timeframes, so that I can identify best-sellers.
21. As a System, I want to enforce role-based access (Admin = full access, Accountant = financials and inventory but no order editing, Seller = orders and inventory view), so that data is secure and untampered with.

## Implementation Decisions

- **Source of Truth**: Luster handles all operational logic; Shopify is strictly the storefront.
- **Product Flow**: Created in Shopify -> Imported to Luster -> Accountant adds Purchase Price in Luster.
- **Fraud Protocol**: Fraud orders restock items but log the shipping attempt fee as a company loss.
- **Discounts**: Cart discounts are generic expenses. BOGO is handled via $0 sale price for accurate inventory cost deduction.
- **Employee Costs**: Tracked as a single lump-sum expense to keep the MVP lean. An HR module will be evaluated later.
- **Shipping Integration**: Phase 1 uses manual entry for shipping company warehouse deductions to avoid third-party API risks.
- **Accounts Receivable**: Cash sits in a transit bucket until the courier pays out, tracked by a weekly counter.

## Testing Decisions (Business Acceptance)

- Ensure Shopify order import perfectly maps province codes.
- Ensure "Pending Inspection" quarantine strictly blocks items from being marked as "Available" until explicitly cleared.
- Ensure Audit Adjustments mathematically balance the Loss accounts when "Compensated" is triggered.

## Out of Scope

- Granular HR & Payroll management module (deferred).
- Automated third-party API integration with the shipping company's warehouse (deferred to Phase 2).
- Bi-directional granular status syncing back to Shopify (Luster remains the Source of Truth).

## Further Notes

- Reference `CONTEXT-MAP.md` for domain terminology.
- `employee-costs-discussion.md` contains future notes for the HR module.
