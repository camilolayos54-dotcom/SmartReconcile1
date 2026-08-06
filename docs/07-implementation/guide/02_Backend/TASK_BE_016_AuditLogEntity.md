# TASK BE-016 — `AuditLog.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/ledger/model/`  
**File Type:** JPA `@Entity` Class  
**Priority:** HIGH — Immutable SOC-2 audit trail.  
**Depends On:** `TASK_BE_007`  
**Blocks:** Compliance logging  

---

## 1. Purpose

Maps SOC-2 audit log entries to PostgreSQL table `audit_logs`, storing 64-character SHA-256 cryptographic hashes.

---

## 2. Step-by-Step Implementation Instructions

1. Create `AuditLog.java`.
2. Map `cryptographicHash` as `String` (64 chars) and `metadata` (`JSONB`).

---

## 3. Verification Command

```bash
./mvnw compile
```
