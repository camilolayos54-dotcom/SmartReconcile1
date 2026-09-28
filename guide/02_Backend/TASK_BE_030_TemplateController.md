# TASK BE-030 — `TemplateController.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/api/`  
**File Type:** `@RestController` Class  
**Priority:** HIGH — Handles `/api/v1/templates` (CRUD for bank parsing schemas `MOD-ING-TPL`).  
**Depends On:** `TASK_BE_015`  
**Blocks:** Bank template studio UI  

---

## 1. Purpose

Exposes REST endpoints to list, create, edit, and dry-run test reusable bank parsing regex schemas. Requires `ROLE_ADMIN`.

---

## 2. Step-by-Step Implementation Instructions

1. Create `TemplateController.java`.
2. Implement `@GetMapping("/api/v1/templates")` and `@PostMapping("/api/v1/templates")`.
3. Implement `@PostMapping("/api/v1/templates/test-dry-run")` to parse a sample CSV file in memory.

---

## 3. Verification Command

```bash
./mvnw test-compile
```
