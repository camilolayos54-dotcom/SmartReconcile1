# Deliverable 2: User Flows & Task Flows [MODULE: MOD-AGT]

**Module Code:** `MOD-AGT` (Agentic AI Discrepancy Resolution Engine)  
**Document ID:** D2-USER-FLOWS-MOD-AGT  
**Phase:** 4 — System Modeling (Track A)  

---

## 1. Task Flow 1: Multi-Tool AI Investigation & Proposal Generation

```mermaid
flowchart TD
    Start1["Pop Discrepancy Payload from Redis"] --> CalcDelta["Compute Delta = Internal Amount - Bank Amount"]
    CalcDelta --> ScrubPII["Scrub PII Attributes from Prompt Context"]
    ScrubPII --> AgentLoop["Execute LangChain Multi-Tool Loop"]
    
    AgentLoop --> ToolFee["Tool Fee Verifier: Query Acquirer Interchange Schedules"]
    AgentLoop --> ToolFX["Tool FX Lookup: Query Historical Exchange Rates"]
    AgentLoop --> ToolTZ["Tool Timezone Shift: Normalize Cutoff Timestamps"]
    
    ToolFee --> Evaluator{"Tool Output Matches Delta?"}
    ToolFX --> Evaluator
    ToolTZ --> Evaluator
    
    Evaluator -- Yes --> ComputeScore["Calculate Confidence Score Sc"]
    Evaluator -- No --> SetLowScore["Set Confidence Score Sc Below Threshold"]
    
    ComputeScore --> ScoreCheck{"Confidence Sc >= 85%?"}
    ScoreCheck -- Yes --> BuildJournal["Construct Double-Entry Balancing Proposal and Step Log"]
    BuildJournal --> Transmit["Transmit Proposal via gRPC to MOD-DET and MOD-UI"]
    
    ScoreCheck -- No --> FlagManual["Flag Status = ESCALATED_MANUAL_REVIEW"]
    SetLowScore --> FlagManual
    FlagManual --> Transmit
    Transmit --> EndFlow1["Task Flow Complete"]
```
