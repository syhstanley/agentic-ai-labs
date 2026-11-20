# Chapter 11 — Enterprise Discovery、ROI 與 Productization

目標：選對問題、取得利害關係人信任，讓技術成果真的被使用並能創造收入。

## 11.1 Process discovery

訪談執行者、主管、IT、security、legal、data owner。記錄 as-is flow、例外、shadow work、等待點、系統 owner、資料敏感度與 baseline；不要只訪談提出需求的主管。

**Lab：** 觀察五次真實或模擬流程，建立 service blueprint。找出哪些步驟應刪除、標準化、自動化、copilot 或保留人工。

## 11.2 Integration architecture

盤點 source of truth、API availability、identity、network、data residency、change window、rate limits、sandbox。若系統沒有 API，依序評估 export/import、database view、RPA/computer use，並清楚標示脆弱性。

**Lab：** 交付 context/container/component 三層架構圖，以及 build-vs-buy decision record。

## 11.3 ROI 與 business case

年度效益不是只算省下工時：

```text
Benefit = capacity released + error loss avoided + cycle-time value + revenue uplift
Cost = build + licenses/API + infrastructure + review time + maintenance + risk reserve
ROI = (Benefit - Cost) / Cost
```

工時節省不一定等於裁員成本；要說明時間被轉移到何處。設定 baseline、target、measurement window、counterfactual。

**Lab：** 為 PoC 建立 low/base/high 三情境，包含 token/API、人工 review、維運、教育訓練與失敗成本。

## 11.4 Adoption 與 change management

設計 champion、training、office hours、feedback loop、escalation、usage analytics、policy acknowledgment。使用者繞過 Agent 通常是流程或信任問題，不只是「抗拒改變」。

**Lab：** 進行 5 人 usability test；記錄 task completion、錯誤、信任過高／過低和建議，迭代 UI 與 SOP。

## 11.5 Productization 與賺錢方式

可選角色：內部 AI automation engineer、AI platform engineer、solution architect、consultant、AI product manager。可銷售的是特定流程成果，不是「我們有一個萬用 Agent」。

把方案拆成：discovery workshop、PoC、production rollout、training、support/SLA、季度 eval 與 governance review。定義理想客戶、共通核心、客製邊界、定價與維運責任。

### Chapter challenge

做 10 分鐘 executive pitch：問題與 baseline、demo、eval 結果、architecture/security、ROI、90 天 rollout、需要的決策。另準備技術附錄接受 security 與 IT review。

## Exit ticket

- [ ] 能拒絕低價值或不適合 Agent 的題目
- [ ] 成功指標包含品質、風險、採用和財務結果
- [ ] PoC 有明確 production gate，非無限試驗
- [ ] 維運、資料 owner、模型變更與 incident 責任清楚

