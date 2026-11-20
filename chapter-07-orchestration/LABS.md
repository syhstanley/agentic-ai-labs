# Chapter 07 Labs

## Lab 07.1 — Pattern comparison

用 sequential pipeline 與 manager-worker 各完成「蒐集三份政策並摘要」。記錄 model calls、tool calls、latency、cost、success、trace nodes。

**驗收：** 相同 dataset/rubric；寫出何時簡單 pipeline 更好；不可只比較單次 run。

## Lab 07.2 — Typed handoff

建立 triage → support/billing handoff schema：case_id、summary、evidence IDs、requested action、risk、return condition。禁止傳完整 hidden history。

**驗收：** wrong route、missing field、handoff loop、recipient unavailable、return-to-human 有 tests。[解答](SOLUTIONS.md#072)

## Lab 07.3 — Queue jobs

API 建 job 回 202/job_id；worker lease job、heartbeat、更新 progress；client 可 status/cancel。加入 dead-letter 與 retry schedule。

**驗收：** request 不等待 job；兩 worker 不同時執行同一 lease；cancel 最晚在下一 safe checkpoint 生效。

## Lab 07.4 — Durable execution

每 step transactionally 保存 checkpoint/output hash。用 kill -9 在任意 step 中斷，重啟後 resume。External writes 使用 idempotency/reconciliation。

**驗收：** 20 次隨機 kill 無遺失與 duplicate write；提供 manual repair CLI；terminal runs 不重開。

## Lab 07.5 — Multi-agent review

將單 Agent 方案提出 multi-agent 改版，再做 complexity budget：新增的 latency、cost、failure modes、permissions、observability。只有隔離或明確品質增益才保留。

**章末交付：** onboarding workflow architecture、state table、failure matrix、SLO、runbook，以及「為何不是更多 Agent」。

