# TASK BE-038 — `statement_parser.py` & `template_engine.py`

**Module:** `ai-coprocessor/app/parser/`  
**File Type:** Python Module  
**Priority:** HIGH — Fast deterministic regex/CSV parser (`MOD-ING-TPL`).  
**Depends On:** `TASK_BE_037`  
**Blocks:** Statement ingestion pipeline  

---

## 1. Purpose

Parses CSV and MT940 bank statement files in <100ms using cached regex schemas from `MOD-ING-TPL` at zero AI cost.

---

## 2. Step-by-Step Implementation Instructions

1. Create `app/parser/template_engine.py` matching header signatures against regex rules.
2. Return clean transaction objects.

---

## 3. Verification Command

```bash
python -m py_compile app/parser/statement_parser.py
```
