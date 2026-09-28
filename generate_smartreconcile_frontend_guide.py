import os
import shutil

docs_frontend_dir = r"c:\PROGRAMMING\PROJECTS\SmartReconcile\docs\07-implementation\guide\03_Frontend"
guide_frontend_dir = r"c:\PROGRAMMING\PROJECTS\SmartReconcile\guide\03_Frontend"

# Ensure directories exist
for d in [docs_frontend_dir, guide_frontend_dir]:
    if not os.path.exists(d):
        os.makedirs(d)

tasks = [
    {
        "id": "TASK_FE_001",
        "file": "TASK_FE_001_ViteTailwindSetup.md",
        "title": "Inicialización del Proyecto Web React 18, Vite y Tailwind CSS",
        "status": "[x]",
        "prog": "0% -> 4%",
        "date": "2026-08-05 08:00",
        "p1": "Navegar al directorio web-ui/ y verificar la instalación de dependencias",
        "p1_subs": ["Verificar la presencia de react, react-dom, vite y tailwindcss en package.json"],
        "p2": "Configurar la estructura física de directorios en src/",
        "p2_subs": ["Crear src/components/ (ui, layout, dashboard, ingestion, discrepancies, templates, audit, ai)", "Crear src/pages/, src/services/, src/store/ y src/utils/"],
        "p3": "Verificar scripts de ejecución e inicialización de servidor Vite",
        "p3_subs": ["Ejecutar npm install", "Probar npm run dev en servidor local"],
        "purpose": "Establece la base física del cliente web transaccional (0%). Estructura el directorio web-ui/ en carpetas modulares dividiendo componentes de interfaz, páginas, tiendas de estado Zustand y servicios REST.",
        "prereqs": [
            ("Arquitectura de Aplicación React 18 (SPA)", "Comprensión del ciclo de vida de componentes funcionales, renderizado declarativo y Hooks de React (useState, useEffect, useMemo, useCallback)."),
            ("Empaquetador Vite 5.x para JSX", "Funcionamiento de la transformación de archivos .jsx a módulos JS nativos y configuración del servidor HMR (Hot Module Replacement)."),
            ("Estructuración de Proyectos Frontend Financieros", "Organización de capas de presentación para dashboards de conciliación con alto volumen de datos y estados complejos.")
        ],
        "steps": [
            ("Ingresar a la carpeta web-ui/ y verificar dependencias", [
                "Dirígete al directorio `web-ui/` en la raíz del repositorio de SmartReconcile.",
                "Verifica que `package.json` contenga las dependencias `react`, `react-dom`, `vite` y `@vitejs/plugin-react`."
            ]),
            ("Crear la estructura modular de carpetas en `src/`", [
                "Crea la carpeta `src/components/` dividida en subcarpetas `ui/`, `layout/`, `dashboard/`, `ingest/`, `discrepancies/`, `templates/`, `audit/` y `ai/`.",
                "Crea `src/pages/` para las vistas de la aplicación.",
                "Crea `src/services/` para el cliente HTTP API.",
                "Crea `src/store/` para las tiendas de estado global Zustand."
            ]),
            ("Inicialización y prueba de servidor", [
                "Ejecuta `npm install` para resolver el árbol de módulos.",
                "Verifica que `npm run dev` inicie el servidor de desarrollo sin advertencias."
            ])
        ]
    },
    {
        "id": "TASK_FE_002",
        "file": "TASK_FE_002_DesignSystemTokens.md",
        "title": "Sistema de Diseño Financiero CSS y Tokens Dark Mode HSL",
        "status": "[x]",
        "prog": "4% -> 8%",
        "date": "2026-08-05 08:30",
        "p1": "Configurar tailwind.config.js con paleta de colores HSL financiera",
        "p1_subs": ["Declarar colores de superficie oscura (slate/zinc), azul primario corporativo, verde éxito de conciliación y rojo discrepancia"],
        "p2": "Configurar src/index.css con directivas Tailwind y Reset",
        "p2_subs": ["Importar @tailwind base, components, utilities", "Configurar tipografía Inter y scrollbars personalizadas para tablas masivas"],
        "purpose": "Define el sistema de diseño visual financiero (8%). Configura los tokens HSL en Tailwind CSS para el modo oscuro corporativo (Dark Mode), optimizando la lectura de tablas de discrepancias con miles de filas.",
        "prereqs": [
            ("Configuración Avanzada de Tailwind CSS", "Uso de tailwind.config.js para extender la paleta de colores con variables HSL, fuentes y sombras personalizadas."),
            ("Diseño de Interfaces Financieras Dark Mode", "Elección de contrastes HSL óptimos para mitigar la fatiga visual en jornadas extensas de auditoría contable."),
            ("Personalización de Barras de Scroll (Custom Scrollbars)", "Estilización de ::-webkit-scrollbar para tablas con scroll horizontal y vertical intenso.")
        ],
        "steps": [
            ("Configurar `tailwind.config.js`", [
                "Abre `tailwind.config.js` y extiende la propiedad `theme.extend.colors`.",
                "Define la paleta cromática: `brand`: azul corporativo (`hsl(217, 91%, 60%)`), `surface`: fondo oscuro (`hsl(222, 47%, 11%)`), `surface-card`: (`hsl(217, 33%, 17%)`), `success`: verde coincidencia (`hsl(142, 71%, 45%)`), `danger`: rojo discrepancia (`hsl(0, 84%, 60%)`), `warning`: amarillo pendiente (`hsl(38, 92%, 50%)`)."
            ]),
            ("Configurar `src/index.css`", [
                "Agrega las directivas `@tailwind base;`, `@tailwind components;`, `@tailwind utilities;`.",
                "Define estilos globales para body con tipografía 'Inter' y color de fondo `--surface`.",
                "Aplica reglas para barras de desplazamiento delgadas en tablas masivas."
            ])
        ]
    },
    {
        "id": "TASK_FE_003",
        "file": "TASK_FE_003_HttpApiService.md",
        "title": "Cliente API REST Axios, Interceptores JWT y Manejo de Errores",
        "status": "[x]",
        "prog": "8% -> 12%",
        "date": "2026-08-05 09:00",
        "p1": "Crear el archivo src/services/api.js",
        "p1_subs": ["Instanciar cliente Axios con baseURL '/api/v1' y timeout de 30 segundos", "Configurar interceptor de solicitud inyectando la cabecera Authorization: Bearer <jwt>"],
        "p2": "Configurar interceptor de respuesta HTTP",
        "p2_subs": ["Capturar errores 401 Unauthorized provocando redirección a login", "Capturar errores 500 y formatear mensajes de respuesta"],
        "purpose": "Encapsula todas las comunicaciones HTTP con el backend Spring Boot (12%). Garantiza el envío del token de sesión JWT y procesa de forma centralizada los errores de red o servidor.",
        "prereqs": [
            ("Cliente HTTP Axios e Interceptores", "Uso de axios.create(), interceptors.request y interceptors.response para mutar peticiones y capturar errores globalmente."),
            ("Manejo de Errores de Red y Códigos de Estado HTTP", "Tratamiento diferenciado para respuestas 401 (Sesión vencida), 403 (Sin permisos) y 500 (Fallo del motor de conciliación).")
        ],
        "steps": [
            ("Crear `src/services/api.js`", [
                "Instala o verifica `axios` en las dependencias.",
                "Crea una instancia `const api = axios.create({ baseURL: '/api/v1', timeout: 30000 })`.",
                "Registra `api.interceptors.request.use` para leer el token del almacén Zustand/localStorage e inyectar `'Authorization': 'Bearer ' + token`."
            ]),
            ("Configurar interceptores de respuesta", [
                "Registra `api.interceptors.response.use` para retornar `response.data` directamente.",
                "En la función de rechazo, evalúa si `error.response.status === 401`: borra el token y redirige a `/login`.",
                "Exporta la instancia `api` por defecto."
            ])
        ]
    },
    {
        "id": "TASK_FE_004",
        "file": "TASK_FE_004_ZustandAuthStore.md",
        "title": "Tienda de Estado Global Zustand para Autenticación y Workspace",
        "status": "[x]",
        "prog": "12% -> 16%",
        "date": "2026-08-05 09:30",
        "p1": "Crear el archivo src/store/useAuthStore.js",
        "p1_subs": ["Definir el estado global: user, token, activeWorkspace, isAuthenticated", "Implementar acciones: loginSuccess(user, token), logout(), setActiveWorkspace(workspace)"],
        "p2": "Configurar persistencia de estado",
        "p2_subs": ["Utilizar el middleware persist de Zustand para almacenar en localStorage"],
        "purpose": "Gestiona el estado global de la aplicación (16%) mediante Zustand. Almacena la sesión del auditor, el workspace contable activo y persiste los datos en localStorage.",
        "prereqs": [
            ("Gestión de Estado Ligero con Zustand", "Creación de tiendas (stores) reactivas con create(), selectores de estado y mutadores sin la complejidad Boilerplate de Redux."),
            ("Middleware de Persistencia de Estado", "Uso de persist() para sincronizar el estado reactivo con el almacenamiento localStorage.")
        ],
        "steps": [
            ("Crear `src/store/useAuthStore.js`", [
                "Importa `create` de `'zustand'` y `persist` de `'zustand/middleware'`.",
                "Define la tienda `useAuthStore` conteniendo los atributos `user`, `token`, `activeWorkspace` e `isAuthenticated`."
            ]),
            ("Implementar acciones reductoras", [
                "Agrega la acción `loginSuccess(userData, token)` que actualice el estado y marque `isAuthenticated: true`.",
                "Agrega la acción `logout()` que reinicie el estado a nulo.",
                "Agrega la acción `setActiveWorkspace(workspace)` para conmutar la empresa/organización en conciliación.",
                "Envuelve la tienda con `persist(..., { name: 'smart_reconcile_auth' })`."
            ])
        ]
    },
    {
        "id": "TASK_FE_005",
        "file": "TASK_FE_005_ToastNotificationUi.md",
        "title": "Componente Sistema de Notificaciones Toast y Error Boundary",
        "status": "[x]",
        "prog": "16% -> 20%",
        "date": "2026-08-05 10:00",
        "p1": "Crear src/components/ui/Toast.jsx y src/store/useToastStore.js",
        "p1_subs": ["Crear tienda Zustand useToastStore gestionando la lista de notificaciones activas", "Crear componente Toast.jsx renderizando alertas flotantes con animaciones Tailwind"],
        "p2": "Crear ErrorBoundary para captura de fallos de renderizado React",
        "p2_subs": ["Implementar ErrorBoundary.jsx para prevenir pantallas blancas ante excepciones en componentes"],
        "purpose": "Proporciona retroalimentación visual inmediata (20%) sobre el procesamiento de archivos de conciliación, errores de red y alertas del sistema.",
        "prereqs": [
            ("Límite de Errores en React (Error Boundaries)", "Componente de clase React utilizando getDerivedStateFromError y componentDidCatch para contener fallos de renderizado."),
            ("Animaciones CSS con Tailwind y React State", "Gestión de entrada/salida de listas emergentes con renderizado condicional y temporizadores.")
        ],
        "steps": [
            ("Crear `src/store/useToastStore.js`", [
                "Crea la tienda Zustand registrando el array `toasts` y las acciones `addToast(msg, type)` y `removeToast(id)`."
            ]),
            ("Crear `src/components/ui/Toast.jsx`", [
                "Crea el componente contenedor renderizado en una posición fija `bottom-5 right-5 z-50`.",
                "Mapea el array `toasts` renderizando tarjetas con colores según el tipo: `success` (verde), `error` (rojo), `info` (azul)."
            ]),
            ("Crear `src/components/ui/ErrorBoundary.jsx`", [
                "Implementa el componente ErrorBoundary de React para capturar excepciones no controladas en el árbol visual."
            ])
        ]
    },
    {
        "id": "TASK_FE_006",
        "file": "TASK_FE_006_AppShellAndNavbar.md",
        "title": "App Shell, Sidebar Navegacional y Layout Principal",
        "status": "[x]",
        "prog": "20% -> 25%",
        "date": "2026-08-05 10:30",
        "p1": "Crear src/components/layout/AppShell.jsx y Sidebar.jsx",
        "p1_subs": ["Diseñar layout de panel administrativo con barra lateral fija y cabecera superior", "Incluir enlaces a Dashboard, Ingestión, Discrepancias, Plantillas, Auditoría y Configuración", "Mostrar selector de Workspace activo e información del usuario logueado"],
        "p2": "Implementar navegación reactiva",
        "p2_subs": ["Resaltar el enlace activo según la ruta actual de la aplicación"],
        "purpose": "Construye la estructura contenedora principal de la aplicación web (25%). Proporciona la barra lateral de navegación (Sidebar), selector de empresa y cabecera de sesión.",
        "prereqs": [
            ("Patrón App Shell para Aplicaciones Web Complejas", "Diseño de la estructura visual fija (Sidebar + Header + Content Container) donde el área de contenido cambia según la vista seleccionada."),
            ("Iconografía SVG React (Lucide-React / Heroicons)", "Integración de componentes de íconos vectoriales para representar cada módulo navegacional.")
        ],
        "steps": [
            ("Crear `src/components/layout/Sidebar.jsx`", [
                "Diseña la barra lateral con el logotipo de SmartReconcile.",
                "Genera los enlaces navegacionales: `Dashboard`, `Ingestión de Datos`, `Discrepancias`, `Plantillas de Reglas`, `Logs de Auditoría`, `Configuración`.",
                "Agrega la sección inferior con el selector de Workspace contable activo."
            ]),
            ("Crear `src/components/layout/AppShell.jsx`", [
                "Une el `Sidebar`, la cabecera superior `Header` (con avatar de usuario y notificación de estado del coprocesador IA) y el contenedor principal `<main>` donde se inyecta la vista actual."
            ])
        ]
    },
    {
        "id": "TASK_FE_007",
        "file": "TASK_FE_007_LandingPage.md",
        "title": "Página Institucional y Promocional de la Plataforma",
        "status": "[x]",
        "prog": "25% -> 30%",
        "date": "2026-08-05 11:00",
        "p1": "Crear el archivo src/pages/LandingPage.jsx",
        "p1_subs": ["Maquetar sección Hero con llamada a la acción 'Iniciar Prueba / Iniciar Sesión'", "Crear bloque de características: Conciliación Inteligente con IA, Procesamiento Masivo, Audit Trail 100%"],
        "p2": "Conectar botones de acceso",
        "p2_subs": ["Vincular botón de acceso al flujo de Login"],
        "purpose": "Presenta la propuesta de valor de SmartReconcile (30%) para potenciales clientes corporativos, destacando el motor de IA explicable y el ahorro de tiempo contable.",
        "prereqs": [
            ("Landing Pages de Conversión B2B", "Estructuración de secciones Hero, prueba social, matriz de funcionalidades y botones CTA principales."),
            ("Animaciones Fluidas de Scroll", "Uso de transiciones suaves para revelar los beneficios del producto.")
        ],
        "steps": [
            ("Crear `src/pages/LandingPage.jsx`", [
                "Maqueta la sección Hero con titular llamativo: 'Conciliación Financiera Automatizada con Explicabilidad por IA'.",
                "Crea la grilla de características principales: 'Motor Heurístico Multi-Criterio', 'Auditoría e Inmutabilidad Hash', 'Explicador IA en Lenguaje Natural'.",
                "Agrega la tabla comparativa de ahorro de horas hombre en procesos de cierre contable mensual."
            ])
        ]
    },
    {
        "id": "TASK_FE_008",
        "file": "TASK_FE_008_LoginPage.md",
        "title": "Vista de Autenticación de Usuario y MFA",
        "status": "[x]",
        "prog": "30% -> 35%",
        "date": "2026-08-05 11:30",
        "p1": "Crear el archivo src/pages/LoginPage.jsx",
        "p1_subs": ["Diseñar el formulario de ingreso con campos para Email y Password", "Conectar el formulario con la API POST /api/v1/auth/login", "Almacenar la respuesta en useAuthStore y redirigir al Dashboard"],
        "p2": "Manejo de errores de credenciales",
        "p2_subs": ["Mostrar alertas Toast en caso de contraseña incorrecta o cuenta bloqueada"],
        "purpose": "Autentica a auditores y contadores (35%), enviando credenciales al backend Spring Boot y guardando el token JWT en el almacén de sesión.",
        "prereqs": [
            ("Formularios Controlados en React (Controlled Components)", "Gestión del estado de los inputs mediante useState y eventos onChange."),
            ("Manejo de Sesión Segura", "Integración con la tienda Zustand para actualizar el estado global de autenticación e iniciar la experiencia del dashboard.")
        ],
        "steps": [
            ("Crear `src/pages/LoginPage.jsx`", [
                "Diseña la tarjeta de inicio de sesión centradora sobre fondo de superficie oscura.",
                "Define los estados React `email` y `password`.",
                "Escribe la función `handleSubmit` enviando la petición `api.post('/auth/login', { email, password })`.",
                "Al recibir la respuesta exitosa, invoca `loginSuccess(response.user, response.token)` de `useAuthStore` y navega hacia `/dashboard`."
            ])
        ]
    },
    {
        "id": "TASK_FE_009",
        "file": "TASK_FE_009_DashboardMetricsOverview.md",
        "title": "Vista Dashboard Ejecutivo de Métricas y KPIs de Conciliación",
        "status": "[x]",
        "prog": "35% -> 40%",
        "date": "2026-08-05 12:00",
        "p1": "Crear el archivo src/pages/DashboardPage.jsx",
        "p1_subs": ["Maquetar tarjetas KPI: Total Registros Procesados, Tasa de Coincidencia %, Discrepancias Pendientes, Monto Cuadrado"],
        "p2": "Consultar métricas al backend",
        "p2_subs": ["Invocar GET /api/v1/reconciliation/metrics usando el cliente API"],
        "purpose": "Proporciona el panel de control ejecutivo (40%), mostrando indicadores clave de rendimiento (KPIs) sobre los procesos de conciliación financiera activos.",
        "prereqs": [
            ("Diseño de Dashboards Financieros", "Disposición de métricas críticas en tarjetas de alto impacto visual con colores de estado (verde/rojo/amarillo)."),
            ("Formateo de Valores Financieros y Porcentajes", "Formateo de cifras de dinero de gran escala y porcentajes de precisión contable.")
        ],
        "steps": [
            ("Crear `src/pages/DashboardPage.jsx`", [
                "Diseña la grilla de 4 tarjetas KPI superiores: 'Registros Totales', 'Tasa de Conciliación', 'Discrepancias Abiertas', 'Monto No Cuadrado'.",
                "Agrega un hook `useEffect` consumiendo `GET '/reconciliation/metrics'` para poblar los valores dinámicamente.",
                "Agrega botones de acción rápida: 'Iniciar Nueva Ingestión', 'Resolver Discrepancias Pendientes'."
            ])
        ]
    },
    {
        "id": "TASK_FE_010",
        "file": "TASK_FE_010_ReconciliationCharts.md",
        "title": "Componente Gráficos Interactivos de Conciliación y Tendencias",
        "status": "[x]",
        "prog": "40% -> 45%",
        "date": "2026-08-05 12:30",
        "p1": "Crear src/components/dashboard/ReconciliationCharts.jsx",
        "p1_subs": ["Integrar gráficos de línea y barra para tendencias de discrepancias por fecha", "Integrar gráfico de dona para distribución de estados de conciliación"],
        "p2": "Conectar con el estado del Dashboard",
        "p2_subs": ["Alimentar los gráficos con los datos históricos recibidos de la API"],
        "purpose": "Visualiza la evolución temporal de las discrepancias contables (45%), ayudando a detectar anomalías o picos de descuadre en fechas específicas.",
        "prereqs": [
            ("Integración de Librerías de Gráficos (Chart.js / Recharts)", "Creación de componentes de gráficos de barras, líneas y dona adaptables al tema oscuro."),
            ("Transformación de Series Temporales de Datos", "Mapeo de respuestas JSON con fechas e importes hacia estructuras consumibles por la librería gráfica.")
        ],
        "steps": [
            ("Crear `src/components/dashboard/ReconciliationCharts.jsx`", [
                "Integra una librería gráfica compatible con React.",
                "Crea el gráfico de líneas 'Tendencia de Discrepancias (Últimos 30 Días)'.",
                "Crea el gráfico de dona 'Distribución por Regla de Coincidencia' (Exacta, Heurística, Pendiente, Ajustada Manualmente)."
            ])
        ]
    },
    {
        "id": "TASK_FE_011",
        "file": "TASK_FE_011_IngestionPage.md",
        "title": "Vista de Ingestión de Datos y Carga de Archivos Drag & Drop",
        "status": "[x]",
        "prog": "45% -> 50%",
        "date": "2026-08-05 13:00",
        "p1": "Crear el archivo src/pages/IngestionPage.jsx",
        "p1_subs": ["Diseñar zona de arrastrar y soltar archivos (Dropzone) para CSV y Excel", "Agregar selector del Origen A (Extracto Bancario) y Origen B (Libro Auxiliar Contable)"],
        "p2": "Implementar barra de progreso de subida",
        "p2_subs": ["Mostrar porcentaje de avance de la carga del archivo"],
        "purpose": "Permite a los auditores subir archivos masivos de extractos bancarios y libros contables (50%) para dar inicio al proceso de conciliación.",
        "prereqs": [
            ("API File HTML5 y Eventos Drag & Drop", "Captura de eventos dragover, dragleave y drop para recibir archivos en el navegador."),
            ("Carga de Archivos Multipart con Seguimiento de Progreso", "Uso de FormData y la opción onUploadProgress de Axios para notificar el progreso de transferencia.")
        ],
        "steps": [
            ("Crear `src/pages/IngestionPage.jsx`", [
                "Maqueta las dos zonas de carga: 'Archivo Origen A (Extracto Bancario)' y 'Archivo Origen B (Libro Auxiliar)'.",
                "Agrega los controladores de eventos Drag & Drop para capturar archivos `.csv`, `.xlsx` o `.txt`.",
                "Muestra la barra de progreso indicando la transferencia en curso."
            ])
        ]
    },
    {
        "id": "TASK_FE_012",
        "file": "TASK_FE_012_ColumnMappingWizard.md",
        "title": "Componente Wizard de Previsualización y Mapeo de Columnas",
        "status": "[ ]",
        "prog": "50% -> 55%",
        "date": "2026-08-05 13:30",
        "p1": "Crear src/components/ingest/ColumnMappingWizard.jsx",
        "p1_subs": ["Diseñar tabla de previsualización de las primeras 5 filas del archivo subido", "Crear selectores desplegables para mapear campos requeridos: Fecha, Referencia/NIT, Monto, Descripción"],
        "p2": "Enviar mapeo al backend",
        "p2_subs": ["Invocar POST /api/v1/ingestion/confirm-mapping para lanzar la conciliación"],
        "purpose": "Guía al usuario en el mapeo de estructuras heterogéneas de archivos (55%), asegurando que las columnas del CSV coincidan con el modelo contable.",
        "prereqs": [
            ("Mapeo Dinámico de Esquemas de Datos (Column Mapping UI)", "Asociación visual entre encabezados de archivos desconocidos y atributos del sistema."),
            ("Validación de Campos Contables Obligatorios", "Garantizar que se hayan asignado las columnas clave de Fecha, Monto e Identificador antes de procesar.")
        ],
        "steps": [
            ("Crear `src/components/ingest/ColumnMappingWizard.jsx`", [
                "Renderiza la tabla de muestra con las primeras filas leídas del archivo.",
                "Agrega controles `<select>` sobre cada columna para asignar la propiedad del sistema (`DATE`, `AMOUNT`, `REFERENCE`, `DESCRIPTION`).",
                "Valida la asignación completa y envía la confirmación de inicio de trabajo de conciliación al servidor."
            ])
        ]
    },
    {
        "id": "TASK_FE_013",
        "file": "TASK_FE_013_DiscrepanciesPage.md",
        "title": "Vista Explorador de Discrepancias y Tabla de Cuadrante",
        "status": "[x]",
        "prog": "55% -> 60%",
        "date": "2026-08-05 14:00",
        "p1": "Crear el archivo src/pages/DiscrepanciesPage.jsx",
        "p1_subs": ["Diseñar la tabla de discrepancias dividida en 2 paneles comparativos (Banco vs Contabilidad)", "Crear barra de filtros por nivel de severidad (Alta, Media, Baja) y estado de resolución"],
        "p2": "Conectar la tabla con la API REST",
        "p2_subs": ["Consultar GET /api/v1/discrepancies con paginación en servidor"],
        "purpose": "Interfaz principal de trabajo de auditoría (60%). Muestra las partidas no conciliadas o descuadradas lado a lado para su inspección y ajuste.",
        "prereqs": [
            ("Tablas Comparativas de Lado a Lado (Side-by-Side Tables)", "Visualización simultánea de dos registros discordantes resaltando las celdas con diferencias numéricas."),
            ("Filtrado y Paginación Servidor de Grandes Volúmenes", "Sincronización de parámetros de consulta con la API para navegar entre miles de discrepancias.")
        ],
        "steps": [
            ("Crear `src/pages/DiscrepanciesPage.jsx`", [
                "Diseña la tabla comparativa con columnas: ID Discrepancia, Fecha, Registro Banco, Registro Libro, Diferencia Moneda, Nivel Severidad, Acciones.",
                "Aplica clases CSS para colorear las celdas de diferencia según su magnitud.",
                "Agrega los botones de filtro por estado: 'Todas', 'Pendientes', 'Ajustadas Manualmente', 'Ignoradas'."
            ])
        ]
    },
    {
        "id": "TASK_FE_014",
        "file": "TASK_FE_014_ResolutionWorkbenchModal.md",
        "title": "Componente Modal de Resolución Manual y Ajuste Contable",
        "status": "[ ]",
        "prog": "60% -> 65%",
        "date": "2026-08-05 14:30",
        "p1": "Crear src/components/discrepancies/ResolutionModal.jsx",
        "p1_subs": ["Diseñar ventana modal para forzar conciliación manual o aplicar nota de ajuste", "Agregar campo para justificación obligatoria del auditor contable"],
        "p2": "Enviar resolución al servidor",
        "p2_subs": ["Invocar POST /api/v1/discrepancies/{id}/resolve enviando la nota de auditoría"],
        "purpose": "Permite al auditor resolver manualmente discrepancias persistentes (65%), registrando la nota de justificación y la firma de auditoría.",
        "prereqs": [
            ("Patrón Modal React y Bloqueo de Foco (Focus Trap)", "Creación de ventanas superpuestas accesibles con cierre mediante tecla ESC y fondo de oscurecimiento."),
            ("Registro de Justificaciones de Auditoría", "Captura obligatoria de notas de texto justificativas para mantener la trazabilidad contable legal.")
        ],
        "steps": [
            ("Crear `src/components/discrepancies/ResolutionModal.jsx`", [
                "Diseña el modal con el detalle completo de la partida descuadrada.",
                "Agrega el selector de tipo de acción: 'Aceptar Diferencia Mínima', 'Crear Nota Débito/Crédito', 'Vincular a Múltiples Registros'.",
                "Requiere la entrada de texto `#audit-note` y envía la resolución a la API REST."
            ])
        ]
    },
    {
        "id": "TASK_FE_015",
        "file": "TASK_FE_015_AiExplanationDrawer.md",
        "title": "Componente Drawer de Explicación IA y Razonamiento Explicable",
        "status": "[ ]",
        "prog": "65% -> 70%",
        "date": "2026-08-05 15:00",
        "p1": "Crear src/components/ai/AiExplanationDrawer.jsx",
        "p1_subs": ["Diseñar panel lateral desplegable (Drawer) para mostrar el análisis del coprocesador IA", "Renderizar el texto en lenguaje natural generado por el modelo explicador contable"],
        "p2": "Conectar con la API gRPC/REST de IA",
        "p2_subs": ["Consultar GET /api/v1/ai/explain/{discrepancyId}"],
        "purpose": "Muestra la explicación generada por la IA (70%) en lenguaje claro sobre el motivo del descuadre contable y las recomendaciones de solución.",
        "prereqs": [
            ("Paneles Laterales Desplegables (Drawers UI)", "Transición de paneles que se deslizan desde el borde derecho sin destruir el contexto de la pantalla principal."),
            ("Formateo de Respuestas de Inteligencia Artificial Explicable (XAI)", "Estructuración de textos de análisis de causalidad contable presentados con claridad pedagógica.")
        ],
        "steps": [
            ("Crear `src/components/ai/AiExplanationDrawer.jsx`", [
                "Diseña el panel deslicable desde la derecha con la cabecera 'Análisis del Coprocesador IA'.",
                "Consume el endpoint de explicación IA para la discrepancia seleccionada.",
                "Inyecta la narrativa explicativa, las variables consideradas por el modelo y el nivel de confianza porcentual."
            ])
        ]
    },
    {
        "id": "TASK_FE_016",
        "file": "TASK_FE_016_TemplatesPage.md",
        "title": "Vista de Plantillas de Reglas y Parámetros de Conciliación",
        "status": "[x]",
        "prog": "70% -> 75%",
        "date": "2026-08-05 15:30",
        "p1": "Crear el archivo src/pages/TemplatesPage.jsx",
        "p1_subs": ["Diseñar grilla de plantillas configuradas (ej: Conciliación Bancaria Mensual, Tarjetas de Crédito)", "Mostrar tolerancias numéricas (margen de error de centavos) y reglas activas"],
        "p2": "Conectar con la API de Plantillas",
        "p2_subs": ["Consultar GET /api/v1/templates y habilitar activación/desactivación"],
        "purpose": "Administra las reglas de negocio y algoritmos de coincidencia (75%), definiendo tolerancias de centavos y márgenes de días entre fechas.",
        "prereqs": [
            ("Gestión de Reglas de Negocio en Frontend", "Configuración de parámetros de tolerancia numérica y temporal para algoritmos de cruce contable."),
            ("Tarjetas de Configuración con Alternadores (Toggle Switches)", "Uso de componentes tipo switch para activar o pausar reglas específicas.")
        ],
        "steps": [
            ("Crear `src/pages/TemplatesPage.jsx`", [
                "Mapea la lista de plantillas conteniendo: Nombre de la plantilla, Tolerancia de días, Margen de diferencia permitida y Estado (Activa/Inactiva).",
                "Agrega botones para 'Crear Nueva Plantilla' y 'Editar Reglas'."
            ])
        ]
    },
    {
        "id": "TASK_FE_017",
        "file": "TASK_FE_017_RuleBuilderModal.md",
        "title": "Componente Constructor de Reglas de Coincidencia Personalizadas",
        "status": "[ ]",
        "prog": "75% -> 80%",
        "date": "2026-08-05 16:00",
        "p1": "Crear src/components/templates/RuleBuilderModal.jsx",
        "p1_subs": ["Diseñar formulario visual de construcción de reglas condicionales (SI Monto es Igual Y Fecha difiere <= X días)", "Agregar validación sintáctica de expresiones de regla"],
        "p2": "Guardar plantilla en el backend",
        "p2_subs": ["Enviar POST /api/v1/templates"],
        "purpose": "Construye reglas de conciliación personalizadas dinámicas (80%), permitiendo a los contadores crear algoritmos de cruce adaptados a su negocio.",
        "prereqs": [
            ("Constructores de Expresiones Lógicas Visuales (Query Builders)", "Creación de interfaces compuestas por bloques de condición (SI, Y, O, IGUAL_A, CONTIENE)."),
            ("Validación de Sintaxis en Cliente", "Verificación de integridad de las reglas antes de ser compiladas por el backend.")
        ],
        "steps": [
            ("Crear `src/components/templates/RuleBuilderModal.jsx`", [
                "Diseña la interfaz de adición de condiciones lógicas dinámicas.",
                "Permite seleccionar campos, operadores de comparación (==, <=, >=, CONTAINS) y valores de tolerancia.",
                "Envía la nueva plantilla configurada al servidor."
            ])
        ]
    },
    {
        "id": "TASK_FE_018",
        "file": "TASK_FE_018_AuditLogsPage.md",
        "title": "Vista de Logs de Auditoría e Inmutabilidad Hash Contable",
        "status": "[x]",
        "prog": "80% -> 85%",
        "date": "2026-08-05 16:30",
        "p1": "Crear el archivo src/pages/AuditLogsPage.jsx",
        "p1_subs": ["Diseñar la tabla de registros de auditoría inmutables (Audit Trail)", "Mostrar sellos de tiempo, usuario ejecutores, tipo de acción y Hashes SHA-256 de verificación"],
        "p2": "Conectar con la API de Auditoría",
        "p2_subs": ["Consultar GET /api/v1/audit/logs"],
        "purpose": "Garantiza el cumplimiento legal y la inmutabilidad de los ajustes contables (85%), presentando el registro completo de auditoría con hashes SHA-256.",
        "prereqs": [
            ("Diseño de Registros Inmutables de Auditoría (Audit Trail)", "Presentación de historiales de eventos de seguridad y cambios contables que no admiten edición ni borrado."),
            ("Visualización de Hashes Criptográficos", "Mapeo truncado de cadenas SHA-256 con opción de copia en portapapeles para verificación externa.")
        ],
        "steps": [
            ("Crear `src/pages/AuditLogsPage.jsx`", [
                "Diseña la tabla de auditoría: Timestamp UTC, Auditor, Acción Realizada, Entidad Afectada, Dirección IP, Hash de Inmutabilidad SHA-256.",
                "Permite filtrar los registros por rango de fechas y tipo de acción realizada."
            ])
        ]
    },
    {
        "id": "TASK_FE_019",
        "file": "TASK_FE_019_AuditFilterExportPanel.md",
        "title": "Componente de Filtrado y Exportación de Reportes Legales",
        "status": "[ ]",
        "prog": "85% -> 88%",
        "date": "2026-08-05 17:00",
        "p1": "Crear src/components/audit/AuditFilterPanel.jsx",
        "p1_subs": ["Diseñar barra de descargas para exportación de reportes en PDF y Excel contable", "Conectar con la API GET /api/v1/audit/export"],
        "p2": "Manejar la descarga de blobs de archivos",
        "p2_subs": ["Implementar función helper de descarga de archivos binarios"],
        "purpose": "Permite la exportación de dictámenes de conciliación y reportes de auditoría (88%) para entregas ante entes de control fiscal.",
        "prereqs": [
            ("Manejo de Descarga de Archivos Binarios Blob en React", "Conversión de respuestas Axios/Fetch tipo arraybuffer a objetos Blob y desencadenamiento de descargas automáticas."),
            ("Generación de Reportes Oficiales", "Integración con servicios de exportación formateados para requisitos de contabilidad legal.")
        ],
        "steps": [
            ("Crear `src/components/audit/AuditFilterPanel.jsx`", [
                "Agrega los botones de exportación 'Exportar en Excel (.xlsx)' y 'Descargar Dictamen PDF'.",
                "Implementa la función de recepción de blobs binarios y simulación de click en enlace de descarga automática."
            ])
        ]
    },
    {
        "id": "TASK_FE_020",
        "file": "TASK_FE_020_SettingsPage.md",
        "title": "Vista de Configuración del Workspace y Miembros de Equipo",
        "status": "[ ]",
        "prog": "88% -> 92%",
        "date": "2026-08-05 17:30",
        "p1": "Crear el archivo src/pages/SettingsPage.jsx",
        "p1_subs": ["Diseñar panel de administración del equipo contable y gestión de permisos por rol", "Implementar invitación de nuevos auditores vía correo electrónico"],
        "p2": "Gestión de datos de la empresa",
        "p2_subs": ["Permitir actualizar el NIT, Razón Social y Moneda Funcional del Workspace"],
        "purpose": "Administra el entorno de trabajo colaborativo (92%), permitiendo invitar auditores, asignar permisos y configurar la moneda base de la organización.",
        "prereqs": [
            ("Gestión de Equipos y Miembros en SaaS B2B", "Interfaz para invitar, cambiar roles y revocar accesos a miembros del equipo contable."),
            ("Configuración Multi-Moneda Base", "Selección de la moneda principal de presentación de informes de conciliación.")
        ],
        "steps": [
            ("Crear `src/pages/SettingsPage.jsx`", [
                "Diseña la pestaña de datos generales del Workspace (Nombre, NIT, Moneda principal COP/USD/EUR).",
                "Diseña la tabla de miembros de equipo con sus roles (Administrador, Auditor Senior, Auditor Junior, Solo Lectura).",
                "Implementa el modal para enviar invitaciones por correo electrónico."
            ])
        ]
    },
    {
        "id": "TASK_FE_021",
        "file": "TASK_FE_021_ProfilePage.md",
        "title": "Vista de Perfil de Usuario y Claves API de Seguridad",
        "status": "[ ]",
        "prog": "92% -> 95%",
        "date": "2026-08-05 18:00",
        "p1": "Crear el archivo src/pages/ProfilePage.jsx",
        "p1_subs": ["Diseñar vista de datos personales del auditor y actualización de contraseña", "Diseñar sección de generación de Claves API (API Keys) para integraciones externas"],
        "p2": "Conectar con la API de Seguridad",
        "p2_subs": ["Implementar cambio seguro de contraseña"],
        "purpose": "Permite al usuario gestionar su perfil (95%), cambiar su clave de acceso y administrar tokens API para integraciones con ERPs contables externos.",
        "prereqs": [
            ("Gestión de Claves de Seguridad API Keys", "Generación, revelado de una sola vez y revocación de credenciales secretas de integración."),
            ("Validación de Cambio de Contraseña Segura", "Confirmación de clave actual y validación de nueva clave en cliente antes de enviar.")
        ],
        "steps": [
            ("Crear `src/pages/ProfilePage.jsx`", [
                "Maqueta el formulario de actualización de datos de perfil.",
                "Implementa la sección de seguridad con la tabla de API Keys generadas para conectores de ERPs.",
                "Agrega la funcionalidad para revocar claves comprometidas."
            ])
        ]
    },
    {
        "id": "TASK_FE_022",
        "file": "TASK_FE_022_BatchProgressDrawer.md",
        "title": "Componente Monitor de Lotes y Progreso de Trabajos en Segundo Plano",
        "status": "[ ]",
        "prog": "95% -> 97%",
        "date": "2026-08-05 18:30",
        "p1": "Crear src/components/jobs/BatchProgressDrawer.jsx",
        "p1_subs": ["Diseñar panel de monitoreo de trabajos de conciliación asíncronos en segundo plano", "Mostrar barra de progreso en tiempo real de registros procesados por segundo"],
        "p2": "Suscripción a eventos de progreso",
        "p2_subs": ["Implementar sondeo SSE / Polling a /api/v1/jobs/active"],
        "purpose": "Notifica en tiempo real el avance de ejecuciones masivas de conciliación (97%) que procesan millones de registros en segundo plano.",
        "prereqs": [
            ("Monitoreo de Procesamiento por Lotes (Batch Jobs)", "Visualización del progreso de tareas pesadas de backend de larga duración."),
            ("Mecanismos de Actualización en Tiempo Real (Server-Sent Events / Polling)", "Recepción contínua de eventos de porcentaje de avance sin recargar la página.")
        ],
        "steps": [
            ("Crear `src/components/jobs/BatchProgressDrawer.jsx`", [
                "Diseña la ventana flotante de monitoreo de tareas de conciliación activas.",
                "Muestra el porcentaje procesado, velocidad de registros por segundo y tiempo estimado de finalización.",
                "Permite cancelar un trabajo de conciliación en curso."
            ])
        ]
    },
    {
        "id": "TASK_FE_023",
        "file": "TASK_FE_023_SystemHealthPage.md",
        "title": "Vista de Diagnóstico de Salud del Sistema y Estado de Servicios",
        "status": "[ ]",
        "prog": "97% -> 99%",
        "date": "2026-08-05 19:00",
        "p1": "Crear el archivo src/pages/SystemHealthPage.jsx",
        "p1_subs": ["Diseñar panel de estado de conectores: Backend Core (Java 21), Coprocesador IA (Python gRPC 9090), PostgreSQL", "Mostrar métricas de latencia de respuestas en milisegundos"],
        "p2": "Consultar endpoint de salud",
        "p2_subs": ["Invocar GET /api/v1/health"],
        "purpose": "Ofrece un diagnóstico del estado técnico de la plataforma (99%), monitoreando el estado de conexión del motor Java y el coprocesador gRPC Python.",
        "prereqs": [
            ("Monitoreo de Salud de Microservicios y Conectores", "Consumo de endpoints Healthcheck para presentar el estado operacional de bases de datos y microservicios sidecar."),
            ("Indicadores de Latencia en Milisegundos", "Medición del tiempo de ida y vuelta (RTT) de las peticiones de verificación.")
        ],
        "steps": [
            ("Crear `src/pages/SystemHealthPage.jsx`", [
                "Diseña las tarjetas de estado de conectividad de los componentes del sistema.",
                "Muestra insignias verdes/rojas indicando el funcionamiento del Backend Core, Coprocesador IA en puerto 9090 y Base de Datos PostgreSQL."
            ])
        ]
    },
    {
        "id": "TASK_FE_024",
        "file": "TASK_FE_024_ErrorPageAndBuildValidation.md",
        "title": "Vista Error Fallback y Validación de Build de Producción",
        "status": "[ ]",
        "prog": "99% -> 100%",
        "date": "2026-08-05 19:30",
        "p1": "Crear el archivo src/pages/ErrorPage.jsx",
        "p1_subs": ["Diseñar página de error 404/500 con botón de retorno al Dashboard"],
        "p2": "Verificación final de compilación de paquete web",
        "p2_subs": ["Ejecutar npm run build en web-ui/ asegurando empaquetado limpio en dist/"],
        "purpose": "Finaliza el desarrollo de la interfaz cliente (100%), garantizando el manejo elegante de errores y la verificación del build de producción.",
        "prereqs": [
            ("Degradación Elegante de Aplicaciones Web", "Implementación de vistas de contingencia amigables ante fallos de rutas o caídas de servidor."),
            ("Validación de Bundles de Producción Vite", "Confirmación de la generación de artefactos estáticos optimizados minificados sin errores en la carpeta dist/.")
        ],
        "steps": [
            ("Crear `src/pages/ErrorPage.jsx`", [
                "Diseña la vista de pantalla completa para manejar errores de navegación y caídas del servidor."
            ]),
            ("Validar Build de Producción 100%", [
                "Ejecuta `npm run build` en la carpeta `web-ui/`.",
                "Comprueba que se genere el directorio `dist/` con todos los bundles compilados sin errores."
            ])
        ]
    }
]

