- [x] TASK_FE_002 — Sistema de Diseño Financiero CSS y Tokens Dark Mode HSL 📅 2026-08-05 08:30
	- [x] Paso 1: Configurar tailwind.config.js con paleta de colores HSL financiera
		- [x] Declarar colores de superficie oscura (slate/zinc), azul primario corporativo, verde éxito de conciliación y rojo discrepancia
	- [x] Paso 2: Configurar src/index.css con directivas Tailwind y Reset
		- [x] Importar @tailwind base, components, utilities
		- [x] Configurar tipografía Inter y scrollbars personalizadas para tablas masivas

# TASK_FE_002 — Sistema de Diseño Financiero CSS y Tokens Dark Mode HSL

**Módulo:** `web-ui/`  
**Porcentaje de Avance:** 4% -> 8%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Define el sistema de diseño visual financiero (8%). Configura los tokens HSL en Tailwind CSS para el modo oscuro corporativo (Dark Mode), optimizando la lectura de tablas de discrepancias con miles de filas.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Configuración Avanzada de Tailwind CSS:** Uso de tailwind.config.js para extender la paleta de colores con variables HSL, fuentes y sombras personalizadas.
* **Diseño de Interfaces Financieras Dark Mode:** Elección de contrastes HSL óptimos para mitigar la fatiga visual en jornadas extensas de auditoría contable.
* **Personalización de Barras de Scroll (Custom Scrollbars):** Estilización de ::-webkit-scrollbar para tablas con scroll horizontal y vertical intenso.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Configurar `tailwind.config.js`
1. Abre `tailwind.config.js` y extiende la propiedad `theme.extend.colors`.
2. Define la paleta cromática: `brand`: azul corporativo (`hsl(217, 91%, 60%)`), `surface`: fondo oscuro (`hsl(222, 47%, 11%)`), `surface-card`: (`hsl(217, 33%, 17%)`), `success`: verde coincidencia (`hsl(142, 71%, 45%)`), `danger`: rojo discrepancia (`hsl(0, 84%, 60%)`), `warning`: amarillo pendiente (`hsl(38, 92%, 50%)`).

### Paso 2: Configurar `src/index.css`
1. Agrega las directivas `@tailwind base;`, `@tailwind components;`, `@tailwind utilities;`.
2. Define estilos globales para body con tipografía 'Inter' y color de fondo `--surface`.
3. Aplica reglas para barras de desplazamiento delgadas en tablas masivas.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
