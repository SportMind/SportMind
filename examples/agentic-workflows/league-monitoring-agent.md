# Agentic Workflow Pattern 5 — League Monitoring Agent

**Continuously monitors an entire football league for signal events that
matter to fan token holders: title races, relegation battles, continental
qualification fights, and managerial instability signals.**

This pattern goes beyond monitoring a single token — it monitors the full
competitive context of a league and surfaces the moments when individual
match outcomes have elevated commercial significance for token-connected clubs.

---

## Why a dedicated league monitor

The pre-match chain (Pattern 2) analyses individual matches when they are
imminent. The portfolio monitor (Pattern 1) tracks tokens in a portfolio.

Neither of these answers the question: *which matches this weekend actually
matter, across the whole league, for fan token holders?*

A standard Round 28 Premier League fixture between two mid-table clubs with
no stakes has FTIS 0.30. The same fixture where the loser drops into the
relegation zone — worth £170M in broadcast revenue — has FTIS 0.65. The
league monitor detects this distinction before the pre-match chain runs,
ensuring that high-stakes matches are flagged early and lower-stakes matches
are deprioritised.

---

## The League Monitor agent

```python
# examples/agentic-workflows/league_monitor.py
"""
SportMind League Monitoring Agent
Pattern 5: Continuous league intelligence for fan token holders.

Monitors: Premier League (configurable to any league)
Cycle: Every 6 hours during season; daily in off-season
Autonomy: Level 2 (alerts autonomously; human decides on action)
"""
import asyncio
import logging
import os
from datetime import datetime, timezone
from pathlib import Path
import json

import aiohttp

SPORTMIND_API  = os.environ.get("SPORTMIND_API", "http://localhost:8080")
ALERT_WEBHOOK  = os.environ.get("ALERT_WEBHOOK", "")
LEAGUE_ID      = "premier-league"
SEASON         = "2025-26"
CYCLE_HOURS    = 6

log = logging.getLogger("sportmind.league-monitor")


# ── League state ──────────────────────────────────────────────────────────────

class LeagueStandings:
    """Tracks current league standings and detects signal events."""

    def __init__(self, league_id: str):
        self.league_id     = league_id
        self.standings     = {}    # {club: {position, points, played, goal_diff}}
        self.token_clubs   = set() # clubs with active fan tokens
        self.last_updated  = None

    def update(self, new_standings: dict):
        """Update standings and detect changes."""
        changes = []

        for club, stats in new_standings.items():
            if club in self.standings:
                old = self.standings[club]
                if stats["position"] != old["position"]:
                    changes.append({
                        "club":         club,
                        "change_type":  "position_change",
                        "old_position": old["position"],
                        "new_position": stats["position"],
                        "has_token":    club in self.token_clubs
                    })

        self.standings    = new_standings
        self.last_updated = datetime.now(timezone.utc)
        return changes

    def detect_stake_events(self, rounds_remaining: int) -> list:
        """
        Detect which clubs are in high-stakes positions.
        Stakes activate different signal weights in football-leagues-advanced.md
        """
        if not self.standings:
            return []

        events = []
        positions = sorted(self.standings.items(), key=lambda x: x[1]["position"])
        total_clubs = len(positions)

        for club, stats in positions:
            pos    = stats["position"]
            points = stats["points"]

            # Title race: within 6 points of leader in last 8 rounds
            if pos <= 3 and rounds_remaining <= 8:
                leader_pts = positions[0][1]["points"]
                if leader_pts - points <= 6:
                    events.append({
                        "type":          "title_race",
                        "club":          club,
                        "position":      pos,
                        "points_behind": leader_pts - points,
                        "signal_weight": 1.40,
                        "has_token":     club in self.token_clubs
                    })

            # Top 4 battle: positions 3-6 within 5 points (Champions League)
            if 3 <= pos <= 6 and rounds_remaining <= 8:
                events.append({
                    "type":         "cl_qualification",
                    "club":         club,
                    "position":     pos,
                    "signal_weight": 1.35,
                    "has_token":    club in self.token_clubs
                })

            # Relegation battle: bottom 6 in last 12 rounds
            if pos >= total_clubs - 5 and rounds_remaining <= 12:
                if pos >= total_clubs - 2:
                    signal_weight = 1.40  # Directly in the drop
                else:
                    signal_weight = 1.20  # Nervously close
                events.append({
                    "type":         "relegation_battle",
                    "club":         club,
                    "position":     pos,
                    "signal_weight": signal_weight,
                    "financial_at_stake": "£170M broadcast revenue",
                    "has_token":    club in self.token_clubs
                })

        return events


# ── Match prioritisation ──────────────────────────────────────────────────────

class LeagueMatchPrioritiser:
    """
    Scores upcoming league fixtures by their fan token signal importance.
    Feeds into pre-match chain agent for prioritised analysis.
    """

    def __init__(self, standings: LeagueStandings, macro_modifier: float):
        self.standings      = standings
        self.macro_modifier = macro_modifier

    def score_fixture(self, fixture: dict) -> dict:
        """
        Score a fixture by its token signal importance.
        Uses football-leagues-advanced.md prize window logic.
        """
        home        = fixture.get("home_team", "")
        away        = fixture.get("away_team", "")
        gameweek    = fixture.get("gameweek", 38)
        rounds_left = max(0, 38 - gameweek)

        # Base score: standard league match
        base_score     = 0.35
        stake_modifiers = []

        # Check both clubs for stake events
        stake_events = self.standings.detect_stake_events(rounds_left)
        for event in stake_events:
            if event["club"] in (home, away):
                base_score = max(base_score, event["signal_weight"] * 0.35)
                stake_modifiers.append(event["type"])

        # Derby check
        is_derby   = fixture.get("is_derby", False)
        if is_derby:
            base_score = max(base_score, 0.65)
            stake_modifiers.append("derby")

        # Macro modifier
        final_score = base_score * self.macro_modifier

        # Token relevance
        home_has_token = home in self.standings.token_clubs
        away_has_token = away in self.standings.token_clubs
        token_relevant = home_has_token or away_has_token

        return {
            "fixture_id":      fixture.get("id"),
            "home":            home,
            "away":            away,
            "gameweek":        gameweek,
            "hours_away":      fixture.get("hours_away", 168),
            "signal_score":    round(final_score, 3),
            "signal_tier":     self._classify_tier(final_score),
            "stake_types":     stake_modifiers,
            "token_relevant":  token_relevant,
            "home_has_token":  home_has_token,
            "away_has_token":  away_has_token,
            "priority":        "HIGH" if final_score >= 0.55 else
                               "MEDIUM" if final_score >= 0.40 else "LOW"
        }

    def _classify_tier(self, score: float) -> str:
        if score >= 0.75:   return "TIER_1"
        elif score >= 0.55: return "TIER_2"
        elif score >= 0.40: return "TIER_3"
        else:               return "LOW_SIGNAL"

    def prioritise_weekend(self, fixtures: list) -> list:
        """Score and sort all upcoming fixtures by token signal importance."""
        scored = [self.score_fixture(f) for f in fixtures]
        # Sort: token-relevant first, then by signal score
        return sorted(scored,
                       key=lambda x: (x["token_relevant"], x["signal_score"]),
                       reverse=True)


# ── League monitoring agent ───────────────────────────────────────────────────

class LeagueMonitorAgent:
    """
    Full league monitoring agent.
    Tracks standings, detects stake events, prioritises fixtures,
    and feeds the pre-match chain with ranked matches.
    """

    def __init__(self):
        self.standings      = LeagueStandings(LEAGUE_ID)
        self.macro_modifier = 1.00
        self.macro_phase    = "UNKNOWN"
        self.cycle_count    = 0
        self.alerts_sent    = 0
        self.skill_stack    = None

        # Token-connected clubs in this league
        # Replace with your actual token mapping
        self.standings.token_clubs = {
            "Manchester City",
            "Arsenal",
            "Chelsea",
            "Manchester United",
            "Tottenham",
        }

    async def initialise(self):
        log.info(f"Initialising League Monitor: {LEAGUE_ID} {SEASON}")

        # Load football intelligence stack
        try:
            async with aiohttp.ClientSession() as s:
                async with s.get(
                    f"{SPORTMIND_API}/stack",
                    params={"sport": "football", "use_case": "fan_token_tier1"}
                ) as r:
                    data             = await r.json()
                    self.skill_stack = data.get("stack", [])
        except Exception as e:
            log.warning(f"Stack unavailable: {e}")

        await self._refresh_macro()
        await self._refresh_standings()
        log.info("League Monitor ready")

    async def run(self):
        await self.initialise()
        log.info(f"Monitoring {LEAGUE_ID} — {CYCLE_HOURS}h cycle")
        while True:
            try:
                await self._run_cycle()
            except Exception as e:
                log.error(f"Cycle error: {e}")
            await asyncio.sleep(CYCLE_HOURS * 3600)

    async def _run_cycle(self):
        self.cycle_count += 1
        log.info(f"── League Monitor Cycle {self.cycle_count} ──")

        # Refresh macro (Tier 3)
        await self._refresh_macro()

        # Refresh standings (Tier 2 — weekly or after match day)
        changes = await self._refresh_standings()
        if changes:
            await self._process_standing_changes(changes)

        # Score upcoming fixtures
        fixtures  = await self._get_upcoming_fixtures()
        prioritiser = LeagueMatchPrioritiser(self.standings, self.macro_modifier)
        prioritised = prioritiser.prioritise_weekend(fixtures)

        # Alert on high-priority token-relevant fixtures
        high_priority = [f for f in prioritised
                         if f["priority"] == "HIGH" and f["token_relevant"]]

        for fixture in high_priority:
            if fixture["hours_away"] <= 72:
                await self._alert_fixture(fixture)

        # Publish to signal bus for pre-match chain agent
        await self._publish_priority_list(prioritised)

        log.info(
            f"Cycle {self.cycle_count}: "
            f"{len(prioritised)} fixtures scored, "
            f"{len(high_priority)} high-priority token fixtures"
        )

    async def _process_standing_changes(self, changes: list):
        """Alert on position changes for token-relevant clubs."""
        for change in changes:
            if change["has_token"]:
                await self._send_alert({
                    "type":         "standing_change",
                    "club":         change["club"],
                    "old_position": change["old_position"],
                    "new_position": change["new_position"],
                    "message":      (
                        f"📊 STANDINGS UPDATE: {change['club']} "
                        f"moved {change['old_position']} → {change['new_position']}"
                    )
                })

    async def _alert_fixture(self, fixture: dict):
        """Alert on high-signal upcoming fixture."""
        emoji = "🔥" if fixture["signal_tier"] == "TIER_1" else "📋"
        message = (
            f"{emoji} HIGH-SIGNAL FIXTURE\n"
            f"{fixture['home']} vs {fixture['away']}\n"
            f"Signal: {fixture['signal_score']} ({fixture['signal_tier']})\n"
            f"Stakes: {', '.join(fixture['stake_types']) or 'standard'}\n"
            f"Token clubs: {[c for c,h in [(fixture['home'],fixture['home_has_token']),(fixture['away'],fixture['away_has_token'])] if h]}\n"
            f"In {fixture['hours_away']}h — pre-match chain scheduled"
        )
        log.info(f"ALERT: {message.split(chr(10))[0]}")
        if ALERT_WEBHOOK:
            async with aiohttp.ClientSession() as s:
                await s.post(ALERT_WEBHOOK, json={"text": message, "fixture": fixture})
        self.alerts_sent += 1

    async def _publish_priority_list(self, prioritised: list):
        """
        Publish prioritised fixture list to signal bus.
        Pre-match chain agent consumes this to decide what to analyse.
        See: examples/agentic-workflows/multi-agent-coordination.md
        """
        output_path = Path("coordination/league_priority.json")
        output_path.parent.mkdir(exist_ok=True)
        output_path.write_text(json.dumps({
            "league":     LEAGUE_ID,
            "generated":  datetime.now(timezone.utc).isoformat(),
            "macro":      {"phase": self.macro_phase, "modifier": self.macro_modifier},
            "fixtures":   prioritised[:20]  # Top 20 by priority
        }, indent=2))

    async def _refresh_standings(self) -> list:
        """
        Refresh league standings.
        REPLACE with your live standings data source.
        football-data.org, Sportradar, or your own database.
        """
        # Stub: return empty changes (replace with live API call)
        return []

    async def _get_upcoming_fixtures(self) -> list:
        """
        Get upcoming fixtures.
        REPLACE with your live fixture data source.
        """
        return []

    async def _refresh_macro(self):
        try:
            async with aiohttp.ClientSession() as s:
                async with s.get(f"{SPORTMIND_API}/macro-state") as r:
                    data            = await r.json()
                    cycle           = data["macro_state"]["crypto_cycle"]
                    self.macro_modifier = cycle["macro_modifier"]
                    self.macro_phase    = cycle["phase"]
        except Exception as e:
            log.warning(f"Macro refresh failed: {e}")

    async def _send_alert(self, alert: dict):
        log.info(f"ALERT: {alert.get('message', alert.get('type'))}")
        if ALERT_WEBHOOK:
            try:
                async with aiohttp.ClientSession() as s:
                    await s.post(ALERT_WEBHOOK, json=alert)
            except Exception as e:
                log.error(f"Alert failed: {e}")

    def get_status(self) -> dict:
        """Observable state for sportmind_agent_status MCP tool."""
        return {
            "agent_id":         "league-monitor-001",
            "agent_type":       "league_monitor",
            "state":            "MONITORING",
            "autonomy_level":   2,
            "league":           LEAGUE_ID,
            "standings_clubs":  len(self.standings.standings),
            "token_clubs":      len(self.standings.token_clubs),
            "cycle_count":      self.cycle_count,
            "alerts_sent":      self.alerts_sent,
            "macro_modifier":   self.macro_modifier,
            "macro_phase":      self.macro_phase,
        }


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")
    asyncio.run(LeagueMonitorAgent().run())
```

