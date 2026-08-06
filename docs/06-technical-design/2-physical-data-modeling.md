# Deliverable 2: Physical Data Modeling (SQL DDL & Indexes) (D2) [GLOBAL]

**Project:** SmartReconcile  
**Document ID:** D2-PHYSICAL-DATA-MODELING  
**Phase:** 6 — Technical Design (Tier 0)  

---

## 1. Raw PostgreSQL SQL DDL Schema Script (`V1__init_schema.sql`)

```sql
-- Flyway Database Migration: V1__init_schema.sql
-- Database: PostgreSQL 16+

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. Multi-Tenant Organization Table
CREATE TABLE tenants (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    company_name VARCHAR(255) NOT NULL,
    base_currency VARCHAR(3) NOT NULL DEFAULT 'USD',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Bank Accounts Table
CREATE TABLE bank_accounts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    bank_name VARCHAR(150) NOT NULL,
    account_number_masked VARCHAR(50) NOT NULL,
    currency VARCHAR(3) NOT NULL DEFAULT 'USD',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. Bank Statement Batches Header Table
CREATE TABLE bank_statement_batches (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    bank_account_id UUID NOT NULL REFERENCES bank_accounts(id) ON DELETE CASCADE,
    file_name VARCHAR(255) NOT NULL,
    format_type VARCHAR(20) NOT NULL, -- PDF, CSV, MT940, BAI2
    status VARCHAR(30) NOT NULL DEFAULT 'INGESTED',
    opening_balance NUMERIC(18, 4) NOT NULL DEFAULT 0.0000,
    closing_balance NUMERIC(18, 4) NOT NULL DEFAULT 0.0000,
    uploaded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 4. Bank Statement Line Items Table
CREATE TABLE bank_statement_lines (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    batch_id UUID NOT NULL REFERENCES bank_statement_batches(id) ON DELETE CASCADE,
    transaction_date DATE NOT NULL,
    reference_id VARCHAR(100) NOT NULL,
    description TEXT,
    debit_amount NUMERIC(18, 4) NOT NULL DEFAULT 0.0000,
    credit_amount NUMERIC(18, 4) NOT NULL DEFAULT 0.0000,
    match_status VARCHAR(30) NOT NULL DEFAULT 'UNMATCHED_BANK',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 5. Internal Transaction Ledger Table
CREATE TABLE transaction_ledgers (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    transaction_date DATE NOT NULL,
    reference_id VARCHAR(100) NOT NULL,
    description TEXT,
    amount NUMERIC(18, 4) NOT NULL,
    type VARCHAR(10) NOT NULL, -- DEBIT / CREDIT
    status VARCHAR(30) NOT NULL DEFAULT 'UNMATCHED_INTERNAL',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 6. Reconciliation Matches Table
CREATE TABLE reconciliation_matches (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    ledger_id UUID REFERENCES transaction_ledgers(id) ON DELETE SET NULL,
    statement_line_id UUID REFERENCES bank_statement_lines(id) ON DELETE SET NULL,
    match_type VARCHAR(30) NOT NULL, -- MATCHED, MATCHED_FUZZY, DISCREPANCY
    delta_amount NUMERIC(18, 4) NOT NULL DEFAULT 0.0000,
    matched_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 7. Discrepancy Items Table
CREATE TABLE discrepancy_items (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    match_id UUID NOT NULL REFERENCES reconciliation_matches(id) ON DELETE CASCADE,
    root_cause_category VARCHAR(50) NOT NULL,
    delta_amount NUMERIC(18, 4) NOT NULL,
    agent_confidence_score INT NOT NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'PENDING_APPROVAL',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 8. Journal Entry Proposals Header Table
CREATE TABLE journal_entry_proposals (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    discrepancy_id UUID NOT NULL REFERENCES discrepancy_items(id) ON DELETE CASCADE,
    explanation_markdown TEXT NOT NULL,
    status VARCHAR(30) NOT NULL DEFAULT 'PENDING_APPROVAL',
    proposed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    approved_by_user_id UUID
);

-- 9. Journal Entry Proposal Lines Table
CREATE TABLE journal_entry_lines (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    proposal_id UUID NOT NULL REFERENCES journal_entry_proposals(id) ON DELETE CASCADE,
    account_code VARCHAR(30) NOT NULL,
    account_name VARCHAR(100) NOT NULL,
    debit_amount NUMERIC(18, 4) NOT NULL DEFAULT 0.0000,
    credit_amount NUMERIC(18, 4) NOT NULL DEFAULT 0.0000
);

-- 10. Bank Schema Templates Table (MOD-ING-TPL)
CREATE TABLE bank_templates (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    bank_name VARCHAR(150) NOT NULL,
    format_type VARCHAR(20) NOT NULL,
    header_regex_signature VARCHAR(255) NOT NULL,
    column_mapping_json JSONB NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 11. Immutable Audit Logs Table (SOC-2)
CREATE TABLE audit_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    event_type VARCHAR(100) NOT NULL,
    actor_id VARCHAR(100) NOT NULL,
    target_ref_id VARCHAR(100) NOT NULL,
    cryptographic_hash VARCHAR(64) NOT NULL, -- SHA-256
    metadata JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Index Declarations for High-Speed Query Execution
CREATE INDEX idx_ledger_tenant_ref ON transaction_ledgers (tenant_id, reference_id);
CREATE INDEX idx_statement_lines_batch ON bank_statement_lines (batch_id, reference_id);
CREATE INDEX idx_matches_ledger_stmt ON reconciliation_matches (ledger_id, statement_line_id);
CREATE INDEX idx_audit_tenant_hash ON audit_logs (tenant_id, cryptographic_hash);
```
