# TASK BE-014 — `JournalEntryProposal.java` & `JournalEntryLine.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/ledger/model/`  
**File Type:** JPA `@Entity` Classes  
**Priority:** HIGH — Double-entry balancing journal entry proposal.  
**Depends On:** `TASK_BE_013`  
**Blocks:** Double-entry accounting guardrail validation  

---

## 1. Purpose

Maps balancing proposals and line items to PostgreSQL tables `journal_entry_proposals` and `journal_entry_lines`.

---

## 2. Step-by-Step Implementation Instructions

1. Create `JournalEntryProposal.java` with `@OneToMany` relationship to `JournalEntryLine.java`.
2. Map line debit/credit amounts as `BigDecimal`.

---

## 3. Verification Command

```bash
./mvnw compile
```
