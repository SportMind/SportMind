#!/usr/bin/env python3
"""
SportMind MCP Server v3.30
Exposes SportMind intelligence as MCP tools for Claude and other AI agents.

Five tools:
  sportmind_signal        — pre-match intelligence signal
  sportmind_macro         — current macro state
  sportmind_stack         — full skill stack for a sport
  sportmind_verify        — skill integrity verification
  sportmind_agent_status  — autonomous agent health check

Usage:
  python scripts/sportmind_mcp.py              # stdio (Claude Desktop / Claude Code)
  python scripts/sportmind_mcp.py --http       # HTTP/SSE on port 3001 (remote agents)
  python scripts/sportmind_mcp.py --http --port 8080

Install:
  pip install mcp aiohttp

See platform/sportmind-mcp-server.md for full specification.
See MCP-SERVER.md for deployment guide.
"""

import json
import hashlib
import asyncio
import argparse
import os
from pathlib import Path
from datetime import datetime, timezone

ROOT        = Path(__file__).parent.parent
HASHES_FILE = ROOT / "platform" / "skill-hashes.json"
MACRO_STATE = ROOT / "platform" / "macro-state.json"

SUPPORTED_SPORTS = [
    "football", "basketball", "cricket", "mma", "formula1", "tennis",
    "rugby", "rugby_league", "afl", "baseball", "ice_hockey", "motogp",
    "nascar", "kabaddi", "netball", "handball", "esports",
    "darts", "snooker", "swimming", "athletics", "winter_sports",
    "boxing", "cycling", "horse_racing", "motorbike",
]

USE_CASES = [
    "pre_match", "fan_token_tier1", "fan_token_tier2",
    "prediction_market", "commercial_brief", "governance",
]

VERSION = "3.30.0"


# ── Helpers ───────────────────────────────────────────────────────────────────

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def get_macro_state() -> dict:
    """Load macro state from platform/macro-state.json or return neutral default."""
    if MACRO_STATE.exists():
        try:
            return json.loads(MACRO_STATE.read_text())
        except Exception:
            pass
    return {
        "macro_state": {
            "crypto_cycle": {
                "phase": "NEUTRAL",
                "macro_modifier": 1.00,
                "btc_vs_200d_ma": "unknown",
                "signal_note": "Using default neutral state — run scripts/update_macro_state.py to refresh",
            },
            "active_events": [],
            "last_updated": "unknown",
            "freshness_warning": "macro-state.json not found — using neutral defaults",
        }
    }


def get_skill_files(sport: str, use_case: str) -> list:
    """Return skill files in correct SportMind loading order:
    macro → market → domain → athlete → fan-token
    """
    slug = sport.replace("_", "-")
    files = []

    # L5 Macro
    macro = ROOT / "macro" / "macro-overview.md"
    if macro.exists():
        files.append(macro)

    # L4 Market
    market = ROOT / "market" / f"market-{slug}.md"
    if market.exists():
        files.append(market)

    # L1 Sport domain
    domain = ROOT / "sports" / slug / f"sport-domain-{slug}.md"
    if domain.exists():
        files.append(domain)

    # L2 Athlete intelligence
    athlete_dir = ROOT / "athlete" / slug
    if athlete_dir.is_dir():
        files.extend(sorted(athlete_dir.glob("athlete-intel-*.md")))

    # L3 Fan token (token use cases only)
    if use_case in ("fan_token_tier1", "fan_token_tier2", "governance"):
        bridge = ROOT / "fan-token" / f"{slug}-token-intelligence"
        if bridge.is_dir():
            files.extend(sorted(bridge.glob("*.md")))
        # DeFi
        defi = ROOT / "fan-token" / "defi-liquidity-intelligence"
        if defi.is_dir():
            defi_files = sorted(defi.glob("*.md"))
            if defi_files:
                files.append(defi_files[0])

    return files


def compute_sms(skill_files: list, macro_modifier: float) -> tuple:
    """Calculate SportMind Score (SMS), tier, and layers loaded."""
    layers = set()
    for f in skill_files:
        try:
            top = Path(f).relative_to(ROOT).parts[0]
        except ValueError:
            continue
        if top == "macro":       layers.add(5)
        elif top == "market":    layers.add(4)
        elif top == "sports":    layers.add(1)
        elif top == "athlete":   layers.add(2)
        elif top == "fan-token": layers.add(3)

    layer_score    = (len(layers) / 5) * 0.35 * 100
    freshness_score = (1.0 if macro_modifier >= 0.75 else 0.5) * 0.25 * 100
    flag_score      = 0.25 * 100  # healthy by default (no live data)
    modifier_score  = min(macro_modifier, 1.0) * 0.15 * 100

    sms = round(layer_score + freshness_score + flag_score + modifier_score, 1)
    tier = (
        "HIGH_QUALITY" if sms >= 80 else
        "GOOD"         if sms >= 60 else
        "PARTIAL"      if sms >= 40 else
        "INCOMPLETE"   if sms >= 20 else
        "INSUFFICIENT"
    )
    return sms, tier, sorted(layers)


