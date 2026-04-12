---
name: api-connector-examples
description: >
  Working connector code for the five data sources most commonly needed
  by SportMind agents beyond the three templates in data-connector-templates.md.
  Covers: MMA/UFC fight data, cricket squad and toss, NBA injury report
  (Q/D/O designations), NHL morning skate lineup, and The Odds API for
  prediction market divergence detection. Each connector is self-contained,
  production-ready, and maps to specific SportMind skills and modifiers.
  See platform/api-providers.md for setup and key registration.
---

# API Connector Examples — SportMind

**Five working connectors for the data sources SportMind agents need most.**

These extend `platform/data-connector-templates.md` (football lineups,
KAYEN, CoinGecko) with the next five most-requested integrations.
Each maps directly to a SportMind skill — the connector gets the data,
SportMind tells the agent what it means.

---

## Connector 4 — MMA fight data (API-MMA / UFC Stats)

```python
# connectors/mma_fight_connector.py
"""
MMA fight data connector for SportMind agents.

Provides: fighter availability, weight cut history, fight card status,
          finishing rates for LQI and style matchup analysis.

API: API-MMA via RapidAPI (https://rapidapi.com/api-sports/api/api-mma)
Free tier: 100 requests/day — sufficient for pre-fight analysis.
Setup: Set RAPIDAPI_KEY environment variable.

SportMind skills this feeds:
  → core/injury-intelligence/injury-intel-mma.md (weight cut, camp signals)
  → core/lineup-quality-index.md (MMA fight card quality)
  → core/historical-intelligence-framework.md (MMA H2H section)
"""

import asyncio
import aiohttp
from datetime import datetime, timezone
from typing import Optional

# Set your API key: export RAPIDAPI_KEY="your_key_here"
RAPIDAPI_KEY  = ""  # Replace with your RapidAPI key
MMA_BASE      = "https://api-mma-v1.p.rapidapi.com"
MMA_HEADERS   = {
    "X-RapidAPI-Key":  RAPIDAPI_KEY,
    "X-RapidAPI-Host": "api-mma-v1.p.rapidapi.com",
}


class MMAFightConnector:
    """
    Fetches UFC/MMA fight card data and fighter stats.
    Maps to SportMind MMA intelligence layer.
    """

    def __init__(self, api_key: str = RAPIDAPI_KEY):
        self.headers = {
            "X-RapidAPI-Key":  api_key,
            "X-RapidAPI-Host": "api-mma-v1.p.rapidapi.com",
        }

    async def get_upcoming_events(self, next_n: int = 3) -> list[dict]:
        """Get next N upcoming MMA events."""
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{MMA_BASE}/events",
                headers=self.headers,
                params={"next": next_n}
            ) as resp:
                data = await resp.json()
                return data.get("response", [])

    async def get_event_fights(self, event_id: int) -> list[dict]:
        """Get all fights on a card with fighter details."""
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{MMA_BASE}/fights",
                headers=self.headers,
                params={"event": event_id}
            ) as resp:
                data = await resp.json()
                return data.get("response", [])

    async def get_fighter_stats(self, fighter_id: int) -> dict:
        """Get fighter career stats including finishing rates."""
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{MMA_BASE}/fighters/statistics",
                headers=self.headers,
                params={"id": fighter_id}
            ) as resp:
                data = await resp.json()
                results = data.get("response", [])
                return results[0] if results else {}

    def compute_sportmind_fight_signal(self, fight: dict) -> dict:
        """
        Convert raw fight data into SportMind-compatible signal.
        
        Maps to: core/lineup-quality-index.md MMA fight card section
        Main event = 0.60 weight; co-main = 0.25; prelims = 0.15 combined
        """
        fighters = fight.get("fighters", {})
        home = fighters.get("home", {})
        away = fighters.get("away", {})

        home_rank = home.get("ranking", 99) or 99
        away_rank = away.get("ranking", 99) or 99

        # LQI fight quality score
        if home_rank <= 10 and away_rank <= 10:
            fight_quality = 1.20
        elif home_rank <= 10 or away_rank <= 10:
            fight_quality = 1.05
        elif home_rank <= 25 and away_rank <= 25:
            fight_quality = 1.00
        else:
            fight_quality = 0.80

        # Late replacement flag
        is_replacement = (
            fight.get("status", "") == "replacement" or
            (fight.get("announcement_days_before", 30) or 30) < 14
        )
        if is_replacement:
            fight_quality *= 0.75
            replacement_flag = True
        else:
            replacement_flag = False

        return {
            "fight_id":          fight.get("id"),
            "home_fighter":      home.get("name"),
            "away_fighter":      away.get("name"),
            "home_rank":         home_rank,
            "away_rank":         away_rank,
            "fight_quality":     round(fight_quality, 3),
            "replacement_flag":  replacement_flag,
            "weight_class":      fight.get("weight", {}).get("name"),
            "is_title_fight":    fight.get("title_fight", False),
            "sportmind_note": (
                "Late replacement — apply ×0.75 quality reduction. "
                "Short camp reduces fight quality signal."
                if replacement_flag else
                "Standard fight card entry."
            ),
        }


# ── Usage example ─────────────────────────────────────────────────────────
async def mma_pre_event_brief(event_id: int):
    """Generate SportMind-compatible pre-event fight card brief."""
    connector = MMAFightConnector()
    fights    = await connector.get_event_fights(event_id)

    if not fights:
        return {"error": "No fights found for this event"}

    # Sort: main event first (highest fight number or title fight)
    main_event = next((f for f in fights if f.get("title_fight")), fights[0])
    other_fights = [f for f in fights if f.get("id") != main_event.get("id")]

    main_signal = connector.compute_sportmind_fight_signal(main_event)
    co_main_signal = (
        connector.compute_sportmind_fight_signal(other_fights[0])
        if other_fights else None
    )

    # Card LQI (main event 60%, co-main 25%, prelims 15%)
    card_lqi = main_signal["fight_quality"] * 0.60
    if co_main_signal:
        card_lqi += co_main_signal["fight_quality"] * 0.25
    card_lqi = min(1.20, card_lqi + 0.15)  # prelim baseline

    return {
        "event_id":     event_id,
        "card_lqi":     round(card_lqi, 3),
        "main_event":   main_signal,
        "co_main":      co_main_signal,
        "total_fights": len(fights),
        "skill_stack": [
            "core/injury-intelligence/injury-intel-mma.md",
            "core/lineup-quality-index.md (MMA fight card section)",
            "athlete/mma/athlete-intel-mma.md",
        ],
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


if __name__ == "__main__":
    # Replace with real event ID from get_upcoming_events()
    result = asyncio.run(mma_pre_event_brief(event_id=1234))
    import json
    print(json.dumps(result, indent=2))
```

