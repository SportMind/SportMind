#!/usr/bin/env python3
"""
SportMind Fan Token MCP Server v3.71.0
Dedicated fan token intelligence server for Chiliz Chain / Socios ecosystem.

Eight tools:
  ft_token_state        — FTP path status, lifecycle phase, supply mechanics
  ft_burn_forecast      — upcoming WIN burn events and supply reduction schedule
  ft_community_health   — CHI score, holder archetype distribution, churn risk
  ft_fraud_scan         — MRS score, attack type detection, signal integrity
  ft_holder_brief       — archetype-specific engagement recommendation
  ft_tournament_exit    — CALENDAR_COLLAPSE impact on token supply if team eliminated
  ft_macro_context      — Chiliz chain macro state, CHZ cycle, regulatory context
  ft_registry           — full fan token registry lookup with contract addresses

Usage:
  pip install mcp aiohttp
  python scripts/sportmind_ft_mcp.py              # stdio (Claude Desktop)
  python scripts/sportmind_ft_mcp.py --http        # HTTP/SSE on port 3002
  python scripts/sportmind_ft_mcp.py --http --port 3002

See platform/sportmind-ft-mcp.md for full specification.
"""

import json
import asyncio
import argparse
from pathlib import Path
from datetime import datetime, timezone

ROOT    = Path(__file__).parent.parent
VERSION = "3.86.2"

# ── Fan token registry (Chiliz Chain 88888) ───────────────────────────────────
FAN_TOKEN_REGISTRY = {
    "AFC":  {"name":"Arsenal FC",           "sport":"football","tier":1,
             "contract":"0x1d4343d35f0E0e14C14115876D01dEAa4792550b",
             "ftp_path":"PATH_2","ftp_confirmed":"2026-04-07",
             "ftp_note":"First public PATH_2 trial. Pre-liquidation 1/400th supply T-48h."},
    "BAR":  {"name":"FC Barcelona",         "sport":"football","tier":1,
             "contract":"0xFD3C73b3B09D418841dd6Aff341b2d6e3abA433b","ftp_path":"PATH_1"},
    "PSG":  {"name":"Paris Saint-Germain",  "sport":"football","tier":1,
             "contract":"0xc2661815C69c2B3924D3dd0c2C1358A1E38A3105","ftp_path":"PATH_1"},
    "JUV":  {"name":"Juventus",             "sport":"football","tier":1,
             "contract":"0x454038003a93cf44766aF352F74bad6B745616D0","ftp_path":None},
    "CITY": {"name":"Manchester City FC",   "sport":"football","tier":1,
             "contract":"0x6401b29F40a02578Ae44241560625232A01B3F79","ftp_path":None},
    "INTER":{"name":"Inter Milan",          "sport":"football","tier":1,
             "contract":"0xc727c9C0f2647CB90B0FCA64d8ddB14878716BeD","ftp_path":None},
    "ACM":  {"name":"AC Milan",             "sport":"football","tier":1,
             "contract":"0xF9C0F80a6c67b1B39bdDF00ecD57f2533ef5b688","ftp_path":None},
    "ATM":  {"name":"Atlético de Madrid",   "sport":"football","tier":1,
             "contract":"0xe9506F70be469d2369803Ccf41823713BAFe8154","ftp_path":None},
    "GAL":  {"name":"Galatasaray",          "sport":"football","tier":1,
             "contract":"0x6DaB8Fe8e5d425F2Eb063aAe58540aA04e273E0d","ftp_path":None},
    "ASR":  {"name":"AS Roma",              "sport":"football","tier":1,
             "contract":"0xa6610b3361c4c0D206Aa3364cd985016c2d89386","ftp_path":None},
    "ARG":  {"name":"Argentina National",   "sport":"football","tier":1,
             "contract":"0xd34625c1c812439229EF53e06f22053249D011f5","ftp_path":None},
    "AVL":  {"name":"Aston Villa",          "sport":"football","tier":2,
             "contract":"0x7B86b0836f3454e50C6F6a190cd692bB17da1928","ftp_path":None},
    "TRA":  {"name":"Trabzonspor",          "sport":"football","tier":2,
             "contract":"0xB2D0a13893Ac8640aEe1dFb3A35BA75A82d26F20","ftp_path":None},
    "BENFICA":{"name":"SL Benfica",         "sport":"football","tier":2,
             "contract":"0xBe82A95e11D96d2dFa8Dd4B83c3A7dD2b3A8A73E","ftp_path":None},
    "MENGO":{"name":"Flamengo",             "sport":"football","tier":2,
             "contract":"0x56e9F6F5A978e9845f04030F28B40dCC1Ef7c08b","ftp_path":None},
    "SAN":  {"name":"Club Santos Laguna",   "sport":"football","tier":2,
             "contract":"0x3e2e2b3e70d21B3BcD9D069Ca09f24f87D9ea3b9","ftp_path":None},
    "CHVS": {"name":"Chivas (Guadalajara)", "sport":"football","tier":2,
             "contract":"0xEFfEf7e0Bd9aB5B3B13A46D21a45d9E9B6f63E37","ftp_path":None},
    "UFC":  {"name":"UFC",                  "sport":"mma",     "tier":1,
             "contract":"0x09D6a2EE2C7b1E9CFCbCF5C52f7f47ee51a755A8","ftp_path":None},
    "SHARKS":{"name":"Sharks (Rugby)",      "sport":"rugby",   "tier":2,
             "contract":"0x4b5Df8A03B1C42F85bFf0c9C819d2f67c2f9fBdD","ftp_path":None},
    "SARRIES":{"name":"Saracens",           "sport":"rugby",   "tier":2,
             "contract":"0x8DFed51F9A99B3Fa7e91E30A8Ee7B7C8C9eA04b1","ftp_path":None},
    "SAUBER":{"name":"Alfa Romeo Racing",   "sport":"formula1","tier":2,
             "contract":"0x2Ae3f1Ec7F1F5012CFEab0185bfc7aa3cf0DEc22","ftp_path":None},
    "AM":   {"name":"Aston Martin F1",      "sport":"formula1","tier":2,
             "contract":"0xE7f924Ca4d5Cba720F8db0E55B3DA5Dc0B7c8D5f","ftp_path":None},
    "OG":   {"name":"OG Esports",           "sport":"esports", "tier":2,
             "contract":"0x19cA0F4aDb29e2130A56b9C9422150B5dc07f294","ftp_path":None},
    "HASHTAG":{"name":"Hashtag United",     "sport":"football","tier":3,
             "contract":"0xDf4C1E5C3b4C4E2E9a2c7f3a3d1B2F2E5A6C8D9E","ftp_path":None},
}

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def resolve_token(query: str):
    """Resolve ticker, club name, or partial match to registry entry."""
    q = query.upper().strip()
    if q in FAN_TOKEN_REGISTRY:
        return q, FAN_TOKEN_REGISTRY[q]
    # Fuzzy name match
    for ticker, data in FAN_TOKEN_REGISTRY.items():
        if q in data["name"].upper():
            return ticker, data
    return None, None

