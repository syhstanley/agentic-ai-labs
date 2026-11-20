# Chapter 03 — Tools、Agent Loop 與 Workflow

目標：不依賴框架，親手做出 Agent 如何選工具、執行、觀察結果並結束的核心迴圈。

## 03.1 Function/tool calling

Tool schema 是 Agent 與程式的 contract。名稱、描述、參數、錯誤語意和權限邊界都會影響正確性。

**Lab：** 寫 `search_customer`、`get_ticket`、`draft_ticket` 三個 tools。先只提供 read tools，再比較加入 write tool 後的風險。

## 03.2 Agent loop

最小迴圈：送出 messages + tool schemas → 收到 tool call → 驗證 arguments → 執行 → 回傳 observation → 重複，直到 final answer 或達到上限。

**Lab：** 實作 framework-free loop，必須有 `max_steps`、tool allowlist、per-tool timeout、structured errors、trace ID。另做 scripted fake model 讓測試不用 API。

## 03.3 Workflow 與 state machine

當步驟可預測時，用明確狀態：`RECEIVED → ENRICHED → DRAFTED → WAITING_APPROVAL → EXECUTED/REJECTED/FAILED`。模型只能產生建議事件，不能直接跳狀態。

**Lab：** 把 Chapter 00 的 CRM 流程做成 state machine，測試非法 transition。

## 03.4 Retry、idempotency、compensation

- Retry：暫時性錯誤再試，使用 exponential backoff + jitter。
- Idempotency：同一請求重送不造成重複副作用。
- Compensation：跨系統無法 transaction 時，對已完成動作做補償或人工處理。

**Fault lab：** 在每一步隨機注入 timeout。證明跑 100 次不會建立重複 ticket。

## 03.5 Human-in-the-loop

核准畫面要顯示 proposed action、理由、來源、diff、風險和到期時間；approve 必須綁定當時 payload hash，避免核准後內容被替換。

**Lab：** 實作 dry-run 與 approval token。Email 寄送、資料刪除、金額變更一律等待核准。

## Exit ticket

- [ ] Agent 永遠不會超過最大步數或無限重試
- [ ] 所有 tool arguments 經 schema 與業務規則驗證
- [ ] 重播相同 request 不產生重複副作用
- [ ] 高風險工具需要核准且留 audit record

