# TASK BE-010 — `BankStatementLine.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/ledger/model/`  
**File Type:** JPA `@Entity` Class  
**Priority:** HIGH — Individual transaction line parsed from bank statement.  
**Depends On:** `TASK_BE_009`  
**Blocks:** Deterministic matching engine input  

---

## 1. Purpose

Maps individual bank transaction rows to PostgreSQL table `bank_statement_lines`.

---

## 2. Step-by-Step Implementation Instructions

1. Create `BankStatementLine.java`.
2. Map fields: `id`, `batchId`, `transactionDate`, `referenceId`, `description`, `BigDecimal debitAmount`, `BigDecimal creditAmount`, `matchStatus`.

---

## 3. Verification Command

```bash
./mvnw compile
```
