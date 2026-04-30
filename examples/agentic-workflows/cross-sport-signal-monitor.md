# Agentic Workflow Pattern 7 — Cross-Sport Signal Monitor

**Monitors multiple sport signals simultaneously and identifies when macro
conditions, correlated narrative events, or fan token market dynamics create
signal alignment opportunities across different sports or tokens.**

This pattern goes beyond monitoring a single sport or a single portfolio. It
watches for moments when multiple independent signals converge — a Champion's
League match, a cricket World Cup game, and a UFC title fight all happening
within 48 hours while the macro modifier is elevated — and identifies when
that convergence creates unusually strong combined intelligence.

---

## Why cross-sport monitoring matters

Fan token markets are not fully independent. The same macro cycle that elevates
$PSG also elevates $BAR and $CITY. A general crypto bull market creates liquidity
and attention that benefits all tokens simultaneously. Conversely, a macro
downturn suppresses all fan token signals regardless of sporting quality.

Beyond macro correlation, narrative events can cross sports: a World Cup period
creates football narrative dominance that compresses signals in other sports. A
UFC mega-event on the same weekend as a Champions League final competes for fan
attention. Understanding these interactions makes portfolio-level decisions more
accurate than analysing each token independently.

---

## The signal convergence model

```python
# examples/agentic-workflows/cross_sport_signal_monitor.py
"""
SportMind Cross-Sport Signal Monitor
Pattern 7: Monitors correlated signals across multiple sports.

Cycle: Every 6 hours
Autonomy: Level 2 (alerts on convergence; human decides on action)
"""
import asyncio
import logging
import json
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import aiohttp

SPORTMIND_API = "http://localhost:8080"
ALERT_WEBHOOK = ""
log = logging.getLogger("sportmind.cross-sport-monitor")


# ── Signal profile per sport/token ────────────────────────────────────────────

@dataclass
class SportSignalProfile:
    """Active signal state for a single sport/token combination."""
    sport:          str
    token:          str
    sms:            float = 0.0
    recommended:    str = "WAIT"
    macro_modifier: float = 1.00
    active_flags:   list = field(default_factory=list)
    hours_to_event: float = 999.0
    event_id:       str = ""
    ncsi_active:    bool = False
    kol_signal:     float = 0.0       # KIS from KOL monitor
    onchain_signal: float = 0.0       # on-chain event composite
    last_updated:   str = ""

    def total_signal_strength(self) -> float:
        """Composite signal strength including all modifiers."""
        base = self.sms / 100.0
        kol_boost   = min(0.15, self.kol_signal * 0.15)
        chain_boost = min(0.10, self.onchain_signal * 0.10)
        ncsi_boost  = 0.08 if self.ncsi_active else 0.0
        return round(min(1.0, base + kol_boost + chain_boost + ncsi_boost), 3)

    def is_actionable(self) -> bool:
        """Is this signal strong enough to consider acting?"""
        return (
            self.recommended in ("ENTER", "REDUCE") and
            self.sms >= 65 and
            "macro_override_active" not in self.active_flags and
            "liquidity_critical" not in self.active_flags
        )


# ── Convergence detection ──────────────────────────────────────────────────────

@dataclass
class ConvergenceEvent:
    """A detected convergence of multiple strong signals."""
    convergence_type:   str
    sports_involved:    list
    tokens_involved:    list
    combined_strength:  float
    macro_modifier:     float
    time_window_hours:  float
    description:        str
    recommendation:     str
    detected_at:        str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class ConvergenceDetector:
    """
    Detects when multiple sport signals align to create
    a stronger combined opportunity.
    """

    def detect(self, profiles: dict[str, SportSignalProfile],
               macro_modifier: float) -> list[ConvergenceEvent]:
        """Scan all active profiles for convergence patterns."""
        events = []
        actionable = [p for p in profiles.values() if p.is_actionable()]

        # Pattern 1: MACRO_BULL_MULTI_SIGNAL
        # Multiple tokens actionable during bull macro
        if macro_modifier >= 1.10 and len(actionable) >= 3:
            combined = sum(p.total_signal_strength() for p in actionable) / len(actionable)
            if combined >= 0.72:
                events.append(ConvergenceEvent(
                    convergence_type  = "MACRO_BULL_MULTI_SIGNAL",
                    sports_involved   = [p.sport for p in actionable],
                    tokens_involved   = [p.token for p in actionable],
                    combined_strength = round(combined, 3),
                    macro_modifier    = macro_modifier,
                    time_window_hours = max(p.hours_to_event for p in actionable),
                    description       = (
                        f"Bull macro ({macro_modifier}) with {len(actionable)} actionable signals "
                        f"across {len(set(p.sport for p in actionable))} sports. "
                        f"Average signal strength: {combined:.2f}"
                    ),
                    recommendation    = "PORTFOLIO_ENTER: consider scaled position across all actionable tokens"
                ))

        # Pattern 2: SAME_WINDOW_MULTI_SPORT
        # Multiple tokens with events within 48h of each other
        time_clustered = [p for p in actionable if p.hours_to_event <= 48]
        if len(time_clustered) >= 2:
            sports_in_window = set(p.sport for p in time_clustered)
            if len(sports_in_window) >= 2:  # Must be different sports
                combined = sum(p.total_signal_strength() for p in time_clustered) / len(time_clustered)
                events.append(ConvergenceEvent(
                    convergence_type  = "SAME_WINDOW_MULTI_SPORT",
                    sports_involved   = list(sports_in_window),
                    tokens_involved   = [p.token for p in time_clustered],
                    combined_strength = round(combined, 3),
                    macro_modifier    = macro_modifier,
                    time_window_hours = 48.0,
                    description       = (
                        f"{len(time_clustered)} tokens across {len(sports_in_window)} sports "
                        f"all have events within 48h. Combined signal: {combined:.2f}"
                    ),
                    recommendation    = "TIMED_ENTRY: consider pre-event entry for all tokens within 48h window"
                ))

        # Pattern 3: NCSI_AMPLIFICATION
        # National team event creating spillover into multiple club tokens
        ncsi_active = [p for p in profiles.values() if p.ncsi_active and p.sms >= 55]
        if len(ncsi_active) >= 2:
            clubs_from_same_nation = self._find_national_clusters(ncsi_active)
            for nation, club_profiles in clubs_from_same_nation.items():
                if len(club_profiles) >= 2:
                    combined = sum(p.total_signal_strength() for p in club_profiles) / len(club_profiles)
                    events.append(ConvergenceEvent(
                        convergence_type  = "NCSI_AMPLIFICATION",
                        sports_involved   = ["football"],
                        tokens_involved   = [p.token for p in club_profiles],
                        combined_strength = round(combined, 3),
                        macro_modifier    = macro_modifier,
                        time_window_hours = 24.0,
                        description       = (
                            f"National team event creating NCSI spillover into "
                            f"{len(club_profiles)} club tokens ({nation}). "
                            f"Combined: {combined:.2f}"
                        ),
                        recommendation    = f"NCSI_ENTER: {nation} performance driving multiple club tokens"
                    ))

        # Pattern 4: COUNTER_CYCLE_OPPORTUNITY
        # Strong sport signal when macro is slightly bearish (counter-cyclical fans)
        if 0.80 <= macro_modifier <= 0.92 and len(actionable) >= 1:
            high_quality = [p for p in actionable if p.sms >= 78]
            if high_quality:
                events.append(ConvergenceEvent(
                    convergence_type  = "COUNTER_CYCLE_OPPORTUNITY",
                    sports_involved   = [p.sport for p in high_quality],
                    tokens_involved   = [p.token for p in high_quality],
                    combined_strength = sum(p.total_signal_strength() for p in high_quality) / len(high_quality),
                    macro_modifier    = macro_modifier,
                    time_window_hours = min(p.hours_to_event for p in high_quality),
                    description       = (
                        f"Bear macro ({macro_modifier}) but high-quality sport signal (SMS ≥ 78). "
                        f"Potential counter-cyclical entry — sport quality outweighs macro headwind."
                    ),
                    recommendation    = "SELECTIVE_ENTER: consider reduced position (50%) on highest-SMS token only"
                ))

        return events

    def _find_national_clusters(self, profiles: list) -> dict:
        """
        Group tokens by national team NCSI source.
        In production: use actual NCSI mapping from fan-token/football-token-intelligence/
        """
        # Simplified: group by common token characteristics
        # In production: load NCSI mapping to detect which national team is causing the signal
        return {"detected_nation": profiles}


# ── The agent ──────────────────────────────────────────────────────────────────

class CrossSportSignalMonitor:
    """
    Monitors multiple sport/token signals simultaneously.
    Detects convergence patterns and alerts on compound opportunities.
    """

    def __init__(self, token_portfolio: list[dict]):
        """
        token_portfolio: list of {token, sport, event_calendar_url}
        Example:
          [
            {"token": "PSG",  "sport": "football"},
            {"token": "BAR",  "sport": "football"},
            {"token": "UFC",  "sport": "mma"},
            {"token": "RBULL", "sport": "formula1"},
          ]
        """
        self.portfolio       = token_portfolio
        self.profiles        = {}   # {token: SportSignalProfile}
        self.macro_modifier  = 1.00
        self.macro_phase     = "UNKNOWN"
        self.detector        = ConvergenceDetector()
        self.convergences    = []   # History of detected convergence events
        self.cycle_count     = 0
        self.alerts_sent     = 0

    async def run(self, cycle_hours: float = 6.0):
        """Main monitoring loop."""
        log.info(f"Cross-Sport Signal Monitor — {len(self.portfolio)} tokens")
        await self._initialise()

        while True:
            try:
                await self._run_cycle()
            except Exception as e:
                log.error(f"Cycle error: {e}")
            await asyncio.sleep(cycle_hours * 3600)

    async def _initialise(self):
        """Initialise signal profiles for all tokens."""
        await self._refresh_macro()
        for token_config in self.portfolio:
            token = token_config["token"]
            self.profiles[token] = SportSignalProfile(
                sport       = token_config["sport"],
                token       = token,
                last_updated = datetime.now(timezone.utc).isoformat()
            )
        log.info(f"Initialised {len(self.profiles)} signal profiles")

    async def _run_cycle(self):
        """Single monitoring cycle."""
        self.cycle_count += 1
        log.info(f"── Cross-Sport Cycle {self.cycle_count} ──")

        # 1. Refresh macro (always first)
        await self._refresh_macro()

        # 2. Refresh all signal profiles
        for token, profile in self.profiles.items():
            await self._refresh_profile(profile)

        # 3. Detect convergence patterns
        new_convergences = self.detector.detect(self.profiles, self.macro_modifier)

        # 4. Alert on new convergences
        for event in new_convergences:
            await self._process_convergence(event)

        # 5. Log cycle summary
        actionable_count = sum(1 for p in self.profiles.values() if p.is_actionable())
        log.info(
            f"Cycle {self.cycle_count}: "
            f"macro={self.macro_modifier} ({self.macro_phase}) | "
            f"{actionable_count}/{len(self.profiles)} tokens actionable | "
            f"{len(new_convergences)} convergences detected"
        )

        # 6. Publish state for downstream agents
        await self._publish_state(new_convergences)

    async def _refresh_profile(self, profile: SportSignalProfile):
        """
        Refresh signal profile for a single token.
        In production: calls SportMind MCP/API for current signal.
        REPLACE with live SportMind signal fetch.
        """
        # STUB: In production, call sportmind_signal MCP tool
        # or GET /signal?token={profile.token}&sport={profile.sport}
        pass

    async def _refresh_macro(self):
        """Refresh macro state."""
        try:
            async with aiohttp.ClientSession() as s:
                async with s.get(f"{SPORTMIND_API}/macro-state") as r:
                    data = await r.json()
                    cycle = data["macro_state"]["crypto_cycle"]
                    self.macro_modifier = cycle["macro_modifier"]
                    self.macro_phase    = cycle["phase"]
        except Exception as e:
            log.warning(f"Macro refresh failed: {e}")

    async def _process_convergence(self, event: ConvergenceEvent):
        """Process a detected convergence event."""
        log.info(f"CONVERGENCE: {event.convergence_type} | {event.tokens_involved}")
        self.convergences.append(event)
        self.alerts_sent += 1

        # Build alert
        alert = {
            "type":            "convergence",
            "convergence_type": event.convergence_type,
            "tokens":          event.tokens_involved,
            "sports":          event.sports_involved,
            "strength":        event.combined_strength,
            "macro":           event.macro_modifier,
            "time_window_h":   event.time_window_hours,
            "description":     event.description,
            "recommendation":  event.recommendation,
            "timestamp":       event.detected_at,
            "advisory_note":   "Level 2: alert generated autonomously; human decides on action"
        }

        if ALERT_WEBHOOK:
            try:
                async with aiohttp.ClientSession() as s:
                    await s.post(ALERT_WEBHOOK, json=alert)
            except Exception as e:
                log.error(f"Alert failed: {e}")

    async def _publish_state(self, convergences: list):
        """Publish current state to coordination layer."""
        state = {
            "generated_at":   datetime.now(timezone.utc).isoformat(),
            "macro_modifier": self.macro_modifier,
            "macro_phase":    self.macro_phase,
            "profiles":       {t: {"sms": p.sms, "recommended": p.recommended,
                                   "hours_to_event": p.hours_to_event,
                                   "signal_strength": p.total_signal_strength()}
                               for t, p in self.profiles.items()},
            "convergences":   [{"type": c.convergence_type, "tokens": c.tokens_involved,
                                 "strength": c.combined_strength} for c in convergences]
        }
        output = Path("coordination/cross_sport_state.json")
        output.parent.mkdir(exist_ok=True)
        output.write_text(json.dumps(state, indent=2))

    def get_status(self) -> dict:
        """Observable state for sportmind_agent_status MCP tool."""
        actionable = [t for t, p in self.profiles.items() if p.is_actionable()]
        return {
            "agent_id":         "cross-sport-monitor-001",
            "agent_type":       "cross_sport_signal_monitor",
            "state":            "MONITORING",
            "autonomy_level":   2,
            "tokens_watched":   len(self.profiles),
            "tokens_actionable": len(actionable),
            "macro_modifier":   self.macro_modifier,
            "macro_phase":      self.macro_phase,
            "cycle_count":      self.cycle_count,
            "alerts_sent":      self.alerts_sent,
            "convergence_types": list(set(c.convergence_type for c in self.convergences[-10:]))
        }


# ── Example deployment ──────────────────────────────────────────────────────────

EXAMPLE_PORTFOLIO = [
    {"token": "PSG",   "sport": "football"},
    {"token": "BAR",   "sport": "football"},
    {"token": "CITY",  "sport": "football"},
    {"token": "JUV",   "sport": "football"},
    {"token": "ATM",   "sport": "football"},
]

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")
    agent = CrossSportSignalMonitor(EXAMPLE_PORTFOLIO)
    asyncio.run(agent.run(cycle_hours=6.0))
```

---

## The four convergence patterns

### Pattern 1 — MACRO_BULL_MULTI_SIGNAL

```
TRIGGER: macro_modifier >= 1.10 AND 3+ tokens actionable AND avg signal >= 0.72

MEANING: The macro environment amplifies all fan token signals simultaneously.
         In a genuine bull market with multiple strong sporting events, the
         combined commercial opportunity is larger than any individual signal.

RECOMMENDATION: PORTFOLIO_ENTER — consider scaled positions across all actionable tokens.
                Allocate proportional to individual SMS scores.
                Standard position sizing but across a wider portfolio.

RISK: All tokens move together → correlated downside risk if macro reverses.
      Monitor macro_modifier every 2h during this pattern.
```

### Pattern 2 — SAME_WINDOW_MULTI_SPORT

```
TRIGGER: 2+ tokens from different sports with events within 48h

MEANING: Multiple different sports events converging in the same commercial window.
         Fan attention and liquidity concentrate around major event weekends.
         UCL mid-week + NBA playoff game + UFC Fight Night on the same weekend
         can collectively lift all three tokens' commercial signals.

RECOMMENDATION: TIMED_ENTRY — pre-event entry for all tokens within the 48h window.
                Avoid conflicts with single-team-focus fan attention.
                Works best when sports are complementary (not competing for same fans).
```

