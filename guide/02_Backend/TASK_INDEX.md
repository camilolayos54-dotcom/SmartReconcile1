# Índice Maestro de Tareas: Backend (Java 21 Spring Boot + Python 3.11 Coprocessor) — SmartReconcile

**Proyecto:** SmartReconcile  
**Capa:** Backend Core Java 21 LTS (`Spring Boot 3.2+`, Virtual Threads) + Coprocesador IA Python 3.11 (`FastAPI`, `gRPC`, `LangChain`)  
**Estructura Base:** `backend-core/` y `ai-coprocessor/`  

---

## Catálogo Detallado de Tareas

### Sprint 1: Scaffolding, Configuración & Esqueleto Base

| ID | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **BE-001** | [`TASK_BE_001`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_001_SmartReconcileApplication.md) | **Punto de entrada Spring Boot Java 21:** Clase `SmartReconcileApplication.java` anotada con `@SpringBootApplication`, `@EnableScheduling` y `@EnableJpaAuditing`. | CRÍTICA | pom.xml |
| **BE-002** | [`TASK_BE_002`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_002_PomXml.md) | **Manifiesto Maven Java 21:** Archivo `pom.xml` con Spring Boot 3.2+, gRPC Protobuf plugin, JJWT 0.12+, PostgreSQL, Redis, Flyway y JUnit 5. | CRÍTICA | Ninguna |
| **BE-003** | [`TASK_BE_003`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_003_ApplicationYml.md) | **Configuración de ambiente:** Archivo `application.yml` activando Virtual Threads (`spring.threads.virtual.enabled=true`), pool HikariCP PostgreSQL, Redis host, gRPC server en puerto 9090 y JWT secret keys. | CRÍTICA | BE-002 |
| **BE-004** | [`TASK_BE_004`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_004_VirtualThreadConfig.md) | **Ejecutor de Virtual Threads Project Loom:** Clase `VirtualThreadConfig.java` registrando un Bean `Executor` basado en `Executors.newVirtualThreadPerTaskExecutor()`. | ALTA | BE-001 |
| **BE-005** | [`TASK_BE_005`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_005_JpaAuditingConfig.md) | **Auditoría automática JPA:** Clase `JpaAuditingConfig.java` para auto-completar `@CreatedDate` y `@LastModifiedDate`. | ALTA | BE-001 |

---

### Sprint 2: Entidades JPA del Dominio (Modelo de Datos)

| ID | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **BE-006** | [`TASK_BE_006`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_006_Enums.md) | **Enums fuertemente tipados:** Enums `MatchType` (`MATCHED`, `MATCHED_FUZZY`, `DISCREPANCY`), `MatchStatus` y `RootCauseCategory` (`UNANNOUNCED_BANK_FEE`, `FX_RATE_VARIANCE`, `TIMEZONE_CUTOFF_SHIFT`). | ALTA | BE-001 |
| **BE-007** | [`TASK_BE_007`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_007_TenantEntity.md) | **Entidad JPA de Organización:** `Tenant.java` mapeando la tabla `tenants` con auditoría y moneda base. | ALTA | BE-005 |
| **BE-008** | [`TASK_BE_008`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_008_BankAccountEntity.md) | **Entidad JPA de Cuenta Bancaria:** `BankAccount.java` mapeando la tabla `bank_accounts`. | ALTA | BE-007 |
| **BE-009** | [`TASK_BE_009`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_009_BankStatementBatchEntity.md) | **Entidad JPA de Lote de Extracto:** `BankStatementBatch.java` almacenando saldos en `BigDecimal`. | ALTA | BE-008 |
| **BE-010** | [`TASK_BE_010`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_010_BankStatementLineEntity.md) | **Entidad JPA de Línea de Extracto:** `BankStatementLine.java` mapeando filas individuales de transacciones bancarias. | ALTA | BE-009 |
| **BE-011** | [`TASK_BE_011`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_011_TransactionLedgerEntity.md) | **Entidad JPA del Libro Interno:** `TransactionLedger.java` mapeando cobros y abonos internos. | ALTA | BE-007 |
| **BE-012** | [`TASK_BE_012`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_012_ReconciliationMatchEntity.md) | **Entidad JPA de Pareja Conciliada:** `ReconciliationMatch.java` asociando transacción interna y extracto bancario. | ALTA | BE-010 |
| **BE-013** | [`TASK_BE_013`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_013_DiscrepancyItemEntity.md) | **Entidad JPA de Discrepancia:** `DiscrepancyItem.java` almacenando la categoría de causa raíz y score de confianza IA. | ALTA | BE-012 |
| **BE-014** | [`TASK_BE_014`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_014_JournalEntryProposalEntity.md) | **Entidades JPA de Propuesta de Ajuste:** `JournalEntryProposal.java` y `JournalEntryLine.java` representando asientos de partida doble. | ALTA | BE-013 |
| **BE-015** | [`TASK_BE_015`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_015_BankTemplateEntity.md) | **Entidad JPA de Plantilla Bancaria:** `BankTemplate.java` almacenando firmas regex y mapeos JSONB (`MOD-ING-TPL`). | ALTA | BE-007 |
| **BE-016** | [`TASK_BE_016`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_016_AuditLogEntity.md) | **Entidad JPA de Auditoría SOC-2:** `AuditLog.java` almacenando hashes criptográficos SHA-256 inmutables. | ALTA | BE-007 |

