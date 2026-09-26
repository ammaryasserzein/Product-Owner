# Luster-EG-System Discovery Notes

## Core Architecture
- **Source of Truth**: Luster-EG-System is the absolute Source of Truth for operations. Raw orders are pulled from Shopify once. All granular tracking (Packaged, Shipped, Damaged, Good) happens exclusively inside Luster.
- **Product Creation**: New products are created in Shopify first (customer-facing details). Luster automatically imports them, and the Accountant adds internal details (Purchase Price, Running Low Threshold).

## Inventory & Audits
- **Returns & Quarantine**: All returned items go into a mandatory "Pending Inspection" (Quarantine) status. They cannot be resold until a warehouse worker physically inspects and marks them as "Good (Restock)" or "Damaged".
- **Audit Adjustments**: When audits reveal missing/damaged items, the system deducts them from "Available" inventory and adds their Purchase Price to total Company Losses.
- **Compensation Tracking**: Damaged items are tracked by responsible party ("Awaiting Supplier Compensation" or "Awaiting Courier Compensation"). When compensation is received, the system offsets the loss and clears the item.

## Accounts & Orders
- **Fraudulent Orders**: Marked as "Fraud". Items are returned to inventory (subject to inspection). The sale is excluded from graphs/profits. Any failed delivery penalty from the shipping company is recorded as a "Loss" in company expenses.
- **Discounts**: Cart-level coupons are a generic "Marketing/Discount Expense". BOGO offers are handled by recording the second item's Sale Price as 0.
- **Employee Costs**: Tracked as a lump-sum "Salaries & Bonuses" expense for now. (A granular HR module will be designed later - see employee-costs-discussion.md).
- **Shipping Integration**: Starts as manual entry (admin clicks "Dispatched by Shipping Co"). API automation deferred to Phase 2.
- **Shipping Returns**: Shipping penalties/returns have a distinct category in the expenses dashboard ("Failed Delivery Penalties").
- **Accounts Receivable & Delayed Collection**: Delivered orders move to an "Awaiting Collection from Courier" bucket. A "Delayed Collection" counter flags older orders. This counter increments by +1 based on specific weekly payout days passing. Once the courier wires the money, the batch is marked "Collected" and moved to realized profits.
