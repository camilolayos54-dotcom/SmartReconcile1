### Phase 6 Brief: Technical Design & Physical Specification

**Project:** SmartReconcile (Hybrid Deterministic & Agentic Transactional Reconciliation Engine)  
**Phase:** 6 — Technical Design  
**Status:** Complete — Ready for Sprint Implementation  

---

### Executive Summary

Phase 6 defines the physical codebase structure, database migration scripts, security middleware implementations, OpenAPI/Swagger specifications, and frontend state management patterns for **SmartReconcile**.

### Technical Design Specifications

1. **Monorepo Directory Layout:**
   - `/proto`: Protobuf contract files (`reconciliation.proto`).
   - `/backend-core`: Maven Java 21 Spring Boot service.
   - `/ai-coprocessor`: Python 3.11 Poetry/Pip FastAPI service.
   - `/web-ui`: Vite + React + Tailwind CSS SPA frontend.
2. **Database Migrations:**
   - Managed via **Flyway / Liquibase** SQL scripts (`V1__init_schema.sql` creating `tenants`, `bank_statement_batches`, `bank_statement_lines`, `transaction_ledgers`, `reconciliation_matches`, `discrepancy_items`, `journal_entry_proposals`, `bank_templates`, and `audit_logs`).
3. **Security Middleware & Headers:**
   - Spring Security & FastAPI CORS middleware.
   - JWT validation filter reading HttpOnly `access_token` cookies.
   - CSRF protection filter verifying `X-CSRF-TOKEN` headers.
