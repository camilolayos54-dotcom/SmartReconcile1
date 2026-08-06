# Deliverable 2: User Flows & Task Flows [MODULE: MOD-DET]

**Module Code:** `MOD-DET` (High-Speed Deterministic Matching Core)  
**Document ID:** D2-USER-FLOWS-MOD-DET  
**Phase:** 4 — System Modeling (Track A)  

---

## 1. Task Flow 1: Sub-Millisecond Event Ingestion & In-Memory Matching

```mermaid
flowchart TD
    Start1["gRPC Stream Event Received"] --> VirtualThread["Spawn Java 21 Virtual Thread Task"]
    VirtualThread --> QueryRedis["Query Redis In-Memory Index for Internal Transaction"]
    QueryRedis --> ExactCheck{"RefID and Exact Amount Match?"}
    
    ExactCheck -- Yes --> SetMatched["Mark State = MATCHED"]
    ExactCheck -- No --> RefCheck{"RefID Match but Amount Differs?"}
    
    RefCheck -- Yes --> SetDisc["Mark State = DISCREPANCY"]
    SetDisc --> PushRedisQueue["Enqueue Payload to MOD-AGT Redis Queue"]
    
    RefCheck -- No --> WindowCheck{"Match within Date Window?"}
    WindowCheck -- Yes --> SetFuzzy["Mark State = MATCHED_FUZZY"]
    WindowCheck -- No --> SetUnmatched["Mark State = UNMATCHED_BANK"]
    
    SetMatched --> AsyncPersist["Async Commit to PostgreSQL Audit Ledger"]
    SetFuzzy --> AsyncPersist
    SetUnmatched --> AsyncPersist
    PushRedisQueue --> AsyncPersist
    AsyncPersist --> EndFlow1["Task Flow Complete"]
```

## 2. Task Flow 2: Double-Entry Validation of AI Journal Proposals

```mermaid
flowchart TD
    Start2["Receive AI Proposal via gRPC"] --> ExtractLines["Extract Debit and Credit Array Items"]
    ExtractLines --> SumMath["Calculate Sum Debits and Sum Credits"]
    SumMath --> DoubleEntryCheck{"Sum Debits Equal Sum Credits?"}
    
    DoubleEntryCheck -- Yes --> SavePending["Save Proposal State = PENDING_APPROVAL in DB"]
    SavePending --> EmitWS["Emit WebSocket Event to MOD-UI Review Queue"]
    EmitWS --> EndFlow2["Task Flow Complete"]
    
    DoubleEntryCheck -- No --> RejectEntry["Throw InvalidAccountingEntryException"]
    RejectEntry --> AuditReject["Log Audit Failure: AI Proposal Rejected"]
    AuditReject --> AlertUI["Send Security Alert Toast to MOD-UI"]
    AlertUI --> EndFlow2
```
