# Worked Scenario 5 — NBA Trade Deadline 2023: Kevin Durant to Phoenix Suns
## February 9, 2023 — Trade Deadline Signal Analysis

**Purpose:** NBA player-centric signal model, trade deadline intelligence, NBATIS
in practice, and how a Tier 1 player move generates immediate token and prediction
market signals completely independent of any sporting event.

---

## The event

Kevin Durant traded from Brooklyn Nets to Phoenix Suns on February 9, 2023.
Package: Mikal Bridges, Cam Johnson, Jae Crowder, four first-round picks, one pick swap.

This is a pure signal event — no game was played. The trade is the signal.

**Commercial outcome:** Suns became immediate NBA Championship contenders.
Nets became a rebuilding team. All associated prediction markets repriced within hours.

---

## Step 0 — The NBA player-centric model (foundational)

```
CRITICAL RULE FOR NBA AGENTS:
  Unlike football where club tokens dominate, NBA commercial value is INDIVIDUAL.
  Kevin Durant is a Tier 1 player — the signal weight from his move is
  60–70% of the total team signal, not a component of it.
  
  Apply: basketball-token-intelligence.md → Tier 1 player taxonomy
  KD Status: Tier 1 (top-3 global recognition; future Hall of Famer)
  
  Trade signal formula:
    Receiving team (Suns): +15–35% token/franchise sentiment
    Trading team (Nets): -20–40% franchise sentiment (losing franchise player)
```

---

## Step 1 — Macro check

```
MACRO STATE (February 9, 2023):
  Crypto market: Early recovery phase (post-FTX lows)
  BTC: ~$21,500 — below 200-day MA (still in bear territory)
  CHZ: ~$0.075 — recovering but below mid-2022 levels
  
  MACRO MODIFIER: × 0.82 (bear market; BTC below 200-day MA = ×0.75 base,
    but recovery trajectory in February 2023 was visible → moderate bear ×0.82)
  
  Agent decision: Macro modifier active but not severe. Token signals dampened
  but not eliminated. Trade event is large enough to partially override macro.
```

---

## Step 2 — Market context

```
LAYER 4: market/market-basketball.md
  Fan token tier: TIER 1 commercially; limited active Socios tokens at time
  NBA Top Shot: $1B+ precedent — fan base demonstrated willingness to buy digital NBA assets
  Prediction markets: DraftKings, FanDuel, various offshore books all active
  
  NBA Championship odds: Standard prediction market — active markets on all books
  
  COMMERCIAL CONTEXT:
    KD arrival transforms Suns from fringe contender to co-favourite
    Suns pre-trade odds: +1800 (implied ~5% championship probability)
    Suns post-trade odds: +550 (implied ~15% championship probability)
    Odds movement = 3× implied probability improvement
```

---

## Step 3 — NBATIS calculation

```
NBATIS for KD → Phoenix Suns:

NBATIS = (Game_Importance × 0.35) + (Star_Player_Status × 0.30)
        + (Playoff_Position × 0.20) + (Market_Sentiment × 0.15)

This is NOT a game event — it is a ROSTER EVENT.
For roster events, apply the trade signal override framework:

KD Trade Signal Framework:
  Player tier: TIER 1 (×1.00 maximum weight)
  Trade direction: ACQUISITION (receiving team positive)
  Trade urgency: PACKAGE SIZE (4 first-round picks = maximum conviction from Suns)
  
  Suns signal: +25% franchise sentiment (within +15–35% Tier 1 range)
  Nets signal: -30% franchise sentiment (within -20–40% losing franchise player)
  
  Star player trade → OVERRIDES standard game-based NBATIS calculation
  Use: Trade Signal Model (basketball-token-intelligence.md)

TIMING SIGNAL:
  Trade reported: February 9, ~2pm ET
  Market hours: Active (NBA season in progress, games that evening)
  
  SIGNAL VELOCITY:
    First 15 minutes: Rumour → Verified reporter confirmation (Woj/Shams)
    15–60 minutes: Trade officially processed; market repricing begins
    1–3 hours: Prediction market odds fully adjusted
    24–48 hours: Token/franchise sentiment fully absorbed
    
    Agent action window: Verified reporter confirmation (Woj tweet)
    → This is the entry point; official confirmation comes later
```

