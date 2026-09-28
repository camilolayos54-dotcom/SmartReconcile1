- [x] TASK_FE_011 — Vista de Ingestión de Datos y Carga de Archivos Drag & Drop 📅 2026-08-05 13:00
	- [x] Paso 1: Crear el archivo src/pages/IngestionPage.jsx
		- [x] Diseñar zona de arrastrar y soltar archivos (Dropzone) para CSV y Excel
		- [x] Agregar selector del Origen A (Extracto Bancario) y Origen B (Libro Auxiliar Contable)
	- [x] Paso 2: Implementar barra de progreso de subida
		- [x] Mostrar porcentaje de avance de la carga del archivo

# TASK_FE_011 — Vista de Ingestión de Datos y Carga de Archivos Drag & Drop

**Módulo:** `web-ui/`  
**Porcentaje de Avance:** 45% -> 50%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Permite a los auditores subir archivos masivos de extractos bancarios y libros contables (50%) para dar inicio al proceso de conciliación.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **API File HTML5 y Eventos Drag & Drop:** Captura de eventos dragover, dragleave y drop para recibir archivos en el navegador.
* **Carga de Archivos Multipart con Seguimiento de Progreso:** Uso de FormData y la opción onUploadProgress de Axios para notificar el progreso de transferencia.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/pages/IngestionPage.jsx`
1. Maqueta las dos zonas de carga: 'Archivo Origen A (Extracto Bancario)' y 'Archivo Origen B (Libro Auxiliar)'.
2. Agrega los controladores de eventos Drag & Drop para capturar archivos `.csv`, `.xlsx` o `.txt`.
3. Muestra la barra de progreso indicando la transferencia en curso.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
