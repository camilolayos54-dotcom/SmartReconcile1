# Deliverable 1: Quality Attributes Map (D1) [GLOBAL]

**Project:** SmartReconcile  
**Document ID:** D1-QUALITY-ATTRIBUTES-MAP  
**Phase:** 5 — Architectural Design (Tier 0)  

---

## 1. Quality Attribute Scenarios (NFR Formalization)

### Scenario 1: High-Throughput Deterministic Matching (Performance & Scalability)
- **Source:** Bank settlement batch stream from `MOD-ING`.
- **Stimulus:** Ingestion of 100,000 transaction events.
- **Artifact:** Java 21 `MOD-DET` Matching Engine.
- **Environment:** Peak production batch run.
- **Response:** Spawns Virtual Threads per event, queries Redis in-memory index, and writes matched pairs.
- **Response Measure:** Matching completed in **<10 seconds** (>10,000 TPS) with **<1.0ms** latency per pair and **0.00% false-positive rate**.

### Scenario 2: Agentic Discrepancy Investigation (Availability & Resiliency)
- **Source:** Redis Discrepancy Queue `queue:discrepancies:ai`.
- **Stimulus:** 1,000 non-matching transaction items enqueued.
- **Artifact:** Python `MOD-AGT` Coprocessor.
- **Environment:** High LLM API latency or external provider outage.
- **Response:** Asynchronous queue consumption; tool execution (FX, Fee tables); falls back to manual escalation if confidence <85%.
- **Response Measure:** High LLM latency or Python worker crashes do not block or slow Java `MOD-DET` batch matching execution.

### Scenario 3: Financial Audit & Double-Entry Integrity (Security & Compliance)
- **Source:** AI Agent proposal or Human Operator approval.
- **Stimulus:** Submission of a balancing journal entry proposal.
- **Artifact:** Java 21 `MOD-DET` Accounting Guardrail.
- **Environment:** Normal operation or malicious/hallucinated proposal input.
- **Response:** Validates $\sum \text{Debits} = \sum \text{Credits}$; throws `InvalidAccountingEntryException` on imbalance; records immutable SHA-256 hash in audit log.
- **Response Measure:** 100% of persisted ledger entries maintain double-entry balance; SOC-2 Type II audit compliant.
