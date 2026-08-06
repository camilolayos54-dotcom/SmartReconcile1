# Deliverable 7: Cross-Cutting Concerns Strategy (D7) [GLOBAL]

**Project:** SmartReconcile  
**Document ID:** D7-CROSS-CUTTING-CONCERNS  
**Phase:** 5 — Architectural Design (Tier 2)  

---

## 1. Global Security Strategy
- **Authentication:** JWT Access Token (15-min expiration) + Refresh Token (7-day rotation).
- **Token Injection:** Transmitted exclusively via `HttpOnly`, `Secure`, `SameSite=Strict` cookies. Storage in `localStorage` is prohibited.
- **CSRF Protection:** `X-CSRF-TOKEN` header required for all state-mutating requests (`POST`, `PUT`, `DELETE`).
- **PII Scrubbing:** Hashing/redaction middleware in Python `MOD-ING` prior to passing payload images or prompts to external LLM APIs.

## 2. Centralized Observability & Structured Logging
- **Log Format:** Structured JSON logging (SLF4J / Logback in Java, structlog in Python).
- **Trace Context:** Every request injects a `X-Correlation-ID` header (UUID) propagated across React -> Java -> Python -> Database.
- **Audit Persistence:** `audit_logs` table stores immutable append-only logs with SHA-256 cryptographic hashes for SOC-2 Type II compliance.

## 3. Global Exception & Error Handling Strategy
- Standardized REST Error Response Schema across Java and Python APIs:
```json
{
  "timestamp": "2026-08-04T22:00:00Z",
  "status": 422,
  "error": "UNPROCESSABLE_ENTITY",
  "message": "Imbalance Error: Sum of Debits ($3.50) does not equal Sum of Credits ($3.00).",
  "correlation_id": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "path": "/api/v1/discrepancies/approve"
}
```
