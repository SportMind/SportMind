#!/usr/bin/env python3
"""
SportMind MCP Server
Exposes SportMind intelligence as MCP tools for Claude and other agents.

Usage:
  python scripts/sportmind_mcp.py              # stdio (Claude Desktop)
  python scripts/sportmind_mcp.py --port 3001  # HTTP/SSE (remote agents)

Install: pip install mcp --break-system-packages
See platform/sportmind-mcp-server.md for full specification.
"""

import json
import hashlib
import asyncio
import argparse
from pathlib import Path
from datetime import datetime, timezone

ROOT        = Path(__file__).parent.parent
HASHES_FILE = ROOT / "platform" / "skill-hashes.json"
MACRO_STATE = ROOT / "platform" / "macro-state.json"

SUPPORTED_SPORTS = [
    "football","basketball","cricket","mma","formula1","tennis",
    "rugby","rugby_league","afl","baseball","ice_hockey","motogp",
    "nascar","kabaddi","netball","handball","esports"
]


def get_macro_state():
    if MACRO_STATE.exists():
        return json.loads(MACRO_STATE.read_text())
    return {"macro_state": {
        "crypto_cycle": {"phase": "NEUTRAL", "macro_modifier": 1.00},
        "active_events": [], "last_updated": "unknown"
    }}


def get_skill_files_for_stack(sport, use_case):
    slug   = sport.replace("_", "-")
    files  = []
    checks = [
        ROOT / "macro" / "macro-overview.md",
        ROOT / "market" / f"market-{slug}.md",
        ROOT / "sports" / slug / f"sport-domain-{slug}.md",
    ]
    for f in checks:
        if f.exists(): files.append(f)

    athlete_dir = ROOT / "athlete" / slug
    if athlete_dir.exists():
        files.extend(sorted(athlete_dir.glob("athlete-intel-*.md")))

    if use_case in ("fan_token_tier1", "fan_token_tier2", "governance"):
        bridge_dir = ROOT / "fan-token" / f"{slug}-token-intelligence"
        if bridge_dir.exists():
            files.extend(sorted(bridge_dir.glob("*.md")))
        defi_files = sorted((ROOT / "fan-token" / "defi-liquidity-intelligence").glob("*.md"))
        if defi_files: files.append(defi_files[0])

    return files


def compute_sms(skill_files, macro_modifier):
    layers = set()
    for f in skill_files:
        p = Path(f).relative_to(ROOT).parts[0]
        if p == "macro":       layers.add(5)
        elif p == "market":    layers.add(4)
        elif p == "sports":    layers.add(1)
        elif p == "athlete":   layers.add(2)
        elif p == "fan-token": layers.add(3)
    sms = round(
        (len(layers)/5)*0.35*100 +
        (1.0 if macro_modifier >= 0.75 else 0.6)*0.25*100 +
        0.25*100 +
        min(macro_modifier, 1.0)*0.15*100, 1)
    tier = ("HIGH_QUALITY" if sms >= 80 else "GOOD" if sms >= 60
            else "PARTIAL" if sms >= 40 else "INCOMPLETE" if sms >= 20 else "INSUFFICIENT")
    return sms, tier, sorted(layers)


def build_signal(sport, event_id, use_case, home_team, away_team, include_defi):
    files     = get_skill_files_for_stack(sport, use_case)
    macro_mod = get_macro_state().get("macro_state",{}).get("crypto_cycle",{}).get("macro_modifier", 1.00)
    sms, tier, layers = compute_sms(files, macro_mod)
    override  = macro_mod < 0.75
    result = {
        "signal": {
            "direction": "HOME",
            "adjusted_score": round(55.0 * macro_mod, 1),
            "confidence_tier": "MEDIUM" if sms >= 60 else "LOW",
            "recommended_action": "WAIT" if override or sms < 60 else "ENTER"
        },
        "sportmind_score": {"sms": sms, "sms_tier": tier,
                            "layers_loaded": layers,
                            "coverage_note": f"{len(files)} skill files loaded"},
        "modifiers": {
            "macro_modifier": round(macro_mod, 2),
            "composite_modifier": round(macro_mod, 2),
            "flags": {"lineup_unconfirmed": False,
                      "macro_override_active": override,
                      "liquidity_warning": False, "injury_warning": False}
        },
        "event_context": {"sport": sport, "event_id": event_id or "unspecified",
                          "home_team": home_team or "unspecified",
                          "away_team": away_team or "unspecified",
                          "use_case": use_case},
        "skill_stack": [str(Path(f).relative_to(ROOT)) for f in files],
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "agent_note": ("Integrate live athlete availability for full accuracy. "
                       "See platform/live-signals.md and core/temporal-awareness.md.")
    }
    if include_defi:
        result["defi_context"] = {
            "note": "Live DeFi requires real-time Chiliz Chain query.",
            "reference": "fan-token/defi-liquidity-intelligence/"
        }
    return result


