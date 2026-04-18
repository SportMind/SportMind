#!/usr/bin/env python3
"""
SportMind Scouting & Transfer MCP Server v3.71.0
Player scouting, transfer valuation, and recruitment intelligence.
Exposes Pattern 10 (CVS scouting formula), DQI, system fit,
valuation gap detection, and transfer timeline intelligence.

Five tools:
  sc_cvs_brief      — Composite Value Score (CVS) scouting brief
  sc_dqi            — Decision Quality Index for a player's metrics
  sc_system_fit     — System fit score for player vs buying club system
  sc_valuation      — Market value vs DQI-adjusted value (undervaluation flag)
  sc_transfer_brief — Transfer timeline intelligence and negotiation context

Usage:
  pip install mcp aiohttp
  python scripts/sportmind_sc_mcp.py              # stdio
  python scripts/sportmind_sc_mcp.py --http        # HTTP/SSE port 3006
"""

import json
import asyncio
import argparse
from datetime import datetime, timezone

VERSION = "3.79.2"

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def tool_cvs_brief(player: str, position: str, age: int, sport: str,
                    dqi_score: float, system_fit_score: float,
                    market_value_m: float, contract_years_remaining: float):
    """Composite Value Score (CVS) — Pattern 10 scouting formula."""

    # CVS components (simplified — full formula in athlete-decision-intelligence.md)
    # Performance (DQI): 0.35
    # Commercial value: 0.25 (age-curve proxy)
    # System fit: 0.25
    # Risk: 0.15 (contract length proxy)

    # Commercial value proxy from age
    if age <= 23:     commercial = 0.90   # development upside
    elif age <= 26:   commercial = 1.00   # peak commercial value
    elif age <= 29:   commercial = 0.85   # declining curve
    elif age <= 31:   commercial = 0.70
    else:             commercial = 0.55   # end of prime

    # Risk proxy from contract years
    if contract_years_remaining <= 1:    risk = 0.90   # leverage, low cost
    elif contract_years_remaining <= 2:  risk = 0.80
    elif contract_years_remaining <= 3:  risk = 0.72
    else:                                risk = 0.65   # high contract cost

    perf_norm   = dqi_score / 100.0
    fit_norm    = system_fit_score / 100.0

    cvs_raw = (perf_norm * 0.35) + (commercial * 0.25) + (fit_norm * 0.25) + (risk * 0.15)
    cvs = round(cvs_raw * 100, 1)

    # UNDERVALUED flag
    dqi_adjusted_value_m = market_value_m * (dqi_score / 65.0)  # 65 = median DQI
    undervalued = dqi_score >= 75 and dqi_adjusted_value_m > market_value_m * 1.20
    valuation_gap_m = round(dqi_adjusted_value_m - market_value_m, 1) if undervalued else 0

    if cvs >= 80:      cvs_label = "STRONG ACQUISITION TARGET"
    elif cvs >= 70:    cvs_label = "VIABLE ACQUISITION"
    elif cvs >= 60:    cvs_label = "INVESTIGATE FURTHER"
    elif cvs >= 50:    cvs_label = "LOW PRIORITY"
    else:              cvs_label = "NOT RECOMMENDED"

    return {
        "player":          player,
        "position":        position,
        "age":             age,
        "sport":           sport,
        "cvs_score":       cvs,
        "cvs_label":       cvs_label,
        "components": {
            "performance_dqi":   round(perf_norm * 100, 1),
            "commercial_value":  round(commercial * 100, 1),
            "system_fit":        round(fit_norm * 100, 1),
            "risk_profile":      round(risk * 100, 1),
        },
        "undervalued_flag": undervalued,
        "valuation_gap_m":  valuation_gap_m,
        "market_value_m":   market_value_m,
        "dqi_adjusted_value_m": round(dqi_adjusted_value_m, 1),
        "contract_leverage": "HIGH" if contract_years_remaining <= 1 else "STANDARD",
        "recommended_bid_range": {
            "low_m":  round(market_value_m * 0.85, 1),
            "mid_m":  round(market_value_m * 1.00, 1),
            "high_m": round(market_value_m * 1.15, 1),
        } if not undervalued else {
            "low_m":  round(market_value_m * 1.00, 1),
            "mid_m":  round(market_value_m * 1.15, 1),
            "high_m": round(market_value_m * 1.30, 1),
            "note":   f"DQI-adjusted value is £{dqi_adjusted_value_m}M — budget to £{round(market_value_m * 1.30, 1)}M is still below true value",
        },
        "load_skills": [
            "core/athlete-decision-intelligence.md",
            "core/spatial-game-intelligence.md",
            "core/transfer-negotiation-intelligence.md",
        ],
        "pattern_reference":  "examples/agentic-workflows/scouting-agent.md (Pattern 10)",
        "sportmind_version":  VERSION,
        "assessed_at":        now_iso(),
    }

