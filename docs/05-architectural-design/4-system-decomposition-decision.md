# Deliverable 4: ADR — System Decomposition Decision (D4) [GLOBAL]

**Project:** SmartReconcile  
**Document ID:** D4-ADR-SYSTEM-DECOMPOSITION  
**Phase:** 5 — Architectural Design (Tier 1 ADR)  
**Status:** Accepted  

---

## 1. Context

SmartReconcile integrates two distinct technical paradigms: high-concurrency deterministic mathematical processing (Java) and flexible artificial intelligence parsing/agentic reasoning (Python). Building this as a single monolithic application would force compromising either Java's multi-threading performance or Python's native AI ecosystem.

## 2. Decision

We decide to adopt a **Polyglot Modular Microservice Decomposition (Dual-Core Architecture)**:

1. **`backend-core` (Java 21):** Handles deterministic matching, accounting guardrails, double-entry validation, and audit persistence.
2. **`ai-coprocessor` (Python 3.11):** Handles bank statement ingestion (PyMuPDF / Vision-LLM), template caching (`MOD-ING-TPL`), and agentic discrepancy investigation.
3. **`web-ui` (React + Tailwind):** Standalone Single-Page Application (SPA) serving as the operator audit interface.

## 3. Consequences

### Positive
- **Best Tool for the Job:** Enables native Java Virtual Threads for >10,000 TPS matching while leveraging Python's rich LLM/Vision libraries for parsing.
- **Polyglot Isolation:** Upgrading Python AI libraries or switching LLM providers requires zero recompilation or downtime for the Java core engine.

### Negative / Trade-offs
- Requires managing inter-process communication (gRPC Protobuf schemas) between services.
