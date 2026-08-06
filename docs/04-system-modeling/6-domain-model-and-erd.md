# Deliverable 6: Domain Model & Conceptual ERD [GLOBAL]

**Project:** SmartReconcile  
**Document ID:** D6-DOMAIN-MODEL-ERD  
**Phase:** 4 — System Modeling (Track B Data Architecture)  

---

## 1. Entity Relationship Diagram (Mermaid ERD)

```mermaid
erDiagram
    TENANT ||--o{ BANK_ACCOUNT : owns
    TENANT ||--o{ TRANSACTION_LEDGER : records
    TENANT ||--o{ BANK_STATEMENT_BATCH : ingests
    TENANT ||--o{ BANK_TEMPLATE : configures

    BANK_STATEMENT_BATCH ||--o{ BANK_STATEMENT_LINE : contains
    BANK_ACCOUNT ||--o{ BANK_STATEMENT_BATCH : receives

    TRANSACTION_LEDGER ||--o| RECONCILIATION_MATCH : participates
    BANK_STATEMENT_LINE ||--o| RECONCILIATION_MATCH : participates

    RECONCILIATION_MATCH ||--o| DISCREPANCY_ITEM : generates
    DISCREPANCY_ITEM ||--o| JOURNAL_ENTRY_PROPOSAL : has

    JOURNAL_ENTRY_PROPOSAL ||--o{ JOURNAL_ENTRY_LINE : contains
    TENANT ||--o{ AUDIT_LOG : tracks

    TENANT {
        uuid id PK
        string company_name
        string base_currency
        timestamp created_at
    }

    BANK_ACCOUNT {
        uuid id PK
        uuid tenant_id FK
        string bank_name
        string account_number_masked
        string currency
    }

    BANK_STATEMENT_BATCH {
        uuid id PK
        uuid tenant_id FK
        uuid bank_account_id FK
        string file_name
        string format_type
        string status
        decimal opening_balance
        decimal closing_balance
        timestamp uploaded_at
    }

    BANK_STATEMENT_LINE {
        uuid id PK
        uuid batch_id FK
        date transaction_date
        string reference_id
        string description
        decimal debit_amount
        decimal credit_amount
        string match_status
    }

    TRANSACTION_LEDGER {
        uuid id PK
        uuid tenant_id FK
        date transaction_date
        string reference_id
        string description
        decimal amount
        string type
        string status
    }

    RECONCILIATION_MATCH {
        uuid id PK
        uuid ledger_id FK
        uuid statement_line_id FK
        string match_type
        decimal delta_amount
        timestamp matched_at
    }

    DISCREPANCY_ITEM {
        uuid id PK
        uuid match_id FK
        string root_cause_category
        decimal delta_amount
        int agent_confidence_score
        string status
    }

    JOURNAL_ENTRY_PROPOSAL {
        uuid id PK
        uuid discrepancy_id FK
        string explanation_markdown
        string status
        timestamp proposed_at
        uuid approved_by_user_id
    }

    JOURNAL_ENTRY_LINE {
        uuid id PK
        uuid proposal_id FK
        string account_code
        string account_name
        decimal debit_amount
        decimal credit_amount
    }

    BANK_TEMPLATE {
        uuid id PK
        uuid tenant_id FK
        string bank_name
        string format_type
        string header_regex_signature
        jsonb column_mapping_json
        string status
    }

    AUDIT_LOG {
        uuid id PK
        uuid tenant_id FK
        string event_type
        string actor_id
        string target_ref_id
        string cryptographic_hash
        jsonb metadata
        timestamp created_at
    }
```

## 2. Relational Schema Data Dictionary

1. **`tenants`:** Multi-tenant organization isolation table.
2. **`bank_statement_batches`:** Metadata header for uploaded CSV/PDF/MT940 files.
3. **`bank_statement_lines`:** Parsed transaction rows from bank statements.
4. **`transaction_ledgers`:** Internal database charges and credits.
5. **`reconciliation_matches`:** Result table associating internal ledgers with bank lines.
6. **`discrepancy_items`:** Unmatched items requiring AI agent diagnosis.
7. **`journal_entry_proposals` & `journal_entry_lines`:** AI-proposed balancing entries verifying $\sum Debits = \sum Credits$.
8. **`bank_templates`:** Cached schema rules for `MOD-ING-TPL`.
9. **`audit_logs`:** SOC-2 compliant append-only event log.
