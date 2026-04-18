#!/usr/bin/env python3
"""
SportMind Agent Lifecycle MCP Server v3.71.0
Manages running SportMind autonomous agents — for orchestrator agents
and multi-agent system coordinators. Enables an orchestrator to spin
up, monitor, receive escalations from, and pause SportMind agents
without manual intervention.

Five tools:
  al_agent_start     — register and initialise a new SportMind agent
  al_agent_status    — get current operational state of a running agent
  al_escalation_inbox— retrieve pending escalations requiring human review
  al_memory_write    — write a signal or context to agent persistent memory
  al_memory_read     — read from agent persistent memory (cross-session)

Usage:
  pip install mcp aiohttp
  python scripts/sportmind_al_mcp.py              # stdio
  python scripts/sportmind_al_mcp.py --http        # HTTP/SSE port 3007
"""

import json
import asyncio
import argparse
from pathlib import Path
from datetime import datetime, timezone

ROOT    = Path(__file__).parent.parent
VERSION = "3.77.0"

# In-process agent registry (for stdio session; HTTP mode persists longer)
_AGENT_REGISTRY = {}
_ESCALATION_QUEUE = {}
_AGENT_MEMORY = {}

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def tool_agent_start(agent_id: str, agent_type: str, terminal_goal: str,
                      sport: str, token: str, autonomy_level: int):
    """Register and initialise a new SportMind agent."""

    if agent_id in _AGENT_REGISTRY:
        existing = _AGENT_REGISTRY[agent_id]
        return {
            "result": "ALREADY_REGISTERED",
            "agent_id": agent_id,
            "registered_at": existing["registered_at"],
            "status": existing["status"],
        }

    agent_types = {
        "pre_match":     {"description": "Pre-match signal agent", "skills": ["sports/","athlete/","core/reasoning-patterns.md"]},
        "fan_token":     {"description": "Fan token commercial monitor", "skills": ["fan-token/","macro/","platform/fraud-signal-intelligence.md"]},
        "portfolio":     {"description": "Multi-token portfolio monitor", "skills": ["fan-token/","macro/","platform/monitoring-alerts.md"]},
        "scouting":      {"description": "Transfer scouting agent (Pattern 10)", "skills": ["core/athlete-decision-intelligence.md","core/spatial-game-intelligence.md"]},
        "live_match":    {"description": "Live match event monitor (Pattern 12)", "skills": ["examples/agentic-workflows/live-match-agent.md"]},
        "governance":    {"description": "Fan token governance delegate", "skills": ["fan-token/sports-governance-intelligence/"]},
        "fraud_monitor": {"description": "Pre-match fraud signal scanner", "skills": ["platform/fraud-signal-intelligence.md"]},
        "orchestrator":  {"description": "Multi-agent orchestrator", "skills": ["core/multi-agent-coordination.md","core/multi-agent-context-sharing.md"]},
    }

    agent_info = agent_types.get(agent_type.lower(), {
        "description": f"Custom agent: {agent_type}",
        "skills": ["core/sportmind-purpose-and-context.md"],
    })

    agent = {
        "agent_id":       agent_id,
        "agent_type":     agent_type,
        "description":    agent_info["description"],
        "terminal_goal":  terminal_goal,
        "sport":          sport or "multi-sport",
        "token":          token or None,
        "autonomy_level": min(4, max(0, autonomy_level)),
        "status":         "INITIALISED",
        "registered_at":  now_iso(),
        "last_active":    now_iso(),
        "cycles":         0,
        "signals_produced": 0,
        "escalations":    0,
        "skills_to_load": agent_info["skills"],
        "boundary_enforced": True,
    }

    _AGENT_REGISTRY[agent_id] = agent
    _ESCALATION_QUEUE[agent_id] = []
    _AGENT_MEMORY[agent_id]     = {}

    autonomy_labels = {
        0: "Level 0 — Supervised (human approves all actions)",
        1: "Level 1 — Advisory (human approves before acting)",
        2: "Level 2 — Semi-Auto (agent acts on standard signals, escalates edge cases)",
        3: "Level 3 — Auto with Review (agent acts autonomously, human reviews logs)",
        4: "Level 4 — Fully Auto (experimental — use with extreme caution)",
    }

    return {
        "result":          "REGISTERED",
        "agent_id":        agent_id,
        "agent":           agent,
        "autonomy_label":  autonomy_labels[agent["autonomy_level"]],
        "agent_boundary":  "This agent produces intelligence only. Financial execution, governance votes, and contract calls are outside scope by architectural design.",
        "loading_instructions": f"Load skills in order: {' → '.join(agent_info['skills'][:3])}",
        "framework_reference": "core/autonomous-agent-framework.md",
        "sportmind_version": VERSION,
    }

