# TASK BE-007 — `Tenant.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/ledger/model/`  
**File Type:** JPA `@Entity` Class  
**Priority:** HIGH — Root multi-tenant domain entity.  
**Depends On:** `TASK_BE_005`  
**Blocks:** All tenant-isolated database entities  

---

## 1. Purpose

Represents an organization tenant account in `SmartReconcile`. Establishes the multi-tenant root entity mapped to PostgreSQL table `tenants`.

---

## 2. Step-by-Step Implementation Instructions

1. Create `Tenant.java` in `com/smartreconcile/ledger/model/`.
2. Annotate class with `@Entity`, `@Table(name = "tenants")`, `@EntityListeners(AuditingEntityListener.class)`.
3. Add `@Id @GeneratedValue(strategy = GenerationType.UUID) private UUID id;`.
4. Add `@Column(name = "company_name", nullable = false) private String companyName;`.
5. Add `@Column(name = "base_currency", nullable = false) private String baseCurrency;`.
6. Add `@CreatedDate @Column(name = "created_at", updatable = false) private Timestamp createdAt;`.
7. Add getters, setters, and no-args constructor.

---

## 3. Verification Command

```bash
./mvnw compile
```
