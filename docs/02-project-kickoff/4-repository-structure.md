# Repository Structure & Directory Architecture (Deliverable 4)

**Project:** SmartReconcile  
**Document ID:** D4-REPOSITORY-STRUCTURE  
**Phase:** 2 — Project Kickoff  

---

## 1. Monorepo Directory Layout

```
smartreconcile/
├── .github/
│   └── workflows/              # CI/CD GitHub Actions pipelines
├── proto/
│   └── reconciliation.proto    # Shared Protobuf schemas for gRPC
├── backend-core/               # Java 21 Spring Boot Project
│   ├── src/main/java/com/smartreconcile/
│   │   ├── engine/             # High-speed deterministic matcher
│   │   ├── ledger/             # Internal accounting ledger model
│   │   ├── grpc/               # gRPC server endpoints
│   │   └── api/                # REST endpoints for React UI
│   ├── src/test/               # JUnit 5 & Integration tests
│   └── pom.xml / build.gradle
├── ai-coprocessor/             # Python 3.11 FastAPI Project
│   ├── app/
│   │   ├── parser/             # PyMuPDF / Vision-LLM bank statement parser
│   │   ├── agent/              # Discrepancy resolution AI agent (LangChain)
│   │   ├── tools/              # FX rate & bank fee lookup tools
│   │   └── grpc_client/        # gRPC client for Java engine
│   ├── tests/                  # Pytest suite
│   ├── requirements.txt
│   └── main.py
├── web-ui/                     # React + Tailwind CSS SPA
│   ├── src/
│   │   ├── components/         # Reusable Tailwind React components
│   │   ├── pages/              # Reconciliation dashboard, audit view
│   │   ├── services/           # API fetch/axios integration
│   │   └── App.jsx
│   ├── tailwind.config.js
│   ├── package.json
│   └── vite.config.js
└── docs/                       # Project lifecycle documentation (Phase 0 - 11)
```
