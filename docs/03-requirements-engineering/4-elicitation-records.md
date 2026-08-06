# Requirements Elicitation Records (Deliverable 4)

**Project:** SmartReconcile  
**Document ID:** D4-ELICITATION-RECORDS  
**Phase:** 3 — Requirements Engineering (Layer 1)  

---

## 1. Elicitation Session Log

- **Session ID:** `ELIC-01`
- **Stakeholders Interviewed:** VP of Finance Ops, Lead Senior Accountant, Payment Engineering Manager.
- **Methodology:** Structured Domain Interviews & Accounting Workflow Walkthroughs.

## 2. Extracted Raw Requirement Statements

| Requirement ID | Stakeholder Statement | Derived Functional Requirement | Target Module |
|---|---|---|---|
| `RAW-01` | *"We need to drop PDF bank statements directly onto a web portal without having to format CSVs first."* | The system shall parse PDF bank statements via OCR/Vision-LLM and extract transaction tables automatically. | `MOD-ING` |
| `RAW-02` | *"The matching engine must process 100,000 transactions in under a minute without dropping any records."* | The Java matching core shall support high-concurrency batch processing (>10,000 TPS) with zero dropped events. | `MOD-DET` |
| `RAW-03` | *"When a fee discrepancy occurs, the system should tell us WHY (e.g., cross-border fee) instead of just showing red flags."* | The AI coprocessor shall analyze unmatched records, identify root-cause category, and output step-by-step reasoning. | `MOD-AGT` |
| `RAW-04` | *"I want a single UI screen built in React where I can see matched summaries, review AI explanations, and click one button to approve."* | The React UI shall provide an interactive dashboard displaying matched metrics, discrepancy details, and approval actions. | `MOD-UI` |
| `RAW-05` | *"Auditors will reject any AI suggestion if we cannot prove who approved it and why the math works."* | The system shall generate immutable audit logs for every AI proposal and human approval action. | `MOD-DET` / `MOD-UI` |
