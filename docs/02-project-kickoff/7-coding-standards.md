# Coding Standards & Guidelines (Deliverable 7)

**Project:** SmartReconcile  
**Document ID:** D7-CODING-STANDARDS  
**Phase:** 2 — Project Kickoff  

---

## 1. Java Coding Standards (Backend Core)

- Follow **Google Java Style Guide**.
- Mandatory use of `BigDecimal` for all monetary amounts (never use `float` or `double`).
- Enforce immutability for domain event DTOs using Java `record` types.
- Require Java 21 Virtual Threads (`Executors.newVirtualThreadPerTaskExecutor()`) for I/O operations.

## 2. Python Coding Standards (AI Coprocessor)

- Follow **PEP 8** style guidelines enforced via `Black` and `Flake8`.
- Require explicit type hinting (`typing` module) for all function arguments and return values.
- Enforce Pydantic v2 schemas for all JSON API request/response payloads.

## 3. React & Tailwind Standards (Web UI)

- Functional components only with React Hooks.
- Class naming using **Tailwind CSS** utility classes; modularize repeating styles using custom components.
- ESLint + Prettier configuration for consistent code formatting.
