# TASK BE-017 — Spring Data JPA Repositories

**Module:** `backend-core/src/main/java/com/smartreconcile/ledger/repository/`  
**File Type:** Java Interfaces extending `JpaRepository`  
**Priority:** HIGH — Database CRUD and query access.  
**Depends On:** `TASK_BE_007` to `TASK_BE_016`  
**Blocks:** Service and Controller layers  

---

## 1. Purpose

Declares 10 Spring Data JPA repository interfaces (`TenantRepository`, `BankAccountRepository`, `BankStatementBatchRepository`, `BankStatementLineRepository`, `TransactionLedgerRepository`, `ReconciliationMatchRepository`, `DiscrepancyItemRepository`, `JournalEntryProposalRepository`, `BankTemplateRepository`, `AuditLogRepository`).

---

## 2. Step-by-Step Implementation Instructions

1. In `com/smartreconcile/ledger/repository/`, create repository interfaces extending `JpaRepository<Entity, UUID>`.
2. Add custom JPQL/Native queries (e.g. `findByBatchIdAndReferenceId`, `findByTenantIdAndCryptographicHash`).

---

## 3. Verification Command

```bash
./mvnw test-compile
```
