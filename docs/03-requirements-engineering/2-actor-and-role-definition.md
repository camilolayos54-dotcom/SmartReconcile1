# Actor & Role Definition (Deliverable 2)

**Project:** SmartReconcile  
**Document ID:** D2-ACTOR-ROLE-DEFINITION  
**Phase:** 3 — Requirements Engineering (Layer 1)  

---

## 1. Human Actor Catalog

| Actor Code | Role Name | Description | Key System Responsibilities |
|---|---|---|---|
| `ACT-FIN` | **Finance Analyst** | Front-line finance team member responsible for day-to-day reconciliation review. | Uploads bank statements, inspects unmatched items, reviews AI discrepancy explanations, approves routine adjustments. |
| `ACT-MGR` | **FinOps Manager** | Senior manager responsible for accounting period closures and high-value approvals. | Approves high-value discrepancy adjustments (> $1,000), signs off on monthly closures, exports ERP journal entries. |
| `ACT-ADM` | **System Administrator** | Technical administrator managing platform settings and user access. | Manages RBAC permissions, configures bank statement parsing rules, monitors gRPC pipeline health. |

## 2. System (Automated) Actor Catalog

| Actor Code | System Actor Name | Description | Key System Responsibilities |
|---|---|---|---|
| `SYS-ING` | **Ingestion Worker** | Python worker process parsing uploaded statement files. | Converts PDF/CSV/MT940 files into structured JSON events and emits gRPC payloads. |
| `SYS-DET` | **Deterministic Engine** | Java 21 high-concurrency matching core. | Matches internal ledgers with bank events in <1ms; categorizes records into Matched/Discrepancy states. |
| `SYS-AGT` | **Agentic AI Coprocessor** | Python AI agent process evaluating unmatched records. | Executes tool calls (FX, fee schedules), computes root cause, generates balancing adjustment proposals. |

## 3. RBAC Permission Matrix

| Function / Action | Finance Analyst (`ACT-FIN`) | FinOps Manager (`ACT-MGR`) | System Admin (`ACT-ADM`) |
|---|---|---|---|
| Upload Bank Statements | **ALLOWED** | **ALLOWED** | **ALLOWED** |
| View Reconciliation Dashboard | **ALLOWED** | **ALLOWED** | **ALLOWED** |
| Approve Standard Adjustment (<$1,000) | **ALLOWED** | **ALLOWED** | DENIED |
| Approve High-Value Adjustment (>$1,000) | DENIED | **ALLOWED** | DENIED |
| Re-run AI Discrepancy Analysis | **ALLOWED** | **ALLOWED** | **ALLOWED** |
| Export Journal Entries to ERP | DENIED | **ALLOWED** | DENIED |
| Manage User Roles & gRPC Keys | DENIED | DENIED | **ALLOWED** |
