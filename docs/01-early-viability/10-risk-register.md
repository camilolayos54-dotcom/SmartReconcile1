# Risk Register (Deliverable 10)

**Project:** SmartReconcile  
**Document ID:** D10-RISK-REGISTER  
**Phase:** 1 — Early Viability  

---

## 1. Phase 1 Consolidated Risk Matrix

| Risk ID | Risk Description | Category | Impact | Likelihood | Mitigation Strategy | Owner |
|---|---|---|---|---|---|---|
| **R-101** | Bank PDF statement format changes without notice. | Technical | Medium | High | Implement self-learning Vision-LLM parser fallback. | Lead Architect |
| **R-102** | LLM API cost spikes on massive settlement files (100k+ rows). | Economic | High | Medium | Pre-filter transactions in Java core; only send unmatched items to Python LLM. | Lead Architect |
| **R-103** | Customer finance teams resist trusting AI-suggested adjustments. | Operational | High | Medium | Provide interactive side-by-side audit UI showing step-by-step mathematical reasoning. | Product Lead |
| **R-104** | gRPC IPC bottlenecks under heavy concurrent batch ingestion. | Performance | Medium | Low | Optimize Protobuf payload serialization and pool gRPC channels. | Java Lead |
