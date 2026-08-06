# Deliverable 2: User Flows & Task Flows [MODULE: MOD-ING]

**Module Code:** `MOD-ING` (Statement Ingestion, Vision Parsing & Bank Template Manager)  
**Document ID:** D2-USER-FLOWS-MOD-ING  
**Phase:** 4 — System Modeling (Track A)  

---

## 1. Task Flow 1: Bank Statement Upload & Deterministic Fast-Parse (MOD-ING-TPL)

```mermaid
flowchart TD
    Start1["Analyst Enters Ingestion Studio"] --> Upload["Drag and Drop Bank File PDF or CSV"]
    Upload --> ReadSig["Extract Header Signature and Bank ID"]
    ReadSig --> CheckCache{"Matching Template in Cache?"}
    
    CheckCache -- Yes --> RunFastParse["Execute Python Regex/CSV Deterministic Engine"]
    RunFastParse --> MathCheck{"Net Balance Equation Valid?"}
    MathCheck -- Yes --> EmitgRPC["Stream TransactionEvents via gRPC to Java Core"]
    EmitgRPC --> ShowSuccess["Display Success Toast: Ingestion Complete"]
    ShowSuccess --> EndFlow1["Task Flow Complete"]

    MathCheck -- No --> FlagCorrupted["Mark Batch Status CORRUPTED_BALANCE"]
    FlagCorrupted --> AlertUI["Display Balance Discrepancy Toast"]
    AlertUI --> EndFlow1

    CheckCache -- No --> RouteVLM["Route File to Vision-LLM Pipeline"]
    RouteVLM --> EndFlow1
```

## 2. User Flow 2: AI Vision Parsing & Reusable Template Creation

```mermaid
flowchart TD
    Start2["Unmapped PDF Received"] --> ConvertPNG["Render PDF Pages to 300DPI PNG Images"]
    ConvertPNG --> MaskPII["Redact Personal Tax IDs and Names"]
    MaskPII --> CallVLM["Send Image Slices to Vision-LLM API"]
    
    CallVLM --> VLMResponse{"VLM Extraction Success?"}
    VLMResponse -- No --> TimeoutFallback["Flag File MANUAL_PARSING_REQUIRED"]
    TimeoutFallback --> EndFlow2["User Flow Complete"]

    VLMResponse -- Yes --> PreviewScreen["Render Extracted Table Preview in React UI"]
    PreviewScreen --> UserDecision{"Analyst Choice"}
    
    UserDecision -- Confirm Data --> StreamJava["Stream TransactionEvents to Java Core"]
    UserDecision -- Save Template --> OpenTemplateStudio["Open Template Studio Mapper"]
    
    OpenTemplateStudio --> SaveSchema["Save Regex and Column Mapping Schema"]
    SaveSchema --> RefreshCache["Invalidate and Reload Redis Template Cache"]
    RefreshCache --> StreamJava
    StreamJava --> EndFlow2
```
