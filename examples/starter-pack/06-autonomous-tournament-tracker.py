#!/usr/bin/env python3
"""
SportMind Starter Pack — Example 06: Autonomous Tournament Tracker
===================================================================
A fully autonomous agent that tracks a tournament from start to finish.

What this demonstrates:
  - Full autonomous agent lifecycle (all 7 states)
  - Level 3 autonomy (acts immediately; human reviews log asynchronously)
  - NCSI computation per match result
  - Audit logging (Safety Principle 5 — every cycle logged)
  - Graceful degradation (Safety Principle 6 — never silent failure)
  - Daily intelligence briefing generation
  - No human input required once started

What you need:
  pip install aiohttp
  python scripts/sportmind_api.py   # in another terminal

What to change first:
  TOURNAMENT_ID   — your tournament identifier
  TOURNAMENT_NAME — display name
  NATIONS_DATA    — which nations are in the tournament + their club token mappings
  BRACKET         — initial tournament bracket

AUTONOMY LEVEL 3:
  This agent acts immediately on every match result.
  It does NOT ask for human approval to update NCSI scores.
  Humans review the daily briefing log, not each individual update.
  Human alert is triggered only for significant NCSI moves (>0.15 delta).

See: core/autonomous-agent-framework.md for the full framework
See: market/international-football-cycle.md for NCSI weights used here
"""

import asyncio
import json
import logging
import os
from datetime import datetime, timezone
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional

import aiohttp

SPORTMIND_API   = os.environ.get("SPORTMIND_API", "http://localhost:8080")
ALERT_WEBHOOK   = os.environ.get("ALERT_WEBHOOK", "")
AUDIT_LOG_PATH  = Path("tournament_audit_log.jsonl")
BRIEFING_PATH   = Path("daily_briefing.md")

logging.basicConfig(
    level  = logging.INFO,
    format = "%(asctime)s [%(levelname)s] %(message)s"
)
log = logging.getLogger("sportmind.tournament-tracker")


# ── Tournament configuration ──────────────────────────────────────────────────

TOURNAMENT_ID   = "euro-2028"
TOURNAMENT_NAME = "UEFA European Championship 2028"
TOURNAMENT_SPORT = "football"

# Nations in tournament and their club token mappings
# Format: nation → [(player_name, club_token, atm_score)]
NATIONS_DATA = {
    "France": [
        {"player": "Key Player 1", "club_token": "PSG",  "atm": 0.88},
        {"player": "Key Player 2", "club_token": "PSG",  "atm": 0.72},
        {"player": "Key Player 3", "club_token": "CITY", "atm": 0.65},
    ],
    "Spain": [
        {"player": "Key Player 1", "club_token": "BAR",  "atm": 0.90},
        {"player": "Key Player 2", "club_token": "BAR",  "atm": 0.75},
    ],
    "England": [
        {"player": "Key Player 1", "club_token": "CITY", "atm": 0.85},
    ],
    # Add all participating nations
}

# NCSI weights by stage — from market/international-football-cycle.md
# Note: for Euros, apply ×1.10 vs World Cup for European club tokens
NCSI_STAGE_WEIGHTS = {
    "group_stage":   1.00 * 1.10,   # Euros bonus for European clubs
    "round_of_16":   1.20 * 1.10,
    "quarter_final": 1.60 * 1.10,
    "semi_final":    1.80 * 1.10,
    "final":         2.00 * 1.10,
    "third_place":   1.20 * 1.10,
}

NCSI_ELIMINATION_PENALTIES = {
    "round_of_16":   -0.08,
    "quarter_final": -0.12,
    "semi_final":    -0.18,
    "final":         -0.10,  # Runner-up: smaller penalty
}


# ── Agent states ──────────────────────────────────────────────────────────────

class AgentState(Enum):
    INITIALISING    = "INITIALISING"
    MONITORING      = "MONITORING"
    ANALYSING       = "ANALYSING"
    ACTING          = "ACTING"
    ESCALATING      = "ESCALATING"
    PAUSED          = "PAUSED"
    TERMINATED      = "TERMINATED"


# ── The autonomous tournament tracker ─────────────────────────────────────────

