# Deliverable 8: CI/CD & Environments Strategy (D8) [GLOBAL]

**Project:** SmartReconcile  
**Document ID:** D8-CICD-ENVIRONMENTS  
**Phase:** 5 — Architectural Design (Tier 2)  

---

## 1. Environment Architecture Matrix

| Environment | Host Infrastructure | Database & Cache | CI/CD Branch Trigger |
|---|---|---|---|
| **Development (`dev`)** | Local Docker Compose | Local Postgres 16 & Redis 7 | Local feature branches (`feature/*`) |
| **Staging (`stage`)** | AWS EKS Staging Namespace | AWS RDS Postgres & ElastiCache (Staging) | PR merge to `main` |
| **Production (`prod`)** | AWS EKS Multi-AZ Cluster | AWS Aurora Postgres & ElastiCache (Prod) | Tagged release (`release/v*`) |

## 2. GitHub Actions CI/CD Pipeline Workflow

```mermaid
flowchart TD
    Push[Push / Pull Request] --> TriggerCI[GitHub Actions CI Pipeline]
    
    subgraph Parallel Validation Checks
        JavaBuild[Java 21 Maven Build & JUnit Tests]
        PythonBuild[Python Pytest & Flake8 Linting]
        ReactBuild[Vite React Build & Vitest Component Tests]
        SecurityScan[Trivy & Dependency Vulnerability Scan]
    end

    TriggerCI --> JavaBuild
    TriggerCI --> PythonBuild
    TriggerCI --> ReactBuild
    TriggerCI --> SecurityScan

    JavaBuild --> MergeCheck{All Checks Passed?}
    PythonBuild --> MergeCheck
    ReactBuild --> MergeCheck
    SecurityScan --> MergeCheck

    MergeCheck -- Yes --> BuildDocker[Build & Push Docker Images to ECR]
    MergeCheck -- No --> BlockPR[Block Merge & Alert Slack]
    BuildDocker --> DeployK8s[Apply Helm Charts to EKS Cluster]
```
