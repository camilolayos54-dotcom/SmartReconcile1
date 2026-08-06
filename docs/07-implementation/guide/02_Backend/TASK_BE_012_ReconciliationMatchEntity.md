# TASK BE-012 — `ReconciliationMatch.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/ledger/model/`  
**File Type:** JPA `@Entity` Class  
**Priority:** HIGH — Association between internal ledger entry and bank statement line.  
**Depends On:** `TASK_BE_010`, `TASK_BE_011`  
**Blocks:** Discrepancy resolution  

---

## 1. Purpose

Maps matching execution output pairs to PostgreSQL table `reconciliation_matches`.

---

## 2. Step-by-Step Implementation Instructions

1. Create `ReconciliationMatch.java`.
2. Map `ledgerId`, `statementLineId`, `matchType`, `BigDecimal deltaAmount`, `matchedAt`.

---

## 3. Verification Command

```bash
./mvnw compile
```
