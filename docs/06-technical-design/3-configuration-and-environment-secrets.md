# Deliverable 3: Configuration & Environment Secrets (D3) [GLOBAL]

**Project:** SmartReconcile  
**Document ID:** D3-ENVIRONMENT-SECRETS  
**Phase:** 6 — Technical Design (Tier 0)  

---

## 1. Environment Variable Template (`.env.example`)

```ini
# ==============================================================================
# SMARTRECONCILE GLOBAL ENVIRONMENT CONFIGURATION
# ==============================================================================

# Global Environment
ENV=development # development | staging | production
PORT_JAVA=8080
PORT_PYTHON=8001
PORT_REACT=3000

# PostgreSQL Configuration
SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/smartreconcile_db
SPRING_DATASOURCE_USERNAME=smart_user
SPRING_DATASOURCE_PASSWORD=SuperSecretPass123!
DATABASE_POOL_MAX_SIZE=20

# Redis Cache & Queue Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=RedisSecretPass123!

# gRPC Configuration
GRPC_SERVER_PORT=9090
GRPC_PYTHON_HOST=localhost
GRPC_PYTHON_PORT=9091

# JWT Security Configuration
JWT_SECRET_KEY=c3VwZXItc2VjcmV0LTI1Ni1iaXQtYjY0LWtleS1mb3Itc21hcnRyZWNvbmNpbGU=
JWT_ACCESS_TOKEN_EXPIRATION_MS=900000 # 15 minutes
JWT_REFRESH_TOKEN_EXPIRATION_MS=604800000 # 7 days
CSRF_SECRET_KEY=csrf_protection_secret_key_9988

# AI / Vision-LLM API Credentials
VISION_LLM_PROVIDER=openai # openai | claude | local_vlm
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
CLAUDE_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
VISION_LLM_MAX_TOKENS=4096
VISION_LLM_TEMPERATURE=0.0

# External FX & Fee Reference APIs
OPEN_EXCHANGE_RATES_APP_ID=oxr_app_id_sample_123456
```
