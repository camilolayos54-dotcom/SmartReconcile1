# Deliverable 11: Authorization & Security Matrix [GLOBAL]

**Project:** SmartReconcile  
**Document ID:** D11-AUTHORIZATION-SECURITY  
**Phase:** 4 — System Modeling (Track C)  

---

## 1. Unified RBAC Authorization Matrix

| UI Route / API Endpoint | HTTP Method | `ROLE_ANALYST` | `ROLE_MANAGER` | `ROLE_ADMIN` | Security Controls Enforced |
|---|---|---|---|---|---|
| `/api/v1/auth/login` | POST | Anonymous | Anonymous | Anonymous | Rate Limiting (5 attempts/15min) |
| `/dashboard` | GET | **ALLOWED** | **ALLOWED** | **ALLOWED** | JWT Cookie + CSRF Token |
| `/ingestion` & `/api/v1/ingest/upload` | POST | **ALLOWED** | **ALLOWED** | **ALLOWED** | PII Redaction, File MIME check |
| `/discrepancies` | GET | **ALLOWED** | **ALLOWED** | **ALLOWED** | Tenant Isolation Filter |
| `/api/v1/discrepancies/{id}/approve` (<$1k) | POST | **ALLOWED** | **ALLOWED** | DENIED | Double-entry check ($\sum D = \sum C$) |
| `/api/v1/discrepancies/{id}/approve` (>$1k) | POST | DENIED | **ALLOWED** | DENIED | High-Value Approval Guard |
| `/templates` & `/api/v1/templates/*` | POST/PUT | DENIED | DENIED | **ALLOWED** | Schema Regex Validation |
| `/settings/audit-logs` | GET | DENIED | **ALLOWED** | **ALLOWED** | Cryptographic Hash Verification |

## 2. Hard Security Controls Summary

1. **Authentication:** JWT Access Token (15m expiration) + Refresh Token (7d rotation in Redis).
2. **Cookie Flags:** `HttpOnly`, `Secure`, `SameSite=Strict` (No `localStorage` token storage).
3. **Cross-Site Request Forgery (CSRF):** `X-CSRF-TOKEN` header required for all mutating endpoints (`POST`, `PUT`, `DELETE`).
4. **Data Isolation:** All database queries include implicit `WHERE tenant_id = :current_tenant_id` constraint.
