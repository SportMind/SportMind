# Agentic Workflow Pattern 12 — Live Match Agent

**Combines live data feeds with SportMind's pre-match intelligence
for in-play reasoning — adaptive signal updates as match events unfold.**

---

## What this pattern does that others do not

Patterns 2 and 11 handle pre-match and post-match. Pattern 12 handles
the match itself — the 90 minutes (or equivalent) when events are
changing faster than any pre-match model can anticipate.

SportMind is deliberately a pre-match intelligence library. It does not
require live data. Pattern 12 is the bridge that shows developers how to
combine live data feeds (via the connectors in `platform/api-providers.md`)
with SportMind's pre-match framework to reason about evolving match state.

**The key principle:** The pre-match signal is the prior. Live events
are the updates. SportMind's modifier chain determines how large each
update is relative to the prior.

---

## When to trigger

```
TRIGGER: Match is live (confirmed kickoff / bout start / tip-off)
FREQUENCY: Event-driven — fire on significant in-match events:
  → Goal scored / try / basket
  → Red card / sending off / DQ / disqualification
  → Significant injury (player leaves field)
  → Half-time (tactical reset window)
  → VAR/TMO review initiated
  → Substitution of key player
  → Scoreline change that crosses the "must-win" threshold
  
NOT event-by-event: Do not fire on every touch, corner, or free kick.
High-frequency noise will drown the signal.
```

---

## Live event modifier framework

```
LIVE EVENT MODIFIERS — how each in-match event updates the pre-match prior:

GOAL / SCORE EVENT:

  Scored BY the team we assessed as HOME direction:
    +5 SMS if expected (high pre-match confidence)
    +10 SMS if unexpected (low pre-match confidence — more informative)
    Update recommended_action: maintain ENTER if already active

  Scored AGAINST the team we assessed:
    -8 SMS (score is harder to reverse than to extend)
    If now trailing: update direction flag
    If trailing by 2+: trigger MUST_WIN_URGENCY modifier
      → Load core/perceptual-pressure-intelligence.md PPI for key players
      → High PPI teams recover better from deficits

  EQUALISER (comeback scenario):
    Apply core/core-narrative-momentum.md — Comeback narrative
    +6 SMS to trailing team momentum window (15-minute window)

RED CARD / DISQUALIFICATION:

  Red card to team we backed:
    Immediate: -12 SMS (ten vs eleven is statistically decisive)
    Fan token: apply CDI negative event; if ATM player: load
    core/star-departure-intelligence.md void model (temporary)
    VAR/TMO check: provisional modifier × 0.82 until confirmed
    (See core/core-officiating-intelligence.md VAR section)

  Red card to opponent:
    +10 SMS (numerical advantage)
    Fan token: mild positive CDI event

KEY INJURY (player leaves field during match):

  ATM player injured during match:
    Load: core/core-athlete-modifier-system.md replacement quality
    If direct replacement available and of similar tier: -4 SMS
    If no direct replacement: -8 SMS (system disruption)
    Fan token: LTUI uncertainty flag for post-match period

HALF-TIME (tactical reset):

  If scoreline differs from pre-match expected:
    Re-run pre-match chain with updated context
    Load: core/manager-intelligence.md — manager tactical adjustment signals
    Press conference language decoder applies at half-time pitchside:
      "We need to be better" = acknowledgement of problem, not tactical change
      "We've made some adjustments" = actual tactical signal; reload D1 in TMAS

SUBSTITUTION OF KEY PLAYER:

  Tactical substitution (system change):
    Reload core/tactical-matchup-intelligence.md TMAS D1 if system changes
    Example: switching from high press to low block = TMAS reversal
  
  Injury substitution (forced):
    Treat as key injury event above
  
  Protecting a lead substitution (defensive sub):
    +3 SMS for leading team (intent signal — team is managing the game)
```

---

## Live data sources (zero cost options first)

