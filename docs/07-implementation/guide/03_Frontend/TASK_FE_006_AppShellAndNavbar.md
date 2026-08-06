- [x] TASK_FE_006 — App Shell, Sidebar Navegacional y Layout Principal 📅 2026-08-05 10:30
	- [x] Paso 1: Crear src/components/layout/AppShell.jsx y Sidebar.jsx
		- [x] Diseñar layout de panel administrativo con barra lateral fija y cabecera superior
		- [x] Incluir enlaces a Dashboard, Ingestión, Discrepancias, Plantillas, Auditoría y Configuración
		- [x] Mostrar selector de Workspace activo e información del usuario logueado
	- [x] Paso 2: Implementar navegación reactiva
		- [x] Resaltar el enlace activo según la ruta actual de la aplicación

# TASK_FE_006 — App Shell, Sidebar Navegacional y Layout Principal

**Módulo:** `web-ui/`  
**Porcentaje de Avance:** 20% -> 25%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Construye la estructura contenedora principal de la aplicación web (25%). Proporciona la barra lateral de navegación (Sidebar), selector de empresa y cabecera de sesión.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Patrón App Shell para Aplicaciones Web Complejas:** Diseño de la estructura visual fija (Sidebar + Header + Content Container) donde el área de contenido cambia según la vista seleccionada.
* **Iconografía SVG React (Lucide-React / Heroicons):** Integración de componentes de íconos vectoriales para representar cada módulo navegacional.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/components/layout/Sidebar.jsx`
1. Diseña la barra lateral con el logotipo de SmartReconcile.
2. Genera los enlaces navegacionales: `Dashboard`, `Ingestión de Datos`, `Discrepancias`, `Plantillas de Reglas`, `Logs de Auditoría`, `Configuración`.
3. Agrega la sección inferior con el selector de Workspace contable activo.

### Paso 2: Crear `src/components/layout/AppShell.jsx`
1. Une el `Sidebar`, la cabecera superior `Header` (con avatar de usuario y notificación de estado del coprocesador IA) y el contenedor principal `<main>` donde se inyecta la vista actual.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
