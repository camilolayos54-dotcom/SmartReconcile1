# System Context Diagram (Deliverable 1)

**Project:** SmartReconcile  
**Document ID:** D1-SYSTEM-CONTEXT  
**Phase:** 3 — Requirements Engineering (Layer 1)  

---

## 1. System Boundary Definition

**SmartReconcile** sits between internal transaction databases/event streams and external financial settlement data sources (acquirer bank statements, gateway payouts, FX feeds).

## 2. Mermaid System Context Diagram

```mermaid
graph TD
    subgraph External Systems
        BANK["Acquiring Banks & PSPs (PDF, CSV, MT940, BAI2)"]
        LEDGER_DB["Internal Transaction Database (PostgreSQL / Kafka)"]
        LLM_API["Enterprise Vision-LLM API (Claude / OpenAI / Local VLM)"]
        ERP["External ERP / Accounting System (NetSuite / SAP / CSV Export)"]
    end

    subgraph SmartReconcile System Boundary
        INGEST["MOD-ING: Statement Ingestion & Vision Parser (Python)"]
        CORE["MOD-DET: High-Speed Deterministic Engine (Java 21)"]
        AGENT["MOD-AGT: Agentic AI Discrepancy Resolver (Python)"]
        UI["MOD-UI: Audit & Approval Dashboard (React + Tailwind)"]
    end

    subgraph Human Actors
        FIN_ANALYST["Finance Analyst (Operator)"]
        FIN_MGR["FinOps Manager (Approver)"]
        SYS_ADMIN["System Administrator"]
    end

    %% Data Flow Connections
    BANK -->|Upload / SFTP / Email| INGEST
    INGEST -->|Parsed JSON Events via gRPC| CORE
    LEDGER_DB -->|Internal Transactions via REST/Kafka| CORE
    CORE -->|Unmatched Discrepancies via gRPC| AGENT
    AGENT <-->|Prompts / Multimodal Analysis| LLM_API
    AGENT -->|Proposed Adjustments & Explanations| CORE
    CORE <-->|REST API / WebSockets| UI
    UI <-->|Interactive Review & Approval| FIN_ANALYST
    UI <-->|Batch Sign-Off & Audit Review| FIN_MGR
    SYS_ADMIN -->|Configuration & System Monitoring| UI
    UI -->|Export Balanced Journal Entries| ERP
```

## 3. External Interface Catalog

1. **Banking & PSP Interface:** Ingests MT940, BAI2, CSV, and PDF statements via SFTP, S3 bucket sync, or Web UI upload.
2. **Internal Transaction Feed:** Ingests internal payment attempts and authorized charges via PostgreSQL connection or Kafka events.
3. **Vision-LLM API Interface:** Sends anonymized PDF table slices and transaction metadata to enterprise Vision-LLMs over HTTPS TLS 1.3.
4. **ERP / Accounting Export:** Exports validated double-entry balancing journal entries as CSV / JSON for NetSuite, SAP, or QuickBooks integration.
