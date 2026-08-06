# Deliverable 1: Content Strategy & Information Architecture [GLOBAL]

**Project:** SmartReconcile  
**Document ID:** D1-INFORMATION-ARCHITECTURE  
**Phase:** 4 — System Modeling (Track A)  

---

## 1. Information Architecture & Sitemap Diagram

The React + Tailwind CSS Single-Page Application (SPA) is structured around four primary navigation hubs:

```mermaid
graph TD
    ROOT["SmartReconcile SPA Portal"] --> DASHBOARD["1. Reconciliation Overview Dashboard"]
    ROOT --> INGESTION["2. Bank Statement Ingestion Studio"]
    ROOT --> DISCREPANCIES["3. Discrepancy Review & Audit Center"]
    ROOT --> TEMPLATES["4. Bank Template Studio MOD-ING-TPL"]
    ROOT --> SETTINGS["5. System Admin & Audit Logs"]

    %% Dashboard Hub
    DASHBOARD --> KPI1["Reconciliation Metrics Matched Rate, TPS Rate"]
    DASHBOARD --> KPI2["Financial Leakage Recovered"]
    DASHBOARD --> STREAM["Real-time Ingestion Stream Feed"]

    %% Ingestion Hub
    INGESTION --> UPLOAD["Drag & Drop File Upload PDF, CSV, MT940"]
    INGESTION --> BATCH_LIST["Active Ingestion Batches"]
    INGESTION --> PARSE_PREVIEW["VLM Table Extraction Preview"]

    %% Discrepancy Hub
    DISCREPANCIES --> QUEUE["Pending Review Queue"]
    QUEUE --> SIDE_BY_SIDE["Side-by-Side Line Item Inspector"]
    SIDE_BY_SIDE --> REASONING_CARD["AI Step-by-Step Reasoning Card"]
    SIDE_BY_SIDE --> APPROVAL_ACTIONS["Approve / Reject Adjustment Actions"]

    %% Template Studio Hub
    TEMPLATES --> TPL_LIST["Active Bank Schemas"]
    TEMPLATES --> TPL_MAPPER["Visual Column Mapper Studio"]
    TEMPLATES --> TPL_TEST["Dry-Run Sample Tester"]

    %% Settings & Audit Hub
    SETTINGS --> AUDIT_LOGS["SOC-2 Immutable Audit Log Table"]
    SETTINGS --> USER_RBAC["User Role Management"]
    SETTINGS --> GRPC_HEALTH["gRPC Inter-Service Health Status"]
```

## 2. Content Taxonomy & Status Identifiers

- **Reconciliation Statuses:** `MATCHED` (Green), `MATCHED_FUZZY` (Blue), `DISCREPANCY` (Amber), `UNMATCHED_INTERNAL` (Purple), `UNMATCHED_BANK` (Orange), `CORRUPTED` (Red).
- **Discrepancy Root-Cause Categories:** `UNANNOUNCED_BANK_FEE`, `FX_RATE_VARIANCE`, `TIMEZONE_CUTOFF_SHIFT`, `DYNAMIC_CURRENCY_CONVERSION`, `UNKNOWN_DISCREPANCY`.
- **Template Statuses:** `DRAFT`, `TESTED_OK`, `ACTIVE_PRODUCTION`, `DEPRECATED`.

## 3. Global Navigation Rules

1. **Header Navigation:** Fixed navbar rendering active tenant, connected bank accounts, real-time WebSocket connection status badge, and user profile avatar.
2. **Side Navigation:** Collapsible left sidebar providing instant 1-click access to Dashboard, Ingestion, Discrepancies, Templates, and Audit Logs.
3. **Contextual Action Bar:** Floating action drawer appearing during discrepancy reviews or template mapping runs.