def tool_dqi(player: str, sport: str, position: str,
              xa_per_90: float, pressured_pass_completion: float,
              shot_quality_score: float, defensive_anticipation: float):
    """Decision Quality Index (DQI) for a player's performance metrics."""

    # DQI component weights by position type
    is_creator = position.lower() in ["midfielder","winger","playmaker","guard","point_guard","fly_half"]

    # xA → Dimension 1 (Chance Creation Quality) — 0.30 weight
    if xa_per_90 >= 0.25:   d1 = 95
    elif xa_per_90 >= 0.18: d1 = 82
    elif xa_per_90 >= 0.12: d1 = 70
    elif xa_per_90 >= 0.07: d1 = 58
    else:                   d1 = 42

    # Pressured pass completion → Dimension 2 — 0.25 weight
    if pressured_pass_completion >= 0.80:   d2 = 95
    elif pressured_pass_completion >= 0.72: d2 = 82
    elif pressured_pass_completion >= 0.65: d2 = 68
    elif pressured_pass_completion >= 0.58: d2 = 55
    else:                                   d2 = 40

    # Shot quality (xG per shot) — Dimension 3 — 0.25 weight (lower for non-strikers)
    if shot_quality_score >= 0.18:   d3 = 90
    elif shot_quality_score >= 0.13: d3 = 78
    elif shot_quality_score >= 0.09: d3 = 65
    else:                            d3 = 50
    w3 = 0.25 if not is_creator else 0.15  # reduced weight for creators

    # Defensive anticipation — Dimension 4 — 0.20 weight
    d4 = min(100, max(0, int(defensive_anticipation)))
    w4 = 0.30 - (w3 - 0.25) if w3 < 0.25 else 0.20  # redistribute weight

    dqi = round((d1 * 0.30) + (d2 * 0.25) + (d3 * w3) + (d4 * w4), 1)

    undervalued_flag = dqi >= 75
    moneyball_signal = dqi >= 75 and xa_per_90 >= 0.18

    return {
        "player":   player,
        "sport":    sport,
        "position": position,
        "dqi_score": dqi,
        "dqi_tier": (
            "ELITE (>90)" if dqi >= 90 else
            "STRONG (75-89)" if dqi >= 75 else
            "ABOVE AVERAGE (60-74)" if dqi >= 60 else
            "AVERAGE (45-59)" if dqi >= 45 else
            "BELOW AVERAGE (<45)"
        ),
        "dimensions": {
            "d1_chance_creation_xA":        {"score": d1, "input": f"xA/90: {xa_per_90}", "weight": 0.30},
            "d2_possession_decision":       {"score": d2, "input": f"pressured_pass_completion: {pressured_pass_completion:.0%}", "weight": 0.25},
            "d3_shot_selection":            {"score": d3, "input": f"shot_quality: {shot_quality_score}", "weight": round(w3, 2)},
            "d4_defensive_anticipation":    {"score": d4, "input": f"score: {defensive_anticipation}", "weight": round(w4, 2)},
        },
        "flags": {
            "decision_quality_undervalued": undervalued_flag,
            "moneyball_signal":             moneyball_signal,
        },
        "interpretation": (
            "DECISION_QUALITY_UNDERVALUED: This player's decision quality exceeds what their market value reflects. "
            "Classic Moneyball signal — market is pricing the output stats, not the decision quality behind them."
        ) if undervalued_flag else "DQI within expected range for market value tier",
        "load_skills":     ["core/athlete-decision-intelligence.md"],
        "sportmind_version": VERSION,
        "assessed_at":     now_iso(),
    }

