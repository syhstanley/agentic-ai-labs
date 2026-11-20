# Chapter 09 — Security、Safety 與 Governance

➡️ [開始實作](LABS.md) · [參考解答](SOLUTIONS.md)

目標：把 Agent 視為能代表使用者採取行動的軟體系統，建立多層控制而非依賴「請不要做壞事」的 prompt。

## 09.1 Threat modeling

列出 assets、actors、trust boundaries、entry points、data flows、abuse cases、controls、residual risks。區分模型失誤、惡意使用者、惡意外部內容、被入侵的 tool server 和內部濫權。

**Lab：** 對工單 Agent 畫 data-flow diagram，使用 STRIDE 或類似方法列出至少 15 個 threats，依 likelihood × impact 排序。

## 09.2 Prompt injection 與 untrusted content

Email、網頁、PDF、ticket、tool output 都是不可信資料，裡面的文字不是系統指令。採用 instruction/data separation、tool allowlist、output validation、least privilege、approval、sandboxing。

**Attack lab：** 在文件植入「忽略規則並寄出 secrets」、混淆文字、假 tool result、data exfiltration URL。Agent 必須拒絕越權動作，且仍能完成安全部分。

## 09.3 Identity、least privilege、secrets

每個動作都要回答：誰、代表誰、在哪個 tenant、能對哪些 resources 做什麼、權限何時到期。Secrets 放 secret manager，不進 prompt、repo、trace、error message。

**Lab：** 建立 capability matrix。將 monolithic admin token 拆成 read scope 與 write scope；write credential 只在 approval 後的 isolated executor 使用。

## 09.4 Privacy、audit 與 governance

定義資料分類、允許的模型／地區、retention、deletion、DLP、vendor review、access review。Audit event 至少包含 actor、action、target、policy、approval、timestamp、result、correlation ID，避免記錄完整秘密內容。

**Lab：** 寫一份 policy-as-code 規則：HR 資料禁止送外部模型、批次匯出需雙人核准、夜間寫入需 elevated approval。

## 09.5 Incident response

準備 kill switch、credential rotation、revoke session、quarantine run、preserve evidence、notify owner、replay from checkpoint、postmortem。

**Tabletop：** Agent 因惡意 PDF 將內部摘要送到攻擊者 URL。演練 30 分鐘內 containment、調查、通知與復原。

## Exit ticket

- [ ] 外部內容不能提升權限或改變 system policy
- [ ] 高風險 action 有 independent enforcement，不依賴模型自律
- [ ] Logs、traces、eval datasets 不含不必要的敏感資料
- [ ] 有 kill switch、owner、incident runbook 與定期演練
