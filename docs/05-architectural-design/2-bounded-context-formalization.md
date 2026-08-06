# Deliverable 2: Bounded Context Formalization (D2) [GLOBAL]

**Project:** SmartReconcile  
**Document ID:** D2-BOUNDED-CONTEXTS  
**Phase:** 5 — Architectural Design (Tier 0)  

---

## 1. Domain-Driven Design (DDD) Bounded Context Map

SmartReconcile is partitioned into **4 explicit Bounded Contexts**:

```mermaid
graph TD
    subgraph BC_ING ["1. Statement Ingestion & Parsing Context (MOD-ING)"]
        IngestAggregate["BankStatementBatch Aggregate"]
        TemplateAggregate["BankTemplateSchema Aggregate"]
    end

    subgraph BC_DET ["2. Deterministic Matching Core Context (MOD-DET)"]
        LedgerAggregate["TransactionLedger Aggregate"]
        MatchAggregate["ReconciliationMatch Aggregate"]
        AuditAggregate["AuditLog Aggregate"]
    end

    subgraph BC_AGT ["3. Agentic AI Resolution Context (MOD-AGT)"]
        DiscrepancyAggregate["DiscrepancyItem Aggregate"]
        ProposalAggregate["JournalEntryProposal Aggregate"]
    end

    subgraph BC_UI ["4. Operator Audit & Approval Context (MOD-UI)"]
        DashboardView["Dashboard Metrics & UI Views"]
        TemplateStudioView["Template Mapper Studio UI"]
    end

    %% Context Relationships
    BC_ING -->|Upstream / Downstream (gRPC Protobuf)| BC_DET
    BC_DET -->|Customer / Supplier (Redis Queue / gRPC)| BC_AGT
    BC_AGT -->|Conformist (Double-Entry Proposals)| BC_DET
    BC_DET <-->|Shared Kernel (REST API / WebSockets)| BC_UI
    BC_ING <-->|Shared Kernel (REST API)| BC_UI
```

## 2. Context Responsibilities & Ubiquitous Language Mapping

1. **Ingestion & Parsing Context (`MOD-ING`):**
   - *Language:* Statement Batch, File Signature, Column Schema, VLM Slice, Row Extraction.
   - *Boundary:* Pure data translation from raw external files to clean `BankTransactionEvent` streams.
2. **Deterministic Matching Context (`MOD-DET`):**
   - *Language:* Partida Doble, In-Memory Exact Key, Windowed Fuzzy Match, Accounting Guardrail.
   - *Boundary:* Core ledger source of truth and state classification.
3. **Agentic Resolution Context (`MOD-AGT`):**
   - *Language:* Discrepancy Delta ($\Delta$), Tool FX Verification, Fee Schedule Match, Confidence Score ($S_c$).
   - *Boundary:* Investigation reasoning and proposal generation; zero write access to production ledgers.
4. **Operator Audit Context (`MOD-UI`):**
   - *Language:* KPI Widgets, Discrepancy Review Panel, Template Studio, Signed Audit Report.
   - *Boundary:* Human-in-the-loop interaction and SOC-2 compliance visualization.
