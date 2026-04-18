#!/usr/bin/env python3
"""
SportMind Broadcast & Commercial MCP Server v3.71.0
Commercial intelligence for broadcasters, rights holders, sponsors, and
content teams. Distinct from the pre-match signal server — answers the
commercial question, not the performance question.

Five tools:
  bc_broadcast_value   — BVS (Broadcast Value Signal) for a match/event
  bc_rights_tier       — rights tier and valuation context for a competition
  bc_audience_reach    — audience reach tier and territory window analysis
  bc_context_quality   — CQS (Context Quality Score) combining all six dimensions
  bc_dts_effect        — Drive to Survive / content catalyst effect on token/engagement

Usage:
  pip install mcp aiohttp
  python scripts/sportmind_bc_mcp.py              # stdio
  python scripts/sportmind_bc_mcp.py --http        # HTTP/SSE port 3004
"""

import json
import asyncio
import argparse
from datetime import datetime, timezone

VERSION = "3.79.2"

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def tool_broadcast_value(sport: str, competition: str, event_label: str,
                          home_club: str, away_club: str):
    """Compute BVS (Broadcast Value Signal) for a match."""

    # Audience reach tier
    reach_tiers = {
        "ucl_final": ("Global Tier 1", 1.00, "300M+"),
        "world_cup_final": ("Global Tier 1", 1.00, "500M+"),
        "world_cup": ("Global Tier 1", 1.00, "300M+"),
        "ucl": ("Global Tier 2", 0.85, "100-300M"),
        "premier_league": ("Major Regional", 0.85, "20-100M"),
        "nba_finals": ("Major Regional", 0.85, "15-50M"),
        "super_bowl": ("Global Tier 1", 1.00, "100M+ US, 200M global"),
        "ipl": ("Global Tier 2", 0.90, "100-500M India-primary"),
        "bundesliga": ("Domestic Primary", 0.70, "5-20M"),
        "ligue_1": ("Domestic Secondary", 0.55, "2-8M"),
        "mls": ("Domestic Secondary", 0.50, "1-5M"),
    }
    comp_key = competition.lower().replace(" ", "_")
    reach_label, reach_score, reach_estimate = reach_tiers.get(comp_key, ("Domestic Primary", 0.65, "3-20M"))

    # Engagement depth
    engagement_map = {
        "ucl_final": 1.00, "world_cup_final": 1.00,
        "ucl": 0.90, "premier_league": 0.80,
        "nba_finals": 0.85, "super_bowl": 0.95,
        "ipl": 0.90, "bundesliga": 0.70,
    }
    engagement = engagement_map.get(comp_key, 0.65)

    # Rights scarcity
    scarcity_map = {
        "ucl": 0.85, "premier_league": 0.85, "nba": 0.80,
        "nfl": 0.85, "super_bowl": 1.00, "ipl": 0.90,
        "bundesliga": 0.75, "ligue_1": 0.55, "mls": 0.55,
    }
    scarcity = scarcity_map.get(comp_key, 0.60)

    # Commercial premium (audience demographics)
    premium_map = {
        "formula1": 0.95, "golf": 0.90, "nfl": 0.90,
        "ucl": 0.85, "premier_league": 0.85,
        "ipl": 0.80, "cricket": 0.75,
        "mls": 0.60, "ligue_1": 0.60,
    }
    sport_key = sport.lower()
    premium = premium_map.get(sport_key, 0.70)

    bvs = round(
        (reach_score * 0.30) + (engagement * 0.25) +
        (scarcity * 0.25) + (premium * 0.20), 3
    )

    return {
        "event": f"{home_club} vs {away_club}" if home_club else event_label,
        "sport": sport,
        "competition": competition,
        "bvs_score": bvs,
        "bvs_interpretation": (
            "PREMIUM EVENT" if bvs >= 0.85 else
            "HIGH VALUE" if bvs >= 0.70 else
            "STANDARD" if bvs >= 0.55 else
            "NICHE"
        ),
        "components": {
            "audience_reach":    {"score": reach_score, "tier": reach_label, "estimate": reach_estimate},
            "engagement_depth":  {"score": engagement},
            "rights_scarcity":   {"score": scarcity},
            "commercial_premium":{"score": premium},
        },
        "load_skills": ["market/broadcaster-media-intelligence.md"],
        "sportmind_version": VERSION,
        "assessed_at": now_iso(),
    }

