#!/usr/bin/env python3
"""
SportMind Web Agent MCP Server v3.71.0
Exposes SportMind's three web agent connector targets as MCP tools for
web-capable agents (Fetch MCP, Claude in Chrome, browser-use, Playwright).

Three tools:
  wa_lineup_target    — returns exact URL, extraction spec, and translation
                        rules for lineup confirmation at T-2h for any sport
  wa_supply_verify    — returns Chiliscan API endpoints, extraction spec,
                        and burn verification logic for PATH_2 tokens
  wa_macro_monitor    — returns regulatory and Chiliz monitoring targets,
                        classification rules, and update workflow

Usage:
  python scripts/sportmind_wa_mcp.py              # stdio (Claude Desktop)
  python scripts/sportmind_wa_mcp.py --http       # HTTP/SSE port 3008

IMPORTANT: This server returns TARGETS AND SPECS, not live data.
  The web agent (Fetch MCP, browser) does the actual fetching.
  SportMind tells you WHAT to fetch and HOW to interpret it.

See platform/web-agent-connectors.md for full integration guide.
"""

import json
import asyncio
import argparse
from pathlib import Path
from datetime import datetime, timezone

ROOT    = Path(__file__).parent.parent
VERSION = "3.76.0"

# ── Fan token registry (contract addresses for supply verification) ───────────
FAN_TOKEN_CONTRACTS = {
    "AFC":     {"name": "Arsenal FC",          "contract": "0x1d4343d35f0E0e14C14115876D01dEAa4792550b", "ftp_path": "PATH_2"},
    "BAR":     {"name": "FC Barcelona",        "contract": "0xFD3C73b3B09D418841dd6Aff341b2d6e3abA433b", "ftp_path": None},
    "PSG":     {"name": "Paris Saint-Germain", "contract": "0xc2661815C69c2B3924D3dd0c2C1358A1E38A3105", "ftp_path": None},
    "CITY":    {"name": "Manchester City",     "contract": "0x6401b29F40a02578Ae44241560625232A01B3F79", "ftp_path": None},
    "JUV":     {"name": "Juventus",            "contract": "0x454038003a93cf44766aF352F74bad6B745616D0", "ftp_path": None},
    "ATM":     {"name": "Atlético de Madrid",  "contract": "0xe9506F70be469d2369803Ccf41823713BAFe8154", "ftp_path": None},
    "ACM":     {"name": "AC Milan",            "contract": "0x7F8b1C89e84c26d51e19Bbc66c21Ca88bD30d73B", "ftp_path": None},
    "INTER":   {"name": "Inter Milan",         "contract": "0xc727c9C0f2647CB90B0FCA64d8ddB14878716BeD", "ftp_path": None},
    "ASR":     {"name": "AS Roma",             "contract": "0xa6610b3361c4c0D206Aa3364cd985016c2d89386", "ftp_path": None},
    "GAL":     {"name": "Galatasaray",         "contract": "0x6DaB8Fe8e5d425F2Eb063aAe58540aA04e273E0d", "ftp_path": None},
    "ARG":     {"name": "Argentina",           "contract": "0xd34625c1c812439229EF53e06f22053249D011f5", "ftp_path": None},
    "UFC":     {"name": "UFC",                 "contract": "0x5C32e5FAf1D45bFdC875A2be78F6aa1b45e7CDf3", "ftp_path": None},
}

BURN_ADDRESS = "0x0000000000000000000000000000000000000000"
CHILISCAN_BASE = "https://chiliscan.com/api"

