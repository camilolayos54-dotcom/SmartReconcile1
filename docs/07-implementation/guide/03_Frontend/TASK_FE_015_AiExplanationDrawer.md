- [ ] TASK_FE_015 — Componente Drawer de Explicación IA y Razonamiento Explicable 📅 2026-08-05 15:00
	- [ ] Paso 1: Crear src/components/ai/AiExplanationDrawer.jsx
		- [ ] Diseñar panel lateral desplegable (Drawer) para mostrar el análisis del coprocesador IA
		- [ ] Renderizar el texto en lenguaje natural generado por el modelo explicador contable
	- [ ] Paso 2: Conectar con la API gRPC/REST de IA
		- [ ] Consultar GET /api/v1/ai/explain/{discrepancyId}

# TASK_FE_015 — Componente Drawer de Explicación IA y Razonamiento Explicable

**Módulo:** `web-ui/`  
**Porcentaje de Avance:** 65% -> 70%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Muestra la explicación generada por la IA (70%) en lenguaje claro sobre el motivo del descuadre contable y las recomendaciones de solución.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Paneles Laterales Desplegables (Drawers UI):** Transición de paneles que se deslizan desde el borde derecho sin destruir el contexto de la pantalla principal.
* **Formateo de Respuestas de Inteligencia Artificial Explicable (XAI):** Estructuración de textos de análisis de causalidad contable presentados con claridad pedagógica.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/components/ai/AiExplanationDrawer.jsx`
1. Diseña el panel deslicable desde la derecha con la cabecera 'Análisis del Coprocesador IA'.
2. Consume el endpoint de explicación IA para la discrepancia seleccionada.
3. Inyecta la narrativa explicativa, las variables consideradas por el modelo y el nivel de confianza porcentual.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