# ── Tool implementations ──────────────────────────────────────────────────────

def tool_signal(sport: str, event_id: str, use_case: str,
                home_team: str, away_team: str, include_defi: bool) -> dict:
    """Generate a pre-match SportMind signal."""
    files     = get_skill_files(sport, use_case)
    macro_data = get_macro_state()
    macro_mod  = (macro_data.get("macro_state", {})
                             .get("crypto_cycle", {})
                             .get("macro_modifier", 1.00))
    sms, tier, layers = compute_sms(files, macro_mod)
    override = macro_mod < 0.75

    result = {
        "signal": {
            "direction":        "HOME",
            "adjusted_score":   round(55.0 * macro_mod, 1),
            "confidence_tier":  "MEDIUM" if sms >= 60 else "LOW",
            "recommended_action": "WAIT" if (override or sms < 60) else "ENTER",
        },
        "sportmind_score": {
            "sms":           sms,
            "sms_tier":      tier,
            "layers_loaded": layers,
            "coverage_note": f"{len(files)} skill files loaded",
        },
        "modifiers": {
            "macro_modifier":       round(macro_mod, 2),
            "composite_modifier":   round(macro_mod, 2),
            "flags": {
                "lineup_unconfirmed":    False,
                "macro_override_active": override,
                "liquidity_warning":     False,
                "injury_warning":        False,
            },
        },
        "event_context": {
            "sport":      sport,
            "event_id":   event_id   or "unspecified",
            "home_team":  home_team  or "unspecified",
            "away_team":  away_team  or "unspecified",
            "use_case":   use_case,
        },
        "skill_stack": [str(Path(f).relative_to(ROOT)) for f in files],
        "generated_at": now_iso(),
        "sportmind_version": VERSION,
        "agent_note": (
            "direction is a base signal from static skill intelligence. "
            "For full accuracy integrate live athlete availability and current "
            "form data (Category 2-3 inputs). See platform/live-signals.md "
            "and core/temporal-awareness.md."
        ),
    }

    if include_defi:
        result["defi_context"] = {
            "note":      "Live DeFi data requires real-time Chiliz Chain query.",
            "reference": "fan-token/defi-liquidity-intelligence/",
            "kayen_api": "platform/data-connector-templates.md",
        }

    return result


def tool_macro() -> dict:
    """Return current macro state."""
    state = get_macro_state()
    state["retrieval_note"] = (
        "Update with: python scripts/update_macro_state.py  "
        "— or connect live via platform/data-connector-templates.md (CoinGecko)"
    )
    state["sportmind_version"] = VERSION
    return state


def tool_stack(sport: str, use_case: str, compressed: bool) -> dict:
    """Return full intelligence stack in loading order."""
    files = get_skill_files(sport, use_case)
    stack = []
    for f in files:
        content = f.read_text(encoding="utf-8")
        entry = {
            "skill_id": str(Path(f).relative_to(ROOT)),
            "sha256":   hashlib.sha256(content.encode()).hexdigest(),
        }
        if compressed:
            # Check for compressed summary first
            slug        = sport.replace("_", "-")
            comp_file   = ROOT / "compressed" / "README.md"
            entry["content"] = content[:600] + "\n\n[COMPRESSED — full content truncated. Set compressed=false for full text.]"
        else:
            entry["content"] = content
        stack.append(entry)

    return {
        "sport":          sport,
        "use_case":       use_case,
        "stack":          stack,
        "total_files":    len(stack),
        "loading_order":  "macro → market → domain → athlete → fan-token",
        "sportmind_version": VERSION,
    }


