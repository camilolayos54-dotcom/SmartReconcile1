# TASK BE-031 — `DashboardController.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/api/`  
**File Type:** `@RestController` Class  
**Priority:** MEDIUM — Handles `/api/v1/dashboard/metrics` (KPI Summary).  
**Depends On:** `TASK_BE_017`, `TASK_BE_026`  
**Blocks:** Dashboard UI metric cards  

---

## 1. Purpose

Aggregates reconciliation KPIs (`totalIngested`, `matchRatePercent`, `pendingDiscrepancies`, `leakageRecovered`) for real-time dashboard display.

---

## 2. Step-by-Step Implementation Instructions

1. Create `DashboardController.java`.
2. Implement `@GetMapping("/api/v1/dashboard/metrics")` querying `ReconciliationMatchRepository` and `DiscrepancyItemRepository`.

---

## 3. Verification Command

```bash
./mvnw test-compile
```
