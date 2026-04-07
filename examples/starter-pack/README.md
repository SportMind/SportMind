# SportMind Starter Pack

**Six working examples covering the full range from the simplest API call
to a production-grade autonomous tournament agent.**

These are not pseudocode or conceptual outlines — they are working Python
implementations that you can run, adapt, and build on. Each one is designed
to be understood in under ten minutes and deployed in under thirty.

---

## Choose your starting point

| Example | What it does | Who it is for | Complexity |
|---|---|---|---|
| [01-simple-signal.py](#01) | One signal, ten lines | Anyone evaluating SportMind | ⭐ |
| [02-claude-conversation.py](#02) | SportMind + Claude via MCP | Claude/Anthropic API developers | ⭐⭐ |
| [03-single-sport-agent.py](#03) | Football token monitor, one sport | Fan token application developers | ⭐⭐⭐ |
| [04-multi-sport-agent.py](#04) | Monitor multiple sports simultaneously | Portfolio intelligence developers | ⭐⭐⭐ |
| [05-sportfi-kit-integration.py](#05) | SportMind + SportFi Kit together | Full-stack fan token developers | ⭐⭐⭐⭐ |
| [06-autonomous-tournament-tracker.py](#06) | Full autonomous tournament agent | Production autonomous systems | ⭐⭐⭐⭐⭐ |

---

## What you need to run these

**All examples:**
```bash
pip install aiohttp anthropic --break-system-packages
```

**For MCP examples (02, 05):**
```bash
pip install mcp --break-system-packages
```

**SportMind running locally:**
```bash
# Skills API (for most examples)
python scripts/sportmind_api.py
# Default: http://localhost:8080

# MCP server (for examples 02, 05)
python scripts/sportmind_mcp.py
```

**Environment variables:**
```bash
export ANTHROPIC_API_KEY=your_key_here    # Required for 02, 05
export SPORTMIND_API=http://localhost:8080 # Optional; default used if not set
export ALERT_WEBHOOK=https://your-webhook  # Optional; for alert examples
```

---

## The SportMind layer model (one paragraph)

SportMind provides intelligence. Your application takes action.

When you call SportMind and get back `adjusted_score: 68.4, sms: 79, recommended_action: ENTER` — that is not an instruction to buy or sell. It is intelligence context that says: the pre-match conditions look favourable for this outcome, the analysis quality is good, and if you were going to act, conditions support it. What you do with that is your application's decision. SportMind never executes trades, submits governance votes, or makes financial commitments. That boundary is what makes autonomous SportMind agents trustworthy enough to run unsupervised.

---

## <a name="01"></a> Example 01 — Simple signal

**`01-simple-signal.py`** — The minimum viable SportMind integration.
Demonstrates: skill loading, macro check, signal generation.
Time to first signal: under 2 minutes.

---

## <a name="02"></a> Example 02 — Claude conversation

**`02-claude-conversation.py`** — SportMind loaded as Claude context via MCP.
Demonstrates: MCP integration, Claude as reasoning engine, structured output.
Requires: Anthropic API key.

---

## <a name="03"></a> Example 03 — Single sport agent

**`03-single-sport-agent.py`** — A complete football token monitoring agent.
Demonstrates: SportMindAgent base class, Level 2 autonomy, alert generation.
Monitors: one token ($PSG), one sport (football), 4-hour cycle.

---

## <a name="04"></a> Example 04 — Multi-sport agent

**`04-multi-sport-agent.py`** — Portfolio agent covering football, cricket, MMA.
Demonstrates: sport routing, format-specific reasoning (dew factor, weigh-in),
               multi-token monitoring, per-sport modifier application.

---

## <a name="05"></a> Example 05 — SportFi Kit integration

**`05-sportfi-kit-integration.py`** — SportMind + SportFi Kit working together.
Demonstrates: intelligence/execution boundary, recommended_action as input to
               token-gating logic, never triggering contracts directly.

---

## <a name="06"></a> Example 06 — Autonomous tournament tracker

**`06-autonomous-tournament-tracker.py`** — Production-grade autonomous agent.
Demonstrates: full lifecycle, NCSI computation, Level 3 autonomy, audit logging,
               graceful degradation, daily briefing generation.
Requires: no human input once started.

---

## Where to go next

Built something? Read:
- `core/autonomous-agent-framework.md` — the full agent model and safety principles
- `examples/agentic-workflows/multi-agent-coordination.md` — coordinating multiple agents
- `platform/freshness-strategy.md` — keeping your agent's intelligence current
- `platform/sportmind-mcp-server.md` — all five MCP tool definitions
- `examples/applications/` — nine full application blueprints

Questions or contributions:
- `community/calibration-data/CONTRIBUTING.md` — submitting calibration records
- `WHO-WE-ARE.md` — what SportMind is and how it fits your stack

*MIT License · SportMind · sportmind.dev*
