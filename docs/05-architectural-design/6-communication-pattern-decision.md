# Deliverable 6: ADR — Communication Pattern Decision (D6) [GLOBAL]

**Project:** SmartReconcile  
**Document ID:** D6-ADR-COMMUNICATION-PATTERNS  
**Phase:** 5 — Architectural Design (Tier 1 ADR)  
**Status:** Accepted  

---

## 1. Context

Inter-service communication between Java (`backend-core`) and Python (`ai-coprocessor`) must transfer thousands of transaction events per second with strict schema validation and sub-millisecond serialization overhead.

## 2. Decision

We decide to adopt **gRPC over HTTP/2 with Shared Protocol Buffers (`proto/reconciliation.proto`)** for all internal inter-process communication, supplemented by **Redis Asynchronous Queues** for background job dispatches:

1. **Java <-> Python IPC:** Executed over gRPC Protobuf binary channels (`StreamBankEvents` and `SubmitAdjustmentProposal`).
2. **Background Discrepancy Queue:** `MOD-DET` pushes unmatched discrepancy payloads to Redis list `queue:discrepancies:ai`, consumed asynchronously by Python AI workers.
3. **Frontend <-> Backend:** Executed over HTTPS REST APIs (JSON) and WebSockets (WSS).

## 3. Consequences

### Positive
- **Ultra-Fast Serialization:** Protobuf binary payloads are up to 6x smaller and 10x faster to serialize than JSON over HTTP/1.1.
- **Strict Schema Enforcement:** `.proto` contract files eliminate payload key mismatch bugs between Java and Python.

### Negative / Trade-offs
- Protobuf schema changes require compiling stubs in both Java (Maven) and Python (Protoc).
