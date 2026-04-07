#!/usr/bin/env python3
"""
SportMind Starter Pack — Example 03: Single Sport Agent
========================================================
A complete football fan token monitoring agent for $PSG.

What this demonstrates:
  - Subclassing SportMindAgent base class
  - Level 2 autonomy (acts when SMS ≥ 80, escalates otherwise)
  - Scheduled 4-hour monitoring cycle
  - Alert generation with full reasoning trail
  - Graceful degradation when data is unavailable

What you need:
  pip install aiohttp schedule
  python scripts/sportmind_api.py   # in another terminal

What to change first:
  TOKEN_SYMBOL  — change to your token ($BAR, $CITY, $JUV, etc.)
  SPORT         — change to your sport
  MIN_SMS       — your confidence threshold (default: 60)
  ALERT_WEBHOOK — your notification endpoint

This agent:
  - Checks macro state every 4 hours
  - Detects upcoming football matches involving PSG
  - Generates pre-match signals at T-48h and T-2h
  - Alerts when signal meets threshold
  - Escalates when confidence is insufficient
"""

import asyncio
import json
import logging
import os
from datetime import datetime, timezone, timedelta

import aiohttp

# ── Configuration ─────────────────────────────────────────────────────────────

TOKEN_SYMBOL    = "PSG"
SPORT           = "football"
CLUB_NAME       = "Paris Saint-Germain"
USE_CASE        = "fan_token_tier1"
SPORTMIND_API   = os.environ.get("SPORTMIND_API", "http://localhost:8080")
ALERT_WEBHOOK   = os.environ.get("ALERT_WEBHOOK", "")
MIN_SMS         = 60.0          # Minimum SMS to recommend ENTER
CYCLE_HOURS     = 4             # How often to run the monitoring cycle
AUTONOMY_LEVEL  = 2             # Level 2: acts at SMS ≥ MIN_SMS, escalates otherwise

logging.basicConfig(
    level   = logging.INFO,
    format  = "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
)
log = logging.getLogger(f"sportmind.{TOKEN_SYMBOL.lower()}-agent")


# ── The agent ─────────────────────────────────────────────────────────────────

