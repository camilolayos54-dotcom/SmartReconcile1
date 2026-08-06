- [x] TASK_FE_008 — Vista de Autenticación de Usuario y MFA 📅 2026-08-05 11:30
	- [x] Paso 1: Crear el archivo src/pages/LoginPage.jsx
		- [x] Diseñar el formulario de ingreso con campos para Email y Password
		- [x] Conectar el formulario con la API POST /api/v1/auth/login
		- [x] Almacenar la respuesta en useAuthStore y redirigir al Dashboard
	- [x] Paso 2: Manejo de errores de credenciales
		- [x] Mostrar alertas Toast en caso de contraseña incorrecta o cuenta bloqueada

# TASK_FE_008 — Vista de Autenticación de Usuario y MFA

**Módulo:** `web-ui/`  
**Porcentaje de Avance:** 30% -> 35%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Autentica a auditores y contadores (35%), enviando credenciales al backend Spring Boot y guardando el token JWT en el almacén de sesión.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Formularios Controlados en React (Controlled Components):** Gestión del estado de los inputs mediante useState y eventos onChange.
* **Manejo de Sesión Segura:** Integración con la tienda Zustand para actualizar el estado global de autenticación e iniciar la experiencia del dashboard.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/pages/LoginPage.jsx`
1. Diseña la tarjeta de inicio de sesión centradora sobre fondo de superficie oscura.
2. Define los estados React `email` y `password`.
3. Escribe la función `handleSubmit` enviando la petición `api.post('/auth/login', { email, password })`.
4. Al recibir la respuesta exitosa, invoca `loginSuccess(response.user, response.token)` de `useAuthStore` y navega hacia `/dashboard`.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