# ── Lineup confirmation targets by sport ─────────────────────────────────────
LINEUP_SOURCES = {
    "football": {
        "timing_before_kickoff_min": 75,
        "sources": [
            {
                "tier": 1,
                "name": "Club official X/Twitter account",
                "url_pattern": "https://twitter.com/{club_handle}",
                "what_to_look_for": "Tweet containing 'Starting XI' or '🚨' + player names",
                "extract": ["11 player names", "formation", "shirt numbers if listed"],
                "note": "Most reliable — official club post is ground truth"
            },
            {
                "tier": 1,
                "name": "Premier League official lineup",
                "url_pattern": "https://www.premierleague.com/match/{match_id}/lineups",
                "what_to_look_for": "Lineup grid with player names and numbers",
                "extract": ["home_xi", "away_xi", "substitutes", "formation"],
                "note": "Use for PL matches — requires match_id from PL website"
            },
            {
                "tier": 1,
                "name": "UEFA official lineup",
                "url_pattern": "https://www.uefa.com/uefachampionsleague/match/{match_id}/lineups",
                "what_to_look_for": "Starting lineup for both teams",
                "extract": ["home_xi", "away_xi", "formations"],
                "note": "Use for UCL/UEL/UECL matches"
            },
            {
                "tier": 2,
                "name": "BBC Sport match centre",
                "url_pattern": "https://www.bbc.co.uk/sport/football/{match_id}",
                "what_to_look_for": "Team lineups section",
                "extract": ["starting_xi", "substitutes"],
                "note": "Tier 2 — slightly delayed, but high reliability"
            }
        ],
        "availability_translation": {
            "confirmed_in_xi":          1.00,
            "confirmed_on_bench":       0.90,
            "confirmed_absent":         0.00,
            "not_in_18":                0.00,
            "source_tier_1_confirms":   0.98,
            "source_tier_2_confirms":   0.93,
            "not_found_in_lineup":      0.70,
        },
        "agent_rules": [
            "Compare extracted XI against expected squad from sportmind_pre_match",
            "Key player absent → raise ABSENCE_CONFIRMED, re-run ARI",
            "Unexpected formation → set TMAS_RECOMPUTE_REQUIRED flag",
            "Source unavailable → set availability_confidence=0.85, raise LINEUP_UNCONFIRMED"
        ]
    },
    "basketball": {
        "timing_before_kickoff_min": 90,
        "sources": [
            {
                "tier": 1,
                "name": "NBA official injury report",
                "url_pattern": "https://www.nba.com/game/{game_id}/injury-report",
                "what_to_look_for": "Player name, status (Available/Questionable/Doubtful/Out)",
                "extract": ["player_name", "status", "reason"],
                "note": "Released at T-90m and T-30m. T-30m is most accurate."
            },
            {
                "tier": 1,
                "name": "ESPN NBA game page",
                "url_pattern": "https://www.espn.com/nba/game/_/gameId/{game_id}",
                "what_to_look_for": "Injury report section",
                "extract": ["player_name", "status"],
                "note": "Mirrors official NBA injury report"
            }
        ],
        "availability_translation": {
            "Available":    1.00,
            "Questionable": 0.65,
            "Doubtful":     0.25,
            "Out":          0.00,
            "GTD":          0.60,
        },
        "agent_rules": [
            "NBA injury report is authoritative — Tier 1 ground truth",
            "GTD (game-time decision) = 0.60 until T-30m report confirms",
            "Star player Out → significant modifier change, re-run signal"
        ]
    },
    "cricket": {
        "timing_before_kickoff_min": 30,
        "sources": [
            {
                "tier": 1,
                "name": "ESPNcricinfo match page",
                "url_pattern": "https://www.espncricinfo.com/series/{series_id}/match/{match_id}",
                "what_to_look_for": "Playing XI announced after toss",
                "extract": ["playing_xi_home", "playing_xi_away", "toss_result", "elected_to"],
                "note": "XI and toss both available post-toss"
            },
            {
                "tier": 1,
                "name": "Official board Twitter",
                "url_pattern": "https://twitter.com/{board_handle}",
                "what_to_look_for": "Official XI announcement",
                "extract": ["11 player names"],
                "note": "ECB: @englandcricket, BCCI: @BCCI, Cricket Australia: @CricketAus"
            }
        ],
        "availability_translation": {
            "confirmed_playing": 1.00,
            "confirmed_absent":  0.00,
        },
        "agent_rules": [
            "Toss result affects signal — load dew_factor if batting second in T20",
            "Fast bowler absent → major signal impact; spinner absent → moderate",
            "Key batter absent → re-run pre-match signal with revised lineup"
        ]
    },
    "mma": {
        "timing_before_kickoff_min": 1440,
        "sources": [
            {
                "tier": 1,
                "name": "UFC official weigh-in results",
                "url_pattern": "https://www.ufc.com/events",
                "what_to_look_for": "Weigh-in results for the event",
                "extract": ["fighter_name", "weight", "made_weight", "missed_weight_by"],
                "note": "Weigh-ins at T-24h — weight miss is a critical signal"
            },
            {
                "tier": 1,
                "name": "MMA Fighting / ESPN MMA",
                "url_pattern": "https://www.mmafighting.com",
                "what_to_look_for": "Weigh-in results, fight cancellations",
                "extract": ["fighter_name", "weight_result"],
                "note": "Fastest mainstream coverage of weigh-in results"
            }
        ],
        "availability_translation": {
            "made_weight":        1.00,
            "missed_weight":      0.72,
            "fight_cancelled":    0.00,
        },
        "agent_rules": [
            "Weight miss → apply MMA weight-cut modifier immediately",
            "Fight cancellation → suspend all analysis, ABSTAIN signal",
            "Weigh-in is the primary availability confirmation in MMA"
        ]
    },
    "ice_hockey": {
        "timing_before_kickoff_min": 180,
        "sources": [
            {
                "tier": 1,
                "name": "NHL official game page",
                "url_pattern": "https://www.nhl.com/game/{game_id}",
                "what_to_look_for": "Starting lineup, injury updates",
                "extract": ["scratches", "goalie_starter"],
                "note": "NHL morning skate reports critical for injury confirmation"
            },
            {
                "tier": 2,
                "name": "Beat reporter Twitter",
                "url_pattern": "https://twitter.com/{beat_reporter}",
                "what_to_look_for": "Morning skate participation (did or did not skate)",
                "extract": ["player_name", "skated/did_not_skate"],
                "note": "Tier 2 — beat reporters reliable but not official"
            }
        ],
        "availability_translation": {
            "confirmed_starter":        1.00,
            "confirmed_scratch":        0.00,
            "morning_skate_confirmed":  0.95,
            "did_not_skate":            0.15,
        },
        "agent_rules": [
            "Morning skate participation is the primary signal T-3h",
            "Goalie confirmation is critical — starter vs backup has outsized impact",
            "Load morning_skate flag from core/core-athlete-modifier-system.md"
        ]
    }
}

