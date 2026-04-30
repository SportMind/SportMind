# SportMind MCP Server

**Connect any AI agent to SportMind sports intelligence in one step.**

The SportMind MCP server exposes the full library as callable tools —
no file loading, no context management. Your agent calls a tool,
SportMind returns structured intelligence.

---

## Quick start — Claude Desktop (2 minutes)

**1. Clone the repository**
```bash
git clone https://github.com/SportMind/SportMind
cd SportMind
```

**2. Install the MCP SDK**
```bash
pip install mcp aiohttp
```

**3. Add to Claude Desktop config**

Open `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS)
or `%APPDATA%\Claude\claude_desktop_config.json` (Windows) and add:

```json
{
  "mcpServers": {
    "sportmind": {
      "command": "python",
      "args": ["/full/path/to/SportMind/scripts/sportmind_mcp.py"],
      "description": "SportMind sports intelligence"
    }
  }
}
```

**4. Restart Claude Desktop**

SportMind tools are now available. Try asking:
- *"Use SportMind to analyse PSG vs Arsenal tonight"*
- *"Check the SportMind macro state for fan tokens"*
- *"Load the full cricket intelligence stack"*

---

## Quick start — Claude Code (1 minute)

```bash
# Install
pip install mcp aiohttp

# Add to your project's MCP config
claude mcp add sportmind python /path/to/SportMind/scripts/sportmind_mcp.py
```

---

## Quick start — Remote deployment (Render, Railway, Fly.io)

Deploy SportMind as a hosted MCP endpoint so any agent can connect
without running a local server.

**Option A — Docker (any cloud)**
```bash
docker build -t sportmind-mcp .
docker run -p 3001:3001 sportmind-mcp
# MCP endpoint: http://your-host:3001/mcp
# Health check: http://your-host:3001/health
```

**Option B — Render (free tier, zero config)**
1. Fork `https://github.com/SportMind/SportMind`
2. Go to render.com → New Web Service → connect your fork
3. Build command: `pip install mcp aiohttp`
4. Start command: `python scripts/sportmind_mcp.py --http --port 3001`
5. Your endpoint: `https://your-app.onrender.com/mcp`

**Option C — Local HTTP server**
```bash
python scripts/sportmind_mcp.py --http --port 3001
# MCP endpoint: http://localhost:3001/mcp
```

---

## Connecting a remote endpoint to your agent

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=2000,
    mcp_servers=[
        {
            "type": "url",
            "url":  "https://your-sportmind-host/mcp",
            "name": "sportmind"
        }
    ],
    messages=[{
        "role":    "user",
        "content": "Check the macro state, then analyse PSG vs Arsenal using SportMind."
    }]
)
```

---

## The ten tools

### `sportmind_signal`
Generate a pre-match intelligence signal. Returns direction, adjusted_score,
SportMind Score (SMS), modifiers, and active flags.

```json
{
  "sport":      "football",
  "event_id":   "ucl-qf-2026-psg-arsenal",
  "use_case":   "fan_token_tier1",
  "home_team":  "PSG",
  "away_team":  "Arsenal",
  "include_defi_context": true
}
```

### `sportmind_macro`
Get the current macro state — crypto cycle phase, macro_modifier, active events.
**Always call this before fan token or DeFi analysis.**

No input parameters required — macro state is global context.

```json
// Request: no parameters needed
{}

// Response schema:
{
  "crypto_cycle_phase":  "bull | bear | neutral | transition",
  "macro_modifier":      0.85,
  "cycle_confidence":    "HIGH | MEDIUM | LOW",
  "active_events": [
    {
      "event":     "string — name of active macro event",
      "impact":    "POSITIVE | NEGATIVE | NEUTRAL",
      "modifier":  1.10,
      "expires":   "ISO-8601 date or null"
    }
  ],
  "regulatory_state": {
    "mica_status":        "string",
    "sec_cftc_guidance":  "string",
    "us_market_open":     true
  },
  "override_active":     false,
  "override_reason":     null
}
```

### `sportmind_stack`
Load the full intelligence stack for a sport in correct loading order
(macro → market → domain → athlete → fan-token).

```json
{
  "sport":      "cricket",
  "use_case":   "pre_match",
  "compressed": false
}
```

Set `compressed: true` to reduce token cost by ~70% for constrained contexts.

### `sportmind_verify`
Verify skill content integrity against `platform/skill-hashes.json`.
Use in production deployments where content authenticity matters.

```json
{
  "skill_id": "domain.football",
  "content":  "<skill content to verify>"
}
```

### `sportmind_agent_status`
Get the operational status of running SportMind autonomous agents.
See `examples/agentic-workflows/` for agent patterns.

---

## Tool call sequencing

Agents should follow this order:

```
1. sportmind_macro          → Always first for token applications
2. sportmind_signal         → For a specific event signal
   OR
   sportmind_stack          → For the full reasoning context
