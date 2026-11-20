# Chapter 10 Labs

## Lab 10.1 — Agent service API

用 FastAPI 或同等框架實作 `POST /runs`、`GET /runs/{id}`、`POST /approve`、`POST /cancel`。Route 只做 auth/validation；domain service 管 state；adapter 接 tools/models。

**驗收：** OpenAPI/contract tests；202 + job ID；typed errors；tenant isolation；request/correlation IDs。[解答](SOLUTIONS.md#101)

## Lab 10.2 — Database + worker

Compose 啟動 API、PostgreSQL、worker。Migration 管 schema；job/approval 持久化；worker crash 後 lease 恢復；dead letter 可重送。

**驗收：** 重建 containers 資料仍在；backup restore 實測；20 次 duplicate request 一個 business result。

## Lab 10.3 — Open WebUI integration

把 Open WebUI 或相容 chat UI 接到 service，顯示 citation、tool activity、run state、approval diff。UI 不持有 write credential。

**驗收：** 隱藏按鈕後直接呼叫 API 仍會被 backend 拒絕；身份傳遞可追溯；選錯 tenant 不洩漏資料。

## Lab 10.4 — CI/CD

Pipeline：lint → unit → contract → eval smoke → dependency/image scan → build immutable image → staging smoke → approval → deploy。產生 SBOM/checksum/version。

**驗收：** 壞 eval 擋 merge；production 不能用 floating `latest`；演練 rollback 到前版且 DB migration 相容。

## Lab 10.5 — Reliability

定義 SLO 與 dashboard：availability、task success、unsafe rate、p95、queue age、tool errors、cost。加入 timeout budget、circuit breaker、capacity/load test、on-call runbook。

**驗收：** 依賴服務故障時不 cascading；readiness 正確；告警可行動；執行一次 chaos + restore drill。

