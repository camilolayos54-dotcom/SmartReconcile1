# Domain Glossary (Deliverable 3)

**Project:** SmartReconcile  
**Document ID:** D3-DOMAIN-GLOSSARY  
**Phase:** 3 — Requirements Engineering (Layer 1)  

---

## 1. Domain Terminology Catalog

| Term | Abbreviation | Definition | Technical Context |
|---|---|---|---|
| **Double-Entry Accounting** | Partida Doble | Accounting principle where every debit entry must be matched by a corresponding credit entry, maintaining $Assets = Liabilities + Equity$. | Enforced by `MOD-DET` and `MOD-AGT` to guarantee balance. |
| **Deterministic Matching** | Det-Match | Algorithmic exact matching of transaction line items based on hard rules (Reference ID, exact amount, timestamp window). | Handled by Java 21 engine in <1ms. |
| **Discrepancy Delta** | Delta ($\Delta$) | The mathematical difference between internal ledger amount and bank settlement amount ($Amount_{internal} - Amount_{bank}$). | Evaluated by AI Agent to find root cause. |
| **Agentic AI Coprocessor** | AI-Coproc | Python service using LLMs and tools to investigate non-matching transaction line items and propose auditable adjustments. | Built with FastAPI, LangChain/LlamaIndex, and Vision-LLM. |
| **Unmatched Internal** | UNM-INT | Transaction present in internal database but absent from bank settlement file. | State flag emitted by Java engine. |
| **Unmatched Bank** | UNM-BNK | Transaction line present in bank settlement file but absent from internal database. | State flag emitted by Java engine. |
| **Vision-LLM Parsing** | VLM-Parse | Processing of unstructured scanned PDF bank statements using multimodal Vision-Language Models to extract table rows as JSON. | Handled by Python `MOD-ING` worker. |
| **Journal Adjustment Entry** | JAE | Accounting record proposed by AI to balance a discrepancy (e.g., debiting Bank Fee Expense, crediting Clearing Account). | Output of `MOD-AGT` requiring operator approval. |
