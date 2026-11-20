# Chapter 06 Labs

## Lab 06.1 — Retrieval baseline

建立 30 份合成 IT/HR/Finance 文件與 30 個 queries，每題標 gold document IDs。比較 whole-document、固定字數、heading-aware chunk；計算 recall@3、precision@3。

**驗收：** dataset 固定版本；結果可重跑；分析至少五個 miss，不以單一漂亮 query 下結論。

## Lab 06.2 — RAG pipeline

實作 ingestion manifest（document ID/version/hash/ACL/chunks）與 query pipeline（rewrite/filter/retrieve/rerank/context/answer）。可先用 TF-IDF/keyword，不必立刻買 vector DB。

**驗收：** 回答有 doc/version/chunk citation；沒有 evidence 時 abstain；重新 ingest 相同 hash 不重複。[解答](SOLUTIONS.md#062)

## Lab 06.3 — RAG evals

為每題評 retrieval recall、context precision、answer correctness、citation correctness、abstention。故意移除 gold doc，確認不是產生假引用。

**驗收：** failure 分成 retrieve miss、ranking miss、generation miss、citation miss；建立 regression baseline。

## Lab 06.4 — Memory consent

做 `propose_memory → confirm → persist`；memory 含 subject、fact、source、confidence、created/expiry、sensitivity。支援 list/update/delete。

**驗收：** 未確認不保存；密碼/token/醫療推測永不保存；過期不進 context；刪除後 cache 同步失效。

## Lab 06.5 — ACL/freshness attack

建立 public/support/finance/HR 文件與四種身份。測 query injection、猜 document ID、撤權、刪除、舊 cache、index lag。

**驗收：** unauthorized recall 為 0；ACL 在 retrieval enforce；dashboard 顯示 source-index lag；delete 有 tombstone/reconciliation。

