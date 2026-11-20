# Chapter 05 Labs

## Lab 05.1 — MCP trust map

畫 Host → client → MCP server → ticket DB。每條線註明 protocol、identity、credential owner、data classification、timeout、audit owner。

**驗收：** 至少四個 trust boundaries；明確指出 tool description 不是 authorization；列出 server 被入侵情境。

## Lab 05.2 — Inspect an MCP server

使用教學或本機 MCP，列出 tools/resources、schemas、annotations。只啟用 read tools，送 valid、invalid、oversized、timeout requests。

**驗收：** 保存 capability inventory；unknown fields 被拒絕；client 不把 tool output 當 instructions；server unavailable 時安全降級。

## Lab 05.3 — Build ticket MCP

用 Python或 TypeScript 實作 `search_tickets`、`get_ticket`、`draft_ticket`、`create_ticket`。資料先用 SQLite；提供 seed command。

**驗收命令：** contract tests 覆蓋 list/call、bad schema、not found、timeout、duplicate key；create 必須帶 approval 與 idempotency key。[解答](SOLUTIONS.md#053)

## Lab 05.4 — Authentication/authorization

建立 Alice(support) 與 Bob(finance)。Ticket 帶 department。用 middleware 解析可信 identity，query 強制 tenant/department filter。

**攻擊：** Alice 修改 arguments 查 Finance ID、偽造 `approved=true`、重播 Bob 的 request；全部回拒絕且產生 audit event。

## Lab 05.5 — Hardening

加入 request/body limit、rate limit、per-tool timeout、redaction、health/readiness、metrics、schema version、graceful shutdown。做 50 concurrent read calls 和 10 duplicate writes。

**驗收：** p95 與 error rate 報告；log 無 token/body；依賴 DB unavailable 時 readiness false；shutdown 不接受新 write。