def generate_markdown(t):
    md = []
    # Checklist at top
    md.append(f"- {t['status']} {t['id']} — {t['title']} 📅 {t['date']}")
    md.append(f"\t- {t['status']} Paso 1: {t['p1']}")
    for sub in t['p1_subs']:
        md.append(f"\t\t- {t['status']} {sub}")
    md.append(f"\t- {t['status']} Paso 2: {t['p2']}")
    for sub in t['p2_subs']:
        md.append(f"\t\t- {t['status']} {sub}")
    if 'p3' in t:
        md.append(f"\t- {t['status']} Paso 3: {t['p3']}")
        for sub in t['p3_subs']:
            md.append(f"\t\t- {t['status']} {sub}")
    
    md.append("")
    md.append(f"# {t['id']} — {t['title']}")
    md.append("")
    md.append(f"**Módulo:** `web-ui/`  ")
    md.append(f"**Porcentaje de Avance:** {t['prog']}  ")
    md.append(f"**Estado:** {'COMPLETADO' if t['status'] == '[x]' else 'PENDIENTE'}  ")
    md.append(f"**Prioridad:** ALTA  ")
    md.append(f"**Depende de:** Tareas previas de la secuencia  ")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 1. Propósito y Justificación Técnica")
    md.append("")
    md.append(t['purpose'])
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 2. Prerrequisitos de Conocimiento Técnico y Conceptos Clave")
    md.append("")
    md.append("Para abordar esta tarea con éxito, el desarrollador debe dominar y aplicar los siguientes conceptos:")
    md.append("")
    for name, desc in t['prereqs']:
        md.append(f"* **{name}:** {desc}")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 3. Instrucciones de Implementación Paso a Paso")
    md.append("")
    
    step_num = 1
    for step_title, sub_steps in t['steps']:
        md.append(f"### Paso {step_num}: {step_title}")
        for idx, s in enumerate(sub_steps, 1):
            md.append(f"{idx}. {s}")
        md.append("")
        step_num += 1

    md.append("---")
    md.append("")
    md.append("## 4. Criterios de Aceptación y Verificación")
    md.append("")
    md.append("| # | Criterio de Aceptación | Método de Verificación |")
    md.append("|---|---|---|")
    md.append("| 1 | Estructura e interacción implementada conforme a la especificación | Inspección visual en navegador y herramientas de desarrollo F12 |")
    md.append("| 2 | Cero errores no capturados en consola de JavaScript | Verificar consola de DevTools sin excepciones rojas |")
    md.append("")
    return "\n".join(md)

