# Índice Maestro de Tareas: Frontend (Vite React 18 + Tailwind CSS) — SmartReconcile

**Proyecto:** SmartReconcile  
**Capa:** Frontend SPA (`Vite 5.x`, `React 18`, `Tailwind CSS`, `Zustand`)  
**Paleta:** Corporativa carismática (Navy `#0B192C`, Yellow `#FFD200`, Crimson `#E11D48`)  

---

## Catálogo Detallado de Tareas

| ID Tarea | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **FE-001** | [`TASK_FE_001`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_001_ViteTailwindSetup.md) | **Scaffolding Vite React & Tokens Tailwind:** Configuración de `web-ui/`, `tailwind.config.js` registrando tokens corporativos, fuentes `Inter` y `JetBrains Mono`. | CRÍTICA | Ninguna |
| **FE-002** | [`TASK_FE_002`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_002_AppShellAndNavbar.md) | **Shell de Navegación Autenticado:** `AppShell.jsx`, `HeaderNavbar.jsx` (selector de moneda base USD/EUR/COP/MXN y selector de tenant) y `Sidebar.jsx`. | ALTA | FE-001 |
| **FE-003** | [`TASK_FE_003`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_003_LandingAndLoginPage.md) | **Landing Pública & Login Split-Screen:** `LandingPage.jsx` (hero con calculadora de ROI interactiva) y `LoginPage.jsx` (autenticación 50/50). | ALTA | FE-002 |
| **FE-004** | [`TASK_FE_004`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_004_DashboardPage.md) | **Panel Principal de Control KPI:** `DashboardPage.jsx` (4 tarjetas KPI, selector multi-moneda y tabla de stream live en tiempo real vía WebSocket). | ALTA | FE-002 |
| **FE-005** | [`TASK_FE_005`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_005_DiscrepanciesPage.md) | **Centro de Revisión de Discrepancias:** `DiscrepanciesPage.jsx` con comparador dinámico lado a lado y tarjetas de razonamiento IA con aprobación en 1 clic. | ALTA | FE-002 |
| **FE-006** | [`TASK_FE_006`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_006_IngestionPage.md) | **Estudio de Ingesta de Extractos Bancarios:** `IngestionPage.jsx` con zona dropzone de carga de archivos (PDF, CSV, MT940) y previsualización de tabla. | ALTA | FE-002 |
| **FE-007** | [`TASK_FE_007`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_007_TemplatesPage.md) | **Estudio Mapeador de Plantillas Bancarias:** `TemplatesPage.jsx` (`MOD-ING-TPL`) con lienzo de mapeo visual de columnas y consola de prueba dry-run. | ALTA | FE-002 |
| **FE-008** | [`TASK_FE_008`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_008_AuditLogsPage.md) | **Visor de Logs de Auditoría SOC-2:** `AuditLogsPage.jsx` con grilla de datos de alta densidad, copia de hash SHA-256 y exportación de informe PDF. | MEDIA | FE-002 |
