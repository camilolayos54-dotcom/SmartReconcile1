# Deliverable 9: Component Diagram — C4 Container Model (D9) [GLOBAL]

**Project:** SmartReconcile  
**Document ID:** D9-C4-CONTAINER-MODEL  
**Phase:** 5 — Architectural Design (Tier 2 C4 Model)  

---

## 1. C4 Container Level Diagram (Mermaid)

```mermaid
graph TD
    user["Finance Operator / FinOps Manager"]
    bank["External Acquiring Banks & PSPs"]
    llm["Enterprise Vision-LLM API"]

    subgraph C4_System ["SmartReconcile System Boundary"]
        spa["Single-Page Application\n[React.js + Tailwind CSS]\nServes UI dashboards, template studio & review panels"]
        
        java_core["Backend Matching Core\n[Java 21 Virtual Threads & Spring Boot]\nExecutes >10k TPS deterministic matching & double-entry guardrails"]
        
        py_coproc["AI Coprocessor Service\n[Python 3.11 FastAPI & LangChain]\nParses bank statements & runs agentic discrepancy investigations"]
        
        redis["In-Memory Cache & Queue\n[Redis 7]\nStores fast matching indexes & discrepancy job queues"]
        
        postgres["Persistent Financial Database\n[PostgreSQL 16]\nStores transaction ledgers, audit logs, matches & bank templates"]
    end

    user -->|HTTPS / WSS| spa
    spa -->|REST JSON / WebSockets| java_core
    spa -->|REST JSON| py_coproc
    bank -->|SFTP / S3 / Upload| py_coproc
    py_coproc -->|gRPC StreamBankEvents| java_core
    py_coproc <-->|HTTPS TLS 1.3| llm
    java_core <-->|Redis Protocol| redis
    py_coproc <-->|Redis Protocol| redis
    java_core <-->|JDBC| postgres
    py_coproc <-->|AsyncPG| postgres
```

## 2. Container Descriptions & Technology Matrix

1. **React Single-Page Application (`web-ui`):** User interface container built with React.js, Tailwind CSS (Bancolombia palette `#0B192C` / `#FFD200`), Vite, and Axios/WebSockets.
2. **Backend Matching Core (`backend-core`):** Java 21 Spring Boot microservice using Virtual Threads (Project Loom) for high-speed deterministic matching and double-entry validation.
3. **AI Coprocessor Service (`ai-coprocessor`):** Python 3.11 FastAPI microservice using PyMuPDF and LangChain for bank statement table parsing and agentic discrepancy investigation.
4. **Redis Data Store:** Redis 7 container serving as the in-memory exact-match reference index and asynchronous job queue.
5. **PostgreSQL Relational DB:** PostgreSQL 16 relational database maintaining multi-tenant ledgers, audit logs, bank templates, and journal entry proposals.
