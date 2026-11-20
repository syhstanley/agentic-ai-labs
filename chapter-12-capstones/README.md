# Chapter 12 — Enterprise Capstones

➡️ [開始實作](LABS.md) · [參考解答與評分基準](SOLUTIONS.md)

目標：用三種不同風險輪廓的作品證明完整能力。至少完成一個，三個都完成才算走完 expert track。

## 12.1 Capstone A — Permission-aware Knowledge Agent

### Scenario

員工詢問 HR、IT、Finance 文件。回答必須有 citations，尊重部門 ACL，文件更新或撤銷要同步。

### Required features

- ingestion、versioning、hybrid retrieval、reranking
- identity-aware filtering、abstention、citation validation
- admin re-index/delete、freshness dashboard
- 50+ eval cases，含跨權限與 prompt injection

### Failure injection

過期政策、同名文件、惡意 PDF、撤權後 cache、vector DB unavailable。

## 12.2 Capstone B — Human-approved Operations Agent

### Scenario

讀取客戶會議紀錄，查 CRM，草擬更新與後續工單；主管核准後才寫入及通知。

### Required features

- MCP read/write tools、OAuth 或模擬 delegated identity
- durable state machine、queue、retry、idempotency、compensation
- approval payload hash、expiry、deny/edit flow、audit log
- cost/latency/task-success dashboard、kill switch

### Failure injection

CRM 429、核准後資料變更、worker crash、重複 webhook、部分寫入、惡意逐字稿。

## 12.3 Capstone C — Software Delivery Agent

### Scenario

Agent 接收 issue，在 sandbox branch 修改程式、執行 tests/security checks、產生 PR；禁止直接 merge 或接觸 production secrets。

### Required features

- repo-specific AGENTS.md、至少兩個 Skills、自製或既有 GitHub MCP
- isolated workspace、command allow/deny policy、network policy
- test selection、diff review、eval dataset、PR summary
- human review gate、trace redaction、artifact retention

### Failure injection

Issue 內 prompt injection、惡意 dependency、測試要求秘密、超大 repo、flaky test、錯誤 branch。

## 12.4 Portfolio 與 defense

每個 Capstone 必須包含：

1. Problem brief、baseline、非目標與成功指標
2. Architecture、data flow、state machine、threat model
3. ADR：為何選 workflow/agent、model、MCP、RAG、UI、deployment
4. 可重現的 setup、seed data、tests、eval report
5. Demo script：happy path、failure path、attack path、recovery path
6. Runbook、SLO、cost model、ROI、90-day rollout
7. 五分鐘非技術介紹與二十分鐘 technical defense

## Expert practical exam

找一位同事或朋友在你不知道的 step 注入三個故障。你必須只依 dashboard、logs、traces 和 run state 定位問題，安全恢復，然後寫 blameless postmortem。

### 評分

| 面向 | 權重 |
|---|---:|
| Business fit 與 ROI | 15% |
| Architecture 與 orchestration | 20% |
| Correctness 與 evals | 20% |
| Security、privacy、governance | 20% |
| Reliability、deployment、operations | 15% |
| Documentation、demo、communication | 10% |

任何一項 safety-critical violation（越權讀取、未核准寫入、洩漏 secrets）都不能以其他分數抵銷，修正並重新測試後才能通過。
