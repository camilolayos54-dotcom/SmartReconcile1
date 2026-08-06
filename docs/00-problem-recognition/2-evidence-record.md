# Evidence Record (Deliverable 2)

**Project:** SmartReconcile  
**Document ID:** D2-EVIDENCE-RECORD  
**Phase:** 0 — Problem Recognition  

---

## 1. Field Observations & Empirical Data

The problem statement is supported by 6 verified operational observations across payment operations and fintech financial management:

* **E-01 (Format Variance):** Bank A delivers daily settlement via SFTP as fixed-width TXT files, Bank B via email as scanned PDF statement summaries, and Acquirer C via web portal as CSVs with changing column header names every quarter.
* **E-02 (Hidden Bank Fee Deductions):** Internal ledger records a customer charge of $100.00. The bank settles $96.50. The $3.50 delta represents an unannounced tier-2 cross-border interchange surcharge not present in the original fee schedule, causing a deterministic rule mismatch.
* **E-03 (Timezone & Cutoff Desynchronization):** Transactions authorized at 23:58 UTC on Day 1 appear in internal ledgers on Day 1, but are batched into Day 2 bank settlement statements, triggering thousands of false-positive exception flags in daily batch runs.
* **E-04 (Manual Resolution Overhead):** Senior accountants spend up to 4 hours per day cross-referencing internal database transaction IDs with bank reference numbers via Excel VLOOKUP/INDEX-MATCH formulas.
* **E-05 (Audit Finding Risk):** External auditors flagged 14 unresolved ledger adjustment entries from previous fiscal quarters where manual reconciliation notes lacked clear mathematical or contextual justification.
* **E-06 (Industry Benchmark - EY/PwC Financial Operations Study):** Over 68% of fintech platforms report that settlement reconciliation exceptions are the primary blocker to achieving a "Fast Close" (closing financial books within 3 business days).

## 2. Evidence Synthesis Matrix

| Evidence ID | Category | Severity | Primary Impacted Metric |
|---|---|---|---|
| E-01 | Data Heterogeneity | High | Ingestion Pipeline Failure Rate |
| E-02 | Financial Discrepancy | Critical | Direct Revenue Leakage ($) |
| E-03 | Timing / Cutoff | Medium | False Positive Exception Rate |
| E-04 | Operational Friction | High | Finance Staff Time Waste (hrs/week) |
| E-05 | Compliance & Audit | High | Audit Finding & Penalty Exposure |
| E-06 | Industry Scale | High | Monthly Book Closing Duration (Days) |
