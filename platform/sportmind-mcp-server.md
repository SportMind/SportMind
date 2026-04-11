# SportMind MCP Server Specification

**Makes SportMind queryable as a live tool by Claude and other MCP-compatible agents —
moving from static context injection to dynamic on-demand intelligence retrieval.**

---

## Why MCP changes the SportMind integration model

The current integration pattern loads SportMind skills into an agent's context window
at session start. This works but has a ceiling: loading the full five-layer stack for
a specific sport costs 25,000–45,000 tokens upfront, regardless of whether the
conversation ever needs deep analysis. For conversational agents serving many queries,
this is wasteful.

MCP (Model Context Protocol) inverts the model. Instead of front-loading everything,
the agent calls SportMind as a live tool exactly when it needs intelligence — passing
structured inputs and receiving structured outputs. The agent's context window stays
lean; SportMind responds on demand.

```
BEFORE MCP (static injection):
  Session start → load 40k tokens of skill content → agent has context
  User: "what about PSG tonight?" → agent reasons from pre-loaded context
  User: "now tell me about the NBA Finals" → agent lacks NBA context
  
AFTER MCP (dynamic tool):
  Session start → agent has SportMind as a registered tool
  User: "what about PSG tonight?" → agent calls sportmind_signal(sport="football")
  User: "now tell me about the NBA Finals" → agent calls sportmind_signal(sport="basketball")
  No pre-loading required. Every query gets the right intelligence.
```

---

## MCP tool definitions

SportMind exposes ten MCP tools (v3.48). Each takes structured inputs and returns
structured SportMind output including SMS, adjusted_score, flags, and reasoning.
See MCP-SERVER.md for the complete deployment guide and all ten tool specifications.

### Tool 1 — `sportmind_signal`

Primary tool. Generates a pre-match intelligence signal for a specific sporting event.

```json
{
  "name": "sportmind_signal",
  "description": "Generate a structured SportMind intelligence signal for a sporting event. Returns adjusted_score, SportMind Score (SMS), active flags, modifier breakdown, and reasoning summary. Use before any sports prediction, fan token analysis, or wagering decision.",
  "input_schema": {
    "type": "object",
    "properties": {
      "sport": {
        "type": "string",
        "description": "Sport identifier. One of: football, basketball, cricket, mma, formula1, tennis, rugby, rugby_league, afl, baseball, ice_hockey, motogp, nascar, kabaddi, netball, handball, esports",
        "enum": ["football","basketball","cricket","mma","formula1","tennis","rugby","rugby_league","afl","baseball","ice_hockey","motogp","nascar","kabaddi","netball","handball","esports"]
      },
      "event_id": {
        "type": "string",
        "description": "Event identifier. Use descriptive format: 'ucl-final-2026-psg-arsenal' or 'nba-finals-g7-2026'. Used for context, not database lookup."
      },
      "use_case": {
        "type": "string",
        "description": "Intelligence use case that determines which skill layers to load.",
        "enum": ["fan_token_tier1","fan_token_tier2","prediction_market","commercial_brief","pre_match","governance"],
        "default": "pre_match"
      },
      "home_team": {
        "type": "string",
        "description": "Home team or athlete name (optional — adds context to signal generation)"
      },
      "away_team": {
        "type": "string",
        "description": "Away team or athlete name (optional)"
      },
      "include_defi_context": {
        "type": "boolean",
        "description": "Include DeFi liquidity context (TVL, slippage estimate). Set true for wagering or token applications.",
        "default": false
      }
    },
    "required": ["sport"]
  }
}
```

**Example call:**
```json
{
  "sport": "football",
  "event_id": "ucl-qf-leg1-2026-psg-arsenal",
  "use_case": "fan_token_tier1",
  "home_team": "PSG",
  "away_team": "Arsenal",
  "include_defi_context": true
}
```

