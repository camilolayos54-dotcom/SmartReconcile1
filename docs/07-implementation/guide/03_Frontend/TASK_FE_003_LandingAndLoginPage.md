# TASK FE-003 — Landing Pública & Login Split-Screen (`LandingPage.jsx` & `LoginPage.jsx`)

**Módulo:** `web-ui/src/pages/`  
**Tipo de Archivo:** Componentes de Página React  
**Prioridad:** ALTA — Embudo público de captación y autenticación B2B.  
**Depende de:** `TASK_FE_001`  
**Bloquea:** Acceso inicial de usuarios  

---

## 1. Propósito y Justificación Técnica

`LandingPage.jsx` es la portada pública de SmartReconcile, incluyendo un widget interactivo de cálculo de ROI (ahorro estimado al automatizar la conciliación de extractos). `LoginPage.jsx` es la pantalla de acceso split-screen 50/50 donde el analista/gerente se autentica recibiendo cookies HttpOnly y token CSRF.

---

## 2. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `LandingPage.jsx`
1. Maqueta sección hero con titular "Reconciliación bancaria automatizada con inteligencia artificial".
2. Implementa calculadora interactiva con slider de volumen mensual de transacciones ($10k a $10M) mostrando el cálculo de ahorro en tiempo e inconsistencias financieras.

### Paso 2: Crear `LoginPage.jsx`
1. Estructura contenedor 50/50: lado izquierdo banner con paleta `brand.navy`, lado derecho formulario de inicio de sesión con validación.
2. Invocación a `POST /api/v1/auth/login`.

---

## 3. Post-Condiciones y Criterios de Tarea Completada con Éxito (Acceptance Criteria)

| # | Condición que Debe Cumplirse | Consecuencia / Riesgo si Falla |
|---|---|---|
| 1 | Calculadora de ROI en la landing recalcula dinámicamente según el slider | Widget estático sin interactividad |
| 2 | Inicio de sesión exitoso guarda sesión y redirige a `/dashboard` | Fallo de autenticación en cliente |

---

## 4. Comando de Verificación

```bash
npm run build
```