# ── Regulatory monitoring targets ─────────────────────────────────────────────
REGULATORY_TARGETS = {
    "tier_1_act_within_24h": [
        {
            "name": "ESMA MiCA whitepaper register",
            "url": "https://www.esma.europa.eu/document/crypto-asset-white-papers",
            "frequency": "weekly",
            "what_to_extract": ["issuer_name", "token_name", "registration_date", "status"],
            "signal_on_new_registration": "regulatory_compliance = CONFIRMED for token",
            "signal_on_revocation": "raise REGULATORY_RISK_FLAG",
            "library_file_to_update": "macro/macro-regulatory-sportfi.md"
        },
        {
            "name": "SEC press releases",
            "url": "https://www.sec.gov/news/pressreleases",
            "frequency": "daily",
            "what_to_extract": ["title", "date", "keywords_fan_token", "ruling_type"],
            "signal": "Any mention of fan tokens, digital collectibles, sports tokens",
            "library_file_to_update": "macro/macro-regulatory-sportfi.md"
        },
        {
            "name": "CFTC press releases",
            "url": "https://www.cftc.gov/PressRoom/PressReleases",
            "frequency": "daily",
            "what_to_extract": ["title", "date", "affected_asset_classes"],
            "signal": "Joint guidance or crypto-asset classification",
            "library_file_to_update": "macro/macro-regulatory-sportfi.md"
        },
        {
            "name": "Chiliz official blog",
            "url": "https://www.chiliz.com/blog",
            "frequency": "daily",
            "what_to_extract": ["title", "date", "club_names_mentioned", "mechanic_changes"],
            "signal": "New fan token partnerships, PATH_2 rollouts, tokenomics changes",
            "library_file_to_update": "scripts/sportmind_ft_mcp.py (FAN_TOKEN_REGISTRY)"
        },
        {
            "name": "Chiliz Twitter",
            "url": "https://twitter.com/Chiliz",
            "frequency": "every_4h",
            "what_to_extract": ["new_partnership_mentions", "supply_mechanic_announcements"],
            "signal": "New FTP paths, club launches, CHZ burn announcements",
            "library_file_to_update": "fan-token/gamified-tokenomics-intelligence/"
        },
    ],
    "tier_2_review_within_72h": [
        {
            "name": "Socios fan tokens page",
            "url": "https://www.socios.com/fan-tokens",
            "frequency": "weekly",
            "what_to_extract": ["active_tokens", "new_listings", "delistings"],
            "signal": "New team launches, delistings, utility changes",
            "library_file_to_update": "platform/sportmind-mcp-server.md (registry)"
        },
        {
            "name": "CoinDesk regulatory coverage",
            "url": "https://www.coindesk.com/policy",
            "frequency": "daily",
            "what_to_extract": ["title", "date", "jurisdiction", "ruling_summary"],
            "signal": "Fan token regulatory developments globally",
            "classification": "Apply core/external-intelligence-intake.md framework"
        },
        {
            "name": "The Block regulatory",
            "url": "https://www.theblock.co/category/regulation",
            "frequency": "daily",
            "what_to_extract": ["title", "date", "affected_entities"],
            "signal": "Crypto regulatory developments affecting sports tokens",
            "classification": "Apply core/external-intelligence-intake.md framework"
        },
    ],
    "classification_workflow": [
        "1. Fetch source URL",
        "2. Extract: headline, date, jurisdiction, affected entities, ruling type",
        "3. Classify per core/external-intelligence-intake.md: Tier 1 / 2 / 3",
        "4. Tier 1: identify which library files need updating",
        "5. Generate update recommendation with file path, section, draft change",
        "6. Human review required before any library change — no auto-updates",
    ]
}


