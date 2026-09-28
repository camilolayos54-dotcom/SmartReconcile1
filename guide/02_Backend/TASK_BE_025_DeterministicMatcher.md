# TASK BE-025 — `DeterministicMatcher.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/engine/`  
**File Type:** Spring `@Service`  
**Priority:** CRITICAL — High-speed deterministic matching core (>10,000 TPS).  
**Depends On:** `TASK_BE_023`, `TASK_BE_024`  
**Blocks:** gRPC streaming ingestion  

---

## 1. Purpose

Executes Java 21 Virtual Thread batch matching of incoming bank statement events against `MemoryIndexManager`. Persists matched pairs to PostgreSQL or enqueues discrepancy payloads to Redis list `queue:discrepancies:ai`.

---

## 2. Step-by-Step Implementation Instructions

1. Create `DeterministicMatcher.java` in `com/smartreconcile/engine/`.
2. Inject `@Qualifier("virtualThreadExecutor") Executor executor`, `MemoryIndexManager`, `ReconciliationMatchRepository`.
3. Implement `processEvent(BankStatementLine line)`:
   - Query `memoryIndexManager.findExactMatch(...)`.
   - If exact match hit, save `ReconciliationMatch` with status `MATCHED`.
   - If delta exists, save match with status `DISCREPANCY` and `redisTemplate.opsForList().leftPush("queue:discrepancies:ai", payload)`.

---

## 3. Verification Command

```bash
./mvnw test-compile
```
