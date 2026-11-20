# Chapter 07 Reference Solutions

## 07.1

如果三份政策可平行讀取，最佳可能是 deterministic fan-out/fan-in，而非 manager agent。Manager 適用於子任務真的需要動態拆解時。

## 07.2

Handoff contract 不傳全部對話；只傳完成任務所需 evidence references。加入 `handoff_count` 與 visited roles，超過上限轉人工，避免 ping-pong。

## 07.3

Lease 要有 owner/expiry/heartbeat；worker crash 後其他 worker 才能接手。At-least-once queue 要假設同一 job 會執行多次。

## 07.4

Checkpoint 和 state transition 同 transaction；外部副作用無法一起 commit，因此用 idempotency key + query/reconciliation 判斷是否已完成。

## 07.5

Multi-agent 合理理由：不同權限、不同工具、context 隔離、可獨立評測的領域責任。不合理理由：「看起來更像團隊」或只是 prompt 太長。