---

## Connector 5 — Cricket squad and toss (CricketData.org)

```python
# connectors/cricket_squad_connector.py
"""
Cricket squad and match connector for SportMind agents.

Provides: Playing XI (at toss), pitch conditions, dew factor inputs,
          upcoming fixtures with format detection (T20/ODI/Test).

API: CricketData.org (https://cricketdata.org)
Free tier: 100 requests/day.
Setup: Get API key at cricketdata.org/register

SportMind skills this feeds:
  → athlete/cricket/athlete-intel-cricket.md
  → core/pre-match-squad-intelligence.md (cricket section)
  → sports/cricket/sport-domain-cricket.md (dew factor, format signals)
"""

import asyncio
import aiohttp
from datetime import datetime, timezone, timedelta

# Set your API key: export CRICKETDATA_KEY="your_key_here"
CRICKET_KEY  = ""  # Replace with your CricketData.org key
CRICKET_BASE = "https://api.cricapi.com/v1"


class CricketSquadConnector:

    def __init__(self, api_key: str = CRICKET_KEY):
        self.key = api_key

    async def get_upcoming_matches(self, days: int = 3) -> list[dict]:
        """Get upcoming cricket matches."""
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{CRICKET_BASE}/matches",
                params={"apikey": self.key, "offset": 0}
            ) as resp:
                data = await resp.json()
                matches = data.get("data", [])
                # Filter to upcoming only
                now = datetime.now(timezone.utc)
                cutoff = now + timedelta(days=days)
                upcoming = []
                for m in matches:
                    try:
                        dt = datetime.fromisoformat(
                            m.get("date", "").replace("Z", "+00:00")
                        )
                        if now < dt < cutoff:
                            upcoming.append(m)
                    except (ValueError, TypeError):
                        pass
                return upcoming

    async def get_match_squads(self, match_id: str) -> dict:
        """
        Get confirmed squads for a specific match.
        At toss (T-0): returns playing XI. Pre-toss: returns full squad.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{CRICKET_BASE}/match_info",
                params={"apikey": self.key, "id": match_id}
            ) as resp:
                data = await resp.json()
                return data.get("data", {})

    async def get_current_matches(self) -> list[dict]:
        """Get live matches — use after toss for confirmed XI."""
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{CRICKET_BASE}/currentMatches",
                params={"apikey": self.key, "offset": 0}
            ) as resp:
                data = await resp.json()
                return data.get("data", [])

    def detect_format(self, match: dict) -> str:
        """Detect match format from match type field."""
        match_type = match.get("matchType", "").lower()
        if "t20" in match_type or "twenty20" in match_type:
            return "T20"
        elif "odi" in match_type or "one day" in match_type:
            return "ODI"
        elif "test" in match_type or "first class" in match_type:
            return "TEST"
        else:
            return "UNKNOWN"

    def assess_dew_risk(self, venue_lat: float, venue_lon: float,
                        match_time_utc: str) -> dict:
        """
        Assess dew risk for evening matches.
        For full dew prediction: combine with Open-Meteo humidity data.
        This function returns the dew risk framework inputs.
        Maps to: sports/cricket/sport-domain-cricket.md dew factor section.
        """
        try:
            dt = datetime.fromisoformat(match_time_utc.replace("Z", "+00:00"))
            local_hour = (dt.hour + round(venue_lon / 15)) % 24
        except (ValueError, AttributeError):
            local_hour = 19  # Default evening

        # Evening matches in humid subcontinental conditions = high dew risk
        is_evening = 17 <= local_hour <= 22
        is_subcontinental = (6 <= venue_lat <= 37) and (60 <= venue_lon <= 100)

        if is_evening and is_subcontinental:
            dew_risk = "HIGH"
            batting_second_advantage = True
            spin_effectiveness_reduced = True
        elif is_evening:
            dew_risk = "MODERATE"
            batting_second_advantage = False
            spin_effectiveness_reduced = False
        else:
            dew_risk = "LOW"
            batting_second_advantage = False
            spin_effectiveness_reduced = False

        return {
            "dew_risk":                   dew_risk,
            "is_evening_match":           is_evening,
            "batting_second_advantage":   batting_second_advantage,
            "spin_effectiveness_reduced": spin_effectiveness_reduced,
            "local_match_hour":           local_hour,
            "note": (
                "Load Open-Meteo humidity at venue to confirm. "
                "sports/cricket/sport-domain-cricket.md dew factor threshold: 70%+ humidity."
                if dew_risk == "HIGH" else
                "Standard dew assessment — confirm with Open-Meteo humidity."
            ),
        }

    def build_squad_brief(self, match_data: dict) -> dict:
        """Build SportMind-compatible squad brief from match data."""
        teams = match_data.get("teamInfo", [])
        toss  = match_data.get("tossWinner", "")
        toss_choice = match_data.get("tossChoice", "")
        squad_1 = match_data.get("squad", {})
        score   = match_data.get("score", [])

        # Toss signal: key for cricket (especially T20, dew conditions)
        toss_signal = {
            "toss_winner":      toss,
            "toss_choice":      toss_choice,
            "toss_decided":     bool(toss),
            "sportmind_note": (
                f"{toss} chose to {toss_choice}. "
                "Toss is critical in dew-risk evening T20s. "
                "See dew_risk assessment."
            ) if toss else "Toss not yet decided — T-0 lineup pending."
        }

        return {
            "match_id":       match_data.get("id"),
            "teams":          [t.get("name") for t in teams],
            "format":         self.detect_format(match_data),
            "status":         match_data.get("status"),
            "toss_signal":    toss_signal,
            "playing_xi_available": bool(squad_1),
            "skill_stack": [
                "athlete/cricket/athlete-intel-cricket.md",
                "core/pre-match-squad-intelligence.md (cricket section)",
                "sports/cricket/sport-domain-cricket.md",
            ],
        }


# ── Usage example ─────────────────────────────────────────────────────────
async def cricket_pre_match_brief(match_id: str, venue_lat: float,
                                   venue_lon: float):
    """Full pre-match cricket brief including dew risk."""
    connector = CricketSquadConnector()
    match_data = await connector.get_match_squads(match_id)

    squad_brief = connector.build_squad_brief(match_data)

    match_time = match_data.get("date", datetime.now(timezone.utc).isoformat())
    dew = connector.assess_dew_risk(venue_lat, venue_lon, match_time)

    return {
        "squad_brief": squad_brief,
        "dew_assessment": dew,
        "combined_note": (
            "HIGH dew risk + evening T20. "
            "Team batting second has structural advantage. "
            "Spin bowling effectiveness reduced from over 15. "
            "Apply: sports/cricket/sport-domain-cricket.md DEW_FACTOR modifier."
            if dew["dew_risk"] == "HIGH" else
            "Standard cricket pre-match brief. No elevated dew risk detected."
        ),
    }


if __name__ == "__main__":
    # Mumbai evening T20 (lat 19.08, lon 72.88)
    result = asyncio.run(
        cricket_pre_match_brief("YOUR_MATCH_ID", venue_lat=19.08, venue_lon=72.88)
    )
    import json
    print(json.dumps(result, indent=2))
```

