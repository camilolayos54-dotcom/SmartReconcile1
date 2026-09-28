# TASK BE-035 — `AgenticDiscrepancyGrpcServer.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/grpc/`  
**File Type:** `@GrpcService` Class  
**Priority:** HIGH — Receives AI discrepancy proposals via gRPC.  
**Depends On:** `TASK_BE_024`, `TASK_BE_033`  
**Blocks:** Python AI agent proposal transmission  

---

## 1. Purpose

Implements gRPC handler receiving `JournalEntryProposal` from Python AI Coprocessor and validating double-entry math before saving to DB.

---

## 2. Step-by-Step Implementation Instructions

1. Create `AgenticDiscrepancyGrpcServer.java`.
2. Validate proposals via `AccountingGuardrail.validateDoubleEntry(...)`.

---

## 3. Verification Command

```bash
./mvnw test-compile
```
