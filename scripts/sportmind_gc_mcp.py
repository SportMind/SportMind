#!/usr/bin/env python3
"""
SportMind Governance & Competition MCP Server v3.71.0
Competition calendar, standings intelligence, and fan token governance.
Answers the season-arc question: where are teams in the competition,
what is the governance state, and what does the table trajectory mean?

Six tools:
  gc_governance_state  — GSI score, vote status, governance health
  gc_vote_alert        — governance vote timing and notification sequence
  gc_standings         — league table position, trajectory signal, threshold proximity
  gc_competition_state — current competition phase, knockout bracket, stakes
  gc_fixtures          — upcoming fixture list with competition context
  gc_calendar          — season arc position and commercial calendar

Usage:
  pip install mcp aiohttp
  python scripts/sportmind_gc_mcp.py              # stdio
  python scripts/sportmind_gc_mcp.py --http        # HTTP/SSE port 3005
"""

import json
import asyncio
import argparse
from datetime import datetime, timezone

VERSION = "3.86.4"

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def tool_governance_state(token: str, participation_rate: float,
                           last_votes: int, votes_participated: int):
    """Governance Signal Index and community governance health."""

    # GSI computation (simplified — full model in sports-governance-intelligence.md)
    participation_score = min(1.0, participation_rate)
    topic_quality_proxy = votes_participated / max(1, last_votes)

    gsi = round((participation_score * 0.50) + (topic_quality_proxy * 0.30) + (0.70 * 0.20), 3)

    if gsi >= 0.75:   gsi_label = "HEALTHY"
    elif gsi >= 0.50: gsi_label = "MODERATE"
    elif gsi >= 0.30: gsi_label = "AT RISK"
    else:             gsi_label = "CRITICAL"

    governor_warning = topic_quality_proxy < 0.50
    churn_risk = participation_rate < 0.30

    return {
        "token": token,
        "gsi_score": gsi,
        "gsi_label": gsi_label,
        "inputs": {
            "participation_rate":   participation_rate,
            "last_n_votes":         last_votes,
            "votes_participated":   votes_participated,
            "topic_quality_proxy":  round(topic_quality_proxy, 2),
        },
        "flags": {
            "governor_disengagement": governor_warning,
            "participation_churn_risk": churn_risk,
        },
        "recommendations": {
            "governor_warning": "Check recent vote topics — trivial votes destroy Governor archetype engagement" if governor_warning else "Vote quality appears adequate",
            "churn_warning":    "Re-engage Governors with 72h advance vote notice" if churn_risk else "Participation within normal range",
        },
        "governance_principles": {
            "min_notice_hours": 72,
            "quality_filter":   "Only publish votes that affect real club decisions",
            "result_notification": "Always explain outcome — not just announce it",
        },
        "load_skills": [
            "fan-token/sports-governance-intelligence/sports-governance-intelligence.md",
            "fan-token/fan-holder-profile-intelligence.md",
        ],
        "sportmind_version": VERSION,
        "assessed_at": now_iso(),
    }

