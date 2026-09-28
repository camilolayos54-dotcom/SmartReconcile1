# TASK BE-029 — `DiscrepancyController.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/api/`  
**File Type:** `@RestController` Class  
**Priority:** HIGH — Handles `/api/v1/discrepancies` (list, approve, reject).  
**Depends On:** `TASK_BE_013`, `TASK_BE_024`  
**Blocks:** Discrepancy review UI  

---

## 1. Purpose

Exposes endpoints for listing pending discrepancy items, reviewing AI step-by-step reasoning cards, and executing single-click approvals.

---

## 2. Step-by-Step Implementation Instructions

1. Create `DiscrepancyController.java`.
2. Implement `@GetMapping("/api/v1/discrepancies")` with pagination.
3. Implement `@PostMapping("/api/v1/discrepancies/{id}/approve")`:
   - Validate double-entry via `AccountingGuardrail`.
   - Update proposal status to `RESOLVED_APPROVED`.
   - Record immutable SHA-256 hash in `AuditLog`.

---

## 3. Verification Command

```bash
./mvnw test-compile
```