# ── Tool implementations ───────────────────────────────────────────────────────

def tool_wa_lineup_target(sport: str, home_team: str = "", competition: str = "",
                           kickoff: str = "", include_all_sources: bool = False):
    sport_key = sport.lower().replace("-", "_").replace(" ", "_")

    if sport_key not in LINEUP_SOURCES:
        supported = list(LINEUP_SOURCES.keys())
        return {
            "error": f"Sport '{sport}' not yet mapped. Supported: {supported}",
            "note": "Add the sport's lineup source to platform/web-agent-connectors.md",
            "version": VERSION,
        }

    config = LINEUP_SOURCES[sport_key]
    sources = config["sources"] if include_all_sources else [s for s in config["sources"] if s["tier"] == 1]

    result = {
        "connector":     "lineup_confirmation",
        "sport":         sport,
        "home_team":     home_team or "not specified",
        "competition":   competition or "not specified",
        "timing": {
            "fetch_at":     f"T-{config['timing_before_kickoff_min']}min before kickoff",
            "kickoff":      kickoff or "not specified",
            "note":         "Fetch earlier sources only for monitoring; use T-2h for confirmation"
        },
        "fetch_targets": sources,
        "extraction_spec": {
            "what_to_extract": ["starting_xi", "formation", "notable_absences", "substitutes"],
            "match_player_names": "Fuzzy match acceptable — 'Saka' matches 'Bukayo Saka' matches 'B. Saka'",
            "compare_against":   "sportmind_pre_match response squad brief"
        },
        "availability_translation": config["availability_translation"],
        "agent_rules":    config["agent_rules"],
        "on_absence_detected": {
            "key_player_absent":    "Re-run ARI with availability_confidence=0.00 for absent player",
            "unexpected_starter":   "Flag UNEXPECTED_INCLUSION, review ARI for that player",
            "formation_change":     "Set TMAS_RECOMPUTE_REQUIRED, reload tactical matchup",
            "source_unavailable":   "Set availability_confidence=0.85, raise LINEUP_UNCONFIRMED"
        },
        "ref":           "platform/web-agent-connectors.md — Connector 1",
        "assessed_at":   datetime.now(timezone.utc).isoformat(),
        "version":       VERSION,
    }
    return result


