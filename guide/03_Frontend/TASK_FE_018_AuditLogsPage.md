- [x] TASK_FE_018 — Vista de Logs de Auditoría e Inmutabilidad Hash Contable 📅 2026-08-05 16:30
	- [x] Paso 1: Crear el archivo src/pages/AuditLogsPage.jsx
		- [x] Diseñar la tabla de registros de auditoría inmutables (Audit Trail)
		- [x] Mostrar sellos de tiempo, usuario ejecutores, tipo de acción y Hashes SHA-256 de verificación
	- [x] Paso 2: Conectar con la API de Auditoría
		- [x] Consultar GET /api/v1/audit/logs

# TASK_FE_018 — Vista de Logs de Auditoría e Inmutabilidad Hash Contable

**Módulo:** `web-ui/`  
**Porcentaje de Avance:** 80% -> 85%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Garantiza el cumplimiento legal y la inmutabilidad de los ajustes contables (85%), presentando el registro completo de auditoría con hashes SHA-256.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Diseño de Registros Inmutables de Auditoría (Audit Trail):** Presentación de historiales de eventos de seguridad y cambios contables que no admiten edición ni borrado.
* **Visualización de Hashes Criptográficos:** Mapeo truncado de cadenas SHA-256 con opción de copia en portapapeles para verificación externa.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/pages/AuditLogsPage.jsx`
1. Diseña la tabla de auditoría: Timestamp UTC, Auditor, Acción Realizada, Entidad Afectada, Dirección IP, Hash de Inmutabilidad SHA-256.
2. Permite filtrar los registros por rango de fechas y tipo de acción realizada.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
