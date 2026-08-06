# Deliverable 5: Class & Entity Diagrams [MODULE: MOD-DET]

**Module Code:** `MOD-DET`  
**Document ID:** D5-CLASS-DIAGRAMS-MOD-DET  
**Phase:** 6 — Technical Design (Tier 1 Backend Blueprints)  

---

## 1. UML Class Diagram (Java Core Matching Engine)

```mermaid
classDiagram
    class DeterministicMatcher {
        -MemoryIndexManager memoryIndex
        -AccountingGuardrail guardrail
        +matchBatch(List~BankTransactionEvent~ events) MatchBatchResult
        +processPair(BankTransactionEvent bankEvent) ReconciliationMatch
    }

    class AccountingGuardrail {
        +validateDoubleEntry(JournalEntryProposal proposal) boolean
        -calculateSumDebits(List~JournalLine~ lines) BigDecimal
        -calculateSumCredits(List~JournalLine~ lines) BigDecimal
    }

    class ReconciliationMatch {
        -UUID id
        -UUID ledgerId
        -UUID statementLineId
        -MatchType matchType
        -BigDecimal deltaAmount
        -Timestamp matchedAt
        +getId() UUID
        +getMatchType() MatchType
    }

    class TransactionLedger {
        -UUID id
        -UUID tenantId
        -LocalDate transactionDate
        -String referenceId
        -BigDecimal amount
        -TransactionType type
        -MatchStatus status
    }

    DeterministicMatcher --> MemoryIndexManager : queries
    DeterministicMatcher --> AccountingGuardrail : uses
    DeterministicMatcher ..> ReconciliationMatch : creates
    ReconciliationMatch --> TransactionLedger : references
```
