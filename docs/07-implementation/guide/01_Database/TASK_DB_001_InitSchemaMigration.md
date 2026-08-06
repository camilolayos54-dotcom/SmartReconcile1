# TASK DB-001 — `V1__init_schema.sql`

**Module:** `backend-core/src/main/resources/db/migration/`  
**File Type:** Flyway SQL DDL Migration  
**Priority:** CRITICAL — Establishes the entire database structure for the application.  
**Depends On:** PostgreSQL 16 container running  
**Blocks:** All JPA entities, repositories, and database integration tests  

---

## 1. Purpose

This file is the initial Flyway migration script responsible for creating all 11 core relational tables (`tenants`, `bank_accounts`, `bank_statement_batches`, `bank_statement_lines`, `transaction_ledgers`, `reconciliation_matches`, `discrepancy_items`, `journal_entry_proposals`, `journal_entry_lines`, `bank_templates`, `audit_logs`). It enables the UUID extension and enforces foreign key relationships and NUMERIC precision for financial balance integrity.

---

## 2. Step-by-Step Implementation Instructions

### Step 1: Create Migration Folder Structure
1. In `backend-core/src/main/resources/`, ensure the directory path `db/migration/` exists.
2. Create the file `V1__init_schema.sql` (note the double underscore after `V1`).

### Step 2: Enable UUID Extension
1. At the top of the SQL file, write the extension declaration to support `uuid_generate_v4()` for primary keys:
   - Command: `CREATE EXTENSION IF NOT EXISTS "uuid-ossp";`

### Step 3: Declare Core Tables in Order of Dependency
1. **`tenants`:** Create table with `id UUID PRIMARY KEY`, `company_name VARCHAR(255)`, `base_currency VARCHAR(3)`, and `created_at TIMESTAMP WITH TIME ZONE`.
2. **`bank_accounts`:** Create table with foreign key `tenant_id REFERENCES tenants(id) ON DELETE CASCADE`, `bank_name`, `account_number_masked`, `currency`.
3. **`bank_statement_batches`:** Create table linking to `tenant_id` and `bank_account_id`, with `file_name`, `format_type`, `status`, `opening_balance NUMERIC(18, 4)`, `closing_balance NUMERIC(18, 4)`.
4. **`bank_statement_lines`:** Create table linking to `batch_id`, storing `transaction_date DATE`, `reference_id VARCHAR(100)`, `description`, `debit_amount NUMERIC(18, 4)`, `credit_amount NUMERIC(18, 4)`, and `match_status`.
5. **`transaction_ledgers`:** Create internal charges table with `tenant_id`, `transaction_date`, `reference_id`, `amount NUMERIC(18, 4)`, `type` (DEBIT/CREDIT), and `status`.
6. **`reconciliation_matches`:** Create matching table linking `ledger_id` and `statement_line_id`, storing `match_type`, `delta_amount NUMERIC(18, 4)`, and `matched_at`.
7. **`discrepancy_items`:** Create discrepancy table linking `match_id`, storing `root_cause_category`, `delta_amount`, `agent_confidence_score INT`, and `status`.
8. **`journal_entry_proposals` & `journal_entry_lines`:** Create balancing proposal tables storing `explanation_markdown`, `account_code`, `debit_amount`, and `credit_amount`.
9. **`bank_templates`:** Create template schema table with `header_regex_signature` and `column_mapping_json JSONB`.
10. **`audit_logs`:** Create immutable audit table storing `cryptographic_hash VARCHAR(64)`, `metadata JSONB`, and timestamps.

---

## 3. Verification Checklist

| # | Check Condition | Risk if Failed |
|---|---|---|
| 1 | Double underscore `V1__` in filename | Flyway ignores migration file completely |
| 2 | `NUMERIC(18, 4)` used for all amounts | Floating point rounding errors corrupt ledger totals |
| 3 | All tables include `tenant_id` foreign keys | Data leakage across tenant organizations |
| 4 | Foreign keys declared with `ON DELETE CASCADE` or `SET NULL` | Referential integrity exceptions on batch deletion |

---

## 4. Verification Command

Run Flyway migration check via Maven:
```bash
./mvnw flyway:info
```
Expected output: `V1__init_schema.sql` marked as `Success`.
