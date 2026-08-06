# Deliverable 10: ADR Consolidation & Master Index (D10) [GLOBAL]

**Project:** SmartReconcile  
**Document ID:** D10-ADR-CONSOLIDATION  
**Phase:** 5 — Architectural Design (Tier 3)  

---

## 1. Master Architecture Decision Records (ADRs) Index

| ADR ID | Decision Title | Status | Summary of Decision | Primary Impact |
|---|---|---|---|---|
| [`D3-ADR`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/05-architectural-design/3-deployment-topology-decision.md) | Deployment Topology | **ACCEPTED** | Containerized Cloud-Native (AWS EKS Kubernetes) with Docker Compose local parity. | High availability & independent pod scaling |
| [`D4-ADR`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/05-architectural-design/4-system-decomposition-decision.md) | System Decomposition | **ACCEPTED** | Polyglot Dual-Core Microservices (`backend-core` Java + `ai-coprocessor` Python + `web-ui` React). | Java >10k TPS speed + Python native AI ecosystem |
| [`D5-ADR`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/05-architectural-design/5-architectural-style-selection.md) | Architectural Style | **ACCEPTED** | Hybrid Event-Driven (Redis Queue/Kafka) + REST / WebSockets APIs. | Uncoupled background AI tasks & live UI updates |
| [`D6-ADR`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/05-architectural-design/6-communication-pattern-decision.md) | Communication Pattern | **ACCEPTED** | gRPC over HTTP/2 with Shared Protobuf (`proto/reconciliation.proto`) for inter-service IPC. | Sub-millisecond binary IPC serialization |
