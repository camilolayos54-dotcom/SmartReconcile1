# TASK BE-024 — `AccountingGuardrail.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/ledger/`  
**File Type:** Spring `@Component`  
**Priority:** CRITICAL — Enforces double-entry accounting math validation ($\sum D = \sum C$).  
**Depends On:** `TASK_BE_014`  
**Blocks:** Journal entry proposal persistence  

---

## 1. Purpose

Validates that proposed balancing journal entries satisfy double-entry accounting principles ($\sum \text{Debits} == \sum \text{Credits}$). Throws `InvalidAccountingEntryException` on imbalance.

---

## 2. Step-by-Step Implementation Instructions

1. Create `AccountingGuardrail.java` in `com/smartreconcile/ledger/`.
2. Implement `validateDoubleEntry(JournalEntryProposal proposal)`:
   - Sum `debitAmount` across all `JournalEntryLine` items.
   - Sum `creditAmount` across all `JournalEntryLine` items.
   - If `sumDebits.compareTo(sumCredits) != 0`, throw `InvalidAccountingEntryException`.

---

## 3. Verification Command

```bash
./mvnw test-compile
```
