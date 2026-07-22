# SportMind — Quickstart

**From zero to a working sports intelligence signal in under 5 minutes.**

---

## 1. Clone and install

```
git clone https://github.com/SportMind/SportMind
cd SportMind
pip install mcp aiohttp anthropic
```

## 2. Start the MCP server

```
python scripts/sportmind_mcp.py
# Running on stdio — ready for Claude Desktop / Claude Code
```

Or for HTTP/SSE (remote agents):

```
python scripts/sportmind_mcp.py --http --port 3001
# MCP endpoint: http://localhost:3001/mcp
# Health check:  http://localhost:3001/health
```

## 3. Copy a template and run it

```
# Fan token monitor (single token, MCP)
cp templates/fan-token-monitor.py my-agent.py
# Edit YOUR_TOKEN and YOUR_SPORT at the top, then:
python my-agent.py

# Portfolio monitor (multiple tokens)
cp templates/portfolio-monitor.py my-portfolio.py
python my-portfolio.py

# One-shot pre-match signal (no MCP required)
cp templates/pre-match-signal.py my-signal.py
python my-signal.py
```

---

## What you will see

```
{
  "recommendation": "ENTER",
  "signal": { "direction": "HOME", "adjusted_score": 72.4, "sms": 100 },
  "modifiers": { "macro": 1.00, "dsm": 1.00, "composite": 1.00 },
  "token": "PSG",
  "sportmind_version": "4.1.18"
}
```

Note: `direction` format depends on use case. Fan token analysis returns
`LONG $TOKEN` / `SHORT $TOKEN` / `DRAW`. Sport intelligence analysis returns
`HOME` / `AWAY` / `DRAW`. See [FIRST-RECORD-GUIDE.md](FIRST-RECORD-GUIDE.md)
for the full distinction.

---

## Where to go next

| Goal                                   | File                              |
| -------------------------------------- | --------------------------------- |
| Understand the five-layer architecture | `WHO-USES-THIS.md`                |
| See all agent prompts                  | `agent-prompts/agent-prompts.md`  |
| Browse worked examples                 | `examples/starter-pack/README.md` |
| Connect Claude Desktop                 | `MCP-SERVER.md`                   |
| Add live data (lineups, prices)        | `platform/api-providers.md`       |
| Read full documentation                | `https://sportmind.dev/docs`      |

---

*MIT License · sportmind.dev · [GitHub](https://github.com/SportMind/SportMind)*
