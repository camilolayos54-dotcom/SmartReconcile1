# TASK FE-005 — Centro de Revisión de Discrepancias (`DiscrepanciesPage.jsx`)

**Módulo:** `web-ui/src/pages/`  
**Tipo de Archivo:** Componente de Página React Autenticado  
**Prioridad:** ALTA — Interfaz maestro-detalle para revisión y aprobación en 1 clic de propuestas IA.  
**Depende de:** `TASK_FE_002`  
**Bloquea:** Flujo de resolución de inconsistencias bancarias  

---

## 1. Propósito y Justificación Técnica

Interfaz donde los analistas revisan las inconsistencias detectadas. Muestra una grilla comparativa lado a lado entre la transacción del libro interno y la línea del extracto bancario, una tarjeta explicativa en Markdown con el razonamiento paso a paso generado por la IA (ej: "Comisión bancaria no anunciada del 1.5%"), la propuesta de ajuste contable de partida doble ($\sum D = \sum C$), score de confianza (ej: 94%), y botón de aprobación en 1 clic.

---

## 2. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `DiscrepanciesPage.jsx`
1. Consulta la lista de discrepancias a `GET /api/v1/discrepancies`.
2. Al seleccionar un ítem de la lista, renderiza en la vista de detalle:
   * Comparador visual lado a lado con colores de acento (débito/crédito).
   * Tarjeta con renderizado Markdown del razonamiento del agente.
   * Tabla con las líneas del asiento contable propuesto.
   * Botón `#btn-approve-proposal` que llama a `POST /api/v1/discrepancies/{id}/approve`.

---

## 3. Post-Condiciones y Criterios de Tarea Completada con Éxito (Acceptance Criteria)

| # | Condición que Debe Cumplirse | Consecuencia / Riesgo si Falla |
|---|---|---|
| 1 | Comparador muestra claramente la diferencia monetaria (delta) entre ambas fuentes | El analista no entiende la causa de la discrepancia |
| 2 | Clic en "Aprobar Ajuste" envía la petición y elimina la discrepancia de la cola activa | Estado duplicado o no resuelto |

---

## 4. Comando de Verificación

```bash
npm run build
```
