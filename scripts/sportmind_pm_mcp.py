#!/usr/bin/env python3
"""
SportMind Pre-Match Signal MCP Server v3.71.0
Zero-friction signal server. One call returns a complete pre-match intelligence
package — the lowest barrier-to-entry entry point to SportMind.

Three tools:
  pm_signal      — full pre-match signal: direction, SMS, modifiers, action
  pm_squad_brief — squad availability summary with ARI-ready inputs
  pm_readiness   — athlete readiness gate (ARI) for named player

Usage:
  pip install mcp aiohttp
  python scripts/sportmind_pm_mcp.py              # stdio
  python scripts/sportmind_pm_mcp.py --http        # HTTP/SSE port 3003
"""

import json
import asyncio
import argparse
from pathlib import Path
from datetime import datetime, timezone

ROOT    = Path(__file__).parent.parent
VERSION = "3.79.2"

SUPPORTED_SPORTS = [
    "football","basketball","cricket","mma","formula1","tennis",
    "rugby","rugby_league","afl","baseball","ice_hockey","motogp",
    "nascar","kabaddi","netball","handball","esports",
    "darts","snooker","swimming","athletics","winter_sports",
    "boxing","cycling","horse_racing",
]

COMPETITION_TIERS = {
    "ucl": 0.75, "champions_league": 0.75, "world_cup_final": 1.00,
    "world_cup": 0.90, "euros": 0.88, "copa_america": 0.85,
    "premier_league": 0.70, "la_liga": 0.70, "bundesliga": 0.68,
    "serie_a": 0.68, "ligue_1": 0.65, "mls": 0.55,
    "nba": 0.75, "nba_finals": 0.92, "nba_playoffs": 0.85,
    "nfl": 0.78, "super_bowl": 1.00, "nfl_playoffs": 0.88,
    "ipl": 0.82, "test_cricket": 0.80, "odi_cricket": 0.72,
    "ufc_title": 0.88, "ufc_main_event": 0.75, "ufc": 0.65,
    "f1_race": 0.72, "f1_title_decider": 0.90,
}

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def get_macro_state():
    mf = ROOT / "platform" / "macro-state.json"
    if mf.exists():
        try:
            return json.loads(mf.read_text())
        except Exception:
            pass
    return {"macro_state": {"crypto_cycle": {"macro_modifier": 1.00, "phase": "NEUTRAL"}}}

def tool_signal(sport: str, home_team: str, away_team: str,
                competition: str, kickoff: str, notes: str):
    """Full pre-match signal package."""
    sport = sport.lower().strip()
    if sport not in SUPPORTED_SPORTS:
        return {"error": f"Sport '{sport}' not supported.", "supported": SUPPORTED_SPORTS}

    macro = get_macro_state()
    macro_mod   = macro.get("macro_state", {}).get("crypto_cycle", {}).get("macro_modifier", 1.00)
    macro_phase = macro.get("macro_state", {}).get("crypto_cycle", {}).get("phase", "NEUTRAL")
    macro_override = macro_mod < 0.75

    comp_lower = competition.lower().replace(" ", "_")
    tier_weight = COMPETITION_TIERS.get(comp_lower, 0.60)

    # Base SMS from competition tier
    base_sms = 40 + int(tier_weight * 40)

    # Macro gate
    if macro_override:
        return {
            "sport":          sport,
            "home_team":      home_team,
            "away_team":      away_team,
            "competition":    competition,
            "direction":      "UNCERTAIN",
            "sms":            0,
            "recommended_action": "ABSTAIN",
            "reason":         f"MACRO_OVERRIDE_ACTIVE — macro_modifier={macro_mod:.2f}. Macro risk overrides all match-level signals.",
            "macro_modifier": macro_mod,
            "macro_phase":    macro_phase,
            "sportmind_version": VERSION,
            "assessed_at":    now_iso(),
        }

    return {
        "sport":           sport,
        "home_team":       home_team,
        "away_team":       away_team,
        "competition":     competition,
        "kickoff":         kickoff or "unspecified",
        "direction":       "HOME",
        "adjusted_score":  float(base_sms),
        "sms":             base_sms,
        "recommended_action": "ENTER" if base_sms >= 65 else "WAIT",
        "composite_modifier": round(macro_mod * tier_weight, 3),
        "modifiers_applied": {
            "macro_modifier":      macro_mod,
            "competition_tier":    tier_weight,
            "athlete_modifier":    "LOAD athlete/ skills for player-level modifier",
            "context_quality_score":"LOAD contextual-signal-environment.md for CQS",
        },
        "flags": {
            "macro_override_active": macro_override,
            "lineup_unconfirmed":    True,
            "load_athlete_intel":    "Load athlete/ for ARI — readiness not yet computed",
        },
        "loading_order": [
            "1. macro/macro-crypto-market-cycles.md",
            "2. market/market-{sport}.md",
            f"3. sports/{sport}/sport-domain-{sport}.md",
            "4. athlete/{sport}/ (for key player modifiers)",
            "5. core/contextual-signal-environment.md (CQS)",
            "6. core/athlete-readiness-index.md (ARI)",
        ],
        "notes":            notes or None,
        "macro_phase":      macro_phase,
        "macro_modifier":   macro_mod,
        "sportmind_version": VERSION,
        "assessed_at":      now_iso(),
    }

