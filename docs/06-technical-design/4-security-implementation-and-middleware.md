# Deliverable 4: Security Implementation & Middleware (D4) [GLOBAL]

**Project:** SmartReconcile  
**Document ID:** D4-SECURITY-MIDDLEWARE  
**Phase:** 6 — Technical Design (Tier 0)  

---

## 1. Security Architecture & Middleware Pipeline

```mermaid
flowchart TD
    ClientReq[Incoming HTTP Request] --> RateLimiter[Rate Limiter Middleware: Max 5 Failures/15min]
    RateLimiter --> CORSMiddleware[CORS Middleware: Strict Origin Whitelist]
    CORSMiddleware --> JwtFilter[JwtAuthenticationFilter: Read HttpOnly Access Cookie]
    
    JwtFilter --> AuthCheck{JWT Valid?}
    AuthCheck -- No --> Return401[Return HTTP 401 Unauthorized]
    
    AuthCheck -- Yes --> CsrfFilter[CsrfProtectionFilter: Verify X-CSRF-TOKEN]
    CsrfFilter --> CsrfCheck{CSRF Token Matches?}
    CsrfCheck -- No --> Return403[Return HTTP 403 Forbidden]
    
    CsrfCheck -- Yes --> RbacFilter[RBAC Permission Filter: Verify User Role]
    RbacFilter --> RoleCheck{Role Authorized for Endpoint?}
    RoleCheck -- No --> Return403
    
    RoleCheck -- Yes --> InjectTenant[Inject TenantContext into ThreadLocal]
    InjectTenant --> Controller[Execute Controller Action]
```

## 2. Java Security Filter Implementation Details

- **`JwtAuthenticationFilter.java`:** Intercepts HTTP requests, reads the `access_token` HttpOnly cookie, verifies SHA-256 signature, extracts user claims, and sets `SecurityContextHolder.getContext().setAuthentication(...)`.
- **`CsrfProtectionFilter.java`:** Compares incoming `X-CSRF-TOKEN` header against session CSRF secret.
- **`TenantContextHolder.java`:** Stores `tenant_id` in Java `ThreadLocal` memory for implicit multi-tenant SQL data isolation.