def tool_rights_tier(competition: str, territory: str):
    """Rights tier and valuation benchmarks for a competition."""

    rights_data = {
        "premier_league": {
            "uk_annual_value":  "£3.3B/yr (3-year cycle)",
            "global_annual":    "£1.2B+ international",
            "tier":             "Global Tier 1",
            "exclusivity":      "Exclusive per territory",
            "key_broadcasters": ["Sky Sports (UK)", "NBC Sports (US)", "DAZN (multiple)", "Canal+ (France)"],
            "streaming_shift":  "Amazon Prime has midweek package — streaming gaining share",
        },
        "nfl": {
            "us_annual_value":  "~$9.5B/yr combined network",
            "tier":             "Domestic Tier 1 (global growing)",
            "exclusivity":      "Split across CBS, NBC, Fox, ESPN/ABC, Amazon TNF",
            "key_broadcasters": ["CBS","NBC","Fox","ESPN","Amazon Prime Video"],
            "streaming_shift":  "Thursday Night Football exclusively Amazon — milestone",
        },
        "ucl": {
            "annual_value":     "€3.5B+ total rights pool",
            "tier":             "Global Tier 1",
            "exclusivity":      "Exclusive per territory",
            "key_broadcasters": ["BT Sport/TNT (UK)", "CBS (US)", "DAZN (DE, ES, IT)", "Canal+ (FR)"],
            "streaming_shift":  "DAZN is primary broadcaster in multiple major markets",
        },
        "ipl": {
            "annual_value":     "$1.1B/yr (5-year deal 2023-2027)",
            "tier":             "Global Tier 2 / Domestic Tier 1 India",
            "exclusivity":      "JioCinema (streaming), Star Sports (linear) India",
            "key_broadcasters": ["JioCinema (free streaming India)", "Star Sports"],
            "streaming_shift":  "JioCinema free streaming — 550M+ potential viewers India",
        },
    }

    comp_key = competition.lower().replace(" ", "_")
    data = rights_data.get(comp_key, {
        "tier": "See market/broadcaster-media-intelligence.md for full rights valuations",
        "note": f"No specific data for '{competition}' — load broadcaster-media-intelligence.md",
    })

    return {
        "competition": competition,
        "territory": territory or "global",
        "rights_data": data,
        "territory_note": (
            f"Rights in {territory} will be territory-specific sub-licensing arrangement."
            if territory else
            "Specify territory for territory-specific rights details."
        ),
        "load_skills": ["market/broadcaster-media-intelligence.md"],
        "sportmind_version": VERSION,
        "assessed_at": now_iso(),
    }

def tool_audience_reach(sport: str, competition: str,
                         kickoff_time_utc: str, primary_market: str):
    """Audience reach tier and active territory window analysis."""

    # Audience reach tiers
    reach_tiers = {
        ("football","ucl_final"):     ("Global Tier 1", 1.40, "400M+"),
        ("football","world_cup"):      ("Global Tier 1", 1.40, "300-500M"),
        ("football","ucl"):            ("Global Tier 2", 1.25, "100-300M"),
        ("football","premier_league"): ("Major Regional", 1.10, "20-100M"),
        ("basketball","nba_finals"):   ("Major Regional", 1.10, "15-50M"),
        ("cricket","ipl"):             ("Global Tier 2", 1.25, "100-500M (India primary)"),
        ("mma","ufc_title"):           ("Major Regional", 1.10, "3-20M"),
        ("formula1","f1_race"):        ("Major Regional", 1.05, "70M global"),
    }
    comp_key = competition.lower().replace(" ", "_")
    reach_key = (sport.lower(), comp_key)
    reach_label, cqs_audience, estimate = reach_tiers.get(reach_key, ("Domestic Primary", 1.00, "3-20M"))

    # Territory window analysis
    territory_windows = {
        "uk":        "European evening (6pm–11pm CET) = score 1.20",
        "europe":    "European evening (6pm–11pm CET) = score 1.20",
        "us":        "Americas afternoon (12pm–6pm EST) = score 1.10",
        "india":     "India evening (7:30pm IST) = India Rule ×1.40 applies",
        "australia": "Asia-Pacific evening = score 1.10",
        "asia":      "Asia-Pacific evening = score 1.10",
    }
    market_key = primary_market.lower() if primary_market else "global"
    territory_note = territory_windows.get(market_key, "Global audience — check CQS territory dimension")

    # Check for EU/Americas overlap (highest engagement window)
    overlap_note = None
    if kickoff_time_utc:
        try:
            hour = int(kickoff_time_utc.split("T")[1][:2]) if "T" in kickoff_time_utc else int(kickoff_time_utc[:2])
            if 19 <= hour <= 22:
                overlap_note = "EU evening + Americas afternoon OVERLAP — add +0.10 to territory score"
        except Exception:
            pass

    return {
        "sport":            sport,
        "competition":      competition,
        "kickoff_utc":      kickoff_time_utc or "not specified",
        "primary_market":   primary_market or "global",
        "audience_tier":    reach_label,
        "audience_estimate":estimate,
        "cqs_audience_score": cqs_audience,
        "territory_window":   territory_note,
        "overlap_premium":    overlap_note,
        "india_rule":         "×1.40 applies when India is primary market (IPL, India cricket)",
        "load_skills": [
            "core/contextual-signal-environment.md",
            "market/broadcaster-media-intelligence.md",
        ],
        "sportmind_version": VERSION,
        "assessed_at": now_iso(),
    }