3. sportmind_verify         → Optional — security-sensitive deployments only
```

**Rule:** Never call `sportmind_signal` before `sportmind_macro` for fan token
or DeFi applications. The macro_modifier directly affects signal interpretation.

---

## Supported sports

football · basketball · cricket · mma · formula1 · tennis · rugby · rugby_league ·
afl · baseball · ice_hockey · motogp · nascar · kabaddi · netball · handball ·
esports · darts · snooker · swimming · athletics · winter_sports · boxing ·
cycling · horse_racing

---

## Supported use cases

| Use case | Description |
|---|---|
| `pre_match` | Standard pre-match intelligence signal |
| `fan_token_tier1` | Tier 1 fan token — full five-layer stack |
| `fan_token_tier2` | Tier 2 fan token — core three layers |
| `prediction_market` | Prediction market entry/exit signal |
| `commercial_brief` | Commercial intelligence summary |
| `governance` | Token governance event analysis |

---

## What the server does not do

**No live data.** SportMind is an intelligence framework, not a data provider.
The signal direction is a structural baseline from skill intelligence. For full
accuracy integrate live athlete availability and current form via
`platform/data-connector-templates.md`.

**No persistent state.** Each tool call is stateless. The server reads skill
files from the repository on each call.

**No authentication.** If deploying publicly, add your own auth layer in front
of the `/mcp` endpoint. The server itself has no built-in auth.

---

## Health check

```bash
curl http://localhost:3001/health
```

Returns:
```json
{
  "status":    "ok",
  "service":   "SportMind MCP Server",
  "version":   "3.30.0",
  "tools":     ["sportmind_signal", "sportmind_macro", "sportmind_stack", "sportmind_verify", "sportmind_agent_status"],
  "timestamp": "2026-04-08T..."
}
```

---

## Relationship to the Skills API

```
SKILLS API (scripts/sportmind_api.py)
  HTTP REST — serves skill files on demand
  Best for: web applications, SportFi Kit, pre-session loading
  Transport: HTTP GET

MCP SERVER (scripts/sportmind_mcp.py)
  MCP protocol — exposes SportMind as callable tools
  Best for: Claude Desktop, Claude Code, Anthropic API agents
  Transport: stdio (local) or HTTP/SSE (remote)

Both serve the same intelligence from the same skill files.
Both can run simultaneously.
```

---

## New tools (added v3.95.3.0.0.0.0.0.0.0.0.0)

### `sportmind_pre_match`
Orchestrated full pre-match reasoning package in one call. Combines sport
domain signal, macro state, availability check source, disciplinary reminder,
narrative momentum, and statistical reasoning reference.
Input: `sport`, `home_team`, `away_team`, `competition`, `kickoff`, `use_case`

### `sportmind_disciplinary`
Disciplinary check for a player and sport. Returns DSM framework tier,
regulatory source to verify, flags to set, and commercial rule.
Input: `player`, `sport`, `club`, `include_framework`

### `sportmind_fan_token_lookup`
Resolve club name, ticker, or sport to Chiliz Chain fan token context.
Returns contract address (Chain ID 88888), chiliscan and fantokens.com links,
market cap tier, and recommended skill stack. 24 verified tokens.
Input: `query` (e.g. "PSG", "football", "Barcelona"), `include_registry`

### `sportmind_sentiment_snapshot`
Multi-axis sentiment state for a fan token. Macro sentiment plus references
for fan sentiment, social lift, commercial, and disciplinary status.
Input: `token` (ticker or club name), `use_case`

### `sportmind_verifiable_source`
Authoritative source for a query type and sport.
Query types: lineup_confirmation, match_result, disciplinary_ban,
player_stats, transfer_news, rankings
Input: `query_type`, `sport`


---

## Extended integrations (v3.95.3.0.0.0.0.0.0.0.0.0)

SportMind works with three additional MCP servers to create a complete
reasoning, memory, and verification stack.

**Sequential Thinking MCP** — explicit step-by-step reasoning chain.
Prevents phase-skipping errors and makes every SportMind decision auditable.
See `platform/sequential-thinking-integration.md` for the full chain definition
and system prompt.

**Memory MCP** — persistent cross-session intelligence. Stores signal history,
DSM status, macro phase at each analysis, and upcoming high-FTIS events.
Enables pattern detection (consecutive WAITs, repeat disciplinary, macro recovery).
See `platform/memory-integration.md` for the full memory schema.

**Fetch MCP** — live disciplinary verification. Fetches authoritative sources
(World Rugby, FA, FIA, USADA, ICC) that `sportmind_verifiable_source` maps out.
Closes the loop between knowing where to look and actually looking.
See `platform/fetch-mcp-disciplinary.md` for the full workflow.

**Four-server configuration:**
```json
{
  "mcpServers": {
    "sportmind":            { "command": "python", "args": ["/path/to/SportMind/scripts/sportmind_mcp.py"] },
    "sequential-thinking":  { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"] },
    "memory":               { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-memory"] },
    "fetch":                { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-fetch"] }
  }
}
```

---

*MIT License · SportMind · sportmind.dev · github.com/SportMind/SportMind*
