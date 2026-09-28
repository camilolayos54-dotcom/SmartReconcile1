- [ ] TASK_FE_014 — Componente Modal de Resolución Manual y Ajuste Contable 📅 2026-08-05 14:30
	- [ ] Paso 1: Crear src/components/discrepancies/ResolutionModal.jsx
		- [ ] Diseñar ventana modal para forzar conciliación manual o aplicar nota de ajuste
		- [ ] Agregar campo para justificación obligatoria del auditor contable
	- [ ] Paso 2: Enviar resolución al servidor
		- [ ] Invocar POST /api/v1/discrepancies/{id}/resolve enviando la nota de auditoría

# TASK_FE_014 — Componente Modal de Resolución Manual y Ajuste Contable

**Módulo:** `web-ui/`  
**Porcentaje de Avance:** 60% -> 65%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Permite al auditor resolver manualmente discrepancias persistentes (65%), registrando la nota de justificación y la firma de auditoría.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Patrón Modal React y Bloqueo de Foco (Focus Trap):** Creación de ventanas superpuestas accesibles con cierre mediante tecla ESC y fondo de oscurecimiento.
* **Registro de Justificaciones de Auditoría:** Captura obligatoria de notas de texto justificativas para mantener la trazabilidad contable legal.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/components/discrepancies/ResolutionModal.jsx`
1. Diseña el modal con el detalle completo de la partida descuadrada.
2. Agrega el selector de tipo de acción: 'Aceptar Diferencia Mínima', 'Crear Nota Débito/Crédito', 'Vincular a Múltiples Registros'.
3. Requiere la entrada de texto `#audit-note` y envía la resolución a la API REST.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