def tool_context_quality(sport: str, competition: str, kickoff_local_time: str,
                          venue_capacity: int, occupancy_pct: float,
                          season_position: str, is_neutral_venue: bool):
    """Compute CQS (Context Quality Score) across all six dimensions."""

    # 1. Schedule slot
    slot_scores = {
        "wednesday_8pm": 1.35, "tuesday_8pm": 1.35,
        "saturday_evening": 1.30, "sunday_evening": 1.25,
        "saturday_afternoon": 1.25, "sunday_afternoon": 1.10,
        "saturday_lunchtime": 1.25, "midweek_league": 1.00,
        "friday_evening": 0.95, "monday_evening": 0.90,
        "weekday_afternoon": 0.80, "pre_season": 0.65,
    }
    slot_key = kickoff_local_time.lower().replace(" ", "_") if kickoff_local_time else "midweek_league"
    slot_score = slot_scores.get(slot_key, 1.00)

    # 2. Venue weight
    if venue_capacity >= 60000:
        cap_tier = "Tier A (>60k)"
        if occupancy_pct >= 0.90:   venue_score = 1.35
        elif occupancy_pct >= 0.75: venue_score = 1.20
        elif occupancy_pct >= 0.50: venue_score = 1.00
        else:                       venue_score = 0.75
    elif venue_capacity >= 35000:
        cap_tier = "Tier B (35k-60k)"
        if occupancy_pct >= 0.90:   venue_score = 1.25
        elif occupancy_pct >= 0.75: venue_score = 1.15
        else:                       venue_score = 0.95
    else:
        cap_tier = "Tier C/D (<35k)"
        venue_score = 0.90 if occupancy_pct >= 0.90 else 0.80

    if is_neutral_venue: venue_score = min(1.40, venue_score + 0.10)

    # 3. Audience reach (simplified from competition)
    reach_scores = {
        "ucl": 1.25, "champions_league": 1.25, "world_cup": 1.40,
        "premier_league": 1.10, "la_liga": 1.10, "nba": 1.10,
        "bundesliga": 1.00, "ligue_1": 0.85, "mls": 0.85,
    }
    comp_key = competition.lower().replace(" ", "_")
    reach_score = reach_scores.get(comp_key, 1.00)

    # 4. Schedule density (simplified)
    density_score = 1.00  # default; varies by fixture calendar

    # 5. Season position
    position_scores = {
        "title_decider": 1.40, "must_win_elimination": 1.25,
        "top4_race": 1.10, "relegation_battle": 1.10,
        "standard_competitive": 1.00, "mid_table": 0.95,
        "dead_rubber": 0.70, "pre_season": 0.65,
    }
    pos_key = season_position.lower().replace(" ", "_") if season_position else "standard_competitive"
    position_score = position_scores.get(pos_key, 1.00)

    # 6. Territory window (simplified)
    territory_score = 1.10  # default; full model in CSE

    cqs = round(
        (slot_score * 0.25) + (venue_score * 0.20) + (reach_score * 0.25) +
        (density_score * 0.15) + (position_score * 0.10) + (territory_score * 0.05),
        3
    )

    return {
        "sport":        sport,
        "competition":  competition,
        "cqs_score":    cqs,
        "cqs_label": (
            "HIGH CONTEXT" if cqs >= 1.20 else
            "ELEVATED CONTEXT" if cqs >= 1.10 else
            "STANDARD" if cqs >= 0.90 else
            "REDUCED CONTEXT"
        ),
        "dimensions": {
            "schedule_slot":        {"score": slot_score, "input": kickoff_local_time or "not specified"},
            "venue_weight":         {"score": venue_score, "capacity": venue_capacity, "occupancy": f"{int(occupancy_pct*100)}%", "tier": cap_tier},
            "audience_reach":       {"score": reach_score},
            "schedule_density":     {"score": density_score, "note": "Default 1.00 — varies by calendar"},
            "season_position":      {"score": position_score, "input": season_position or "standard_competitive"},
            "territory_window":     {"score": territory_score, "note": "Default 1.10 — load CSE for full model"},
        },
        "cqs_application": "Apply to FTIS and CDI — NOT to on-pitch SMS",
        "load_skills": ["core/contextual-signal-environment.md"],
        "sportmind_version": VERSION,
        "assessed_at": now_iso(),
    }

