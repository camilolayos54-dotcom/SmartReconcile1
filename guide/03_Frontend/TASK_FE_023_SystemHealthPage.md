- [ ] TASK_FE_023 — Vista de Diagnóstico de Salud del Sistema y Estado de Servicios 📅 2026-08-05 19:00
	- [ ] Paso 1: Crear el archivo src/pages/SystemHealthPage.jsx
		- [ ] Diseñar panel de estado de conectores: Backend Core (Java 21), Coprocesador IA (Python gRPC 9090), PostgreSQL
		- [ ] Mostrar métricas de latencia de respuestas en milisegundos
	- [ ] Paso 2: Consultar endpoint de salud
		- [ ] Invocar GET /api/v1/health

# TASK_FE_023 — Vista de Diagnóstico de Salud del Sistema y Estado de Servicios

**Módulo:** `web-ui/`  
**Porcentaje de Avance:** 97% -> 99%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Ofrece un diagnóstico del estado técnico de la plataforma (99%), monitoreando el estado de conexión del motor Java y el coprocesador gRPC Python.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Monitoreo de Salud de Microservicios y Conectores:** Consumo de endpoints Healthcheck para presentar el estado operacional de bases de datos y microservicios sidecar.
* **Indicadores de Latencia en Milisegundos:** Medición del tiempo de ida y vuelta (RTT) de las peticiones de verificación.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/pages/SystemHealthPage.jsx`
1. Diseña las tarjetas de estado de conectividad de los componentes del sistema.
2. Muestra insignias verdes/rojas indicando el funcionamiento del Backend Core, Coprocesador IA en puerto 9090 y Base de Datos PostgreSQL.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
