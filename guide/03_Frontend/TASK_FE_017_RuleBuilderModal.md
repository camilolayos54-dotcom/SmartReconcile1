- [ ] TASK_FE_017 — Componente Constructor de Reglas de Coincidencia Personalizadas 📅 2026-08-05 16:00
	- [ ] Paso 1: Crear src/components/templates/RuleBuilderModal.jsx
		- [ ] Diseñar formulario visual de construcción de reglas condicionales (SI Monto es Igual Y Fecha difiere <= X días)
		- [ ] Agregar validación sintáctica de expresiones de regla
	- [ ] Paso 2: Guardar plantilla en el backend
		- [ ] Enviar POST /api/v1/templates

# TASK_FE_017 — Componente Constructor de Reglas de Coincidencia Personalizadas

**Módulo:** `web-ui/`  
**Porcentaje de Avance:** 75% -> 80%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Construye reglas de conciliación personalizadas dinámicas (80%), permitiendo a los contadores crear algoritmos de cruce adaptados a su negocio.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Constructores de Expresiones Lógicas Visuales (Query Builders):** Creación de interfaces compuestas por bloques de condición (SI, Y, O, IGUAL_A, CONTIENE).
* **Validación de Sintaxis en Cliente:** Verificación de integridad de las reglas antes de ser compiladas por el backend.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/components/templates/RuleBuilderModal.jsx`
1. Diseña la interfaz de adición de condiciones lógicas dinámicas.
2. Permite seleccionar campos, operadores de comparación (==, <=, >=, CONTAINS) y valores de tolerancia.
3. Envía la nueva plantilla configurada al servidor.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