---

## Step 4 — Athlete modifier (NBA player-centric)

```
PRE-TRADE ASSESSMENT:

Kevin Durant profile:
  Availability: CONFIRMED (healthy — no major injury at trade)
  Form: KD scoring 29.7 PPG for Brooklyn (elite form)
  Impact: Net Rating +8.1 with KD on court for Brooklyn
  Fit with Phoenix: 
    Devin Booker + Chris Paul + KD = three-star lineup
    Fit assessment: KD is a natural scoring complement to Booker
    Chris Paul (point guard): Elite orchestration of KD's scoring opportunities
    Mikal Bridges leaving: Defensive anchor departs — net defensive loss for Suns
  
  KD athlete modifier for Phoenix: ×1.20 (full elite availability; top form; strong fit)
  
  Phoenix without KD (pre-trade context): Devin Booker ×1.10 (All-Star level)
  Phoenix WITH KD post-trade: Combined × AMPLIFIED — three elite players

LOAD MANAGEMENT CONSIDERATION:
  Trade mid-season: KD will need time to integrate new system
  Estimated 5–10 game integration window: slight uncertainty on immediate impact
  Integration modifier: First 5 games × 0.95 (system learning period)
  From game 6 onwards: Full modifier applies
```

---

## Step 5 — Signal output (trade event)

```
TRADE EVENT SIGNAL ANALYSIS:
  Event type: Roster event (not game event)
  Signal type: Franchise-level; championship probability
  
  Primary signals generated:
  
  1. CHAMPIONSHIP ODDS SIGNAL:
     Suns: +1800 → +550 (immediate 3× probability improvement)
     Signal: STRONG POSITIVE for Suns championship position
     Confidence: HIGH (Tier 1 player; large trade package = Suns conviction)
  
  2. SEASON WIN TOTAL SIGNAL:
     Suns win total pre-trade: ~47.5 wins
     Suns win total post-trade: ~52.5 wins (+5 win adjustment expected)
     Signal: POSITIVE; bet season win totals if market slow to adjust
  
  3. INDIVIDUAL AWARD SIGNALS:
     KD: Scoring title odds improve (he is on a new team with offensive opportunities)
     Devin Booker: Potential assists increase (off-ball player next to KD)
     
  4. DEPARTURE SIGNAL (Nets):
     Mikal Bridges: Now primary Nets scorer → individual stats improve
     Nets championship: Near-zero; rebuild signal
     Nets win total: Drops significantly
```

---

## SportMind confidence output (trade event)

```json
{
  "sportmind_output": {
    "generated_at": "2023-02-09T19:30:00Z",
    "event": {
      "sport": "basketball",
      "competition": "NBA 2022-23 Season — Trade Analysis",
      "home_team": "Phoenix Suns (KD acquiring)",
      "away_team": "Brooklyn Nets (KD departing)",
      "kickoff_utc": "N/A — roster event",
      "venue": "N/A"
    },
    "signal": {
      "base_score": 50.0,
      "adjusted_score": 74.5,
      "direction": "PHOENIX_SUNS",
      "confidence_tier": "HIGH",
      "confidence_pct": 74.5
    },
    "modifiers_applied": {
      "athlete_modifier": 1.20,
      "trade_signal_override": 1.25,
      "integration_period_discount": 0.95,
      "macro_modifier": 0.82,
      "composite_modifier": 1.177
    },
    "flags": {
      "macro_override_active": false,
      "narrative_active": true,
      "trade_event": true,
      "integration_window_active": true
    },
    "reasoning": {
      "primary_signal_driver": "Tier 1 player acquisition — Kevin Durant to Phoenix",
      "supporting_factors": [
        "KD + Booker + Paul = three-star lineup; rare in NBA",
        "Championship odds improved 3× (1800 → 550)",
        "Suns gave maximum package (4 picks) = maximum conviction signal",
        "Reporter verification (Woj/Shams confirmed): highest reliability tier"
      ],
      "risk_factors": [
        "Integration period: 5–10 game adjustment window",
        "Mikal Bridges departing: significant defensive loss",
        "Macro modifier active (×0.82): bear crypto market dampens token signals",
        "Chris Paul injury history: durability risk for three-star lineup"
      ],
      "abstain_reason": null
    },
    "sizing": {
      "recommended_action": "ENTER",
      "position_size_pct": 75.0,
      "entry_condition": "Verified reporter (Woj/Shams) confirmation only",
      "exit_condition": "Reassess after 10 games with KD in lineup"
    },
    "token_signal": {
      "applicable": true,
      "token_direction": "POSITIVE",
      "token_signal_strength": "MODERATE",
      "relevant_tokens": ["$NBA_SUNS_IF_EXISTS"],
      "note": "Macro modifier (×0.82) dampens token signal; prediction market stronger signal"
    }
  }
}
```

