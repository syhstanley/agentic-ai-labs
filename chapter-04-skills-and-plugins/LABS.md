# Chapter 04 Labs

## Lab 04.1 — AGENTS.md experiment

複製一個小 repo，先請 Coding Agent 加 endpoint，記錄它讀哪些檔、跑哪些測試。加入 AGENTS.md：架構入口、測試命令、禁止事項、review checklist，再做相似任務比較。

**驗收：** guidance 少於 100 行；每條可操作；至少改善兩個可量測行為；不放 secrets、長篇教科書或單次任務。

## Lab 04.2 — Ticket triage Skill

建立 `work/ticket-triage/SKILL.md`，metadata 清楚說明 trigger/non-trigger；流程為 validate → classify → retrieve policy → propose → escalate。定義 P0/security/payroll 一律轉人工。

**驗收：** 10 trigger、10 non-trigger cases；輸出 schema；禁止 write action；不因 ticket 內指令改流程。[解答](SOLUTIONS.md#042)

## Lab 04.3 — Scripts/references/assets

把 severity validation 寫進 `scripts/validate.py`，把詳細分類政策放 `references/policy.md`，範例輸出放 `assets/example.json`。SKILL.md 只保留 routing 指令。

**驗收：** script 有 tests；只在需要時讀 reference；修改政策不必改 validator；Skill 不超過必要 context。

## Lab 04.4 — Distributable plugin

替 Skill 建 manifest、version、owner、license、changelog、install/update/uninstall、相容性與 mock connector。打 `v0.1.0` tag，故意做壞 `v0.2.0` 再演練 rollback。

**驗收：** 新使用者可依 README 安裝；缺少 dependency 時有清楚錯誤；升級不覆蓋 credentials；移除後不留 background service。