def tool_agent_status(agent_id: str, include_memory_summary: bool):
    """Get operational state of a running agent."""

    if agent_id not in _AGENT_REGISTRY:
        return {
            "error": f"Agent '{agent_id}' not registered in this session.",
            "hint":  "Use al_agent_start to register the agent, or it may be registered in a different session.",
            "registered_agents": list(_AGENT_REGISTRY.keys()),
        }

    agent = _AGENT_REGISTRY[agent_id]
    escalations = _ESCALATION_QUEUE.get(agent_id, [])
    memory = _AGENT_MEMORY.get(agent_id, {})

    status = {
        "agent_id":        agent_id,
        "status":          agent["status"],
        "agent_type":      agent["agent_type"],
        "terminal_goal":   agent["terminal_goal"],
        "autonomy_level":  agent["autonomy_level"],
        "sport":           agent["sport"],
        "token":           agent["token"],
        "cycles":          agent["cycles"],
        "signals_produced":agent["signals_produced"],
        "escalations_pending": len(escalations),
        "last_active":     agent["last_active"],
        "registered_at":   agent["registered_at"],
        "boundary_enforced": agent["boundary_enforced"],
        "sportmind_version": VERSION,
        "assessed_at":     now_iso(),
    }

    if include_memory_summary:
        status["memory_summary"] = {
            "keys":  list(memory.keys()),
            "count": len(memory),
            "last_write": memory.get("_last_write", "none"),
        }

    if escalations:
        status["escalation_preview"] = escalations[-1] if escalations else None
        status["escalation_action"]  = "Call al_escalation_inbox to review all pending escalations"

    return status

def tool_escalation_inbox(agent_id: str, resolve_id: str):
    """Retrieve and optionally resolve pending escalations."""

    if agent_id not in _ESCALATION_QUEUE:
        return {
            "agent_id": agent_id,
            "pending":  0,
            "escalations": [],
            "note": "No escalation queue found. Agent may not be registered in this session.",
        }

    queue = _ESCALATION_QUEUE[agent_id]

    if resolve_id:
        before = len(queue)
        _ESCALATION_QUEUE[agent_id] = [e for e in queue if e.get("escalation_id") != resolve_id]
        resolved = before - len(_ESCALATION_QUEUE[agent_id])
        return {
            "agent_id":    agent_id,
            "action":      "RESOLVED",
            "escalation_id": resolve_id,
            "resolved":    resolved,
            "remaining":   len(_ESCALATION_QUEUE[agent_id]),
        }

    # Format escalations for review
    formatted = []
    for i, esc in enumerate(queue, 1):
        formatted.append({
            "index":           i,
            "escalation_id":   esc.get("escalation_id", f"esc_{i}"),
            "type":            esc.get("type", "UNSPECIFIED"),
            "reason":          esc.get("reason", ""),
            "signal":          esc.get("signal", {}),
            "created_at":      esc.get("created_at", "unknown"),
            "requires_human":  True,
            "resolve_action":  f"Call al_escalation_inbox with resolve_id='{esc.get('escalation_id', f'esc_{i}')}' to mark as reviewed",
        })

    if not formatted:
        formatted_msg = "No pending escalations."
    else:
        formatted_msg = f"{len(formatted)} escalation(s) pending human review."

    return {
        "agent_id":    agent_id,
        "pending":     len(formatted),
        "message":     formatted_msg,
        "escalations": formatted,
        "escalation_types": {
            "MACRO_OVERRIDE":     "Macro state override active — all signals suspended",
            "SMS_BELOW_THRESHOLD":"Signal quality insufficient for autonomous action",
            "FRAUD_COMPROMISED":  "MRS 75+ — signal integrity cannot be trusted",
            "INJURY_RISK_HIGH":   "Key player ARI < 0.65 — requires human review",
            "LINEUP_UNCONFIRMED": "Lineup not confirmed at T-2h — uncertainty flag",
            "MULTI_FLAG":         "Multiple concern flags active simultaneously",
        },
        "sportmind_version": VERSION,
        "assessed_at": now_iso(),
    }

