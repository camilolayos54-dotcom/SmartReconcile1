# TASK BE-041 — `ingestion_servicer.py`

**Module:** `ai-coprocessor/app/grpc_server/`  
**File Type:** Python gRPC Servicer Class  
**Priority:** HIGH — Streams extracted transaction events to Java backend core.  
**Depends On:** `TASK_BE_033`, `TASK_BE_037`  
**Blocks:** Python <-> Java gRPC event pipeline  

---

## 1. Purpose

Streams parsed transaction events over gRPC (`StreamBankEvents`) to Java `backend-core` for sub-millisecond matching.

---

## 2. Step-by-Step Implementation Instructions

1. Create `app/grpc_server/ingestion_servicer.py` inheriting from generated `reconciliation_pb2_grpc.StatementIngestionServiceServicer`.

---

## 3. Verification Command

```bash
python -m py_compile app/grpc_server/ingestion_servicer.py
```
