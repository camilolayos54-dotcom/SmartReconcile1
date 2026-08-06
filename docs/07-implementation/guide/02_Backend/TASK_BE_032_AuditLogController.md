# TASK BE-032 — `AuditLogController.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/api/`  
**File Type:** `@RestController` Class  
**Priority:** MEDIUM — Handles `/api/v1/audit-logs` and SOC-2 PDF report exports.  
**Depends On:** `TASK_BE_016`  
**Blocks:** Audit log UI viewer  

---

## 1. Purpose

Exposes paginated query access to immutable audit logs and generates signed PDF compliance reports.

---

## 2. Step-by-Step Implementation Instructions

1. Create `AuditLogController.java`.
2. Implement `@GetMapping("/api/v1/audit-logs")`.
3. Implement `@GetMapping(value = "/api/v1/audit-logs/export-pdf", produces = MediaType.APPLICATION_PDF_VALUE)`.

---

## 3. Verification Command

```bash
./mvnw test-compile
```
