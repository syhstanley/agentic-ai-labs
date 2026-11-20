# Chapter 04 — AGENTS.md、Skills 與 Plugins

目標：把個人提示詞升級成可被團隊發現、執行、測試、版本管理及安裝的工作能力。

## 04.1 AGENTS.md

AGENTS.md 放每次進 repo 都應遵守的規則：build/test commands、架構慣例、review policy、安全限制。不要塞入整本公司手冊。

**Lab：** 為 Chapter 03 專案寫 AGENTS.md，故意讓 coding agent 修改程式，再檢查它能否選對測試、避免 secrets、遵守 write-action policy。

## 04.2 Skill anatomy

Skill 通常由 `SKILL.md` 加上可選的 `scripts/`、`references/`、`assets/` 組成。Description 應清楚說明何時觸發，也要說何時不使用。

**Lab：** 將「工單分流 SOP」做成 Skill：先分類、查相似案例、草擬處理方式、高風險類別轉人工。

## 04.3 Progressive disclosure 與測試

Metadata 用來發現，SKILL.md 用來執行，references 只在需要時讀取。把 deterministic validation 寫成 script；不要要求模型記住 200 條欄位規則。

**Lab：** 建立 20 個 trigger/non-trigger cases，測 Skill 是否在正確任務啟用；再測流程完整性與輸出驗證。

## 04.4 Plugin 與團隊分發

Skill 是 authoring format；Plugin 可包裝 skills、connectors/MCP 與設定供安裝。管理 semantic version、changelog、owner、相容性與 rollback。

### Chapter challenge

交付一個可安裝的內部 workflow package，包含：Skill、mock MCP dependency、範例、測試、版本、license、threat notes、uninstall/rollback 說明。

## Exit ticket

- [ ] 能判斷規則該放 AGENTS.md、Skill、script 還是 MCP
- [ ] Skill 的 trigger 和 non-trigger cases 都有測試
- [ ] 團隊成員能安裝、升級與回滾
- [ ] 文件不含公司秘密或環境專用 credential

