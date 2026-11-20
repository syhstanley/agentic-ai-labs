# Chapter 02 — LLM Application Foundations

➡️ [開始實作](LABS.md) · [參考解答](SOLUTIONS.md)

目標：把模型當成有機率、會失敗、需要驗證的元件，而不是資料庫或規則引擎。

## 02.1 Model、token、latency、cost

理解 input/output token、context window、reasoning、temperature、streaming、rate limit。建立 model routing 表：任務複雜度、品質需求、延遲上限、成本上限、資料政策。

**Lab：** 對同一個分類任務比較至少兩種模型或 mock policy，記錄正確率、p50/p95 latency、每 1,000 件估算成本。

## 02.2 Prompt 與 context engineering

把 instructions、user data、retrieved context、tool results 分離。提供清楚目標、限制、輸出 schema、edge cases；不要用 prompt 取代權限控制。

**Lab：** 做客服意圖分類器。建立 30 筆含模糊、錯字、prompt injection 的資料，不可只測三個漂亮例子。

## 02.3 Structured output

用 JSON Schema/Pydantic 驗證輸出，區分 parse failure、schema failure、semantic failure。金額、日期、ID 必須再由程式驗證。

**Lab：** 從會議文字抽取 `customer_id?`、participants、decisions、actions、due_date。缺值保持 `null`，禁止猜測。

## 02.4 Model routing 與 fallback

設計 cheap-first、complexity routing、fallback、timeout budget。Fallback 不等於無限重試；資料政策可能禁止跨供應商。

**Lab：** 實作 router，簡單分類走小模型，複雜抽取走強模型；達到 cost budget 後安全停止。

## 02.5 Failure taxonomy

建立分類：hallucination、instruction miss、bad retrieval、wrong tool、bad arguments、tool failure、loop、unsafe action、stale data、format error。不同 failure 需要不同修法。

### Chapter challenge

交付一個 `meeting_extractor` package，含 schema、30+ case dataset、tests、錯誤報告及成本估算。測試資料不得含真實客戶資訊。

## Exit ticket

- [ ] 不靠人工目視即可驗證輸出格式
- [ ] 能區分 prompt 問題、資料問題、model 問題與 tool 問題
- [ ] 不會把模型輸出直接當 SQL、shell、URL 或權限決策
- [ ] 有明確 timeout、token 與成本上限
