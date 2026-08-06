# Critical Assumptions List (Deliverable 11)

**Project:** SmartReconcile  
**Document ID:** D11-CRITICAL-ASSUMPTIONS  
**Phase:** 1 — Early Viability  

---

## 1. Key Operational & Technical Assumptions

1. **Assumption A1 (Deterministic Dominance):** At least **95% of transactions** can be matched deterministically by the Java engine based on amount, date window, and reference tokens, leaving ≤5% for AI agent processing.
2. **Assumption A2 (Vision-LLM Precision):** Commercial or open Vision-LLMs can achieve **>98% line-item table extraction accuracy** on scanned PDF bank statements when prompted with structured JSON schemas.
3. **Assumption A3 (Audit Tolerance):** External auditors will accept AI-assisted accounting adjustment recommendations provided every proposal includes a deterministic, human-readable justification trail.
4. **Assumption A4 (Integration Willingness):** Target clients are willing to export transaction ledgers via REST API, CSV upload, or Kafka events.
