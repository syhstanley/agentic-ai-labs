# Chapter 11 Labs

## Lab 11.1 — Discovery interview

訪談執行者、主管、IT/security 各一位，觀察五次流程。問具體最近案例、例外、返工、等待、shadow tools；不要問「你想要什麼 AI」。

**驗收：** as-is map、baseline、pain evidence、data/system owners、non-goals；受訪者 review 過摘要。

## Lab 11.2 — Architecture decision

對同一需求比較 SaaS、內建功能、自建 API workflow、Open WebUI、RPA。從 identity、data policy、integration、quality、cost、lock-in、operations 評分。

**驗收：** 寫 ADR，包含 rejected options、assumptions、revisit trigger；不是因流行選框架。

## Lab 11.3 — ROI model

做 low/base/high spreadsheet：volume、minutes saved、review time、error avoided、API/license、infra、build、maintenance、training、risk reserve。

**驗收：** 區分 capacity released 與 cash saving；列 breakeven；敏感度分析指出最關鍵假設。[解答](SOLUTIONS.md#113)

## Lab 11.4 — Pilot/adoption

設計 5–10 人、4 週 pilot：training、champion、support、feedback、usage/quality metrics、stop criteria。做五次 usability test。

**驗收：** 有 control/baseline；量測 override 與 automation bias；pilot 不直接取得全面 production write。

## Lab 11.5 — Productize

將方案拆 discovery、PoC、production、training、support/SLA、quarterly eval/governance。定義 ideal customer、80% common core、20% integration boundary、pricing、responsibility matrix。

**章末：** 10 分鐘 executive pitch + technical appendix，回答「為何不能只買 ChatGPT？」與「出事誰負責？」

