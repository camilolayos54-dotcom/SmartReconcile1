# TASK FE-002 — Shell de Navegación Autenticado (`AppShell.jsx`, `HeaderNavbar.jsx`, `Sidebar.jsx`)

**Módulo:** `web-ui/src/components/layout/`  
**Tipo de Archivo:** Componentes de Disposición React  
**Prioridad:** ALTA — Marco de navegación de la aplicación autenticada.  
**Depende de:** `TASK_FE_001`  
**Bloquea:** Todas las vistas autenticadas de SmartReconcile  

---

## 1. Propósito y Justificación Técnica

Construye la estructura contenedora de la aplicación. `HeaderNavbar.jsx` incluye el selector global de moneda base (`USD`, `EUR`, `COP`, `MXN`), el selector de tenant u organización activa, e indicador del estado de la conexión WebSocket. `Sidebar.jsx` proporciona acceso directo a los módulos operacionales (Dashboard, Discrepancias, Ingesta, Plantillas, Auditoría).

---

## 2. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear `HeaderNavbar.jsx`
1. Renderiza la barra superior fija con el logotipo de `SmartReconcile` y acento amarillo `#FFD200`.
2. Implementa selector `<select>` para la moneda base (`USD`, `EUR`, `COP`, `MXN`) sincronizado con el store Zustand `useCurrencyStore`.
3. Implementa badge dinámico de estado WebSocket (`Conectado` / `Reconectando`).

### Paso 2: Crear `Sidebar.jsx`
1. Define enlaces de navegación con iconos de `lucide-react`:
   * Dashboard (`/dashboard`) -> Icono `LayoutDashboard`
   * Discrepancias (`/discrepancies`) -> Icono `AlertTriangle`
   * Ingesta (`/ingestion`) -> Icono `UploadCloud`
   * Plantillas (`/templates`) -> Icono `FileCode`
   * Auditoría (`/audit-logs`) -> Icono `ShieldCheck`

### Paso 3: Crear `AppShell.jsx`
1. Conecta `HeaderNavbar` y `Sidebar` alrededor del contenedor principal de rutas `<Outlet />`.

---

## 3. Post-Condiciones y Criterios de Tarea Completada con Éxito (Acceptance Criteria)

| # | Condición que Debe Cumplirse | Consecuencia / Riesgo si Falla |
|---|---|---|
| 1 | Cambio de moneda en HeaderNavbar actualiza el store global Zustand | Monedas desalineadas en las vistas de métricas |
| 2 | Enlaces del Sidebar marcan correctamente la ruta activa actual | Inconsistencia en la navegación del usuario |
| 3 | Layout responsive soporta ocultar Sidebar en pantallas angostas | Desbordamiento visual |

---

## 4. Comando de Verificación

```bash
npm run build
```