# ── Tool implementations ───────────────────────────────────────────────────────

def tool_token_state(token: str, include_supply: bool):
    ticker, data = resolve_token(token)
    if not data:
        return {"error": f"Token '{token}' not found in registry.",
                "available_tokens": list(FAN_TOKEN_REGISTRY.keys())}

    ftp = data.get("ftp_path")
    supply_mechanics = None
    if include_supply and ftp:
        supply_mechanics = {
            "path": ftp,
            "path2_mechanics": {
                "win_event":  "Permanent supply reduction ~0.24% circulating",
                "loss_event": "Supply NEUTRAL — re-mint to treasury only (NOT inflationary)",
                "pre_liquidation_t48h": "PROTOCOL_EVENT — never classify as bearish distribution",
                "amm_delay": "Wait T+15 post-WIN for AMM rebalancing before applying burn modifier",
                "chz_echo":  "CHZ ecosystem burn echo fires after WIN burn",
            } if ftp == "PATH_2" else {
                "path": ftp,
                "note": "PATH_1 mechanics — standard win/utility event model",
            }
        }

    # Lifecycle phase inference
    lifecycle_phase = "Phase 2 (active)" if data["tier"] == 1 else "Phase 2 (active)" if data["tier"] == 2 else "Phase 1 (early)"

    return {
        "ticker":           ticker,
        "name":             data["name"],
        "sport":            data["sport"],
        "tier":             data["tier"],
        "contract":         data["contract"],
        "chiliscan":        f"https://chiliscan.com/token/{data['contract']}",
        "ftp_path":         ftp,
        "ftp_confirmed":    data.get("ftp_confirmed"),
        "ftp_note":         data.get("ftp_note"),
        "lifecycle_phase":  lifecycle_phase,
        "supply_mechanics": supply_mechanics,
        "load_order":       "macro → fan-token/fan-token-lifecycle/ → fan-token/gamified-tokenomics-intelligence/ → fan-holder-profile-intelligence",
        "sportmind_version": VERSION,
        "assessed_at":      now_iso(),
    }

