# TASK BE-006 — Domain Enums (`MatchType`, `MatchStatus`, `RootCauseCategory`)

**Module:** `backend-core/src/main/java/com/smartreconcile/ledger/model/`  
**File Type:** Java Enums  
**Priority:** HIGH — Strongly-typed domain states for reconciliation engine.  
**Depends On:** `TASK_BE_001`  
**Blocks:** All JPA entities  

---

## 1. Purpose

Establishes strongly-typed Java enums for matching state classifications and root cause categories to eliminate string-based bugs.

---

## 2. Step-by-Step Implementation Instructions

1. In `com/smartreconcile/ledger/model/`, create `MatchType.java`:
   - Enum values: `MATCHED`, `MATCHED_FUZZY`, `DISCREPANCY`.
2. Create `MatchStatus.java`:
   - Enum values: `UNMATCHED_BANK`, `UNMATCHED_INTERNAL`, `MATCHED`, `DISCREPANCY`.
3. Create `RootCauseCategory.java`:
   - Enum values: `UNANNOUNCED_BANK_FEE`, `FX_RATE_VARIANCE`, `TIMEZONE_CUTOFF_SHIFT`, `DYNAMIC_CURRENCY_CONVERSION`, `UNKNOWN_DISCREPANCY`.

---

## 3. Verification Command

```bash
./mvnw compile
```
