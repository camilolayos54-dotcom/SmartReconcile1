# Database Master Guide & Schema Architecture

**Project:** SmartReconcile  
**Database Engine:** PostgreSQL 16+  
**Migration Tool:** Flyway (`classpath:db/migration`)  

Este archivo es la referencia maestra de la capa de base de datos. Contiene la estructura de scripts de migración, convenciones de nombrado y pre-consideraciones que aplican exclusivamente a PostgreSQL y Flyway.

---

## 1. Estructura de Archivos de Migración

```
backend-core/src/main/resources/
└── db/
    └── migration/
        ├── V1__create_tenants_and_bank_accounts.sql
        ├── V2__create_statement_batches_and_lines.sql
        ├── V3__create_transaction_ledgers.sql
        ├── V4__create_reconciliation_matches.sql
        ├── V5__create_discrepancy_and_journal_tables.sql
        ├── V6__create_bank_templates.sql
        ├── V7__create_audit_logs.sql
        └── V8__create_indexes.sql
```

---

## 2. Pre-Consideraciones Técnicas (Database-Specific)

### 2.1 Convenciones de Nombrado SQL
- **Tablas:** snake_case plural (ej: `tenants`, `bank_accounts`, `reconciliation_matches`).
- **Columnas:** snake_case singular (ej: `tenant_id`, `transaction_date`, `delta_amount`).
- **Primary Keys:** Siempre `id UUID` generado con `uuid_generate_v4()`.
- **Foreign Keys:** Nombradas como `{tabla_referenciada_singular}_id` (ej: `tenant_id`, `batch_id`).

### 2.2 Tipos de Datos Obligatorios
- **Montos monetarios:** `NUMERIC(18, 4)`. Nunca usar `FLOAT`, `DOUBLE` ni `REAL`. Los errores de redondeo en punto flotante son inaceptables para datos financieros.
- **Fechas de transacción:** `DATE` (sin hora) para fechas de transacción bancaria. `TIMESTAMP WITH TIME ZONE` para timestamps de sistema (created_at, matched_at).
- **UUIDs:** Requieren la extensión `uuid-ossp`. Activar con `CREATE EXTENSION IF NOT EXISTS "uuid-ossp"` al inicio del primer script.
- **JSON flexible:** `JSONB` (no `JSON`) para campos como `column_mapping_json` y `metadata`. JSONB permite indexación y consultas eficientes.

### 2.3 Estrategia de Migración Flyway
- Cada script tiene prefijo `V{N}__` (dos underscores). Flyway los ejecuta en orden numérico.
- Una vez ejecutado un script en producción, NUNCA se modifica. Para cambios posteriores, crear un nuevo script `V{N+1}__alter_xxx.sql`.
- El `ddl-auto` de Hibernate debe ser `validate` (nunca `create` ni `update`). Flyway gestiona el esquema, Hibernate solo valida que coincida con las entidades.

### 2.4 Multi-Tenancy
- Todas las tablas con datos de negocio contienen `tenant_id UUID NOT NULL REFERENCES tenants(id)`.
- La aplicación Java inyecta `tenant_id` automáticamente en cada query mediante un filtro de contexto (`TenantContextHolder`).
- Esto garantiza aislamiento de datos entre organizaciones sin necesidad de schemas separados por tenant.
