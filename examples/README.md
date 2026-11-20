# Reference examples

目前提供一個無外部依賴的 orchestration core，示範：

- explicit state transitions
- duplicate event idempotency
- approval 綁定 proposed payload
- illegal transition rejection

執行：

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
```

或直接執行 `uv run --python 3.11 --extra dev pytest`。

它刻意不呼叫模型。Chapter 03 的任務是把 model/tool loop 放進這個可靠外殼，Chapter 07 再把 in-memory state 換成 database 與 queue。