---

## How this integrates with other agents

```
LEAGUE MONITOR IN THE COORDINATED SYSTEM:

League Monitor FEEDS:
  → Pre-Match Chain (Pattern 2): priority fixture list
    Pre-match chain uses league_priority.json to decide which matches to analyse
    High-signal fixtures get full T-48h + T-2h analysis
    Low-signal fixtures may be skipped or get minimal analysis
    
  → Portfolio Monitor (Pattern 1): standings change alerts
    When a token-connected club moves in/out of relegation zone,
    portfolio monitor receives the alert and adjusts holding recommendations
    
  → Signal Bus: publishes stake_event signals
    Any agent subscribed to the bus receives standing changes and fixture priorities

League Monitor RECEIVES:
  → Match results (from your data source)
  → Standings updates (from your data source)
  → Nothing from other SportMind agents (it is a data intake agent)

ECOSYSTEM INTEGRATION:
  FanTokenIntel: reads league_priority.json for portfolio context
  SportFi Kit: reads token-relevant high-signal fixture list for UI prioritisation
  Human operators: receive consolidated weekly priority briefing
```

---

## Compatibility

**Football leagues advanced:** `market/football-leagues-advanced.md` — prize window and relegation stake values
**Derby intelligence:** `core/derby-intelligence.md` — derby detection
**Manager intelligence:** `core/manager-intelligence.md` — managerial instability as stake signal
**Pre-match chain:** Pattern 2 in `examples/agentic-workflows/README.md`
**Multi-agent coordination:** `examples/agentic-workflows/multi-agent-coordination.md`
**Agent framework:** `core/autonomous-agent-framework.md`

*MIT License · SportMind · sportmind.dev*
