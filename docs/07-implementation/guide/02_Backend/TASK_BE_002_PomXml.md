# TASK BE-002 — `pom.xml`

**Module:** `backend-core/`  
**File Type:** Maven Build Manifest  
**Priority:** CRITICAL — Defines Java 21 target, Spring Boot starters, gRPC plugins, and dependencies.  
**Depends On:** None  
**Blocks:** All Java compilation and Maven builds  

---

## 1. Purpose

This file is the **master build configuration** for the `backend-core` Java service. It defines Java 21 LTS as the compiler target, specifies Spring Boot 3.2+ as the parent framework, configures the `protobuf-maven-plugin` for compiling `.proto` gRPC contracts, and lists all required dependencies (Spring Web, Security, Data JPA, Redis, Flyway, PostgreSQL, JWT, gRPC).

---

## 2. Step-by-Step Implementation Instructions

### Step 1: Create the File in the Backend Root
1. In `backend-core/`, create `pom.xml`.

### Step 2: Define Project Coordinates and Spring Boot Parent
1. Declare `<modelVersion>4.0.0</modelVersion>`.
2. Define parent artifact:
   - `groupId`: `org.springframework.boot`
   - `artifactId`: `spring-boot-starter-parent`
   - `version`: `3.2.3`
3. Define project coordinates:
   - `groupId`: `com.smartreconcile`
   - `artifactId`: `backend-core`
   - `version`: `1.0.0-SNAPSHOT`
   - `name`: `SmartReconcile Backend Core`

### Step 3: Define Properties
1. Set `<java.version>21</java.version>`.
2. Set `<grpc.version>1.61.1</grpc.version>`.
3. Set `<protobuf.version>3.25.3</protobuf.version>`.
4. Set `<jjwt.version>0.12.5</jjwt.version>`.

### Step 4: Add Starter Dependencies
1. Add `spring-boot-starter-web` (REST APIs).
2. Add `spring-boot-starter-security` (Spring Security).
3. Add `spring-boot-starter-data-jpa` (Hibernate & JPA).
4. Add `spring-boot-starter-data-redis` (Redis Spring Data).
5. Add `spring-boot-starter-validation` (Bean validation annotations).
6. Add `spring-boot-starter-websocket` (WebSocket STOMP support).

### Step 5: Add Database, Security & gRPC Dependencies
1. Add `postgresql` (JDBC Driver).
2. Add `flyway-core` and `flyway-database-postgresql`.
3. Add JWT dependencies: `jjwt-api`, `jjwt-impl`, `jjwt-jackson`.
4. Add gRPC dependencies: `grpc-netty-shaded`, `grpc-protobuf`, `grpc-stub`.
5. Add `grpc-spring-boot-starter`.

### Step 6: Configure Build Plugins
1. Add `spring-boot-maven-plugin` for executable JAR packaging.
2. Add `protobuf-maven-plugin` referencing `proto/reconciliation.proto` to generate Java Protobuf classes into `target/generated-sources/`.

---

## 3. Verification Checklist

| # | Check Condition | Risk if Failed |
|---|---|---|
| 1 | `<java.version>21</java.version>` declared | Maven attempts to compile with older JDK 17/11 syntax |
| 2 | `flyway-database-postgresql` included | Flyway 10+ throws `Missing database plugin` error for PostgreSQL |
| 3 | JJWT version set to 0.12+ | Older JJWT 0.9.x methods (`Jwts.parser()`) throw deprecation errors |

---

## 4. Verification Command

Run Maven dependency tree check:
```bash
./mvnw dependency:tree
```
Expected result: Build succeeds with `BUILD SUCCESS`.
