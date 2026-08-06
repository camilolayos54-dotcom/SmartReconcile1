### Phase 5 Brief: Architectural Design & System Topology

**Project:** SmartReconcile (Hybrid Deterministic & Agentic Transactional Reconciliation Engine)  
**Phase:** 5 — Architectural Design  
**Status:** Complete — Ready for Sprint Implementation  

---

### Executive Summary

Phase 5 formalizes the high-level system architecture, bounded contexts, component topology, deployment strategy, and ADR (Architectural Decision Records) for **SmartReconcile**.

### Key Architectural Decisions

1. **Microservice Topology:**
   - `backend-core` (Java 21 Virtual Threads, Spring Boot 3): High-speed deterministic matching (>10,000 TPS).
   - `ai-coprocessor` (Python 3.11, FastAPI, LangChain/LlamaIndex): Asynchronous Vision-LLM bank statement parsing and multi-tool agentic discrepancy resolution.
   - `web-ui` (React.js + Tailwind CSS): Single-Page Application with Bancolombia corporate design tokens (`#0B192C` Navy, `#FFD200` Yellow, `#E11D48` Crimson).
2. **Inter-Service Communication:**
   - gRPC over HTTP/2 with Protobuf for Java <-> Python IPC (<2.5ms latency).
   - REST + WebSockets over TLS 1.3 for React UI <-> Backend communication.
3. **Data Layer Architecture:**
   - PostgreSQL 16: Primary relational store for ACID transactional ledgers, audit logs, and bank statement line items.
   - Redis 7: In-memory cache for fast exact-matching indexes and asynchronous discrepancy job queues (`queue:discrepancies:ai`).
4. **Deployment Strategy:**
   - Docker & Docker Compose for local development; Kubernetes (AWS EKS) with Helm charts for production multi-AZ scaling.
