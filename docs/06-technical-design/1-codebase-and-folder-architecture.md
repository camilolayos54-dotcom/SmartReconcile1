# Deliverable 1: Codebase & Folder Architecture (D1) [GLOBAL]

**Project:** SmartReconcile  
**Document ID:** D1-CODEBASE-FOLDER-ARCHITECTURE  
**Phase:** 6 — Technical Design (Tier 0 Structural Foundations)  

---

## 1. Physical Monorepo Folder Tree

```
smartreconcile/
├── .github/
│   └── workflows/
│       ├── ci-backend.yml
│       ├── ci-python.yml
│       └── ci-frontend.yml
├── docker-compose.yml
├── README.md
├── proto/
│   └── reconciliation.proto
├── backend-core/
│   ├── pom.xml
│   └── src/
│       ├── main/
│       │   ├── java/com/smartreconcile/
│       │   │   ├── SmartReconcileApplication.java
│       │   │   ├── engine/
│       │   │   │   ├── DeterministicMatcher.java
│       │   │   │   ├── VirtualThreadExecutorConfig.java
│       │   │   │   └── MemoryIndexManager.java
│       │   │   ├── ledger/
│       │   │   │   ├── model/
│       │   │   │   │   ├── TransactionLedger.java
│       │   │   │   │   ├── ReconciliationMatch.java
│       │   │   │   │   └── AuditLog.java
│       │   │   │   ├── repository/
│       │   │   │   │   ├── LedgerRepository.java
│       │   │   │   │   └── AuditLogRepository.java
│       │   │   │   └── AccountingGuardrail.java
│       │   │   ├── grpc/
│       │   │   │   ├── StatementIngestionGrpcServer.java
│       │   │   │   └── AgenticDiscrepancyGrpcServer.java
│       │   │   ├── security/
│       │   │   │   ├── JwtAuthenticationFilter.java
│       │   │   │   ├── CsrfProtectionFilter.java
│       │   │   │   └── SecurityConfig.java
│       │   │   └── api/
│       │   │       ├── DashboardApiController.java
│       │   │       ├── DiscrepancyApiController.java
│       │   │       └── TemplateApiController.java
│       │   └── resources/
│       │       ├── application.yml
│       │       └── db/migration/
│       │           └── V1__init_schema.sql
│       └── test/java/com/smartreconcile/
│           ├── engine/DeterministicMatcherTest.java
│           └── ledger/AccountingGuardrailTest.java
├── ai-coprocessor/
│   ├── pyproject.toml
│   ├── requirements.txt
│   ├── main.py
│   └── app/
│       ├── parser/
│       │   ├── pdf_vlm_parser.py
│       │   └── template_engine.py
│       ├── agent/
│       │   ├── discrepancy_agent.py
│       │   └── tools/
│       │       ├── fx_tool.py
│       │       ├── fee_tool.py
│       │       └── timezone_tool.py
│       ├── grpc_client/
│       │   └── grpc_client_stubs.py
│       └── config.py
└── web-ui/
    ├── package.json
    ├── tailwind.config.js
    ├── vite.config.js
    └── src/
        ├── App.jsx
        ├── main.jsx
        ├── components/
        │   ├── ui/ (Button, Input, Badge, Card, Modal)
        │   └── layout/ (HeaderNavbar, Sidebar, AppShell)
        ├── pages/
        │   ├── LandingPage.jsx
        │   ├── LoginPage.jsx
        │   ├── OnboardingPage.jsx
        │   ├── DashboardPage.jsx
        │   ├── IngestionPage.jsx
        │   ├── DiscrepanciesPage.jsx
        │   ├── TemplatesPage.jsx
        │   └── AuditLogsPage.jsx
        └── services/
            ├── api.js
            └── websocket.js
```