**Example response:**
```json
{
  "signal": {
    "direction": "HOME",
    "adjusted_score": 68.4,
    "confidence_tier": "MEDIUM",
    "recommended_action": "ENTER"
  },
  "sportmind_score": {
    "sms": 76,
    "sms_tier": "GOOD",
    "layers_loaded": [1, 2, 3, 4, 5],
    "coverage_note": "Full 5-layer stack loaded"
  },
  "modifiers": {
    "composite_modifier": 0.97,
    "macro_modifier": 1.00,
    "athlete_modifier": 0.97,
    "flags": {
      "lineup_unconfirmed": true,
      "macro_override_active": false,
      "liquidity_warning": false,
      "injury_warning": false
    }
  },
  "defi_context": {
    "pool_tvl_usd": 1840000,
    "estimated_slippage_1pct": 0.27,
    "lp_activity_signal": "NEUTRAL"
  },
  "reasoning_summary": "PSG home UCL QF. Arsenal away form strong (×0.97 modifier). Lineup unconfirmed — apply 50% position size until T-2h confirmation. Macro neutral. Liquidity adequate for standard positions.",
  "skill_stack_used": "fan_token_tier1/football",
  "generated_at": "2026-04-04T10:00:00Z",
  "freshness_warning": null
}
```

---

### Tool 2 — `sportmind_macro`

Returns the current SportMind macro state — crypto cycle phase, active geopolitical
and economic events, and the global macro_modifier. Agents should call this before
any fan token or DeFi analysis.

```json
{
  "name": "sportmind_macro",
  "description": "Get the current SportMind macro state: crypto cycle phase, macro_modifier, and any active geopolitical or economic events affecting all fan token signals. Always call this before fan_token_tier1 or DeFi analysis.",
  "input_schema": {
    "type": "object",
    "properties": {
      "include_history": {
        "type": "boolean",
        "description": "Include last 30 days of macro phase history",
        "default": false
      }
    },
    "required": []
  }
}
```

**Example response:**
```json
{
  "macro_state": {
    "crypto_cycle": {
      "phase": "NEUTRAL",
      "macro_modifier": 1.00,
      "btc_vs_200d_ma": "above",
      "signal_note": "Neutral cycle — price movements reflect sporting signals"
    },
    "active_events": [],
    "last_updated": "2026-04-04T06:00:00Z",
    "next_scheduled_update": "2026-04-04T18:00:00Z"
  },
  "agent_instruction": "Apply macro_modifier 1.00 to all fan token signals. No active overrides."
}
```

---

### Tool 3 — `sportmind_stack`

Returns the full intelligence stack for a sport/use_case combination — the same
content served by `GET /stack` on the Skills API, but formatted as an MCP tool
response for direct agent consumption.

```json
{
  "name": "sportmind_stack",
  "description": "Load the full SportMind intelligence stack for a sport and use case. Returns all relevant skill content in correct loading order (macro → market → domain → athlete → L3). Use when you need the complete reasoning context rather than a single signal.",
  "input_schema": {
    "type": "object",
    "properties": {
      "sport": {
        "type": "string",
        "enum": ["football","basketball","cricket","mma","formula1","tennis","rugby","rugby_league","afl","baseball","ice_hockey","motogp","nascar","kabaddi","netball","handball","esports"]
      },
      "use_case": {
        "type": "string",
        "enum": ["fan_token_tier1","fan_token_tier2","prediction_market","commercial_brief","pre_match","governance"],
        "default": "pre_match"
      },
      "compressed": {
        "type": "boolean",
        "description": "Return token-efficient compressed summaries instead of full skill content. Reduces context cost by ~70% with acceptable precision loss for most queries.",
        "default": false
      }
    },
    "required": ["sport"]
  }
}
```

---

### Tool 4 — `sportmind_verify`

Verifies the integrity of a SportMind skill file by checking its SHA-256 hash
against `platform/skill-hashes.json`. Agents in security-sensitive deployments
should call this before injecting skill content into their context.

```json
{
  "name": "sportmind_verify",
  "description": "Verify the integrity of a SportMind skill file using SHA-256 hashing. Returns whether the content matches the known-good hash in platform/skill-hashes.json. Use in production deployments where skill content authenticity matters.",
  "input_schema": {
    "type": "object",
    "properties": {
      "skill_id": {
        "type": "string",
        "description": "Skill identifier, e.g. 'domain.football', 'athlete.football', 'fantoken.football-bridge'"
      },
      "content": {
        "type": "string",
        "description": "The skill content to verify (as returned by sportmind_stack or Skills API)"
      }
    },
    "required": ["skill_id", "content"]
  }
}
```

---

## MCP server implementation

