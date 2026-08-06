# TASK FE-007 — Estudio Mapeador de Plantillas Bancarias (`TemplatesPage.jsx`)

**Módulo:** `web-ui/src/pages/`  
**Tipo de Archivo:** Componente de Página React Autenticado  
**Prioridad:** ALTA — Configuración y prueba interactiva de mapeos de extractos bancarios (`MOD-ING-TPL`).  
**Depende de:** `TASK_FE_002`  
**Bloquea:** Creación de plantillas dinámicas por el usuario  

---

## 1. Propósito y Justificación Técnica

Galería de plantillas bancarias activas e interfaz interactiva para mapear visualmente columnas de archivos CSV/Excel a los campos estándar (Fecha, Referencia, Descripción, Débito, Crédito). Incluye una consola de pruebas dry-run para evaluar expresiones regulares antes de guardarlas.

---

## 2. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `TemplatesPage.jsx`
1. Consulta plantillas existentes a `GET /api/v1/templates`.
2. Implementa formulario de creación/edición de plantilla con asignación gráfica de índices de columna.
3. Botón "Probar Plantilla (Dry-Run)" enviando `POST /api/v1/templates/test-dry-run` para validar el resultado del parsing en tiempo real.

---

## 3. Post-Condiciones y Criterios de Tarea Completada con Éxito (Acceptance Criteria)

| # | Condición que Debe Cumplirse | Consecuencia / Riesgo si Falla |
|---|---|---|
| 1 | Consola dry-run parsea un archivo de muestra sin persistir datos | Imposible saber si una expresión regular es correcta |
| 2 | Guardado de plantilla persiste la firma regex en la base de datos | Mapeo perdido al recargar |

---

## 4. Comando de Verificación

```bash
npm run build
```
