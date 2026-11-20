# References

本課程優先理解可長期轉移的工程原理，再使用特定平台。以下是起始參考；每次實作前請重新確認最新版文件與安全建議。

## OpenAI official documentation

- [Building agents learning track](https://developers.openai.com/tracks/building-agents)
- [Function calling](https://developers.openai.com/api/docs/guides/function-calling)
- [Evals](https://developers.openai.com/api/docs/guides/evals)
- [Codex customization: AGENTS.md, Skills, MCP, Subagents](https://learn.chatgpt.com/docs/customization/overview)
- [Build Skills](https://learn.chatgpt.com/docs/build-skills)
- [Model Context Protocol in Codex](https://learn.chatgpt.com/docs/extend/mcp)

## Reading protocol

閱讀任何框架教學時回答：

1. 它替我抽象掉哪一段 loop 或 state？
2. Retry、timeout、idempotency、auth 在哪一層？
3. State 存在哪裡，process crash 後會怎樣？
4. Tool input/output 如何驗證？
5. Trace、eval、cost 如何取得？
6. 若明天移除這個 framework，我保留了哪些可轉移能力？

