# TASK BE-011 — `TransactionLedger.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/ledger/model/`  
**File Type:** JPA `@Entity` Class  
**Priority:** HIGH — Internal ledger charge/credit entry.  
**Depends On:** `TASK_BE_007`  
**Blocks:** Deterministic matching core  

---

## 1. Purpose

Maps internal database charges and credits to PostgreSQL table `transaction_ledgers`.

---

## 2. Step-by-Step Implementation Instructions

1. Create `TransactionLedger.java`.
2. Map `amount` to `BigDecimal` and `type` (DEBIT/CREDIT).

---

## 3. Verification Command

```bash
./mvnw compile
```