def tool_system_fit(player: str, position: str,
                     buying_club_ppda: float, buying_club_system: str,
                     player_progressive_passes_per_90: float,
                     player_pressured_completion: float):
    """System fit score — how well a player suits the buying club's tactical system."""

    # PPDA-based system classification
    if buying_club_ppda <= 7:
        system_type = "HIGH_PRESS"
        fit_demand = "high_decision_speed"
    elif buying_club_ppda <= 12:
        system_type = "MODERATE_PRESS"
        fit_demand = "balanced_decision_speed"
    else:
        system_type = "LOW_BLOCK"
        fit_demand = "positional_discipline"

    # System fit scoring
    if system_type == "HIGH_PRESS":
        # High press rewards: pressured completion + progressive passing
        fit_score = (
            (min(1.0, player_pressured_completion / 0.78) * 60) +
            (min(1.0, player_progressive_passes_per_90 / 8.0) * 40)
        )
    elif system_type == "MODERATE_PRESS":
        fit_score = (
            (min(1.0, player_pressured_completion / 0.70) * 40) +
            (min(1.0, player_progressive_passes_per_90 / 6.0) * 60)
        )
    else:
        fit_score = (
            (min(1.0, player_progressive_passes_per_90 / 5.0) * 70) +
            (min(1.0, player_pressured_completion / 0.65) * 30)
        )

    fit_score = round(fit_score, 1)

    if fit_score >= 85:    fit_label = "EXCELLENT"
    elif fit_score >= 70:  fit_label = "GOOD"
    elif fit_score >= 55:  fit_label = "ADEQUATE"
    elif fit_score >= 40:  fit_label = "POOR"
    else:                  fit_label = "MISMATCH"

    # CVS multiplier from system fit
    if fit_score >= 85:   cvs_mult = 1.08
    elif fit_score >= 70: cvs_mult = 1.00
    elif fit_score >= 55: cvs_mult = 0.95
    else:                 cvs_mult = 0.88

    return {
        "player":               player,
        "position":             position,
        "buying_club_system":   buying_club_system or f"PPDA {buying_club_ppda} ({system_type})",
        "system_type":          system_type,
        "ppda":                 buying_club_ppda,
        "fit_score":            fit_score,
        "fit_label":            fit_label,
        "cvs_multiplier":       cvs_mult,
        "player_metrics": {
            "progressive_passes_per_90": player_progressive_passes_per_90,
            "pressured_pass_completion": f"{int(player_pressured_completion * 100)}%",
        },
        "fit_reasoning": (
            f"{position} with {player_progressive_passes_per_90:.1f} progressive passes/90 "
            f"and {int(player_pressured_completion*100)}% pressured completion "
            f"in a {system_type} system ({buying_club_ppda:.1f} PPDA)."
        ),
        "load_skills":         ["core/spatial-game-intelligence.md","core/tactical-matchup-intelligence.md"],
        "sportmind_version":   VERSION,
        "assessed_at":         now_iso(),
    }

