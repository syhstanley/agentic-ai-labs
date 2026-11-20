# Chapter 07 — Advanced Orchestration

➡️ [開始實作](LABS.md) · [參考解答](SOLUTIONS.md)

目標：設計可恢復、可觀察、可控的多步驟 Agent 工作流，而非堆疊更多 Agent。

## 07.1 常見 orchestration patterns

- Sequential pipeline：A 輸出給 B
- Router：根據意圖或風險選路徑
- Parallel fan-out/fan-in：多來源同時查詢後合併
- Evaluator-optimizer：產生、評估、有限次修訂
- Manager-worker：管理者拆工作，worker 執行
- Event-driven state machine：事件推動持久狀態

**Lab：** 對相同研究任務各用 pipeline 與 manager-worker 實作，比較品質、成本、trace 複雜度與 failure surface。

## 07.2 Handoff 與 context boundaries

Handoff 是把控制權、instructions、tools 和必要 context 交給另一角色。只傳最小必要資訊；用 schema 交接，不要把整段 hidden history 無限制轉送。

**Lab：** 建立 triage → billing/support agent handoff。測錯誤路由、跨部門資料洩漏、handoff loop、回到人工。

## 07.3 Queue 與長任務

Web request 不應等待十分鐘。使用 job ID、queue、worker、heartbeat、lease、progress events、cancel、deadline 與 dead-letter queue。

**Lab：** 將文件處理改成 async job。Client 重送、worker crash、job cancel、依賴服務 30 分鐘 unavailable 都要有定義結果。

## 07.4 Durable execution

每個 step 完成後保存 checkpoint；重啟從安全位置恢復。區分 at-most-once、at-least-once、effectively-once。外部副作用要用 idempotency 或 reconciliation。

**Chaos lab：** 在任意 step kill worker，再啟動後不得遺失 run 或重複寄信。加入 manual repair command。

## 07.5 多 Agent 的取捨

多 Agent 適合權限、工具、領域或 context 確實需要隔離時。若只是 prompt 很長，先改善模組化。每多一個 Agent 都增加 latency、cost、non-determinism、debug difficulty。

### Chapter challenge

做「新客戶 onboarding」流程：文件檢查、風險分類、CRM 草稿、人工核准、建立任務、通知。附 BPMN/sequence diagram、state schema、failure matrix、SLO。

## Exit ticket

- [ ] 每個 run 可 pause、resume、cancel、inspect
- [ ] Handoff 有 typed contract 與 context minimization
- [ ] Worker crash 不造成資料遺失或重複副作用
- [ ] 能用數據辯護為何需要或不需要 multi-agent
