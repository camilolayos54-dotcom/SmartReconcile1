# TASK BE-028 — `IngestController.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/api/`  
**File Type:** `@RestController` Class  
**Priority:** HIGH — Handles `/api/v1/ingest/upload` multipart file ingestion.  
**Depends On:** `TASK_BE_009`, `TASK_BE_026`  
**Blocks:** Statement ingestion UI  

---

## 1. Purpose

Receives multipart statement uploads (PDF, CSV, MT940), validates MIME type, enforces 50MB size limit, and dispatches batch processing.

---

## 2. Step-by-Step Implementation Instructions

1. Create `IngestController.java` annotated with `@RestController` and `@RequestMapping("/api/v1/ingest")`.
2. Implement `@PostMapping("/upload")`:
   - Enforce file size <= 50MB.
   - Save `BankStatementBatch` record to PostgreSQL.
   - Dispatch file payload to parsing worker.

---

## 3. Verification Command

```bash
./mvnw test-compile
```
