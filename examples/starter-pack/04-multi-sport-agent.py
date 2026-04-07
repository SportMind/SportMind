#!/usr/bin/env python3
"""
SportMind Starter Pack — Example 04: Multi-Sport Agent
=======================================================
A portfolio agent monitoring football, cricket, and MMA simultaneously.

What this demonstrates:
  - Sport routing (different reasoning per sport)
  - Format-first rule for cricket (T20 vs ODI vs Test)
  - MMA weigh-in protocol (check before match analysis)
  - Football lineup window (T-2h critical)
  - Level 2 autonomy across multiple sports
  - Per-sport modifier application

What you need:
  pip install aiohttp
  python scripts/sportmind_api.py   # in another terminal

What to change first:
  PORTFOLIO   — your tokens and sports
  MIN_SMS     — confidence threshold
  CYCLE_HOURS — monitoring frequency

Key insight — why sports need different reasoning:
  Cricket: format (T20/ODI/Test) changes the ENTIRE signal model. Check first.
  MMA:     weigh-in result supersedes all other analysis. Always check.
  Football: lineup at T-2h is critical. Set lineup_unconfirmed until confirmed.
  F1:      qualifying delta is the primary variable. Load before form data.
"""

import asyncio
import logging
import os
from datetime import datetime, timezone

import aiohttp

SPORTMIND_API = os.environ.get("SPORTMIND_API", "http://localhost:8080")
CYCLE_HOURS   = 4
MIN_SMS       = 60.0

# Your token portfolio — add or remove entries
PORTFOLIO = [
    {"token": "PSG",  "sport": "football", "club": "PSG"},
    {"token": "BAR",  "sport": "football", "club": "FC Barcelona"},
    {"token": "CITY", "sport": "football", "club": "Manchester City"},
    # Cricket tokens (PSL active; IPL when regulatory clarity arrives)
    {"token": "LAH",  "sport": "cricket",  "club": "Lahore Qalandars"},
]

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("sportmind.multi-sport")


