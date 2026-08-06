# TASK BE-039 — `pdf_vlm_parser.py`

**Module:** `ai-coprocessor/app/vlm/`  
**File Type:** Python Vision-LLM Parser  
**Priority:** HIGH — Scanned PDF statement table extraction module.  
**Depends On:** `TASK_BE_037`  
**Blocks:** PDF bank statement ingestion  

---

## 1. Purpose

Renders PDF pages to 300DPI PNG images via PyMuPDF, redacts PII data, and extracts table line items using Vision-LLM APIs.

---

## 2. Step-by-Step Implementation Instructions

1. Create `app/vlm/pdf_vlm_parser.py`.
2. Convert PDF pages -> PNG -> Call Vision API -> Parse JSON response table.

---

## 3. Verification Command

```bash
python -m py_compile app/vlm/pdf_vlm_parser.py
```