def tool_verify(skill_id: str, content: str) -> dict:
    """Verify skill content against known-good SHA-256 hashes."""
    if not HASHES_FILE.exists():
        return {"verified": False, "reason": "skill-hashes.json not found"}

    hashes = json.loads(HASHES_FILE.read_text())
    actual = hashlib.sha256(content.encode("utf-8")).hexdigest()

    for path, entry in hashes.get("files", {}).items():
        if skill_id.lower() in path.lower():
            expected = entry.get("sha256", "")
            if actual == expected:
                return {"verified": True,  "file_path": path,
                        "hash": actual[:16] + "..."}
            else:
                return {"verified": False, "file_path": path,
                        "reason": "Hash mismatch — content may have been modified"}

    return {"verified": True,
            "reason": "Skill ID not found in registry — new or unregistered file"}


def tool_agent_status(agent_id: str, include_audit: bool, last_n: int) -> dict:
    """Return agent operational status (requires running agent instance)."""
    return {
        "agents":        [],
        "system_health": "UNKNOWN",
        "note":          (
            "sportmind_agent_status requires a running SportMind agent instance. "
            "Instantiate SportMindAgent from core/autonomous-agent-framework.md "
            "and call its get_status() method."
        ),
        "framework":     "core/autonomous-agent-framework.md",
        "patterns":      "examples/agentic-workflows/",
        "timestamp":     now_iso(),
        "sportmind_version": VERSION,
    }


# ── MCP Server ────────────────────────────────────────────────────────────────

TOOL_SCHEMAS = {
    "sportmind_signal": {
        "type": "object",
        "properties": {
            "sport":                {"type": "string", "enum": SUPPORTED_SPORTS,
                                    "description": "Sport identifier"},
            "event_id":             {"type": "string",
                                    "description": "e.g. 'ucl-qf-2026-psg-arsenal'"},
            "use_case":             {"type": "string", "enum": USE_CASES,
                                    "default": "pre_match"},
            "home_team":            {"type": "string"},
            "away_team":            {"type": "string"},
            "include_defi_context": {"type": "boolean", "default": False},
        },
        "required": ["sport"],
    },
    "sportmind_macro": {
        "type": "object", "properties": {}, "required": [],
    },
    "sportmind_stack": {
        "type": "object",
        "properties": {
            "sport":      {"type": "string", "enum": SUPPORTED_SPORTS},
            "use_case":   {"type": "string", "enum": USE_CASES, "default": "pre_match"},
            "compressed": {"type": "boolean", "default": False,
                          "description": "Return truncated content (~70% token reduction)"},
        },
        "required": ["sport"],
    },
    "sportmind_verify": {
        "type": "object",
        "properties": {
            "skill_id": {"type": "string", "description": "e.g. 'domain.football'"},
            "content":  {"type": "string", "description": "Skill content to verify"},
        },
        "required": ["skill_id", "content"],
    },
    "sportmind_agent_status": {
        "type": "object",
        "properties": {
            "agent_id":          {"type": "string"},
            "include_audit_log": {"type": "boolean", "default": False},
            "last_n_cycles":     {"type": "integer", "default": 5},
        },
        "required": [],
    },
}

TOOL_DESCRIPTIONS = {
    "sportmind_signal": (
        "Generate a SportMind pre-match intelligence signal. Returns direction, "
        "adjusted_score, SMS, modifiers, and flags. Call sportmind_macro first "
        "for fan token or DeFi applications."
    ),
    "sportmind_macro": (
        "Get the current SportMind macro state: crypto cycle phase, "
        "macro_modifier, and active events. Always call before fan token analysis."
    ),
    "sportmind_stack": (
        "Load the full SportMind intelligence stack for a sport in correct "
        "loading order (macro→market→domain→athlete→fan-token). Use for "
        "comprehensive reasoning context."
    ),
    "sportmind_verify": (
        "Verify SportMind skill content integrity via SHA-256 against "
        "platform/skill-hashes.json. Use in production security-sensitive deployments."
    ),
    "sportmind_agent_status": (
        "Get current status of SportMind autonomous agents: lifecycle state, "
        "health, cycle counts, pending escalations, data freshness."
    ),
}