def tool_memory_write(agent_id: str, key: str, value: str, ttl_hours: int):
    """Write a signal or context item to agent memory."""

    if agent_id not in _AGENT_MEMORY:
        _AGENT_MEMORY[agent_id] = {}

    if len(_AGENT_MEMORY[agent_id]) >= 200:
        # Evict oldest non-system entries
        non_sys = [k for k in _AGENT_MEMORY[agent_id] if not k.startswith("_")]
        if non_sys:
            del _AGENT_MEMORY[agent_id][non_sys[0]]

    _AGENT_MEMORY[agent_id][key] = {
        "value":      value,
        "written_at": now_iso(),
        "ttl_hours":  ttl_hours or None,
        "expires_at": None,  # TTL enforcement in production layer
    }
    _AGENT_MEMORY[agent_id]["_last_write"] = now_iso()

    # Update agent last_active if registered
    if agent_id in _AGENT_REGISTRY:
        _AGENT_REGISTRY[agent_id]["last_active"] = now_iso()

    return {
        "result":    "WRITTEN",
        "agent_id":  agent_id,
        "key":       key,
        "ttl_hours": ttl_hours,
        "memory_keys_total": len([k for k in _AGENT_MEMORY[agent_id] if not k.startswith("_")]),
        "note":      "Memory persists for the duration of this server session. For cross-session persistence, implement platform/memory-integration.md",
        "sportmind_version": VERSION,
    }

def tool_memory_read(agent_id: str, key: str, list_keys: bool):
    """Read from agent memory."""

    if agent_id not in _AGENT_MEMORY:
        return {
            "agent_id": agent_id,
            "error":    "No memory found for this agent in this session.",
            "hint":     "Memory is session-scoped. For cross-session persistence, implement platform/memory-integration.md",
        }

    memory = _AGENT_MEMORY[agent_id]

    if list_keys:
        user_keys = {k: v.get("written_at") for k, v in memory.items() if not k.startswith("_")}
        return {
            "agent_id":  agent_id,
            "keys":      user_keys,
            "count":     len(user_keys),
            "sportmind_version": VERSION,
        }

    if key:
        entry = memory.get(key)
        if not entry:
            return {"agent_id": agent_id, "key": key, "error": "Key not found in agent memory"}
        return {
            "agent_id":  agent_id,
            "key":       key,
            "value":     entry["value"],
            "written_at":entry["written_at"],
            "ttl_hours": entry["ttl_hours"],
            "sportmind_version": VERSION,
        }

    # Return last 5 entries
    user_entries = {k: v for k, v in memory.items() if not k.startswith("_")}
    recent = dict(list(user_entries.items())[-5:])
    return {
        "agent_id":    agent_id,
        "recent_entries": recent,
        "total_keys":  len(user_entries),
        "sportmind_version": VERSION,
    }

# ── MCP wiring ─────────────────────────────────────────────────────────────────

TOOL_DESCRIPTIONS = {
    "al_agent_start":     "Register and initialise a new SportMind agent with a terminal goal, sport, token, and autonomy level.",
    "al_agent_status":    "Get operational state of a registered agent — cycles, signals, escalations, last active.",
    "al_escalation_inbox":"Retrieve pending escalations from a running agent that require human review or approval.",
    "al_memory_write":    "Write a signal, result, or context item to agent persistent memory (session-scoped).",
    "al_memory_read":     "Read from agent memory by key, or list all stored keys for an agent.",
}

TOOL_SCHEMAS = {
    "al_agent_start": {
        "type": "object",
        "properties": {
            "agent_id":       {"type":"string","description":"Unique agent identifier (e.g. 'afc-fan-token-monitor-001')"},
            "agent_type":     {"type":"string","description":"Agent type","enum":["pre_match","fan_token","portfolio","scouting","live_match","governance","fraud_monitor","orchestrator"],"default":"fan_token"},
            "terminal_goal":  {"type":"string","description":"The agent's top-level objective (e.g. 'Monitor $AFC fan token commercial signals')"},
            "sport":          {"type":"string","description":"Primary sport focus","default":"football"},
            "token":          {"type":"string","description":"Primary fan token ticker (if applicable)","default":""},
            "autonomy_level": {"type":"integer","description":"Autonomy level 0-4 (0=supervised, 1=advisory, 2=semi-auto, 3=auto+review, 4=fully auto)","minimum":0,"maximum":4,"default":1},
        },
        "required": ["agent_id","terminal_goal"],
    },
    "al_agent_status": {
        "type": "object",
        "properties": {
            "agent_id":              {"type":"string","description":"Agent identifier"},
            "include_memory_summary":{"type":"boolean","description":"Include memory key summary","default":False},
        },
        "required": ["agent_id"],
    },
    "al_escalation_inbox": {
        "type": "object",
        "properties": {
            "agent_id":   {"type":"string","description":"Agent identifier"},
            "resolve_id": {"type":"string","description":"Escalation ID to mark as resolved (optional)","default":""},
        },
        "required": ["agent_id"],
    },
    "al_memory_write": {
        "type": "object",
        "properties": {
            "agent_id":  {"type":"string","description":"Agent identifier"},
            "key":       {"type":"string","description":"Memory key (e.g. 'last_signal_afc', 'path2_status')"},
            "value":     {"type":"string","description":"Value to store (JSON string or plain text)"},
            "ttl_hours": {"type":"integer","description":"Time-to-live in hours (0 = no expiry)","default":0},
        },
        "required": ["agent_id","key","value"],
    },
    "al_memory_read": {
        "type": "object",
        "properties": {
            "agent_id":  {"type":"string","description":"Agent identifier"},
            "key":       {"type":"string","description":"Specific key to read (leave empty to see recent entries)","default":""},
            "list_keys": {"type":"boolean","description":"List all memory keys for this agent","default":False},
        },
        "required": ["agent_id"],
    },
}