class MultiSportAgent:
    """
    Portfolio monitoring agent covering multiple sports.
    Routes each event to the correct sport-specific reasoning.
    """

    def __init__(self):
        self.macro_modifier  = 1.00
        self.macro_phase     = "UNKNOWN"
        self.skill_stacks    = {}   # {sport: stack}
        self.cycle_count     = 0

    async def initialise(self):
        log.info(f"Initialising multi-sport agent. Portfolio: {len(PORTFOLIO)} tokens")

        # Load macro state
        await self._refresh_macro()

        # Load skill stacks for each sport (Tier 0 — permanent, load once)
        sports = set(p["sport"] for p in PORTFOLIO)
        for sport in sports:
            await self._load_stack(sport)

        log.info(f"Ready. Sports covered: {sorted(sports)}")

    async def _load_stack(self, sport: str):
        try:
            async with aiohttp.ClientSession() as s:
                async with s.get(
                    f"{SPORTMIND_API}/stack",
                    params={"sport": sport, "use_case": "fan_token_tier1"}
                ) as r:
                    data = await r.json()
                    self.skill_stacks[sport] = data.get("stack", [])
                    log.info(f"Loaded {len(self.skill_stacks[sport])} files for {sport}")
        except Exception as e:
            log.error(f"Stack load failed for {sport}: {e}")
            self.skill_stacks[sport] = []

    # ── Main cycle ────────────────────────────────────────────────────────────

    async def run_cycle(self):
        self.cycle_count += 1
        log.info(f"── Cycle {self.cycle_count} | Macro: {self.macro_phase} ──")

        if self._macro_is_stale():
            await self._refresh_macro()

        # Process each portfolio item
        for item in PORTFOLIO:
            events = await self._get_events(item)
            for event in events:
                await self._route_event(item, event)

    # ── Sport routing — the key function in this example ─────────────────────

    async def _route_event(self, portfolio_item: dict, event: dict):
        """
        Route event to the correct sport-specific reasoning.

        This is where multi-sport intelligence works differently from
        loading a single sport — each sport has different primary variables
        and different sequencing rules.
        """
        sport    = portfolio_item["sport"]
        event_id = event.get("event_id", "unknown")

        log.info(f"[{event_id}] Routing — sport: {sport}")

        if sport == "football":
            signal = await self._analyse_football(portfolio_item, event)

        elif sport == "cricket":
            signal = await self._analyse_cricket(portfolio_item, event)

        elif sport == "mma":
            signal = await self._analyse_mma(portfolio_item, event)

        elif sport == "formula1":
            signal = await self._analyse_f1(portfolio_item, event)

        elif sport == "basketball":
            signal = await self._analyse_basketball(portfolio_item, event)

        else:
            # Generic: use base signal without sport-specific modifiers
            signal = await self._analyse_generic(portfolio_item, event)

        # Common: apply autonomy decision
        self._apply_autonomy_decision(signal, event)

    # ── Sport-specific analysis functions ─────────────────────────────────────

    async def _analyse_football(self, item: dict, event: dict) -> dict:
        """
        Football analysis.
        Key rules:
          1. Competition tier (UCL > domestic league) is primary weight
          2. Lineup_unconfirmed until T-2h
          3. Derby: apply form compression if applicable
        See: sports/football/sport-domain-football.md
        """
        hours_away        = event.get("hours_away", 999)
        lineup_unconfirmed = hours_away > 2

        competition_weights = {
            "ucl_final": 1.00, "ucl_knockout": 0.75,
            "ucl_group": 0.55, "league_decider": 0.65,
            "league_standard": 0.35, "cup": 0.50
        }
        comp_weight = competition_weights.get(event.get("competition", "league_standard"), 0.35)

        # Derby check
        is_derby    = event.get("is_derby", False)
        form_discount = 0.40 if is_derby else 0.00  # 40% form compression for derbies

        signal = self._build_signal(
            item       = item,
            event      = event,
            modifiers  = {
                "competition_weight":   comp_weight,
                "lineup_unconfirmed":   lineup_unconfirmed,
                "derby_form_discount":  form_discount,
                "macro_modifier":       self.macro_modifier
            }
        )

        if lineup_unconfirmed:
            signal["flags"]["lineup_unconfirmed"] = True
            signal["flags"]["position_size"] = "50%"
            log.info(f"[{item['token']}] Lineup unconfirmed — 50% position size")

        if is_derby:
            log.info(f"[{item['token']}] Derby detected — 40% form compression applied")

        return signal

    async def _analyse_cricket(self, item: dict, event: dict) -> dict:
        """
        Cricket analysis.
        KEY RULE: FORMAT FIRST. T20 / ODI / Test have completely different models.
        Never apply T20 analysis to a Test match.
        See: sports/cricket/sport-domain-cricket.md
        """
        format_type = event.get("format", "T20")  # ALWAYS check format first

        # Format-specific signal weights
        format_weights = {
            "T20":  {"token_impact": 1.00, "signal_speed": "FAST"},
            "ODI":  {"token_impact": 0.75, "signal_speed": "MODERATE"},
            "Test": {"token_impact": 0.40, "signal_speed": "SLOW"}
        }
        fmt = format_weights.get(format_type, format_weights["T20"])

        # India premium check
        teams       = [event.get("home_team",""), event.get("away_team","")]
        india_match = "India" in teams
        ind_pak     = "India" in teams and "Pakistan" in teams

        india_modifier   = 2.00 if ind_pak else (1.40 if india_match else 1.00)
        if india_modifier > 1.00:
            log.info(f"[{item['token']}] India premium applied: ×{india_modifier}")

        # Dew factor check for evening T20s in South Asia
        dew_risk     = event.get("dew_risk", "LOW")
        dew_modifier = {"LOW": 1.00, "MODERATE": 1.05, "HIGH": 1.08, "VERY_HIGH": 1.12}
        dew_mod      = dew_modifier.get(dew_risk, 1.00)
        if dew_mod > 1.00:
            log.info(f"[{item['token']}] Dew factor ({dew_risk}): ×{dew_mod} for batting-second team")

        return self._build_signal(
            item      = item,
            event     = event,
            modifiers = {
                "format":          format_type,
                "format_weight":   fmt["token_impact"],
                "india_modifier":  india_modifier,
                "dew_modifier":    dew_mod,
                "macro_modifier":  self.macro_modifier
            }
        )

    async def _analyse_mma(self, item: dict, event: dict) -> dict:
        """
        MMA analysis.
        KEY RULE: WEIGH-IN FIRST. Weight miss supersedes ALL other analysis.
        If a fighter misses weight, reload analysis from scratch with weight_miss flag.
        See: sports/mma/sport-domain-mma.md
        """
        weigh_in_result = event.get("weigh_in_result", "PENDING")

        if weigh_in_result == "MISS":
            # Weight miss: apply ×0.72 modifier for missing fighter
            log.warning(f"[{item['token']}] WEIGHT MISS — reloading analysis")
            return self._build_signal(
                item      = item,
                event     = event,
                modifiers = {
                    "weight_miss_modifier": 0.72,
                    "weight_miss_active":   True,
                    "confidence_reduction": True,
                    "macro_modifier":       self.macro_modifier
                }
            )

        # Clean weigh-in: standard analysis
        is_title_fight    = event.get("is_title_fight", False)
        title_modifier    = 1.35 if is_title_fight else 1.00

        return self._build_signal(
            item      = item,
            event     = event,
            modifiers = {
                "title_modifier":    title_modifier,
                "weigh_in_result":   weigh_in_result,
                "macro_modifier":    self.macro_modifier
            }
        )

    async def _analyse_f1(self, item: dict, event: dict) -> dict:
        """
        Formula 1 analysis.
        PRIMARY VARIABLE: Qualifying delta — most predictive single F1 variable.
        Weather override: rain probability > 40% → hardware tier reset.
        See: sports/formula1/sport-domain-formula1.md
        """
        qualifying_delta = event.get("qualifying_delta_seconds", 0.0)
        rain_probability = event.get("rain_probability", 0.0)
        hardware_tier    = event.get("hardware_tier", 2)  # 1=champion, 4=backmarker

        # Weather override
        if rain_probability > 0.40:
            log.info(f"[{item['token']}] Wet race signal: hardware tier reset")
            hardware_modifier = 0.75  # Reduced in wet — specialist overrides tier
        else:
            hardware_modifiers = {1: 1.15, 2: 1.05, 3: 1.00, 4: 0.88}
            hardware_modifier  = hardware_modifiers.get(hardware_tier, 1.00)

        # Qualifying delta modifier
        if qualifying_delta >= 0.3:
            qual_modifier = 1.15  # Strong pole advantage
        elif qualifying_delta >= 0.1:
            qual_modifier = 1.05
        else:
            qual_modifier = 1.00

        return self._build_signal(
            item      = item,
            event     = event,
            modifiers = {
                "qualifying_delta":   qualifying_delta,
                "qual_modifier":      qual_modifier,
                "hardware_modifier":  hardware_modifier,
                "rain_probability":   rain_probability,
                "macro_modifier":     self.macro_modifier
            }
        )

    async def _analyse_basketball(self, item: dict, event: dict) -> dict:
        """
        NBA/Basketball analysis.
        STAR PLAYER: dominant variable. DNP-rest → ×0.70 modifier.
        Back-to-back: second game → automatic flag.
        See: sports/basketball/sport-domain-basketball.md
        """
        star_available = event.get("star_player_available", True)
        is_b2b_second  = event.get("back_to_back_second", False)
        net_rating_diff = event.get("on_off_net_rating_diff", 0.0)

        star_modifier = 1.05 if star_available else 0.70
        b2b_modifier  = 0.88 if is_b2b_second else 1.00
        rating_modifier = min(1.20, 1.00 + (net_rating_diff / 100))

        if not star_available:
            log.warning(f"[{item['token']}] Star player DNP — signal strongly negative")

        return self._build_signal(
            item      = item,
            event     = event,
            modifiers = {
                "star_modifier":    star_modifier,
                "b2b_modifier":     b2b_modifier,
                "rating_modifier":  rating_modifier,
                "macro_modifier":   self.macro_modifier
            }
        )

    async def _analyse_generic(self, item: dict, event: dict) -> dict:
        """Generic analysis for any sport not specifically handled above."""
        return self._build_signal(
            item=item, event=event,
            modifiers={"macro_modifier": self.macro_modifier}
        )

    # ── Signal builder ────────────────────────────────────────────────────────

    def _build_signal(self, item: dict, event: dict, modifiers: dict) -> dict:
        """Build the standard confidence output from modifiers."""
        stack  = self.skill_stacks.get(item["sport"], [])
        layers = set()
        for skill in stack:
            p = skill.get("skill_id","")
            if p.startswith("macro"):       layers.add(5)
            elif p.startswith("market"):    layers.add(4)
            elif p.startswith("sports"):    layers.add(1)
            elif p.startswith("athlete"):   layers.add(2)
            elif p.startswith("fan-token"): layers.add(3)

        macro_mod = modifiers.get("macro_modifier", 1.00)
        sms = round(
            (len(layers)/5)*0.35*100 +
            (1.0 if macro_mod >= 0.75 else 0.6)*0.25*100 +
            0.25*100 + min(macro_mod,1.0)*0.15*100, 1
        )

        return {
            "token":      item["token"],
            "sport":      item["sport"],
            "event_id":   event.get("event_id",""),
            "sms":        sms,
            "sms_tier":   "GOOD" if sms >= 60 else "PARTIAL",
            "modifiers":  modifiers,
            "flags":      {"macro_override_active": macro_mod < 0.75},
            "action":     "ENTER" if sms >= MIN_SMS and macro_mod >= 0.75 else "WAIT",
            "generated_at": datetime.now(timezone.utc).isoformat()
        }

    # ── Autonomy ──────────────────────────────────────────────────────────────

    def _apply_autonomy_decision(self, signal: dict, event: dict):
        """Apply autonomy decision and log outcome."""
        sms    = signal["sms"]
        action = signal["action"]
        token  = signal["token"]
        sport  = signal["sport"]

        if signal["flags"].get("macro_override_active"):
            log.warning(f"[{token}/{sport}] ESCALATE — macro override active")
        elif sms < MIN_SMS:
            log.warning(f"[{token}/{sport}] ESCALATE — SMS {sms} < {MIN_SMS}")
        else:
            log.info(f"[{token}/{sport}] {action} | SMS {sms} | Macro {self.macro_phase}")

    # ── Infrastructure ────────────────────────────────────────────────────────

    async def _get_events(self, portfolio_item: dict) -> list:
        """Get upcoming events for a portfolio item. Replace with live fixture data."""
        # REPLACE with your fixture data source
        return []

    async def _refresh_macro(self):
        try:
            async with aiohttp.ClientSession() as s:
                async with s.get(f"{SPORTMIND_API}/macro-state") as r:
                    data = await r.json()
                    cycle = data["macro_state"]["crypto_cycle"]
                    self.macro_modifier = cycle["macro_modifier"]
                    self.macro_phase    = cycle["phase"]
        except Exception as e:
            log.error(f"Macro refresh failed: {e}")

    def _macro_is_stale(self) -> bool:
        return self.cycle_count % 2 == 0  # Refresh every other cycle (~8h)

    # ── Main loop ─────────────────────────────────────────────────────────────

    async def run(self):
        await self.initialise()
        log.info("Multi-sport agent running.")
        while True:
            try:
                await self.run_cycle()
            except Exception as e:
                log.error(f"Cycle error: {e}")
            await asyncio.sleep(CYCLE_HOURS * 3600)


if __name__ == "__main__":
    asyncio.run(MultiSportAgent().run())

# ── See also ──────────────────────────────────────────────────────────────────
# 05-sportfi-kit-integration.py — connecting this agent to SportFi Kit
# 06-autonomous-tournament-tracker.py — full autonomous operation
# core/reasoning-patterns.md — sport-specific chain variations (Section 4)
