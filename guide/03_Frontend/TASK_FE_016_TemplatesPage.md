- [x] TASK_FE_016 — Vista de Plantillas de Reglas y Parámetros de Conciliación 📅 2026-08-05 15:30
	- [x] Paso 1: Crear el archivo src/pages/TemplatesPage.jsx
		- [x] Diseñar grilla de plantillas configuradas (ej: Conciliación Bancaria Mensual, Tarjetas de Crédito)
		- [x] Mostrar tolerancias numéricas (margen de error de centavos) y reglas activas
	- [x] Paso 2: Conectar con la API de Plantillas
		- [x] Consultar GET /api/v1/templates y habilitar activación/desactivación

# TASK_FE_016 — Vista de Plantillas de Reglas y Parámetros de Conciliación

**Módulo:** `web-ui/`  
**Porcentaje de Avance:** 70% -> 75%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Administra las reglas de negocio y algoritmos de coincidencia (75%), definiendo tolerancias de centavos y márgenes de días entre fechas.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Gestión de Reglas de Negocio en Frontend:** Configuración de parámetros de tolerancia numérica y temporal para algoritmos de cruce contable.
* **Tarjetas de Configuración con Alternadores (Toggle Switches):** Uso de componentes tipo switch para activar o pausar reglas específicas.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/pages/TemplatesPage.jsx`
1. Mapea la lista de plantillas conteniendo: Nombre de la plantilla, Tolerancia de días, Margen de diferencia permitida y Estado (Activa/Inactiva).
2. Agrega botones para 'Crear Nueva Plantilla' y 'Editar Reglas'.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
