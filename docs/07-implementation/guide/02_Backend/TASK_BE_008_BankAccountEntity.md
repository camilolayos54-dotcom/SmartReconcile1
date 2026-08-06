# TASK BE-008 — `BankAccount.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/ledger/model/`  
**File Type:** JPA `@Entity` Class  
**Priority:** HIGH — Represents connected acquiring bank accounts.  
**Depends On:** `TASK_BE_007`  
**Blocks:** Statement batch ingestion  

---

## 1. Purpose

Maps connected acquiring bank accounts to PostgreSQL table `bank_accounts`, enforcing foreign key constraint to `Tenant`.

---

## 2. Step-by-Step Implementation Instructions

1. Create `BankAccount.java` in `com/smartreconcile/ledger/model/`.
2. Annotate with `@Entity` and `@Table(name = "bank_accounts")`.
3. Add `@Id @GeneratedValue(strategy = GenerationType.UUID) private UUID id;`.
4. Add `@Column(name = "tenant_id", nullable = false) private UUID tenantId;`.
5. Add `bankName`, `accountNumberMasked`, `currency`.

---

## 3. Verification Command

```bash
./mvnw compile
```
