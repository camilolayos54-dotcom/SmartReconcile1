# Data Accessibility Record (Deliverable 6)

**Project:** SmartReconcile  
**Document ID:** D6-DATA-ACCESSIBILITY  
**Phase:** 1 — Early Viability  

---

## 1. Required Data Sources & Formats

| Data Source | Format | Protocol / Access Method | Feasibility Status |
|---|---|---|---|
| **Internal Transaction Ledgers** | JSON / SQL Database / Kafka Events | JDBC / Kafka Consumer / REST API | **AVAILABLE** |
| **Standard Bank Statements** | MT940, BAI2, ISO 20022 XML | SFTP / S3 / Direct API | **AVAILABLE** |
| **Unstructured Bank Statements** | PDF, Scanned Images, CSV | Email Attachment / File Upload | **ACCESSIBLE via Vision-LLM** |
| **FX & Rate Reference Feeds** | JSON API | Open Exchange Rates / ECB API | **AVAILABLE** |

## 2. Data Privacy & Anonymization Protocols

- PII (Personally Identifiable Information) such as customer names or card numbers will be hashed or redacted prior to passing payloads to the LLM agentic service.
- Financial transaction IDs, amounts, timestamps, and currency codes are retained for deterministic matching.