---

## Connector 6 — NBA injury report (Q/D/O designations)

```python
# connectors/nba_injury_connector.py
"""
NBA injury report connector for SportMind agents.

Parses official NBA injury designations (OUT/DOUBTFUL/QUESTIONABLE/
PROBABLE/GTD) and maps them to SportMind availability modifiers.

Sources:
  Primary: nba.com/players/injuries (official — no API key needed)
  Backup:  balldontlie.io API (free, 60 req/min)

SportMind skills this feeds:
  → core/pre-match-squad-intelligence.md (NBA Q/D/O/GTD decoder section)
  → core/lineup-quality-index.md (basketball star premium section)
  → athlete/nba/athlete-intel-nba.md
"""

import asyncio
import re
import aiohttp
from datetime import datetime, timezone
from typing import Optional

BALLDONTLIE_KEY = ""  # Free tier: no key needed for basic endpoints
NBA_INJURY_URL  = "https://www.nba.com/players/injuries"
BDL_BASE        = "https://api.balldontlie.io/v1"

# SportMind availability modifier mapping per NBA designation
# Source: core/pre-match-squad-intelligence.md NBA section
DESIGNATION_MODIFIERS = {
    "OUT":         {"availability_pct": 0,   "modifier": 0.00, "act_on": True},
    "DOUBTFUL":    {"availability_pct": 20,  "modifier": 0.75, "act_on": True},
    "QUESTIONABLE":{"availability_pct": 50,  "modifier": 0.92, "act_on": True},
    "PROBABLE":    {"availability_pct": 80,  "modifier": 1.00, "act_on": False},
    "GTD":         {"availability_pct": 50,  "modifier": 0.92, "act_on": True,
                    "note": "Check 90min before tip-off for final status"},
    "REST":        {"availability_pct": 0,   "modifier": 0.00, "act_on": True,
                    "note": "Load management — not injury. Commercial signal: reduced star engagement."},
}


class NBAInjuryConnector:

    async def fetch_injury_report_html(self) -> str:
        """Fetch the official NBA injury report page."""
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; SportMind/3.52)",
            "Accept": "text/html",
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(NBA_INJURY_URL, headers=headers) as resp:
                return await resp.text()

    def parse_injury_report(self, html: str) -> list[dict]:
        """
        Parse NBA injury report HTML into structured player status list.
        Returns list of {player, team, designation, reason}.
        """
        # Extract injury rows from the NBA injury report table
        # Pattern matches player name, team, designation in the report
        pattern = re.compile(
            r'<tr[^>]*>.*?'
            r'<td[^>]*>(.*?)</td>.*?'   # Player
            r'<td[^>]*>(.*?)</td>.*?'   # Team
            r'<td[^>]*>(.*?)</td>.*?'   # Designation
            r'<td[^>]*>(.*?)</td>.*?'   # Reason
            r'</tr>',
            re.DOTALL | re.IGNORECASE
        )
        results = []
        for m in pattern.finditer(html):
            player, team, designation, reason = [
                re.sub(r'<[^>]+>', '', g).strip()
                for g in m.groups()
            ]
            if player and designation:
                desig_upper = designation.upper()
                modifier_info = DESIGNATION_MODIFIERS.get(desig_upper, {})
                results.append({
                    "player":           player,
                    "team":             team,
                    "designation":      desig_upper,
                    "reason":           reason,
                    "availability_pct": modifier_info.get("availability_pct", 100),
                    "modifier":         modifier_info.get("modifier", 1.00),
                    "act_on":           modifier_info.get("act_on", False),
                    "note":             modifier_info.get("note", ""),
                })
        return results

    async def get_today_games(self) -> list[dict]:
        """Get today's NBA games via balldontlie API."""
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{BDL_BASE}/games",
                params={"dates[]": today},
                headers={"Authorization": BALLDONTLIE_KEY} if BALLDONTLIE_KEY else {}
            ) as resp:
                data = await resp.json()
                return data.get("data", [])

    def get_game_injury_relevance(self, injury_report: list[dict],
                                   home_team: str, away_team: str) -> dict:
        """
        Filter injury report to players relevant to a specific game.
        Returns injuries for home and away teams with SportMind modifiers.
        """
        home_injuries = [
            p for p in injury_report
            if home_team.lower() in p["team"].lower()
            and p["act_on"]
        ]
        away_injuries = [
            p for p in injury_report
            if away_team.lower() in p["team"].lower()
            and p["act_on"]
        ]

        # Compute team-level availability modifier
        def team_modifier(injuries: list) -> float:
            if not injuries:
                return 1.00
            # Star player absent = largest impact
            # Apply composite: each OUT player reduces by weighted amount
            out_players = [i for i in injuries if i["designation"] == "OUT"]
            gtd_players = [i for i in injuries if i["designation"] in ("GTD", "QUESTIONABLE")]
            modifier = 1.00
            for _ in out_players:
                modifier *= 0.82  # Each OUT: ×0.82 per absent player
            for _ in gtd_players:
                modifier *= 0.95  # Each GTD: ×0.95 uncertainty
            return round(max(0.55, modifier), 3)

        return {
            "game":             f"{home_team} vs {away_team}",
            "home_injuries":    home_injuries,
            "away_injuries":    away_injuries,
            "home_modifier":    team_modifier(home_injuries),
            "away_modifier":    team_modifier(away_injuries),
            "gtd_check_required": any(
                p["designation"] in ("GTD", "QUESTIONABLE")
                for p in home_injuries + away_injuries
            ),
            "gtd_check_time":   "90 minutes before tip-off",
            "skill_reference":  "core/pre-match-squad-intelligence.md — NBA section",
        }


# ── Usage example ─────────────────────────────────────────────────────────
async def nba_pre_game_brief(home_team: str, away_team: str) -> dict:
    """Generate SportMind NBA pre-game injury brief."""
    connector = NBAInjuryConnector()

    html    = await connector.fetch_injury_report_html()
    report  = connector.parse_injury_report(html)
    result  = connector.get_game_injury_relevance(report, home_team, away_team)

    return {
        "pre_game_brief":  result,
        "total_on_report": len(report),
        "generated_at":    datetime.now(timezone.utc).isoformat(),
        "next_check":      "90 min before tip-off for GTD updates",
    }


if __name__ == "__main__":
    result = asyncio.run(nba_pre_game_brief("Los Angeles Lakers", "Boston Celtics"))
    import json
    print(json.dumps(result, indent=2))
```

