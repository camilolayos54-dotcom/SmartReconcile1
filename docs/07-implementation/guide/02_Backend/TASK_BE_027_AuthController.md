# TASK BE-027 — `AuthController.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/api/`  
**File Type:** `@RestController` Class  
**Priority:** HIGH — Handles `/api/v1/auth/login`, `/logout`, and `/refresh`.  
**Depends On:** `TASK_BE_019`, `TASK_BE_026`  
**Blocks:** Frontend authentication  

---

## 1. Purpose

Exposes user login, logout, and token refresh REST endpoints. Sets HttpOnly, Secure, SameSite=Strict `access_token` cookies.

---

## 2. Step-by-Step Implementation Instructions

1. Create `AuthController.java` annotated with `@RestController` and `@RequestMapping("/api/v1/auth")`.
2. Implement `login(@Valid @RequestBody LoginRequest request, HttpServletResponse response)`:
   - Validate credentials.
   - Generate JWT via `JwtService`.
   - Set `ResponseCookie` with `HttpOnly(true)` and `SameSite("Strict")`.

---

## 3. Verification Command

```bash
./mvnw test-compile
```
