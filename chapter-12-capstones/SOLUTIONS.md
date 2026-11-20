# Chapter 12 Reference Architecture and Rubric

Capstone 沒有唯一 code answer；以下是最低合格 architecture，不能直接複製當設計理由。

## Knowledge Agent

Identity gateway → query service → ACL filter → retriever/reranker → answer contract → citation validator。Ingestion 有 version/hash/tombstone；eval 分 retrieval/generation/security。

## Operations Agent

API → durable state store/queue → planner(read-only) → approval store → isolated write executor → MCP/CRM。Approval 綁 payload；所有外部 write idempotent/reconcilable。

## Software Agent

Issue ingestor → policy gate → isolated ephemeral workspace → coding agent → tests/scanners → diff/PR publisher → human review。Command/network/secret boundaries 由 sandbox enforce。

## Pass rubric

每項 0–4：business fit、architecture、correctness/evals、security/governance、reliability/operations、communication。平均至少 3；security 不得低於 3；任何越權讀取、未核准 write、secret leak 直接重考。

## Fault drill answer pattern

先 stop blast radius → 保存 evidence → 用 correlation ID 找 failing span → 判斷 transient/permanent/policy → 安全恢復／reconcile → 加 regression → postmortem。禁止在不知 state 時直接重跑整個 workflow。