---

## Connector 7 — NHL morning skate lineup (Daily Faceoff + NHL API)

```python
# connectors/nhl_morning_skate_connector.py
"""
NHL morning skate lineup connector for SportMind agents.

The morning skate (T-3h to T-1h on game day) is the primary
goaltender confirmation window in hockey. This connector checks
both the NHL official API and Daily Faceoff for lineup projections.

Sources:
  NHL API (unofficial): https://api-web.nhle.com/v1/
  Daily Faceoff: https://www.dailyfaceoff.com/projected-lineups
                 (via Fetch MCP — no API)

SportMind skills this feeds:
  → athlete/nhl/athlete-intel-nhl.md (morning skate section)
  → core/lineup-quality-index.md (hockey GK weight 2.0)
  → core/pre-match-squad-intelligence.md (NHL section)
"""

import asyncio
import re
import aiohttp
from datetime import datetime, timezone

NHL_API_BASE = "https://api-web.nhle.com/v1"

# Team code to NHL API abbreviation mapping (common tokens)
TEAM_CODES = {
    "Toronto Maple Leafs": "TOR", "Boston Bruins": "BOS",
    "New York Rangers": "NYR",    "Pittsburgh Penguins": "PIT",
    "Tampa Bay Lightning": "TBL", "Colorado Avalanche": "COL",
    "Vegas Golden Knights": "VGK","Edmonton Oilers": "EDM",
    "Carolina Hurricanes": "CAR", "New Jersey Devils": "NJD",
}

# GSAx benchmarks for LQI goaltender rating (normalised 0-100)
# Source: naturalstattrick.com season leaders
def gsax_to_lqi_rating(gsax: float) -> int:
    """Convert GSAx to 0-100 rating for LQI calculation."""
    if gsax >= 15:   return 92
    elif gsax >= 10: return 85
    elif gsax >= 5:  return 78
    elif gsax >= 0:  return 70
    elif gsax >= -5: return 60
    else:            return 50


class NHLMorningSkatConnector:

    async def get_team_roster(self, team_code: str) -> dict:
        """Get current roster including goaltenders."""
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{NHL_API_BASE}/roster/{team_code}/current"
            ) as resp:
                return await resp.json()

    async def get_todays_games(self) -> list[dict]:
        """Get today's NHL schedule."""
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{NHL_API_BASE}/schedule/now") as resp:
                data = await resp.json()
                game_week = data.get("gameWeek", [{}])
                today = game_week[0] if game_week else {}
                return today.get("games", [])

    async def get_player_landing(self, player_id: int) -> dict:
        """Get player status and stats."""
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{NHL_API_BASE}/player/{player_id}/landing"
            ) as resp:
                return await resp.json()

    def build_goaltender_brief(self, roster: dict, team_code: str) -> dict:
        """
        Identify starting and backup goaltender for morning skate.
        Maps to: core/lineup-quality-index.md hockey section (GK weight 2.0)
        """
        goalies = [
            p for p in roster.get("goalies", [])
            if p.get("positionCode") == "G"
        ]

        if not goalies:
            return {
                "team": team_code,
                "starter": None,
                "backup": None,
                "lineup_unconfirmed": True,
                "note": "No goaltender data available — check Daily Faceoff",
            }

        # Sort by games played (starter = more games)
        goalies_sorted = sorted(
            goalies,
            key=lambda g: g.get("careerTotals", {})
                           .get("regularSeason", {})
                           .get("gamesPlayed", 0),
            reverse=True
        )

        starter = goalies_sorted[0] if goalies_sorted else None
        backup  = goalies_sorted[1] if len(goalies_sorted) > 1 else None

        starter_name = (
            f"{starter.get('firstName',{}).get('default','')} "
            f"{starter.get('lastName',{}).get('default','')}"
            if starter else "Unknown"
        )
        backup_name = (
            f"{backup.get('firstName',{}).get('default','')} "
            f"{backup.get('lastName',{}).get('default','')}"
            if backup else "Unknown"
        )

        return {
            "team":              team_code,
            "probable_starter":  starter_name.strip(),
            "probable_backup":   backup_name.strip(),
            "lineup_unconfirmed": True,  # Always True until morning skate
            "confirm_at":        "Morning skate T-3h to T-1h",
            "confirmation_signal": (
                "If probable_starter is absent from morning skate drills: "
                "backup is starting. Apply backup GK modifier."
            ),
            "lqi_note": (
                "GK positional weight = 2.0 in hockey LQI. "
                "Backup starting = significant LQI reduction. "
                "See: core/lineup-quality-index.md hockey section."
            ),
            "skill_reference": "athlete/nhl/athlete-intel-nhl.md",
        }

    def compute_back_to_back_flag(self, games: list, team_code: str) -> dict:
        """
        Check if a team is on a back-to-back (played last night).
        Back-to-backs significantly affect goaltender rotation.
        """
        today = datetime.now(timezone.utc).date()
        yesterday_games = [
            g for g in games
            if (
                g.get("awayTeam", {}).get("abbrev") == team_code or
                g.get("homeTeam", {}).get("abbrev") == team_code
            )
        ]
        # If this team played yesterday, it is a back-to-back
        # In practice: check the schedule endpoint for previous day
        return {
            "team":             team_code,
            "back_to_back":     len(yesterday_games) > 0,
            "modifier_if_true": 0.92,
            "note": (
                "Back-to-back: expect backup goaltender to start. "
                "Apply ×0.92 team fatigue modifier."
                if yesterday_games else
                "No back-to-back detected."
            ),
        }


# ── Usage example ─────────────────────────────────────────────────────────
async def nhl_morning_skate_brief(home_team_name: str, away_team_name: str) -> dict:
    """Generate morning skate brief for an NHL matchup."""
    connector    = NHLMorningSkatConnector()
    home_code    = TEAM_CODES.get(home_team_name, home_team_name[:3].upper())
    away_code    = TEAM_CODES.get(away_team_name, away_team_name[:3].upper())

    home_roster  = await connector.get_team_roster(home_code)
    away_roster  = await connector.get_team_roster(away_code)

    return {
        "matchup":          f"{home_team_name} vs {away_team_name}",
        "home_goaltenders": connector.build_goaltender_brief(home_roster, home_code),
        "away_goaltenders": connector.build_goaltender_brief(away_roster, away_code),
        "morning_skate_window": "T-3h to T-1h — primary confirmation window",
        "daily_faceoff_url": "https://www.dailyfaceoff.com/projected-lineups",
        "generated_at":     datetime.now(timezone.utc).isoformat(),
        "important": (
            "Do not finalise NHL signal until morning skate confirms starter. "
            "GK weight = 2.0 in LQI — starter identity is the highest-impact variable."
        ),
    }


if __name__ == "__main__":
    result = asyncio.run(nhl_morning_skate_brief("Toronto Maple Leafs", "Boston Bruins"))
    import json
    print(json.dumps(result, indent=2))
```