class PSGTokenAgent:
    """
    Single-sport SportMind agent monitoring $PSG fan token.
    Level 2 autonomy: generates recommendations autonomously; alerts operator.
    Does NOT execute trades or financial actions — see core/autonomous-agent-framework.md.
    """

    def __init__(self):
        self.macro_modifier     = 1.00
        self.macro_phase        = "UNKNOWN"
        self.macro_last_updated = None
        self.cycle_count        = 0
        self.alert_count        = 0
        self.skill_stack        = None

    # ── Initialisation ────────────────────────────────────────────────────────

    async def initialise(self):
        log.info(f"Initialising {TOKEN_SYMBOL} agent (Level {AUTONOMY_LEVEL} autonomy)")

        # Step 1: Load skill stack (Tier 0 — permanent, load once)
        await self._load_skill_stack()

        # Step 2: Fetch initial macro state
        await self._refresh_macro()

        log.info(
            f"Initialised. Stack: {len(self.skill_stack or [])} files. "
            f"Macro: {self.macro_phase} ({self.macro_modifier})"
        )

    async def _load_skill_stack(self):
        """Load SportMind skill stack. Permanent content — load once per session."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"{SPORTMIND_API}/stack",
                    params={"sport": SPORT, "use_case": USE_CASE}
                ) as r:
                    data = await r.json()
                    self.skill_stack = data.get("stack", [])
                    log.info(f"Loaded {len(self.skill_stack)} skill files")
        except Exception as e:
            log.error(f"Could not load skill stack: {e}")
            self.skill_stack = []

    # ── Monitoring cycle ──────────────────────────────────────────────────────

    async def run_cycle(self):
        """Main monitoring cycle — runs every CYCLE_HOURS hours."""
        self.cycle_count += 1
        log.info(f"── Cycle {self.cycle_count} ──────────────────────")

        # Step 1: Refresh macro if stale (Tier 3 — daily)
        if self._macro_is_stale():
            await self._refresh_macro()

        # Step 2: Check for upcoming PSG matches
        events = await self._get_upcoming_events()

        for event in events:
            await self._process_event(event)

        log.info(f"Cycle {self.cycle_count} complete. Macro: {self.macro_phase}")

    async def _get_upcoming_events(self) -> list:
        """
        Detect upcoming events for this club.
        In production: call your sports data API here.
        This stub returns a simulated upcoming event for demonstration.
        """
        # REPLACE THIS with your live fixture data source:
        # e.g. football-data.org, Sportradar, your own database
        #
        # async with aiohttp.ClientSession() as session:
        #     async with session.get(f"https://your-api/fixtures?team={CLUB_NAME}") as r:
        #         fixtures = await r.json()
        #         return [f for f in fixtures if 0 < f["hours_away"] < 72]

        # Stub: simulated UCL match in 46 hours
        return [
            {
                "event_id":   "ucl-qf-psg-arsenal-2026",
                "home_team":  "PSG",
                "away_team":  "Arsenal",
                "hours_away": 46,
                "competition": "ucl_knockout",
                "competition_tier": "TIER_1"
            }
        ]

    async def _process_event(self, event: dict):
        """Process a single upcoming event through the SportMind reasoning chain."""
        event_id   = event["event_id"]
        hours_away = event["hours_away"]
        tier       = event.get("competition_tier", "TIER_3")

        # Determine which analysis window we are in
        if hours_away <= 2:
            window = "T-2h"
        elif hours_away <= 48:
            window = "T-48h"
        else:
            return  # Too far away; skip

        log.info(f"[{event_id}] Processing {window} signal (Tier: {tier})")

        # Generate signal
        signal = await self._generate_signal(event, window)

        # Apply autonomy decision
        sms    = signal["sportmind_score"]["sms"]
        action = signal["signal"]["recommended_action"]

        if self._should_act(signal):
            await self._send_alert(signal, event, window)
            self.alert_count += 1
        else:
            await self._escalate(signal, event, window,
                                  reason=f"SMS {sms} below threshold {MIN_SMS}")

    # ── Signal generation ─────────────────────────────────────────────────────

    async def _generate_signal(self, event: dict, window: str) -> dict:
        """
        Generate SportMind signal using the six-step reasoning chain.
        See core/reasoning-patterns.md for the full chain specification.
        """

        # STEP 1: Macro already loaded — apply modifier
        # STEP 2: Competition classification
        comp_weights = {
            "ucl_final": 1.00, "ucl_knockout": 0.75,
            "league_decider": 0.65, "league_standard": 0.35,
            "domestic_cup": 0.50
        }
        comp_weight = comp_weights.get(event.get("competition"), 0.35)

        # STEP 3: Athlete availability
        lineup_unconfirmed = event["hours_away"] > 2

        # STEP 4: Signal computation
        base_score       = 55.0  # Replace with your form model
        adjusted_score   = round(base_score * self.macro_modifier * comp_weight / 0.35, 1)
        adjusted_score   = min(adjusted_score, 100.0)

        # STEP 5: DeFi context (if fan token application)
        # See platform/realtime-integration-patterns.md Pattern 3 for live TVL fetch
        liquidity_warning = False  # Replace with live TVL check

        # STEP 6: SMS computation
        layers = set()
        for skill in (self.skill_stack or []):
            p = skill.get("skill_id", "")
            if p.startswith("macro"):       layers.add(5)
            elif p.startswith("market"):    layers.add(4)
            elif p.startswith("sports"):    layers.add(1)
            elif p.startswith("athlete"):   layers.add(2)
            elif p.startswith("fan-token"): layers.add(3)

        sms = round(
            (len(layers)/5) * 0.35 * 100 +
            (1.0 if self.macro_modifier >= 0.75 else 0.6) * 0.25 * 100 +
            0.25 * 100 +
            min(self.macro_modifier, 1.0) * 0.15 * 100, 1
        )
        sms_tier = (
            "HIGH_QUALITY" if sms >= 80 else "GOOD" if sms >= 60
            else "PARTIAL" if sms >= 40 else "INSUFFICIENT"
        )

        flags = {
            "lineup_unconfirmed":    lineup_unconfirmed,
            "macro_override_active": self.macro_modifier < 0.75,
            "liquidity_warning":     liquidity_warning
        }

        # Position size recommendation
        if any(flags.values()):
            position_size = "50%"
        elif sms >= 80:
            position_size = "100%"
        elif sms >= 60:
            position_size = "65%"
        else:
            position_size = "WAIT"

        return {
            "event_id":    event["event_id"],
            "window":      window,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "signal": {
                "direction":          "HOME" if event["home_team"] == CLUB_NAME else "AWAY",
                "adjusted_score":     adjusted_score,
                "confidence_tier":    "MEDIUM" if sms >= 60 else "LOW",
                "recommended_action": "ENTER" if sms >= MIN_SMS and not flags["macro_override_active"] else "WAIT",
                "position_size":      position_size
            },
            "sportmind_score": {
                "sms": sms, "sms_tier": sms_tier,
                "layers_loaded": sorted(layers)
            },
            "modifiers": {
                "macro_modifier":    self.macro_modifier,
                "comp_weight":       comp_weight,
                "composite":         round(self.macro_modifier * comp_weight, 3),
                "flags":             flags
            },
            "token": TOKEN_SYMBOL,
            "agent_note": (
                "SportMind intelligence — not financial advice. "
                "Integrate live lineup and form data for full accuracy."
            )
        }

    # ── Autonomy decision ─────────────────────────────────────────────────────

    def _should_act(self, signal: dict) -> bool:
        """
        Level 2 autonomy decision: act autonomously or escalate?
        Implements the Autonomous Action Matrix from core/autonomous-agent-framework.md.
        """
        sms   = signal["sportmind_score"]["sms"]
        flags = signal["modifiers"]["flags"]

        # Blocking flags are absolute — see Safety Principle 3
        if flags.get("macro_override_active"): return False
        if flags.get("liquidity_critical"):    return False

        # Confidence threshold
        return sms >= MIN_SMS

    # ── Actions ───────────────────────────────────────────────────────────────

    async def _send_alert(self, signal: dict, event: dict, window: str):
        """Send alert to operator. DOES NOT execute any financial action."""
        sms    = signal["sportmind_score"]["sms"]
        action = signal["signal"]["recommended_action"]

        message = (
            f"📊 {TOKEN_SYMBOL} SIGNAL [{window}]\n"
            f"Event: {event['home_team']} vs {event['away_team']}\n"
            f"Action: {action} | SMS: {sms} ({signal['sportmind_score']['sms_tier']})\n"
            f"Macro: {self.macro_phase} ({self.macro_modifier})\n"
            f"Position size: {signal['signal']['position_size']}\n"
            f"Flags: {[k for k,v in signal['modifiers']['flags'].items() if v]}"
        )

        log.info(f"ALERT: {message}")

        if ALERT_WEBHOOK:
            try:
                async with aiohttp.ClientSession() as session:
                    await session.post(ALERT_WEBHOOK, json={
                        "text": message, "signal": signal
                    })
            except Exception as e:
                log.error(f"Alert webhook failed: {e}")

    async def _escalate(self, signal: dict, event: dict, window: str, reason: str):
        """
        Escalate to human review — Safety Principle 4 (escalation completeness).
        Provides full reasoning trail, not just 'confidence too low'.
        """
        sms   = signal["sportmind_score"]["sms"]
        flags = signal["modifiers"]["flags"]

        escalation_brief = (
            f"⚠️ ESCALATION REQUIRED [{window}]\n"
            f"Event: {event['home_team']} vs {event['away_team']}\n"
            f"Reason: {reason}\n"
            f"SMS: {sms} | Macro: {self.macro_phase}\n"
            f"Active flags: {[k for k,v in flags.items() if v] or 'none'}\n"
            f"What would resolve this: "
            f"{'lineup confirmation at T-2h' if flags.get('lineup_unconfirmed') else ''}"
            f"{'macro improvement above 0.75' if flags.get('macro_override_active') else ''}"
            f"{'additional skill data' if sms < MIN_SMS else ''}"
        )

        log.warning(f"ESCALATE: {escalation_brief}")

        if ALERT_WEBHOOK:
            try:
                async with aiohttp.ClientSession() as session:
                    await session.post(ALERT_WEBHOOK, json={
                        "text": escalation_brief,
                        "type": "escalation",
                        "signal": signal
                    })
            except Exception as e:
                log.error(f"Escalation webhook failed: {e}")

    # ── Macro management ──────────────────────────────────────────────────────

    async def _refresh_macro(self):
        """Refresh macro state — Tier 3 (4-8 hour cycle)."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{SPORTMIND_API}/macro-state") as r:
                    data = await r.json()
                    cycle = data["macro_state"]["crypto_cycle"]
                    self.macro_modifier     = cycle["macro_modifier"]
                    self.macro_phase        = cycle["phase"]
                    self.macro_last_updated = datetime.now(timezone.utc)
                    log.info(f"Macro refreshed: {self.macro_phase} ({self.macro_modifier})")
        except Exception as e:
            log.error(f"Macro refresh failed — using last known state: {e}")
            # Graceful degradation: keep existing state, don't fail

    def _macro_is_stale(self) -> bool:
        """Macro state is stale if > 8 hours old — see core/temporal-awareness.md."""
        if not self.macro_last_updated: return True
        age = datetime.now(timezone.utc) - self.macro_last_updated
        return age > timedelta(hours=8)

    # ── Main loop ─────────────────────────────────────────────────────────────

    async def run(self):
        """Run the agent continuously."""
        await self.initialise()

        log.info(f"Agent running. Cycle: {CYCLE_HOURS}h. Min SMS: {MIN_SMS}")
        log.info("This agent generates intelligence alerts. It does NOT execute trades.")

        while True:
            try:
                await self.run_cycle()
            except Exception as e:
                log.error(f"Cycle error: {e}")
                # Errors never stop the agent — Safety Principle 6 (graceful degradation)

            await asyncio.sleep(CYCLE_HOURS * 3600)


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    agent = PSGTokenAgent()
    asyncio.run(agent.run())

# ── What to change to use this for a different token ─────────────────────────
# 1. TOKEN_SYMBOL = "BAR"  (or CITY, JUV, etc.)
# 2. SPORT = "football"    (same — all Socios football tokens)
# 3. CLUB_NAME = "FC Barcelona"
# 4. Replace _get_upcoming_events() with your fixture data source
# 5. Optionally add live lineup fetch before _generate_signal()
#    See platform/realtime-integration-patterns.md Pattern 2
#
# See 04-multi-sport-agent.py for monitoring multiple tokens/sports