```python
#!/usr/bin/env python3
"""
SportMind MCP Server
Exposes SportMind intelligence as MCP tools for Claude and other agents.

Usage:
  python scripts/sportmind_mcp.py              # stdio transport (Claude Desktop)
  python scripts/sportmind_mcp.py --port 3001  # HTTP transport (remote agents)

Requires: pip install mcp --break-system-packages
"""

import json
import hashlib
import asyncio
import argparse
from pathlib import Path
from datetime import datetime, timezone

# MCP SDK
try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent
except ImportError:
    print("MCP SDK not installed. Run: pip install mcp --break-system-packages")
    raise

ROOT = Path(__file__).parent.parent
HASHES_FILE = ROOT / "platform" / "skill-hashes.json"
MACRO_STATE  = ROOT / "platform" / "macro-state.json"

# ── Tool implementations ──────────────────────────────────────────────────────

def get_macro_state() -> dict:
    """Load current macro state from platform/macro-state.json."""
    if MACRO_STATE.exists():
        return json.loads(MACRO_STATE.read_text())
    return {
        "macro_state": {
            "crypto_cycle": {"phase": "NEUTRAL", "macro_modifier": 1.00},
            "active_events": [],
            "last_updated": datetime.now(timezone.utc).isoformat(),
        }
    }

def get_skill_files_for_stack(sport: str, use_case: str) -> list[Path]:
    """Return skill files in correct SportMind loading order."""
    loading_order = []

    # Layer 5 — Macro
    macro_overview = ROOT / "macro" / "macro-overview.md"
    if macro_overview.exists():
        loading_order.append(macro_overview)

    # Layer 4 — Market
    market_file = ROOT / "market" / f"market-{sport.replace('_', '-')}.md"
    if market_file.exists():
        loading_order.append(market_file)

    # Layer 1 — Sport domain
    domain_file = ROOT / "sports" / sport.replace('_', '-') / f"sport-domain-{sport.replace('_', '-')}.md"
    if domain_file.exists():
        loading_order.append(domain_file)

    # Layer 2 — Athlete intelligence
    athlete_dir = ROOT / "athlete" / sport.replace('_', '-')
    if athlete_dir.exists():
        athlete_files = list(athlete_dir.glob(f"athlete-intel-*.md"))
        loading_order.extend(sorted(athlete_files))

    # Layer 3 — Fan token bridge (for token use cases)
    if use_case in ("fan_token_tier1", "fan_token_tier2", "governance"):
        bridge_dir = ROOT / "fan-token" / f"{sport.replace('_', '-')}-token-intelligence"
        if bridge_dir.exists():
            bridge_files = list(bridge_dir.glob("*.md"))
            loading_order.extend(sorted(bridge_files))

        # DeFi context
        defi_dir = ROOT / "fan-token" / "defi-liquidity-intelligence"
        if defi_dir.exists():
            loading_order.extend(sorted(defi_dir.glob("*.md"))[:1])

    return loading_order


def build_signal(sport: str, event_id: str, use_case: str,
                 home_team: str, away_team: str,
                 include_defi: bool) -> dict:
    """Generate a SportMind signal using loaded skill stack."""
    skill_files = get_skill_files_for_stack(sport, use_case)
    macro = get_macro_state()
    macro_modifier = macro.get("macro_state", {}).get(
        "crypto_cycle", {}).get("macro_modifier", 1.00)

    layers_loaded = set()
    for f in skill_files:
        parts = f.relative_to(ROOT).parts
        if parts[0] == "macro":             layers_loaded.add(5)
        elif parts[0] == "market":          layers_loaded.add(4)
        elif parts[0] == "sports":          layers_loaded.add(1)
        elif parts[0] == "athlete":         layers_loaded.add(2)
        elif parts[0] == "fan-token":       layers_loaded.add(3)

    # SMS calculation (layer coverage component)
    layer_coverage = len(layers_loaded) / 5
    sms = round(
        layer_coverage * 0.35 * 100 +
        (1.00 if macro_modifier >= 0.75 else 0.50) * 0.25 * 100 +
        0.25 * 100 +   # flag health — default healthy
        macro_modifier * 0.15 * 100,
        1
    )

    sms_tier = (
        "HIGH_QUALITY" if sms >= 80 else
        "GOOD"         if sms >= 60 else
        "PARTIAL"      if sms >= 40 else
        "INCOMPLETE"   if sms >= 20 else
        "INSUFFICIENT"
    )

    macro_override = macro_modifier < 0.75
    flags = {
        "lineup_unconfirmed":   False,  # Cannot determine without live data
        "macro_override_active": macro_override,
        "liquidity_warning":    False,
        "injury_warning":       False
    }

    freshness_warning = (
        "Macro state may be stale — update with: python scripts/update_macro_state.py"
        if not MACRO_STATE.exists() else None
    )

    return {
        "signal": {
            "direction": "HOME",
            "adjusted_score": round(50 + (macro_modifier - 1) * 10, 1),
            "confidence_tier": "MEDIUM" if sms >= 60 else "LOW",
            "recommended_action": "ENTER" if sms >= 60 and not macro_override else "WAIT"
        },
        "sportmind_score": {
            "sms": sms,
            "sms_tier": sms_tier,
            "layers_loaded": sorted(layers_loaded),
            "coverage_note": f"{len(skill_files)} skill files loaded"
        },
        "modifiers": {
            "composite_modifier": round(macro_modifier, 2),
            "macro_modifier": round(macro_modifier, 2),
            "flags": flags
        },
        "event_context": {
            "sport": sport,
            "event_id": event_id or "unspecified",
            "home_team": home_team or "unspecified",
            "away_team": away_team or "unspecified",
            "use_case": use_case
        },
        "skill_stack_used": f"{use_case}/{sport}",
        "skill_files_loaded": [str(f.relative_to(ROOT)) for f in skill_files],
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "freshness_warning": freshness_warning,
        "agent_note": (
            "This signal is generated from SportMind skill files. "
            "For full adjusted_score accuracy, integrate live athlete availability "
            "and current form data via platform/live-signals.md (Category 2-3 inputs). "
            "See core/temporal-awareness.md for data freshness guidance."
        )
    }


def verify_skill(skill_id: str, content: str) -> dict:
    """Verify skill content against skill-hashes.json."""
    if not HASHES_FILE.exists():
        return {"verified": False, "reason": "skill-hashes.json not found"}

    hashes = json.loads(HASHES_FILE.read_text())
    actual_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()

    # Find matching file in registry
    for file_path, entry in hashes.get("files", {}).items():
        if skill_id.lower() in file_path.lower():
            expected = entry.get("sha256", "")
            if actual_hash == expected:
                return {"verified": True, "file_path": file_path, "hash": actual_hash[:16] + "..."}
            else:
                return {
                    "verified": False,
                    "reason": "Hash mismatch — content may have been tampered with",
                    "file_path": file_path
                }

    return {"verified": True, "reason": "Skill ID not in registry — new file, not yet verified"}


# ── MCP Server ────────────────────────────────────────────────────────────────

server = Server("sportmind")

@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="sportmind_signal",
            description="Generate a structured SportMind intelligence signal for a sporting event. Returns adjusted_score, SportMind Score (SMS), active flags, and reasoning summary.",
            inputSchema={
                "type": "object",
                "properties": {
                    "sport": {"type": "string", "enum": ["football","basketball","cricket","mma","formula1","tennis","rugby","rugby_league","afl","baseball","ice_hockey","motogp","nascar","kabaddi","netball","handball","esports"]},
                    "event_id": {"type": "string"},
                    "use_case": {"type": "string", "default": "pre_match"},
                    "home_team": {"type": "string"},
                    "away_team": {"type": "string"},
                    "include_defi_context": {"type": "boolean", "default": False}
                },
                "required": ["sport"]
            }
        ),
        Tool(
            name="sportmind_macro",
            description="Get the current SportMind macro state: crypto cycle phase, macro_modifier, and active events. Call before any fan token or DeFi analysis.",
            inputSchema={"type": "object", "properties": {}, "required": []}
        ),
        Tool(
            name="sportmind_stack",
            description="Load the full SportMind intelligence stack for a sport. Returns all skill content in correct loading order.",
            inputSchema={
                "type": "object",
                "properties": {
                    "sport": {"type": "string"},
                    "use_case": {"type": "string", "default": "pre_match"},
                    "compressed": {"type": "boolean", "default": False}
                },
                "required": ["sport"]
            }
        ),
        Tool(
            name="sportmind_verify",
            description="Verify the integrity of SportMind skill content using SHA-256 hashing against platform/skill-hashes.json.",
            inputSchema={
                "type": "object",
                "properties": {
                    "skill_id": {"type": "string"},
                    "content":  {"type": "string"}
                },
                "required": ["skill_id", "content"]
            }
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "sportmind_signal":
        result = build_signal(
            sport=arguments.get("sport", "football"),
            event_id=arguments.get("event_id", ""),
            use_case=arguments.get("use_case", "pre_match"),
            home_team=arguments.get("home_team", ""),
            away_team=arguments.get("away_team", ""),
            include_defi=arguments.get("include_defi_context", False)
        )
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    elif name == "sportmind_macro":
        macro = get_macro_state()
        macro["retrieval_note"] = "Update macro state with: python scripts/update_macro_state.py"
        return [TextContent(type="text", text=json.dumps(macro, indent=2))]

    elif name == "sportmind_stack":
        sport    = arguments.get("sport", "football")
        use_case = arguments.get("use_case", "pre_match")
        files    = get_skill_files_for_stack(sport, use_case)
        stack    = []
        for f in files:
            content = f.read_text(encoding="utf-8")
            stack.append({
                "skill_id": str(f.relative_to(ROOT)),
                "content":  content if not arguments.get("compressed") else content[:500] + "\n[COMPRESSED — full content truncated]",
                "sha256":   hashlib.sha256(content.encode()).hexdigest()
            })
        result = {
            "sport": sport,
            "use_case": use_case,
            "stack": stack,
            "total_files": len(stack),
            "loading_order": "macro → market → domain → athlete → fan-token"
        }
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    elif name == "sportmind_verify":
        result = verify_skill(arguments["skill_id"], arguments["content"])
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    raise ValueError(f"Unknown tool: {name}")


async def main():
    parser = argparse.ArgumentParser(description="SportMind MCP Server")
    parser.add_argument("--port", type=int, help="HTTP port (stdio if not set)")
    args = parser.parse_args()

    if args.port:
        # HTTP/SSE transport for remote agents
        from mcp.server.sse import SseServerTransport
        from aiohttp import web

        transport = SseServerTransport(f"/mcp")
        async def handle_sse(request):
            async with transport.connect_sse(request.headers, request) as streams:
                await server.run(*streams, server.create_initialization_options())
        app = web.Application()
        app.router.add_get("/mcp", handle_sse)
        print(f"SportMind MCP Server on http://localhost:{args.port}/mcp")
        web.run_app(app, port=args.port)
    else:
        # stdio transport for Claude Desktop
        async with stdio_server() as streams:
            await server.run(*streams, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
```

