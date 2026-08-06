# Deliverable 9: Frontend Component & State Architecture [MODULE: MOD-UI]

**Module Code:** `MOD-UI`  
**Document ID:** D9-FRONTEND-COMPONENT-STATE  
**Phase:** 6 — Technical Design (Tier 2 Frontend Blueprints)  

---

## 1. React Component Hierarchy Tree

```
App (Router + AuthGuard)
├── PublicLayout
│   ├── LandingPage (/landing)
│   │   ├── PublicHeaderNavbar (Logo, NavLinks, CTA Button)
│   │   ├── HeroSectionBlock (H1, Product Teaser, CTA)
│   │   ├── ROICalculatorWidget (Volume Slider, Annual Savings Display)
│   │   ├── PricingSectionBlock (Pricing Cards Grid)
│   │   └── PublicFooter
│   ├── LoginPage (/login)
│   │   ├── LoginFormBlock (EmailInput, PasswordInput, SubmitButton)
│   │   └── BrandShowcaseBlock
│   └── OnboardingPage (/onboarding)
│       └── OnboardingWizardBlock (3-Step Stepper + Form)
└── AppShell (Private Authorized Shell)
    ├── AppHeaderNavbar (TenantSwitcher, BaseCurrencySelector, WebSocketBadge)
    ├── SidebarNavigation (Collapsible Route Links)
    ├── NotificationToastContainer
    └── RouterOutlet
        ├── DashboardPage (/dashboard)
        │   ├── TopMetricsGrid (4 x MetricCard)
        │   ├── LiveActivityFeedBlock (Matching Stream Table)
        │   └── UrgentAlertsBlock
        ├── IngestionPage (/ingestion)
        │   ├── IngestionHeaderBlock
        │   ├── UploadZoneBlock (UploadDropzone)
        │   └── ParsedDataPreviewTable
        ├── DiscrepanciesPage (/discrepancies)
        │   ├── DiscrepancyQueueBlock (Filterable Queue List)
        │   └── SideBySideInspectorBlock
        │       ├── TransactionComparatorCard (Internal vs Bank)
        │       ├── AIReasoningStepCard (Sparkles + Markdown Log)
        │       └── AIProposalApprovalBlock (Journal Entry Table + Approve Button)
        ├── TemplatesPage (/templates)
        │   ├── TemplateGalleryBlock
        │   └── VisualColumnMapperStudio
        └── AuditLogsPage (/settings/audit-logs)
            ├── AuditFilterToolbar
            ├── AuditLogTableBlock (Paginated Table + AuditHashBadge)
            └── AuditDetailDrawer
```

## 2. React Global State Management Architecture (Zustand Stores)

1. **`useAuthStore`:** Stores current `user` profile, `isAuthenticated` boolean, and `login`/`logout` actions.
2. **`useReconciliationStore`:** Manages real-time `metrics` (Match Rate %, Ingested Count), `liveStream` events array, and active WebSocket connection.
3. **`useCurrencyStore`:** Manages `baseCurrency` (`USD`, `EUR`, `COP`, `MXN`) and exchange rate conversion multipliers.
