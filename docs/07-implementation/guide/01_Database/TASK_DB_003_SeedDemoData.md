# TASK DB-003 — `V3__seed_demo_data.sql`

**Module:** `backend-core/src/main/resources/db/migration/`  
**File Type:** Flyway SQL DML Seed Script  
**Priority:** MEDIUM — Provides initial demo tenant records, acquiring bank accounts, and pre-configured bank parsing schemas (`MOD-ING-TPL`).  
**Depends On:** `TASK_DB_002`  
**Blocks:** Initial UI dashboard rendering and dry-run template tests  

---

## 1. Purpose

Seeds the PostgreSQL database with a primary demonstration tenant (`Acme Fintech Corp`), a default USD acquiring bank account (`Chase Bank USD Clearing`), and pre-configured bank statement parsing schemas (`MOD-ING-TPL` JSON mappings) for standard CSV and MT940 statement layouts.

---

## 2. Step-by-Step Implementation Instructions

### Step 1: Create the SQL Migration File
1. In `backend-core/src/main/resources/db/migration/`, create `V3__seed_demo_data.sql`.

### Step 2: Insert Default Demo Tenant Record
1. Insert fixed UUID tenant record into `tenants`:
   - SQL: `INSERT INTO tenants (id, company_name, base_currency) VALUES ('00000000-0000-0000-0000-000000000001', 'Acme Fintech Corp', 'USD') ON CONFLICT DO NOTHING;`

### Step 3: Insert Default Bank Account
1. Insert primary acquiring bank account record into `bank_accounts`:
   - SQL: `INSERT INTO bank_accounts (id, tenant_id, bank_name, account_number_masked, currency) VALUES ('11111111-1111-1111-1111-111111111111', '00000000-0000-0000-0000-000000000001', 'Chase Bank', '•••• 4829', 'USD') ON CONFLICT DO NOTHING;`

### Step 4: Insert Pre-configured Bank Parsing Schema (`MOD-ING-TPL`)
1. Insert default template record into `bank_templates`:
   - SQL: `INSERT INTO bank_templates (id, tenant_id, bank_name, format_type, header_regex_signature, column_mapping_json, status) VALUES ('22222222-2222-2222-2222-222222222222', '00000000-0000-0000-0000-000000000001', 'Chase Standard CSV', 'CSV', '^Date,RefID,Description,Amount', '{"date": 0, "ref": 1, "description": 2, "amount": 3}', 'ACTIVE') ON CONFLICT DO NOTHING;`

---

## 3. Verification Checklist

| # | Check Condition | Risk if Failed |
|---|---|---|
| 1 | Fixed UUID strings used for seed IDs | Duplicate key errors on repeated migration runs |
| 2 | `ON CONFLICT DO NOTHING` applied to inserts | Flyway fails on test database resets |
| 3 | JSONB mapping format matches `MOD-ING-TPL` parser | Template engine fails during CSV dry-run test |

---

## 4. Verification Command

```bash
./mvnw flyway:info
```
Confirm `V3__seed_demo_data.sql` status is `Success`.
