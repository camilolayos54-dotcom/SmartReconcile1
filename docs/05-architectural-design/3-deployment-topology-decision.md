# Deliverable 3: ADR — Deployment Topology Decision (D3) [GLOBAL]

**Project:** SmartReconcile  
**Document ID:** D3-ADR-DEPLOYMENT-TOPOLOGY  
**Phase:** 5 — Architectural Design (Tier 1 ADR)  
**Status:** Accepted  

---

## 1. Context

SmartReconcile requires high computational performance for its Java 21 deterministic matching engine (>10,000 TPS), flexible Python worker environments for Vision-LLM parsing and agentic investigations, and high-availability database infrastructure for multi-tenant financial data.

## 2. Decision

We decide to adopt a **Containerized Cloud-Native Kubernetes Topology (AWS EKS / Multi-AZ K8s) with Local Docker Compose Parity**:

1. **Local Development (`dev`):** Docker Compose orchestrating `backend-core` (Java 21 JVM), `ai-coprocessor` (Python 3.11 FastAPI), `web-ui` (Vite React), PostgreSQL 16, and Redis 7.
2. **Production (`prod`):** AWS EKS Kubernetes cluster with independent pod auto-scaling:
   - `smartreconcile-core-pod`: Java 21 Spring Boot container with 2CPU / 4GB RAM limits.
   - `smartreconcile-ai-pod`: Python 3.11 FastAPI container with 2CPU / 2GB RAM limits (horizontal pod auto-scaler based on Redis queue depth).
   - `smartreconcile-ui-pod`: Nginx static container serving React SPA build.
   - Managed Cloud Services: AWS Aurora PostgreSQL (Multi-AZ) and AWS ElastiCache for Redis.

## 3. Consequences

### Positive
- **Independent Scaling:** High-volume batch ingestion scales `smartreconcile-core-pod` without over-provisioning Python AI pods.
- **Environment Parity:** Docker Compose guarantees zero "works on my machine" friction between local dev and cloud staging/prod.
- **Fault Isolation:** High LLM API memory consumption in Python pods will never crash the core Java matching JVM.

### Negative / Trade-offs
- Increased DevOps complexity managing Kubernetes Helm charts and infrastructure-as-code (Terraform).
