# Chapter 09 Reference Solutions

## 09.1

高優先例：越權 tool call、跨租戶 retrieval、approval payload substitution、credential leak、dependency compromise。Control 要落在可信邊界，不是只加 prompt。

## 09.2

多層防護：標記 untrusted content、最小 context、schema validation、URL/tool allowlist、least privilege、sandbox、approval、egress control、audit/evals。沒有單一「防 injection prompt」。

## 09.3

Write credential 不提供給 planner/model process；核准後由 isolated executor 依 signed request 取得短期權限。即使 planner 被 injection，也無直接寫入能力。

## 09.4

Audit log 記 `target_id` 和 payload hash，完整敏感 payload 留在原 source of truth。Retention 到期需可驗證刪除，不只 UI 隱藏。

## 09.5

Root cause 應是「不可信文件可控制 unrestricted outbound tool，且缺少 approval/egress policy」，不是「使用者上傳惡意文件」。

