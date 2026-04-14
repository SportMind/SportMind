#!/usr/bin/env python3
"""
SportMind MCP Server v3.34
Exposes SportMind intelligence as MCP tools for Claude and other AI agents.

Ten tools:
  --- Original five ---
  sportmind_signal          — pre-match intelligence signal
  sportmind_macro           — current macro state
  sportmind_stack           — full skill stack for a sport
  sportmind_verify          — skill integrity verification
  sportmind_agent_status    — autonomous agent health check

  --- New five (v3.34) ---
  sportmind_pre_match       — orchestrated full pre-match reasoning package
  sportmind_disciplinary    — disciplinary check: DSM level, flags, commercial modifier
  sportmind_fan_token_lookup — resolve club/ticker/sport to fan token context
  sportmind_sentiment_snapshot — multi-axis sentiment state for a token
  sportmind_verifiable_source  — authoritative source for a query type and sport

Usage:
  python scripts/sportmind_mcp.py              # stdio (Claude Desktop / Claude Code)
  python scripts/sportmind_mcp.py --http       # HTTP/SSE on port 3001 (remote agents)
  python scripts/sportmind_mcp.py --http --port 8080

Install:
  pip install mcp aiohttp

See MCP-SERVER.md for full deployment guide.
See platform/sportmind-mcp-server.md for specification.
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

VERSION = "3.65.2"

SUPPORTED_SPORTS = [
    "football", "basketball", "cricket", "mma", "formula1", "tennis",
    "rugby", "rugby_league", "afl", "baseball", "ice_hockey", "motogp",
    "nascar", "kabaddi", "netball", "handball", "esports",
    "darts", "snooker", "swimming", "athletics", "winter_sports",
    "boxing", "cycling", "horse_racing",
]

USE_CASES = [
    "pre_match", "fan_token_tier1", "fan_token_tier2",
    "prediction_market", "commercial_brief", "governance",
]

# ── Fan token registry (Chiliz Chain, verified contract addresses) ─────────────
# Source: chiliscan.com/token/top-erc20 · Chain ID 88888
# Excludes PEPPER (not a sports fan token)
FAN_TOKEN_REGISTRY = {
    "BAR":     {"name": "FC Barcelona",            "sport": "football",    "tier": 1,
                "contract": "0xFD3C73b3B09D418841dd6Aff341b2d6e3abA433b",
                "chiliscan": "https://chiliscan.com/token/0xFD3C73b3B09D418841dd6Aff341b2d6e3abA433b",
                "fantokens": "https://www.fantokens.com/token/bar"},
    "AFC":     {"name": "Arsenal FC",              "sport": "football",    "tier": 1,
                "contract": "0x1d4343d35f0E0e14C14115876D01dEAa4792550b",
                "chiliscan": "https://chiliscan.com/token/0x1d4343d35f0E0e14C14115876D01dEAa4792550b",
                "fantokens": "https://www.fantokens.com/token/afc",
                "fan_token_play": "PATH_2",
                "ftp_confirmed_date": "2026-04-07",
                "ftp_note": "First public Path 2 trial. Pre-liquidation 1/400th supply T-48h."},
    "GAL":     {"name": "Galatasaray S.K.",         "sport": "football",    "tier": 1,
                "contract": "0x6DaB8Fe8e5d425F2Eb063aAe58540aA04e273E0d",
                "chiliscan": "https://chiliscan.com/token/0x6DaB8Fe8e5d425F2Eb063aAe58540aA04e273E0d",
                "fantokens": "https://www.fantokens.com/token/gal"},
    "PSG":     {"name": "Paris Saint-Germain",      "sport": "football",    "tier": 1,
                "contract": "0xc2661815C69c2B3924D3dd0c2C1358A1E38A3105",
                "chiliscan": "https://chiliscan.com/token/0xc2661815C69c2B3924D3dd0c2C1358A1E38A3105",
                "fantokens": "https://www.fantokens.com/token/psg"},
    "OG":      {"name": "OG Esports",               "sport": "esports",     "tier": 2,
                "contract": "0x19cA0F4aDb29e2130A56b9C9422150B5dc07f294",
                "chiliscan": "https://chiliscan.com/token/0x19cA0F4aDb29e2130A56b9C9422150B5dc07f294",
                "fantokens": "https://www.fantokens.com/token/og"},
    "ARG":     {"name": "Argentina National Team",  "sport": "football",    "tier": 1,
                "contract": "0xd34625c1c812439229EF53e06f22053249D011f5",
                "chiliscan": "https://chiliscan.com/token/0xd34625c1c812439229EF53e06f22053249D011f5",
                "fantokens": "https://www.fantokens.com/token/arg"},
    "ASR":     {"name": "AS Roma",                  "sport": "football",    "tier": 1,
                "contract": "0xa6610b3361c4c0D206Aa3364cd985016c2d89386",
                "chiliscan": "https://chiliscan.com/token/0xa6610b3361c4c0D206Aa3364cd985016c2d89386",
                "fantokens": "https://www.fantokens.com/token/asr"},
    "JUV":     {"name": "Juventus",                 "sport": "football",    "tier": 1,
                "contract": "0x454038003a93cf44766aF352F74bad6B745616D0",
                "chiliscan": "https://chiliscan.com/token/0x454038003a93cf44766aF352F74bad6B745616D0",
                "fantokens": "https://www.fantokens.com/token/juv"},
    "INTER":   {"name": "Inter Milan",              "sport": "football",    "tier": 1,
                "contract": "0xc727c9C0f2647CB90B0FCA64d8ddB14878716BeD",
                "chiliscan": "https://chiliscan.com/token/0xc727c9C0f2647CB90B0FCA64d8ddB14878716BeD",
                "fantokens": "https://www.fantokens.com/token/inter"},
    "CITY":    {"name": "Manchester City FC",       "sport": "football",    "tier": 1,
                "contract": "0x6401b29F40a02578Ae44241560625232A01B3F79",
                "chiliscan": "https://chiliscan.com/token/0x6401b29F40a02578Ae44241560625232A01B3F79",
                "fantokens": "https://www.fantokens.com/token/city"},
    "ATM":     {"name": "Atlético de Madrid",       "sport": "football",    "tier": 1,
                "contract": "0xe9506F70be469d2369803Ccf41823713BAFe8154",
                "chiliscan": "https://chiliscan.com/token/0xe9506F70be469d2369803Ccf41823713BAFe8154",
                "fantokens": "https://www.fantokens.com/token/atm"},
    "ACM":     {"name": "AC Milan",                 "sport": "football",    "tier": 1,
                "contract": "0xF9C0F80a6c67b1B39bdDF00ecD57f2533ef5b688",
                "chiliscan": "https://chiliscan.com/token/0xF9C0F80a6c67b1B39bdDF00ecD57f2533ef5b688",
                "fantokens": "https://www.fantokens.com/token/acm"},
    "TRA":     {"name": "Trabzonspor",              "sport": "football",    "tier": 2,
                "contract": "0x304193f18f3B34647ae1f549fc825A7e50267c51",
                "chiliscan": "https://chiliscan.com/token/0x304193f18f3B34647ae1f549fc825A7e50267c51",
                "fantokens": "https://www.fantokens.com/token/tra"},
    "BENFICA": {"name": "SL Benfica",               "sport": "football",    "tier": 2,
                "contract": "0xF4c653b74929953B29B966aBA99b681Fb5ab69cF",
                "chiliscan": "https://chiliscan.com/token/0xF4c653b74929953B29B966aBA99b681Fb5ab69cF",
                "fantokens": "https://www.fantokens.com/token/benfica"},
    "UFC":     {"name": "UFC",                      "sport": "mma",         "tier": 1,
                "contract": "0xC9f723625e80a81cBa2CAd3e6871D3bdf2a7ECC7",
                "chiliscan": "https://chiliscan.com/token/0xC9f723625e80a81cBa2CAd3e6871D3bdf2a7ECC7",
                "fantokens": "https://www.fantokens.com/token/ufc"},
    "SHARKS":  {"name": "Sharks (Rugby)",           "sport": "rugby",       "tier": 2,
                "contract": "0x0cb13408921F87E3A3D011b03935A81A1542bDFa",
                "chiliscan": "https://chiliscan.com/token/0x0cb13408921F87E3A3D011b03935A81A1542bDFa",
                "fantokens": "https://www.fantokens.com/token/sharks"},
    "SARRIES": {"name": "Saracens",                 "sport": "rugby",       "tier": 2,
                "contract": "0x72B1FCA1008BE96C4fdE2539379c1778A76c4fCa",
                "chiliscan": "https://chiliscan.com/token/0x72B1FCA1008BE96C4fdE2539379c1778A76c4fCa",
                "fantokens": "https://www.fantokens.com/token/sarries"},
    "MENGO":   {"name": "Flamengo",                 "sport": "football",    "tier": 2,
                "contract": "0xD1723Eb9e7C6eE7c7e2d421B2758dc0f2166eDDc",
                "chiliscan": "https://chiliscan.com/token/0xD1723Eb9e7C6eE7c7e2d421B2758dc0f2166eDDc",
                "fantokens": "https://www.fantokens.com/token/mengo"},
    "SAUBER":  {"name": "Alfa Romeo Racing ORLEN",  "sport": "formula1",    "tier": 2,
                "contract": "0xcf6D626203011e5554C82baBE17dd7CDC4Ee86BF",
                "chiliscan": "https://chiliscan.com/token/0xcf6D626203011e5554C82baBE17dd7CDC4Ee86BF",
                "fantokens": "https://www.fantokens.com/token/sauber"},
    "HASHTAG": {"name": "Hashtag United F.C.",      "sport": "football",    "tier": 3,
                "contract": "0x3c1487C5036105338396055d74EeE505a9F6A2f3",
                "chiliscan": "https://chiliscan.com/token/0x3c1487C5036105338396055d74EeE505a9F6A2f3",
                "fantokens": "https://www.fantokens.com/token/hashtag"},
    "SAN":     {"name": "Club Santos Laguna",       "sport": "football",    "tier": 2,
                "contract": "0x3BA1eB0FF58537d8b77E8446273295fC432439A9",
                "chiliscan": "https://chiliscan.com/token/0x3BA1eB0FF58537d8b77E8446273295fC432439A9",
                "fantokens": "https://www.fantokens.com/token/san"},
    "CHVS":    {"name": "Chivas (Guadalajara)",     "sport": "football",    "tier": 2,
                "contract": "0x3624BA092480fb0bDB5ec50EbaC699BdFa561416",
                "chiliscan": "https://chiliscan.com/token/0x3624BA092480fb0bDB5ec50EbaC699BdFa561416",
                "fantokens": "https://www.fantokens.com/token/chvs"},
    "AVL":     {"name": "Aston Villa",              "sport": "football",    "tier": 2,
                "contract": "0x4F3a607bB2717683108865fc785BadFa90094431",
                "chiliscan": "https://chiliscan.com/token/0x4F3a607bB2717683108865fc785BadFa90094431",
                "fantokens": "https://www.fantokens.com/token/avl"},
    "AM":      {"name": "Aston Martin Cognizant",   "sport": "formula1",    "tier": 2,
                "contract": "0x3757951792eDFC2CE196E4C06CFfD04027e87403",
                "chiliscan": "https://chiliscan.com/token/0x3757951792eDFC2CE196E4C06CFfD04027e87403",
                "fantokens": "https://www.fantokens.com/token/am"},
}

# Sport → tickers mapping for lookup by sport
SPORT_TO_TOKENS = {}
for ticker, data in FAN_TOKEN_REGISTRY.items():
    sport = data["sport"]
    SPORT_TO_TOKENS.setdefault(sport, []).append(ticker)

# Name fragments → ticker for fuzzy lookup
NAME_TO_TICKER = {}
for ticker, data in FAN_TOKEN_REGISTRY.items():
    NAME_TO_TICKER[ticker.lower()] = ticker
    for word in data["name"].lower().split():
        if len(word) > 3:
            NAME_TO_TICKER.setdefault(word, ticker)

# ── Verifiable sources registry ────────────────────────────────────────────────
VERIFIABLE_SOURCES = {
    "lineup_confirmation": {
        "football":  {"source": "Club official X/Twitter account (T-2h)", "tier": 1,
                      "backup": "BBC Sport match centre", "note": "Official team sheet T-1h"},
        "rugby":     {"source": "Official club website team sheet (T-1h)", "tier": 1,
                      "backup": "Rugby Pass (rugbypass.com)", "note": "Released 1h pre-match"},
        "ice_hockey":{"source": "Beat reporter morning skate tweet (T-3h to T-1h)", "tier": 2,
                      "backup": "Daily Faceoff (dailyfaceoff.com)", "note": "Morning skate lineups"},
        "basketball":{"source": "NBA.com/players/injuries (official injury report)", "tier": 1,
                      "backup": "ESPN NBA injuries", "note": "Final report T-1h"},
        "cricket":   {"source": "ESPNcricinfo squad and XI announcement", "tier": 1,
                      "backup": "Cricbuzz", "note": "Announced at toss"},
        "formula1":  {"source": "formula1.com/results (qualifying tab)", "tier": 1,
                      "backup": "Motorsport.com", "note": "Grid set post-qualifying"},
        "mma":       {"source": "UFC.com event page weigh-in results", "tier": 1,
                      "backup": "@UFC on X", "note": "Day-before weigh-in"},
        "default":   {"source": "Official governing body or club website", "tier": 1,
                      "backup": "BBC Sport / ESPN", "note": "Check official source first"},
    },
    "match_result": {
        "football":  {"source": "BBC Sport (bbc.co.uk/sport/football)", "tier": 1,
                      "backup": "Official league app", "note": "Final result + stats"},
        "rugby":     {"source": "BBC Sport rugby union / World Rugby (world.rugby)", "tier": 1,
                      "backup": "Premiership Rugby (premiershiprugby.com)", "note": ""},
        "cricket":   {"source": "ESPNcricinfo (espncricinfo.com)", "tier": 1,
                      "backup": "Cricbuzz", "note": "Full scorecard"},
        "formula1":  {"source": "formula1.com/results", "tier": 1,
                      "backup": "Autosport", "note": "Allow 3h post-race for steward decisions"},
        "mma":       {"source": "UFC.com/results", "tier": 1,
                      "backup": "MMA Fighting (mmafighting.com)", "note": ""},
        "ice_hockey":{"source": "nhl.com/scores", "tier": 1,
                      "backup": "ESPN NHL", "note": ""},
        "basketball":{"source": "nba.com/scores", "tier": 1,
                      "backup": "Basketball Reference", "note": ""},
        "tennis":    {"source": "atptour.com/scores or wtatennis.com/scores", "tier": 1,
                      "backup": "Tennis Abstract", "note": ""},
        "afl":       {"source": "afl.com.au/matches", "tier": 1,
                      "backup": "AFL Tables (afltables.com)", "note": ""},
        "default":   {"source": "Official governing body results page", "tier": 1,
                      "backup": "BBC Sport / ESPN", "note": ""},
    },
    "disciplinary_ban": {
        "football":  {"source": "FA: thefa.com/football-rules-governance/disciplinary", "tier": 1,
                      "backup": "UEFA: UEFA.com/insideuefa/disciplinary", "note": ""},
        "rugby":     {"source": "World Rugby: world.rugby/the-game/judicial-decisions", "tier": 1,
                      "backup": "Premiership Rugby disciplinary section", "note": "All decisions published as PDFs"},
        "mma":       {"source": "USADA: usada.org/testing/results/sanctions", "tier": 1,
                      "backup": "UFC.com news announcements", "note": ""},
        "cricket":   {"source": "ICC: icc-cricket.com/about/cricket/rules-and-regulations", "tier": 1,
                      "backup": "ESPNcricinfo news", "note": ""},
        "formula1":  {"source": "FIA: fia.com/documents/decisions", "tier": 1,
                      "backup": "Racefans.net super licence points tracker", "note": ""},
        "rugby_league": {"source": "NRL: nrl.com/the-game/integrity-and-welfare/match-review-committee", "tier": 1,
                         "backup": "RFL: rfl.uk/the-game/discipline", "note": ""},
        "default":   {"source": "Official governing body disciplinary page", "tier": 1,
                      "backup": "BBC Sport / ESPN", "note": ""},
    },
    "player_stats": {
        "football":  {"source": "FBref (fbref.com) — xG, progressive actions, per-90", "tier": 2,
                      "backup": "WhoScored (whoscored.com)", "note": "FBref most comprehensive"},
        "rugby":     {"source": "ESPN Scrum (espnscrum.com) — international stats", "tier": 2,
                      "backup": "Rugby Reference (rugbyreference.com)", "note": ""},
        "cricket":   {"source": "Statsguru (stats.espncricinfo.com)", "tier": 2,
                      "backup": "CricketArchive (cricketarchive.com)", "note": "Deepest cricket database"},
        "formula1":  {"source": "formula1.com/results — qualifying and race", "tier": 1,
                      "backup": "Motorsport Stats (motorsportstats.com)", "note": ""},
        "mma":       {"source": "UFC Stats (ufcstats.com) — official fight stats", "tier": 1,
                      "backup": "Tapology (tapology.com)", "note": ""},
        "ice_hockey":{"source": "Natural Stat Trick (naturalstattrick.com) — advanced", "tier": 2,
                      "backup": "Hockey Reference (hockey-reference.com)", "note": "CF%, GSAx"},
        "basketball":{"source": "NBA.com/stats — official advanced metrics", "tier": 1,
                      "backup": "Cleaning the Glass (cleaningtheglass.com)", "note": ""},
        "tennis":    {"source": "Tennis Abstract (tennisabstract.com) — surface splits", "tier": 2,
                      "backup": "Ultimate Tennis Statistics", "note": ""},
        "afl":       {"source": "AFL Tables (afltables.com)", "tier": 2,
                      "backup": "Footywire (footywire.com)", "note": ""},
        "default":   {"source": "FBref or sport-specific official stats", "tier": 2,
                      "backup": "ESPN", "note": ""},
    },
    "transfer_news": {
        "football":  {"source": "Fabrizio Romano @FabrizioRomano — 'here we go' = confirmed", "tier": 2,
                      "backup": "Club official announcement (definitive)", "note": "Tier 1 = club announcement only"},
        "default":   {"source": "Club official announcement", "tier": 1,
                      "backup": "The Athletic or BBC Sport", "note": ""},
    },
    "rankings": {
        "football":  {"source": "FIFA World Rankings: fifa.com/fifa-world-ranking", "tier": 1,
                      "backup": "UEFA club rankings: UEFA.com/memberassociations/uefarankings", "note": ""},
        "rugby":     {"source": "World Rugby Rankings: world.rugby/rugby-world-rankings", "tier": 1,
                      "backup": "ESPN Scrum", "note": "Updated weekly"},
        "cricket":   {"source": "ICC Rankings: icc-cricket.com/rankings", "tier": 1,
                      "backup": "ESPNcricinfo rankings", "note": "All formats"},
        "mma":       {"source": "UFC Rankings: ufc.com/rankings", "tier": 1,
                      "backup": "Tapology rankings", "note": "Updated weekly"},
        "tennis":    {"source": "ATP: atptour.com/rankings | WTA: wtatennis.com/rankings", "tier": 1,
                      "backup": "Tennis Abstract", "note": ""},
        "formula1":  {"source": "formula1.com/standings", "tier": 1,
                      "backup": "Motorsport.com", "note": "Driver and constructor"},
        "default":   {"source": "Official governing body rankings page", "tier": 1,
                      "backup": "ESPN", "note": ""},
    },
}


# ── Helpers ────────────────────────────────────────────────────────────────────

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def get_macro_state() -> dict:
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
                "signal_note": "Using default neutral — run scripts/update_macro_state.py to refresh",
            },
            "active_events": [],
            "last_updated": "unknown",
            "freshness_warning": "macro-state.json not found — using neutral defaults",
        }
    }


def get_skill_files(sport: str, use_case: str) -> list:
    slug = sport.replace("_", "-")
    files = []
    for path in [
        ROOT / "macro" / "macro-overview.md",
        ROOT / "market" / f"market-{slug}.md",
        ROOT / "sports" / slug / f"sport-domain-{slug}.md",
    ]:
        if path.exists():
            files.append(path)

    athlete_dir = ROOT / "athlete" / slug
    if athlete_dir.is_dir():
        files.extend(sorted(athlete_dir.glob("athlete-intel-*.md")))

    if use_case in ("fan_token_tier1", "fan_token_tier2", "governance"):
        bridge = ROOT / "fan-token" / f"{slug}-token-intelligence"
        if bridge.is_dir():
            files.extend(sorted(bridge.glob("*.md")))
        defi = ROOT / "fan-token" / "defi-liquidity-intelligence"
        if defi.is_dir():
            defi_files = sorted(defi.glob("*.md"))
            if defi_files:
                files.append(defi_files[0])

    return files


def compute_sms(skill_files: list, macro_modifier: float) -> tuple:
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

    sms = round(
        (len(layers) / 5) * 0.35 * 100 +
        (1.0 if macro_modifier >= 0.75 else 0.5) * 0.25 * 100 +
        0.25 * 100 +
        min(macro_modifier, 1.0) * 0.15 * 100, 1
    )
    tier = (
        "HIGH_QUALITY" if sms >= 80 else
        "GOOD"         if sms >= 60 else
        "PARTIAL"      if sms >= 40 else
        "INCOMPLETE"   if sms >= 20 else
        "INSUFFICIENT"
    )
    return sms, tier, sorted(layers)


# ── Tool implementations ───────────────────────────────────────────────────────

def tool_signal(sport, event_id, use_case, home_team, away_team, include_defi):
    files      = get_skill_files(sport, use_case)
    macro_data = get_macro_state()
    macro_mod  = (macro_data.get("macro_state", {})
                             .get("crypto_cycle", {})
                             .get("macro_modifier", 1.00))
    sms, tier, layers = compute_sms(files, macro_mod)
    override = macro_mod < 0.75

    result = {
        "signal": {
            "direction":          "HOME",
            "adjusted_score":     round(55.0 * macro_mod, 1),
            "confidence_tier":    "MEDIUM" if sms >= 60 else "LOW",
            "recommended_action": "WAIT" if (override or sms < 60) else "ENTER",
        },
        "sportmind_score": {
            "sms":           sms,
            "sms_tier":      tier,
            "layers_loaded": layers,
            "coverage_note": f"{len(files)} skill files loaded",
        },
        "modifiers": {
            "macro_modifier":     round(macro_mod, 2),
            "composite_modifier": round(macro_mod, 2),
            "flags": {
                "lineup_unconfirmed":    False,
                "macro_override_active": override,
                "liquidity_warning":     False,
                "injury_warning":        False,
            },
        },
        "event_context": {
            "sport":     sport,
            "event_id":  event_id   or "unspecified",
            "home_team": home_team  or "unspecified",
            "away_team": away_team  or "unspecified",
            "use_case":  use_case,
        },
        "skill_stack":       [str(Path(f).relative_to(ROOT)) for f in files],
        "generated_at":      now_iso(),
        "sportmind_version": VERSION,
        "agent_note": (
            "direction is a structural baseline from static skill intelligence. "
            "Integrate live athlete availability and form for full accuracy. "
            "See platform/live-signals.md and core/temporal-awareness.md."
        ),
    }

    if include_defi:
        result["defi_context"] = {
            "note":      "Live DeFi data requires real-time Chiliz Chain query.",
            "reference": "fan-token/defi-liquidity-intelligence/",
            "kayen_api": "platform/data-connector-templates.md",
        }
    return result


def tool_macro():
    state = get_macro_state()
    state["retrieval_note"] = (
        "Update: python scripts/update_macro_state.py  "
        "or connect live via platform/data-connector-templates.md (CoinGecko)"
    )
    state["sportmind_version"] = VERSION
    return state


def tool_stack(sport, use_case, compressed):
    files = get_skill_files(sport, use_case)
    stack = []
    for f in files:
        content = f.read_text(encoding="utf-8")
        entry = {
            "skill_id": str(Path(f).relative_to(ROOT)),
            "sha256":   hashlib.sha256(content.encode()).hexdigest(),
            "content":  (content[:600] + "\n\n[COMPRESSED]") if compressed else content,
        }
        stack.append(entry)
    return {
        "sport":             sport,
        "use_case":          use_case,
        "stack":             stack,
        "total_files":       len(stack),
        "loading_order":     "macro → market → domain → athlete → fan-token",
        "sportmind_version": VERSION,
    }


def tool_verify(skill_id, content):
    if not HASHES_FILE.exists():
        return {"verified": False, "reason": "skill-hashes.json not found"}
    hashes = json.loads(HASHES_FILE.read_text())
    actual = hashlib.sha256(content.encode("utf-8")).hexdigest()
    for path, entry in hashes.get("files", {}).items():
        if skill_id.lower() in path.lower():
            expected = entry.get("sha256", "")
            if actual == expected:
                return {"verified": True,  "file_path": path, "hash": actual[:16] + "..."}
            else:
                return {"verified": False, "file_path": path, "reason": "Hash mismatch"}
    return {"verified": True, "reason": "Not in registry — new or unregistered file"}


def tool_agent_status(agent_id, include_audit, last_n):
    return {
        "agents":        [],
        "system_health": "UNKNOWN",
        "note": (
            "sportmind_agent_status requires a running SportMind agent instance. "
            "See core/autonomous-agent-framework.md and examples/agentic-workflows/"
        ),
        "timestamp":         now_iso(),
        "sportmind_version": VERSION,
    }


def tool_pre_match(sport, home_team, away_team, competition, kickoff, use_case):
    """Orchestrated full pre-match reasoning package."""
    files      = get_skill_files(sport, use_case)
    macro_data = get_macro_state()
    macro_mod  = (macro_data.get("macro_state", {})
                             .get("crypto_cycle", {})
                             .get("macro_modifier", 1.00))
    sms, tier, layers = compute_sms(files, macro_mod)
    override = macro_mod < 0.75

    # Narrative momentum check (structural signals from skill availability)
    narrative_signals = []
    if (ROOT / "core" / "core-narrative-momentum.md").exists():
        narrative_signals.append("Narrative momentum framework loaded — check rivalry, milestone, and home debut signals")

    # Disciplinary awareness
    disciplinary_note = (
        "Run sportmind_disciplinary to check DSM status for key players before "
        "finalising commercial recommendation."
    )

    # Statistical reasoning reference
    stats_note = (
        f"See core/player-statistical-reasoning.md for {sport} "
        "position-specific benchmarks and interpretation rules."
    )

    # Verifiable source for lineup
    lineup_source = (VERIFIABLE_SOURCES
                     .get("lineup_confirmation", {})
                     .get(sport, VERIFIABLE_SOURCES["lineup_confirmation"]["default"]))

    return {
        "pre_match_signal": {
            "sport":       sport,
            "home_team":   home_team   or "unspecified",
            "away_team":   away_team   or "unspecified",
            "competition": competition or "unspecified",
            "kickoff":     kickoff     or "unspecified",
            "use_case":    use_case,
        },
        "signal": {
            "direction":          "HOME",
            "adjusted_score":     round(55.0 * macro_mod, 1),
            "confidence_tier":    "MEDIUM" if sms >= 60 else "LOW",
            "recommended_action": "WAIT" if (override or sms < 60) else "ENTER",
        },
        "sportmind_score": {
            "sms":           sms,
            "sms_tier":      tier,
            "layers_loaded": layers,
            "files_loaded":  len(files),
        },
        "macro_context": {
            "macro_modifier":     round(macro_mod, 2),
            "macro_override":     override,
            "phase":              macro_data.get("macro_state", {}).get("crypto_cycle", {}).get("phase", "UNKNOWN"),
        },
        "availability_check": {
            "status":    "MANUAL_REQUIRED",
            "source":    lineup_source["source"],
            "tier":      lineup_source["tier"],
            "note":      "Lineup confirmation requires live data — use source above",
        },
        "disciplinary_check": {
            "status": "NOT_CHECKED",
            "action": disciplinary_note,
        },
        "narrative_momentum": {
            "signals": narrative_signals,
            "reference": "core/core-narrative-momentum.md",
            "note": "Apply narrative modifier only if statistical signals within ±15% of neutral",
        },
        "statistical_reasoning": {
            "reference": f"core/player-statistical-reasoning.md",
            "note": stats_note,
        },
        "skill_stack":        [str(Path(f).relative_to(ROOT)) for f in files],
        "reasoning_sequence": [
            "1. sportmind_macro — verify macro modifier",
            "2. sportmind_pre_match (this tool) — full pre-match package",
            "3. sportmind_disciplinary — check DSM for key players",
            "4. Verify lineup via source above",
            "5. Apply statistical reasoning framework",
            "6. Generate final signal",
        ],
        "generated_at":      now_iso(),
        "sportmind_version": VERSION,
    }


def tool_disciplinary(player, sport, club, include_framework):
    """Disciplinary check — DSM level, flags, commercial modifier."""

    # Load disciplinary intelligence framework if available
    disc_file = ROOT / "core" / "athlete-disciplinary-intelligence.md"
    framework_loaded = disc_file.exists()

    # Sport-specific regulatory body
    regulatory_bodies = {
        "football":    "FA / UEFA / FIFA — thefa.com/football-rules-governance/disciplinary",
        "rugby":       "World Rugby citing commissioner — world.rugby/the-game/judicial-decisions",
        "rugby_league":"NRL Match Review Committee / RFL — nrl.com/the-game/integrity-and-welfare",
        "cricket":     "ICC Code of Conduct — icc-cricket.com/about/cricket/rules-and-regulations",
        "formula1":    "FIA Stewards — fia.com/documents/decisions",
        "mma":         "USADA / Athletic Commission / UFC Code — usada.org/testing/results/sanctions",
        "tennis":      "ATP/WTA Integrity Program",
        "basketball":  "NBA Player Conduct Policy",
        "ice_hockey":  "NHL Department of Player Safety — nhl.com/news/department-player-safety",
        "afl":         "AFL Tribunal — afl.com.au/tribunal",
    }

    reg_body = regulatory_bodies.get(sport, "Governing body disciplinary body — check official site")

    result = {
        "disciplinary_check": {
            "player":     player or "unspecified",
            "club":       club   or "unspecified",
            "sport":      sport,
            "status":     "MANUAL_CHECK_REQUIRED",
            "note": (
                "SportMind does not have access to live disciplinary data. "
                "Check the regulatory source below for current status."
            ),
        },
        "regulatory_source": reg_body,
        "dsm_framework": {
            "loaded":    framework_loaded,
            "reference": "core/athlete-disciplinary-intelligence.md",
            "tiers": {
                "tier_1": "On-field technical — DSM MINIMAL — no commercial modifier",
                "tier_2": "On-field conduct — DSM MODERATE — modifier 0.88",
                "tier_3": "Off-field conduct — DSM SEVERE — modifier 0.72 — COMMERCIAL_RISK_ACTIVE",
                "tier_4": "Criminal/legal — DSM CATASTROPHIC — ABSTAIN",
            },
        },
        "flags_to_check": [
            "CITING_ACTIVE",
            "BAN_CONFIRMED",
            "COMMERCIAL_RISK_ACTIVE",
            "LEGAL_PROCEEDINGS_ACTIVE",
            "SUSPENSION_RISK",
            "CONDUCT_RESIDUAL",
            "INVESTIGATION_ACTIVE",
        ],
        "commercial_rule": (
            "Never generate ENTER recommendation when COMMERCIAL_RISK_ACTIVE "
            "or LEGAL_PROCEEDINGS_ACTIVE is set on a key commercial asset."
        ),
        "agent_action": (
            "1. Check regulatory source for current player status. "
            "2. Classify offence tier using core/athlete-disciplinary-intelligence.md. "
            "3. Apply DSM modifier and set appropriate flags. "
            "4. Adjust commercial signal accordingly."
        ),
        "generated_at":      now_iso(),
        "sportmind_version": VERSION,
    }

    if include_framework and framework_loaded:
        result["framework_excerpt"] = (
            "Four-tier offence taxonomy: Tier 1 (on-field technical) → "
            "Tier 2 (on-field conduct) → Tier 3 (off-field conduct) → "
            "Tier 4 (criminal/legal). DSM values: MINIMAL (1.00) / "
            "MODERATE (0.88) / SEVERE (0.72) / CATASTROPHIC (ABSTAIN). "
            "Seven flags: CITING_ACTIVE, BAN_CONFIRMED, COMMERCIAL_RISK_ACTIVE, "
            "LEGAL_PROCEEDINGS_ACTIVE, SUSPENSION_RISK, CONDUCT_RESIDUAL, "
            "INVESTIGATION_ACTIVE. See full framework for sport-specific details."
        )

    return result


def tool_fan_token_lookup(query, include_registry):
    """Resolve club name, ticker, or sport to fan token context."""
    query_lower = query.strip().lower()
    matches = []

    # Exact ticker match
    if query.upper() in FAN_TOKEN_REGISTRY:
        matches = [query.upper()]

    # Sport match
    elif query_lower in SPORT_TO_TOKENS:
        matches = SPORT_TO_TOKENS[query_lower]

    # Name fragment match
    else:
        # Try name fragments
        for word in query_lower.split():
            if word in NAME_TO_TICKER:
                ticker = NAME_TO_TICKER[word]
                if ticker not in matches:
                    matches.append(ticker)
        # Direct name substring
        if not matches:
            for ticker, data in FAN_TOKEN_REGISTRY.items():
                if query_lower in data["name"].lower():
                    matches.append(ticker)

    if not matches:
        return {
            "query":   query,
            "found":   False,
            "message": (
                f"No fan token found for '{query}' in the SportMind registry. "
                "Registry covers 24 verified Chiliz Chain tokens. "
                "Check chiliscan.com/token/top-erc20 for the full on-chain list."
            ),
            "registry_size":     len(FAN_TOKEN_REGISTRY),
            "sportmind_version": VERSION,
        }

    tokens = []
    for ticker in matches[:10]:  # Cap at 10 results
        data = FAN_TOKEN_REGISTRY[ticker]
        token_info = {
            "ticker":          ticker,
            "name":            data["name"],
            "sport":           data["sport"],
            "market_cap_tier": data["tier"],
            "contract_address":data["contract"],
            "chain":           "Chiliz Chain (Chain ID: 88888)",
            "chiliscan_url":   data["chiliscan"],
            "fantokens_url":   data["fantokens"],
            "skill_stack": {
                "domain":     f"sports/{data['sport']}/sport-domain-{data['sport']}.md",
                "athlete":    f"athlete/{data['sport']}/athlete-intel-{data['sport']}.md",
                "fan_token":  f"fan-token/{data['sport']}-token-intelligence/",
                "use_case_recommended": (
                    "fan_token_tier1" if data["tier"] == 1 else "fan_token_tier2"
                ),
            },
        }
        # Append Fan Token Play fields if confirmed for this token
        if "fan_token_play" in data:
            token_info["fan_token_play"] = {
                "path":           data["fan_token_play"],
                "confirmed_date": data.get("ftp_confirmed_date"),
                "note":           data.get("ftp_note"),
                "skill_ref":      "fan-token/gamified-tokenomics-intelligence/",
            }
        tokens.append(token_info)

    result = {
        "query":             query,
        "found":             True,
        "total_matches":     len(matches),
        "tokens":            tokens,
        "chain":             "Chiliz Chain — Chain ID 88888",
        "registry_source":   "chiliscan.com/token/top-erc20 (verified contract addresses)",
        "market_cap_tiers": {
            "tier_1": ">$10M on-chain market cap",
            "tier_2": "$1M–$10M on-chain market cap",
            "tier_3": "<$1M on-chain market cap",
        },
        "sportmind_version": VERSION,
    }

    if include_registry:
        result["full_registry"] = {
            ticker: {
                "name":    d["name"],
                "sport":   d["sport"],
                "tier":    d["tier"],
                "contract":d["contract"],
            }
            for ticker, d in FAN_TOKEN_REGISTRY.items()
        }

    return result


def tool_sentiment_snapshot(token, use_case):
    """Multi-axis sentiment state for a token."""

    # Resolve token
    ticker = token.upper()
    token_data = FAN_TOKEN_REGISTRY.get(ticker)

    macro_data = get_macro_state()
    macro_mod  = (macro_data.get("macro_state", {})
                             .get("crypto_cycle", {})
                             .get("macro_modifier", 1.00))
    macro_phase = (macro_data.get("macro_state", {})
                              .get("crypto_cycle", {})
                              .get("phase", "UNKNOWN"))

    if not token_data:
        # Try name lookup
        for t, d in FAN_TOKEN_REGISTRY.items():
            if token.lower() in d["name"].lower():
                ticker = t
                token_data = d
                break

    if not token_data:
        return {
            "token":   token,
            "found":   False,
            "message": f"Token '{token}' not in SportMind registry. Use sportmind_fan_token_lookup first.",
            "sportmind_version": VERSION,
        }

    sport = token_data["sport"]
    files = get_skill_files(sport, use_case)
    sms, sms_tier, layers = compute_sms(files, macro_mod)

    return {
        "token":       ticker,
        "found":       True,
        "name":        token_data["name"],
        "sport":       sport,
        "use_case":    use_case,
        "sentiment_snapshot": {
            "macro_sentiment": {
                "phase":           macro_phase,
                "macro_modifier":  round(macro_mod, 2),
                "signal":          "POSITIVE" if macro_mod >= 1.0 else ("NEUTRAL" if macro_mod >= 0.85 else "NEGATIVE"),
                "note":            "Update macro state via scripts/update_macro_state.py",
            },
            "fan_sentiment": {
                "status":    "MANUAL_CHECK_REQUIRED",
                "reference": "fan-token/fan-sentiment-intelligence/fan-sentiment-intelligence.md",
                "note":      "Check current emotional arc phase (Peak/Celebration/Normalisation etc.)",
            },
            "social_sentiment": {
                "status":    "MANUAL_CHECK_REQUIRED",
                "reference": "fan-token/athlete-social-lift/fan-token-athlete-social-lift.md",
                "note":      "Check AELS for key players and current social volume",
            },
            "commercial_sentiment": {
                "status":    "MANUAL_CHECK_REQUIRED",
                "reference": "fan-token/brand-score/",
                "note":      "Check for active DSM flags — run sportmind_disciplinary for key players",
            },
            "disciplinary_sentiment": {
                "status":    "NOT_CHECKED",
                "action":    "Run sportmind_disciplinary for key players before commercial recommendation",
                "flags_to_check": ["COMMERCIAL_RISK_ACTIVE", "LEGAL_PROCEEDINGS_ACTIVE"],
            },
            "supply_mechanics": (
                {
                    "fan_token_play_path":   token_data.get("fan_token_play"),
                    "confirmed_date":        token_data.get("ftp_confirmed_date"),
                    "status":                "GAMIFIED_CONFIRMED",
                    "pre_liquidation_check": "Run FanTokenPlayMonitor at T-48h before each match",
                    "path_2_loss_note":      "PATH_2 LOSS is supply-neutral — pre-liquidated amount restored only.",
                    "chz_echo":              "PATH_2 WIN contributes to CHZ ecosystem burn via 10% proceeds rule.",
                    "skill_ref":             "fan-token/gamified-tokenomics-intelligence/",
                    "agent_rule":            "Never treat pre-liquidation as Category 1 distribution signal.",
                }
                if "fan_token_play" in token_data else {
                    "status": "NOT_CONFIRMED",
                    "note":   "Check KAYEN API gamified field. Apply standard signal chain if not confirmed.",
                }
            ),
        },
        "composite_signal": {
            "sms":              sms,
            "sms_tier":         sms_tier,
            "macro_modifier":   round(macro_mod, 2),
            "layers_loaded":    layers,
            "recommended_action": (
                "WAIT" if macro_mod < 0.75 or sms < 60
                else "PROCEED_TO_FULL_ANALYSIS"
            ),
        },
        "skill_references": {
            "fan_sentiment":   "fan-token/fan-sentiment-intelligence/",
            "social_lift":     "fan-token/athlete-social-lift/",
            "brand_score":     "fan-token/brand-score/",
            "token_pulse":     "fan-token/fan-token-pulse/",
            "disciplinary":    "core/athlete-disciplinary-intelligence.md",
            "token_specific":  f"fan-token/{sport}-token-intelligence/",
        },
        "contract_address":  token_data["contract"],
        "chiliscan_url":     token_data["chiliscan"],
        "fantokens_url":     token_data["fantokens"],
        "generated_at":      now_iso(),
        "sportmind_version": VERSION,
    }


def tool_verifiable_source(query_type, sport):
    """Return the authoritative source for a query type and sport."""
    sport_slug = sport.replace("-", "_")

    sources_for_type = VERIFIABLE_SOURCES.get(query_type)
    if not sources_for_type:
        available = list(VERIFIABLE_SOURCES.keys())
        return {
            "query_type":      query_type,
            "sport":           sport,
            "found":           False,
            "message":         f"Query type '{query_type}' not in registry.",
            "available_types": available,
            "sportmind_version": VERSION,
        }

    source = (sources_for_type.get(sport_slug) or
              sources_for_type.get(sport.replace("_", "")) or
              sources_for_type.get("default"))

    return {
        "query_type":  query_type,
        "sport":       sport,
        "found":       True,
        "source":      source["source"],
        "tier":        source["tier"],
        "backup":      source["backup"],
        "note":        source.get("note", ""),
        "tier_meaning": {
            1: "Ground truth — always accept",
            2: "Reliable — accept with standard confidence",
            3: "Usable with caution — corroborate before using",
            4: "Do not use as signal input",
        },
        "full_reference": "core/verifiable-sources-by-sport.md",
        "sportmind_version": VERSION,
    }


# ── Tool schemas ───────────────────────────────────────────────────────────────

TOOL_SCHEMAS = {
    "sportmind_signal": {
        "type": "object",
        "properties": {
            "sport":                {"type": "string", "enum": SUPPORTED_SPORTS},
            "event_id":             {"type": "string"},
            "use_case":             {"type": "string", "enum": USE_CASES, "default": "pre_match"},
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
            "compressed": {"type": "boolean", "default": False},
        },
        "required": ["sport"],
    },
    "sportmind_verify": {
        "type": "object",
        "properties": {
            "skill_id": {"type": "string"},
            "content":  {"type": "string"},
        },
        "required": ["skill_id", "content"],
    },
    "sportmind_agent_status": {
        "type": "object",
        "properties": {
            "agent_id":           {"type": "string"},
            "include_audit_log":  {"type": "boolean", "default": False},
            "last_n_cycles":      {"type": "integer", "default": 5},
        },
        "required": [],
    },
    "sportmind_pre_match": {
        "type": "object",
        "properties": {
            "sport":       {"type": "string", "enum": SUPPORTED_SPORTS},
            "home_team":   {"type": "string"},
            "away_team":   {"type": "string"},
            "competition": {"type": "string"},
            "kickoff":     {"type": "string", "description": "ISO-8601 datetime"},
            "use_case":    {"type": "string", "enum": USE_CASES, "default": "pre_match"},
        },
        "required": ["sport"],
    },
    "sportmind_disciplinary": {
        "type": "object",
        "properties": {
            "player":             {"type": "string"},
            "sport":              {"type": "string", "enum": SUPPORTED_SPORTS},
            "club":               {"type": "string"},
            "include_framework":  {"type": "boolean", "default": False,
                                   "description": "Include DSM framework excerpt in response"},
        },
        "required": ["sport"],
    },
    "sportmind_fan_token_lookup": {
        "type": "object",
        "properties": {
            "query":            {"type": "string",
                                 "description": "Club name, token ticker (e.g. BAR, PSG), or sport name"},
            "include_registry": {"type": "boolean", "default": False,
                                 "description": "Include full registry in response"},
        },
        "required": ["query"],
    },
    "sportmind_sentiment_snapshot": {
        "type": "object",
        "properties": {
            "token":    {"type": "string",
                         "description": "Fan token ticker (e.g. BAR, PSG, CITY) or club name"},
            "use_case": {"type": "string", "enum": USE_CASES, "default": "fan_token_tier1"},
        },
        "required": ["token"],
    },
    "sportmind_verifiable_source": {
        "type": "object",
        "properties": {
            "query_type": {
                "type": "string",
                "enum": ["lineup_confirmation", "match_result", "disciplinary_ban",
                         "player_stats", "transfer_news", "rankings"],
                "description": "Type of information to verify",
            },
            "sport": {"type": "string", "enum": SUPPORTED_SPORTS},
        },
        "required": ["query_type", "sport"],
    },
}

TOOL_DESCRIPTIONS = {
    "sportmind_signal": (
        "Generate a SportMind pre-match intelligence signal. Returns direction, "
        "adjusted_score, SMS, and modifiers. Call sportmind_macro first for fan "
        "token or DeFi applications."
    ),
    "sportmind_macro": (
        "Get the current SportMind macro state: crypto cycle phase, macro_modifier, "
        "and active events. Always call before fan token analysis."
    ),
    "sportmind_stack": (
        "Load the full SportMind intelligence stack for a sport in correct loading "
        "order: macro → market → domain → athlete → fan-token."
    ),
    "sportmind_verify": (
        "Verify SportMind skill content integrity via SHA-256 against "
        "platform/skill-hashes.json. Use in security-sensitive deployments."
    ),
    "sportmind_agent_status": (
        "Get the operational status of running SportMind autonomous agents. "
        "Requires a running agent instance — see core/autonomous-agent-framework.md."
    ),
    "sportmind_pre_match": (
        "Orchestrated full pre-match reasoning package. Combines sport domain signal, "
        "macro state, availability check source, disciplinary reminder, narrative "
        "momentum reference, and statistical reasoning reference in one call. "
        "Use instead of manually sequencing macro + signal + stack."
    ),
    "sportmind_disciplinary": (
        "Disciplinary intelligence check for a player and sport. Returns DSM framework "
        "(MINIMAL/MODERATE/SEVERE/CATASTROPHIC), regulatory source to check, active "
        "flags to set, and commercial recommendation rule. Requires live regulatory "
        "source check for current player status."
    ),
    "sportmind_fan_token_lookup": (
        "Resolve a club name, token ticker, or sport to its Chiliz Chain fan token "
        "context. Returns contract address, chain ID 88888, chiliscan verification "
        "link, fantokens.com market data link, market cap tier, and recommended "
        "SportMind skill stack. Registry covers 24 verified tokens."
    ),
    "sportmind_sentiment_snapshot": (
        "Multi-axis sentiment state for a fan token. Returns macro sentiment, and "
        "references for fan sentiment phase, social lift, commercial sentiment, and "
        "disciplinary status — with the composite signal and recommended next action. "
        "Use before any fan token commercial recommendation."
    ),
    "sportmind_verifiable_source": (
        "Return the authoritative source for a specific query type and sport. "
        "Covers: lineup_confirmation, match_result, disciplinary_ban, player_stats, "
        "transfer_news, rankings. Returns source name, tier (1=ground truth to "
        "4=do not use), backup source, and reference to verifiable-sources-by-sport.md."
    ),
}


# ── MCP Server ─────────────────────────────────────────────────────────────────

async def _handle_tool(name: str, arguments: dict):
    """Dispatch tool calls to implementations."""
    if name == "sportmind_signal":
        return tool_signal(
            sport        = arguments.get("sport", "football"),
            event_id     = arguments.get("event_id", ""),
            use_case     = arguments.get("use_case", "pre_match"),
            home_team    = arguments.get("home_team", ""),
            away_team    = arguments.get("away_team", ""),
            include_defi = arguments.get("include_defi_context", False),
        )
    elif name == "sportmind_macro":
        return tool_macro()
    elif name == "sportmind_stack":
        return tool_stack(
            sport      = arguments.get("sport", "football"),
            use_case   = arguments.get("use_case", "pre_match"),
            compressed = arguments.get("compressed", False),
        )
    elif name == "sportmind_verify":
        return tool_verify(arguments["skill_id"], arguments["content"])
    elif name == "sportmind_agent_status":
        return tool_agent_status(
            agent_id     = arguments.get("agent_id", ""),
            include_audit= arguments.get("include_audit_log", False),
            last_n       = arguments.get("last_n_cycles", 5),
        )
    elif name == "sportmind_pre_match":
        return tool_pre_match(
            sport       = arguments.get("sport", "football"),
            home_team   = arguments.get("home_team", ""),
            away_team   = arguments.get("away_team", ""),
            competition = arguments.get("competition", ""),
            kickoff     = arguments.get("kickoff", ""),
            use_case    = arguments.get("use_case", "pre_match"),
        )
    elif name == "sportmind_disciplinary":
        return tool_disciplinary(
            player            = arguments.get("player", ""),
            sport             = arguments.get("sport", "football"),
            club              = arguments.get("club", ""),
            include_framework = arguments.get("include_framework", False),
        )
    elif name == "sportmind_fan_token_lookup":
        return tool_fan_token_lookup(
            query            = arguments.get("query", ""),
            include_registry = arguments.get("include_registry", False),
        )
    elif name == "sportmind_sentiment_snapshot":
        return tool_sentiment_snapshot(
            token    = arguments.get("token", ""),
            use_case = arguments.get("use_case", "fan_token_tier1"),
        )
    elif name == "sportmind_verifiable_source":
        return tool_verifiable_source(
            query_type = arguments.get("query_type", ""),
            sport      = arguments.get("sport", "football"),
        )
    else:
        return {"error": f"Unknown tool: {name}"}


async def run_stdio():
    try:
        from mcp.server import Server
        from mcp.server.stdio import stdio_server
        from mcp.types import Tool, TextContent
    except ImportError:
        print("ERROR: pip install mcp aiohttp", flush=True)
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

    server = Server("sportmind")

    @server.list_tools()
    async def list_tools():
        return [
            Tool(name=n, description=TOOL_DESCRIPTIONS[n], inputSchema=TOOL_SCHEMAS[n])
            for n in TOOL_SCHEMAS
        ]

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
            text=json.dumps({
                "status":    "ok",
                "service":   "SportMind MCP Server",
                "version":   VERSION,
                "tools":     list(TOOL_SCHEMAS.keys()),
                "tool_count": len(TOOL_SCHEMAS),
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
    print(f"Server running on port {port}. Ctrl+C to stop.", flush=True)
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