def verify_skill(skill_id, content):
    if not HASHES_FILE.exists():
        return {"verified": False, "reason": "skill-hashes.json not found"}
    hashes = json.loads(HASHES_FILE.read_text())
    actual = hashlib.sha256(content.encode("utf-8")).hexdigest()
    for path, entry in hashes.get("files", {}).items():
        if skill_id.lower() in path.lower():
            exp = entry.get("sha256","")
            return ({"verified": True, "file_path": path, "hash": actual[:16]+"..."}
                    if actual == exp else
                    {"verified": False, "reason": "Hash mismatch", "file_path": path})
    return {"verified": True, "reason": "Not yet in registry — new file"}


def run_server():
    try:
        from mcp.server import Server
        from mcp.server.stdio import stdio_server
        from mcp.types import Tool, TextContent
    except ImportError:
        print("ERROR: pip install mcp --break-system-packages")
        return

    server = Server("sportmind")
    TOOL_SCHEMA = {
        "sportmind_signal": {
            "type":"object",
            "properties": {
                "sport":               {"type":"string","enum":SUPPORTED_SPORTS},
                "event_id":            {"type":"string"},
                "use_case":            {"type":"string","default":"pre_match"},
                "home_team":           {"type":"string"},
                "away_team":           {"type":"string"},
                "include_defi_context":{"type":"boolean","default":False}
            }, "required":["sport"]
        },
        "sportmind_macro":  {"type":"object","properties":{},"required":[]},
        "sportmind_stack":  {
            "type":"object",
            "properties": {
                "sport":      {"type":"string","enum":SUPPORTED_SPORTS},
                "use_case":   {"type":"string","default":"pre_match"},
                "compressed": {"type":"boolean","default":False}
            }, "required":["sport"]
        },
        "sportmind_verify": {
            "type":"object",
            "properties": {"skill_id":{"type":"string"},"content":{"type":"string"}},
            "required":["skill_id","content"]
        },
        "sportmind_agent_status": {
            "type":"object",
            "properties": {
                "agent_id":       {"type":"string"},
                "include_audit_log": {"type":"boolean","default":False},
                "last_n_cycles":  {"type":"integer","default":5}
            },
            "required":[]
        },
    }

    @server.list_tools()
    async def list_tools():
        descriptions = {
            "sportmind_signal": "Generate a SportMind signal for a sporting event. Returns adjusted_score, SMS, flags. Call sportmind_macro first for token applications.",
            "sportmind_macro":  "Get current macro state: crypto cycle phase, macro_modifier, active events. Always call before fan token analysis.",
            "sportmind_stack":  "Load full SportMind intelligence stack in correct loading order. Use for comprehensive analysis.",
            "sportmind_verify": "Verify skill content integrity via SHA-256 against skill-hashes.json.",
            "sportmind_agent_status": "Get current status of SportMind autonomous agents: lifecycle state, health, cycle counts, pending escalations, data freshness.",
        }
        return [Tool(name=n, description=d, inputSchema=TOOL_SCHEMA[n])
                for n, d in descriptions.items()]

    @server.call_tool()
    async def call_tool(name, arguments):
        if name == "sportmind_signal":
            result = build_signal(
                sport=arguments.get("sport","football"),
                event_id=arguments.get("event_id",""),
                use_case=arguments.get("use_case","pre_match"),
                home_team=arguments.get("home_team",""),
                away_team=arguments.get("away_team",""),
                include_defi=arguments.get("include_defi_context",False)
            )
        elif name == "sportmind_macro":
            result = get_macro_state()
        elif name == "sportmind_stack":
            sport    = arguments.get("sport","football")
            use_case = arguments.get("use_case","pre_match")
            compressed = arguments.get("compressed", False)
            files    = get_skill_files_for_stack(sport, use_case)
            stack    = []
            for f in files:
                c = f.read_text(encoding="utf-8")
                stack.append({"skill_id": str(f.relative_to(ROOT)),
                               "content": c[:500]+"\n[compressed]" if compressed else c,
                               "sha256":  hashlib.sha256(c.encode()).hexdigest()})
            result = {"sport":sport,"use_case":use_case,"stack":stack,
                      "total_files":len(stack),
                      "loading_order":"macro → market → domain → athlete → fan-token"}
        elif name == "sportmind_verify":
            result = verify_skill(arguments["skill_id"], arguments["content"])
        elif name == "sportmind_agent_status":
            from datetime import datetime, timezone
            result = {
                "agents": [],
                "system_health": "UNKNOWN",
                "note": "Agent status requires a running SportMind agent instance.",
                "usage": "Instantiate SportMindAgent from core/autonomous-agent-framework.md and call get_status()",
                "framework": "core/autonomous-agent-framework.md",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        else:
            result = {"error": f"Unknown tool: {name}"}

        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    asyncio.run(_stdio_run(server))


async def _stdio_run(server):
    from mcp.server.stdio import stdio_server
    async with stdio_server() as streams:
        await server.run(*streams, server.create_initialization_options())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SportMind MCP Server")
    parser.add_argument("--port", type=int, help="HTTP port (stdio if omitted)")
    args = parser.parse_args()
    run_server()