---

## What actually happened — calibration

```
ACTUAL OUTCOME:
  Suns did advance to the second round of the 2023 playoffs before being eliminated
  by the Denver Nuggets (who went on to win the championship).
  
  The immediate market repricing was correct — Suns became championship co-favourites.
  
  What changed post-trade and tested the model:
    Chris Paul injury: Suns lost Paul for the playoff run (injury concern flagged)
    KD adaptation: Integration period was real — first 10 games below full impact
    Ultimate result: Suns didn't win — trade value took 2–3 seasons to fully materialise

WHAT THE MODEL GOT RIGHT:
  ✅ Direction: PHOENIX SUNS positive (correct)
  ✅ Trade signal: Tier 1 acquisition → +25% franchise sentiment (market confirmed this)
  ✅ Reporter reliability: Verified Woj/Shams before entry (correct protocol)
  ✅ Integration window: Correctly flagged 5–10 game adjustment period
  ✅ Macro modifier: ×0.82 correctly dampened token signals in bear market
  ✅ Chris Paul durability: Correctly listed as risk factor

WHAT THE MODEL SHOWS FOR NBA AGENTS:
  1. SEPARATE immediate vs long-term signals.
     The immediate odds repricing was the correct signal to act on.
     Championship likelihood is a multi-season assessment — not a single-game event.
     
  2. REPORTER VERIFICATION IS THE ENTRY TRIGGER.
     Entering on unverified rumour is the primary NBA trade deadline risk.
     Wait for Woj or Shams confirmation — these are the highest-reliability sources
     in the entire SportMind library for any sport.
     
  3. MACRO MODIFIER APPLIES TO TOKENS, NOT PREDICTION MARKETS.
     The prediction market signal (championship odds repricing) was strong and correct.
     The token signal was damped by ×0.82. Separating these correctly is critical.

CALIBRATION TAKEAWAY FOR DEVELOPERS:
  NBA trade deadline (February) is one of the highest-signal periods in the library.
  The player-centric model is correct — KD moving created more signal than any
  individual game result. Agents operating in NBA markets need real-time
  reporter monitoring (Twitter/X for Woj and Shams) more than any data platform.
  The entry trigger is reporter verification, not official NBA confirmation.
```

---

## Key SportMind files used in this scenario

- `fan-token/basketball-token-intelligence/` — NBATIS, player-centric model, trade signals
- `macro/macro-crypto-market-cycles.md` — bear market modifier
- `market/market-basketball.md` — NBA commercial tier, Top Shot precedent
- `sports/basketball/sport-domain-basketball.md` — trade deadline calendar
- `athlete/nba/athlete-intel-nba.md` — load management, on/off splits, fit assessment
- `core/core-narrative-momentum.md` — championship narrative activation
- `core/confidence-output-schema.md` — output with trade_event flag

---

*Based on publicly reported trade details and market data. Prediction market
odds movements approximate. No proprietary trading data used.*
