# TASK OPS-002 — `.github/workflows/ci.yml`

**Module:** `.github/workflows/`  
**File Type:** GitHub Actions Workflow Configuration  
**Priority:** HIGH — Automated CI pipeline running unit tests and builds on PR.  
**Depends On:** `TASK_OPS_001`  
**Blocks:** Continuous integration  

---

## 1. Purpose

Automates Maven `mvn test` execution for Java core and `pytest` execution for Python AI coprocessor on every pull request.

---

## 2. Step-by-Step Implementation Instructions

1. Create `.github/workflows/ci.yml`.
2. Configure parallel jobs for Java 21 JDK build and Python 3.11 test suite.

---

## 3. Verification Command

Validate YAML syntax:
```bash
git check-ref-format
```
