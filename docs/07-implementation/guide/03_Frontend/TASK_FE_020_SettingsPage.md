- [ ] TASK_FE_020 — Vista de Configuración del Workspace y Miembros de Equipo 📅 2026-08-05 17:30
	- [ ] Paso 1: Crear el archivo src/pages/SettingsPage.jsx
		- [ ] Diseñar panel de administración del equipo contable y gestión de permisos por rol
		- [ ] Implementar invitación de nuevos auditores vía correo electrónico
	- [ ] Paso 2: Gestión de datos de la empresa
		- [ ] Permitir actualizar el NIT, Razón Social y Moneda Funcional del Workspace

# TASK_FE_020 — Vista de Configuración del Workspace y Miembros de Equipo

**Módulo:** `web-ui/`  
**Porcentaje de Avance:** 88% -> 92%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Administra el entorno de trabajo colaborativo (92%), permitiendo invitar auditores, asignar permisos y configurar la moneda base de la organización.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Gestión de Equipos y Miembros en SaaS B2B:** Interfaz para invitar, cambiar roles y revocar accesos a miembros del equipo contable.
* **Configuración Multi-Moneda Base:** Selección de la moneda principal de presentación de informes de conciliación.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/pages/SettingsPage.jsx`
1. Diseña la pestaña de datos generales del Workspace (Nombre, NIT, Moneda principal COP/USD/EUR).
2. Diseña la tabla de miembros de equipo con sus roles (Administrador, Auditor Senior, Auditor Junior, Solo Lectura).
3. Implementa el modal para enviar invitaciones por correo electrónico.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
