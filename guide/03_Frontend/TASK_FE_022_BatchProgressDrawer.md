- [ ] TASK_FE_022 — Componente Monitor de Lotes y Progreso de Trabajos en Segundo Plano 📅 2026-08-05 18:30
	- [ ] Paso 1: Crear src/components/jobs/BatchProgressDrawer.jsx
		- [ ] Diseñar panel de monitoreo de trabajos de conciliación asíncronos en segundo plano
		- [ ] Mostrar barra de progreso en tiempo real de registros procesados por segundo
	- [ ] Paso 2: Suscripción a eventos de progreso
		- [ ] Implementar sondeo SSE / Polling a /api/v1/jobs/active

# TASK_FE_022 — Componente Monitor de Lotes y Progreso de Trabajos en Segundo Plano

**Módulo:** `web-ui/`  
**Porcentaje de Avance:** 95% -> 97%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Notifica en tiempo real el avance de ejecuciones masivas de conciliación (97%) que procesan millones de registros en segundo plano.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Monitoreo de Procesamiento por Lotes (Batch Jobs):** Visualización del progreso de tareas pesadas de backend de larga duración.
* **Mecanismos de Actualización en Tiempo Real (Server-Sent Events / Polling):** Recepción contínua de eventos de porcentaje de avance sin recargar la página.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/components/jobs/BatchProgressDrawer.jsx`
1. Diseña la ventana flotante de monitoreo de tareas de conciliación activas.
2. Muestra el porcentaje procesado, velocidad de registros por segundo y tiempo estimado de finalización.
3. Permite cancelar un trabajo de conciliación en curso.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
