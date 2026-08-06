# Índice Maestro de Tareas: DevOps & CI/CD — SmartReconcile

**Proyecto:** SmartReconcile  
**Capa:** DevOps & Infraestructura de Contenedores (`Docker Compose`, `GitHub Actions`)  

---

## Catálogo Detallado de Tareas

| ID Tarea | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **OPS-001** | [`TASK_OPS_001`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/04_CICD_Docker/TASK_OPS_001_DockerComposeSetup.md) | **Orquestación de entorno local:** Archivo `docker-compose.yml` en la raíz del monorepo levanta contenedores con `postgres:16-alpine` (puerto 5432) y `redis:7-alpine` (puerto 6379) con volumen de almacenamiento persistente. | CRÍTICA | Ninguna |
| **OPS-002** | [`TASK_OPS_002`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/04_CICD_Docker/TASK_OPS_002_GitHubActionsPipeline.md) | **Pipeline de integración continua (CI):** Archivo `.github/workflows/ci.yml` ejecutando builds paralelos de `mvn test` para Java core y `pytest` para el coprocesador IA Python en cada Pull Request. | ALTA | OPS-001 |
