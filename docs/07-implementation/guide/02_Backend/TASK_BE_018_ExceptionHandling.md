# TASK BE-018 — `GlobalExceptionHandler.java` & Custom Exceptions

**Module:** `backend-core/src/main/java/com/smartreconcile/exception/`  
**File Type:** `@RestControllerAdvice` Class & Custom Exceptions  
**Priority:** HIGH — Centralized RFC 7807 REST error handling.  
**Depends On:** `TASK_BE_001`  
**Blocks:** REST Controllers  

---

## 1. Purpose

Captures runtime exceptions (`ResourceNotFoundException`, `InvalidAccountingEntryException`, `UnauthorizedException`) and formats standard RFC 7807 JSON error objects containing `timestamp`, `status`, `error`, `message`, and `correlation_id`.

---

## 2. Step-by-Step Implementation Instructions

1. Create `GlobalExceptionHandler.java` in `com/smartreconcile/exception/`.
2. Annotate with `@RestControllerAdvice`.
3. Add `@ExceptionHandler(InvalidAccountingEntryException.class)` handler returning HTTP 422 Unprocessable Entity.
4. Add `@ExceptionHandler(ResourceNotFoundException.class)` returning HTTP 404.

---

## 3. Verification Command

```bash
./mvnw test-compile
```
