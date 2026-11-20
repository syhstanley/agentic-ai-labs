# Chapter 00 Labs

建立 `work/` 後完成四份 Markdown。這章不寫 Agent，先學會選對問題。

## Lab 00.1 — Agent or not?

**示範：** 「每天 09:00 匯出固定報表」是 automation；「閱讀客訴後選擇查訂單、退款政策或轉主管」才有 agentic decision。

**任務：** 在 `work/opportunity-map.md` 列 12 個工作，欄位為 `frequency`、`minutes`、`input`、`action`、`semantic_uncertainty(1-5)`、`impact(1-5)`、`recommended_pattern`。Pattern 只能是 rule、automation、copilot、agent。

**驗收：** 至少三個任務被判定「不該用 Agent」；高 impact 任務有人工核准；每項有理由。

**Debug Challenge：** 主管要求「所有流程都用 multi-agent」。寫 150 字反駁並提出較安全版本。

**Hints：** 先問步驟是否固定；再問錯一次會不會造成外部損失。[解答](SOLUTIONS.md#001)

## Lab 00.2 — 畫出 orchestration

**示範：** `RECEIVED → EXTRACTED → DRAFTED → WAITING_APPROVAL → EXECUTED`。模型可以抽取內容，但不能自行偽造 `APPROVED` 事件。

**任務：** 在 `work/crm-flow.md` 用 Mermaid 畫會議紀錄更新 CRM 的 sequence diagram 和 state diagram。加入 timeout、客戶不存在、拒絕、重複 webhook、寫入成功但通知失敗。

**驗收：** 每個 state 有 owner、input、output、timeout、retry、terminal condition；write 前有 approval；重試不重複寫入。

**Debug Challenge：** CRM 已寫入但通知失敗，整個 run 應算失敗嗎？提出狀態與補償策略。

**Hints：** 把 business action 與 notification 分開記錄。[解答](SOLUTIONS.md#002)

## Lab 00.3 — 練習機健檢

依序執行並把輸出摘要寫入 `work/environment.md`：

```bash
pwd; git --version; gh auth status
uv --version; docker --version; docker compose version
uv run --python 3.11 --extra dev pytest
```

建立 `.env`，只放假值 `DEMO_TOKEN=not-a-real-token`，確認 `git status` 不會列出它。

**驗收：** 測試通過；能說明 `.env.example` 和 `.env` 差異；沒有把 credential 貼進報告。

**Debug Challenge：** `python` 不存在但 `python3` 存在。說明為什麼課程用 `uv run --python 3.11`。

## Lab 00.4 — Problem brief

訪談一位使用者或模擬「內部 IT 工單分流」。在 `work/problem-brief.md` 寫：問題、使用者、as-is steps、每月件數、平均時間、錯誤率、非目標、資料、風險、PoC scope、success metrics。

**驗收：** 指標有 baseline 與 target；PoC 可在兩週驗證；沒有用「做一個聊天機器人」當問題描述。

**章末口試：** 用兩分鐘說明 Agent、workflow、orchestration 的差異，不可使用「比較聰明」作解釋。