---

## Connector 8 — Odds API divergence detector

```python
# connectors/odds_divergence_connector.py
"""
Prediction market divergence detector using The Odds API.

Compares SportMind's directional signal against market-implied
probabilities to detect high-value divergence signals.

API: The Odds API (https://the-odds-api.com)
Free tier: 500 requests/month — sufficient for pre-match analysis.
Setup: Get API key at the-odds-api.com

SportMind skills this feeds:
  → core/prediction-market-intelligence.md (divergence detection)
  → core/historical-intelligence-framework.md (probability conversion)
"""

import asyncio
import aiohttp
from typing import Optional
from datetime import datetime, timezone

# Set your API key: export ODDS_API_KEY="your_key_here"
ODDS_KEY  = ""  # Replace with your The Odds API key
ODDS_BASE = "https://api.the-odds-api.com/v4"

# Sport keys for The Odds API
SPORT_KEYS = {
    "football":    "soccer_epl",           # Premier League
    "ucl":         "soccer_uefa_champs_league",
    "la_liga":     "soccer_spain_la_liga",
    "bundesliga":  "soccer_germany_bundesliga",
    "basketball":  "basketball_nba",
    "mma":         "mma_mixed_martial_arts",
    "cricket_ipl": "cricket_ipl",
    "ice_hockey":  "icehockey_nhl",
    "tennis_atp":  "tennis_atp",
}

# Bookmakers to use for probability calculation
PREFERRED_BOOKS = ["pinnacle", "betfair_ex_uk", "bet365", "unibet"]


class OddsDivergenceConnector:

    def __init__(self, api_key: str = ODDS_KEY):
        self.key = api_key

    async def get_odds(self, sport: str,
                       regions: str = "uk,eu") -> list[dict]:
        """Get pre-match odds for a sport."""
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{ODDS_BASE}/sports/{sport}/odds",
                params={
                    "apiKey":   self.key,
                    "regions":  regions,
                    "markets":  "h2h",      # Head-to-head (match result)
                    "oddsFormat": "decimal",
                }
            ) as resp:
                data = await resp.json()
                return data if isinstance(data, list) else []

    def decimal_to_probability(self, decimal_odds: float) -> float:
        """Convert decimal odds to implied probability."""
        if decimal_odds <= 0:
            return 0.0
        return round(1 / decimal_odds, 4)

    def get_best_book_odds(self, event: dict) -> Optional[dict]:
        """
        Get odds from the highest-quality bookmaker available.
        Priority: Pinnacle > Betfair > Bet365 > first available.
        Sharp books (Pinnacle) closest to true probability.
        """
        bookmakers = event.get("bookmakers", [])
        if not bookmakers:
            return None

        for preferred in PREFERRED_BOOKS:
            for bm in bookmakers:
                if bm.get("key") == preferred:
                    markets = bm.get("markets", [])
                    h2h = next((m for m in markets if m.get("key") == "h2h"), None)
                    if h2h:
                        return {
                            "bookmaker": bm.get("title"),
                            "outcomes":  h2h.get("outcomes", []),
                        }

        # Fallback: first available
        first = bookmakers[0]
        markets = first.get("markets", [])
        h2h = next((m for m in markets if m.get("key") == "h2h"), None)
        return {
            "bookmaker": first.get("title"),
            "outcomes":  h2h.get("outcomes", []) if h2h else [],
        }

    def detect_divergence(self, sportmind_direction: str,
                           sportmind_sms: int,
                           event: dict) -> dict:
        """
        Compare SportMind signal against market-implied probability.
        
        Maps to: core/prediction-market-intelligence.md
        High-value signal: SMS ≥ 70 AND market strongly disagrees.
        """
        best_odds = self.get_best_book_odds(event)
        if not best_odds:
            return {"divergence": "NO_MARKET_DATA", "signal": "NEUTRAL"}

        outcomes     = best_odds["outcomes"]
        home_team    = event.get("home_team", "")
        away_team    = event.get("away_team", "")

        # Build probability map
        probs = {}
        raw_probs = {}
        for o in outcomes:
            name  = o.get("name", "")
            price = o.get("price", 2.0)
            raw_probs[name] = self.decimal_to_probability(price)

        # Remove overround: normalise to sum to 1.0
        total = sum(raw_probs.values())
        if total > 0:
            probs = {k: round(v / total, 4) for k, v in raw_probs.items()}
        else:
            probs = raw_probs

        # Get market probability for SportMind's direction
        if sportmind_direction == "HOME":
            market_prob = probs.get(home_team, 0.5)
        elif sportmind_direction == "AWAY":
            market_prob = probs.get(away_team, 0.5)
        else:  # DRAW
            draw_keys = [k for k in probs if k.lower() == "draw"]
            market_prob = probs.get(draw_keys[0], 0.33) if draw_keys else 0.33

        # Divergence assessment
        # SportMind SMS → implied confidence range
        # SMS 80-100 → 65-75% | SMS 60-79 → 55-65% | SMS 40-59 → 48-55%
        if sportmind_sms >= 80:
            sm_implied_prob = 0.70
        elif sportmind_sms >= 60:
            sm_implied_prob = 0.60
        elif sportmind_sms >= 40:
            sm_implied_prob = 0.52
        else:
            sm_implied_prob = 0.50

        prob_gap = sm_implied_prob - market_prob

        if sportmind_sms >= 70 and prob_gap >= 0.10:
            divergence_type = "STRUCTURAL_EDGE"
            divergence_note = (
                f"SportMind SMS {sportmind_sms} implies ~{sm_implied_prob:.0%} "
                f"but market prices {sportmind_direction} at {market_prob:.0%}. "
                f"Gap of {abs(prob_gap):.0%}. SportMind may have structural intelligence "
                f"the market has not priced. High conviction signal."
            )
        elif sportmind_sms >= 70 and -0.05 <= prob_gap <= 0.05:
            divergence_type = "CONFIRMING"
            divergence_note = (
                f"SportMind and market agree. SMS {sportmind_sms}, "
                f"market prob {market_prob:.0%}. Elevated conviction."
            )
        elif sportmind_sms >= 70 and prob_gap <= -0.15:
            divergence_type = "MARKET_CONTRADICTS"
            divergence_note = (
                f"Market strongly contradicts SportMind. SMS {sportmind_sms} "
                f"({sportmind_direction}) but market prices it at only {market_prob:.0%}. "
                f"Review: does market have information SportMind has not incorporated?"
            )
        else:
            divergence_type = "NEUTRAL"
            divergence_note = (
                f"SMS {sportmind_sms} — moderate signal. "
                f"Market: {market_prob:.0%}. No strong divergence."
            )

        return {
            "event":              f"{home_team} vs {away_team}",
            "sportmind_direction": sportmind_direction,
            "sportmind_sms":      sportmind_sms,
            "market_prob":        market_prob,
            "sm_implied_prob":    sm_implied_prob,
            "probability_gap":    round(prob_gap, 4),
            "bookmaker":          best_odds["bookmaker"],
            "divergence_type":    divergence_type,
            "divergence_note":    divergence_note,
            "market_probabilities": probs,
            "skill_reference":    "core/prediction-market-intelligence.md",
        }

    async def find_best_divergences(self, sport_key: str,
                                     min_sms: int = 65) -> list[dict]:
        """
        Scan all upcoming events in a sport for divergence signals.
        Returns events where SportMind has highest structural edge.
        Note: Requires SportMind signals to already be generated.
        This connector provides the market comparison layer only.
        """
        events = await self.get_odds(sport_key)
        print(f"Found {len(events)} events for {sport_key}")
        print("Note: Pass your SportMind signals to detect_divergence() per event.")
        return [
            {
                "event_id":   e.get("id"),
                "home_team":  e.get("home_team"),
                "away_team":  e.get("away_team"),
                "commence":   e.get("commence_time"),
                "bookmakers": len(e.get("bookmakers", [])),
            }
            for e in events
        ]


# ── Usage example ─────────────────────────────────────────────────────────
async def odds_divergence_check(sport: str, home_team: str, away_team: str,
                                  sportmind_direction: str,
                                  sportmind_sms: int) -> dict:
    """
    Check if SportMind signal diverges from market for a specific fixture.
    
    Args:
        sport:                One of SPORT_KEYS keys (e.g. "football")
        home_team:            Home team name as it appears in odds markets
        away_team:            Away team name
        sportmind_direction:  "HOME", "AWAY", or "DRAW" from SportMind signal
        sportmind_sms:        SportMind Score (0-100) from pre-match signal
    """
    connector = OddsDivergenceConnector()
    sport_key = SPORT_KEYS.get(sport, sport)
    events    = await connector.get_odds(sport_key)

    # Find the specific event
    target = next(
        (e for e in events
         if home_team.lower() in e.get("home_team", "").lower() and
            away_team.lower() in e.get("away_team", "").lower()),
        None
    )

    if not target:
        return {
            "error": f"Event not found in odds market for {sport_key}",
            "available_events": [
                f"{e['home_team']} vs {e['away_team']}"
                for e in events[:5]
            ],
        }

    return connector.detect_divergence(sportmind_direction, sportmind_sms, target)


if __name__ == "__main__":
    # Example: SportMind said HOME with SMS 78, check if market agrees
    result = asyncio.run(odds_divergence_check(
        sport="football",
        home_team="Arsenal",
        away_team="Bournemouth",
        sportmind_direction="HOME",
        sportmind_sms=78,
    ))
    import json
    print(json.dumps(result, indent=2))
```

