# TASK FE-008 — Visor de Logs de Auditoría SOC-2 (`AuditLogsPage.jsx`)

**Módulo:** `web-ui/src/pages/`  
**Tipo de Archivo:** Componente de Página React Autenticado  
**Prioridad:** MEDIA — Visor de trazabilidad inmutable e informes de cumplimiento SOC-2.  
**Depende de:** `TASK_FE_002`  
**Bloquea:** Auditoría de seguridad y descargas de reportes  

---

## 1. Propósito y Justificación Técnica

Muestra la bitácora inmutable de auditoría. Permite a los gerentes de cumplimiento inspeccionar cada acción realizada en la plataforma, copiar los hashes criptográficos SHA-256 de 64 caracteres de cada evento y descargar un informe oficial firmado en formato PDF (`GET /api/v1/audit-logs/export-pdf`).

---

## 2. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `AuditLogsPage.jsx`
1. Consulta paginada a `GET /api/v1/audit-logs`.
2. Muestra grilla de datos con columnas: Timestamp, Usuario, Tipo de Evento, Hash Criptográfico (con botón de 1 clic para copiar al portapapeles) y Detalles JSON.
3. Botón "Descargar Informe SOC-2 (PDF)" que activa la descarga del PDF binario.

---

## 3. Post-Condiciones y Criterios de Tarea Completada con Éxito (Acceptance Criteria)

| # | Condición que Debe Cumplirse | Consecuencia / Riesgo si Falla |
|---|---|---|
| 1 | Grilla de auditoría muestra el hash SHA-256 completo de 64 caracteres | Pérdida de verificabilidad criptográfica |
| 2 | Botón de exportación descarga un PDF válido y legible | Falla la generación del reporte de auditoría |

---

## 4. Comando de Verificación

```bash
npm run build
```
