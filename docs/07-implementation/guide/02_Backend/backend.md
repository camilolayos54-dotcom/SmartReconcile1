# Backend Master Guide & Technology Architecture

**Project:** SmartReconcile  
**Primary Stack:** Java 21 (Spring Boot 3.2+) & Python 3.11+ (FastAPI)  
**IPC Protocol:** gRPC over HTTP/2 (`reconciliation.proto`)  

Este archivo es la referencia maestra de la capa backend. Contiene la estructura de paquetes, configuraciones iniciales y pre-consideraciones técnicas que NO están en las Global Rules y que aplican exclusivamente a la implementación del backend Java y del coprocesador Python.

---

## 1. Java Backend Package Architecture (`backend-core/`)

```
backend-core/
├── pom.xml
├── Dockerfile
└── src/
    ├── main/
    │   ├── java/com/smartreconcile/
    │   │   ├── SmartReconcileApplication.java              <- Entry point
    │   │   ├── config/
    │   │   │   ├── VirtualThreadConfig.java                <- Project Loom executor
    │   │   │   ├── SecurityConfig.java                     <- Spring Security filter chain
    │   │   │   ├── CorsConfig.java                         <- CORS whitelist
    │   │   │   ├── RedisConfig.java                        <- Redis connection factory
    │   │   │   └── JpaAuditingConfig.java                  <- @CreatedDate, @LastModifiedDate
    │   │   ├── security/
    │   │   │   ├── JwtService.java                         <- Genera y valida JWT tokens
    │   │   │   ├── JwtAuthenticationFilter.java            <- Intercepta requests, valida cookie HttpOnly
    │   │   │   └── CsrfProtectionFilter.java               <- Verifica X-CSRF-TOKEN header
    │   │   ├── engine/
    │   │   │   ├── DeterministicMatcher.java                <- Motor de matching >10k TPS
    │   │   │   └── MemoryIndexManager.java                 <- Administrador de índice Redis in-memory
    │   │   ├── ledger/
    │   │   │   ├── AccountingGuardrail.java                 <- Validación Sum(D) == Sum(C)
    │   │   │   ├── model/
    │   │   │   │   ├── Tenant.java
    │   │   │   │   ├── BankAccount.java
    │   │   │   │   ├── BankStatementBatch.java
    │   │   │   │   ├── BankStatementLine.java
    │   │   │   │   ├── TransactionLedger.java
    │   │   │   │   ├── ReconciliationMatch.java
    │   │   │   │   ├── DiscrepancyItem.java
    │   │   │   │   ├── JournalEntryProposal.java
    │   │   │   │   ├── JournalEntryLine.java
    │   │   │   │   ├── BankTemplate.java
    │   │   │   │   ├── AuditLog.java
    │   │   │   │   ├── MatchType.java                      <- Enum
    │   │   │   │   ├── MatchStatus.java                    <- Enum
    │   │   │   │   └── RootCauseCategory.java              <- Enum
    │   │   │   └── repository/
    │   │   │       ├── TenantRepository.java
    │   │   │       ├── BankAccountRepository.java
    │   │   │       ├── BankStatementBatchRepository.java
    │   │   │       ├── BankStatementLineRepository.java
    │   │   │       ├── TransactionLedgerRepository.java
    │   │   │       ├── ReconciliationMatchRepository.java
    │   │   │       ├── DiscrepancyItemRepository.java
    │   │   │       ├── JournalEntryProposalRepository.java
    │   │   │       ├── BankTemplateRepository.java
    │   │   │       └── AuditLogRepository.java
    │   │   ├── api/
    │   │   │   ├── AuthController.java
    │   │   │   ├── DashboardController.java
    │   │   │   ├── IngestController.java
    │   │   │   ├── DiscrepancyController.java
    │   │   │   ├── TemplateController.java
    │   │   │   └── AuditLogController.java
    │   │   ├── dto/
    │   │   │   ├── LoginRequest.java
    │   │   │   ├── AuthResponse.java
    │   │   │   ├── IngestionResponse.java
    │   │   │   ├── DiscrepancyDetailDTO.java
    │   │   │   └── TemplateDTO.java
    │   │   ├── grpc/
    │   │   │   ├── StatementIngestionGrpcServer.java
    │   │   │   └── AgenticDiscrepancyGrpcServer.java
    │   │   └── exception/
    │   │       ├── GlobalExceptionHandler.java
    │   │       ├── ResourceNotFoundException.java
    │   │       ├── InvalidAccountingEntryException.java
    │   │       └── UnauthorizedException.java
    │   └── resources/
    │       ├── application.yml
    │       └── db/migration/
    │           └── V1__init_schema.sql
    └── test/java/com/smartreconcile/
        ├── engine/DeterministicMatcherTest.java
        └── ledger/AccountingGuardrailTest.java
```