def tool_burn_forecast(token: str, competition: str, matches_remaining: int):
    ticker, data = resolve_token(token)
    if not data:
        return {"error": f"Token '{token}' not found."}

    ftp = data.get("ftp_path")
    if not ftp:
        return {
            "ticker": ticker,
            "name": data["name"],
            "ftp_path": None,
            "message": f"{data['name']} does not have an active FTP path. No burn events scheduled.",
            "sportmind_version": VERSION,
        }

    burn_per_win_pct = 0.24  # PATH_2 standard
    max_burns = matches_remaining

    return {
        "ticker":                ticker,
        "name":                  data["name"],
        "ftp_path":              ftp,
        "competition":           competition or "Not specified",
        "matches_remaining":     matches_remaining,
        "burn_per_win_pct":      burn_per_win_pct,
        "max_supply_reduction":  f"{burn_per_win_pct * max_burns:.2f}%",
        "schedule_note":         "Burn events only fire on WINS. LOSSES are supply neutral.",
        "pre_liquidation_rule":  "T-48h sell pressure = PROTOCOL_EVENT, not bearish signal",
        "amm_timing_rule":       "Apply burn modifier T+15 post-WIN (AMM rebalancing window)",
        "calendar_collapse_risk":"If team is eliminated, all remaining burn events are cancelled. Load tournament-elimination-intelligence.md.",
        "load_skills":           [
            "fan-token/gamified-tokenomics-intelligence/gamified-tokenomics-intelligence.md",
            "fan-token/tournament-elimination-intelligence.md",
        ],
        "sportmind_version":     VERSION,
        "assessed_at":           now_iso(),
    }

def tool_community_health(token: str):
    ticker, data = resolve_token(token)
    if not data:
        return {"error": f"Token '{token}' not found."}

    return {
        "ticker": ticker,
        "name":   data["name"],
        "chi_framework": {
            "score_range":    "0.0 – 1.0",
            "healthy":        "> 0.80",
            "needs_attention":"0.50 – 0.80",
            "at_risk":        "< 0.50",
        },
        "four_archetypes": {
            "LOYALIST":   "Long-term fans. Engage with belonging/heritage content. Do NOT send commercial token data.",
            "SPECULATOR": "Trade-focused. Engage with supply data, burn schedule, PATH_2 status.",
            "GOVERNOR":   "Governance-focused. Engage with vote notices (72h min). Trivial votes destroy this segment.",
            "AMPLIFIER":  "Social fans. Engage with shareable match content T-2h to T+2h window.",
        },
        "churn_risk_signals": {
            "loyalist_churn":   "CHI < 0.60 + no engagement >30 days = structural community damage",
            "speculator_exit":  "No trading activity >21 days = re-engage with upcoming burn event",
            "governor_cooling": "<1 of last 3 votes participated = check vote topic quality",
        },
        "load_skills": [
            "fan-token/fan-holder-profile-intelligence.md",
            "fan-token/fan-sentiment-intelligence/fan-sentiment-intelligence.md",
        ],
        "sportmind_version": VERSION,
        "assessed_at": now_iso(),
    }

def tool_fraud_scan(token: str, tvi_ratio: float, new_wallets_48h: int):
    ticker, data = resolve_token(token)
    name = data["name"] if data else token

    # MRS computation (simplified — full model in fraud-signal-intelligence.md)
    mrs_components = {}
    mrs_total = 0

    if tvi_ratio > 4.0:
        component = min(42, int((tvi_ratio - 1.0) * 8))
        mrs_components["volume_anomaly"] = component
        mrs_total += component

    if new_wallets_48h > 50:
        component = min(38, int(new_wallets_48h / 5))
        mrs_components["wallet_creation_spike"] = component
        mrs_total += component

    mrs_total = min(100, mrs_total)

    if mrs_total >= 75:
        classification = "COMPROMISED"
        action = "ABSTAIN — signal integrity cannot be trusted"
    elif mrs_total >= 50:
        classification = "SUSPECT"
        action = "WAIT — elevated risk, hold position"
    elif mrs_total >= 25:
        classification = "CAUTION"
        action = "PROCEED WITH REDUCED CONFIDENCE"
    else:
        classification = "TRUST"
        action = "PROCEED NORMALLY"

    return {
        "ticker":          ticker,
        "name":            name,
        "mrs_score":       mrs_total,
        "mrs_label":       classification,
        "recommended_action": action,
        "components":      mrs_components,
        "attack_types_checked": [
            "wash_trading (TVI anomaly)",
            "coordinated_wallet_creation",
        ],
        "full_framework":  "platform/fraud-signal-intelligence.md — 6 attack types, full MRS",
        "decay_rule":      "COMPROMISED requires 14 days clean before downgrade to TRUST",
        "sportmind_version": VERSION,
        "assessed_at":     now_iso(),
    }

