# CI/CD & Docker Deployment Master Guide

**Project:** SmartReconcile  
**Containers:** PostgreSQL 16, Redis 7, Java 21 Spring Boot, Python 3.11 FastAPI, Vite React  

---

## 1. Local Container Environment (`docker-compose.yml`)

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:16-alpine
    container_name: smartreconcile-postgres
    environment:
      POSTGRES_DB: smartreconcile_db
      POSTGRES_USER: smart_user
      POSTGRES_PASSWORD: SuperSecretPass123!
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    container_name: smartreconcile-redis
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

---

## 2. CI/CD Task Index

1. [`TASK_OPS_001_DockerComposeSetup.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/04_CICD_Docker/TASK_OPS_001_DockerComposeSetup.md) — Create local `docker-compose.yml` for PostgreSQL and Redis.
2. [`TASK_OPS_002_GitHubActionsPipeline.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/04_CICD_Docker/TASK_OPS_002_GitHubActionsPipeline.md) — Create `.github/workflows/ci.yml` for automated Maven and Pytest building.