---

### Sprint 3: Repositorios JPA & Excepciones

| ID | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **BE-017** | [`TASK_BE_017`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_017_Repositories.md) | **Interfaces de Acceso a Datos JPA:** 10 interfaces `JpaRepository` con consultas custom por tenant y referencia. | ALTA | BE-007 a BE-016 |
| **BE-018** | [`TASK_BE_018`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_018_ExceptionHandling.md) | **Manejador Global de Excepciones REST:** `GlobalExceptionHandler.java` respondiendo según el estándar RFC 7807. | ALTA | BE-001 |

---

### Sprint 4: Seguridad (JWT, CSRF, RBAC)

| ID | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **BE-019** | [`TASK_BE_019`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_019_JwtService.md) | **Servicio de firma JWT:** `JwtService.java` gestionando creación y validación HMAC-SHA256. | CRÍTICA | BE-001 |
| **BE-020** | [`TASK_BE_020`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_020_JwtAuthenticationFilter.md) | **Filtro de Cookie HttpOnly JWT:** `JwtAuthenticationFilter.java` extrayendo el token seguro de cookie HttpOnly. | CRÍTICA | BE-019 |
| **BE-021** | [`TASK_BE_021`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_021_CsrfProtectionFilter.md) | **Filtro de Verificación Anti-CSRF:** `CsrfProtectionFilter.java` validando el header `X-CSRF-TOKEN`. | ALTA | BE-020 |
| **BE-022** | [`TASK_BE_022`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_022_SecurityConfig.md) | **Configuración Spring Security Chain:** `SecurityConfig.java` registrando filtros y reglas de autorización. | CRÍTICA | BE-020 |

---

### Sprint 5: Motor de Matching & Lógica Contable Core

| ID | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **BE-023** | [`TASK_BE_023`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_023_MemoryIndexManager.md) | **Administrador del Índice Redis en Memoria:** `MemoryIndexManager.java` para búsqueda sub-milisegundo. | CRÍTICA | BE-004 |
| **BE-024** | [`TASK_BE_024`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_024_AccountingGuardrail.md) | **Validador Contable de Partida Doble:** `AccountingGuardrail.java` garantizando $\sum D = \sum C$. | CRÍTICA | BE-014 |
| **BE-025** | [`TASK_BE_025`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_025_DeterministicMatcher.md) | **Motor de Matching en Hilos Virtuales:** `DeterministicMatcher.java` ejecutando conciliaciones a >10.000 TPS. | CRÍTICA | BE-023 |

