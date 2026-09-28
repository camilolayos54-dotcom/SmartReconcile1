# TASK BE-023 — `MemoryIndexManager.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/engine/`  
**File Type:** Spring `@Service`  
**Priority:** CRITICAL — Manages Redis in-memory exact-match index.  
**Depends On:** `TASK_BE_004`, `TASK_BE_017`  
**Blocks:** `DeterministicMatcher.java`  

---

## 1. Purpose

Provides sub-millisecond Redis key lookup (`match:{tenant_id}:{ref_id}:{amount}`) using `StringRedisTemplate` to match incoming statement events against internal ledgers.

---

## 2. Step-by-Step Implementation Instructions

1. Create `MemoryIndexManager.java` in `com/smartreconcile/engine/`.
2. Inject `StringRedisTemplate`.
3. Implement `indexLedger(TransactionLedger ledger)` setting TTL = 24 hours.
4. Implement `findExactMatch(String tenantId, String refId, BigDecimal amount)` returning internal `ledgerId` or `null`.

---

## 3. Verification Command

```bash
./mvnw test-compile
```
