# Chapter 05 — Model Context Protocol (MCP)

➡️ [開始實作](LABS.md) · [參考解答](SOLUTIONS.md)

目標：能使用、開發及保護 MCP，讓 Agent 以清楚 contract 存取外部工具與資料。

## 05.1 Architecture

Host 是 Agent 應用；client 維護連線；server 暴露 capabilities。常見 capability：

- Tools：可執行動作，例如查 ticket、建立草稿
- Resources：可讀內容，例如 schema、文件、狀態
- Prompts：可重複使用的 prompt template

MCP 是協定，不會自動解決 authentication、authorization、資料品質或安全。

**Lab：** 畫出 Host → MCP client → internal server → database 的 trust boundaries，列出每一段的 identity、protocol、credential、log 與 failure mode。

## 05.2 使用 MCP client

練習檢查 server metadata、列出 tools、閱讀 schema、使用 read-only tool、處理 unavailable/timeout。不要因 server 名稱可信就接受其所有輸出。

**Lab：** 連接本機教學 server，呼叫 `list_tickets`。記錄 request/response schema、latency、錯誤和資料敏感等級。

## 05.3 開發 MCP server

用 Python 或 TypeScript 建立工單 server：

- `search_tickets(query, limit)`：read-only
- `get_ticket(ticket_id)`：read-only
- `draft_ticket(title, body, severity)`：無外部副作用
- `create_ticket(draft_id, approval_id, idempotency_key)`：write

**驗收：** schema test、invalid input、not found、timeout、duplicate request、concurrent calls 全部覆蓋。

## 05.4 Identity、auth 與 permissions

區分 user-delegated identity 與 service identity。Server 必須自己 enforce authorization；不能相信模型說「使用者已核准」。Token scope、tenant、resource ownership 都要驗證。

**Attack lab：** 嘗試用 A 部門身份讀 B 部門 ticket、修改 approval payload、重播 write request。所有攻擊應被拒絕並留下不含秘密的 audit event。

## 05.5 Production hardening

加入 rate limit、timeout、circuit breaker、request size limit、output redaction、schema version、healthcheck、metrics、dependency pinning 與 graceful shutdown。

### Chapter challenge

將工單 MCP dockerize，讓 Chapter 03 agent 使用。提交 threat model、OpenAPI/JSON schemas、contract tests、load test、runbook。

## Exit ticket

- [ ] 能清楚解釋 Skill 是流程、MCP 是外部能力邊界
- [ ] Read 與 write tools 分離，write 支援 dry-run、approval、idempotency
- [ ] Server 在自身邊界驗證身份與授權
- [ ] Client 能安全處理惡意或格式錯誤的 tool output
