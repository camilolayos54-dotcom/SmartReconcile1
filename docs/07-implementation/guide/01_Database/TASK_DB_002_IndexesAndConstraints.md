# TASK DB-002 — `V2__add_indexes.sql`

**Module:** `backend-core/src/main/resources/db/migration/`  
**File Type:** Flyway SQL DDL Migration  
**Priority:** HIGH — Guarantees sub-millisecond query performance during >10,000 TPS matching runs.  
**Depends On:** `TASK_DB_001` (`V1__init_schema.sql`)  
**Blocks:** Performance load testing and high-speed in-memory indexing  

---

## 1. Purpose

This migration script builds specialized B-Tree and Hash indexes on foreign keys, transaction reference IDs, date ranges, and cryptographic audit hashes. Without these explicit indexes, PostgreSQL reverts to sequential full table scans, causing database CPU spikes and increasing query latency from <1.0ms to >500ms when table sizes exceed 100,000 rows.

---

## 2. Step-by-Step Implementation Instructions

### Step 1: Create the SQL Migration File
1. Navigate to `backend-core/src/main/resources/db/migration/`.
2. Create `V2__add_indexes.sql` (ensure exact double underscore after `V2`).

### Step 2: Add High-Speed Transaction Matching Indexes
1. Add composite index on `transaction_ledgers (tenant_id, reference_id)` to speed up internal ledger lookups by reference code:
   - SQL: `CREATE INDEX idx_ledger_tenant_ref ON transaction_ledgers (tenant_id, reference_id);`
2. Add composite index on `bank_statement_lines (batch_id, reference_id)` to accelerate statement line indexing during batch runs:
   - SQL: `CREATE INDEX idx_statement_lines_batch ON bank_statement_lines (batch_id, reference_id);`
3. Add composite index on `reconciliation_matches (ledger_id, statement_line_id)` to accelerate join queries when fetching matched pairs:
   - SQL: `CREATE INDEX idx_matches_ledger_stmt ON reconciliation_matches (ledger_id, statement_line_id);`

### Step 3: Add Audit & Discrepancy Query Indexes
1. Add index on `audit_logs (tenant_id, cryptographic_hash)` for instant SOC-2 hash verification lookup:
   - SQL: `CREATE INDEX idx_audit_tenant_hash ON audit_logs (tenant_id, cryptographic_hash);`
2. Add index on `discrepancy_items (status, created_at)` for filtering pending review queues in `MOD-UI`:
   - SQL: `CREATE INDEX idx_discrepancy_status_date ON discrepancy_items (status, created_at DESC);`
3. Add index on `bank_templates (tenant_id, header_regex_signature)` for matching incoming bank file headers in `MOD-ING-TPL`:
   - SQL: `CREATE INDEX idx_bank_templates_sig ON bank_templates (tenant_id, header_regex_signature);`

---

## 3. Verification Checklist

| # | Check Condition | Risk if Failed |
|---|---|---|
| 1 | Double underscore `V2__` in filename | Flyway skips index creation completely |
| 2 | Indexes include `tenant_id` prefix | Cross-tenant queries perform full table scan |
| 3 | Date indexes use `DESC` ordering | Dashboard queue pagination performs sorting in memory |

---

## 4. Verification Commands

1. Execute Flyway migration:
   ```bash
   ./mvnw flyway:info
   ```
2. Verify index creation in PostgreSQL terminal (`psql`):
   ```sql
   \d transaction_ledgers
   ```
   Confirm `idx_ledger_tenant_ref` appears under `Indexes:`.