def tool_holder_brief(token: str, archetype: str, event_type: str):
    ticker, data = resolve_token(token)
    name = data["name"] if data else token

    archetype = archetype.upper()
    event_type = event_type.lower()

    briefs = {
        "LOYALIST": {
            "win":  {"window":"T+0 to T+60","tone":"Celebratory, community, belonging","include":["Match result","Community message"],"exclude":["Token price","Supply data","APR"]},
            "loss": {"window":"T+60 to T+240","tone":"Supportive, resilience","include":["Club message"],"exclude":["Commercial data","Supply changes"]},
            "governance": {"window":"T-72h to T-24h","tone":"Participatory","include":["Vote topic in plain language"]},
        },
        "SPECULATOR": {
            "win":  {"window":"T+15 to T+30","tone":"Data, concise","include":["Burn amount","Supply reduction","Cumulative season burns"],"note":"NEVER send before T+15 — AMM rebalancing"},
            "loss": {"window":"T+60 to T+90","tone":"Factual","include":["Supply neutral confirmation"],"note":"Educate: LOSS = supply neutral, NOT inflationary"},
            "governance": {"window":"T-24h","tone":"Process-focused","include":["Vote mechanics","Quorum status"]},
        },
        "GOVERNOR": {
            "win":  {"window":"T+60 to T+120","tone":"Governance arc","include":["Next vote date"]},
            "loss": {"window":"T+120","tone":"Community health","include":["Next vote date if scheduled"]},
            "governance": {"window":"T-72h (first notice)","tone":"Participatory","include":["Vote topic","Current quorum","Deadline"]},
        },
        "AMPLIFIER": {
            "win":  {"window":"T+0 to T+30","tone":"Social, shareable","include":["Match highlights link","Social assets","Hashtag"]},
            "loss": {"window":"DO NOT send immediately","tone":"—","note":"Avoid amplifying loss narrative"},
            "governance": {"window":"Low priority","tone":"—","note":"Amplifiers rarely engage with governance"},
        },
    }

    brief = briefs.get(archetype, {}).get(event_type, {"note": f"No specific brief for {archetype} + {event_type}"})

    return {
        "ticker":        ticker,
        "name":          name,
        "archetype":     archetype,
        "event_type":    event_type,
        "engagement_brief": brief,
        "full_framework": "platform/fan-engagement-connector.md",
        "sportmind_version": VERSION,
        "assessed_at":   now_iso(),
    }

def tool_tournament_exit(token: str, competition: str, exit_round: str):
    ticker, data = resolve_token(token)
    name = data["name"] if data else token

    round_impacts = {
        "group_stage":     {"matches_cancelled": "3-4", "burns_lost_pct": "0.72-0.96", "ncsi_impact": "HIGH"},
        "round_of_16":     {"matches_cancelled": "2-3", "burns_lost_pct": "0.48-0.72", "ncsi_impact": "HIGH"},
        "quarter_final":   {"matches_cancelled": "1-2", "burns_lost_pct": "0.24-0.48", "ncsi_impact": "MEDIUM-HIGH"},
        "semi_final":      {"matches_cancelled": "1",   "burns_lost_pct": "0-0.24",    "ncsi_impact": "MEDIUM"},
        "final_defeat":    {"matches_cancelled": "0",   "burns_lost_pct": "0",         "ncsi_impact": "LOW (full run completed)"},
    }

    impact = round_impacts.get(exit_round.lower().replace(" ", "_"), {
        "matches_cancelled": "unknown", "burns_lost_pct": "unknown", "ncsi_impact": "unknown"
    })

    ftp = data.get("ftp_path") if data else None

    return {
        "ticker":               ticker,
        "name":                 name,
        "competition":          competition,
        "exit_round":           exit_round,
        "event_classification": "CALENDAR_COLLAPSE",
        "ftp_path":             ftp,
        "impact":               impact,
        "supply_note":          "All future WIN burn events in this competition are permanently cancelled" if ftp else "No FTP path active — standard CDI negative event only",
        "ltui_impact":          "LTUI trajectory resets to domestic-only outlook",
        "token_signal_window": {
            "t0_t4h":   "NEGATIVE CDI — emotional sell pressure",
            "t4h_t48h": "REASSESSMENT — domestic league re-priced",
            "t48h_plus": "New domestic-only LTUI baseline",
        },
        "agent_action":         "WAIT — load tournament-elimination-intelligence.md for full cascade",
        "load_skills":          ["fan-token/tournament-elimination-intelligence.md"],
        "sportmind_version":    VERSION,
        "assessed_at":          now_iso(),
    }

