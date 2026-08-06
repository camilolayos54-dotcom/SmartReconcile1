# TASK BE-036 — `WebSocketConfig.java`

**Module:** `backend-core/src/main/java/com/smartreconcile/config/`  
**File Type:** `@Configuration` Class  
**Priority:** MEDIUM — Enables real-time WebSocket push updates to React UI.  
**Depends On:** `TASK_BE_022`  
**Blocks:** Real-time UI live match stream  

---

## 1. Purpose

Configures WebSocket STOMP endpoint (`/ws-reconcile`) for pushing match metrics and discrepancy alerts to the frontend.

---

## 2. Step-by-Step Implementation Instructions

1. Create `WebSocketConfig.java` implementing `WebSocketMessageBrokerConfigurer`.
2. Register `/ws-reconcile` with allowed origin patterns.

---

## 3. Verification Command

```bash
./mvnw test-compile
```
