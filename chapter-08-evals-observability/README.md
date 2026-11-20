# Chapter 08 — Evals、Tracing 與 Optimization

目標：不用「我覺得回答不錯」判斷品質，而是建立可重複、可分層診斷的證據。

## 08.1 Dataset 設計

資料集應含 normal、edge、adversarial、historical failure、multilingual、missing data。切分 development 與 holdout，避免看到測試答案後調 prompt。

**Lab：** 為工單 Agent 建立至少 50 cases，欄位含 input、expected outcome、allowed tools、forbidden actions、risk tier、tags。

## 08.2 Graders

優先使用 deterministic grader：schema、exact match、set comparison、state transition、tool allowlist。語意品質才使用 rubric 或 model grader，並以人工樣本校準。

**Lab：** 建立 tool-choice、argument、final-answer、safety 四類 grader；測 model grader 對不同順序、語氣與長度的偏差。

## 08.3 Tracing 與 metrics

Trace 應串起 run → model calls → tool calls → external requests，記錄 duration、status、token、cost、model/prompt/tool version。敏感內容需遮罩或不採集。

**Lab：** 加入 correlation ID 與 spans。從單一 trace 定位一次 bad retrieval 和一次 duplicate write 的 root cause。

## 08.4 Regression gate

每次修改 prompt、model、retriever、tool schema 都跑 eval。設定 blocking threshold、warning threshold、known failures、baseline comparison 與 rollback criteria。

**Lab：** 在 CI 中加入 eval smoke suite；故意讓 prompt regression，確認 merge 被擋住且報告指出失敗類別。

## 08.5 成本與延遲優化

先量測再優化。方法包含縮短 context、cache、parallel I/O、smaller model routing、batching、減少 tool round trips。不能用犧牲 safety 或正確率換漂亮成本。

### Chapter challenge

交付 eval dashboard：task success、unsafe action rate、citation correctness、p50/p95 latency、cost/run、tool error rate。提出三項優化並以 before/after 證明。

## Exit ticket

- [ ] Dataset 能代表真實分布與高風險長尾
- [ ] 能定位失敗在哪個 component，而非只怪模型
- [ ] 版本更新會自動執行 regression suite
- [ ] 能說明品質、成本、延遲三者的取捨