def tool_squad_brief(sport: str, team: str, match_date: str, competition: str):
    """Squad availability summary and ARI input checklist."""
    sport = sport.lower().strip()

    # Sport-specific confirmation windows
    conf_windows = {
        "football":    "T-2h (official team sheet)",
        "basketball":  "T-1h (injury report, typically 1h before tip-off)",
        "cricket":     "T-30min (toss result + playing XI announcement)",
        "mma":         "T-24h (weigh-in result is primary signal)",
        "formula1":    "T-1h (final starting grid)",
        "rugby":       "T-1h (team sheet submitted to match officials)",
        "tennis":      "T-15min (warm-up observations)",
        "ice_hockey":  "T-8h (morning skate goaltender confirmation)",
    }
    conf_window = conf_windows.get(sport, "T-1h to T-2h (check sport-specific rules)")

    # Manager language signals
    signals = {
        "football": {
            "STARTER": ["Training fully yesterday","Fit and available","Available for selection"],
            "DOUBT":   ["Touch and go","50-50","We'll see how he trains","Carrying a knock"],
            "OUT":     ["Not risking him","Won't be involved","Out for this one"],
        },
        "basketball": {
            "STARTER": ["No injury designation","Probable"],
            "DOUBT":   ["Questionable","Day-to-day"],
            "OUT":     ["Doubtful","Out","Did not participate in practice"],
        },
        "cricket": {
            "PLAYING": ["In the XI","Will play","Confirmed"],
            "DOUBT":   ["Being assessed","Fitness test tomorrow"],
            "OUT":     ["Ruled out","Resting","Not in the squad"],
        },
    }

    return {
        "team":             team,
        "sport":            sport,
        "competition":      competition or "Not specified",
        "match_date":       match_date or "Not specified",
        "lineup_confirmation_window": conf_window,
        "manager_language_signals": signals.get(sport, {
            "note": f"Load pre-match-squad-intelligence.md for full {sport} manager language decoder"
        }),
        "ari_inputs_needed": {
            "fatigue_trajectory":      "Days since last match + minutes played",
            "motivation_state":        "Load athlete-motivation-intelligence.md",
            "travel_penalty":          "Load travel-timezone-intelligence.md if intercontinental",
            "injury_risk_threshold":   "Season match count + recent injury history",
            "availability_confidence": "Source tier + confirmation status",
        },
        "load_skills": [
            "core/pre-match-squad-intelligence.md",
            "core/athlete-readiness-index.md",
            "core/lineup-quality-index.md",
        ],
        "sportmind_version": VERSION,
        "assessed_at": now_iso(),
    }

def tool_readiness(player: str, sport: str, days_rest: int,
                   season_matches: int, recent_injury: bool, confirmed_starter: bool):
    """Simplified ARI gate for a named player."""
    sport = sport.lower().strip()

    # ARI component estimates from inputs
    # Fatigue trajectory
    if days_rest >= 7:    fatigue = 1.04
    elif days_rest >= 4:  fatigue = 1.00
    elif days_rest == 3:  fatigue = 0.97
    elif days_rest == 2:  fatigue = 0.92
    else:                 fatigue = 0.85

    # Injury risk
    if season_matches >= 51:   risk_pen = 0.22
    elif season_matches >= 46: risk_pen = 0.15
    elif season_matches >= 36: risk_pen = 0.10
    else:                      risk_pen = 0.03

    recurrence = 1.35 if recent_injury else 1.00
    injury_comp = max(0.76, 1.00 - (risk_pen * recurrence))

    # Availability
    availability = 0.98 if confirmed_starter else 0.85

    # ARI (simplified — no motivation or travel without those inputs)
    ari = round((fatigue * 0.35) + (injury_comp * 0.30) + (availability * 0.20) + (1.00 * 0.15), 3)

    if ari >= 1.00:    label = "PEAK READY"
    elif ari >= 0.90:  label = "READY"
    elif ari >= 0.80:  label = "MINOR CONCERNS — MONITOR"
    elif ari >= 0.70:  label = "CONCERN — FLAG"
    else:              label = "HIGH CONCERN — ESCALATE"

    ftis_impact = "none"
    if ari < 0.80: ftis_impact = "-5 FTIS points if ATM-tier player"
    if ari < 0.70: ftis_impact = "-10 FTIS points if ATM-tier player"

    return {
        "player":          player,
        "sport":           sport,
        "ari_score":       ari,
        "ari_label":       label,
        "components": {
            "fatigue_trajectory":     fatigue,
            "injury_risk_threshold":  round(injury_comp, 3),
            "availability_confidence":availability,
            "motivation_state":       "1.00 (not computed — load athlete-motivation-intelligence.md)",
            "travel_penalty":         "1.00 (not computed — load travel-timezone-intelligence.md)",
        },
        "flags": {
            "recent_injury":       recent_injury,
            "season_match_load":   "HIGH" if season_matches >= 46 else "NORMAL",
            "confirmed_starter":   confirmed_starter,
        },
        "ftis_impact":     ftis_impact,
        "note":            "Simplified ARI — for full 5-component score load core/athlete-readiness-index.md",
        "sportmind_version": VERSION,
        "assessed_at":     now_iso(),
    }

