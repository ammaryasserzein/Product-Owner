# Luster Operational Context

Central operational hub acting as the single source of truth for inventory, order fulfillment lifecycle, and financial reconciliation for Luster.

## Language

**Pending Inspection**:
Quarantine state for returned or disputed items awaiting physical warehouse verification before restocking or write-off.
_Avoid_: Quarantine bin, Returned pending

**Available Inventory**:
Sellable units verified in the warehouse and ready for allocation to incoming customer orders.
_Avoid_: Stock on hand, Total stock

**Awaiting Collection from Courier**:
Accounting state for delivered Cash-on-Delivery (COD) orders whose customer payments have not yet been remitted by the shipping partner.
_Avoid_: In-transit cash, Courier pending

**Delayed Collection**:
An aging metric and alert state tracking COD receivables that remain unremitted across scheduled weekly payout settlement cycles.
_Avoid_: Overdue COD, Late money

**Failed Delivery Penalty**:
Shipping partner fee charged for non-delivered, rejected, or fraudulent shipments, recognized immediately as an operational loss.
_Avoid_: Return fee, Shipping loss

**Purchase Price**:
Internal unit acquisition cost entered by the Accountant to calculate gross margin and inventory asset value.
_Avoid_: Cost of goods, Wholesale price

**Compensated**:
The financial and status reversal of an inventory loss upon receipt of reimbursement from a supplier or courier for damaged goods.
_Avoid_: Refunded, Reimbursed, Settled claim
