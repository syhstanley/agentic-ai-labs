# Chapter 06 — RAG、Enterprise Search 與 Memory

目標：建立會引用來源、尊重文件權限、能持續更新且可量測的知識系統。

## 06.1 Embeddings 與 retrieval

理解 chunk、embedding、similarity、top-k、metadata filter、hybrid search、reranking。Embedding 是相關性表示，不是真相或權限系統。

**Lab：** 用 30 份合成公司文件，比較固定 chunk、段落 chunk、metadata filter。建立 20 個 queries 並標記 relevant document IDs。

## 06.2 RAG pipeline

Ingestion：parse → clean → classify → chunk → embed → index。Query：rewrite → retrieve → filter → rerank → compose context → answer。

**Lab：** 實作最小 RAG，回答必須只使用 context；找不到證據時回覆不知道。保存 document version 與 chunk lineage。

## 06.3 Citation 與 retrieval evals

分開測：retrieval recall、context precision、answer correctness、citation correctness、abstention。只看回答「像不像」會掩蓋錯誤來源。

**Lab：** 針對 30 題建立 gold sources，輸出 failure table：沒取回、取回錯誤、模型沒使用、引用錯誤。

## 06.4 Memory

- Working memory：本次 run 狀態
- Conversation memory：對話摘要與歷史
- Semantic memory：經核准保存的使用者／組織事實
- Episodic memory：過去任務及結果

Memory 必須有寫入規則、provenance、TTL、修改及刪除方式；不要自動把每段對話永久保存。

**Lab：** 實作 memory proposal → user confirmation → persist，並支援列出、修正、忘記。

## 06.5 ACL、freshness 與 deletion

檢索前後都要考慮 ACL。原文件權限撤銷或刪除後，index 也必須同步；cache、embedding 與備份都要有 policy。

**Attack lab：** 建立 public、finance、HR 文件。證明不同身份只能取得授權 chunks；query 中要求「忽略權限」不得奏效。

## Exit ticket

- [ ] 每個答案可追溯到文件版本與 chunk
- [ ] 無證據時能 abstain，不編造 citation
- [ ] 權限在 retrieval system enforce，而非 prompt enforce
- [ ] 有 re-index、deletion、staleness monitoring 與 owner

