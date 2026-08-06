# Risk Register & Scope Boundary Gates (Deliverable 8)

**Project:** SmartReconcile  
**Document ID:** D8-RISK-REGISTER  
**Phase:** 0 — Problem Recognition  

---

## 1. Initial Risk Register

| Risk ID | Description | Impact | Likelihood | Mitigation Strategy |
|---|---|---|---|---|
| **R-01** | LLM hallucination during discrepancy root-cause analysis. | Critical | Medium | Enforce strict deterministic math validation in Java prior to executing any AI-proposed adjustment. |
| **R-02** | High latency in Python Agentic pipeline blocking real-time workflows. | High | Medium | Decouple Agentic resolution from Java matching core using asynchronous Kafka queue. |
| **R-03** | Malformed or low-quality scanned PDF bank statements failing OCR/Vision parsing. | Medium | High | Implement fallback Vision-LLM models with confidence score thresholds and manual escalation triggers. |
| **R-04** | Data privacy breach sending financial statement data to external LLM APIs. | High | Low | Use enterprise private LLM deployments or self-hosted open-weights models (e.g., Llama/Qwen) with PII redaction. |

## 2. Mandatory Scope Boundary Gates (Hard Constraints)

- **Gate Constraint 1 (No Unverified Adjustments):** The system must **NEVER** automatically write an adjustment entry directly into the production ledger without passing deterministic mathematical validation and human-in-the-loop approval thresholds.
- **Gate Constraint 2 (Strict System Decoupling):** The Java deterministic engine must operate independently of the Python AI service so that AI downtime never halts core batch matching.
- **Gate Constraint 3 (Execution Scope Limit):** The system is limited to statement ingestion, matching, and adjustment proposal; direct bank account wire transfers are strictly out of scope.