```
FREE / LOW-COST LIVE DATA:

  ESPN / BBC Sport / Sky Sports live score APIs (unofficial):
    Score, scorers, cards, substitutions
    Delay: 30–90 seconds
    Sufficient for: goal events, card events, substitutions
    
  Sofascore unofficial API:
    Detailed live events, lineups, xG live
    Delay: 15–30 seconds
    
  The Odds API (live in-play odds):
    Implied probability moves faster than any other signal
    A sudden 20-point odds swing = market has detected something
    Load: platform/prediction-market-intelligence.md for divergence framework
    
  Twitter/X live:
    Journalists tweet faster than any API
    Load: platform/social-intelligence-connector.md
    Tier 1 journalists (Fabrizio Romano, David Ornstein, Shams Charania):
    their match live-tweets are faster than official APIs

PAID LIVE DATA:

  Sportradar Live: full event stream, real-time xG, possession
  Stats Perform (Opta): same tier
  API-Football (RapidAPI): $15/month for live events
  
  See: platform/api-providers.md for full connection templates
  See: platform/api-connector-examples.md for working connectors

CHILIZ CHAIN LIVE:

  FTP PATH_2 events: monitor on-chain in real time
  Burn transaction detected on Chiliscan = WIN confirmed
  No delay — blockchain finality is faster than any broadcast
  Load: platform/chiliz-chain-address-intelligence.md + 
        fan-token/defi-liquidity-intelligence/ Section 10
        (algorithmic market feedback delay: wait T+15 before applying modifier)
```

---

## Agent implementation

```python
"""
Pattern 12 — Live Match Agent
Combines SportMind pre-match intelligence with live data feeds.
Run Pattern 2 (Pre-Match Chain) before this pattern starts.
"""

import asyncio
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class LiveMatchState:
    pre_match_sms:       int          # from Pattern 2
    pre_match_direction: str          # HOME/AWAY/DRAW
    current_sms:         int          # updated by events
    current_score:       str = "0-0"
    home_eleven:         bool = True
    away_eleven:         bool = True
    match_minute:        int = 0
    events:              list = field(default_factory=list)
    ftp_token:           Optional[str] = None
    ftp_path:            Optional[str] = None

class LiveMatchAgent:
    def __init__(self, state: LiveMatchState):
        self.state = state

    def process_event(self, event: dict) -> dict:
        """Process a live match event and update the signal."""
        event_type = event.get('type')
        team       = event.get('team')     # 'home' or 'away'
        player     = event.get('player')
        minute     = event.get('minute', self.state.match_minute)

        signal_update = {
            'event':       event_type,
            'minute':      minute,
            'sms_before':  self.state.current_sms,
            'sms_after':   self.state.current_sms,
            'flags':       [],
            'action':      None
        }

        if event_type == 'GOAL':
            if team == self.state.pre_match_direction.lower():
                # Scored in our favour
                confidence_gap = 100 - self.state.pre_match_sms
                self.state.current_sms += 5 if confidence_gap < 20 else 10
            else:
                self.state.current_sms -= 8
                if self.is_now_trailing():
                    signal_update['flags'].append('TRAILING')

        elif event_type == 'RED_CARD':
            if team == self.state.pre_match_direction.lower():
                self.state.current_sms -= 12
                signal_update['flags'].append('NUMERICAL_DISADVANTAGE')
                signal_update['action'] = 'CHECK_VAR'  # provisional
            else:
                self.state.current_sms += 10

        elif event_type == 'KEY_INJURY':
            atm_tier = event.get('atm_tier', 'squad')
            sms_delta = {'top_star': -8, 'first_xi': -4, 'squad': -2}
            self.state.current_sms += sms_delta.get(atm_tier, -2)
            signal_update['flags'].append('INJURY_WARNING')

        elif event_type == 'VAR_OVERTURNED':
            # Reverse the provisional modifier
            original_event = event.get('original_event')
            if original_event == 'RED_CARD_HOME':
                self.state.current_sms += 12  # restored
                signal_update['flags'].append('VAR_REVERSAL')
            elif original_event == 'GOAL_HOME':
                self.state.current_sms -= 10  # goal disallowed

        elif event_type == 'HALF_TIME':
            signal_update['action'] = 'RELOAD_TACTICAL_ASSESSMENT'
            signal_update['note'] = 'Re-run TMAS with current score context'

        # Cap SMS
        self.state.current_sms = max(5, min(98, self.state.current_sms))
        signal_update['sms_after'] = self.state.current_sms
        self.state.events.append(signal_update)
        return signal_update

    def is_now_trailing(self) -> bool:
        """Check if team we backed is now trailing."""
        try:
            h, a = map(int, self.state.current_score.split('-'))
            return (h < a if self.state.pre_match_direction == 'HOME'
                    else a < h)
        except Exception:
            return False

    def get_current_signal(self) -> dict:
        """Return current signal with context."""
        return {
            'pre_match_sms':    self.state.pre_match_sms,
            'current_sms':      self.state.current_sms,
            'direction':        self.state.pre_match_direction,
            'score':            self.state.current_score,
            'minute':           self.state.match_minute,
            'signal_drift':     self.state.current_sms - self.state.pre_match_sms,
            'recommended_action': self._get_action(),
            'active_flags':     [e['flags'] for e in self.state.events if e['flags']],
            'sportmind_version':'3.62.0'
        }

    def _get_action(self) -> str:
        sms = self.state.current_sms
        if sms >= 60:   return 'HOLD'    # maintain position
        elif sms >= 40: return 'MONITOR' # watch for further events
        else:           return 'REVIEW'  # signal has weakened significantly
```

