- [x] TASK_FE_003 — Cliente API REST Axios, Interceptores JWT y Manejo de Errores 📅 2026-08-05 09:00
	- [x] Paso 1: Crear el archivo src/services/api.js
		- [x] Instanciar cliente Axios con baseURL '/api/v1' y timeout de 30 segundos
		- [x] Configurar interceptor de solicitud inyectando la cabecera Authorization: Bearer <jwt>
	- [x] Paso 2: Configurar interceptor de respuesta HTTP
		- [x] Capturar errores 401 Unauthorized provocando redirección a login
		- [x] Capturar errores 500 y formatear mensajes de respuesta

# TASK_FE_003 — Cliente API REST Axios, Interceptores JWT y Manejo de Errores

**Módulo:** `web-ui/`  
**Porcentaje de Avance:** 8% -> 12%  
**Estado:** COMPLETADO  
**Prioridad:** ALTA  
**Depende de:** Tareas previas de la secuencia  

---

## 1. Propósito y Justificación Técnica

Encapsula todas las comunicaciones HTTP con el backend Spring Boot (12%). Garantiza el envío del token de sesión JWT y procesa de forma centralizada los errores de red o servidor.

---

## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave

Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:

* **Cliente HTTP Axios e Interceptores:** Uso de axios.create(), interceptors.request y interceptors.response para mutar peticiones y capturar errores globalmente.
* **Manejo de Errores de Red y Códigos de Estado HTTP:** Tratamiento diferenciado para respuestas 401 (Sesión vencida), 403 (Sin permisos) y 500 (Fallo del motor de conciliación).

---

## 3. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `src/services/api.js`
1. Instala o verifica `axios` en las dependencias.
2. Crea una instancia `const api = axios.create({ baseURL: '/api/v1', timeout: 30000 })`.
3. Registra `api.interceptors.request.use` para leer el token del almacén Zustand/localStorage e inyectar `'Authorization': 'Bearer ' + token`.

### Paso 2: Configurar interceptores de respuesta
1. Registra `api.interceptors.response.use` para retornar `response.data` directamente.
2. En la función de rechazo, evalúa si `error.response.status === 401`: borra el token y redirige a `/login`.
3. Exporta la instancia `api` por defecto.

---

## 4. Criterios de Aceptación y Verificación

| # | Criterio de Aceptación | Método de Verificación |
|---|---|---|
| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |
| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |
