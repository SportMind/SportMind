# Agentic Workflow Pattern 6 — Athlete Commercial Tracker

**Continuously monitors the commercial signals of a portfolio of athletes,
tracking APS changes, AELS movements, transfer rumour progression, and
the commercial events that affect athlete brand value and fan token NCSI.**

This pattern is the commercial equivalent of the portfolio monitor — it watches
athletes as commercial assets, not just sporting performers.

---

## Why a dedicated athlete commercial tracker

The transfer window monitor (Pattern 4) tracks rumour-to-confirmation for specific
athletes. The portfolio monitor (Pattern 1) tracks fan token signals.

Neither tracks the *ongoing commercial health* of an athlete's brand — the social
health score trend, the sponsorship deal signals, the APS trajectory, the ATM
evolution as a career develops. An athlete's commercial value changes continuously:
a breakout tournament performance, a viral social moment, a disciplinary incident,
a national team call-up, a contract year announcement. Each of these shifts the
athlete's commercial profile in ways that affect both their individual value and
the NCSI they generate for club tokens.

---

## The Athlete Commercial Tracker agent

```python
# examples/agentic-workflows/athlete_commercial_tracker.py
"""
SportMind Athlete Commercial Tracker Agent
Pattern 6: Continuous athlete commercial intelligence.

Monitors: A portfolio of athletes across sports
Cycle: Every 12 hours (commercial signals change more slowly than match signals)
Autonomy: Level 1 (advisory — surfaces intelligence; human decides)
"""
import asyncio
import logging
import os
import json
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field
from typing import Optional
from pathlib import Path

import aiohttp

SPORTMIND_API = os.environ.get("SPORTMIND_API", "http://localhost:8080")
ALERT_WEBHOOK = os.environ.get("ALERT_WEBHOOK", "")
CYCLE_HOURS   = 12
AUDIT_LOG     = Path("athlete_commercial_audit.jsonl")

log = logging.getLogger("sportmind.athlete-commercial-tracker")


# ── Athlete commercial profile ────────────────────────────────────────────────

@dataclass
class AthleteCommercialProfile:
    """
    Current commercial state of a monitored athlete.
    Tracks changes over time for trend analysis.
    """
    athlete_id:      str
    name:            str
    sport:           str
    club:            str
    club_token:      Optional[str]
    national_team:   Optional[str]

    # Current commercial metrics (updated each cycle)
    aps:             float = 0.55   # Athlete Portability Score
    aels:            float = 0.45   # Athlete Engagement Lift Score
    abs_score:       float = 60.0   # Athlete Brand Score (0-100)
    shs:             float = 65.0   # Social Health Score
    dts:             float = 70.0   # Development Trajectory Score
    tai:             float = 70.0   # Training Adaptation Index (injury risk)

    # Contract state
    contract_years_remaining: float = 2.0
    pre_contract_eligible:    bool  = False
    release_clause_active:    bool  = False

    # Historical for trend detection
    aps_history:       list = field(default_factory=list)
    shs_history:       list = field(default_factory=list)
    alert_history:     list = field(default_factory=list)

    def update_metrics(self, new_metrics: dict):
        """Update metrics and record history for trend analysis."""
        # Record previous values before updating
        self.aps_history.append({"value": self.aps, "at": datetime.now(timezone.utc).isoformat()})
        self.shs_history.append({"value": self.shs, "at": datetime.now(timezone.utc).isoformat()})

        # Keep last 30 readings
        if len(self.aps_history) > 30: self.aps_history.pop(0)
        if len(self.shs_history) > 30: self.shs_history.pop(0)

        # Apply updates
        for key, value in new_metrics.items():
            if hasattr(self, key):
                setattr(self, key, value)

        # Auto-compute financial modifiers
        self.pre_contract_eligible = self.contract_years_remaining <= 0.5
        self.release_clause_active = getattr(self, '_release_clause', False)

    def aps_trend(self) -> str:
        """APS trend: RISING, STABLE, DECLINING."""
        if len(self.aps_history) < 3: return "INSUFFICIENT_DATA"
        recent  = [h["value"] for h in self.aps_history[-3:]]
        delta   = recent[-1] - recent[0]
        if delta > 0.05:   return "RISING"
        elif delta < -0.05: return "DECLINING"
        else:               return "STABLE"

    def shs_trend(self) -> str:
        """Social health trend."""
        if len(self.shs_history) < 3: return "INSUFFICIENT_DATA"
        recent = [h["value"] for h in self.shs_history[-3:]]
        delta  = recent[-1] - recent[0]
        if delta > 5:    return "IMPROVING"
        elif delta < -5: return "DECLINING"
        else:            return "STABLE"

    def financial_aps_adjusted(self) -> float:
        """
        APS adjusted for financial context.
        See core/athlete-financial-intelligence.md for full formula.
        """
        # Contract stage multiplier
        if self.pre_contract_eligible:
            contract_mult = 1.25
        elif self.contract_years_remaining <= 1.0:
            contract_mult = 1.15
        elif self.contract_years_remaining <= 2.0:
            contract_mult = 1.00
        else:
            contract_mult = 0.85  # Long contract; financial barrier higher

        # Release clause
        if self.release_clause_active:
            contract_mult = min(contract_mult * 1.20, 1.30)

        return round(self.aps * contract_mult, 3)

    def ncsi_potential(self, competition_weight: float = 1.00) -> float:
        """
        Estimated NCSI this athlete can generate for their club token.
        NCSI = competition_weight × ATM × macro_modifier
        ATM estimated from APS and AELS.
        """
        atm_estimate = (self.aps * 0.6) + (self.aels * 0.4)  # Simplified ATM
        return round(competition_weight * atm_estimate, 3)


# ── Commercial event detection ────────────────────────────────────────────────

class CommercialEventDetector:
    """
    Detects commercially significant events for a tracked athlete.
    Each event type has a defined signal impact.
    """

    EVENT_TYPES = {
        "aps_rising":          {"signal": "POSITIVE", "impact": "moderate", "ltui": "+3-5"},
        "aps_declining":       {"signal": "NEGATIVE", "impact": "moderate", "ltui": "-3-5"},
        "shs_declining":       {"signal": "NEGATIVE", "impact": "moderate", "ltui": "-2-4"},
        "pre_contract_window": {"signal": "POSITIVE", "impact": "high",     "aps_boost": "+0.25"},
        "release_clause":      {"signal": "POSITIVE", "impact": "high",     "aps_boost": "+0.20"},
        "national_callup":     {"signal": "POSITIVE", "impact": "moderate", "ncsi": "activated"},
        "injury_warning":      {"signal": "NEGATIVE", "impact": "high",     "tai_impact": "significant"},
        "social_crisis":       {"signal": "NEGATIVE", "impact": "high",     "abs_impact": "-10-20"},
        "nft_launch":          {"signal": "POSITIVE", "impact": "low",      "aps_boost": "+0.04-0.06"},
        "contract_extension":  {"signal": "POSITIVE", "impact": "moderate", "stability": "confirmed"},
    }

    def detect(self, profile: AthleteCommercialProfile,
               new_data: dict) -> list:
        """
        Detect events by comparing new data against current profile.
        Returns list of detected events with their signal impact.
        """
        events = []

        # APS trend change
        aps_trend = profile.aps_trend()
        if aps_trend == "RISING" and profile.aps >= 0.70:
            events.append({
                "type":    "aps_rising",
                "athlete": profile.name,
                "current_aps": profile.aps,
                "adjusted_aps": profile.financial_aps_adjusted(),
                "trend":   aps_trend,
            })
        elif aps_trend == "DECLINING" and profile.aps <= 0.60:
            events.append({
                "type":    "aps_declining",
                "athlete": profile.name,
                "current_aps": profile.aps,
                "decline_concern": profile.aps < 0.50
            })

        # SHS declining — social health concern
        if profile.shs_trend() == "DECLINING" and profile.shs < 60:
            events.append({
                "type":    "shs_declining",
                "athlete": profile.name,
                "current_shs": profile.shs,
                "phase3_risk": profile.shs < 50
            })

        # Pre-contract window opening
        if profile.pre_contract_eligible and not any(
            a["type"] == "pre_contract_window" for a in profile.alert_history[-10:]
        ):
            events.append({
                "type":              "pre_contract_window",
                "athlete":           profile.name,
                "adjusted_aps":      profile.financial_aps_adjusted(),
                "action_recommended": "Clubs: approach now for pre-contract talks",
                "window":            "Pre-contract eligible — zero transfer fee possible"
            })

        # National team call-up signal
        if new_data.get("national_callup") and profile.national_team:
            ncsi = profile.ncsi_potential(new_data.get("competition_weight", 0.55))
            events.append({
                "type":            "national_callup",
                "athlete":         profile.name,
                "national_team":   profile.national_team,
                "club_token":      profile.club_token,
                "estimated_ncsi":  ncsi,
                "message":         (
                    f"{profile.name} called up for {profile.national_team}. "
                    f"Estimated NCSI for ${profile.club_token}: {ncsi:.3f}"
                )
            })

        # Injury warning
        if new_data.get("injury_reported") and profile.tai < 70:
            events.append({
                "type":            "injury_warning",
                "athlete":         profile.name,
                "tai":             profile.tai,
                "injury_details":  new_data.get("injury_details", "Unknown"),
                "expected_return": new_data.get("expected_return", "Unknown"),
                "club_token":      profile.club_token,
                "signal":          "NEGATIVE — flag injury_warning for club token"
            })

        return events


# ── The agent ─────────────────────────────────────────────────────────────────

class AthleteCommercialTrackerAgent:
    """
    Monitors athlete commercial profiles and surfaces intelligence changes.
    Level 1 autonomy: generates intelligence briefings; human decides on action.
    """

    def __init__(self, athlete_portfolio: list):
        self.portfolio       = {
            a["athlete_id"]: AthleteCommercialProfile(**a)
            for a in athlete_portfolio
        }
        self.detector        = CommercialEventDetector()
        self.macro_modifier  = 1.00
        self.cycle_count     = 0
        self.events_detected = 0

    async def run(self):
        log.info(f"Athlete Commercial Tracker — {len(self.portfolio)} athletes")
        await self._refresh_macro()

        while True:
            try:
                await self._run_cycle()
            except Exception as e:
                log.error(f"Cycle error: {e}")
            await asyncio.sleep(CYCLE_HOURS * 3600)

    async def _run_cycle(self):
        self.cycle_count += 1
        log.info(f"── Commercial Tracker Cycle {self.cycle_count} ──")

        await self._refresh_macro()

        for athlete_id, profile in self.portfolio.items():
            new_data = await self._fetch_athlete_data(athlete_id)
            if new_data:
                profile.update_metrics(new_data)
                events = self.detector.detect(profile, new_data)

                for event in events:
                    await self._process_event(event, profile)
                    self.events_detected += 1

        # Weekly commercial briefing
        if self.cycle_count % 14 == 0:  # Every ~7 days at 12h cycle
            await self._generate_weekly_briefing()

    async def _process_event(self, event: dict, profile: AthleteCommercialProfile):
        """Process detected event — Level 1 advisory output."""
        event_type = event["type"]
        impact     = CommercialEventDetector.EVENT_TYPES.get(event_type, {})

        log.info(f"EVENT: {event_type} | {profile.name} | {impact.get('signal')}")

        # Build intelligence brief
        brief = {
            "event_type":     event_type,
            "athlete":        profile.name,
            "sport":          profile.sport,
            "club":           profile.club,
            "club_token":     profile.club_token,
            "signal":         impact.get("signal"),
            "impact_level":   impact.get("impact"),
            "current_metrics": {
                "aps":          profile.aps,
                "aps_adjusted": profile.financial_aps_adjusted(),
                "aels":         profile.aels,
                "abs":          profile.abs_score,
                "shs":          profile.shs,
                "dts":          profile.dts,
            },
            "aps_trend":      profile.aps_trend(),
            "shs_trend":      profile.shs_trend(),
            "details":        event,
            "generated_at":   datetime.now(timezone.utc).isoformat(),
            "advisory_note":  (
                "Level 1 advisory — SportMind surfaces this intelligence. "
                "Commercial decisions require human review."
            )
        }

        # Audit log
        with open(AUDIT_LOG, "a") as f:
            f.write(json.dumps(brief) + "\n")

        # Alert for high-impact events
        if impact.get("impact") == "high":
            await self._send_alert(brief)

    async def _generate_weekly_briefing(self):
        """Generate weekly commercial intelligence briefing."""
        now = datetime.now(timezone.utc)
        lines = [
            f"# Weekly Athlete Commercial Intelligence",
            f"Generated: {now.strftime('%Y-%m-%d %H:%M UTC')}",
            f"Macro: {self.macro_phase} ({self.macro_modifier})",
            f"Athletes monitored: {len(self.portfolio)}",
            "",
            "## Top Commercial Assets (by adjusted APS)",
            ""
        ]

        # Rank by adjusted APS
        ranked = sorted(self.portfolio.values(),
                        key=lambda p: p.financial_aps_adjusted(),
                        reverse=True)

        for profile in ranked[:10]:
            lines.append(
                f"- **{profile.name}** ({profile.sport}) — "
                f"APS: {profile.aps:.2f} → Adjusted: {profile.financial_aps_adjusted():.2f} | "
                f"AELS: {profile.aels:.2f} | ABS: {profile.abs_score:.0f} | "
                f"Trend: {profile.aps_trend()}"
            )

        # Pre-contract windows
        pre_contract = [p for p in self.portfolio.values() if p.pre_contract_eligible]
        if pre_contract:
            lines.extend(["", "## ⚡ Pre-Contract Windows Open", ""])
            for p in pre_contract:
                lines.append(
                    f"- **{p.name}**: APS adjusted {p.financial_aps_adjusted():.2f} "
                    f"(×1.25 contract multiplier active)"
                )

        briefing_path = Path("athlete_commercial_briefing.md")
        briefing_path.write_text("\n".join(lines))
        log.info(f"Weekly briefing: {briefing_path}")

    async def _fetch_athlete_data(self, athlete_id: str) -> dict:
        """
        Fetch current athlete commercial data.
        REPLACE with your athlete data source.
        
        Possible sources:
          - TransferMarkt API (market values, transfer rumours)
          - Social media analytics APIs (SHS proxy)
          - Internal scouting database
          - Your own athlete tracking system
        """
        # Stub: return empty dict (replace with live data)
        return {}

    async def _refresh_macro(self):
        try:
            async with aiohttp.ClientSession() as s:
                async with s.get(f"{SPORTMIND_API}/macro-state") as r:
                    data             = await r.json()
                    self.macro_modifier = data["macro_state"]["crypto_cycle"]["macro_modifier"]
                    self.macro_phase    = data["macro_state"]["crypto_cycle"]["phase"]
        except Exception as e:
            log.warning(f"Macro refresh failed: {e}")

    async def _send_alert(self, brief: dict):
        log.warning(f"HIGH-IMPACT EVENT: {brief['athlete']} — {brief['event_type']}")
        if ALERT_WEBHOOK:
            try:
                async with aiohttp.ClientSession() as s:
                    await s.post(ALERT_WEBHOOK, json=brief)
            except: pass

    def get_status(self) -> dict:
        """Observable state for sportmind_agent_status MCP tool."""
        return {
            "agent_id":         "athlete-commercial-tracker-001",
            "agent_type":       "athlete_commercial_tracker",
            "state":            "MONITORING",
            "autonomy_level":   1,
            "athletes_tracked": len(self.portfolio),
            "cycle_count":      self.cycle_count,
            "events_detected":  self.events_detected,
            "macro_modifier":   self.macro_modifier,
            "cycle_hours":      CYCLE_HOURS
        }


# ── Example portfolio ──────────────────────────────────────────────────────────

EXAMPLE_PORTFOLIO = [
    {
        "athlete_id":   "player-psg-001",
        "name":         "PSG Forward",
        "sport":        "football",
        "club":         "Paris Saint-Germain",
        "club_token":   "PSG",
        "national_team": "France",
        "aps":          0.82,
        "aels":         0.74,
        "abs_score":    84.0,
        "shs":          78.0,
        "dts":          76.0,
        "tai":          72.0,
        "contract_years_remaining": 1.5
    },
    {
        "athlete_id":   "player-bar-001",
        "name":         "Barcelona Midfielder",
        "sport":        "football",
        "club":         "FC Barcelona",
        "club_token":   "BAR",
        "national_team": "Spain",
        "aps":          0.75,
        "aels":         0.68,
        "abs_score":    78.0,
        "shs":          72.0,
        "dts":          80.0,
        "tai":          75.0,
        "contract_years_remaining": 0.4  # Pre-contract eligible!
    },
]


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")
    agent = AthleteCommercialTrackerAgent(EXAMPLE_PORTFOLIO)
    asyncio.run(agent.run())
```

