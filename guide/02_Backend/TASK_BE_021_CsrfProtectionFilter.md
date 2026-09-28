# TASK BE-021 — `CsrfProtectionFilter.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/security/`  
**File Type:** `OncePerRequestFilter` Class  
**Priority:** HIGH — Verifies `X-CSRF-TOKEN` header on mutating HTTP requests.  
**Depends On:** `TASK_BE_020`  
**Blocks:** Anti-CSRF protection  

---

## 1. Purpose

Validates incoming `X-CSRF-TOKEN` request header on mutating REST methods (`POST`, `PUT`, `DELETE`), rejecting unauthenticated CSRF attempts with HTTP 403 Forbidden.

---

## 2. Step-by-Step Implementation Instructions

1. Create `CsrfProtectionFilter.java` extending `OncePerRequestFilter`.
2. Skip verification for GET/OPTIONS/HEAD methods.
3. Compare header token against user session CSRF secret token.

---

## 3. Verification Command

```bash
./mvnw test-compile
```
