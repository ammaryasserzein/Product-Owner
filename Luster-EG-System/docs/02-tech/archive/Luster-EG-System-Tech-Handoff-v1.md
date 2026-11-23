> ⛔ **SUPERSEDED / ARCHIVED SPECIFICATION**  
> **Status**: INACTIVE / OBSOLETE  
> **Effective Replacement**: `docs/02-tech/Luster-EG-System-Developer-Spec.md`  
> **Notice**: Do NOT implement requirements or test cases from this document. It is preserved strictly for historical auditing and violates current PO guidelines.

# Luster-EG-System: Developer Handoff & Edge Case Matrix

## 1. Integration (Shopify Sync & Resilience)
**Technical User Story**: As a system, I want to guarantee zero dropped Shopify orders by combining real-time webhooks with a resilient polling fallback.
* **Scenario: Recovering missed webhook orders**
  * Given the Shopify API webhook delivery failed or the server was down
  * When the hourly reconciliation cron job executes
  * Then the system fetches all orders created since the last_successful_sync timestamp and imports them safely.

## 2. Concurrency (Inventory Race Conditions)
**Technical User Story**: As a Seller, I want the database to strictly prevent negative inventory when multiple users package orders simultaneously.
* **Scenario: Concurrent packaging of the last inventory unit**
  * Given a product has exactly 1 unit in vailable_stock
  * And Seller A and Seller B attempt to transition different orders containing this product to "Packaged" at the exact same millisecond
  * When the requests hit the database
  * Then the system uses a pessimistic lock (or atomic UPDATE ... WHERE count >= 1)
  * And Seller A's request succeeds
  * And Seller B's request receives a graceful "Out of Stock" UI error instead of causing negative inventory.

## 3. Security (Deep RBAC Enforcement)
**Technical User Story**: As an Admin, I want strict backend authorization so that technical users cannot bypass frontend UI restrictions.
* **Scenario: Seller attempts to access financial APIs**
  * Given a user is authenticated with the "Seller" role
  * When they construct a direct API request to an Accountant/Admin endpoint (e.g., GET /api/finances/net-profit)
  * Then the backend middleware intercepts the request
  * And immediately returns a 403 Forbidden response.

## 4. State Anomalies (Quarantine Leakage)
**Technical User Story**: As a Warehouse Worker, I want returned items physically isolated in the database so they cannot accidentally be sold.
* **Scenario: Preventing sale of quarantined goods**
  * Given an item is returned and added to the quarantined_stock integer column
  * When a Seller attempts to manually create a new Meta order for that product
  * Then the system validates the request strictly against the separate vailable_stock column
  * And mathematically prevents the quarantined item from being allocated.

## 5. Data Anomalies (Orphaned Shopify Products)
**Technical User Story**: As an Admin, I want order imports to never fail due to unrecognized product IDs from Shopify.
* **Scenario: Shopify pushes an order with an unknown Product ID**
  * Given Shopify sends an order containing a product not found in the local catalog
  * When the system processes the import
  * Then the system soft-creates a "stub" product record
  * And successfully imports the order
  * And triggers an alert for the Accountant to update the missing "Purchase Price" later.

## 6. Scale Limits (API Rate Limiting)
**Technical User Story**: As a system, I want background jobs to gracefully handle Shopify API rate limits without crashing or losing data.
* **Scenario: Hitting Shopify HTTP 429 limits during batch sync**
  * Given the reconciliation cron job is fetching a large historical batch of orders
  * When Shopify returns an HTTP 429 Too Many Requests error
  * Then the background worker applies an exponential backoff strategy
  * And waits the required duration before retrying
  * And resumes processing exactly where it left off without dropping the batch.
