# TASK BE-009 — `BankStatementBatch.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/ledger/model/`  
**File Type:** JPA `@Entity` Class  
**Priority:** HIGH — Header record for uploaded statement files.  
**Depends On:** `TASK_BE_008`  
**Blocks:** Statement line items  

---

## 1. Purpose

Maps bank statement file ingestion batches to PostgreSQL table `bank_statement_batches`, storing `openingBalance` and `closingBalance` as `BigDecimal`.

---

## 2. Step-by-Step Implementation Instructions

1. Create `BankStatementBatch.java`.
2. Annotate with `@Entity` and `@Table(name = "bank_statement_batches")`.
3. Add fields: `id`, `tenantId`, `bankAccountId`, `fileName`, `formatType`, `status`, `BigDecimal openingBalance`, `BigDecimal closingBalance`, `uploadedAt`.

---

## 3. Verification Command

```bash
./mvnw compile
```
