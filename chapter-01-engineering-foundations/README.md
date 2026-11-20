# Chapter 01 — Engineering Foundations

目標：能獨立下載 GitHub 專案、理解執行方式、修錯、測試並安全地交付變更。

## 01.1 Python for agents

學習型別、dataclass/Pydantic、exceptions、async/await、context manager、logging、CLI 與 package structure。

**Lab：** 寫 `Ticket` schema 與匯入 CLI，讀取 JSONL、驗證欄位、把壞資料送進 dead-letter file。禁止用模型修正必填欄位。

## 01.2 Git 與 GitHub

學習 clone、branch、commit、diff、merge/rebase、tag、release、issue、PR、Actions。讀陌生 repo 時依序看：license → README → lockfile → entry point → tests → CI → recent issues。

**Lab：** Fork 或建立練習 repo，以三個小 commits 完成功能、測試、文件；開 PR 並自行 review diff。

**供應鏈檢查：** license 能否商用、maintainer 活躍度、release 頻率、known vulnerabilities、install script、transitive dependencies、是否要求過大權限。

## 01.3 HTTP、REST、Webhook、OAuth

掌握 method、status code、header、JSON、pagination、rate limit、timeout、retry、webhook signature；理解 API key、OAuth authorization code、service account 的差異。

**Lab：** 對 mock ticket API 寫 client，支援 pagination、5 秒 timeout、429 backoff、request ID。測試不得呼叫真網路。

## 01.4 SQL 與資料模型

掌握 CRUD、join、transaction、unique constraint、index 與 migration。Agent state、business records、trace 和 audit log 不應混成一張表。

**Lab：** 設計 `runs`、`steps`、`approvals`、`tool_calls` 四張表；用 unique key 阻止重複寫入。

## 01.5 測試與除錯

學 pytest、fixture、mock、unit/integration/contract test，以及從 stack trace、log、最小重現找到 root cause。

**Debug challenge：** client 偶爾建立兩張相同 ticket。不得用 `sleep` 修；找出 retry 與非 idempotent POST 的交互問題。

## 01.6 Linux 與 Docker

學 process、port、permission、signal、stdout/stderr、volume、network、healthcheck 與 image pinning。

**Lab：** 將 mock API 與 client 包成 Compose，加入 non-root user、healthcheck、read-only secret mount。

## Exit ticket

- [ ] 陌生 repo 能在 30 分鐘內列出 entry point、設定、測試與風險
- [ ] API client 通過 timeout、429、500、invalid JSON、pagination 測試
- [ ] 能解釋 transaction、idempotency key 與 retry 的關係
- [ ] Docker container 不以 root 執行且不含 secrets

