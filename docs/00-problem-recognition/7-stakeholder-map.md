# Stakeholder Map (Deliverable 7)

**Project:** SmartReconcile  
**Document ID:** D7-STAKEHOLDER-MAP  
**Phase:** 0 — Problem Recognition  

---

## 1. Stakeholder Classification Matrix

| Stakeholder Role | Influence | Interest | Key Responsibilities & Needs |
|---|---|---|---|
| **Project Sponsor (CFO / VP FinOps)** | High | High | Approves resource allocation; requires financial leakage reduction and fast monthly close. |
| **Lead Systems Architect (Java/AI)** | High | High | Defines technical architecture; ensures sub-second latencies and gRPC IPC integrity. |
| **Finance Operations Managers** | Medium | High | End-users of the discrepancy resolution dashboard; require clear explanations for AI suggestions. |
| **Compliance & External Auditors** | High | Medium | Require strict audit logs, zero hallucination in adjustment entries, and SOC compliance. |
| **Acquiring Banks & PSP Partners** | Low | Low | External data providers delivering settlement files via SFTP/S3/Webhooks. |

## 2. Governance & Decision Authority

- **Final Gate Authorization:** Project Sponsor & Lead Systems Architect.
- **Domain Validation Authority:** Finance Operations Manager & Lead Auditor.
