# Chapter 12 Labs

三個 Capstone 都使用前面相同驗收語言。至少 A 或 B 完整 production-like；C 可作第二作品。

## Lab 12.1 — Knowledge Agent

依 [README](README.md#121-capstone-a--permission-aware-knowledge-agent) 實作。Milestones：dataset/baseline → ingestion/retrieval → ACL/citations → evals/attacks → deploy/operate。

**Demo 必演：** 正常引用、無答案 abstain、跨權限拒絕、惡意文件、撤權/cache、index failure/recovery。

## Lab 12.2 — Operations Agent

Milestones：state/tool contracts → MCP → approval → durable worker → eval/security → deploy。用 fake CRM 開始，最後才接 sandbox service。

**Demo 必演：** happy path、拒絕、payload tamper、duplicate webhook、CRM timeout after success、kill worker/resume。

## Lab 12.3 — Software Delivery Agent

Milestones：sandbox repo → AGENTS/Skills → issue-to-branch → tests/security → PR → injection/evals。不得有 merge 或 production credential 權限。

**Demo 必演：** 正常 issue、惡意 issue、dependency attack、flaky test、錯 branch、human rejection。

## Lab 12.4 — Defense

準備 5 分鐘 executive demo、20 分鐘 technical defense、unknown fault drill。請第三方秘密選三種故障注入。

**驗收：** 不看 source 先用 metrics/trace 定位；安全停止；恢復後補 regression；交 blameless postmortem。

## Submission tree

```text
capstone/
├── README.md              # problem, setup, demo
├── docs/                  # architecture, ADRs, threat model, runbook, ROI
├── src/                   # services/domain/adapters
├── tests/                 # unit, contract, integration, security
├── evals/                 # versioned dataset, graders, report
├── deploy/                # compose/IaC/CI
└── evidence/              # screenshots or sanitized trace/report
```

