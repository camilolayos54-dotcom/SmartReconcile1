# Module Limits & System Boundary Constraints

**Project:** SmartReconcile  

---

## 1. System Constraints & Boundary Rules

1. **`MOD-ING` (Statement Ingestion):**
   - Maximum upload file size: 50MB per statement.
   - Vision-LLM API timeout: 25 seconds per page slice.
2. **`MOD-DET` (Matching Core Engine):**
   - Maximum batch memory matching chunk: 50,000 transactions per Virtual Thread batch.
   - Delta tolerance for exact match: Absolute 0.0000.
3. **`MOD-AGT` (Agentic AI Resolution):**
   - Maximum AI tool loop iterations: 5 tool calls per discrepancy.
   - Minimum automated proposal confidence threshold: 85% ($S_c \ge 85$).
4. **`MOD-UI` (React Frontend):**
   - Dashboard WebSocket reconnection backoff: 2s, 4s, 8s, 16s, 30s.
