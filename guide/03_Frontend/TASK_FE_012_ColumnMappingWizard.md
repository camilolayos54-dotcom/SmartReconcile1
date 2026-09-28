- [ ] TASK_FE_012 — Componente Wizard de Previsualización y Mapeo de Columnas 📅 2026-08-05 13:30
	- [ ] Paso 1: Crear src/components/ingest/ColumnMappingWizard.jsx
		- [ ] Diseñar tabla de previsualización de las primeras 5 filas del archivo subido
		- [ ] Crear selectores desplegables para mapear campos requeridos: Fecha, Referencia/NIT, Monto, Descripción
	- [ ] Paso 2: Enviar mapeo al backend
		- [ ] Invocar POST /api/v1/ingestion/confirm-mapping para lanzar la conciliación

# TASK_FE_012 — Componente Wizard de Previsualización y Mapeo de Columnas

**Módulo:** `web-ui/`  
**Porcentaje de Avance:** 50% -> 55%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Guía al usuario en el mapeo de estructuras heterogéneas de archivos (55%), asegurando que las columnas del CSV coincidan con el modelo contable.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Mapeo Dinámico de Esquemas de Datos (Column Mapping UI):** Asociación visual entre encabezados de archivos desconocidos y atributos del sistema.
* **Validación de Campos Contables Obligatorios:** Garantizar que se hayan asignado las columnas clave de Fecha, Monto e Identificador antes de procesar.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/components/ingest/ColumnMappingWizard.jsx`
1. Renderiza la tabla de muestra con las primeras filas leídas del archivo.
2. Agrega controles `<select>` sobre cada columna para asignar la propiedad del sistema (`DATE`, `AMOUNT`, `REFERENCE`, `DESCRIPTION`).
3. Valida la asignación completa y envía la confirmación de inicio de trabajo de conciliación al servidor.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
