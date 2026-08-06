# TASK BE-020 — `JwtAuthenticationFilter.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/security/`  
**File Type:** `OncePerRequestFilter` Class  
**Priority:** CRITICAL — Security filter parsing HttpOnly JWT cookie.  
**Depends On:** `TASK_BE_019`  
**Blocks:** Spring Security integration  

---

## 1. Purpose

Intercepts every incoming HTTP request, extracts the `access_token` cookie, validates signature via `JwtService`, and populates Spring's `SecurityContextHolder`.

---

## 2. Step-by-Step Implementation Instructions

1. Create `JwtAuthenticationFilter.java` extending `OncePerRequestFilter`.
2. Extract cookie from `request.getCookies()`.
3. If token valid, set `UsernamePasswordAuthenticationToken` in `SecurityContextHolder`.

---

## 3. Verification Command

```bash
./mvnw test-compile
```
