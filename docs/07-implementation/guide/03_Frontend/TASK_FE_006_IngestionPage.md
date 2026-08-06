# TASK FE-006 — Estudio de Ingesta de Extractos Bancarios (`IngestionPage.jsx`)

**Módulo:** `web-ui/src/pages/`  
**Tipo de Archivo:** Componente de Página React Autenticado  
**Prioridad:** ALTA — Carga de archivos de extractos bancarios en múltiples formatos.  
**Depende de:** `TASK_FE_002`  
**Bloquea:** Ingesta de archivos para conciliación  

---

## 1. Propósito y Justificación Técnica

Permite al usuario subir archivos de extractos bancarios (PDF escaneados, CSV, MT940) mediante una zona interactiva Drag-and-Drop. Muestra una barra de progreso en tiempo real y una tabla de previsualización con los datos parseados y el nivel de confianza de extracción antes de enviar la orden de conciliación masiva.

---

## 2. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `IngestionPage.jsx`
1. Maqueta zona dropzone de carga de archivos con soporte para soltar o explorar archivos.
2. Al soltar un archivo, realiza petición `FormData` multipart a `POST /api/v1/ingest/upload`.
3. Muestra estado de procesamiento y renderiza los primeros 50 registros extraídos en una tabla de previsualización.

---

## 3. Post-Condiciones y Criterios de Tarea Completada con Éxito (Acceptance Criteria)

| # | Condición que Debe Cumplirse | Consecuencia / Riesgo si Falla |
|---|---|---|
| 1 | Carga multipart soporta archivos de hasta 50MB | Archivos grandes son rechazados sin indicación |
| 2 | Previsualización muestra las transacciones parseadas correctamente | El usuario no puede verificar la extracción |

---

## 4. Comando de Verificación

```bash
npm run build
```