def tool_wa_supply_verify(token: str, pre_match_supply: float = 0.0,
                           match_result: str = "", hours_since_match: float = 0.0):
    ticker = token.upper().strip()
    data   = FAN_TOKEN_CONTRACTS.get(ticker)

    if not data:
        return {
            "error": f"Token '{ticker}' not in registry. Use ft_registry for full list.",
            "version": VERSION,
        }

    contract = data["contract"]
    ftp_path = data.get("ftp_path")

    # Build Chiliscan API endpoints
    api_endpoints = {
        "token_info": (
            f"{CHILISCAN_BASE}?module=token&action=tokeninfo"
            f"&contractaddress={contract}"
        ),
        "burn_transactions": (
            f"{CHILISCAN_BASE}?module=account&action=tokentx"
            f"&contractaddress={contract}"
            f"&address={BURN_ADDRESS}"
            f"&sort=desc&offset=10"
        ),
        "supply_browser": f"https://chiliscan.com/token/{contract}",
    }

    # Timing guidance
    timing_ok  = hours_since_match <= 0 or hours_since_match >= 0.25  # T+15m minimum
    timing_def = hours_since_match <= 0 or hours_since_match >= 6.0   # T+6h definitive

    # Expected burn if PATH_2 WIN
    expected_burn_pct = 0.0024  # 0.24%
    expected_burn_abs = pre_match_supply * expected_burn_pct if pre_match_supply > 0 else None

    # Determine what to verify based on match_result
    verification_context = {}
    if match_result.upper() in ("WIN", "HOME", "AWAY"):
        if ftp_path == "PATH_2":
            verification_context = {
                "expected_event":      "WIN_BURN",
                "expected_supply_change": f"−{expected_burn_pct*100:.2f}% (approximately {round(expected_burn_abs):,} tokens burned)" if expected_burn_abs else f"−{expected_burn_pct*100:.2f}% of circulating supply",
                "burn_address":        BURN_ADDRESS,
                "tolerance":           "±0.05% of expected burn amount",
                "confirmation_rule":   "Transaction to 0x0000... from contract within T+4h of match end",
                "timing_warning":      None if timing_def else "AMM rebalancing may still be in progress — wait until T+6h for definitive check",
            }
        else:
            verification_context = {
                "expected_event": "WIN — no PATH_2 active, no supply change expected",
                "note": "Token has no active Fan Token Play path. No burn mechanics.",
            }
    elif match_result.upper() in ("LOSS", "DRAW"):
        if ftp_path == "PATH_2":
            verification_context = {
                "expected_event":   "LOSS_SUPPLY_NEUTRAL",
                "expected_change":  "Zero — pre-liquidated amount re-mints to treasury only",
                "verification":     "Confirm: post-match supply = pre-match supply (±0.001%)",
                "critical_rule":    "If supply INCREASED: raise UNEXPECTED_SUPPLY_CHANGE immediately",
                "agent_rule":       "NEVER apply dilution modifier after PATH_2 loss"
            }

    return {
        "connector":            "path2_supply_verification",
        "token":                ticker,
        "name":                 data["name"],
        "ftp_path":             ftp_path,
        "contract_address":     contract,
        "chain_id":             88888,
        "api_endpoints":        api_endpoints,
        "match_result":         match_result or "not specified",
        "verification_context": verification_context,
        "extraction_spec": {
            "from_tokeninfo":        ["totalSupply", "circulatingSupply", "holders"],
            "from_burn_transactions": ["tx_hash", "amount", "blockTimestamp"],
            "compute":               "supply_delta = pre_match_supply - post_match_supply",
            "confirm_burn":          "delta / pre_match_supply ≈ 0.0024 (PATH_2 WIN)",
        },
        "timing_rules": {
            "minimum_wait":      "T+15min (AMM rebalancing)",
            "recommended_check": "T+30min",
            "definitive_check":  "T+6h",
            "maximum_wait":      "T+24h before BURN_MISSING flag",
            "timing_ok":         timing_ok,
            "timing_definitive": timing_def,
        },
        "season_log_schema": {
            "fields": ["date", "match", "result", "supply_before", "supply_after", "burn_pct", "tx_hash", "confirmed"],
            "store":  "Update after each confirmed event; feed into ft_supply_history tool"
        },
        "failure_modes": {
            "api_unavailable":    "Try browser URL: " + api_endpoints["supply_browser"],
            "supply_mismatch":    "Flag SUPPLY_ANOMALY — halt automated tracking, escalate",
            "no_burn_at_T+4h":   "Wait until T+15h before BURN_MISSING flag (treasury may not have settled)",
        },
        "ref":     "platform/web-agent-connectors.md — Connector 2",
        "assessed_at": datetime.now(timezone.utc).isoformat(),
        "version": VERSION,
    }


