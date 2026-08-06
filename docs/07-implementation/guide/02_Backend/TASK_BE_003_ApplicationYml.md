# TASK BE-003 — `application.yml`

**Module:** `backend-core/src/main/resources/`  
**File Type:** Spring Boot Configuration File  
**Priority:** CRITICAL — Configures database connection pool, Redis, JWT keys, and Virtual Threads.  
**Depends On:** `TASK_BE_002`  
**Blocks:** Backend application startup  

---

## 1. Purpose

Configures the runtime environment for Spring Boot, establishing the HikariCP PostgreSQL database pool, Redis cache and queue connections, Virtual Thread concurrency (`spring.threads.virtual.enabled=true`), Flyway migration location, gRPC port configuration, and JWT secret key bindings.

---

## 2. Step-by-Step Implementation Instructions

### Step 1: Create the Configuration File
1. In `backend-core/src/main/resources/`, create `application.yml`.

### Step 2: Configure Server Port and Virtual Threads
1. Set HTTP server port: `server.port: 8080`.
2. Enable Spring Boot 3.2 Virtual Threads: `spring.threads.virtual.enabled: true`.

### Step 3: Configure Database Datasource & HikariCP
1. Bind PostgreSQL URL using environment variable fallback:
   - `spring.datasource.url: ${SPRING_DATASOURCE_URL:jdbc:postgresql://localhost:5432/smartreconcile_db}`
2. Bind username and password:
   - `spring.datasource.username: ${SPRING_DATASOURCE_USERNAME:smart_user}`
   - `spring.datasource.password: ${SPRING_DATASOURCE_PASSWORD:SuperSecretPass123!}`
3. Configure HikariCP connection pool limits:
   - `spring.datasource.hikari.maximum-pool-size: 20`
   - `spring.datasource.hikari.minimum-idle: 5`

### Step 4: Configure JPA & Flyway
1. Set Hibernate DDL auto validation: `spring.jpa.hibernate.ddl-auto: validate`.
2. Disable SQL logging in production: `spring.jpa.show-sql: false`.
3. Enable Flyway migrations: `spring.flyway.enabled: true` and `spring.flyway.locations: classpath:db/migration`.

### Step 5: Configure Redis & gRPC
1. Set Redis connection properties: `spring.data.redis.host: ${REDIS_HOST:localhost}` and `port: ${REDIS_PORT:6379}`.
2. Set gRPC server port: `grpc.server.port: 9090`.

### Step 6: Configure Application JWT Keys
1. Set JWT secret and expirations:
   - `app.jwt.secret: ${JWT_SECRET_KEY:c3VwZXItc2VjcmV0LTI1Ni1iaXQtYjY0LWtleS1mb3Itc21hcnRyZWNvbmNpbGU=}`
   - `app.jwt.access-token-expiration-ms: 900000` (15 minutes)
   - `app.jwt.refresh-token-expiration-ms: 604800000` (7 days)

---

## 3. Verification Checklist

| # | Check Condition | Risk if Failed |
|---|---|---|
| 1 | `spring.threads.virtual.enabled: true` set | Spring runs on traditional OS thread pool, reducing matching throughput |
| 2 | `ddl-auto: validate` set | Hibernate attempts to drop or alter database tables automatically |
| 3 | Environment variables specified with default fallbacks | Application crashes if local `.env` variable is missing |

---

## 4. Verification Command

Test Spring Boot configuration loading:
```bash
./mvnw spring-boot:run -Dspring-boot.run.arguments="--server.port=8081"
```
