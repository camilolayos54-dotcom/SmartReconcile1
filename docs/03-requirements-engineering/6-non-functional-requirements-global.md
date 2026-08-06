# Global Non-Functional Requirements (Deliverable 6)

**Project:** SmartReconcile  
**Document ID:** D6-NFR-GLOBAL  
**Phase:** 3 — Requirements Engineering (Layer 1)  

---

## 1. Security & Compliance NFRs

- **NFR-SEC-01 (Encryption in Transit):** 100% of inter-module communications (gRPC, REST, WebSockets) must enforce TLS 1.3 encryption.
- **NFR-SEC-02 (Encryption at Rest):** All persistent database volumes (PostgreSQL, Redis backups) must be encrypted using AES-256 keys.
- **NFR-SEC-03 (PII Redaction):** Customer PII (Names, PANs, Emails) must be masked or redacted before sending payload data to `MOD-AGT` or external LLMs.
- **NFR-SEC-04 (SOC-2 Compliance):** System must generate immutable, append-only audit trail logs for all human approvals and AI-proposed journal entries.

## 2. Performance & Reliability NFRs

- **NFR-PERF-01 (Matching Engine Latency):** `MOD-DET` must complete deterministic matching in **<1.0 ms** per transaction pair in memory.
- **NFR-PERF-02 (Matching Throughput):** `MOD-DET` must sustain **>10,000 TPS** under peak load testing.
- **NFR-PERF-03 (AI Resolution Latency):** `MOD-AGT` must return root-cause analysis and adjustment proposals in **<30 seconds** per discrepancy item.
- **NFR-REL-01 (Availability):** `MOD-DET` must maintain **99.95% system uptime**.
- **NFR-REL-02 (Fault Tolerance):** Temporary downtime in `MOD-AGT` must not block or crash `MOD-DET` batch matching execution.

## 3. Usability & UI NFRs

- **NFR-USA-01 (React FCP):** `MOD-UI` First Contentful Paint must load in **<1.2 seconds**.
- **NFR-USA-02 (Responsive Design):** `MOD-UI` must render responsively on desktop displays (1920x1080 to 1280x720) using Tailwind CSS.
