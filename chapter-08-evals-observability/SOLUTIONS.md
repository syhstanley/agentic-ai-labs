# Chapter 08 Reference Solutions

## 08.1

Dataset 不是隨機聊天紀錄集合。每筆要對應可判斷結果與業務風險；高風險長尾可過度抽樣，但報告需另算真實分布指標。

## 08.2

先 deterministic：JSON valid → route exact/set → tool allowed → args constraints → legal transition。Rubric grader只補充摘要品質；它不能覆蓋未核准 write 等 hard failure。

## 08.3

Duplicate write trace 常見形狀：POST timeout → retry 使用新 idempotency key。修 client key reuse 與 server unique constraint，不是把 timeout 調長就結束。

## 08.4

Baseline 更新應像程式變更：附原因、差異、風險 owner。Known failure 要有 issue/expiry，不能永久排除。

## 08.5

通常先減少無關 context 和 round trips，再降模型。每個優化只改一個變因，否則無法歸因。