async def _handle(name: str, args: dict):
    if name == "al_agent_start":
        return tool_agent_start(args.get("agent_id",""), args.get("agent_type","fan_token"),
            args.get("terminal_goal",""), args.get("sport","football"),
            args.get("token",""), args.get("autonomy_level",1))
    elif name == "al_agent_status":
        return tool_agent_status(args.get("agent_id",""), args.get("include_memory_summary",False))
    elif name == "al_escalation_inbox":
        return tool_escalation_inbox(args.get("agent_id",""), args.get("resolve_id",""))
    elif name == "al_memory_write":
        return tool_memory_write(args.get("agent_id",""), args.get("key",""),
            args.get("value",""), args.get("ttl_hours",0))
    elif name == "al_memory_read":
        return tool_memory_read(args.get("agent_id",""), args.get("key",""), args.get("list_keys",False))
    return {"error": f"Unknown tool: {name}"}


async def run_stdio():
    try:
        from mcp.server import Server
        from mcp.server.stdio import stdio_server
        from mcp.types import Tool
    except ImportError:
        print("ERROR: pip install mcp", flush=True); return

    server = Server("sportmind-agent-lifecycle")

    @server.list_tools()
    async def list_tools():
        return [Tool(name=n, description=TOOL_DESCRIPTIONS[n], inputSchema=TOOL_SCHEMAS[n]) for n in TOOL_SCHEMAS]

    @server.call_tool()
    async def call_tool(name, arguments):
        from mcp.types import TextContent
        return [TextContent(type="text", text=json.dumps(await _handle(name, arguments), indent=2))]

    async with stdio_server() as streams:
        await server.run(*streams, server.create_initialization_options())


async def run_http(port: int):
    try:
        from mcp.server import Server
        from mcp.server.sse import SseServerTransport
        from mcp.types import Tool
        from aiohttp import web
    except ImportError:
        print("ERROR: pip install mcp aiohttp", flush=True); return

    server = Server("sportmind-agent-lifecycle")

    @server.list_tools()
    async def list_tools():
        return [Tool(name=n, description=TOOL_DESCRIPTIONS[n], inputSchema=TOOL_SCHEMAS[n]) for n in TOOL_SCHEMAS]

    @server.call_tool()
    async def call_tool(name, arguments):
        from mcp.types import TextContent
        return [TextContent(type="text", text=json.dumps(await _handle(name, arguments), indent=2))]

    transport = SseServerTransport("/mcp")

    async def handle_sse(req):
        async with transport.connect_sse(req.headers, req) as streams:
            await server.run(*streams, server.create_initialization_options())

    async def handle_health(req):
        registered = len(_AGENT_REGISTRY)
        pending_esc = sum(len(q) for q in _ESCALATION_QUEUE.values())
        return web.Response(content_type="application/json", text=json.dumps({
            "service":          "SportMind Agent Lifecycle MCP",
            "version":          VERSION,
            "tools":            list(TOOL_SCHEMAS.keys()),
            "registered_agents":registered,
            "pending_escalations": pending_esc,
        }, indent=2))

    app = web.Application()
    app.router.add_get("/mcp",    handle_sse)
    app.router.add_get("/health", handle_health)
    app.router.add_get("/",       handle_health)

    print(f"SportMind Agent Lifecycle MCP v{VERSION} — port {port}", flush=True)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "0.0.0.0", port).start()
    try:
        await asyncio.Event().wait()
    except (KeyboardInterrupt, asyncio.CancelledError):
        pass
    finally:
        await runner.cleanup()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SportMind Agent Lifecycle MCP")
    parser.add_argument("--http", action="store_true")
    parser.add_argument("--port", type=int, default=3007)
    args = parser.parse_args()
    asyncio.run(run_http(args.port) if args.http else run_stdio())
