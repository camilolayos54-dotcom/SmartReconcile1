# Frontend Master Guide & Technology Architecture

**Project:** SmartReconcile  
**Framework:** React 18 + Vite  
**Styling:** Tailwind CSS (Bancolombia Corporate Palette)  
**State Management:** Zustand  

---

## 1. Frontend Folder Structure (`web-ui/src/`)

```
web-ui/src/
├── main.jsx
├── App.jsx
├── tailwind.config.js                          <- Theme Tokens (#0B192C Navy, #FFD200 Yellow, #E11D48 Crimson)
├── assets/
├── components/
│   ├── ui/ (Button, Input, Badge, Card, Modal, Spinner)
│   └── layout/ (HeaderNavbar, Sidebar, AppShell)
├── pages/
│   ├── LandingPage.jsx (/landing)
│   ├── LoginPage.jsx (/login)
│   ├── OnboardingPage.jsx (/onboarding)
│   ├── DashboardPage.jsx (/dashboard)
│   ├── IngestionPage.jsx (/ingestion)
│   ├── DiscrepanciesPage.jsx (/discrepancies)
│   ├── TemplatesPage.jsx (/templates)
│   └── AuditLogsPage.jsx (/settings/audit-logs)
└── services/
    ├── api.js                                  <- Axios Instance with CSRF Header Injection
    ├── websocket.js                            <- WebSocket client with backoff reconnect
    └── stores/ (useAuthStore, useReconciliationStore, useCurrencyStore)
```

---

## 2. Frontend Task Index

1. [`TASK_FE_001_ViteTailwindSetup.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_001_ViteTailwindSetup.md) — Initialize Vite React SPA and configure `tailwind.config.js` with Bancolombia design tokens.
2. [`TASK_FE_002_AppShellAndNavbar.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_002_AppShellAndNavbar.md) — Create `AppShell.jsx`, `HeaderNavbar.jsx`, and `Sidebar.jsx`.
3. [`TASK_FE_003_LandingAndLoginPage.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_003_LandingAndLoginPage.md) — Create `LandingPage.jsx` and `LoginPage.jsx`.
4. [`TASK_FE_004_DashboardPage.jsx.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_004_DashboardPage.md) — Create `DashboardPage.jsx` with KPI metric cards and real-time match stream table.
5. [`TASK_FE_005_DiscrepanciesPage.jsx.md`](file:///c:/PROGRAMMING/PROJECTS/SmartReconcile/docs/07-implementation/guide/03_Frontend/TASK_FE_005_DiscrepanciesPage.md) — Create `DiscrepanciesPage.jsx` with side-by-side inspector and AI reasoning cards.
