# TASK BE-037 — Python Coprocessor Setup (`pyproject.toml`, `requirements.txt`, `main.py`)

**Module:** `ai-coprocessor/`  
**File Type:** Python Project Setup & Entry Point  
**Priority:** HIGH — Initializes FastAPI & gRPC Python worker service.  
**Depends On:** Python 3.11  
**Blocks:** All Python parsing and AI agent modules  

---

## 1. Purpose

Sets up Python FastAPI server and gRPC stubs loader for Vision-LLM bank statement parsing and agentic investigations.

---

## 2. Step-by-Step Implementation Instructions

1. In `ai-coprocessor/`, create `requirements.txt` with `fastapi`, `uvicorn`, `grpcio`, `protobuf`, `langchain`, `pymupdf`.
2. Create `main.py` launching FastAPI on port `8001` and gRPC servicer on port `9091`.

---

## 3. Verification Command

```bash
python -m py_compile main.py
```
