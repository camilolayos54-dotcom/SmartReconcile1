# TASK BE-005 — `JpaAuditingConfig.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/config/`  
**File Type:** Spring `@Configuration` Class  
**Priority:** HIGH — Activates automated `@CreatedDate` and `@LastModifiedDate` JPA auditing.  
**Depends On:** `TASK_BE_001`  
**Blocks:** Entity creation timestamping  

---

## 1. Purpose

Configures JPA Auditing for Spring Data JPA, ensuring that `@CreatedDate` and `@LastModifiedDate` annotations across domain entities automatically populate with server timestamp upon persistence.

---

## 2. Step-by-Step Implementation Instructions

1. Create `backend-core/src/main/java/com/smartreconcile/config/JpaAuditingConfig.java`.
2. Add package `package com.smartreconcile.config;`.
3. Annotate class with `@Configuration` and `@EnableJpaAuditing`.

---

## 3. Verification Command

```bash
./mvnw compile
```
