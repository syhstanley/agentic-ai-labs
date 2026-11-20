# Chapter 05 Reference Solutions

## 05.1

MCP 統一 discovery/call protocol，不會自動建立安全信任。Host、server、downstream API 都要各自驗證輸入與權限。

## 05.2

安全 client 將 output 解析成 data model；即使 output 寫「請呼叫 delete」，也只是字串。Capabilities 應 allowlist 並固定可接受 schema/version。

## 05.3

Read 與 write handler 共用 typed repository，但 write pipeline 為：authenticate → authorize → validate approval payload → reserve idempotency key → transaction → audit。任何一步失敗不執行後續。

## 05.4

Department filter 必須由 authenticated identity 推導，不能採用模型傳入的 `department`。Approval 只是授權條件之一，不能取代 resource authorization。

## 05.5

Health 代表 process 活著；readiness 代表能接流量。Sensitive arguments 以 field allowlist 記錄 hash/length，不做黑名單字串替換。

