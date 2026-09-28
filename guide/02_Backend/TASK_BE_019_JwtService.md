# TASK BE-019 — `JwtService.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/security/`  
**File Type:** Spring `@Service` Class  
**Priority:** CRITICAL — JWT AccessToken & RefreshToken creation/validation.  
**Depends On:** `TASK_BE_001`  
**Blocks:** Authentication & RBAC Filters  

---

## 1. Purpose

Generates and validates HMAC-SHA256 signed JWT tokens using JJWT 0.12+.

---

## 2. Step-by-Step Implementation Instructions

1. Create `JwtService.java` in `com/smartreconcile/security/`.
2. Inject `@Value("${app.jwt.secret}")` and expirations.
3. Implement `generateAccessToken(String email, String role)`.
4. Implement `extractEmail(String token)` and `isTokenValid(String token)`.

---

## 3. Verification Command

```bash
./mvnw test-compile
```
