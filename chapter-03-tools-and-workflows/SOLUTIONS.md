# Chapter 03 Reference Solutions

## 03.1

Tool contract 至少含 schema version、risk、required scope、timeout、retriable errors。`draft_ticket` 無副作用；`create_ticket` 驗證 signed approval 與 idempotency key。

## 03.2

```python
for step in range(max_steps):
    output = model.next(messages, tools=allowed_schemas)
    if output.final is not None:
        return output.final
    call = validate_call(output.tool_call)
    if fingerprint(call) in recent_calls:
        raise RepeatedToolCall()
    result = execute_with_timeout(call)
    trace.append({"step": step, "tool": call.name, "status": result.status})
    messages.append(tool_observation(result))
raise StepLimitExceeded(max_steps)
```

Executor 仍須自己做 auth、validation；模型選了 allowlisted tool 不代表有權執行。

## 03.3

`CANCELLED` 應是 terminal；通常只有非 terminal states 接受 `CANCEL`。`NEEDS_REVIEW` 是否可回 `DRAFTED` 要明確定義 reviewer event，不讓模型自行跳回。

## 03.4

Server 將 `(tenant,idempotency_key)` 設 unique，第一次成功即保存 response。重送回傳原結果。Response 遺失時 client 用 key 查狀態，不能換新 key 再 POST。

## 03.5

Approval payload 應 canonicalize：`run_id/tool/arguments_hash/approver/issued_at/expires_at`。執行時重新算 arguments hash、檢查 expiry 和 scope，再以 constant-time compare 驗證。

