# SportMind Agentic Workflow Patterns

**Reusable workflow patterns for SportMind agents operating autonomously over time.**

These patterns go beyond single-query analysis. They define how SportMind agents
should behave as continuous, long-running processes — monitoring events, triggering
analysis, escalating to human review, and completing autonomously.

---

## What makes a SportMind workflow agentic

A single SportMind query is: "Analyse PSG vs Arsenal tonight."
An agentic SportMind workflow is: "Monitor all UCL matches for the next 3 months,
generate pre-match intelligence 48h before each game, detect when signal quality
drops below SMS 60, and alert me before I miss an opportunity."

The difference is:
- **Time horizon:** Hours or months, not one conversation
- **Triggers:** Events or schedules, not user prompts
- **Autonomy:** Runs without human input between triggers
- **Escalation:** Knows when to alert a human vs complete independently
- **Memory:** Retains context across multiple trigger cycles

---

## The four workflow patterns

| Pattern | Use case | Trigger | Duration |
|---|---|---|---|
| [1. Continuous Portfolio Monitor](#pattern-1) | Fan token portfolio intelligence | Scheduled (4h) + event-driven | Ongoing |
| [2. Pre-Match Intelligence Chain](#pattern-2) | Pre-match signal for specific events | Calendar-driven (T-48h, T-2h) | Per match |
| [3. Tournament Tracker](#pattern-3) | Tournament NCSI monitoring | Match results + bracket events | Tournament duration |
| [4. Transfer Window Monitor](#pattern-4) | Transfer intelligence during windows | Daily + breaking news | Window duration |
| [5. League Monitoring Agent](#pattern-5) | Full league signal prioritisation | 6h cycle | Season duration |
| [6. Athlete Commercial Tracker](#pattern-6) | APS/AELS/SHS commercial monitoring | 12h cycle | Ongoing |
| [7. Cross-Sport Signal Monitor](#pattern-7) | Correlated signal convergence | 6h cycle | Ongoing |
| [8. Fan Token Play Monitor](#pattern-8) | PATH_2 match cycle (T-48h → T+48h) | Event-driven (match calendar) | Per match |
| [9. Smart Governance Delegate](#pattern-9) | Pre-vote commercial intelligence brief | New proposal detected + 12h cycle | Ongoing |
| [10. Moneyball Scouting Agent](#pattern-10) | Transfer target commercial ranking | On-demand (transfer window) | Per window |
| [11. Post-Match Analysis Agent](#pattern-11) | Result → layers → FTP → plain-English brief | Full-time confirmed | Per match |
| [12. Live Match Agent](#pattern-12) | Pre-match prior + live event updates → adaptive signal | Event-driven (in-match) |
| [13. Web Agent Live Data](#pattern-13) | Autonomous lineup confirmation, supply verification, regulatory monitoring | Scheduled + event-driven | Per match |

---

## Pattern 1 — Continuous Portfolio Monitor

**Purpose:** Monitors a fan token portfolio continuously, explaining price movements,
surfacing upcoming signal events, and alerting when significant signals approach.

```python
# workflow/portfolio_monitor.py

import schedule, time, json, requests
from datetime import datetime, timezone
from pathlib import Path

SPORTMIND_API = "http://localhost:8080"
PORTFOLIO = ["PSG", "BAR", "CITY", "JUV"]  # tokens to monitor

def check_macro():
    """Step 1: Always check macro first."""
    macro = requests.get(f"{SPORTMIND_API}/macro-state").json()
    modifier = macro["macro_state"]["crypto_cycle"]["macro_modifier"]
    phase = macro["macro_state"]["crypto_cycle"]["phase"]
    return modifier, phase

def analyse_token(symbol: str, macro_modifier: float) -> dict:
    """Step 2: Generate intelligence for each token."""
    sport = TOKEN_TO_SPORT[symbol]  # e.g. "PSG" → "football"
    stack = requests.get(
        f"{SPORTMIND_API}/stack?use_case=fan_token_tier1&sport={sport}"
    ).json()
    
    sms = compute_sms(stack, macro_modifier)
    return {
        "symbol": symbol,
        "sms": sms,
        "macro_modifier": macro_modifier,
        "upcoming_events": extract_upcoming_events(stack, sport),
        "flags": stack.get("modifiers", {}).get("flags", {}),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

def should_alert(analysis: dict) -> tuple[bool, str]:
    """Step 3: Determine if human alert is needed."""
    flags = analysis["flags"]
    
    if flags.get("macro_override_active") and analysis["macro_modifier"] < 0.60:
        return True, f"EXTREME BEAR: {analysis['symbol']} signals unreliable"
    
    if any(e["signal_weight"] == "VERY_HIGH" and e["hours_away"] < 48
           for e in analysis.get("upcoming_events", [])):
        return True, f"HIGH SIGNAL EVENT in 48h: {analysis['symbol']}"
    
    if flags.get("injury_warning"):
        return True, f"INJURY FLAG: Key player concern for {analysis['symbol']}"
    
    return False, ""

def run_portfolio_cycle():
    """Main workflow cycle — runs every 4 hours."""
    macro_modifier, phase = check_macro()
    
    alerts = []
    intelligence = []
    
    for symbol in PORTFOLIO:
        analysis = analyse_token(symbol, macro_modifier)
        intelligence.append(analysis)
        
        needs_alert, message = should_alert(analysis)
        if needs_alert:
            alerts.append(message)
    
    # Log intelligence
    save_intelligence_record(intelligence)
    
    # Send alerts if any
    if alerts:
        send_alerts(alerts)  # email / push / webhook
    
    print(f"[{datetime.now().isoformat()}] Cycle complete. "
          f"Macro: {phase} ({macro_modifier}). Alerts: {len(alerts)}")

# Scheduling
schedule.every(4).hours.do(run_portfolio_cycle)
schedule.every().day.at("06:00").do(run_portfolio_cycle)  # Morning refresh

if __name__ == "__main__":
    run_portfolio_cycle()  # Run immediately on start
    while True:
        schedule.run_pending()
        time.sleep(60)
```

**Escalation rules:**
- SMS < 40: log but do not alert (insufficient intelligence, not a signal)
- Macro override active: alert immediately
- Very high signal event < 48h: alert
- Injury flag active: alert
- Token price moves > 10% without identified signal: alert (unexplained movement)

---

## Pattern 2 — Pre-Match Intelligence Chain

**Purpose:** Generates complete pre-match intelligence for a specific fixture
at T-48h and T-2h, with automatic lineup update at T-2h.

```python
# workflow/prematch_chain.py

from datetime import datetime, timezone, timedelta
import requests, json

SPORTMIND_API = "http://localhost:8080"

class PreMatchChain:
    def __init__(self, event_id: str, sport: str, match_time: datetime):
        self.event_id   = event_id
        self.sport      = sport
        self.match_time = match_time
        self.t48_signal = None
        self.t2_signal  = None

    def run_t48_analysis(self):
        """T-48h: Full intelligence, lineup_unconfirmed expected."""
        macro = requests.get(f"{SPORTMIND_API}/macro-state").json()
        stack = requests.get(
            f"{SPORTMIND_API}/stack?use_case=fan_token_tier1&sport={self.sport}"
        ).json()
        
        self.t48_signal = {
            "event_id":        self.event_id,
            "generated_at":    datetime.now(timezone.utc).isoformat(),
            "window":          "T-48h",
            "macro_modifier":  macro["macro_state"]["crypto_cycle"]["macro_modifier"],
            "sms":             compute_sms(stack),
            "flags": {
                "lineup_unconfirmed": True,  # Expected at T-48h
                "macro_override_active": False,
                "position_size_recommendation": "50%"  # Half size until lineup
            },
            "direction":       extract_direction(stack),
            "adjusted_score":  extract_adjusted_score(stack),
            "reasoning":       extract_reasoning(stack)
        }
        
        save_signal(self.t48_signal)
        return self.t48_signal

    def run_t2_update(self, lineup_confirmed: bool, key_player_absent: bool = False):
        """T-2h: Lineup update — most critical window."""
        if not self.t48_signal:
            raise ValueError("Must run T-48h analysis before T-2h update")
        
        if key_player_absent:
            # Key player absent: reload analysis entirely
            return self.run_full_reload(reason="key_player_absent")
        
        # Lineup confirmed: update flags and position size
        self.t2_signal = {
            **self.t48_signal,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "window": "T-2h",
            "flags": {
                **self.t48_signal["flags"],
                "lineup_unconfirmed": not lineup_confirmed,
                "position_size_recommendation": "100%" if lineup_confirmed else "50%"
            },
            "t48_signal_reference": self.t48_signal["generated_at"]
        }
        
        save_signal(self.t2_signal)
        return self.t2_signal

    def run_full_reload(self, reason: str):
        """Reload analysis entirely when conditions change significantly."""
        print(f"Full reload triggered: {reason}")
        return self.run_t48_analysis()

# Schedule the chain
def schedule_match_chain(event_id, sport, match_time):
    chain = PreMatchChain(event_id, sport, match_time)
    
    t48_time = match_time - timedelta(hours=48)
    t2_time  = match_time - timedelta(hours=2)
    
    schedule.every().day.at(t48_time.strftime("%H:%M")).do(
        chain.run_t48_analysis
    ).tag(event_id)
    
    schedule.every().day.at(t2_time.strftime("%H:%M")).do(
        lambda: chain.run_t2_update(
            lineup_confirmed=check_lineup_confirmed(event_id),
            key_player_absent=check_key_player_absent(event_id)
        )
    ).tag(event_id)
```

**Key rules:**
- T-48h: Always set lineup_unconfirmed = True; position size = 50%
- T-2h: If lineup confirmed → clear flag, full size. If key player absent → full reload
- Never carry forward a T-48h signal past T-2h without updating
- SMS < 60 at T-2h: do not enter regardless of lineup status

---

## Pattern 3 — Tournament Tracker

**Purpose:** Monitors every match in a tournament (World Cup, Euros, etc.),
calculates NCSI spillover for each result, and updates a club token signal map.

```python
# workflow/tournament_tracker.py

class TournamentTracker:
    """
    Tracks NCSI signals across a full tournament.
    Maintains a club token signal map updated after each match.
    """
    
    def __init__(self, tournament_id: str, sport: str):
        self.tournament_id = tournament_id
        self.sport         = sport
        self.ncsi_map      = {}   # club_symbol → cumulative NCSI
        self.match_log     = []   # all processed matches
        self.macro_modifier = 1.0

    def initialise(self, squad_data: dict):
        """
        Build initial NCSI map from squad data.
        squad_data: {national_team: [{player, club_token, atm_score}]}
        """
        self.squad_data = squad_data
        self.macro_modifier = self._get_macro_modifier()
        
        # Pre-calculate which club tokens have NCSI exposure
        self.token_exposure = {}
        for nation, players in squad_data.items():
            for player in players:
                token = player.get("club_token")
                if token:
                    if token not in self.token_exposure:
                        self.token_exposure[token] = []
                    self.token_exposure[token].append({
                        "player": player["name"],
                        "nation": nation,
                        "atm":    player["atm_score"]
                    })
        
        return self.token_exposure

    def process_match_result(self, match: dict):
        """
        Process a match result and update NCSI signals.
        match: {home_nation, away_nation, home_score, away_score, scorers, stage}
        """
        # Determine NCSI weight from international cycle model
        ncsi_weight = self._get_ncsi_weight(match["stage"])
        
        # Apply tournament fatigue modifier if late stage
        if match["stage"] in ("semi_final", "final"):
            fatigue_modifier = 0.85  # teams have played many matches
        else:
            fatigue_modifier = 1.00
        
        # Calculate NCSI for each scorer's club token
        for scorer in match.get("scorers", []):
            player_data = self._find_player(scorer["name"], scorer["nation"])
            if not player_data or not player_data.get("club_token"):
                continue
            
            token    = player_data["club_token"]
            atm      = player_data["atm_score"]
            ncsi_val = ncsi_weight * atm * fatigue_modifier * self.macro_modifier
            
            if token not in self.ncsi_map:
                self.ncsi_map[token] = 0.0
            self.ncsi_map[token] += ncsi_val
        
        # Handle elimination signals
        loser = self._determine_loser(match)
        if loser and match["stage"] not in ("group_stage",):
            self._apply_elimination_signal(loser, match["stage"])
        
        self.match_log.append({
            "match": match,
            "ncsi_updates": self._get_recent_updates(),
            "processed_at": datetime.now(timezone.utc).isoformat()
        })
        
        return self.ncsi_map

    def get_signal_report(self) -> dict:
        """Generate current tournament signal report."""
        return {
            "tournament_id":    self.tournament_id,
            "macro_modifier":   self.macro_modifier,
            "matches_processed": len(self.match_log),
            "ncsi_map":         dict(sorted(
                self.ncsi_map.items(), key=lambda x: x[1], reverse=True
            )),
            "top_gainers":      self._get_top_n(5, positive=True),
            "top_losers":       self._get_top_n(5, positive=False),
            "generated_at":     datetime.now(timezone.utc).isoformat()
        }

    def _get_ncsi_weight(self, stage: str) -> float:
        """NCSI weights from market/international-football-cycle.md"""
        weights = {
            "group_stage":   1.00,
            "round_of_32":   1.20,
            "round_of_16":   1.40,
            "quarter_final": 1.60,
            "semi_final":    1.80,
            "third_place":   1.20,
            "final":         2.00
        }
        return weights.get(stage, 1.00)

    def _apply_elimination_signal(self, nation: str, stage: str):
        """Apply negative NCSI to tokens of eliminated nation's players."""
        stage_impact = {
            "round_of_32":   -0.05,
            "round_of_16":   -0.08,
            "quarter_final": -0.12,
            "semi_final":    -0.18,
            "final":         -0.10  # Runner-up: smaller penalty (still strong tournament)
        }
        impact = stage_impact.get(stage, -0.05)
        
        for player in self.squad_data.get(nation, []):
            token = player.get("club_token")
            if token and token in self.ncsi_map:
                self.ncsi_map[token] += impact * player["atm_score"]
```

---

## Pattern 4 — Transfer Window Monitor

**Purpose:** Monitors transfer intelligence during open windows (January, summer),
tracking rumour progression, APS recalculations, and token impact assessments.

```python
# workflow/transfer_monitor.py

class TransferWindowMonitor:
    """
    Monitors transfer intelligence during active windows.
    Tracks rumour → confirmation progression for token-relevant players.
    """
    
    RUMOUR_TIERS = {
        1: "Tier 1 journalist (Sky Sports, Fabrizio Romano)",
        2: "Reliable club journalist",
        3: "Regional journalist or fan media",
        4: "Social media / unverified"
    }
    
    def __init__(self, window: str = "summer"):
        self.window    = window  # "summer" or "january"
        self.watchlist = {}      # player → current intelligence
    
    def add_player(self, player_id: str, player_name: str, 
                   current_club_token: str, target_club_token: str = None):
        """Add a player to the transfer watchlist."""
        self.watchlist[player_id] = {
            "name":                player_name,
            "current_club_token":  current_club_token,
            "target_club_token":   target_club_token,
            "aps":                 None,   # calculated on first run
            "tsi":                 0.0,
            "rumour_tier":         None,
            "confirmed":           False,
            "aps_recalculated":    False
        }
    
    def update_rumour(self, player_id: str, tier: int, source: str):
        """Update TSI when a new rumour emerges."""
        if player_id not in self.watchlist:
            return
        
        # TSI calculation: tier 1 = 0.80 confidence, tier 4 = 0.15
        tier_confidence = {1: 0.80, 2: 0.60, 3: 0.35, 4: 0.15}
        new_tsi = tier_confidence.get(tier, 0.15)
        
        player = self.watchlist[player_id]
        # TSI is the maximum of existing TSI and new signal (doesn't drop on rumours)
        player["tsi"] = max(player["tsi"], new_tsi)
        player["rumour_tier"] = tier
        
        # High-confidence rumour: trigger APS recalculation
        if new_tsi >= 0.60 and not player["aps_recalculated"]:
            self._recalculate_aps(player_id)
    
    def _recalculate_aps(self, player_id: str):
        """Recalculate APS when transfer becomes likely."""
        player  = self.watchlist[player_id]
        stack   = requests.get(
            f"{SPORTMIND_API}/stack?use_case=commercial_brief"
        ).json()
        
        # APS calculation would use the commercial brief stack
        # In production: integrate with athlete intelligence API
        player["aps"]              = calculate_aps_from_stack(stack, player["name"])
        player["aps_recalculated"] = True
        
        # Token impact assessment
        if player["current_club_token"]:
            self._assess_selling_club_impact(player)
        if player["target_club_token"]:
            self._assess_buying_club_impact(player)
    
    def confirm_transfer(self, player_id: str, fee: float):
        """Mark transfer as confirmed and generate final token impact report."""
        player = self.watchlist[player_id]
        player["confirmed"] = True
        player["fee"]       = fee
        
        return {
            "player":    player["name"],
            "confirmed": True,
            "fee":       fee,
            "aps":       player.get("aps", "not calculated"),
            "selling_club_token_impact": self._get_selling_impact(player),
            "buying_club_token_impact":  self._get_buying_impact(player)
        }
```

---

## Human escalation principles

All four patterns share the same escalation philosophy:

```
ESCALATE TO HUMAN when:
  1. SMS < 40 on a high-value decision (insufficient intelligence)
  2. Macro override active + major portfolio decision pending
  3. Key player injury confirmed during agentic workflow
  4. Transfer confirmed for high-APS player in watchlist
  5. Signal contradicts itself across two consecutive cycles

COMPLETE AUTONOMOUSLY when:
  1. SMS >= 60 AND no blocking flags AND macro_modifier >= 0.75
  2. Routine portfolio monitoring with no alert conditions
  3. Pre-match T-2h lineup update (no key player changes)
  4. Tournament NCSI calculation (mathematical, not judgement)

NEVER complete autonomously:
  1. Financial execution decisions (always require human approval)
  2. Governance votes (always require human token holder)
  3. Transfer offers (always require club decision-makers)

SportMind generates intelligence and flags conditions.
Humans make decisions.
```

---

## References

- `core/temporal-awareness.md` — Freshness tiers for each data type in workflows
- `platform/sportmind-mcp-server.md` — MCP integration for agentic contexts
- `core/multi-agent-coordination.md` — Multi-agent session management
- `market/international-football-cycle.md` — NCSI weights for Pattern 3
- `fan-token/transfer-signal/` — APS and TSI for Pattern 4


---

## Pattern 7 — Cross-Sport Signal Monitor

**Purpose:** Monitors multiple sport/token signals simultaneously and detects
convergence patterns — when macro conditions, correlated narratives, or event
timing create compound commercial opportunities across different sports.

**Four convergence types:**
- `MACRO_BULL_MULTI_SIGNAL`: bull macro + 3+ actionable tokens → portfolio entry
- `SAME_WINDOW_MULTI_SPORT`: multiple sports with events in 48h → timed entry
- `NCSI_AMPLIFICATION`: national team event spillover into multiple club tokens
- `COUNTER_CYCLE_OPPORTUNITY`: exceptional sport signal in mild bear market

**See:** `examples/agentic-workflows/cross-sport-signal-monitor.md` for full implementation.

*MIT License · SportMind · sportmind.dev*
