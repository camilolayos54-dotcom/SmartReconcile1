# Phase 2 Risk Register Update (Deliverable 12)

**Project:** SmartReconcile  
**Document ID:** D12-RISK-REGISTER-UPDATE  
**Phase:** 2 — Project Kickoff  

---

## 1. Updated Risk Register Matrix

| Risk ID | Description | Impact | Likelihood | Mitigation Strategy | Status |
|---|---|---|---|---|---|
| **R-201** | Protobuf schema desynchronization between Java & Python modules. | High | Medium | Store `.proto` files in a shared `/proto` directory and enforce automated compilation checks in CI. | **ACTIVE** |
| **R-202** | Tailwind CSS class pollution causing UI maintenance friction. | Low | Medium | Enforce component modularization and ESLint Tailwind plugin rules. | **ACTIVE** |
| **R-203** | Local Docker environment resource exhaustion (Java JVM + Python LLM worker + Postgres). | Medium | Medium | Define explicit memory limits in `docker-compose.yml` (e.g., 2GB JVM limit, 1GB Python worker). | **ACTIVE** |
