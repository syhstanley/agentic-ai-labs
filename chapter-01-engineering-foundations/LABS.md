# Chapter 01 Labs

所有程式放 `work/`，至少使用 Python 3.11、type hints、pytest。

## Lab 01.1 — Python validation CLI

**示範輸入：** `{"id":"T-1","title":"VPN fails","severity":2}`。建立 `Ticket`，拒絕空 title、severity 不在 1–5、未知欄位。

**任務：** 寫 `ticket_import.py INPUT.jsonl --valid valid.jsonl --dead-letter bad.jsonl`；逐行處理，單筆錯誤不可中止整批；log 不輸出完整內容。

**驗收：** 10 筆混合資料產生 7 valid/3 bad；exit code 與 summary 正確；`pytest` 覆蓋 boundary。[解答](SOLUTIONS.md#011)

## Lab 01.2 — Git/GitHub workflow

建立 `lab/01-engineering` branch，分成 `feat`、`test`、`docs` 三個 commits。用 `git diff main...HEAD` review，再開 PR。

**驗收：** 不使用 `git add .`；commit 可獨立理解；PR 有動機、測試證據、風險、rollback。

**Debug Challenge：** 假設 secrets 出現在上一個 commit；只刪目前檔案為何不夠？寫處置步驟。

## Lab 01.3 — Resilient HTTP client

**任務：** 對 fake transport 寫 `TicketClient.list_all()`，處理 pagination、2 秒 timeout、429 `Retry-After`、最多三次 5xx retry、invalid JSON；每次帶 request ID。

**驗收：** 測試不連外網；400 不 retry、429/503 才 retry；重試使用 injectable sleeper，測試不真的等待。[解答](SOLUTIONS.md#013)

## Lab 01.4 — SQL state model

用 SQLite 建 `runs`、`steps`、`tool_calls`、`approvals`。加入 foreign keys、timestamps、status check、`(run_id,idempotency_key)` unique constraint。

**驗收：** migration 可重跑或明確拒絕；重複 idempotency key 不產生第二筆；transaction rollback 測試通過。

## Lab 01.5 — Test pyramid

對 importer/client/database 各寫 unit tests；另寫一個從 JSONL → validation → database 的 integration test，以及 API response contract test。

**驗收：** 至少 15 tests；測行為而不是 private implementation；故意破壞 validation 時測試會失敗。

## Lab 01.6 — Docker

建立 Dockerfile 與 Compose：non-root user、pinned base、healthcheck、read-only filesystem、volume 放資料、環境變數注入設定。

```bash
docker compose build
docker compose up -d
docker compose ps
docker compose logs --no-log-prefix
```

**驗收：** image 不含 `.env`；container user 不是 root；SIGTERM 後正常結束；重建 container 資料仍在。