def tool_valuation(player: str, sport: str, age: int, position: str,
                    market_value_m: float, dqi_score: float,
                    contract_years: float, comparable_tier_low_m: float,
                    comparable_tier_high_m: float):
    """Market value vs DQI-adjusted value — undervaluation detection."""

    # DQI-adjusted market rate
    dqi_adjustment = dqi_score / 65.0  # 65 = typical market median DQI
    dqi_adjusted_m  = round(market_value_m * dqi_adjustment, 1)

    # Age curve adjustment
    if age <= 23:      age_mult = 1.20  # development premium
    elif age <= 26:    age_mult = 1.10  # peak approaching
    elif age <= 29:    age_mult = 1.00  # peak / plateau
    elif age <= 31:    age_mult = 0.85
    else:              age_mult = 0.65

    fair_value_m = round(dqi_adjusted_m * age_mult, 1)

    # Contract leverage
    if contract_years <= 1:    leverage = "HIGH — expires soon, club must sell or lose for free"
    elif contract_years <= 2:  leverage = "MODERATE — within standard negotiation window"
    else:                      leverage = "LOW — selling club has full leverage"

    undervalued = dqi_score >= 75 and fair_value_m > market_value_m * 1.15
    overvalued  = market_value_m > fair_value_m * 1.25

    gap_m = round(fair_value_m - market_value_m, 1)
    gap_pct = round((fair_value_m - market_value_m) / max(1, market_value_m) * 100, 1)

    return {
        "player":               player,
        "sport":                sport,
        "age":                  age,
        "position":             position,
        "market_value_m":       market_value_m,
        "dqi_adjusted_value_m": dqi_adjusted_m,
        "fair_value_m":         fair_value_m,
        "valuation_gap_m":      gap_m,
        "valuation_gap_pct":    f"{gap_pct:+.1f}%",
        "comparable_tier":      {"low_m": comparable_tier_low_m, "high_m": comparable_tier_high_m},
        "flags": {
            "decision_quality_undervalued": undervalued,
            "potentially_overvalued":       overvalued,
        },
        "contract_leverage":    leverage,
        "contract_years":       contract_years,
        "agent_recommendation": (
            "ACQUIRE — DQI-adjusted value significantly exceeds market price. Gap will close." if undervalued else
            "CAUTION — market price exceeds DQI-adjusted fair value. Scrutinise." if overvalued else
            "FAIR VALUE — market price within DQI-adjusted range."
        ),
        "load_skills":          ["core/athlete-decision-intelligence.md","core/transfer-negotiation-intelligence.md"],
        "sportmind_version":    VERSION,
        "assessed_at":          now_iso(),
    }

def tool_transfer_brief(player: str, buying_club: str, selling_club: str,
                         transfer_window: str, urgency: str,
                         market_value_m: float, contract_years: float):
    """Transfer timeline, negotiation context, and RAF formula brief."""

    # RAF formula (Rational Acquisition Formula) context
    # Full formula in core/transfer-negotiation-intelligence.md
    urgency_modifier = {
        "critical":  1.25,  # must sign this window
        "high":      1.10,
        "moderate":  1.00,
        "low":       0.90,
    }.get(urgency.lower(), 1.00)

    # Contract leverage
    seller_leverage = "HIGH" if contract_years >= 3 else "MODERATE" if contract_years >= 2 else "LOW"
    buyer_leverage  = "LOW"  if contract_years >= 3 else "MODERATE" if contract_years >= 2 else "HIGH"

    # Window timing phases (from transfer-negotiation-intelligence.md)
    window_phases = {
        "summer": {
            "opens":       "June 15 (varies by league)",
            "peak":        "Late July – early August",
            "deadline":    "August 31 (Premier League/La Liga), September 3 (Bundesliga)",
            "late_penalty":"Price inflates 15-25% in final 72h — avoid if possible",
        },
        "winter": {
            "opens":       "January 1",
            "peak":        "January 15-28",
            "deadline":    "January 31",
            "late_penalty":"Price inflates 10-20% in final 48h",
        },
    }
    window_data = window_phases.get(transfer_window.lower(), {
        "note": f"Load transfer-negotiation-intelligence.md for {transfer_window} window details"
    })

    estimated_fee_m = round(market_value_m * urgency_modifier, 1)

    return {
        "player":           player,
        "buying_club":      buying_club,
        "selling_club":     selling_club,
        "transfer_window":  transfer_window,
        "urgency":          urgency,
        "market_value_m":   market_value_m,
        "estimated_fee_m":  estimated_fee_m,
        "urgency_modifier": urgency_modifier,
        "leverage": {
            "seller_leverage": seller_leverage,
            "buyer_leverage":  buyer_leverage,
            "contract_years":  contract_years,
        },
        "window_data":      window_data,
        "raf_formula_note": "Full RAF (Rational Acquisition Formula): initial_bid × leverage_modifier × urgency_modifier × market_cycle_modifier — see core/transfer-negotiation-intelligence.md",
        "negotiation_phases": [
            "Phase 1 — Interest signal (agent contact)",
            "Phase 2 — Informal valuation alignment",
            "Phase 3 — Formal bid submission",
            "Phase 4 — Counter-bid cycle",
            "Phase 5 — Personal terms",
            "Phase 6 — Medical + announcement",
        ],
        "fan_token_note": "Transfer of key ATM-tier player triggers AELS void in star-departure-intelligence.md — load for commercial impact on selling club token",
        "load_skills":     ["core/transfer-negotiation-intelligence.md","core/star-departure-intelligence.md"],
        "sportmind_version": VERSION,
        "assessed_at":     now_iso(),
    }