class AutonomousTournamentTracker:
    """
    Level 3 autonomous agent: tracks a tournament, computes NCSI per result,
    generates daily briefings, escalates significant signal moves.

    Operates continuously without human input.
    Humans review the daily briefing and act on escalation alerts.
    """

    def __init__(self):
        self.state           = AgentState.INITIALISING
        self.ncsi_map        = {}   # {token: cumulative_ncsi_delta}
        self.match_log       = []   # All processed matches
        self.token_exposure  = {}   # {token: [players from that club]}
        self.macro_modifier  = 1.00
        self.macro_phase     = "UNKNOWN"
        self.skill_stack     = None
        self.cycle_count     = 0
        self.start_time      = datetime.now(timezone.utc)

        # AUDIT LOG — Safety Principle 5: every action logged
        AUDIT_LOG_PATH.parent.mkdir(exist_ok=True)

    # ── Lifecycle ─────────────────────────────────────────────────────────────

    async def start(self):
        """Full autonomous agent lifecycle."""
        await self._initialise()

        log.info(f"Autonomous tracking started: {TOURNAMENT_NAME}")
        log.info("Autonomy Level 3: acts immediately, humans review daily briefing")
        log.info(f"Audit log: {AUDIT_LOG_PATH}")

        while self.state not in (AgentState.PAUSED, AgentState.TERMINATED):
            await self._run_cycle()

    async def _initialise(self):
        self._transition(AgentState.INITIALISING)
        log.info(f"Initialising tournament tracker: {TOURNAMENT_NAME}")

        # Load macro state
        await self._refresh_macro()

        # Load football intelligence stack
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"{SPORTMIND_API}/stack",
                    params={"sport": TOURNAMENT_SPORT, "use_case": "fan_token_tier1"}
                ) as r:
                    data       = await r.json()
                    self.skill_stack = data.get("stack", [])
        except Exception as e:
            log.warning(f"Skill stack unavailable ({e}) — using degraded mode")
            self.skill_stack = []

        # Build token exposure map
        for nation, players in NATIONS_DATA.items():
            for player in players:
                token = player.get("club_token")
                if token:
                    if token not in self.token_exposure:
                        self.token_exposure[token] = []
                    self.token_exposure[token].append({
                        "nation": nation,
                        "player": player["player"],
                        "atm":    player["atm"]
                    })

        log.info(f"Tracking {len(self.token_exposure)} tokens across {len(NATIONS_DATA)} nations")
        self._audit("initialised", {"tokens": list(self.token_exposure.keys())})
        self._transition(AgentState.MONITORING)

    # ── Main cycle ────────────────────────────────────────────────────────────

    async def _run_cycle(self):
        """
        Monitoring cycle: checks for new match results and processes them.
        In production: poll your match data API here.
        """
        self.cycle_count += 1
        self._transition(AgentState.MONITORING)

        # Refresh macro if stale
        if self.cycle_count % 24 == 0:  # Every ~24 cycles (~6h at 15min intervals)
            await self._refresh_macro()

        # Poll for new match results
        # REPLACE with your live match data source:
        # e.g. football-data.org, Sportradar, UEFA API
        new_results = await self._poll_match_results()

        for result in new_results:
            self._transition(AgentState.ANALYSING)
            ncsi_updates = self._compute_ncsi(result)

            self._transition(AgentState.ACTING)
            await self._apply_ncsi_updates(ncsi_updates, result)

        # Generate daily briefing at midnight UTC
        if datetime.now(timezone.utc).hour == 0 and self.cycle_count % 96 == 0:
            await self._generate_daily_briefing()

        # Sleep 15 minutes between cycles
        await asyncio.sleep(900)

    # ── NCSI computation ──────────────────────────────────────────────────────

    def _compute_ncsi(self, match: dict) -> dict:
        """
        Compute NCSI deltas for all affected tokens after a match result.
        Implements market/international-football-cycle.md NCSI weight model.

        Returns: {token: delta}
        """
        stage        = match.get("stage", "group_stage")
        ncsi_weight  = NCSI_STAGE_WEIGHTS.get(stage, 1.00)
        winner       = match.get("winner")
        loser        = match.get("loser")
        is_knockout  = stage not in ("group_stage",)

        updates = {}

        # Positive NCSI: winning nation's players' club tokens
        if winner:
            for player in NATIONS_DATA.get(winner, []):
                token = player.get("club_token")
                if not token: continue
                delta = ncsi_weight * player["atm"] * self.macro_modifier
                updates[token] = updates.get(token, 0) + delta

        # Negative NCSI: eliminated nation's players' club tokens
        if loser and is_knockout:
            penalty = NCSI_ELIMINATION_PENALTIES.get(stage, -0.05)
            for player in NATIONS_DATA.get(loser, []):
                token = player.get("club_token")
                if not token: continue
                delta = penalty * player["atm"]
                updates[token] = updates.get(token, 0) + delta

        return updates

    # ── Applying updates ──────────────────────────────────────────────────────

    async def _apply_ncsi_updates(self, updates: dict, match: dict):
        """
        Apply NCSI updates and escalate significant moves.
        Level 3 autonomy: applies immediately, escalates significant moves.
        """
        significant_moves = []

        for token, delta in updates.items():
            old_ncsi = self.ncsi_map.get(token, 0.0)
            new_ncsi = old_ncsi + delta
            self.ncsi_map[token] = round(new_ncsi, 4)

            log.info(
                f"[{token}] NCSI {old_ncsi:+.3f} → {new_ncsi:+.3f} "
                f"(delta: {delta:+.3f}) | {match.get('match_name', '')}"
            )

            # AUDIT: Safety Principle 5 — every action logged
            self._audit("ncsi_update", {
                "token": token, "delta": delta, "cumulative": new_ncsi,
                "match": match.get("match_id"), "stage": match.get("stage")
            })

            # Significant move: escalate to operator
            if abs(delta) > 0.15:
                significant_moves.append((token, delta, new_ncsi))

        # Log match
        self.match_log.append({
            "match":      match,
            "updates":    updates,
            "processed":  datetime.now(timezone.utc).isoformat()
        })

        # Escalate significant moves
        for token, delta, cumulative in significant_moves:
            await self._escalate_significant_move(token, delta, cumulative, match)

    # ── Escalation ────────────────────────────────────────────────────────────

    async def _escalate_significant_move(self, token: str, delta: float,
                                          cumulative: float, match: dict):
        """
        Significant NCSI move: alert operator.
        Safety Principle 4: full reasoning trail provided.
        """
        self._transition(AgentState.ESCALATING)

        direction = "📈" if delta > 0 else "📉"
        message   = (
            f"{direction} SIGNIFICANT NCSI MOVE: {token}\n"
            f"Match: {match.get('match_name', 'Unknown')}\n"
            f"Stage: {match.get('stage', 'Unknown')}\n"
            f"Delta: {delta:+.3f} | Cumulative: {cumulative:+.3f}\n"
            f"Macro: {self.macro_phase} ({self.macro_modifier})\n"
            f"Players contributing: "
            f"{[p['player'] for p in self.token_exposure.get(token, [])]}"
        )

        log.warning(f"ESCALATE: {message}")
        self._audit("escalation", {"token": token, "delta": delta, "match": match})

        if ALERT_WEBHOOK:
            try:
                async with aiohttp.ClientSession() as session:
                    await session.post(ALERT_WEBHOOK, json={"text": message})
            except Exception as e:
                log.error(f"Alert failed: {e}")
                # Graceful degradation — escalation failure never stops agent

        self._transition(AgentState.MONITORING)

    # ── Daily briefing ────────────────────────────────────────────────────────

    async def _generate_daily_briefing(self):
        """
        Generate daily intelligence briefing.
        Level 3 autonomy: generated automatically; humans read it asynchronously.
        """
        now       = datetime.now(timezone.utc)
        top_gainers = sorted(self.ncsi_map.items(), key=lambda x: x[1], reverse=True)[:5]
        top_losers  = sorted(self.ncsi_map.items(), key=lambda x: x[1])[:5]

        briefing = f"""# SportMind Tournament Intelligence Briefing
**{TOURNAMENT_NAME}**
Generated: {now.strftime("%Y-%m-%d %H:%M UTC")}
Matches processed: {len(self.match_log)}
Agent uptime: {(now - self.start_time).days} days

## Macro Context
Phase: {self.macro_phase} | Modifier: {self.macro_modifier}

## NCSI Leaders (Positive)
{chr(10).join(f"- **{t}**: {v:+.3f}" for t,v in top_gainers if v > 0)}

## NCSI Laggards (Negative)
{chr(10).join(f"- **{t}**: {v:+.3f}" for t,v in top_losers if v < 0)}

## All Token NCSI
{chr(10).join(f"| {t} | {v:+.4f} |" for t,v in sorted(self.ncsi_map.items()))}

## Recent Matches
{chr(10).join(f"- {m['match'].get('match_name','?')} ({m['match'].get('stage','?')})"
              for m in self.match_log[-10:])}

---
*Autonomous generation by SportMind Tournament Tracker (Level 3)*
*See tournament_audit_log.jsonl for full decision trail*
"""

        BRIEFING_PATH.write_text(briefing)
        log.info(f"Daily briefing written to {BRIEFING_PATH}")
        self._audit("daily_briefing", {"path": str(BRIEFING_PATH)})

    # ── Infrastructure ────────────────────────────────────────────────────────

    async def _poll_match_results(self) -> list:
        """
        Poll for new match results.
        REPLACE with your live data source.

        Example APIs:
          football-data.org — free tier available
          Sportradar — professional sports data
          UEFA official API — for UEFA competitions
          Your own database of tracked results
        """
        # Stub: returns empty list (replace with live source)
        # async with aiohttp.ClientSession() as session:
        #     async with session.get(
        #         f"https://api.football-data.org/v4/competitions/{TOURNAMENT_ID}/matches",
        #         headers={"X-Auth-Token": os.environ.get("FOOTBALL_DATA_KEY")}
        #     ) as r:
        #         data = await r.json()
        #         return [m for m in data["matches"] if m["status"] == "FINISHED"
        #                 and m["id"] not in self._processed_match_ids]
        return []

    async def _refresh_macro(self):
        try:
            async with aiohttp.ClientSession() as s:
                async with s.get(f"{SPORTMIND_API}/macro-state") as r:
                    data             = await r.json()
                    cycle            = data["macro_state"]["crypto_cycle"]
                    self.macro_modifier = cycle["macro_modifier"]
                    self.macro_phase    = cycle["phase"]
        except Exception as e:
            log.warning(f"Macro refresh failed — continuing with last known: {e}")

    def _transition(self, new_state: AgentState):
        if new_state != self.state:
            log.debug(f"State: {self.state.value} → {new_state.value}")
            self.state = new_state

    def _audit(self, event_type: str, data: dict):
        """
        Safety Principle 5: every action written to audit log.
        JSONL format: one JSON object per line, easy to tail/grep.
        """
        entry = {
            "timestamp":  datetime.now(timezone.utc).isoformat(),
            "agent":      "tournament-tracker",
            "tournament": TOURNAMENT_ID,
            "event_type": event_type,
            "state":      self.state.value,
            "cycle":      self.cycle_count,
            **data
        }
        with open(AUDIT_LOG_PATH, "a") as f:
            f.write(json.dumps(entry) + "\n")

    def get_status(self) -> dict:
        """Observable state for sportmind_agent_status MCP tool."""
        now = datetime.now(timezone.utc)
        return {
            "agent_id":        "tournament-tracker-001",
            "agent_type":      "tournament_tracker",
            "state":           self.state.value,
            "autonomy_level":  3,
            "health":          "HEALTHY",
            "uptime_hours":    round((now - self.start_time).total_seconds() / 3600, 1),
            "cycles":          self.cycle_count,
            "matches_tracked": len(self.match_log),
            "tokens_monitored": len(self.ncsi_map),
            "macro_modifier":  self.macro_modifier,
            "macro_phase":     self.macro_phase,
            "top_ncsi": dict(sorted(self.ncsi_map.items(),
                                    key=lambda x: x[1], reverse=True)[:3])
        }


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    tracker = AutonomousTournamentTracker()

    print(f"Starting autonomous tracker: {TOURNAMENT_NAME}")
    print(f"Autonomy Level 3 — no human input required")
    print(f"Audit log: {AUDIT_LOG_PATH}")
    print(f"Daily briefing: {BRIEFING_PATH}")
    print()

    asyncio.run(tracker.start())

# ── Extending this for other tournaments ─────────────────────────────────────
# World Cup 2026:
#   TOURNAMENT_ID   = "wc-2026"
#   NATIONS_DATA    = include all 48 qualified nations + their token mappings
#   NCSI weights are the same (WC Final = 2.00; no Euros ×1.10 bonus)
#
# PSL 2027:
#   TOURNAMENT_SPORT = "cricket"
#   Import cricket NCSI weights from market/international-cricket-cycle.md
#   IPL auction signal: add auction result handler to _apply_ncsi_updates
#
# NBA Playoffs:
#   TOURNAMENT_SPORT = "basketball"
#   Stage weights differ: series Game 7 > Game 1-6
#   Import star player ATM tiers from athlete/nba/athlete-intel-nba.md
#
# See: core/autonomous-agent-framework.md for the full agent model
# See: examples/agentic-workflows/multi-agent-coordination.md to connect
#      this tracker to a portfolio monitor and pre-match chain
