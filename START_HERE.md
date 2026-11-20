# Start Here：在 Linux 練習機開始上課

## 1. 登入與進入課程

```bash
ssh stanley@YOUR_HOST
cd /home/stanley/agentic-ai-labs
git pull
```

目前尚未拿到主機位址時，也可以直接從 Telegram 請蝦秘酷ㄅ在練習機執行命令。

## 2. 建立課程環境

```bash
uv sync --python 3.11 --extra dev
uv run pytest
```

看到 `4 passed` 代表環境正常。前半課程使用 fake model，不需要 API key。

## 3. 每個 Chapter 怎麼讀

每章有三份文件：

- `README.md`：概念地圖與學習目標
- `LABS.md`：示範、任務、驗收、Debug Challenge、提示
- `SOLUTIONS.md`：卡住後才看的參考解答

實作放在章節的 `work/` 目錄。例如：

```bash
mkdir -p chapter-00-orientation/work
cp PROGRESS.md MY_PROGRESS.md
```

`work/` 是你的答案；不要直接修改 `SOLUTIONS.md`。

## 4. 正確的求助方式

先依序使用：

1. 重讀錯誤訊息與 Acceptance Criteria
2. 看 `LABS.md` 的 Hint 1
3. 寫最小重現、看 Hint 2
4. 請 Agent 只提供 review 或下一個提示
5. 最後才看 `SOLUTIONS.md`

不要一開始就叫 Agent 完成整題。可以這樣問：

> 請只 review 我的做法，指出第一個不符合驗收條件的地方，不要直接給答案。

## 5. 每題完成定義

- 指令可在乾淨環境重現
- Happy path 與 failure path 都測過
- 驗收條件逐項附證據
- 無 secrets、真實個資或公司機密
- 能不用術語向同事解釋設計取捨
- Commit 訊息包含章節，例如 `lab(03.2): implement bounded agent loop`