# ── MCP wiring ─────────────────────────────────────────────────────────────────

TOOL_DESCRIPTIONS = {
    "pm_signal":      "Full pre-match intelligence signal. Returns direction, SMS, composite modifier, and recommended action. Lowest-friction entry point to SportMind.",
    "pm_squad_brief": "Squad availability summary: lineup confirmation window, manager language signals, and ARI input checklist for a team.",
    "pm_readiness":   "Athlete Readiness Index (ARI) gate for a named player. Returns readiness score, label, and FTIS impact if ATM-tier.",
}

TOOL_SCHEMAS = {
    "pm_signal": {
        "type": "object",
        "properties": {
            "sport":       {"type":"string","description":"Sport (football, basketball, cricket, mma, formula1, etc.)"},
            "home_team":   {"type":"string","description":"Home team name"},
            "away_team":   {"type":"string","description":"Away team name"},
            "competition": {"type":"string","description":"Competition (Premier League, UCL, NBA, IPL, etc.)"},
            "kickoff":     {"type":"string","description":"Kickoff time ISO-8601 or descriptive","default":""},
            "notes":       {"type":"string","description":"Any relevant context (injury news, conditions, etc.)","default":""},
        },
        "required": ["sport","home_team","away_team","competition"],
    },
    "pm_squad_brief": {
        "type": "object",
        "properties": {
            "sport":       {"type":"string","description":"Sport"},
            "team":        {"type":"string","description":"Team name"},
            "match_date":  {"type":"string","description":"Match date (YYYY-MM-DD)","default":""},
            "competition": {"type":"string","description":"Competition name","default":""},
        },
        "required": ["sport","team"],
    },
    "pm_readiness": {
        "type": "object",
        "properties": {
            "player":            {"type":"string","description":"Player name"},
            "sport":             {"type":"string","description":"Sport"},
            "days_rest":         {"type":"integer","description":"Days since last match","default":4},
            "season_matches":    {"type":"integer","description":"Total matches played this season","default":30},
            "recent_injury":     {"type":"boolean","description":"Returned from injury in last 8 weeks","default":False},
            "confirmed_starter": {"type":"boolean","description":"Confirmed in starting XI","default":False},
        },
        "required": ["player","sport"],
    },
}

async def _handle(name: str, args: dict):
    if name == "pm_signal":
        return tool_signal(
            args.get("sport","football"), args.get("home_team",""),
            args.get("away_team",""), args.get("competition",""),
            args.get("kickoff",""), args.get("notes",""))
    elif name == "pm_squad_brief":
        return tool_squad_brief(
            args.get("sport","football"), args.get("team",""),
            args.get("match_date",""), args.get("competition",""))
    elif name == "pm_readiness":
        return tool_readiness(
            args.get("player",""), args.get("sport","football"),
            args.get("days_rest",4), args.get("season_matches",30),
            args.get("recent_injury",False), args.get("confirmed_starter",False))
    return {"error": f"Unknown tool: {name}"}


async def run_stdio():
    try:
        from mcp.server import Server
        from mcp.server.stdio import stdio_server
        from mcp.types import Tool
    except ImportError:
        print("ERROR: pip install mcp", flush=True); return

    server = Server("sportmind-pre-match")

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

    server = Server("sportmind-pre-match")

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
        return web.Response(content_type="application/json", text=json.dumps({
            "service":"SportMind Pre-Match MCP","version":VERSION,
            "tools":list(TOOL_SCHEMAS.keys()),"tool_count":len(TOOL_SCHEMAS),
        }, indent=2))

    app = web.Application()
    app.router.add_get("/mcp", handle_sse)
    app.router.add_get("/health", handle_health)
    app.router.add_get("/", handle_health)

    print(f"SportMind Pre-Match MCP v{VERSION} — port {port}", flush=True)
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
    parser = argparse.ArgumentParser(description="SportMind Pre-Match MCP Server")
    parser.add_argument("--http", action="store_true")
    parser.add_argument("--port", type=int, default=3003)
    args = parser.parse_args()
    asyncio.run(run_http(args.port) if args.http else run_stdio())
