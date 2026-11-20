# Chapter 00 — Orientation：先看懂整個 Agent 系統

目標：把「Agent 很聰明」改寫成可以畫圖、測試和問責的工程描述。

## 00.1 Agent、chatbot、automation、workflow

### Mental model

- Chatbot：回答問題，通常不改變外部世界。
- Automation：步驟預先寫死，相同輸入走相同路徑。
- Workflow：多步驟流程，可能含條件、等待、重試和人工任務。
- Agent：具有 instructions、guardrails、tools，能根據狀態選擇下一步。

Agent 不一定比 workflow 好。薪資計算、付款金額、權限判斷等規則應由 deterministic code 控制；分類、摘要、非結構化資料理解才適合模型。

### Lab — 四象限分類

挑選公司內 12 個任務，標記「語意不確定性」及「執行風險」高低，決定使用規則、自動化、copilot 或 agent。

**產出：** `work/opportunity-map.md`。每個任務要有頻率、工時、輸入、輸出、風險、建議方案。

## 00.2 Orchestration

Orchestration 管理多步驟、工具、context、handoff、guardrail 與完成條件。它可能是一段 `while` loop、一個狀態機、一套 workflow engine，或 Agents SDK；不是某個特定產品。

### Lab — CRM 跟進流程

畫出「會議逐字稿 → 抽取資訊 → 查 CRM → 草擬更新 → 核准 → 寫入 → 通知」的 sequence diagram。補上：CRM timeout、找不到客戶、重複請求、主管拒絕、寫入成功但通知失敗。

**驗收：** 每個 state 有輸入、輸出、owner、timeout、retry、terminal status；所有 write action 都有 approval 或明確 policy。

## 00.3 工作環境與秘密

安裝 Git、GitHub CLI、Python、`uv`、Docker、VS Code 或其他 IDE。練習 `.env.example`、環境變數與 `.gitignore`。

### Lab — 安全的 Hello Service

建立虛擬環境、執行測試、建立 feature branch。故意在測試用假 repo commit 一個假 token，再用 history rewrite 清除；不要使用真實 credential。

## 00.4 流程盤點與 baseline

Agent 專案先記錄現況：每月件數、平均處理時間、返工率、錯誤成本、等待時間及人員滿意度。

### Chapter challenge

訪談一位流程使用者，交付一頁式 problem brief。不得先指定「做 chatbot」；必須寫問題、baseline、非目標、風險、成功指標與最小 PoC。

## Exit ticket

- [ ] 能用一句話區分 agent 與 workflow
- [ ] 能畫出 happy path 和至少五條 failure paths
- [ ] 能說明為何不是所有流程都應 agentic
- [ ] 已選定一個貫穿全課程的企業案例

