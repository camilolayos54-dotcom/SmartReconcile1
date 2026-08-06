# TASK FE-001 — Vite React & Tailwind Setup (`tailwind.config.js`)

**Módulo:** `web-ui/`  
**Tipo de Archivo:** Configuración de Proyecto Vite React 18 & Tailwind CSS  
**Prioridad:** CRÍTICA — Configura los tokens de diseño corporativo y la base del SPA.  
**Depende de:** Node.js 18+  
**Bloquea:** Todos los componentes y vistas React  

---

## 1. Propósito y Justificación Técnica

Inicializa la aplicación Single Page Application (SPA) `web-ui` con Vite 5.x, React 18, y Tailwind CSS. Registra la paleta cromática corporativa (Navy `#0B192C`, Yellow `#FFD200`, Crimson `#E11D48`), las fuentes `Inter` y `JetBrains Mono` y las utilidades del sistema.

---

## 2. Instrucciones de Implementación Paso a Paso

### Paso 1: Crear el proyecto Vite React
1. En la raíz de `SmartReconcile`, navega a `web-ui/`.
2. Ejecuta: `npx create-vite@latest . --template react`.
3. Instala dependencias base y de desarrollo:
   `npm install lucide-react zustand axios clsx tailwind-merge`
   `npm install -D tailwindcss postcss autoprefixer`

### Paso 2: Configurar Tailwind CSS y Tokens
1. Inicializa Tailwind: `npx tailwindcss init -p`.
2. En `tailwind.config.js`, extiende la paleta de colores:
   ```javascript
   module.exports = {
     content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
     theme: {
       extend: {
         colors: {
           brand: {
             navy: "#0B192C",
             navyLight: "#1E3E62",
             yellow: "#FFD200",
             crimson: "#E11D48",
             surface: "#080F19",
             card: "#0F1C2E",
             border: "#1E293B"
           }
         },
         fontFamily: {
           sans: ['Inter', 'sans-serif'],
           mono: ['JetBrains Mono', 'monospace']
         }
       }
     },
     plugins: []
   };
   ```

---

## 3. Post-Condiciones y Criterios de Tarea Completada con Éxito (Acceptance Criteria)

| # | Condición que Debe Cumplirse | Consecuencia / Riesgo si Falla |
|---|---|---|
| 1 | Tokens `brand.navy`, `brand.yellow`, `brand.crimson` disponibles en clases Tailwind | Fallos en el renderizado de estilos |
| 2 | Compilación `npm run build` sin errores en carpeta `dist` | Empaquetado roto |

---

## 4. Comando de Verificación

```bash
npm run build
```