# ── MCP wiring ─────────────────────────────────────────────────────────────────

TOOL_DESCRIPTIONS = {
    "sc_cvs_brief":     "Composite Value Score (CVS) scouting brief — Pattern 10. Combines DQI, commercial value, system fit, and risk into a single acquisition score.",
    "sc_dqi":           "Decision Quality Index for a player using xA/90, pressured pass completion, shot quality, and defensive anticipation.",
    "sc_system_fit":    "System fit score — how well a player's metrics match the buying club's tactical system (PPDA-based).",
    "sc_valuation":     "Market value vs DQI-adjusted fair value. Detects DECISION_QUALITY_UNDERVALUED (the Moneyball signal).",
    "sc_transfer_brief":"Transfer timeline, window timing, RAF formula context, and negotiation phase guidance.",
}

TOOL_SCHEMAS = {
    "sc_cvs_brief": {
        "type": "object",
        "properties": {
            "player":                  {"type":"string","description":"Player name"},
            "position":                {"type":"string","description":"Position (winger, midfielder, striker, etc.)"},
            "age":                     {"type":"integer","description":"Player age"},
            "sport":                   {"type":"string","description":"Sport","default":"football"},
            "dqi_score":               {"type":"number","description":"DQI score (0-100) — use sc_dqi to compute"},
            "system_fit_score":        {"type":"number","description":"System fit score (0-100) — use sc_system_fit to compute"},
            "market_value_m":          {"type":"number","description":"Current market value in millions"},
            "contract_years_remaining":{"type":"number","description":"Contract years remaining","default":2.0},
        },
        "required": ["player","position","age","dqi_score","system_fit_score","market_value_m"],
    },
    "sc_dqi": {
        "type": "object",
        "properties": {
            "player":                     {"type":"string","description":"Player name"},
            "sport":                      {"type":"string","description":"Sport","default":"football"},
            "position":                   {"type":"string","description":"Position"},
            "xa_per_90":                  {"type":"number","description":"Expected assists per 90 minutes","default":0.10},
            "pressured_pass_completion":  {"type":"number","description":"Pass completion under pressure (0.0–1.0)","default":0.68},
            "shot_quality_score":         {"type":"number","description":"xG per shot (shot quality metric)","default":0.10},
            "defensive_anticipation":     {"type":"number","description":"Defensive anticipation score (0-100)","default":60.0},
        },
        "required": ["player","position"],
    },
    "sc_system_fit": {
        "type": "object",
        "properties": {
            "player":                          {"type":"string","description":"Player name"},
            "position":                        {"type":"string","description":"Position"},
            "buying_club_ppda":                {"type":"number","description":"Buying club PPDA (Passes Allowed per Defensive Action). <7=high press, 7-12=moderate, >12=low block"},
            "buying_club_system":              {"type":"string","description":"System description (optional)","default":""},
            "player_progressive_passes_per_90":{"type":"number","description":"Progressive passes per 90 minutes","default":6.0},
            "player_pressured_completion":     {"type":"number","description":"Pass completion under pressure (0.0–1.0)","default":0.68},
        },
        "required": ["player","position","buying_club_ppda"],
    },
    "sc_valuation": {
        "type": "object",
        "properties": {
            "player":                  {"type":"string","description":"Player name"},
            "sport":                   {"type":"string","description":"Sport","default":"football"},
            "age":                     {"type":"integer","description":"Player age"},
            "position":                {"type":"string","description":"Position"},
            "market_value_m":          {"type":"number","description":"Current market value (millions)"},
            "dqi_score":               {"type":"number","description":"DQI score (0-100)"},
            "contract_years":          {"type":"number","description":"Contract years remaining","default":2.0},
            "comparable_tier_low_m":   {"type":"number","description":"Low end of comparable tier market values","default":0},
            "comparable_tier_high_m":  {"type":"number","description":"High end of comparable tier market values","default":0},
        },
        "required": ["player","age","position","market_value_m","dqi_score"],
    },
    "sc_transfer_brief": {
        "type": "object",
        "properties": {
            "player":           {"type":"string","description":"Player name"},
            "buying_club":      {"type":"string","description":"Buying club"},
            "selling_club":     {"type":"string","description":"Selling club"},
            "transfer_window":  {"type":"string","description":"Transfer window (summer, winter)","enum":["summer","winter"],"default":"summer"},
            "urgency":          {"type":"string","description":"Acquisition urgency","enum":["critical","high","moderate","low"],"default":"moderate"},
            "market_value_m":   {"type":"number","description":"Market value (millions)"},
            "contract_years":   {"type":"number","description":"Seller's contract years remaining","default":2.0},
        },
        "required": ["player","buying_club","selling_club","market_value_m"],
    },
}