---

## 2. Python AI Coprocessor Package Architecture (`ai-coprocessor/`)

```
ai-coprocessor/
├── pyproject.toml
├── requirements.txt
├── Dockerfile
├── main.py                                     <- FastAPI + gRPC Entry Point
└── app/
    ├── config.py                               <- Pydantic Settings (env vars)
    ├── parser/
    │   ├── statement_parser.py                 <- Dispatcher: Template vs VLM
    │   └── template_engine.py                  <- Regex/CSV deterministic parser
    ├── vlm/
    │   └── pdf_vlm_parser.py                   <- PyMuPDF + Vision-LLM extractor
    ├── agent/
    │   ├── discrepancy_agent.py                <- LangChain agent orchestrator
    │   └── tools/
    │       ├── fx_tool.py                      <- Historical FX rate lookup
    │       ├── fee_tool.py                     <- Acquirer interchange fee verifier
    │       └── timezone_tool.py                <- UTC vs local cutoff normalizer
    └── grpc_server/
        ├── ingestion_servicer.py               <- gRPC server for StreamBankEvents
        └── proto_stubs/                        <- Auto-generated Python Protobuf stubs
```

---

## 3. Pre-Consideraciones Técnicas (Backend-Specific)

### 3.1 Java 21 Virtual Threads
- Spring Boot 3.2+ soporta Virtual Threads de forma nativa con la property `spring.threads.virtual.enabled=true` en `application.yml`.
- Alternativamente, se puede configurar un `Executor` bean personalizado usando `Executors.newVirtualThreadPerTaskExecutor()`.
- El motor de matching (`DeterministicMatcher`) debe usar Virtual Threads para procesar eventos de transacción en paralelo sin agotar el pool de OS threads.

### 3.2 gRPC & Protobuf
- El archivo `.proto` compartido vive en `/proto/reconciliation.proto` en la raíz del monorepo.
- Java genera stubs con el plugin Maven `protobuf-maven-plugin`.
- Python genera stubs con `grpcio-tools` (`python -m grpc_tools.protoc`).
- Ambos servicios deben usar la misma versión de Protobuf (v3).

### 3.3 Redis como Índice de Matching
- Redis almacena índices temporales de matching durante el ciclo de reconciliación. NO es la base de datos persistente.
- Estructura de clave Redis para matching exacto: `match:{tenant_id}:{reference_id}:{amount}:{currency}`.
- Redis también sirve como cola de trabajos para discrepancias: `LPUSH queue:discrepancies:ai {json_payload}`.

### 3.4 Maven Dependencies (pom.xml)
Dependencias obligatorias para `backend-core`:
- `spring-boot-starter-web` (Spring MVC REST)
- `spring-boot-starter-security` (Spring Security)
- `spring-boot-starter-data-jpa` (Hibernate + JPA)
- `spring-boot-starter-data-redis` (Spring Data Redis)
- `spring-boot-starter-validation` (Bean Validation @NotNull, @Size)
- `spring-boot-starter-websocket` (WebSocket support)
- `postgresql` (JDBC driver)
- `flyway-core` + `flyway-database-postgresql` (SQL migrations)
- `jjwt-api`, `jjwt-impl`, `jjwt-jackson` (JWT - io.jsonwebtoken 0.12+)
- `grpc-spring-boot-starter` (gRPC server integration)
- `protobuf-java` (Google Protobuf runtime)
- `spring-boot-starter-test` (JUnit 5, Mockito)

### 3.5 Dockerfile del Backend Java

Debe usar un multi-stage build con Eclipse Temurin JDK 21 para compilar y JRE 21 para ejecutar. El entrypoint es `java -jar app.jar`. Puerto expuesto: `8080` (REST) y `9090` (gRPC).

### 3.6 Dockerfile del AI Coprocessor Python

Debe usar `python:3.11-slim` como imagen base. Instalar dependencias con `pip install -r requirements.txt`. El entrypoint ejecuta `uvicorn main:app` en el puerto `8001` (REST) y un servidor gRPC en el puerto `9091`.
