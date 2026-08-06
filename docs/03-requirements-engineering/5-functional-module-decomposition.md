# Functional Module Decomposition (Deliverable 5)

**Project:** SmartReconcile  
**Document ID:** D5-FUNCTIONAL-MODULE-DECOMPOSITION  
**Phase:** 3 — Requirements Engineering (Layer 1)  

---

## 1. Module Architecture Overview

SmartReconcile is decomposed into **4 primary functional modules**:

```
+-----------------------------------------------------------------------------------+
|                                  SMARTRECONCILE                                   |
+-------------------+-------------------+-------------------+-----------------------+
| MOD-ING           | MOD-DET           | MOD-AGT           | MOD-UI                |
| Ingestion &       | Deterministic     | Agentic AI        | Audit & Approval      |
| Vision Parsing    | Matching Engine   | Discrepancy       | Dashboard             |
| Module (Python)   | Core (Java 21)    | Resolver (Python) | (React + Tailwind CSS)|
+-------------------+-------------------+-------------------+-----------------------+
```

## 2. Module Specifications Summary

### Module 1: `MOD-ING` — Statement Ingestion, Vision Parsing & Template Manager Engine
* **Primary Tech:** Python 3.11, FastAPI, PyMuPDF, Vision-LLM API.
* **Sub-component `MOD-ING-TPL` (Bank Template & Schema Manager):** Manages reusable bank statement parsing templates (column mappings, character/decimal formats, date layouts). Directs structured files through zero-cost deterministic parsers, reserving Vision-LLM parsing for unstructured or new bank formats. Auto-generates reusable templates from successful LLM extractions.
* **Responsibilities:** Receives bank statements (PDF, CSV, MT940), applies cached templates or Vision-LLM extractions, validates table structures, and emits standardized JSON payloads via gRPC to `MOD-DET`.

### Module 2: `MOD-DET` — High-Speed Deterministic Matching Core
* **Primary Tech:** Java 21 (Virtual Threads), Spring Boot, PostgreSQL, Redis.
* **Responsibilities:** Ingests internal ledgers and bank JSON events, performs high-speed key matching (>10,000 TPS), categorizes records into Matched/Unmatched/Discrepancy, and enforces accounting integrity guardrails.

### Module 3: `MOD-AGT` — Agentic AI Discrepancy Resolution Engine
* **Primary Tech:** Python 3.11, LangChain/LlamaIndex, FX API, Fee Tools.
* **Responsibilities:** Receives unmatched discrepancy records, runs multi-tool investigation (FX rate, fee schedules, timezone shift), determines root cause, and generates balancing journal entries with step-by-step reasoning logs.

### Module 4: `MOD-UI` — Operator Audit & Approval Dashboard
* **Primary Tech:** React.js, Tailwind CSS, Vite, REST/WebSocket API.
* **Responsibilities:** Provides interactive Single-Page Application (SPA) for finance operators to view real-time reconciliation metrics, inspect AI discrepancy reasoning, manage bank statement templates (`MOD-ING-TPL`), approve adjustment entries, and export journal reports.

## 3. Intra-Module Dependency Matrix

| Module | Depends On | Interface Mechanism |
|---|---|---|
| `MOD-ING` | External Bank Files, Template DB | HTTP Upload / SFTP Sync / PostgreSQL |
| `MOD-DET` | `MOD-ING`, Internal DB | gRPC Protocol Buffers / JDBC |
| `MOD-AGT` | `MOD-DET` | gRPC Protocol Buffers / Redis Queue |
| `MOD-UI` | `MOD-DET`, `MOD-AGT`, `MOD-ING-TPL` | REST API / WebSockets |