def tool_vote_alert(token: str, vote_topic: str,
                    vote_close_utc: str, current_participation_pct: float):
    """Governance vote timing and notification sequence generator."""

    # Parse hours until close
    hours_until_close = 48  # default
    try:
        close = datetime.fromisoformat(vote_close_utc.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        hours_until_close = max(0, int((close - now).total_seconds() / 3600))
    except Exception:
        pass

    # Determine which notifications should fire now
    notifications = []
    if hours_until_close >= 72:
        notifications.append({
            "type":    "FIRST_NOTICE",
            "channel": "in-app + email (NOT push — not urgent yet)",
            "audience":"Governor segment + interested Loyalists",
            "message": f"Upcoming vote: {vote_topic}",
            "action":  "See what's being decided",
        })
    if hours_until_close <= 24:
        notifications.append({
            "type":    "REMINDER",
            "channel": "push + email",
            "audience":"Governors who have not voted",
            "message": f"Vote closes in {hours_until_close}h — {int(current_participation_pct*100)}% have voted",
            "action":  "Your vote is needed",
        })
    if hours_until_close <= 4:
        notifications.append({
            "type":    "FINAL_REMINDER",
            "channel": "push ONLY (time-critical)",
            "audience":"Governors who have not voted — high urgency",
            "message": f"Last chance — vote closes in {hours_until_close}h",
            "action":  "Vote before close",
        })

    # Quality check
    quality_flags = []
    if not vote_topic or len(vote_topic) < 10:
        quality_flags.append("TOPIC_TOO_VAGUE — risk of trivial vote destroying Governor engagement")

    return {
        "token":               token,
        "vote_topic":          vote_topic,
        "vote_close_utc":      vote_close_utc,
        "hours_until_close":   hours_until_close,
        "participation_pct":   int(current_participation_pct * 100),
        "notifications_due":   notifications,
        "quality_flags":       quality_flags,
        "notification_sequence":{
            "T-72h": "First notice — in-app + email — accessible topic description",
            "T-24h": "Reminder — push + email — current participation % shown",
            "T-4h":  "Final reminder — push only — last chance message",
            "T+2h":  "Result notification — all voters + non-voters — explain outcome",
        },
        "post_close_action":   "Always publish result with plain-language explanation",
        "load_skills": ["platform/fan-engagement-connector.md"],
        "sportmind_version": VERSION,
        "assessed_at": now_iso(),
    }

def tool_standings(club: str, league: str, current_position: int,
                   total_clubs: int, points: int, games_played: int,
                   points_to_title: int, points_to_top4: int, points_above_relegation: int):
    """League table position, trajectory signal, and threshold proximity."""

    # Position percentile
    position_pct = (total_clubs - current_position) / max(1, total_clubs - 1)

    # Threshold analysis
    thresholds = []
    if points_to_title <= 6:    thresholds.append({"zone": "TITLE_RACE",      "points_needed": points_to_title, "signal": "PEAK commercial window — title_decider season position"})
    if points_to_top4 <= 6:     thresholds.append({"zone": "TOP4_RACE",       "points_needed": points_to_top4,  "signal": "ELEVATED commercial — UCL qualification stakes"})
    if points_above_relegation <= 6: thresholds.append({"zone": "RELEGATION_BATTLE", "points_needed": 0, "points_buffer": points_above_relegation, "signal": "ELEVATED commercial — fear amplifies engagement"})

    if not thresholds:
        commercial_signal = "MID_TABLE — standard commercial window"
        season_pos_score = 0.95
    elif any(t["zone"] == "TITLE_RACE" for t in thresholds):
        commercial_signal = "TITLE_RACE — peak season position score"
        season_pos_score = 1.35
    elif any(t["zone"] == "RELEGATION_BATTLE" for t in thresholds):
        commercial_signal = "RELEGATION_BATTLE — fear drives engagement above mid-table"
        season_pos_score = 1.10
    else:
        commercial_signal = "QUALIFICATION_RACE — elevated engagement"
        season_pos_score = 1.10

    ppg = round(points / max(1, games_played), 2)

    return {
        "club":             club,
        "league":           league,
        "position":         current_position,
        "total_clubs":      total_clubs,
        "points":           points,
        "games_played":     games_played,
        "ppg":              ppg,
        "thresholds":       thresholds,
        "commercial_signal": commercial_signal,
        "season_position_cqs_score": season_pos_score,
        "standings_intelligence": {
            "title_race_note":     "Mathematically decisive match = CQS season_position 1.40",
            "relegation_note":     "Relegation fear generates HIGHER token engagement than comfortable mid-table",
            "dead_rubber_note":    "Nothing at stake = CQS season_position 0.70 — dampens all signals",
        },
        "load_skills": [
            "core/contextual-signal-environment.md",
            "core/core-result-impact-matrices.md",
        ],
        "sportmind_version": VERSION,
        "assessed_at": now_iso(),
    }

def tool_competition_state(competition: str, sport: str, current_round: str,
                            home_club: str, away_club: str,
                            home_aggregate: int, away_aggregate: int,
                            is_second_leg: bool):
    """Current competition phase, knockout context, and commercial stakes."""

    # Competition tier
    comp_tiers = {
        "ucl": {"name": "UEFA Champions League", "tier_weight": 0.75, "final_weight": 1.00, "global_audience": "Global Tier 2"},
        "world_cup": {"name": "FIFA World Cup", "tier_weight": 0.90, "final_weight": 1.00, "global_audience": "Global Tier 1"},
        "premier_league": {"name": "Premier League", "tier_weight": 0.70, "final_weight": None, "global_audience": "Major Regional"},
        "nba": {"name": "NBA", "tier_weight": 0.75, "final_weight": 0.92, "global_audience": "Major Regional"},
        "ipl": {"name": "IPL", "tier_weight": 0.82, "final_weight": 0.95, "global_audience": "Global Tier 2 (India primary)"},
    }
    comp_key = competition.lower().replace(" ", "_")
    comp_data = comp_tiers.get(comp_key, {
        "name": competition, "tier_weight": 0.60, "global_audience": "Domestic"
    })

    # Two-legged tie logic
    two_leg_context = None
    if is_second_leg:
        aggregate_diff = home_aggregate - away_aggregate
        if aggregate_diff > 0:
            two_leg_context = {
                "aggregate":       f"{home_club} {home_aggregate}–{away_aggregate} {away_club} on aggregate",
                "home_team_needs": "WIN or DRAW to advance",
                "away_team_needs": f"WIN by {aggregate_diff + 1}+ goals OR win by {aggregate_diff} and force extra time",
                "away_goals_note": "Away goals rule REMOVED from UEFA competitions since 2021 — aggregate only",
                "extra_time":      f"If {away_club} equalise on aggregate → extra time → penalties",
            }
        elif aggregate_diff < 0:
            two_leg_context = {
                "aggregate":       f"{home_club} {home_aggregate}–{away_aggregate} {away_club} on aggregate",
                "home_team_needs": f"WIN by {abs(aggregate_diff) + 1}+ goals OR win by {abs(aggregate_diff)} and force extra time",
                "away_team_needs": "WIN or DRAW to advance",
                "away_goals_note": "Away goals rule REMOVED from UEFA competitions since 2021",
            }
        else:
            two_leg_context = {
                "aggregate":  f"Level on aggregate ({home_aggregate}–{away_aggregate})",
                "result":     "Extra time will be played if still level after 90 min",
            }

    return {
        "competition":       competition,
        "sport":             sport,
        "current_round":     current_round,
        "home_club":         home_club,
        "away_club":         away_club,
        "competition_data":  comp_data,
        "two_leg_context":   two_leg_context,
        "calendar_collapse_risk": (
            "ACTIVE — if eliminated, FTP PATH_2 burn events for remaining rounds are cancelled. "
            "Load tournament-elimination-intelligence.md."
        ) if comp_key in ["ucl","world_cup","ufc","nba_playoffs"] else "Standard competition — load cup-competition-intelligence.md",
        "load_skills": [
            "core/cup-competition-intelligence.md",
            "fan-token/tournament-elimination-intelligence.md",
        ],
        "sportmind_version": VERSION,
        "assessed_at": now_iso(),
    }

def tool_fixtures(club: str, sport: str, competitions: list):
    """Upcoming fixture context and commercial calendar signal."""

    return {
        "club":         club,
        "sport":        sport,
        "competitions": competitions or ["All"],
        "fixture_intelligence": {
            "loading_instruction": "Live fixture data requires a data connector — load platform/api-connectors.md for sport-specific fixture APIs",
            "free_sources": {
                "football":   "football-data.org (free tier, 10 competitions), OpenFootball GitHub",
                "basketball": "balldontlie.io (NBA, free), basketball-reference.com",
                "cricket":    "cricapi.com (free tier), ESPNCricinfo",
                "mma":        "ESPN MMA schedule (public), UFC.com/events",
                "formula1":   "ergast.com/api/f1 (historical + current season), formula1.com",
            },
            "commercial_calendar_note": "Path-2 clubs: each upcoming match = potential WIN burn event. Cluster of fixtures in 7 days = concentrated supply reduction opportunity.",
        },
        "schedule_density_rule": {
            "3_matches_7_days":  "TIER 1 congestion — performance modifier ×0.88",
            "3_matches_8_12_days":"TIER 2 congestion — modifier ×0.93",
            "fan_token_density": "Multiple PATH_2 fixtures in short window = concentrated burn opportunity OR concentrated risk if losses",
        },
        "load_skills": [
            "core/core-fixture-congestion.md",
            "core/contextual-signal-environment.md",
            "platform/api-connector-examples.md",
        ],
        "sportmind_version": VERSION,
        "assessed_at": now_iso(),
    }

def tool_calendar(sport: str, competition: str, current_month: int):
    """Season arc position and commercial calendar window."""

    # Football seasonal calendar
    football_calendar = {
        8:  {"phase": "SEASON_OPENER",    "cqs_season": 1.15, "signal": "New season narrative, new signings, optimism arc"},
        9:  {"phase": "EARLY_SEASON",     "cqs_season": 0.92, "signal": "Form settling — stakes not yet clear"},
        10: {"phase": "FORM_BUILDING",    "cqs_season": 0.95, "signal": "Early standings taking shape"},
        11: {"phase": "AUTUMN_FORM",      "cqs_season": 1.00, "signal": "International break disruption ends"},
        12: {"phase": "DECEMBER_RUSH",    "cqs_season": 1.05, "signal": "Holiday fixture pile-up — schedule density HIGH"},
        1:  {"phase": "WINTER_TRANSFER",  "cqs_season": 1.10, "signal": "Transfer window open — star departure/arrival risk"},
        2:  {"phase": "UCL_KNOCKOUT_R16", "cqs_season": 1.15, "signal": "UCL Round of 16 — premium knockout window"},
        3:  {"phase": "TITLE_RACE_BUILD", "cqs_season": 1.20, "signal": "Title/relegation races crystallising — stakes rising"},
        4:  {"phase": "UCL_QF_SF",        "cqs_season": 1.35, "signal": "UCL Quarter/Semi-Finals — maximum commercial window"},
        5:  {"phase": "SEASON_DECIDER",   "cqs_season": 1.35, "signal": "Final weeks — title, relegation, European spots"},
        6:  {"phase": "POST_SEASON",      "cqs_season": 0.75, "signal": "Domestic season over — transfer speculation only"},
        7:  {"phase": "PRE_SEASON",       "cqs_season": 0.65, "signal": "Pre-season friendlies — low commercial signal"},
    }

    nba_calendar = {
        10: {"phase": "SEASON_OPENER", "cqs_season": 1.15, "signal": "Opening night premium"},
        11: {"phase": "EARLY_SEASON",  "cqs_season": 0.95, "signal": "82-game season starting"},
        12: {"phase": "MID_SEASON",    "cqs_season": 0.95, "signal": "Standard regular season"},
        1:  {"phase": "MID_SEASON",    "cqs_season": 0.95, "signal": "MLK Day games premium"},
        2:  {"phase": "ALL_STAR",      "cqs_season": 1.10, "signal": "All-Star weekend commercial peak"},
        3:  {"phase": "PLAYOFF_PUSH",  "cqs_season": 1.15, "signal": "Playoff seeding race"},
        4:  {"phase": "PLAYOFFS",      "cqs_season": 1.25, "signal": "First round"},
        5:  {"phase": "CONF_FINALS",   "cqs_season": 1.30, "signal": "Conference finals"},
        6:  {"phase": "NBA_FINALS",    "cqs_season": 1.40, "signal": "Maximum commercial window"},
        7:  {"phase": "OFFSEASON",     "cqs_season": 0.70, "signal": "Draft + free agency"},
    }

    calendars = {
        "football": football_calendar,
        "soccer":   football_calendar,
        "basketball": nba_calendar,
        "nba":      nba_calendar,
    }

    sport_key = sport.lower()
    cal = calendars.get(sport_key, {})
    month_data = cal.get(current_month, {
        "phase": "UNKNOWN",
        "cqs_season": 1.00,
        "signal": f"Load market/international-{sport_key}-cycle.md for sport-specific calendar"
    })

    return {
        "sport":       sport,
        "competition": competition or "general",
        "month":       current_month,
        "season_arc":  month_data,
        "world_cup_2026_note": (
            "FIFA World Cup 2026 is June/July 2026 (North America). "
            "National team tokens peak during tournament. "
            "Club tokens: player availability risk during tournament. "
            "Load fan-token/world-cup-2026-intelligence/ for full framework."
        ) if current_month in [6, 7] else None,
        "load_skills": [
            f"market/international-{sport_key.replace('soccer','football')}-cycle.md",
            "core/contextual-signal-environment.md",
        ],
        "sportmind_version": VERSION,
        "assessed_at": now_iso(),
    }

# ── MCP wiring ─────────────────────────────────────────────────────────────────

TOOL_DESCRIPTIONS = {
    "gc_governance_state": "Fan token governance health — GSI score, participation rate, Governor archetype risk, and vote quality assessment.",
    "gc_vote_alert":        "Governance vote timing — notification sequence (T-72h/T-24h/T-4h/T+2h) and quality filter check.",
    "gc_standings":         "League table intelligence — position, threshold proximity (title/top4/relegation), and commercial signal from table position.",
    "gc_competition_state": "Current competition phase, knockout bracket context, two-legged tie aggregate rules (away goals removed 2021), and CALENDAR_COLLAPSE risk.",
    "gc_fixtures":          "Upcoming fixture context, schedule density, and data connector guidance for live fixture feeds.",
    "gc_calendar":          "Season arc position — where a competition currently sits in the commercial calendar and what it means for engagement.",
}

TOOL_SCHEMAS = {
    "gc_governance_state": {
        "type": "object",
        "properties": {
            "token":                {"type":"string","description":"Token ticker or club name"},
            "participation_rate":   {"type":"number","description":"Governance participation rate (0.0–1.0)","default":0.30},
            "last_votes":           {"type":"integer","description":"Number of recent votes to assess","default":3},
            "votes_participated":   {"type":"integer","description":"Of last_votes, how many holder participated in","default":1},
        },
        "required": ["token"],
    },
    "gc_vote_alert": {
        "type": "object",
        "properties": {
            "token":                     {"type":"string","description":"Token ticker"},
            "vote_topic":                {"type":"string","description":"Vote topic description"},
            "vote_close_utc":            {"type":"string","description":"Vote closing time ISO-8601","default":""},
            "current_participation_pct": {"type":"number","description":"Current participation as decimal (0.35 = 35%)","default":0.0},
        },
        "required": ["token","vote_topic"],
    },
    "gc_standings": {
        "type": "object",
        "properties": {
            "club":                    {"type":"string","description":"Club name"},
            "league":                  {"type":"string","description":"League name"},
            "current_position":        {"type":"integer","description":"Current league position"},
            "total_clubs":             {"type":"integer","description":"Total clubs in league","default":20},
            "points":                  {"type":"integer","description":"Current points total"},
            "games_played":            {"type":"integer","description":"Games played","default":30},
            "points_to_title":         {"type":"integer","description":"Points behind leader","default":15},
            "points_to_top4":          {"type":"integer","description":"Points behind 4th place","default":8},
            "points_above_relegation": {"type":"integer","description":"Points above relegation zone","default":10},
        },
        "required": ["club","league","current_position","points"],
    },
    "gc_competition_state": {
        "type": "object",
        "properties": {
            "competition":     {"type":"string","description":"Competition name (UCL, World Cup, Premier League, etc.)"},
            "sport":           {"type":"string","description":"Sport"},
            "current_round":   {"type":"string","description":"Current round (Quarter-Final, Group Stage, etc.)"},
            "home_club":       {"type":"string","description":"Home club/team"},
            "away_club":       {"type":"string","description":"Away club/team"},
            "home_aggregate":  {"type":"integer","description":"Home side aggregate goals (for 2-legged ties)","default":0},
            "away_aggregate":  {"type":"integer","description":"Away side aggregate goals (for 2-legged ties)","default":0},
            "is_second_leg":   {"type":"boolean","description":"Is this a second leg of a two-legged tie?","default":False},
        },
        "required": ["competition","sport","current_round"],
    },
    "gc_fixtures": {
        "type": "object",
        "properties": {
            "club":         {"type":"string","description":"Club/team name"},
            "sport":        {"type":"string","description":"Sport"},
            "competitions": {"type":"array","items":{"type":"string"},"description":"Competitions to include","default":[]},
        },
        "required": ["club","sport"],
    },
    "gc_calendar": {
        "type": "object",
        "properties": {
            "sport":         {"type":"string","description":"Sport (football, basketball, cricket, etc.)"},
            "competition":   {"type":"string","description":"Competition name (optional)","default":""},
            "current_month": {"type":"integer","description":"Current month (1–12)","default":4},
        },
        "required": ["sport"],
    },
}

async def _handle(name: str, args: dict):
    if name == "gc_governance_state":
        return tool_governance_state(args.get("token",""), args.get("participation_rate",0.30),
            args.get("last_votes",3), args.get("votes_participated",1))
    elif name == "gc_vote_alert":
        return tool_vote_alert(args.get("token",""), args.get("vote_topic",""),
            args.get("vote_close_utc",""), args.get("current_participation_pct",0.0))
    elif name == "gc_standings":
        return tool_standings(args.get("club",""), args.get("league",""),
            args.get("current_position",10), args.get("total_clubs",20),
            args.get("points",40), args.get("games_played",30),
            args.get("points_to_title",15), args.get("points_to_top4",8),
            args.get("points_above_relegation",10))
    elif name == "gc_competition_state":
        return tool_competition_state(args.get("competition",""), args.get("sport",""),
            args.get("current_round",""), args.get("home_club",""), args.get("away_club",""),
            args.get("home_aggregate",0), args.get("away_aggregate",0), args.get("is_second_leg",False))
    elif name == "gc_fixtures":
        return tool_fixtures(args.get("club",""), args.get("sport",""), args.get("competitions",[]))
    elif name == "gc_calendar":
        return tool_calendar(args.get("sport",""), args.get("competition",""), args.get("current_month",4))
    return {"error": f"Unknown tool: {name}"}


async def run_stdio():
    try:
        from mcp.server import Server
        from mcp.server.stdio import stdio_server
        from mcp.types import Tool
    except ImportError:
        print("ERROR: pip install mcp", flush=True); return

    server = Server("sportmind-governance")

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

    server = Server("sportmind-governance")

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
            "service":"SportMind Governance & Competition MCP","version":VERSION,
            "tools":list(TOOL_SCHEMAS.keys()),"tool_count":len(TOOL_SCHEMAS),
        }, indent=2))

    app = web.Application()
    app.router.add_get("/mcp", handle_sse)
    app.router.add_get("/health", handle_health)
    app.router.add_get("/", handle_health)

    print(f"SportMind Governance & Competition MCP v{VERSION} — port {port}", flush=True)
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
    parser = argparse.ArgumentParser(description="SportMind Governance & Competition MCP")
    parser.add_argument("--http", action="store_true")
    parser.add_argument("--port", type=int, default=3005)
    args = parser.parse_args()
    asyncio.run(run_http(args.port) if args.http else run_stdio())
