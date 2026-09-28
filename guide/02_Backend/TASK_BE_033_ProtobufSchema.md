# TASK BE-033 — `proto/reconciliation.proto`

**Module:** `proto/`  
**File Type:** Protocol Buffers Schema v3  
**Priority:** CRITICAL — Defines binary IPC contract between Java and Python.  
**Depends On:** None  
**Blocks:** `TASK_BE_034`, `TASK_BE_035`, `TASK_BE_041`  

---

## 1. Purpose

Declares gRPC services (`StatementIngestionService` and `AgenticDiscrepancyService`) and binary message structures (`BankTransactionEvent`, `JournalEntryProposal`).

---

## 2. Step-by-Step Implementation Instructions

1. In monorepo root, create `proto/reconciliation.proto`.
2. Define `syntax = "proto3";`.
3. Declare `option java_package = "com.smartreconcile.grpc";`.
4. Declare `service StatementIngestionService` and `service AgenticDiscrepancyService`.

---

## 3. Verification Command

Generate Java Protobuf stubs:
```bash
./mvnw protobuf:compile protobuf:compile-custom
```
