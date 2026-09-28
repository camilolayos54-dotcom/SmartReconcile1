# Índice Maestro de Tareas: Base de Datos (PostgreSQL 16+) — SmartReconcile

**Proyecto:** SmartReconcile  
**Capa:** Base de Datos Relacional (`PostgreSQL 16+` & `Flyway`)  
**Ubicación de Migraciones:** `backend-core/src/main/resources/db/migration/`  

---

## Descripción General de la Capa de Datos

SmartReconcile utiliza PostgreSQL 16 con Flyway para migraciones evolutivas. Garantiza:
- Claves primarias UUID (`uuid_generate_v4()`).
- Precisión numérica obligatoria `NUMERIC(18, 4)` para saldos e importes financieros (sin flotantes).
- Tablas aisladas por cliente mediante `tenant_id UUID NOT NULL`.
- Almacenamiento JSONB para mapeos dinámicos de extractos bancarios.

---

## Catálogo Detallado de Tareas

| ID Tarea | Archivo de Especificación | Descripción Técnica Detallada | Prioridad | Dependencias |
|---|---|---|---|---|
| **DB-001** | [`TASK_DB_001`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/01_Database/TASK_DB_001_InitSchemaMigration.md) | **Creación del esquema relacional completo (11 tablas):** Script `V1__init_schema.sql`. Activa la extensión `uuid-ossp` y declara en orden las 11 tablas del dominio: `tenants` (organizaciones multi-tenant), `bank_accounts` (cuentas recaudadoras), `bank_statement_batches` (lotes de extractos), `bank_statement_lines` (líneas individuales de extractos), `transaction_ledgers` (libro contable interno), `reconciliation_matches` (parejas conciliadas), `discrepancy_items` (ítems no conciliados), `journal_entry_proposals` y `journal_entry_lines` (propuestas de partida doble), `bank_templates` (plantillas JSONB) y `audit_logs` (trazabilidad SOC-2). | CRÍTICA | Ninguna |
| **DB-002** | [`TASK_DB_002`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/01_Database/TASK_DB_002_IndexesAndConstraints.md) | **Construcción de índices B-Tree de alto rendimiento:** Script `V2__add_indexes.sql`. Crea índices compuestos en columnas de alta frecuencia (`transaction_ledgers(tenant_id, reference_id)`, `bank_statement_lines(batch_id, reference_id)`, `reconciliation_matches(ledger_id, statement_line_id)` y `audit_logs(tenant_id, cryptographic_hash)`) para garantizar tiempos de coincidencia <1ms durante ejecuciones de >10.000 TPS. | ALTA | DB-001 |
| **DB-003** | [`TASK_DB_003`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/01_Database/TASK_DB_003_SeedDemoData.md) | **Sembrado de datos iniciales y plantillas bancarias:** Script `V3__seed_demo_data.sql`. Inserta la organización de prueba por defecto (`Acme Fintech Corp`), cuenta bancaria recaudadora USD y plantillas pre-configuradas de parsing regex para extractos bancarios en CSV y MT940 (`MOD-ING-TPL`). | MEDIA | DB-002 |
