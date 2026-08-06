# TASK BE-015 — `BankTemplate.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/ledger/model/`  
**File Type:** JPA `@Entity` Class  
**Priority:** HIGH — Bank statement column mapping schema (`MOD-ING-TPL`).  
**Depends On:** `TASK_BE_007`  
**Blocks:** Statement template manager UI & parser  

---

## 1. Purpose

Maps bank statement parsing schemas to PostgreSQL table `bank_templates`.

---

## 2. Step-by-Step Implementation Instructions

1. Create `BankTemplate.java`.
2. Map `headerRegexSignature` and `columnMappingJson` (`JSONB`).

---

## 3. Verification Command

```bash
./mvnw compile
```
