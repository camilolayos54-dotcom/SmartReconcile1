# MVP Definition Document (Deliverable 12)

**Project:** SmartReconcile  
**Document ID:** D12-MVP-DEFINITION  
**Phase:** 1 — Early Viability  

---

## 1. Core Technology Stack

- **Backend Matching Core:** Java 21 (Virtual Threads, Spring Boot / High-throughput gRPC service).
- **AI & Agentic Coprocessor:** Python 3.11+ (FastAPI, LangChain/LlamaIndex, PyMuPDF, Vision-LLMs, gRPC).
- **Web UI Frontend:** React.js (JavaScript/TypeScript) + Tailwind CSS + HTML5/CSS3.

## 2. Core MVP Feature Scope

The Minimum Viable Product (MVP) of **SmartReconcile** focuses on proving the end-to-end hybrid workflow:

### Feature Module 1: Heterogeneous Ingestion Engine (Python)
- Web UI & REST/gRPC API endpoint for uploading bank settlement files (CSV, PDF, MT940).
- Vision-LLM parser converting PDF/CSV lines into standardized JSON transaction event streams.

### Feature Module 2: High-Speed Deterministic Matching Core (Java 21)
- In-memory event matching engine using exact key matching (Reference ID + Amount) and windowed fuzzy matching (Date ±3 days, Amount ±0.05).
- Output categories: **Matched**, **Unmatched Internal**, **Unmatched Bank**, **Discrepancy (Amount Delta)**.

### Feature Module 3: Agentic AI Root-Cause Coprocessor (Python)
- Discrepancy resolution agent equipped with FX rate lookup and bank fee schedule verifier.
- Generates root-cause diagnostic (e.g., *"Unannounced 3.5% cross-border interchange fee applied by acquiring bank"*).
- Produces proposed balancing journal entry with step-by-step reasoning.

### Feature Module 4: Operator Audit & Approval Dashboard (React + Tailwind CSS)
- Interactive Single-Page Application (SPA) built with React and styled using Tailwind CSS.
- Displays real-time matched summary metrics, interactive discrepancy flags, AI reasoning logs, and a one-click "Approve & Export Journal Entry" trigger.

## 3. Out of MVP Scope
- Live automated wire transfer execution.
- Real-time point-of-sale card authorization.
- Multi-tenant enterprise SSO (deferred to Phase 3/4).
