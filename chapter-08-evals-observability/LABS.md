# Chapter 08 Labs

## Lab 08.1 — Build an eval dataset

建立 50 筆 ticket cases：normal 20、edge 10、historical failures 10、adversarial 10。欄位含 expected route、allowed tools、forbidden actions、risk、tags；保留 20% holdout。

**驗收：** case IDs 穩定；無 production 個資；分布與選樣理由有文件；調 prompt 時不可偷看 holdout。

## Lab 08.2 — Layered graders

實作 schema、route、tool allowlist、argument、state transition、citation graders；最後才加 rubric/model grader 評語意品質。

**驗收：** grader 本身有 unit tests；人工抽查 20 筆校準 model grader；critical safety failure 單獨阻擋。[解答](SOLUTIONS.md#082)

## Lab 08.3 — Trace a run

為 run/model/tool/HTTP/database 建 nested spans，記 version、duration、status、token/cost、retry、correlation ID。對 body 採 allowlist/redaction。

**任務：** 從 trace 找出一次 bad retrieval 和 duplicate write root cause，不准只靠最終回答。

## Lab 08.4 — CI regression gate

Push 時跑 10-case smoke；nightly 跑完整 50 cases。比較 baseline：task success 不可降 2%、unsafe actions 必須 0、p95/cost 不超 budget。

**驗收：** 故意破壞 prompt 會擋 PR；report 顯示 case/tag/component；可更新 baseline 但需 review reason。

## Lab 08.5 — Optimize with evidence

嘗試 context trimming、parallel I/O、cache、model routing，逐項跑相同 eval。提交 before/after 的品質、p50/p95、cost/run。

**驗收：** 不以 safety/accuracy 顯著下降換成本；cache key 包含 identity/document version；結論含 confidence/樣本數。