async def _handle(name: str, args: dict):
    if name == "sc_cvs_brief":
        return tool_cvs_brief(args.get("player",""), args.get("position",""), args.get("age",24),
            args.get("sport","football"), args.get("dqi_score",65.0), args.get("system_fit_score",65.0),
            args.get("market_value_m",20.0), args.get("contract_years_remaining",2.0))
    elif name == "sc_dqi":
        return tool_dqi(args.get("player",""), args.get("sport","football"), args.get("position",""),
            args.get("xa_per_90",0.10), args.get("pressured_pass_completion",0.68),
            args.get("shot_quality_score",0.10), args.get("defensive_anticipation",60.0))
    elif name == "sc_system_fit":
        return tool_system_fit(args.get("player",""), args.get("position",""),
            args.get("buying_club_ppda",9.0), args.get("buying_club_system",""),
            args.get("player_progressive_passes_per_90",6.0), args.get("player_pressured_completion",0.68))
    elif name == "sc_valuation":
        return tool_valuation(args.get("player",""), args.get("sport","football"), args.get("age",25),
            args.get("position",""), args.get("market_value_m",20.0), args.get("dqi_score",65.0),
            args.get("contract_years",2.0), args.get("comparable_tier_low_m",0), args.get("comparable_tier_high_m",0))
    elif name == "sc_transfer_brief":
        return tool_transfer_brief(args.get("player",""), args.get("buying_club",""), args.get("selling_club",""),
            args.get("transfer_window","summer"), args.get("urgency","moderate"),
            args.get("market_value_m",20.0), args.get("contract_years",2.0))
    return {"error": f"Unknown tool: {name}"}


async def run_stdio():
    try:
        from mcp.server import Server
        from mcp.server.stdio import stdio_server
        from mcp.types import Tool
    except ImportError:
        print("ERROR: pip install mcp", flush=True); return

    server = Server("sportmind-scouting")

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

    server = Server("sportmind-scouting")

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
            "service":"SportMind Scouting & Transfer MCP","version":VERSION,
            "tools":list(TOOL_SCHEMAS.keys()),"tool_count":len(TOOL_SCHEMAS),
        }, indent=2))

    app = web.Application()
    app.router.add_get("/mcp", handle_sse)
    app.router.add_get("/health", handle_health)
    app.router.add_get("/", handle_health)

    print(f"SportMind Scouting & Transfer MCP v{VERSION} — port {port}", flush=True)
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
    parser = argparse.ArgumentParser(description="SportMind Scouting & Transfer MCP")
    parser.add_argument("--http", action="store_true")
    parser.add_argument("--port", type=int, default=3006)
    args = parser.parse_args()
    asyncio.run(run_http(args.port) if args.http else run_stdio())
