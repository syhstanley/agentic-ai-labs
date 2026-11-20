# Section XX.Y — Title

## Objectives

- 完成後能具體做出的事情

## Prerequisites

- 前置章節與工具

## Mental model

用自己的話解釋概念、適用時機與不適用時機。

## Lab

1. 建立最小可運作版本。
2. 加入測試與錯誤案例。
3. 注入至少一種故障。
4. 記錄設計選擇。

## Deliverables

- 原始碼、README、測試、範例輸出、決策紀錄

## Acceptance criteria

- [ ] Happy path 通過
- [ ] Failure path 可預期且不破壞資料
- [ ] 無 secrets 或真實個資
- [ ] 另一個人能依 README 重現

## Debug challenge

說明故障症狀，要求學生從 logs/tests/trace 找到 root cause。

## Reflection

- 哪部分應由 deterministic code 控制？
- 若流量、資料量或權限範圍增加 100 倍，哪裡先壞？

