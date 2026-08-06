- [ ] TASK_FE_021 — Vista de Perfil de Usuario y Claves API de Seguridad 📅 2026-08-05 18:00
	- [ ] Paso 1: Crear el archivo src/pages/ProfilePage.jsx
		- [ ] Diseñar vista de datos personales del auditor y actualización de contraseña
		- [ ] Diseñar sección de generación de Claves API (API Keys) para integraciones externas
	- [ ] Paso 2: Conectar con la API de Seguridad
		- [ ] Implementar cambio seguro de contraseña

# TASK_FE_021 — Vista de Perfil de Usuario y Claves API de Seguridad

**Módulo:** `web-ui/`  
**Porcentaje de Avance:** 92% -> 95%  
**Estado:** PENDIENTE  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Permite al usuario gestionar su perfil (95%), cambiar su clave de acceso y administrar tokens API para integraciones con ERPs contables externos.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Gestión de Claves de Seguridad API Keys:** Generación, revelado de una sola vez y revocación de credenciales secretas de integración.
* **Validación de Cambio de Contraseña Segura:** Confirmación de clave actual y validación de nueva clave en cliente antes de enviar.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/pages/ProfilePage.jsx`
1. Maqueta el formulario de actualización de datos de perfil.
2. Implementa la sección de seguridad con la tabla de API Keys generadas para conectores de ERPs.
3. Agrega la funcionalidad para revocar claves comprometidas.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
