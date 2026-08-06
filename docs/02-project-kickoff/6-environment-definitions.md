# Environment Definitions (Deliverable 6)

**Project:** SmartReconcile  
**Document ID:** D6-ENVIRONMENT-DEFINITIONS  
**Phase:** 2 — Project Kickoff  

---

## 1. Environment Architecture Matrix

| Environment | Purpose | Infrastructure | Data Isolation |
|---|---|---|---|
| **Development (`dev`)** | Local developer testing and rapid prototyping. | Local Docker Compose (Java + Python + React + Postgres + Redis). | Synthetic anonymized test data. |
| **Staging (`stage`)** | Pre-production validation, E2E testing, partner trials. | AWS EKS / GCP Kubernetes Cluster (Staging namespace). | Anonymized historical batch data. |
| **Production (`prod`)** | Live customer reconciliation & transaction processing. | AWS EKS Multi-AZ Kubernetes with Auto-Scaling. | Full production isolation (AES-256 encrypted). |

## 2. Infrastructure as Code (IaC)

- Containerization via **Docker** and **Docker Compose**.
- Cloud orchestration managed via **Terraform** and **Helm charts**.
