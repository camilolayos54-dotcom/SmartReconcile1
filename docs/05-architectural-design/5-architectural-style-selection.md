# Deliverable 5: ADR — Architectural Style Selection (D5) [GLOBAL]

**Project:** SmartReconcile  
**Document ID:** D5-ADR-ARCHITECTURAL-STYLE  
**Phase:** 5 — Architectural Design (Tier 1 ADR)  
**Status:** Accepted  

---

## 1. Context

The system must support streaming batch file ingestion, real-time matching, asynchronous background AI investigations, and instant UI state updates.

## 2. Decision

We decide to adopt a **Hybrid Event-Driven & Microservices Architectural Style**:

1. **Event-Driven Pipeline (Redis Queue + Kafka):** Ingestion streams and discrepancy investigation requests pass as asynchronous events across queues, ensuring uncoupling.
2. **REST & WebSockets Interface:** React SPA consumes REST endpoints for synchronous actions (login, manual approvals, template edits) and WebSockets for real-time dashboard stream updates.
3. **gRPC Internal Pipeline:** High-speed binary RPC channel between Java and Python modules.

## 3. Consequences

### Positive
- **High Responsiveness:** Background AI agent processing does not block HTTP request threads.
- **Sub-Second UI Updates:** WebSockets push live match metrics to `MOD-UI` without requiring manual page refreshes.

### Negative / Trade-offs
- Eventual consistency management between Redis discrepancy queues and PostgreSQL persistent storage.