### Pattern 3 — NCSI_AMPLIFICATION

```
TRIGGER: 2+ club tokens with active NCSI from same national team

MEANING: A national team event is simultaneously creating commercial spillover
         into multiple club tokens. Real Madrid and Barcelona both benefit when
         Spain wins at a World Cup. This is free leverage on a single sporting event.

RECOMMENDATION: NCSI_ENTER — enter both/all affected club tokens proportional
                to each player's ATM weight for the national team.
                Higher ATM player = larger position in their club token.
```

### Pattern 4 — COUNTER_CYCLE_OPPORTUNITY

```
TRIGGER: macro_modifier between 0.80-0.92 AND high SMS sport signal (≥ 78)

MEANING: The macro environment is mildly bearish but an exceptional sport signal
         may outweigh the macro headwind. SportMind does not recommend entering
         against strong macro pressure, but a genuinely elite sport signal (SMS 78+)
         from a Tier 1 event can justify a cautious position even in a mild bear.

RECOMMENDATION: SELECTIVE_ENTER at 50% position — reduced size acknowledges macro risk;
                quality signal justifies not abstaining entirely.
                Only valid for SMS >= 78 with Tier 1 competition.
```

---

## Coordination with other agents

```
CROSS-SPORT MONITOR FEEDS:
  → Portfolio Monitor (Pattern 1): convergence alerts as portfolio signals
    When MACRO_BULL_MULTI_SIGNAL detected: portfolio monitor receives
    combined opportunity brief for all affected tokens

  → Pre-Match Chain (Pattern 2): SAME_WINDOW events get prioritised analysis
    The 48h window detection triggers pre-match chain for all clustered events

  → Signal Bus: publishes convergence events
    Any agent subscribed to the bus receives convergence notifications
    See: examples/agentic-workflows/multi-agent-coordination.md

CROSS-SPORT MONITOR RECEIVES:
  → KOL monitor output: kol_signal per token
  → On-chain monitor: onchain_signal per token  
  → Macro monitor: macro_modifier and phase
  → Pre-match chain: SMS scores for upcoming events

SUITE INTEGRATION:
  SportFi Kit: reads cross_sport_state.json for portfolio dashboard display
  Fan Digital Twin (App 10): NCSI_AMPLIFICATION events update FLS for national team events
```

---

## Compatibility

**Agent framework:** `core/autonomous-agent-framework.md` — lifecycle and safety model
**Multi-agent coordination:** `examples/agentic-workflows/multi-agent-coordination.md` — signal bus
**Portfolio monitor:** `examples/agentic-workflows/README.md` — Pattern 1 (primary consumer)
**KOL monitor:** `fan-token/kol-influence-intelligence/` — kol_signal input
**On-chain monitor:** `fan-token/on-chain-event-intelligence/` — onchain_signal input
**Goal framework:** `core/agent-goal-framework.md` — can be goal-directed variant

*MIT License · SportMind · sportmind.dev*