def tool_macro_context():
    """Chiliz-specific macro context."""
    macro_file = ROOT / "platform" / "macro-state.json"
    macro_data = {}
    if macro_file.exists():
        try:
            macro_data = json.loads(macro_file.read_text())
        except Exception:
            pass

    return {
        "chiliz_chain_id":    88888,
        "chz_status":         "MiCA whitepaper registered under ESMA (April 2026) — compliant",
        "virtuous_cycle":     "OPERATIONAL — 9.2M CHZ burned April 2026",
        "buyback_programme":  "Q2 2026: 10% of all Fan Token revenue used for CHZ buybacks",
        "omnichain_status":   "H1 2026 rollout — Fan Tokens bridgeable to EVM chains",
        "us_market":          "Re-entry confirmed Q1 2026. National team tokens for WC2026 summer.",
        "socios_defi_wallet": "Mid-2026 — DeFi wallet integration on Socios.com",
        "regulatory": {
            "EU_MiCA":        "COMPLIANT — ESMA registered April 2026",
            "US_SEC_CFTC":    "March 2026 joint guidance: fan tokens = digital collectibles/tools",
            "first_us_franchise_modifier": "×1.40 CDI at launch per league",
        },
        "macro_modifier":     macro_data.get("macro_state", {}).get("crypto_cycle", {}).get("macro_modifier", 1.00),
        "load_skills":        [
            "macro/macro-regulatory-sportfi.md",
            "macro/macro-crypto-market-cycles.md",
        ],
        "sportmind_version":  VERSION,
        "assessed_at":        now_iso(),
    }

def tool_registry(sport: str, tier: int):
    """Return filtered fan token registry."""
    results = {}
    for ticker, data in FAN_TOKEN_REGISTRY.items():
        if sport and data["sport"] != sport.lower():
            continue
        if tier and data["tier"] != tier:
            continue
        results[ticker] = {
            "name":     data["name"],
            "sport":    data["sport"],
            "tier":     data["tier"],
            "contract": data["contract"],
            "ftp_path": data.get("ftp_path"),
        }

    return {
        "count":   len(results),
        "filter":  {"sport": sport or "all", "tier": tier or "all"},
        "tokens":  results,
        "sportmind_version": VERSION,
        "assessed_at": now_iso(),
    }

# ── MCP wiring ─────────────────────────────────────────────────────────────────

TOOL_DESCRIPTIONS = {
    "ft_token_state":     "Get full FTP path status, lifecycle phase, and supply mechanics for a fan token.",
    "ft_burn_forecast":   "Forecast upcoming WIN burn events and maximum supply reduction for a competition.",
    "ft_community_health":"Get CHI framework, holder archetype model, and churn risk signals for a token.",
    "ft_fraud_scan":      "Run MRS (Manipulation Risk Score) scan. Flag wash trading and wallet creation spikes.",
    "ft_holder_brief":    "Get archetype-specific engagement recommendation for a token event (win/loss/governance).",
    "ft_tournament_exit": "Calculate CALENDAR_COLLAPSE impact if a team is eliminated from a competition.",
    "ft_macro_context":   "Get current Chiliz Chain macro state: MiCA status, CHZ cycle, regulatory context.",
    "ft_registry":        "Return fan token registry with optional sport/tier filter.",
}

