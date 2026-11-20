# Chapter 02 Reference Solutions

## 02.1

報告至少要有 `case_id/model/version/correct/latency_ms/input_tokens/output_tokens/cost`。模型選擇不是單一排行榜：簡單任務用便宜模型，風險高或複雜任務才提高能力。

## 02.2

分類 label 由程式 enum 驗證。Injection 只是 user data；模型即使輸出 `VIP` 也會 schema failure，不能進下游。

## 02.3

```python
class Action(BaseModel):
    text: str
    owner: str | None = None
    due_date: date | None = None

class Meeting(BaseModel):
    participants: list[str]
    decisions: list[str]
    actions: list[Action]
    customer_id: str | None = None
```

Schema validity 不代表內容正確；另用 source span 或人工標註檢查 semantic accuracy。

## 02.4

Router 順序：data policy → task support → remaining budget → complexity → latency。Policy 必須最先，否則 fallback 可能把受限資料送往不允許的服務。

## 02.5

Bad retrieval 應檢查 query、metadata filter、index freshness、reranking 和 gold source；加強 prompt 頂多讓模型更自信地使用錯誤 context。

