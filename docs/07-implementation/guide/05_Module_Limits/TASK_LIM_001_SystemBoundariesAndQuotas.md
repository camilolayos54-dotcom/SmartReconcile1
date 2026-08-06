# TASK LIM-001 — Operational Boundaries & Quota Enforcement

**Module:** Global System Constraints  
**File Type:** System Limit Contract Specification  
**Priority:** HIGH — Prevents resource exhaustion and runaway LLM costs.  
**Depends On:** `limits.md`  
**Blocks:** Production boundary validation  

---

## 1. Purpose

Defines maximum operational limits: 50MB file upload ceiling, 25s Vision-LLM API timeout, 50k transaction batch Virtual Thread matching chunks, 5-loop agentic tool cap, and 85% AI confidence proposal threshold.

---

## 2. Step-by-Step Implementation Instructions

1. Enforce max file size check in `IngestController.java`.
2. Enforce max 5 tool loop counter in Python `discrepancy_agent.py`.
3. Enforce 85% confidence score filter before emitting gRPC proposal.

---

## 3. Verification Command

Verify boundary limits configuration across services.