---

## Integration with other agents

```
ATHLETE COMMERCIAL TRACKER IN THE COORDINATED SYSTEM:

Tracker FEEDS:
  → Transfer Monitor (Pattern 4): pre-contract window alerts
    When APS adjusted rises above 0.75 and contract < 6 months,
    transfer monitor adds athlete to high-priority watchlist
    
  → Portfolio Monitor (Pattern 1): NCSI potential updates
    When national call-up detected, portfolio monitor receives
    estimated NCSI impact for the relevant club token
    
  → Governance Agent (App 8): commercial brief for signing votes
    Pre-vote governance analysis uses tracker's current APS + AELS data
    
  → Talent Scouting (App 9): live commercial profile
    Scouting reports pull current tracker data for APS and ABS sections

Tracker RECEIVES:
  → Match results (for form-based APS recalculation)
  → Social monitoring feeds (for SHS updates)
  → Transfer news (for TSI calculation)
  → Nothing from other SportMind agents (standalone data intake)
```

---

## Compatibility

**Athlete financial intelligence:** `core/athlete-financial-intelligence.md` — APS adjustment formula
**Transfer signal:** `fan-token/transfer-signal/` — APS base calculation
**Talent scouting:** `examples/applications/app-09-talent-scouting.md` — consuming commercial tracker data
**Governance intelligence:** `examples/applications/app-08-governance-intelligence.md` — commercial brief
**Multi-agent coordination:** `examples/agentic-workflows/multi-agent-coordination.md`
**Agent framework:** `core/autonomous-agent-framework.md`

*MIT License · SportMind · sportmind.dev*
