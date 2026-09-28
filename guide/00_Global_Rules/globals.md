# Global Coding Rules & Development Guidelines

**Project:** SmartReconcile  
**Target:** Manual Step-by-Step Implementation Guide  

---

## 1. Core Principles & Coding Philosophy
- **Clean Architecture & DDD:** Strict separation of Concerns. Domain entities must remain pure POJOs/Records without framework dependencies where possible.
- **Double-Entry Accounting Guardrail:** Every financial adjustment MUST satisfy $\sum \text{Debits} = \sum \text{Credits}$. Imbalanced entries must throw `InvalidAccountingEntryException`.
- **Multi-Tenant Isolation:** Every SQL table (except system metadata) must contain `tenant_id UUID`. All queries must filter by `tenant_id`.
- **Zero Raw Secrets in Code:** Passwords, JWT keys, and API tokens must be injected via environment variables (`.env`).
- **Standardized Error Responses:** APIs must return standard RFC 7807 error JSON objects with `X-Correlation-ID`.

---

## 2. Technology Stack & Framework Versions
- **Backend Core:** Java 21 (Virtual Threads), Spring Boot 3.2+, Maven, PostgreSQL 16, Redis 7, gRPC.
- **AI Coprocessor:** Python 3.11+, FastAPI, LangChain, PyMuPDF, Protoc gRPC.
- **Frontend SPA:** React 18 (Vite), Tailwind CSS (Bancolombia Navy `#0B192C` / Yellow `#FFD200`), Zustand state management, Axios, Lucide-React Icons.