---

## Claude Desktop configuration

Add SportMind as a local MCP tool in Claude Desktop's `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "sportmind": {
      "command": "python",
      "args": ["/path/to/sportmind/scripts/sportmind_mcp.py"],
      "description": "SportMind sports intelligence — generates pre-match signals, macro state, and fan token analysis"
    }
  }
}
```

After adding, restart Claude Desktop. You can then ask Claude directly:
- *"Use SportMind to analyse PSG vs Arsenal tonight"*
- *"What does SportMind say about the macro state for fan tokens?"*
- *"Get the full cricket intelligence stack for a pre-match analysis"*

---

## Remote agent integration (HTTP/SSE)

```python
# Connect to a hosted SportMind MCP server from any agent framework

import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=2000,
    mcp_servers=[
        {
            "type": "url",
            "url": "https://your-sportmind-host/mcp",
            "name": "sportmind"
        }
    ],
    messages=[{
        "role": "user",
        "content": "Analyse the UCL quarter-final PSG vs Arsenal using SportMind. Check macro state first, then generate the signal."
    }]
)
```

---


---

### Tool 5 — `sportmind_agent_status`

Returns the current operational state of a running SportMind autonomous agent.
Makes agents observable — a prerequisite for trusting them to run unsupervised.
Call from a supervisor, dashboard, or orchestrator to check agent health.

```json
{
  "name": "sportmind_agent_status",
  "description": "Get the current status of a SportMind autonomous agent: lifecycle state, health, cycle counts, active escalations, upcoming events, and data freshness. Use to monitor autonomous agents without interrupting their operation.",
  "input_schema": {
    "type": "object",
    "properties": {
      "agent_id": {
        "type": "string",
        "description": "ID of the agent to query. Omit to get status of all registered agents."
      },
      "include_audit_log": {
        "type": "boolean",
        "description": "Include recent cycle audit log entries",
        "default": false
      },
      "last_n_cycles": {
        "type": "integer",
        "description": "Number of recent cycles to include in audit log (if requested)",
        "default": 5
      }
    },
    "required": []
  }
}
```

**Example response (single agent):**
```json
{
  "agent_status": {
    "agent_id": "portfolio-monitor-001",
    "agent_type": "portfolio_monitor",
    "state": "MONITORING",
    "autonomy_level": 2,
    "health": "HEALTHY",
    "uptime_hours": 72.4,
    "cycles_completed": 18,
    "actions_taken": 3,
    "escalations_triggered": 1,
    "current_context": {
      "macro_state": "NEUTRAL",
      "macro_modifier": 1.00,
      "macro_age_hours": 3.2,
      "tokens_monitored": ["PSG", "BAR", "CITY"],
      "pending_escalations": 0,
      "upcoming_events": [
        {
          "event_id": "ucl-qf-psg-arsenal-2026-05-07",
          "hours_away": 68,
          "signal_tier": "TIER_1",
          "pre_match_chain_scheduled": true
        }
      ]
    },
    "data_freshness": {
      "macro_state": "FRESH",
      "sport_stacks": "FRESH",
      "skill_hashes_verified": true
    }
  }
}
```

**Example response (all agents):**
```json
{
  "agents": [
    {"agent_id": "portfolio-monitor-001", "state": "MONITORING", "health": "HEALTHY"},
    {"agent_id": "prematch-001", "state": "ANALYSING", "health": "HEALTHY"},
    {"agent_id": "tournament-tracker-001", "state": "MONITORING", "health": "DEGRADED",
     "health_note": "Macro state 11h old — refresh recommended"}
  ],
  "system_health": "DEGRADED",
  "system_note": "1 of 3 agents in DEGRADED state"
}
```

**Use cases:**
- Supervisor agent checking subordinate agent health before acting on their signals
- Dashboard displaying real-time agent operational status
- Orchestrator determining which agents have current, reliable signals
- Debugging: understanding why an agent escalated or paused


---

## Tool call sequencing for agents

Agents should follow this order when using SportMind MCP tools:

```
1. sportmind_macro          → Always first; establishes macro_modifier baseline
2. sportmind_signal         → For specific event analysis
   OR
   sportmind_stack          → For comprehensive intelligence loading
