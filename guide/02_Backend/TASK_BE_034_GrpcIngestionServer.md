# TASK BE-034 — `StatementIngestionGrpcServer.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/grpc/`  
**File Type:** `@GrpcService` Class  
**Priority:** HIGH — Serves gRPC stream receiver for transaction events.  
**Depends On:** `TASK_BE_025`, `TASK_BE_033`  
**Blocks:** Python -> Java gRPC ingestion pipeline  

---

## 1. Purpose

Implements gRPC server handler receiving `StreamBankEvents` stream from Python ingestion worker.

---

## 2. Step-by-Step Implementation Instructions

1. Create `StatementIngestionGrpcServer.java` extending `StatementIngestionServiceGrpc.StatementIngestionServiceImplBase`.
2. Override `streamBankEvents(...)` delegating received events to `DeterministicMatcher`.

---

## 3. Verification Command

```bash
./mvnw test-compile
```