def tool_wa_macro_monitor(tier: str = "all", domain: str = "all"):
    tier_filter = tier.lower()
    domain_filter = domain.lower()

    targets = {}

    if tier_filter in ("all", "1", "tier_1"):
        t1 = REGULATORY_TARGETS["tier_1_act_within_24h"]
        if domain_filter != "all":
            t1 = [t for t in t1 if domain_filter in t["name"].lower() or domain_filter in t["url"].lower()]
        targets["tier_1_act_within_24h"] = t1

    if tier_filter in ("all", "2", "tier_2"):
        t2 = REGULATORY_TARGETS["tier_2_review_within_72h"]
        if domain_filter != "all":
            t2 = [t for t in t2 if domain_filter in t["name"].lower() or domain_filter in t["url"].lower()]
        targets["tier_2_review_within_72h"] = t2

    return {
        "connector":              "regulatory_macro_monitoring",
        "monitoring_targets":     targets,
        "classification_workflow": REGULATORY_TARGETS["classification_workflow"],
        "library_files_at_risk": [
            "macro/macro-regulatory-sportfi.md — regulatory status, US market, ESMA",
            "macro/macro-crypto-market-cycles.md — CHZ virtuous cycle, burn confirmations",
            "fan-token/gamified-tokenomics-intelligence/ — supply mechanic changes",
            "scripts/sportmind_ft_mcp.py — FAN_TOKEN_REGISTRY new tokens",
            "platform/sportmind-mcp-server.md — tool registry updates",
        ],
        "critical_rules": [
            "Tier 1 regulatory facts require human confirmation before library update",
            "Official sources (ESMA, SEC, CFTC, Chiliz) always supersede media reporting",
            "Foreign-language regulatory text: flag for human review, do not auto-classify",
            "Conflicting signals: official source wins; flag conflict for review",
            "NO automatic library changes from web agent output — ever",
        ],
        "monitoring_schedule": {
            "ESMA_register":  "Weekly",
            "SEC_CFTC":       "Daily (active regulatory period)",
            "Chiliz_blog":    "Daily",
            "Chiliz_Twitter": "Every 4h",
            "Socios":         "Weekly",
            "CoinDesk_Block": "Daily",
        },
        "intake_ref":  "core/external-intelligence-intake.md — classification tiers",
        "sources_ref": "core/verifiable-sources-by-sport.md — tier definitions",
        "ref":         "platform/web-agent-connectors.md — Connector 3",
        "assessed_at": datetime.now(timezone.utc).isoformat(),
        "version":     VERSION,
    }


# ── MCP schemas ────────────────────────────────────────────────────────────────

TOOL_DESCRIPTIONS = {
    "wa_lineup_target": (
        "Returns exact URL targets, extraction spec, and SportMind translation rules "
        "for lineup confirmation at T-2h for any supported sport. Call before fetching "
        "lineup data — this tool tells the web agent what to fetch and how to interpret it. "
        "Supported sports: football, basketball, cricket, mma, ice_hockey."
    ),
    "wa_supply_verify": (
        "Returns Chiliscan API endpoints, extraction spec, and burn verification logic "
        "for PATH_2 fan token supply confirmation. Provide token ticker and match result "
        "for context-specific verification instructions. Returns timing rules, expected "
        "burn amounts, and failure mode handling."
    ),
    "wa_macro_monitor": (
        "Returns regulatory and Chiliz monitoring targets with fetch URLs, extraction specs, "
        "classification workflow, and library files at risk. Filter by tier (1=act within 24h, "
        "2=review within 72h) or domain (chiliz, esma, sec, socios). Use to build a "
        "monitoring agent that keeps the SportMind macro layer current."
    ),
}

