# Chapter 10 — Platform、Open WebUI 與 Production Deployment

目標：把 notebook／CLI 原型變成多人可用、可更新、可監控、可回滾的服務。

## 10.1 Service boundary 與 FastAPI

API layer 處理 authentication、validation、rate limit 與 request lifecycle；domain layer 放 business workflow；adapter layer 接模型與外部系統。不要把所有邏輯塞在 route handler。

**Lab：** 暴露 `POST /runs`、`GET /runs/{id}`、`POST /runs/{id}/approve`、`POST /runs/{id}/cancel`。使用 request ID、typed errors、OpenAPI contract tests。

## 10.2 Persistence、queue、worker

使用 PostgreSQL 保存 business state，queue 執行長任務，object storage 放大型 artifacts。設定 migrations、backup、restore test、retention 和 dead-letter handling。

**Lab：** Docker Compose 啟動 API、worker、database。Kill worker 後 run 可恢復；重啟 stack 不遺失 approval。

## 10.3 Open WebUI 的定位

Open WebUI 可作為聊天入口、模型／知識庫介面及內部使用者體驗層，但 business authorization、orchestration、audit、evals 仍應由後端 enforce。UI 隱藏按鈕不是安全控制。

**Lab：** 將你的 Agent service 接到 Open WebUI 或相容前端；顯示 citations、run status、approval card、tool activity。比較直接模型聊天與受控 workflow 的差異。

**Decision record：** 何時使用 Open WebUI、客製 Web app、Slack/Teams bot 或純 API？從身份整合、UX、維護、稽核與風險選擇。

## 10.4 CI/CD 與 environments

建立 lint → unit → contract → eval smoke → security scan → image build → staging → approval → production。Artifacts 必須 immutable、版本可追溯、設定與程式分離。

**Lab：** GitHub Actions 建置 pinned image；staging smoke test 通過才部署。模擬壞版本並 rollback。

## 10.5 Reliability 與 SRE

定義 SLI/SLO：availability、task success、p95 latency、queue age、unsafe action rate。加入 health/readiness、timeout budget、circuit breaker、capacity plan、on-call runbook。

### Chapter challenge

在本機或雲端部署 end-to-end Agent。進行 load test 與 chaos test，提供 architecture diagram、dashboard、backup/restore evidence、deployment/rollback video 或紀錄。

## Exit ticket

- [ ] UI、orchestration、business policy、tool execution 清楚分層
- [ ] 部署可重現，image 與 dependencies 固定版本
- [ ] 可觀測、備份、恢復、rollback 都實際演練過
- [ ] Production credentials 不會出現在 developer laptop 或 CI logs

