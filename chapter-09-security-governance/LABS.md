# Chapter 09 Labs

## Lab 09.1 — Threat model

畫工單 Agent DFD，列 assets、actors、boundaries、entry points。用 STRIDE 或 attack tree 找 15 個 threats，評 likelihood/impact/control/residual risk/owner。

**驗收：** 包含 malicious user、external document、compromised MCP、insider、model mistake；top 5 有可測 control。

## Lab 09.2 — Prompt injection red team

建立 20 個攻擊：直接／間接 injection、編碼混淆、假 system message、data exfil URL、tool-output injection、multi-turn persistence。

**驗收：** external content 永遠標示 data；outbound URL allowlist；敏感資料不進 tool args；安全部分仍可完成。[解答](SOLUTIONS.md#092)

## Lab 09.3 — Least privilege

建立 read identity、draft identity、approved-write executor。Secrets 只在需要的 process/runtime 注入，設定 TTL/rotation；測 developer/CI/production 分離。

**攻擊：** 從 prompt、exception、trace、`docker inspect`、process args 找 secret；全部不得取得。

## Lab 09.4 — Audit/privacy policy

定義 data classes、allowed model/location、retention、deletion、DLP、access review。產生 audit event：actor/action/target/policy/approval/result/correlation，敏感內容只存 hash/reference。

**驗收：** 能回答誰在何時代表誰做了什麼；user deletion request 可追到 cache/index/artifacts；logs 有存取控制。

## Lab 09.5 — Incident tabletop

情境：惡意 PDF 促使 Agent 將摘要送往攻擊者 URL。演練 detect → kill switch → revoke → scope → preserve evidence → notify → recover → postmortem。

**驗收：** 30 分鐘 timeline；owner/communication 明確；恢復前加 regression test；postmortem 不以「模型笨」當 root cause。

