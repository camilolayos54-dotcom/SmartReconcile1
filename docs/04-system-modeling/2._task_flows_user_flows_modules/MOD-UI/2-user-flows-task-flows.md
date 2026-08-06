# Deliverable 2: User Flows & Task Flows [MODULE: MOD-UI]

**Module Code:** `MOD-UI` (Operator Audit & Approval Dashboard)  
**Document ID:** D2-USER-FLOWS-MOD-UI  
**Phase:** 4 — System Modeling (Track A)  

---

## 1. User Flow 1: Interactive Discrepancy Review & Single-Click Approval

```mermaid
flowchart TD
    Start1["Analyst Opens Discrepancy Review Panel"] --> SelectRow["Select Pending Item from Queue"]
    SelectRow --> RenderPanel["Render Side-by-Side Line Items and AI Reasoning Card"]
    RenderPanel --> ReviewDetails["Analyst Reviews Step-by-Step Mathematical Log"]
    
    ReviewDetails --> Decision{"Analyst Action"}
    
    Decision -- Approve Adjustment --> PostApprove["Send POST /api/v1/discrepancies/approve"]
    PostApprove --> TriggerAudit["Java Core Writes Immutable Audit Entry"]
    TriggerAudit --> ToastSuccess["Display Success Toast: Entry Posted"]
    ToastSuccess --> ClearRow["Remove Item from Queue and Update Dashboard KPIs"]
    ClearRow --> EndFlow1["User Flow Complete"]

    Decision -- Reject Adjustment --> OpenRejectModal["Open Rejection Modal and Select Reason"]
    OpenRejectModal --> PostReject["Send POST /api/v1/discrepancies/reject"]
    PostReject --> FlagManual["Flag Item for Manual Bank Dispute"]
    FlagManual --> ClearRow
```

## 2. User Flow 2: Bank Statement Template Studio (MOD-ING-TPL) Workflow

```mermaid
flowchart TD
    Start2["User Opens Bank Template Studio"] --> DropSample["Drop Sample Bank Statement CSV or PDF"]
    DropSample --> RenderPreview["Render Header and Row Preview Table"]
    RenderPreview --> MapColumns["Drag and Drop Column Headers: Date, RefID, Amount"]
    MapColumns --> SetFormats["Configure Date Layout and Decimal Separators"]
    
    SetFormats --> RunTest["Click Dry Run Test Parsing"]
    RunTest --> TestResult{"Dry Run Parsing Success?"}
    
    TestResult -- Errors Found --> HighlightErrors["Highlight Failing Cells in Red"]
    HighlightErrors --> MapColumns
    
    TestResult -- 100% Success --> ClickPublish["Click Publish Template"]
    ClickPublish --> SaveDB["Save Template Schema in PostgreSQL and Redis Cache"]
    SaveDB --> ShowToast["Display Success Toast: Template Active"]
    ShowToast --> EndFlow2["User Flow Complete"]
```
