# Deliverable 9: API Conceptual Design [MODULE: MOD-UI & SYSTEM-WIDE]

**Module Code:** `MOD-UI` / Global System API Specs  
**Document ID:** D9-API-CONCEPTUAL-DESIGN  
**Phase:** 4 — System Modeling (Track B)  

---

## 1. REST API Specification (Frontend React <-> Backend Java Core)

### A. Authentication & Session Endpoints
- `POST /api/v1/auth/login`
  - **Request Body:** `{ "email": "analyst@fintech.com", "password": "SecretPassword123!" }`
  - **Response 200 OK:** `{ "user": { "id": "uuid", "email": "...", "role": "ROLE_ANALYST" } }` (Sets HttpOnly Cookie `access_token` and `refresh_token`).
- `POST /api/v1/auth/logout`
  - **Response 200 OK:** Revokes refresh token in Redis and clears HttpOnly cookies.

### B. Ingestion & Template Endpoints
- `POST /api/v1/ingest/upload`
  - **Headers:** `Content-Type: multipart/form-data`
  - **Payload:** File binary (`.pdf`, `.csv`, `.mt940`), `bank_account_id` (UUID).
  - **Response 200 OK:** `{ "batch_id": "uuid", "status": "INGESTED", "total_rows": 1500, "template_matched": true }`
- `GET /api/v1/templates`
  - **Response 200 OK:** List of active bank parsing schemas in `MOD-ING-TPL`.
- `POST /api/v1/templates/create`
  - **Request Body:** `{ "bank_name": "Chase Bank", "format_type": "CSV", "header_regex": "^Date,Ref,Amount", "column_mapping": { "date": 0, "ref": 1, "amount": 3 } }`
  - **Response 201 Created:** `{ "template_id": "uuid", "status": "ACTIVE" }`

### C. Discrepancy & Approval Endpoints
- `GET /api/v1/discrepancies`
  - **Query Params:** `status=PENDING_APPROVAL&limit=20&page=1`
  - **Response 200 OK:** Page of discrepancy items with side-by-side transaction values and AI reasoning cards.
- `POST /api/v1/discrepancies/{id}/approve`
  - **Headers:** `X-CSRF-TOKEN: token`
  - **Response 200 OK:** `{ "discrepancy_id": "uuid", "status": "RESOLVED_APPROVED", "audit_hash": "0x7f8a..." }`
- `POST /api/v1/discrepancies/{id}/reject`
  - **Request Body:** `{ "reason": "Incorrect Fee Category", "manual_note": "Bank confirmed billing error" }`
  - **Response 200 OK:** `{ "discrepancy_id": "uuid", "status": "RESOLVED_REJECTED" }`

---

## 2. Shared Protobuf Schema (`proto/reconciliation.proto`)

```protobuf
syntax = "proto3";

package com.smartreconcile.grpc;

option java_multiple_files = true;
option java_package = "com.smartreconcile.grpc";

// Ingestion Stream Service
service StatementIngestionService {
  rpc StreamBankEvents (stream BankTransactionEvent) returns (IngestionResponse);
}

// AI Coprocessor Service
service AgenticDiscrepancyService {
  rpc SubmitAdjustmentProposal (JournalEntryProposal) returns (ProposalAck);
}

message BankTransactionEvent {
  string event_id = 1;
  string tenant_id = 2;
  string bank_account_id = 3;
  string transaction_date = 4; // ISO-8601 YYYY-MM-DD
  string reference_id = 5;
  string description = 6;
  double debit_amount = 7;
  double credit_amount = 8;
  string currency = 9;
}

message IngestionResponse {
  string batch_id = 1;
  int32 total_events_received = 2;
  string status = 3;
}

message JournalEntryProposal {
  string proposal_id = 1;
  string discrepancy_id = 2;
  string root_cause_category = 3;
  int32 confidence_score = 4;
  string reasoning_markdown = 5;
  repeated JournalLine lines = 6;
}

message JournalLine {
  string account_code = 1;
  string account_name = 2;
  double debit_amount = 3;
  double credit_amount = 4;
}

message ProposalAck {
  string proposal_id = 1;
  string status = 2; // VALIDATED or REJECTED
  string audit_hash = 3;
}
```