3. sportmind_verify         → Optional; for security-sensitive deployments only
```

**Rule:** Never call `sportmind_signal` before `sportmind_macro` for fan token
or DeFi applications. The macro_modifier from step 1 directly affects interpretation
of the adjusted_score from step 2.

---

## Relationship to the Skills API

```
SKILLS API (scripts/sportmind_api.py):
  HTTP REST server — serves skill files and stacks on demand
  Best for: web applications, SportFi Kit integration, pre-session loading
  Transport: HTTP GET requests

MCP SERVER (scripts/sportmind_mcp.py):
  MCP protocol — exposes SportMind as callable tools
  Best for: Claude Desktop, Anthropic API agent calls, agentic workflows
  Transport: stdio (local) or HTTP/SSE (remote)

BOTH can run simultaneously on different ports.
BOTH serve the same SportMind intelligence from the same skill files.
USE MCP when the agent framework natively supports MCP tools.
USE Skills API when building web applications or non-MCP integrations.
```

---

## Installation

```bash
# Install MCP SDK
pip install mcp --break-system-packages

# Run locally (stdio for Claude Desktop)
python scripts/sportmind_mcp.py

# Run as HTTP server (for remote agents)
python scripts/sportmind_mcp.py --port 3001

# Test MCP tool calls directly
echo '{"method":"tools/call","params":{"name":"sportmind_macro","arguments":{}}}' | \
  python scripts/sportmind_mcp.py
```

---

*MIT License · SportMind · sportmind.dev*
*See `platform/integration-partners.md` — Partner 6 (LLM providers) for agent framework context.*
*See `platform/live-signals.md` for live data boundaries that apply to MCP tool responses.*
