# Business Requirements Document (BRD) - Luster-EG-System

## 1. Executive Summary
Luster is experiencing operational friction and financial blind spots due to a reliance on high-level, generalized statuses provided by Shopify (e.g., "Canceled"). The business requires a centralized operational hub—Luster-EG-System—to act as the absolute source of truth for inventory management, granular order tracking, and precise profit/loss accounting.

## 2. Business Objectives
- **Financial Accuracy**: Eliminate blind spots in profit calculations by precisely tracking "hidden" costs like failed delivery penalties, supplier compensations, and damaged goods.
- **Inventory Protection**: Prevent the accidental resale of damaged returns through a mandatory "Pending Inspection" quarantine workflow.
- **Cash Flow Visibility**: Track uncollected funds sitting with third-party couriers via an automated "Delayed Collection" aging system tied to weekly payout schedules.
- **Operational Independence**: Decouple backend fulfillment and accounting from the Shopify storefront, ensuring Luster owns and controls its operational data.

## 3. Stakeholders & Roles
- **System Admin / Business Owner**: Requires full visibility into total profits, losses, inventory audits, and high-level analytics to make strategic decisions. Full system access.
- **Accountant**: Requires access to sensitive financial data (Purchase Prices, Profit Margins, Lump-sum Expenses, Delivery Penalties) to balance the books, without modifying active customer orders.
- **Sellers / Fulfillment Team**: Requires the ability to process orders through granular fulfillment states and view inventory levels, without access to cost/profit metrics.
- **Warehouse Workers**: Requires a strict workflow to quarantine and inspect returned items before restocking them into available inventory.

## 4. Core Business Rules & Constraints
- **Source of Truth**: Luster-EG-System is the primary operational ledger. Shopify remains solely the customer-facing storefront.
- **Product Origin Rule**: All new products must originate in Shopify to ensure public details exist, followed by financial enrichment (Purchase Costs, Low Stock Thresholds) within Luster.
- **Fraud Protocol**: Fraudulent orders must isolate associated delivery penalties as business losses and explicitly exclude the order from sales metrics and product graphs.
- **Discount Valuation**: Cart-wide discounts are treated as generic marketing expenses. BOGO offers must record the second item's sale price as $0 to accurately deduct inventory cost against profit.
- **Compensation Offsets**: Financial losses logged from damaged inventory must be strictly reversible when compensation is finally received from a supplier or courier.

## 5. Out of Scope (Phase 1)
- Granular HR, Payroll, and employee-specific cost tracking.
- Automated API integrations with third-party shipping company warehouses.
- Bi-directional sync of granular operational statuses back to Shopify.