def tool_dts_effect(sport: str, content_type: str, franchise: str):
    """Drive to Survive / content catalyst effect on commercial signals."""

    dts_data = {
        "formula1": {
            "content": "Drive to Survive (Netflix)",
            "audience_growth": "+40% US viewership growth attributed 2019-2023",
            "token_impact": "New fan cohort with lower sport knowledge but high engagement intent",
            "commercial_arc": "4-6 weeks post-series release = peak new fan acquisition window",
            "dts_modifier": 1.25,
            "note": "Series release = new F1 token commercial window; apply ×1.25 CDI for 30 days",
        },
        "tennis": {
            "content": "Break Point (Netflix)",
            "audience_growth": "Documented player follower growth 20-40% during series window",
            "token_impact": "Player-level commercial signal elevated during and after release",
            "commercial_arc": "Release week + 2 weeks = peak",
            "dts_modifier": 1.15,
        },
        "football": {
            "content": "Various club documentaries (Amazon, Netflix)",
            "audience_growth": "Club-specific; typically +15-25% digital engagement during release",
            "token_impact": "Club token CHI elevated; Loyalist + Amplifier archetypes most responsive",
            "commercial_arc": "Release week = peak; sustained 4-6 weeks",
            "dts_modifier": 1.15,
        },
        "mma": {
            "content": "UFC embedded / countdown series",
            "audience_growth": "Fight-week content drives 2-3× normal social volume",
            "token_impact": "UFC token engagement peaks fight week regardless of fighter narrative",
            "commercial_arc": "Fight week only; no sustained arc",
            "dts_modifier": 1.10,
        },
    }

    sport_key = sport.lower()
    data = dts_data.get(sport_key, {
        "note": f"No documented DTS-equivalent effect for {sport}",
        "dts_modifier": 1.00,
        "recommendation": "Load market/broadcaster-media-intelligence.md for sport-specific content signals",
    })

    if franchise:
        data["franchise_note"] = f"Franchise/club-specific content about {franchise} would apply modifier to {franchise} token specifically"

    return {
        "sport":        sport,
        "content_type": content_type or "documentary/series",
        "franchise":    franchise or None,
        "dts_effect":   data,
        "load_skills":  ["market/broadcaster-media-intelligence.md"],
        "sportmind_version": VERSION,
        "assessed_at":  now_iso(),
    }

# ── MCP wiring ─────────────────────────────────────────────────────────────────

TOOL_DESCRIPTIONS = {
    "bc_broadcast_value": "Compute BVS (Broadcast Value Signal) for a match or event — commercial value to broadcasters and rights holders.",
    "bc_rights_tier":     "Rights tier, annual valuation, and key broadcaster breakdown for a competition and territory.",
    "bc_audience_reach":  "Audience reach tier, territory window analysis, and India Rule flag for a match.",
    "bc_context_quality": "Compute CQS (Context Quality Score) across all six dimensions: slot, venue, reach, density, season position, territory.",
    "bc_dts_effect":      "Drive to Survive / content catalyst effect — how documentary/streaming content amplifies commercial signals.",
}

