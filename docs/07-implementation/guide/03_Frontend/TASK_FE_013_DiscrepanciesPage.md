- [x] TASK_FE_013 — Vista Explorador de Discrepancias y Tabla de Cuadrante 📅 2026-08-05 14:00
	- [x] Paso 1: Crear el archivo src/pages/DiscrepanciesPage.jsx
		- [x] Diseñar la tabla de discrepancias dividida en 2 paneles comparativos (Banco vs Contabilidad)
		- [x] Crear barra de filtros por nivel de severidad (Alta, Media, Baja) y estado de resolución
	- [x] Paso 2: Conectar la tabla con la API REST
		- [x] Consultar GET /api/v1/discrepancies con paginación en servidor

# TASK_FE_013 — Vista Explorador de Discrepancias y Tabla de Cuadrante

**Módulo:** `web-ui/`  
**Porcentaje de Avance:** 55% -> 60%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Interfaz principal de trabajo de auditoría (60%). Muestra las partidas no conciliadas o descuadradas lado a lado para su inspección y ajuste.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Tablas Comparativas de Lado a Lado (Side-by-Side Tables):** Visualización simultánea de dos registros discordantes resaltando las celdas con diferencias numéricas.
* **Filtrado y Paginación Servidor de Grandes Volúmenes:** Sincronización de parámetros de consulta con la API para navegar entre miles de discrepancias.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/pages/DiscrepanciesPage.jsx`
1. Diseña la tabla comparativa con columnas: ID Discrepancia, Fecha, Registro Banco, Registro Libro, Diferencia Moneda, Nivel Severidad, Acciones.
2. Aplica clases CSS para colorear las celdas de diferencia según su magnitud.
3. Agrega los botones de filtro por estado: 'Todas', 'Pendientes', 'Ajustadas Manualmente', 'Ignoradas'.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
