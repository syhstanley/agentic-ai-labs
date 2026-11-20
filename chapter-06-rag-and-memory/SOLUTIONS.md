# Chapter 06 Reference Solutions

## 06.1

Heading-aware 通常讓 chunk 語意完整，但答案可能跨段；結論必須來自 dataset。先做 keyword baseline，否則無法證明 embedding 帶來改善。

## 06.2

最小 answer contract：`answer | abstain_reason | citations[{doc_id,version,chunk_id,quote}]`。產出後驗證 quote 確實存在指定 chunk，否則 citation invalid。

## 06.3

Retrieval miss 改 index/query；ranking miss 改 reranker；generation miss 改 context/prompt/model；citation miss 改 contract/validator。不要全部歸因於 prompt。

## 06.4

Memory proposal 不是 memory。只有使用者確認或明確 policy 允許後才 persist；每筆提供 provenance 和 delete handle。

## 06.5

先用身份產生 permitted resource filter，再 retrieval；取回後再 defensive check。Prompt 裡寫「只看有權文件」不是存取控制。

