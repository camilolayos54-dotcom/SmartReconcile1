- [x] TASK_FE_004 — Tienda de Estado Global Zustand para Autenticación y Workspace 📅 2026-08-05 09:30
	- [x] Paso 1: Crear el archivo src/store/useAuthStore.js
		- [x] Definir el estado global: user, token, activeWorkspace, isAuthenticated
		- [x] Implementar acciones: loginSuccess(user, token), logout(), setActiveWorkspace(workspace)
	- [x] Paso 2: Configurar persistencia de estado
		- [x] Utilizar el middleware persist de Zustand para almacenar en localStorage

# TASK_FE_004 — Tienda de Estado Global Zustand para Autenticación y Workspace

**Módulo:** `web-ui/`  
**Porcentaje de Avance:** 12% -> 16%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Gestiona el estado global de la aplicación (16%) mediante Zustand. Almacena la sesión del auditor, el workspace contable activo y persiste los datos en localStorage.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Gestión de Estado Ligero con Zustand:** Creación de tiendas (stores) reactivas con create(), selectores de estado y mutadores sin la complejidad Boilerplate de Redux.
* **Middleware de Persistencia de Estado:** Uso de persist() para sincronizar el estado reactivo con el almacenamiento localStorage.

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/store/useAuthStore.js`
1. Importa `create` de `'zustand'` y `persist` de `'zustand/middleware'`.
2. Define la tienda `useAuthStore` conteniendo los atributos `user`, `token`, `activeWorkspace` e `isAuthenticated`.

### Paso 2: Implementar acciones reductoras
1. Agrega la acción `loginSuccess(userData, token)` que actualice el estado y marque `isAuthenticated: true`.
2. Agrega la acción `logout()` que reinicie el estado a nulo.
3. Agrega la acción `setActiveWorkspace(workspace)` para conmutar la empresa/organización en conciliación.
4. Envuelve la tienda con `persist(..., { name: 'smart_reconcile_auth' })`.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
