# Non-Functional Requirements & System Constraints (Deliverable 2)

**Project:** SmartReconcile  
**Document ID:** D2-NFR-CONSTRAINTS  
**Phase:** 2 — Project Kickoff  

---

## 1. Performance & Throughput Targets

- **Java Matching Engine Throughput:** Minimum **10,000 Transactions Per Second (TPS)** per node.
- **Java Deterministic Matching Latency:** **<1.0 ms** per transaction pair in memory.
- **Python Agent Discrepancy Latency:** **<30 seconds** end-to-end for AI root-cause analysis and proposed adjustment generation.
- **React UI Response Time:** First Contentful Paint **<1.2s**; API response latency **<200ms**.

## 2. Security & Compliance Constraints

- **Data Encryption:** TLS 1.3 for all gRPC and REST communications; AES-256 for persistent database storage.
- **PII Protection:** Hashing or redaction of customer names, card PANs, and emails before sending payload data to Python LLM pipelines.
- **Audit Logging:** Immutable append-only log tables for all operator approvals and system state changes.

## 3. Availability & Reliability Targets

- **Uptime:** **99.95% Availability** for the Java core engine.
- **Fault Isolation:** Python AI service failures must gracefully degrade the system by queuing unmatched transactions without interrupting Java batch ingestion.
