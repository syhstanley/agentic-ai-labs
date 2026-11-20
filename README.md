# Agentic AI Labs 🤖

一套以企業落地為目標、從 AI 工具使用者成長為 Agentic AI Engineer 的實作課程。

你不只會「叫模型做事」，而會學會把真實公司流程拆解成可測試的系統，接上資料與工具，加入權限、核准、評測、監控與部署，最後用成果證明商業價值。

> 專家不是記住所有框架，而是能在需求不完整、資料混亂、工具會失敗且有資安限制時，仍設計出可靠方案。

## 你最後會具備的能力

- 用 Python、Git、API、SQL、Docker 組裝可維護的服務
- 理解 model、prompt、context、tool、memory、workflow、agent 的邊界
- 實作 tool-calling loop、狀態機、handoff、重試、人工核准與補償動作
- 撰寫 AGENTS.md、Skill、Plugin，開發與保護 MCP server
- 建立 RAG、企業文件權限、短期與長期記憶
- 用 evals、traces、metrics 衡量品質、成本、延遲及安全性
- 防範 prompt injection、資料外洩、越權操作與供應鏈風險
- 部署 FastAPI、worker、database、Open WebUI 與 CI/CD
- 訪談流程、估算 ROI，將內部工具變成可重複銷售的解決方案

## Agent orchestration 到底是什麼？

Orchestration（編排）就是管理 Agent 完成任務的整段流程：

```text
使用者需求
   ↓
分類與風險檢查
   ↓
規劃下一步 ──→ 呼叫工具 ──→ 驗證結果
   ↑                           │
   └──── 失敗重試／改走替代路徑 ┘
   ↓
高風險動作等待人工核准
   ↓
執行、記錄、評測、回覆
```

例如「整理會議並更新 CRM」不是一個 prompt，而是：讀逐字稿 → 抽取客戶與待辦 → 驗證客戶編號 → 草擬 CRM 變更 → 人工核准 → 寫入 CRM → 失敗重試 → 留下 audit log。決定這些步驟、狀態、工具、權限和失敗路徑，就是 orchestration。

## 課程地圖

| 階段 | Chapter | 主題 | 完成作品 |
|---|---:|---|---|
| 起點 | [00](chapter-00-orientation/) | Agent、workflow、orchestration 與環境 | 第一張流程圖與風險表 |
| 基礎 | [01](chapter-01-engineering-foundations/) | Python、Git、API、SQL、測試、Docker | 可測試的 API client |
| 基礎 | [02](chapter-02-llm-foundations/) | LLM、prompt、structured output、context | 結構化資訊抽取器 |
| 核心 | [03](chapter-03-tools-and-workflows/) | Tool calling、agent loop、狀態機、核准 | 不依賴框架的 Agent loop |
| 核心 | [04](chapter-04-skills-and-plugins/) | AGENTS.md、Skill、Plugin、版本管理 | 公司 SOP Skill |
| 核心 | [05](chapter-05-mcp/) | MCP client/server、tools、resources、auth | 內部工單 MCP server |
| 核心 | [06](chapter-06-rag-and-memory/) | Embedding、retrieval、RAG、memory、ACL | 有引用及權限的知識助理 |
| 進階 | [07](chapter-07-orchestration/) | Handoff、多 Agent、queue、長任務 | 可恢復的多步工作流 |
| 進階 | [08](chapter-08-evals-observability/) | Dataset、grader、trace、成本與回歸 | 自動化品質閘門 |
| 進階 | [09](chapter-09-security-governance/) | Injection、least privilege、audit、治理 | Agent threat model |
| 生產 | [10](chapter-10-platform-deployment/) | FastAPI、DB、worker、Open WebUI、CI/CD | 可部署的 Agent service |
| 商業 | [11](chapter-11-enterprise-product/) | 系統整合、需求訪談、ROI、導入 | 企業導入提案與 PoC |
| 畢業 | [12](chapter-12-capstones/) | 三個企業級 Capstone | 可面試／接案作品集 |

完整能力對照與每節產出請看 [CURRICULUM.md](CURRICULUM.md)，學習紀錄請複製 [PROGRESS.md](PROGRESS.md)。

## 建議用法

1. 依序完成 Chapter 00–03，不要跳過底層實作。
2. 每個 Section 先自行完成，再請 Coding Agent review；不要直接要求它代做。
3. 每章把成果放在該章的 `work/` 目錄，附上 README、測試和決策紀錄。
4. 所有驗收條件通過才勾選進度。
5. Chapter 04–06 完成後可開始做小型公司 PoC；Chapter 08–10 完成後才適合接觸正式資料和寫入權限。

每週 8–10 小時約需 8–12 個月。進度快慢不重要，能否在沒有答案的情況下除錯、驗證與說明取捨才重要。

## Quick start

本課程範例使用 Python 3.11+。若已安裝 `uv`：

```bash
git clone https://github.com/syhstanley/agentic-ai-labs.git
cd agentic-ai-labs
uv run --python 3.11 --extra dev pytest
```

沒有 `uv` 時，可用系統的 Python 3.11+ 建立 virtual environment，再執行 `pip install -e '.[dev]'`。先從 [Chapter 00](chapter-00-orientation/) 開始，不需要 API key。

## 成本與帳號

前半課程可以用 mock model 完成。需要雲端模型的 Lab 會明確標示，請設定 `.env`，不要把 API key commit。Open WebUI、local model 與雲端 API 都會練習，課程不要求只用一家供應商。

## 官方核心參考

- [OpenAI — Building agents](https://developers.openai.com/tracks/building-agents)
- [OpenAI — Codex customization](https://learn.chatgpt.com/docs/customization/overview)