---

## Wiring all five connectors into a pre-match agent chain

```python
# examples/full_pre_match_with_apis.py
"""
Complete pre-match agent chain combining SportMind MCP + all five connectors.

This is the pattern for production SportMind agents:
  1. SportMind MCP → intelligence signal
  2. Sport-specific API connector → live data
  3. Odds API → market confirmation
  4. Combine → final signal with full context

For the SportMind-specific intelligence calls (macro, squad, FTP etc.),
run the MCP server first: python scripts/sportmind_mcp.py --http --port 3001
"""

import asyncio
import aiohttp
import json
from datetime import datetime, timezone

# MCP server: python scripts/sportmind_mcp.py --http --port 3001
SPORTMIND_MCP = "http://localhost:3001/mcp"


async def call_mcp(tool: str, args: dict) -> dict:
    """Call SportMind MCP tool."""
    payload = {
        "jsonrpc": "2.0",
        "method":  "tools/call",
        "params":  {"name": tool, "arguments": args},
        "id":      1,
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(SPORTMIND_MCP, json=payload) as resp:
            data = await resp.json()
            content = data.get("result", {}).get("content", [{}])
            text = content[0].get("text", "{}") if content else "{}"
            return json.loads(text)


async def full_football_pre_match(home: str, away: str,
                                   competition: str, token: str) -> dict:
    """
    Full pre-match chain: SportMind intelligence + live API data + odds.
    
    Requires:
      - ODDS_API_KEY environment variable
      - SportMind MCP server running
      - Optional: API-Football key for lineup data
    """
    print(f"\nPre-match: {home} vs {away} ({competition})")
    print("=" * 50)

    # PHASE 1: SportMind intelligence (MCP)
    print("Phase 1: SportMind intelligence...")
    macro    = await call_mcp("sportmind_macro", {})
    signal   = await call_mcp("sportmind_pre_match", {
        "sport": "football", "home_team": home,
        "away_team": away, "competition": competition,
        "use_case": "fan_token_tier1"
    })
    sentiment = await call_mcp("sportmind_sentiment_snapshot", {
        "token": token, "use_case": "fan_token_tier1"
    })

    macro_mod  = macro.get("macro_state", {}).get("crypto_cycle", {}).get("macro_modifier", 1.0)
    direction  = signal.get("signal", {}).get("direction", "HOME")
    sms        = signal.get("sportmind_score", {}).get("sms", 60)
    adj_score  = signal.get("signal", {}).get("adjusted_score", 50.0)

    print(f"  SportMind: direction={direction}, SMS={sms}, macro={macro_mod}")

    # PHASE 2: Market divergence check (Odds API)
    print("Phase 2: Market divergence check...")
    try:
        from connectors.odds_divergence_connector import odds_divergence_check
        divergence = await odds_divergence_check(
            "football", home, away, direction, sms
        )
        div_type = divergence.get("divergence_type", "NEUTRAL")
        print(f"  Market: {div_type} — {divergence.get('divergence_note','')[:80]}")
    except Exception as e:
        divergence = {"error": str(e), "divergence_type": "UNAVAILABLE"}
        div_type = "UNAVAILABLE"
        print(f"  Market: unavailable ({e})")

    # PHASE 3: Assemble final signal
    final_confidence = "HIGH" if sms >= 70 and div_type == "CONFIRMING" else \
                       "ELEVATED" if sms >= 70 and div_type == "STRUCTURAL_EDGE" else \
                       "MEDIUM" if sms >= 55 else "LOW"

    return {
        "match":             f"{home} vs {away}",
        "competition":       competition,
        "token":             token,
        "generated_at":      datetime.now(timezone.utc).isoformat(),

        "sportmind_signal": {
            "direction":      direction,
            "sms":            sms,
            "adjusted_score": adj_score,
            "macro_modifier": macro_mod,
        },

        "market_signal": {
            "divergence_type": div_type,
            "market_prob":     divergence.get("market_prob"),
            "gap":             divergence.get("probability_gap"),
        },

        "combined": {
            "final_confidence": final_confidence,
            "recommended":      "ENTER" if final_confidence in ("HIGH","ELEVATED") else "WAIT",
            "note": (
                "SportMind + market confirming → high conviction." if div_type == "CONFIRMING"
                else "SportMind structural edge vs market → investigate further." if div_type == "STRUCTURAL_EDGE"
                else "Market contradicts — review before acting." if div_type == "MARKET_CONTRADICTS"
                else "Standard pre-match signal."
            ),
        },

        "skill_stack": [
            "macro/macro-overview.md",
            "sports/football/sport-domain-football.md",
            "core/prediction-market-intelligence.md",
            "fan-token/football-token-intelligence/",
        ],
    }


if __name__ == "__main__":
    result = asyncio.run(
        full_football_pre_match(
            home="Arsenal", away="Bournemouth",
            competition="Premier League", token="AFC"
        )
    )
    print(json.dumps(result, indent=2))
```

---

*SportMind v3.52 · MIT License · sportmind.dev*
*See also: platform/api-providers.md · platform/data-connector-templates.md*
*core/prediction-market-intelligence.md · core/pre-match-squad-intelligence.md*
*core/lineup-quality-index.md · examples/agentic-workflows/*
