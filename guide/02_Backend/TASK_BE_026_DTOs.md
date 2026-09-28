# TASK BE-026 — Java DTO Records

**Module:** `backend-core/src/main/java/com/smartreconcile/dto/`  
**File Type:** Java `record` Types  
**Priority:** HIGH — Strongly-typed JSON request and response payloads.  
**Depends On:** `TASK_BE_006`  
**Blocks:** REST API Controllers  

---

## 1. Purpose

Declares immutable Java 21 DTO records for REST API communication.

---

## 2. Step-by-Step Implementation Instructions

1. Create `LoginRequest.java`: `public record LoginRequest(@NotBlank @Email String email, @NotBlank String password) {}`.
2. Create `AuthResponse.java`: `public record AuthResponse(String status, String role) {}`.
3. Create `IngestionResponse.java`: `public record IngestionResponse(UUID batchId, int totalRows, boolean templateMatched) {}`.
4. Create `MetricsResponse.java`: `public record MetricsResponse(long totalIngested, double matchRatePercent, long pendingDiscrepancies, BigDecimal leakageRecovered) {}`.

---

## 3. Verification Command

```bash
./mvnw test-compile
```
