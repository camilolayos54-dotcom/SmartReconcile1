# TASK BE-004 — `VirtualThreadConfig.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/config/`  
**File Type:** Spring `@Configuration` Bean Class  
**Priority:** HIGH — Configures Java 21 Project Loom Virtual Thread executor for high-concurrency matching.  
**Depends On:** `TASK_BE_001`  
**Blocks:** Sub-millisecond >10,000 TPS matching execution  

---

## 1. Purpose

Configures an explicit `Executor` Spring Bean leveraging Java 21 Project Loom Virtual Threads (`Executors.newVirtualThreadPerTaskExecutor()`). This allows `DeterministicMatcher` to spawn lightweight virtual threads per transaction event without OS thread context-switching overhead.

---

## 2. Step-by-Step Implementation Instructions

### Step 1: Create Package & Class
1. Create `backend-core/src/main/java/com/smartreconcile/config/VirtualThreadConfig.java`.
2. Add package header: `package com.smartreconcile.config;`.

### Step 2: Add Spring Annotations & Imports
1. Import `org.springframework.context.annotation.Bean`.
2. Import `org.springframework.context.annotation.Configuration`.
3. Import `java.util.concurrent.Executor`.
4. Import `java.util.concurrent.Executors`.
5. Annotate class with `@Configuration`.

### Step 3: Define Virtual Thread Executor Bean
1. Write method:
   ```java
   @Bean(name = "virtualThreadExecutor")
   public Executor virtualThreadExecutor() {
       return Executors.newVirtualThreadPerTaskExecutor();
   }
   ```

---

## 3. Verification Checklist

| # | Check Condition | Risk if Failed |
|---|---|---|
| 1 | Class annotated with `@Configuration` | Spring fails to register the executor Bean |
| 2 | Bean name set to `"virtualThreadExecutor"` | `@Qualifier("virtualThreadExecutor")` injections fail |

---

## 4. Verification Command

Compile project:
```bash
./mvnw compile
```
