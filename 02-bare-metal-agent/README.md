# 02 — Bare-Metal Agent (target: running by Jul 17, finished by mid-Aug)

**The point:** you've built agents *inside* Claude Code (skills + MCP). You've
never built the machine itself. After this module, nothing about agents is
magic to you — an agent is a `while` loop that calls a model, runs tools, and
feeds results back. That sentence is the whole industry secret.

Maps to: **AI Engineering Techniques & Architectures** (you'll be ahead of it).

## Ground rules

- No frameworks. No LangChain, no CrewAI. Just `anthropic` (the raw SDK) — the
  point is to see the mechanism.
- `agent_skeleton.py` has the scaffolding; **you type the loop** (the `# YOU:`
  blocks). Pair with Claude on everything else — reading errors, explaining
  API responses, designing new tools.

## Setup

```bash
cd "02-bare-metal-agent"
uv venv && source .venv/bin/activate
uv pip install anthropic python-dotenv
cp .env.example .env     # then put your real key in .env (gitignored — verify!)
python agent_skeleton.py
```

Get an API key at https://console.anthropic.com/ — a few dollars of credit
covers this whole module. **The key lives in `.env` and nowhere else. Ever.**

## The build, in stages

**Stage 1 — one round trip.** Make the skeleton send a message and print the
reply. Read the raw response object top to bottom (`print(response)`). Notice
`stop_reason`. That field drives everything.

**Stage 2 — the loop.** Implement the agent loop: while `stop_reason ==
"tool_use"`, execute the requested tool, append the result, call again. Two
toy tools are provided (`calculator`, `read_file`). When your agent chains
two tool calls to answer one question, stop and appreciate what just
happened — you built the thing.

**Stage 3 — your tools.** Delete the toys. Write tools that hit your world:
`get_quote(symbol)` (stub it with fake prices first), `get_positions()`
(read a JSON file), `log_decision(text)`. Now ask it "should I trim NVDA?"
and watch it use them.

**Stage 4 — make it survive contact.** Three upgrades, in order:
1. Tool errors: a tool that throws should return an error string to the
   model, not crash the loop. Watch the model *recover* — this is why
   agents work.
2. A `max_turns` guard so a confused model can't loop forever.
3. Track token usage per run (`response.usage`) and print cost at exit.
   You did spend-guarding in Braintrust; now compute it from first principles.

**Stage 5 (stretch) — streaming + system prompt.** Stream the response
token-by-token; move your trading rules (your no-buy list!) into the system
prompt and verify the agent refuses a PLTR buy.

## Reading (short, all of it worth it)

- Anthropic: *Building effective agents* — https://www.anthropic.com/engineering/building-effective-agents
  (Read this twice. It's the best thing written on the topic and it's framework-skeptical, like this module.)
- Tool use docs: https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview
- Messages API reference: https://docs.claude.com/en/api/messages

## Done when

- [ ] Your agent answers a question that requires chaining ≥2 tool calls
- [ ] A deliberately broken tool doesn't crash it
- [ ] It prints cost per run
- [ ] You can explain `stop_reason`, the messages array, and why tool results
      are sent back as *user* messages — out loud, to Claude, and get graded
- [ ] Pushed to GitHub as part of the workspace repo — the pre-push hook
      screens it automatically, but still eyeball `git status` first:
      `.env` must show as ignored, never staged