---

## Fan token live signal rules

```
FTP PATH_2 LIVE RULES:

  DURING MATCH:
    Signal is pre-match based. Do not apply live score to FTP decision.
    The FTP WIN/LOSS determination is at FULL-TIME only.
    Exception: injury to ATM player → LTUI uncertainty flag (not score-dependent)

  GOAL SCORED (leading to expected WIN):
    Do NOT adjust PATH_2 modifier intra-match.
    Markets will react but the supply change is not confirmed until full-time.
    
  FULL-TIME WIN CONFIRMED:
    T+0: on-chain burn transaction → wait T+15 for algorithmic rebalancing
    T+15: apply full FTP WIN modifier
    See: fan-token/defi-liquidity-intelligence/ Section 10 (algo feedback timing)
    
  FULL-TIME LOSS:
    Supply neutral. Do not apply any negative modifier.
    See: fan-token/gamified-tokenomics-intelligence/ LOSS = supply-neutral rule.

  FRAUD CHECK AT FULL-TIME:
    If significant price movement pre-match was detected as anomalous:
    Load: platform/fraud-signal-intelligence.md MRS check before applying WIN modifier.
```

---

## Connection to other patterns

```
RECEIVES FROM:
  Pattern 2 (Pre-Match Chain)  — pre_match_sms, pre_match_direction, modifiers
  Pattern 8 (FTP Monitor)      — FTP PATH status, pre-liquidation confirmation

FEEDS INTO:
  Pattern 11 (Post-Match Agent) — what happened during match; events log
  Pattern 2 (next fixture)      — condition snapshot update
  community/calibration-data/   — live match as calibration record with
                                  full condition snapshot
  
CALIBRATION OPPORTUNITY:
  Live match agents produce the richest calibration data.
  Include: pre-match state, each event delta, final outcome.
  core/match-condition-snapshot.md — capture full snapshot at pre-match
  and update with in-match events for the most complete historical record.
```

---

*SportMind v3.62 · MIT License · sportmind.dev*
*See: core/tactical-matchup-intelligence.md · core/perceptual-pressure-intelligence.md*
*core/core-officiating-intelligence.md (VAR timing) · platform/fraud-signal-intelligence.md*
*fan-token/defi-liquidity-intelligence/ (Section 10, algo market feedback)*
*platform/api-providers.md · platform/api-connector-examples.md*