TOOL_SCHEMAS = {
    "bc_broadcast_value": {
        "type": "object",
        "properties": {
            "sport":       {"type":"string","description":"Sport"},
            "competition": {"type":"string","description":"Competition name"},
            "event_label": {"type":"string","description":"Event label if no home/away teams","default":""},
            "home_club":   {"type":"string","description":"Home team/club","default":""},
            "away_club":   {"type":"string","description":"Away team/club","default":""},
        },
        "required": ["sport","competition"],
    },
    "bc_rights_tier": {
        "type": "object",
        "properties": {
            "competition": {"type":"string","description":"Competition (Premier League, UCL, NFL, IPL, etc.)"},
            "territory":   {"type":"string","description":"Territory (UK, US, France, Germany, India, etc.)","default":""},
        },
        "required": ["competition"],
    },
    "bc_audience_reach": {
        "type": "object",
        "properties": {
            "sport":              {"type":"string","description":"Sport"},
            "competition":        {"type":"string","description":"Competition"},
            "kickoff_time_utc":   {"type":"string","description":"Kickoff time UTC (ISO-8601 or HH:MM)","default":""},
            "primary_market":     {"type":"string","description":"Primary audience market (UK, US, India, etc.)","default":"global"},
        },
        "required": ["sport","competition"],
    },
    "bc_context_quality": {
        "type": "object",
        "properties": {
            "sport":                {"type":"string","description":"Sport"},
            "competition":          {"type":"string","description":"Competition"},
            "kickoff_local_time":   {"type":"string","description":"Kickoff slot (saturday_evening, wednesday_8pm, etc.)","default":""},
            "venue_capacity":       {"type":"integer","description":"Stadium/venue capacity","default":40000},
            "occupancy_pct":        {"type":"number","description":"Occupancy as decimal (0.90 = 90%)","default":0.85},
            "season_position":      {"type":"string","description":"Season position context (title_decider, dead_rubber, standard_competitive, etc.)","default":"standard_competitive"},
            "is_neutral_venue":     {"type":"boolean","description":"Neutral venue (Cup final, etc.)","default":False},
        },
        "required": ["sport","competition"],
    },
    "bc_dts_effect": {
        "type": "object",
        "properties": {
            "sport":        {"type":"string","description":"Sport"},
            "content_type": {"type":"string","description":"Content type (documentary, embedded, countdown)","default":"documentary"},
            "franchise":    {"type":"string","description":"Specific club/team/franchise for targeted content","default":""},
        },
        "required": ["sport"],
    },
}

async def _handle(name: str, args: dict):
    if name == "bc_broadcast_value":
        return tool_broadcast_value(args.get("sport",""), args.get("competition",""),
            args.get("event_label",""), args.get("home_club",""), args.get("away_club",""))
    elif name == "bc_rights_tier":
        return tool_rights_tier(args.get("competition",""), args.get("territory",""))
    elif name == "bc_audience_reach":
        return tool_audience_reach(args.get("sport",""), args.get("competition",""),
            args.get("kickoff_time_utc",""), args.get("primary_market","global"))
    elif name == "bc_context_quality":
        return tool_context_quality(args.get("sport",""), args.get("competition",""),
            args.get("kickoff_local_time",""), args.get("venue_capacity",40000),
            args.get("occupancy_pct",0.85), args.get("season_position","standard_competitive"),
            args.get("is_neutral_venue",False))
    elif name == "bc_dts_effect":
        return tool_dts_effect(args.get("sport",""), args.get("content_type","documentary"),
            args.get("franchise",""))
    return {"error": f"Unknown tool: {name}"}


async def run_stdio():
    try:
        from mcp.server import Server
        from mcp.server.stdio import stdio_server
        from mcp.types import Tool
    except ImportError:
        print("ERROR: pip install mcp", flush=True); return

    server = Server("sportmind-broadcast")

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

    server = Server("sportmind-broadcast")

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
            "service":"SportMind Broadcast & Commercial MCP","version":VERSION,
            "tools":list(TOOL_SCHEMAS.keys()),"tool_count":len(TOOL_SCHEMAS),
        }, indent=2))

    app = web.Application()
    app.router.add_get("/mcp", handle_sse)
    app.router.add_get("/health", handle_health)
    app.router.add_get("/", handle_health)

    print(f"SportMind Broadcast & Commercial MCP v{VERSION} — port {port}", flush=True)
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
    parser = argparse.ArgumentParser(description="SportMind Broadcast & Commercial MCP")
    parser.add_argument("--http", action="store_true")
    parser.add_argument("--port", type=int, default=3004)
    args = parser.parse_args()
    asyncio.run(run_http(args.port) if args.http else run_stdio())