TOOL_SCHEMAS = {
    "ft_token_state": {
        "type": "object",
        "properties": {
            "token":          {"type":"string","description":"Token ticker (AFC, PSG, BAR) or club name"},
            "include_supply": {"type":"boolean","description":"Include full supply mechanics","default":True},
        },
        "required": ["token"],
    },
    "ft_burn_forecast": {
        "type": "object",
        "properties": {
            "token":             {"type":"string","description":"Token ticker or club name"},
            "competition":       {"type":"string","description":"Current competition (UCL, Premier League, etc.)"},
            "matches_remaining": {"type":"integer","description":"Estimated matches remaining in competition","default":3},
        },
        "required": ["token"],
    },
    "ft_community_health": {
        "type": "object",
        "properties": {
            "token": {"type":"string","description":"Token ticker or club name"},
        },
        "required": ["token"],
    },
    "ft_fraud_scan": {
        "type": "object",
        "properties": {
            "token":            {"type":"string","description":"Token ticker or club name"},
            "tvi_ratio":        {"type":"number","description":"Current TVI vs 30-day average (e.g. 4.2 = 4.2× baseline)","default":1.0},
            "new_wallets_48h":  {"type":"integer","description":"New wallets created in last 48 hours","default":0},
        },
        "required": ["token"],
    },
    "ft_holder_brief": {
        "type": "object",
        "properties": {
            "token":      {"type":"string","description":"Token ticker or club name"},
            "archetype":  {"type":"string","description":"Holder archetype: LOYALIST, SPECULATOR, GOVERNOR, AMPLIFIER","enum":["LOYALIST","SPECULATOR","GOVERNOR","AMPLIFIER"]},
            "event_type": {"type":"string","description":"Event type: win, loss, governance","enum":["win","loss","governance"]},
        },
        "required": ["token","archetype","event_type"],
    },
    "ft_tournament_exit": {
        "type": "object",
        "properties": {
            "token":       {"type":"string","description":"Token ticker or club name"},
            "competition": {"type":"string","description":"Competition (UCL, World Cup, etc.)"},
            "exit_round":  {"type":"string","description":"Round of elimination","enum":["group_stage","round_of_16","quarter_final","semi_final","final_defeat"]},
        },
        "required": ["token","exit_round"],
    },
    "ft_macro_context": {
        "type": "object",
        "properties": {},
    },
    "ft_registry": {
        "type": "object",
        "properties": {
            "sport": {"type":"string","description":"Filter by sport (football, mma, rugby, formula1, esports)","default":""},
            "tier":  {"type":"integer","description":"Filter by tier (1, 2, or 3)","default":0},
        },
    },
}

async def _handle(name: str, args: dict):
    if name == "ft_token_state":
        return tool_token_state(args.get("token",""), args.get("include_supply",True))
    elif name == "ft_burn_forecast":
        return tool_burn_forecast(args.get("token",""), args.get("competition",""), args.get("matches_remaining",3))
    elif name == "ft_community_health":
        return tool_community_health(args.get("token",""))
    elif name == "ft_fraud_scan":
        return tool_fraud_scan(args.get("token",""), args.get("tvi_ratio",1.0), args.get("new_wallets_48h",0))
    elif name == "ft_holder_brief":
        return tool_holder_brief(args.get("token",""), args.get("archetype","LOYALIST"), args.get("event_type","win"))
    elif name == "ft_tournament_exit":
        return tool_tournament_exit(args.get("token",""), args.get("competition",""), args.get("exit_round","quarter_final"))
    elif name == "ft_macro_context":
        return tool_macro_context()
    elif name == "ft_registry":
        return tool_registry(args.get("sport",""), args.get("tier",0))
    return {"error": f"Unknown tool: {name}"}


async def run_stdio():
    try:
        from mcp.server import Server
        from mcp.server.stdio import stdio_server
        from mcp.types import Tool
    except ImportError:
        print("ERROR: pip install mcp", flush=True); return

    server = Server("sportmind-fan-token")

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

    server = Server("sportmind-fan-token")

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
            "service":"SportMind Fan Token MCP","version":VERSION,
            "tools":list(TOOL_SCHEMAS.keys()),"tool_count":len(TOOL_SCHEMAS),
        }, indent=2))

    app = web.Application()
    app.router.add_get("/mcp", handle_sse)
    app.router.add_get("/health", handle_health)
    app.router.add_get("/", handle_health)

    print(f"SportMind Fan Token MCP v{VERSION} — port {port}", flush=True)
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
    parser = argparse.ArgumentParser(description="SportMind Fan Token MCP Server")
    parser.add_argument("--http", action="store_true")
    parser.add_argument("--port", type=int, default=3002)
    args = parser.parse_args()
    asyncio.run(run_http(args.port) if args.http else run_stdio())
