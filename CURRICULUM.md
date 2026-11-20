# Curriculum and competency matrix

## 能力分級

### Level 1 — Operator

能有效使用 AI coding agent，讀懂變更、執行測試、不洩漏秘密。對應 Chapter 00–02。

### Level 2 — Builder

能開發單 Agent、tools、Skill、MCP 與基本 RAG，並處理常見錯誤。對應 Chapter 03–06。

### Level 3 — Production Engineer

能設計 orchestration、evals、observability、安全控制及部署。對應 Chapter 07–10。

### Level 4 — Enterprise Lead

能選題、估算 ROI、跨部門協作、定義治理並帶領 PoC 到 production。對應 Chapter 11–12。

## 52 Sections

| Chapter | Sections |
|---|---|
| 00 | 00.1 Agent vs chatbot vs automation · 00.2 Orchestration · 00.3 工作環境 · 00.4 流程與風險盤點 |
| 01 | 01.1 Python · 01.2 Git/GitHub · 01.3 HTTP/API/OAuth · 01.4 SQL · 01.5 測試 · 01.6 Docker/Linux |
| 02 | 02.1 模型與 token · 02.2 Prompt/context · 02.3 Structured output · 02.4 模型選擇 · 02.5 Failure taxonomy |
| 03 | 03.1 Function calling · 03.2 Agent loop · 03.3 Workflow/state machine · 03.4 Retry/idempotency · 03.5 Human approval |
| 04 | 04.1 AGENTS.md · 04.2 Skill · 04.3 Skill scripts/references · 04.4 Plugin/distribution |
| 05 | 05.1 MCP architecture · 05.2 MCP client · 05.3 MCP server · 05.4 Auth/permissions · 05.5 Production hardening |
| 06 | 06.1 Embeddings/retrieval · 06.2 RAG pipeline · 06.3 Citations/evals · 06.4 Memory · 06.5 ACL/freshness |
| 07 | 07.1 Orchestration patterns · 07.2 Handoffs · 07.3 Queue/long jobs · 07.4 Durable execution · 07.5 Multi-agent tradeoffs |
| 08 | 08.1 Test dataset · 08.2 Deterministic/model graders · 08.3 Tracing · 08.4 Regression gates · 08.5 Cost/latency |
| 09 | 09.1 Threat modeling · 09.2 Prompt injection · 09.3 Least privilege/secrets · 09.4 Audit/privacy · 09.5 Incident response |
| 10 | 10.1 FastAPI/service boundary · 10.2 Persistence/workers · 10.3 Open WebUI · 10.4 CI/CD · 10.5 Reliability |
| 11 | 11.1 Process discovery · 11.2 Integration architecture · 11.3 ROI · 11.4 Adoption/change · 11.5 Productization |
| 12 | 12.1 Knowledge agent · 12.2 Operations agent · 12.3 Software agent · 12.4 Portfolio/defense |

## 畢業判定

你必須能獨立展示以下證據，而不是只說「我學過」：

- 一個 deterministic workflow 與一個 agentic workflow，並能說明為何如此選擇
- 一個自製 MCP server，含 authentication、read/write 分離、schema tests
- 一個 RAG 系統，回答附引用，且不同使用者看不到無權文件
- 至少 30 筆 eval dataset、回歸報告及成本／延遲預算
- threat model、approval policy、audit log、incident runbook
- Docker 化部署、CI gate、監控圖表與 rollback 示範
- 一份包含基準值、節省工時、風險與推廣計畫的企業提案
- Capstone 現場故障注入：API timeout、重複請求、惡意文件、模型輸出格式錯誤

