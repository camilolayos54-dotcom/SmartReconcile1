# TASK BE-040 — `discrepancy_agent.py` & Tools

**Module:** `ai-coprocessor/app/agent/`  
**File Type:** LangChain Agent Module  
**Priority:** HIGH — Multi-tool AI discrepancy resolution engine (`MOD-AGT`).  
**Depends On:** `TASK_BE_037`, `TASK_BE_033`  
**Blocks:** Automated balancing proposal generation  

---

## 1. Purpose

Consumes Redis discrepancy payloads, executes FX rate lookup, fee schedule verification, and timezone shift tools, and generates step-by-step reasoning logs and double-entry proposals.

---

## 2. Step-by-Step Implementation Instructions

1. Create `app/agent/discrepancy_agent.py` with custom tools (`Tool_FX_Lookup`, `Tool_Fee_Verifier`, `Tool_Timezone_Shift`).
2. Calculate confidence score $S_c$. If $S_c < 85\%$, flag for manual human review.

---

## 3. Verification Command

```bash
python -m py_compile app/agent/discrepancy_agent.py
```