# Clean out old task files in docs/07-implementation/guide/03_Frontend
for f in os.listdir(docs_frontend_dir):
    if f.startswith("TASK_FE_"):
        os.remove(os.path.join(docs_frontend_dir, f))

# Write 24 tasks
for t in tasks:
    filepath = os.path.join(docs_frontend_dir, t['file'])
    content = generate_markdown(t)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Write TASK_INDEX.md
index_content = """# Índice de Tareas de Implementación Frontend (0% -> 100%) — SmartReconcile

**Proyecto:** SmartReconcile  
**Módulo:** `03_Frontend` (`web-ui/`)  
**Estado General:** En Desarrollo  

---

## Hoja de Ruta Completa de Implementación Frontend (24 Tareas Secuenciales)

| Tarea ID | Archivo de Especificación | Descripción de la Tarea | Rango | Estado |
|---|---|---|---|---|
| **TASK_FE_001** | [`TASK_FE_001_ViteTailwindSetup.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_001_ViteTailwindSetup.md) | Inicialización del Proyecto Web React 18, Vite y Tailwind CSS | 0% -> 4% | COMPLETADO |
| **TASK_FE_002** | [`TASK_FE_002_DesignSystemTokens.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_002_DesignSystemTokens.md) | Sistema de Diseño Financiero CSS y Tokens Dark Mode HSL | 4% -> 8% | COMPLETADO |
| **TASK_FE_003** | [`TASK_FE_003_HttpApiService.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_003_HttpApiService.md) | Cliente API REST Axios, Interceptores JWT y Manejo de Errores | 8% -> 12% | COMPLETADO |
| **TASK_FE_004** | [`TASK_FE_004_ZustandAuthStore.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_004_ZustandAuthStore.md) | Tienda de Estado Global Zustand para Autenticación y Workspace | 12% -> 16% | COMPLETADO |
| **TASK_FE_005** | [`TASK_FE_005_ToastNotificationUi.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_005_ToastNotificationUi.md) | Componente Sistema de Notificaciones Toast y Error Boundary | 16% -> 20% | COMPLETADO |
| **TASK_FE_006** | [`TASK_FE_006_AppShellAndNavbar.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_006_AppShellAndNavbar.md) | App Shell, Sidebar Navegacional y Layout Principal | 20% -> 25% | COMPLETADO |
| **TASK_FE_007** | [`TASK_FE_007_LandingPage.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_007_LandingPage.md) | Página Institucional y Promocional de la Plataforma | 25% -> 30% | COMPLETADO |
| **TASK_FE_008** | [`TASK_FE_008_LoginPage.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_008_LoginPage.md) | Vista de Autenticación de Usuario y MFA | 30% -> 35% | COMPLETADO |
| **TASK_FE_009** | [`TASK_FE_009_DashboardMetricsOverview.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_009_DashboardMetricsOverview.md) | Vista Dashboard Ejecutivo de Métricas y KPIs de Conciliación | 35% -> 40% | COMPLETADO |
| **TASK_FE_010** | [`TASK_FE_010_ReconciliationCharts.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_010_ReconciliationCharts.md) | Componente Gráficos Interactivos de Conciliación y Tendencias | 40% -> 45% | COMPLETADO |
| **TASK_FE_011** | [`TASK_FE_011_IngestionPage.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_011_IngestionPage.md) | Vista de Ingestión de Datos y Carga de Archivos Drag & Drop | 45% -> 50% | COMPLETADO |
| **TASK_FE_012** | [`TASK_FE_012_ColumnMappingWizard.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_012_ColumnMappingWizard.md) | Componente Wizard de Previsualización y Mapeo de Columnas | 50% -> 55% | PENDIENTE |
| **TASK_FE_013** | [`TASK_FE_013_DiscrepanciesPage.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_013_DiscrepanciesPage.md) | Vista Explorador de Discrepancias y Tabla de Cuadrante | 55% -> 60% | COMPLETADO |
| **TASK_FE_014** | [`TASK_FE_014_ResolutionWorkbenchModal.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_014_ResolutionWorkbenchModal.md) | Componente Modal de Resolución Manual y Ajuste Contable | 60% -> 65% | PENDIENTE |
| **TASK_FE_015** | [`TASK_FE_015_AiExplanationDrawer.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_015_AiExplanationDrawer.md) | Componente Drawer de Explicación IA y Razonamiento Explicable | 65% -> 70% | PENDIENTE |
| **TASK_FE_016** | [`TASK_FE_016_TemplatesPage.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_016_TemplatesPage.md) | Vista de Plantillas de Reglas y Parámetros de Conciliación | 70% -> 75% | COMPLETADO |
| **TASK_FE_017** | [`TASK_FE_017_RuleBuilderModal.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_017_RuleBuilderModal.md) | Componente Constructor de Reglas de Coincidencia Personalizadas | 75% -> 80% | PENDIENTE |
| **TASK_FE_018** | [`TASK_FE_018_AuditLogsPage.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_018_AuditLogsPage.md) | Vista de Logs de Auditoría e Inmutabilidad Hash Contable | 80% -> 85% | COMPLETADO |
| **TASK_FE_019** | [`TASK_FE_019_AuditFilterExportPanel.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_019_AuditFilterExportPanel.md) | Componente de Filtrado y Exportación de Reportes Legales | 85% -> 88% | PENDIENTE |
| **TASK_FE_020** | [`TASK_FE_020_SettingsPage.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_020_SettingsPage.md) | Vista de Configuración del Workspace y Miembros de Equipo | 88% -> 92% | PENDIENTE |
| **TASK_FE_021** | [`TASK_FE_021_ProfilePage.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_021_ProfilePage.md) | Vista de Perfil de Usuario y Claves API de Seguridad | 92% -> 95% | PENDIENTE |
| **TASK_FE_022** | [`TASK_FE_022_BatchProgressDrawer.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_022_BatchProgressDrawer.md) | Componente Monitor de Lotes y Progreso de Trabajos en Segundo Plano | 95% -> 97% | PENDIENTE |
| **TASK_FE_023** | [`TASK_FE_023_SystemHealthPage.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_023_SystemHealthPage.md) | Vista de Diagnóstico de Salud del Sistema y Estado de Servicios | 97% -> 99% | PENDIENTE |
| **TASK_FE_024** | [`TASK_FE_024_ErrorPageAndBuildValidation.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_024_ErrorPageAndBuildValidation.md) | Vista Error Fallback y Validación de Build de Producción | 99% -> 100% | PENDIENTE |
"""

with open(os.path.join(docs_frontend_dir, "TASK_INDEX.md"), "w", encoding="utf-8") as f:
    f.write(index_content)

# Copy docs/07-implementation/guide to guide/
shutil.rmtree(r"c:\PROGRAMMING\PROJECTS\SmartReconcile\guide", ignore_errors=True)
shutil.copytree(r"c:\PROGRAMMING\PROJECTS\SmartReconcile\docs\07-implementation\guide", r"c:\PROGRAMMING\PROJECTS\SmartReconcile\guide")

print("Successfully generated 24 expanded tasks for SmartReconcile and synchronized guide directories.")
