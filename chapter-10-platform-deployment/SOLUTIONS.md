# Chapter 10 Reference Solutions

## 10.1

API 不同步等待 Agent 完成；建立 run 後回 202。Approval endpoint 接 `run_id + proposal_hash + decision`，domain layer 驗 transition，executor 再驗權限。

## 10.2

Database 是 state source of truth；queue 只傳 job ID。Worker 讀目前 state 後決定是否可執行，不能相信過期 queue payload。

## 10.3

Open WebUI 是體驗層，不是 policy enforcement point。Backend 用 authenticated identity/tenant 再檢查每次 retrieval/tool action。

## 10.4

Rollback 不一定是舊 code 配舊 DB；migration 採 expand/contract，先向後相容，再移除舊欄位。

## 10.5

SLO 示例：月 task success 99%、unsafe write 0、p95 interactive <15s、queue age p95 <2m。Unsafe action 是 hard invariant，不可用 availability 抵銷。

