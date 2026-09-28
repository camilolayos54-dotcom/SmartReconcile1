# TASK BE-022 — `SecurityConfig.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/security/`  
**File Type:** Spring Security `@Configuration`  
**Priority:** CRITICAL — Defines HTTP Security Filter Chain and RBAC rules.  
**Depends On:** `TASK_BE_020`, `TASK_BE_021`  
**Blocks:** All API endpoints  

---

## 1. Purpose

Configures Spring Security `SecurityFilterChain` bean, public vs authenticated route rules, CORS whitelist, stateless session management, and filter registration order.

---

## 2. Step-by-Step Implementation Instructions

1. Create `SecurityConfig.java`.
2. Configure `http.csrf(csrf -> csrf.disable())` (since custom CSRF filter handles it).
3. Configure `sessionManagement(session -> session.sessionCreationPolicy(SessionCreationPolicy.STATELESS))`.
4. Configure `authorizeHttpRequests`: `/api/v1/auth/login` permitAll, `/settings/audit-logs` hasRole('MANAGER'), others authenticated.
5. Add `JwtAuthenticationFilter` and `CsrfProtectionFilter` before `UsernamePasswordAuthenticationFilter`.

---

## 3. Verification Command

```bash
./mvnw test-compile
```
