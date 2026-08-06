# TASK FE-004 — Panel Principal de Control KPI (`DashboardPage.jsx`)

**Módulo:** `web-ui/src/pages/`  
**Tipo de Archivo:** Componente de Página React Autenticado  
**Prioridad:** ALTA — Centro de mando operacional de la conciliación bancaria.  
**Depende de:** `TASK_FE_002`  
**Bloquea:** Vista de monitoreo operacional en tiempo real  

---

## 1. Propósito y Justificación Técnica

Renderiza las 4 tarjetas KPI centrales:
1. `Volumen Total Ingestado`
2. `% de Coincidencia Automática` (ej: 98.4%)
3. `Discrepancias Pendientes` (con alerta roja `#E11D48`)
4. `Fuga Financiera Recuperada` (en la moneda base seleccionada: USD, EUR, COP, MXN)

Debajo de las tarjetas, renderiza la tabla de stream en vivo de emparejamientos en tiempo real recibidos mediante WebSocket STOMP (`/ws-reconcile`).

---

## 2. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `DashboardPage.jsx`
1. Consulta inicial de métricas a `GET /api/v1/dashboard/metrics`.
2. Suscripción a canal WebSocket `/topic/matches` actualizando dinámicamente la grilla de stream.
3. Formatea automáticamente los montos de fuga financiera según la moneda base activa en `useCurrencyStore`.

---

## 3. Post-Condiciones y Criterios de Tarea Completada con Éxito (Acceptance Criteria)

| # | Condición que Debe Cumplirse | Consecuencia / Riesgo si Falla |
|---|---|---|
| 1 | Las 4 tarjetas KPI se llenan con datos reales del backend | Métricas en cero o no disponibles |
| 2 | El stream de eventos WebSocket inserta nuevas filas en la tabla sin parpadeos del DOM | Inconsistencia de eventos en vivo |
| 3 | Cambiar la moneda en el header convierte dinámicamente la tarjeta de fuga financiera | Monto desalineado de la divisa elegida |

---

## 4. Comando de Verificación

```bash
npm run build
```
