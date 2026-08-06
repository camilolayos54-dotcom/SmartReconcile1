# Branching & Release Strategy (Deliverable 5)

**Project:** SmartReconcile  
**Document ID:** D5-BRANCHING-STRATEGY  
**Phase:** 2 — Project Kickoff  

---

## 1. Git Workflow Model

The project follows a **Trunk-Based Development with Short-Lived Feature Branches** workflow:

- `main`: Production-ready branch. Continuous deployment to staging/production.
- `feature/*`: Short-lived feature branches created from `main` (lifetime <48 hours).
- `fix/*`: Bugfix branches for hotfixes or patch releases.
- `release/*`: Tagged version releases (e.g., `release/v1.0.0-mvp`).

## 2. Pull Request Rules & Quality Gates

1. Every PR requires at least **1 senior peer code review approval**.
2. Automated CI checks must pass before merging:
   - Java Maven/Gradle build & JUnit test execution (100% pass, >85% coverage).
   - Python Pytest & Flake8/Black linting pass.
   - React Vite build & ESLint pass.
3. No direct commits to `main` branch permitted (enforced by branch protection rules).
