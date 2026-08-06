# Deliverable 7: System Sequence Diagrams [MODULE: MOD-DET]

**Module Code:** `MOD-DET`  
**Document ID:** D7-SEQUENCE-DIAGRAMS-MOD-DET  
**Phase:** 4 — System Modeling (Track B)  

---

## 1. System Sequence Diagram: High-Speed Ingestion & Deterministic Match Stream

```mermaid
sequenceDiagram
    autonumber
    actor Analyst as Finance Analyst
    participant UI as React UI (MOD-UI)
    participant ING as Ingestion Worker (MOD-ING)
    participant DET as Matching Core (MOD-DET - Java 21)
    participant REDIS as Redis Cache & Queue
    participant DB as PostgreSQL DB
    participant AGT as AI Agent (MOD-AGT)

    Analyst->>UI: Upload Bank Statement (CSV/PDF)
    UI->>ING: POST /api/v1/ingest/upload
    ING->>ING: Parse & Validate Rows
    ING->>DET: gRPC StreamBankEvents(TransactionEvents)
    
    loop Per Transaction Event (Java Virtual Thread)
        DET->>REDIS: Query Exact RefID + Amount Key Index
        alt Exact Match Found
            REDIS-->>DET: Match Hit (Internal Ledger ID)
            DET->>DB: INSERT INTO reconciliation_matches (MATCHED)
        else Amount Discrepancy (RefID Matches, Amount Delta != 0)
            REDIS-->>DET: RefID Hit, Delta = $3.50
            DET->>REDIS: LPUSH queue:discrepancies:ai (Payload)
            DET->>DB: INSERT INTO reconciliation_matches (DISCREPANCY)
        else No Match Found
            DET->>DB: INSERT INTO reconciliation_matches (UNMATCHED_BANK)
        end
    end

    DET-->>ING: gRPC StreamResponse (Batch Complete)
    ING-->>UI: HTTP 200 OK (Ingestion Metrics)
    DET->>UI: WebSocket Push (KPI Update: % Matched Rate)
    REDIS->>AGT: Async Pop Discrepancy Payload
```

## 2. System Sequence Diagram: AI Proposal Validation & Operator Sign-Off

```mermaid
sequenceDiagram
    autonumber
    actor Analyst as Finance Analyst
    participant UI as React UI (MOD-UI)
    participant AGT as AI Agent (MOD-AGT)
    participant DET as Java Core (MOD-DET)
    participant DB as PostgreSQL DB

    AGT->>AGT: Multi-Tool Fee & FX Investigation
    AGT->>DET: gRPC SubmitAdjustmentProposal(JournalEntryProposal)
    
    DET->>DET: Validate Double-Entry Math (Sum Debits == Sum Credits)
    alt Double-Entry Valid
        DET->>DB: INSERT INTO journal_entry_proposals (PENDING_APPROVAL)
        DET->>UI: WebSocket Push (New Discrepancy Alert)
        Analyst->>UI: Inspect Side-by-Side Reasoning Card
        Analyst->>UI: Click 'Approve Adjustment'
        UI->>DET: POST /api/v1/discrepancies/{id}/approve (JWT + CSRF)
        DET->>DB: UPDATE journal_entry_proposals SET status = RESOLVED_APPROVED
        DET->>DB: INSERT INTO audit_logs (Immutable Hash)
        DET-->>UI: HTTP 200 OK
        UI-->>Analyst: Show Success Toast & Clear Row
    else Imbalance Detected (Debits != Credits)
        DET->>DB: INSERT INTO audit_logs (REJECTED_VALIDATION_FAILURE)
        DET-->>AGT: gRPC ProposalAck (REJECTED)
    end
```