---

### Sprint 6: DTOs & Controladores REST API

| ID | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **BE-026** | [`TASK_BE_026`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_026_DTOs.md) | **Records DTO Java:** Records inmutables para peticiones y respuestas REST. | ALTA | BE-006 |
| **BE-027** | [`TASK_BE_027`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_027_AuthController.md) | **Controlador REST Autenticación:** `AuthController.java` expuesto en `/api/v1/auth/login`. | ALTA | BE-019 |
| **BE-028** | [`TASK_BE_028`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_028_IngestController.md) | **Controlador REST Ingesta de Extractos:** `IngestController.java` (`POST /api/v1/ingest/upload`). | ALTA | BE-009 |
| **BE-029** | [`TASK_BE_029`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_029_DiscrepancyController.md) | **Controlador REST Discrepancias:** `DiscrepancyController.java` para lista y aprobación en 1 clic. | ALTA | BE-013 |
| **BE-030** | [`TASK_BE_030`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_030_TemplateController.md) | **Controlador REST Plantillas Bancarias:** `TemplateController.java` (`CRUD /api/v1/templates`). | ALTA | BE-015 |
| **BE-031** | [`TASK_BE_031`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_031_DashboardController.md) | **Controlador REST Métricas Dashboard:** `DashboardController.java` (`GET /api/v1/dashboard/metrics`). | MEDIA | BE-017 |
| **BE-032** | [`TASK_BE_032`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_032_AuditLogController.md) | **Controlador REST Auditoría SOC-2:** `AuditLogController.java` con exportación a PDF firmado. | MEDIA | BE-016 |

---

### Sprint 7: Servidores gRPC & WebSocket

| ID | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **BE-033** | [`TASK_BE_033`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_033_ProtobufSchema.md) | **Esquema Protobuf de IPC:** Archivo `proto/reconciliation.proto` declarando servicios gRPC. | CRÍTICA | Ninguna |
| **BE-034** | [`TASK_BE_034`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_034_GrpcIngestionServer.md) | **Servidor gRPC de Ingesta:** `StatementIngestionGrpcServer.java` recibiendo stream de eventos. | ALTA | BE-025 |
| **BE-035** | [`TASK_BE_035`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_035_GrpcAgentServer.md) | **Servidor gRPC de Agente IA:** `AgenticDiscrepancyGrpcServer.java` recibiendo propuestas de ajuste. | ALTA | BE-024 |
| **BE-036** | [`TASK_BE_036`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_036_WebSocketConfig.md) | **Configuración WebSocket STOMP:** `WebSocketConfig.java` empujando métricas en tiempo real a React UI. | MEDIA | BE-022 |

---

### Sprint 8: Coprocesador IA Python

| ID | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **BE-037** | [`TASK_BE_037`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_037_PythonProjectSetup.md) | **Scaffolding Python FastAPI:** `pyproject.toml`, `requirements.txt` y `main.py`. | ALTA | Python 3.11 |
| **BE-038** | [`TASK_BE_038`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_038_StatementParser.md) | **Parser Determinista de Extractos:** `statement_parser.py` y `template_engine.py` (regex CSV/MT940). | ALTA | BE-037 |
| **BE-039** | [`TASK_BE_039`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_039_VisionLLMParser.md) | **Parser de PDFs escaneados con Vision-LLM:** `pdf_vlm_parser.py` (PyMuPDF + VLM). | ALTA | BE-037 |
| **BE-040** | [`TASK_BE_040`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_040_DiscrepancyAgent.md) | **Agente Investigador LangChain:** `discrepancy_agent.py` con herramientas de divisas, comisiones y zona horaria. | ALTA | BE-033 |
| **BE-041** | [`TASK_BE_041`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/02_Backend/TASK_BE_041_PythonGrpcServer.md) | **Servidor gRPC Python:** `ingestion_servicer.py` transmitiendo eventos a Java core. | ALTA | BE-033 |
