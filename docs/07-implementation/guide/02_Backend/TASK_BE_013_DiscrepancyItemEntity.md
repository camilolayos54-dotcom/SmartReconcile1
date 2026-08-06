# TASK BE-013 — `DiscrepancyItem.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/ledger/model/`  
**File Type:** JPA `@Entity` Class  
**Priority:** HIGH — Non-matching transaction discrepancy item.  
**Depends On:** `TASK_BE_012`  
**Blocks:** AI proposal generation  

---

## 1. Purpose

Maps unmatched items to PostgreSQL table `discrepancy_items`.

---

## 2. Step-by-Step Implementation Instructions

1. Create `DiscrepancyItem.java`.
2. Map `matchId`, `rootCauseCategory`, `BigDecimal deltaAmount`, `Integer agentConfidenceScore`, `status`.

---

## 3. Verification Command

```bash
./mvnw compile
```
