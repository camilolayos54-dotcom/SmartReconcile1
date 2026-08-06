# Deliverable 7: API Contracts (OpenAPI 3.0 Specification) [MODULE: MOD-UI & SYSTEM-WIDE]

**Module Code:** `MOD-UI` / System OpenAPI  
**Document ID:** D7-OPENAPI-SPECIFICATION  
**Phase:** 6 — Technical Design (Tier 1 Backend Blueprints)  

---

## 1. OpenAPI 3.0 YAML Contract Specification

```yaml
openapi: 3.0.3
info:
  title: SmartReconcile Core REST API
  description: Official REST API for SmartReconcile React Web UI and Operations Integration.
  version: 1.0.0
servers:
  - url: http://localhost:8080/api/v1
    description: Local Development Server

paths:
  /auth/login:
    post:
      summary: User Authentication Login
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [email, password]
              properties:
                email:
                  type: string
                  example: analyst@fintech.com
                password:
                  type: string
                  example: SecretPassword123!
      responses:
        '200':
          description: Authentication Successful (Sets HttpOnly Cookie)
          headers:
            Set-Cookie:
              schema:
                type: string
                example: access_token=jwt_token; HttpOnly; Secure; SameSite=Strict

  /ingest/upload:
    post:
      summary: Upload Bank Statement File (CSV/PDF)
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  type: string
                  format: binary
                bank_account_id:
                  type: string
                  format: uuid
      responses:
        '200':
          description: File Ingested Successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  batch_id:
                    type: string
                    format: uuid
                  total_rows:
                    type: integer
                  template_matched:
                    type: boolean

  /discrepancies/{id}/approve:
    post:
      summary: Approve AI Discrepancy Adjustment Proposal
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
        - name: X-CSRF-TOKEN
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Proposal Approved & Journal Entry Posted
          content:
            application/json:
              schema:
                type: object
                properties:
                  discrepancy_id:
                    type: string
                  status:
                    type: string
                    example: RESOLVED_APPROVED
                  audit_hash:
                    type: string
                    example: 0x7f8a3b...
```