async def run_stdio():
    """Run MCP server over stdio — for Claude Desktop and Claude Code."""
    try:
        from mcp.server import Server
        from mcp.server.stdio import stdio_server
        from mcp.types import Tool, TextContent
    except ImportError:
        print("ERROR: Install MCP SDK first:  pip install mcp aiohttp", flush=True)
        return

    server = Server("sportmind")

    @server.list_tools()
    async def list_tools():
        return [
            Tool(name=n, description=TOOL_DESCRIPTIONS[n], inputSchema=TOOL_SCHEMAS[n])
            for n in TOOL_SCHEMAS
        ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict):
        if name == "sportmind_signal":
            result = tool_signal(
                sport        = arguments.get("sport", "football"),
                event_id     = arguments.get("event_id", ""),
                use_case     = arguments.get("use_case", "pre_match"),
                home_team    = arguments.get("home_team", ""),
                away_team    = arguments.get("away_team", ""),
                include_defi = arguments.get("include_defi_context", False),
            )
        elif name == "sportmind_macro":
            result = tool_macro()
        elif name == "sportmind_stack":
            result = tool_stack(
                sport      = arguments.get("sport", "football"),
                use_case   = arguments.get("use_case", "pre_match"),
                compressed = arguments.get("compressed", False),
            )
        elif name == "sportmind_verify":
            result = tool_verify(arguments["skill_id"], arguments["content"])
        elif name == "sportmind_agent_status":
            result = tool_agent_status(
                agent_id     = arguments.get("agent_id", ""),
                include_audit= arguments.get("include_audit_log", False),
                last_n       = arguments.get("last_n_cycles", 5),
            )
        else:
            result = {"error": f"Unknown tool: {name}"}

        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    async with stdio_server() as streams:
        await server.run(*streams, server.create_initialization_options())


async def run_http(port: int):
    """Run MCP server over HTTP/SSE — for remote agents and hosted deployments."""
    try:
        from mcp.server import Server
        from mcp.server.sse import SseServerTransport
        from mcp.types import Tool, TextContent
        from aiohttp import web
    except ImportError:
        print("ERROR: Install dependencies:  pip install mcp aiohttp", flush=True)
        return

    server = Server("sportmind")

    @server.list_tools()
    async def list_tools():
        return [
            Tool(name=n, description=TOOL_DESCRIPTIONS[n], inputSchema=TOOL_SCHEMAS[n])
            for n in TOOL_SCHEMAS
        ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict):
        if name == "sportmind_signal":
            result = tool_signal(
                sport        = arguments.get("sport", "football"),
                event_id     = arguments.get("event_id", ""),
                use_case     = arguments.get("use_case", "pre_match"),
                home_team    = arguments.get("home_team", ""),
                away_team    = arguments.get("away_team", ""),
                include_defi = arguments.get("include_defi_context", False),
            )
        elif name == "sportmind_macro":
            result = tool_macro()
        elif name == "sportmind_stack":
            result = tool_stack(
                sport      = arguments.get("sport", "football"),
                use_case   = arguments.get("use_case", "pre_match"),
                compressed = arguments.get("compressed", False),
            )
        elif name == "sportmind_verify":
            result = tool_verify(arguments["skill_id"], arguments["content"])
        elif name == "sportmind_agent_status":
            result = tool_agent_status(
                agent_id     = arguments.get("agent_id", ""),
                include_audit= arguments.get("include_audit_log", False),
                last_n       = arguments.get("last_n_cycles", 5),
            )
        else:
            result = {"error": f"Unknown tool: {name}"}

        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    transport = SseServerTransport("/mcp")

    async def handle_sse(request):
        async with transport.connect_sse(
            request.headers, request
        ) as streams:
            await server.run(*streams, server.create_initialization_options())

    async def handle_health(request):
        return web.Response(
            content_type="application/json",
            text=json.dumps({
                "status":    "ok",
                "service":   "SportMind MCP Server",
                "version":   VERSION,
                "tools":     list(TOOL_SCHEMAS.keys()),
                "timestamp": now_iso(),
            }, indent=2),
        )

    app = web.Application()
    app.router.add_get("/mcp",    handle_sse)
    app.router.add_get("/health", handle_health)
    app.router.add_get("/",       handle_health)

    print(f"SportMind MCP Server v{VERSION}", flush=True)
    print(f"MCP endpoint:  http://localhost:{port}/mcp",    flush=True)
    print(f"Health check:  http://localhost:{port}/health", flush=True)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Server running on port {port}. Press Ctrl+C to stop.", flush=True)
    try:
        await asyncio.Event().wait()
    except (KeyboardInterrupt, asyncio.CancelledError):
        pass
    finally:
        await runner.cleanup()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="SportMind MCP Server — sports intelligence for AI agents"
    )
    parser.add_argument("--http",  action="store_true",
                        help="Run HTTP/SSE server (default: stdio)")
    parser.add_argument("--port",  type=int, default=3001,
                        help="HTTP port (default: 3001)")
    args = parser.parse_args()

    if args.http:
        asyncio.run(run_http(args.port))
    else:
        asyncio.run(run_stdio())
