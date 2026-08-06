# Technical Stack Decision Record (Deliverable 3)

**Project:** SmartReconcile  
**Document ID:** D3-STACK-DECISION  
**Phase:** 2 — Project Kickoff  

---

## 1. Locked Technical Architecture

| System Layer | Selected Technology | Alternative Evaluated | Decision Rationale |
|---|---|---|---|
| **Core Matching Engine** | **Java 21 (Virtual Threads, Spring Boot 3)** | Node.js / Go | Superior concurrency model, memory safety, enterprise financial ecosystem. |
| **AI & Ingestion Service** | **Python 3.11+ (FastAPI, PyMuPDF, LangChain)** | LangChain4j (Java) | Python possesses superior PDF parsing libraries and native AI/LLM ecosystem. |
| **Frontend Web UI** | **React.js + Tailwind CSS (Vite, TS/JS)** | Thymeleaf / Angular | Modern SPA user experience, fast component rendering, utility-first styling. |
| **Inter-Service Communication** | **gRPC over HTTP/2 + Protobuf** | REST JSON APIs | Sub-millisecond serialization speed and strict interface schema contracts. |
| **Database & Caching** | **PostgreSQL 16 + Redis 7** | MongoDB | PostgreSQL provides ACID compliance for financial data; Redis enables fast lookup. |
