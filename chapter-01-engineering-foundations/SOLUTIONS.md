# Chapter 01 Reference Solutions

## 01.1

核心流程應是 `parse → validate → route`，而非 try/except 包住整個檔案：

```python
for line_no, raw in enumerate(source, 1):
    try:
        ticket = Ticket.from_json(raw)
    except (ValueError, TypeError, json.JSONDecodeError) as exc:
        write_dead_letter(line_no, type(exc).__name__)
    else:
        write_valid(ticket)
```

Dead letter 記 line、error code 與可安全識別的 record ID，不保存可能含個資的完整 exception。

## 01.2

Credential 出現在 commit 後：先 revoke/rotate，再清 history，force push 前協調協作者，最後檢查 CI artifacts、fork、logs。刪檔不能讓已洩漏 token 恢復安全。

## 01.3

Retry policy 參考：

```python
if status == 429 or 500 <= status < 600:
    if attempt == max_attempts: raise RetryExhausted()
    sleeper(retry_after or min(2 ** attempt, 8))
    continue
if 400 <= status < 500:
    raise PermanentHttpError(status)
```

Transport、clock、sleeper 都注入，才可快速且 deterministic 測試。

## 01.4

關鍵 constraint：`UNIQUE(run_id, idempotency_key)`；先開始 transaction，再寫 tool call 與 state，任一步失敗都 rollback。SQLite 測試記得 `PRAGMA foreign_keys=ON`。

## 01.5

合理分布：validation 8 unit、retry 5 unit、SQL 3 integration、API 2 contract、end-to-end 1。Coverage 數字不是目標；每個重要 invariant 至少有一個會失敗的反例。

## 01.6

可接受 Dockerfile 特徵：specific Python tag、先複製 lockfile、建立 UID、`USER app`、exec-form CMD、health endpoint。Secrets 由 runtime 提供，不能 `COPY .env` 或寫在 image layer。