TOOL_SCHEMAS = {
    "wa_lineup_target": {
        "type": "object",
        "properties": {
            "sport": {
                "type": "string",
                "enum": ["football", "basketball", "cricket", "mma", "ice_hockey"],
                "description": "Sport for lineup confirmation"
            },
            "home_team":           {"type": "string", "description": "Home team name (for context)"},
            "competition":         {"type": "string", "description": "Competition name (e.g. UCL, Premier League)"},
            "kickoff":             {"type": "string", "description": "ISO-8601 kickoff datetime"},
            "include_all_sources": {"type": "boolean", "default": False,
                                    "description": "Include Tier 2 sources in addition to Tier 1"},
        },
        "required": ["sport"],
    },
    "wa_supply_verify": {
        "type": "object",
        "properties": {
            "token":              {"type": "string", "description": "Fan token ticker (e.g. AFC, PSG)"},
            "pre_match_supply":   {"type": "number", "description": "Supply figure before the match (for delta calculation)", "default": 0},
            "match_result":       {"type": "string", "enum": ["WIN", "LOSS", "DRAW", "HOME", "AWAY", ""],
                                   "description": "Match result for context-specific verification"},
            "hours_since_match":  {"type": "number", "description": "Hours since match ended (for timing guidance)", "default": 0},
        },
        "required": ["token"],
    },
    "wa_macro_monitor": {
        "type": "object",
        "properties": {
            "tier":   {"type": "string", "enum": ["all", "1", "2", "tier_1", "tier_2"], "default": "all",
                       "description": "Filter by monitoring tier"},
            "domain": {"type": "string", "default": "all",
                       "description": "Filter by domain: chiliz, esma, sec, socios, coindesk, all"},
        },
        "required": [],
    },
}


# ── Dispatcher ─────────────────────────────────────────────────────────────────

async def _handle_tool(name: str, arguments: dict):
    if name == "wa_lineup_target":
        return tool_wa_lineup_target(
            arguments.get("sport", "football"),
            arguments.get("home_team", ""),
            arguments.get("competition", ""),
            arguments.get("kickoff", ""),
            arguments.get("include_all_sources", False),
        )
    elif name == "wa_supply_verify":
        return tool_wa_supply_verify(
            arguments.get("token", ""),
            arguments.get("pre_match_supply", 0.0),
            arguments.get("match_result", ""),
            arguments.get("hours_since_match", 0.0),
        )
    elif name == "wa_macro_monitor":
        return tool_wa_macro_monitor(
            arguments.get("tier", "all"),
            arguments.get("domain", "all"),
        )
    else:
        return {"error": f"Unknown tool: {name}"}


# ── Server runners ─────────────────────────────────────────────────────────────

async def run_stdio():
    try:
        from mcp.server import Server
        from mcp.server.stdio import stdio_server
        from mcp.types import Tool, TextContent
    except ImportError:
        print("ERROR: pip install mcp aiohttp", flush=True)
        return

    server = Server("sportmind-web-agent")

    @server.list_tools()
    async def list_tools():
        return [Tool(name=n, description=TOOL_DESCRIPTIONS[n], inputSchema=TOOL_SCHEMAS[n])
                for n in TOOL_SCHEMAS]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict):
        result = await _handle_tool(name, arguments)
        from mcp.types import TextContent
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    async with stdio_server() as streams:
        await server.run(*streams, server.create_initialization_options())


async def run_http(port: int):
    try:
        from mcp.server import Server
        from mcp.server.sse import SseServerTransport
        from mcp.types import Tool, TextContent
        from aiohttp import web
    except ImportError:
        print("ERROR: pip install mcp aiohttp", flush=True)
        return

    server = Server("sportmind-web-agent")

    @server.list_tools()
    async def list_tools():
        return [Tool(name=n, description=TOOL_DESCRIPTIONS[n], inputSchema=TOOL_SCHEMAS[n])
                for n in TOOL_SCHEMAS]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict):
        result = await _handle_tool(name, arguments)
        from mcp.types import TextContent
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    transport = SseServerTransport("/mcp")

    async def handle_sse(request):
        async with transport.connect_sse(request.headers, request) as streams:
            await server.run(*streams, server.create_initialization_options())

    async def handle_health(request):
        return web.Response(
            content_type="application/json",
            text=json.dumps({"status": "ok", "server": "sportmind-web-agent", "version": VERSION}),
        )

    app = web.Application()
    app.router.add_get("/health", handle_health)
    app.router.add_get("/mcp", handle_sse)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"SportMind Web Agent MCP running on port {port}", flush=True)
    await asyncio.Event().wait()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SportMind Web Agent MCP Server")
    parser.add_argument("--http", action="store_true")
    parser.add_argument("--port", type=int, default=3008)
    args = parser.parse_args()
    asyncio.run(run_http(args.port) if args.http else run_stdio())
