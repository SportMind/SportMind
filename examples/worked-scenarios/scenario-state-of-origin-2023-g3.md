# Worked Scenario 3 — NRL State of Origin Game 3, 2023
## Queensland Maroons vs NSW Blues · Suncorp Stadium · 12 July 2023

**Purpose:** Fixture congestion intelligence (State of Origin disruption), must-win
narrative, and home venue advantage in rugby league context.

---

## The event

State of Origin 2023 Game 3. Series tied 1-1. Queensland hosting the decider
at Suncorp Stadium (Lang Park), Brisbane — a fortress for the Maroons.

**Actual result:** Queensland Maroons 28–12 — series win for QLD.

---

## Step 1 — Macro check

```
MACRO STATE (July 2023):
  Crypto market: Neutral-to-recovering
  BTC 200-day MA: Crossing above (early bull recovery signs)
  CHZ price: ~$0.105 (recovering from 2022 lows)
  
  Macro modifier: × 1.00 (neutral — no active macro events)
  Agent decision: No macro override. Proceed normally.
```

---

## Step 2 — Market context

```
LAYER 4: market/market-rugby-league.md
  Fan token tier: TIER 2 — near-term credibility, no active major tokens
  
  This is a prediction market scenario primarily.
  State of Origin has no active fan tokens at this event.
  Layer 3 (fan token intelligence): NOT APPLICABLE for this event.
  
  Commercial context: State of Origin is the highest-profile rugby league event
  in the world. This is the peak commercial window for NRL-related markets.
```

---

## Step 3 — Sport domain (sports/rugby-league)

```
EVENT IMPORTANCE:
  State of Origin Game 3 (series decider): Maximum importance = 1.00
  
APPLICABLE PLAYBOOK:
  Playbook 4 (State of Origin Game 3 — decider):
  Trigger: Series tied 1-1; Game 3 at Brisbane
  Filter: Key players confirmed (check Origin availability carefully)
  Sizing: 1.4× standard — highest-intensity single match in rugby league
  
HOME ADVANTAGE:
  Suncorp Stadium (Brisbane): QLD fortress
  Queensland home record in State of Origin at Suncorp: historically dominant
  Home advantage modifier in State of Origin: documented +4–6% for QLD
  
MUST-WIN CONTEXT:
  Both teams in must-win: Modifier applies to both
  Game 3 decider at venue = MAXIMUM motivational signal for both teams
  Apply: core-narrative-momentum.md → Category 7 (elimination/must-win) both teams
```

---

## Step 4 — Athlete modifier (athlete/rugby-league)

```
CONGESTION ANALYSIS (most important Layer 2 factor for State of Origin):
  State of Origin players compete in Origin midweek AND NRL weekends.
  Game 3 (12 July) follows NRL Round 19 (8-9 July) — 3-4 days between.
  
  NRL clubs with highest Origin representation:
    Melbourne Storm: 4 players (2 QLD, 2 NSW)
    Penrith Panthers: 5 players (4 NSW, 1 QLD)
    Brisbane Broncos: 4 players (4 QLD)
    
  Load: core/core-fixture-congestion.md → State of Origin congestion section
  
  FOR QUEENSLAND:
    Key players: Daly Cherry-Evans (c), Cameron Munster, Kalyn Ponga, Patrick Carrigan
    All played NRL Round 19: Tier 2 CONGESTION → ×0.93 modifier
    
    BUT: Suncorp home advantage OFFSETS congestion for Queensland
    Home advantage: ×1.05
    Net modifier after offset: ×0.93 × 1.05 = ×0.977

  FOR NSW BLUES:
    Key players: Nathan Cleary (c), Latrell Mitchell, Cameron Murray, Jarome Luai
    Also played Round 19: Tier 2 CONGESTION → ×0.93 modifier
    
    Away from home at Suncorp: ×0.96 (away disadvantage)
    Net modifier after offset: ×0.93 × 0.96 = ×0.893

PLAYER AVAILABILITY:
  Queensland: Full squad available; no injury concerns
  NSW Blues: Cameron Murray (hamstring): DOUBT → ×0.85 for NSW
  
PAS (Player Availability Score) calculation:
  QLD overall PAS: 0.92 (full squad, minor congestion)
  NSW overall PAS: 0.81 (congestion + Murray doubt)

QLD COMPOSITE MODIFIER: ×1.12 (PAS + home advantage)
NSW COMPOSITE MODIFIER: ×0.87 (PAS + away + Murray doubt)

MODIFIER DIFFERENTIAL: +0.25 in QLD's favour
This is a LARGE differential — agent should recognise high confidence signal.
```

---

## Step 5 — No Layer 3 (no active tokens for this event)

```
LAYER 3 STATUS: NOT APPLICABLE
Rugby league is Tier 2 — no active Socios/Chiliz tokens for NRL or State of Origin.

PREDICTION MARKET ONLY:
  This scenario is entirely prediction market focused.
  No token position sizing considerations.
  No fan-token-pulse, no HAS/TVI, no FTIS applicable.
  
  Agent should load: market/market-rugby-league.md for commercial context only.
  All token Layer 3 skills: skip.
```

---

## Step 6 — Core modifiers

```
NARRATIVE MOMENTUM:
  Both teams in must-win scenario: +4% for both (equal; cancels out)
  QLD home fortress narrative: +3% for QLD specifically
  Net narrative advantage: +3% QLD

OFFICIATING:
  State of Origin referee: Experienced NRL referees assigned
  No specific referee modifier applicable without individual assignment data

WEATHER:
  Brisbane July: Typical temperature 15–21°C; evening match
  July is Brisbane's dry season — no weather risk
  Weather modifier: ×1.00

FINAL COMPOSITE (QLD): ×1.12 × 1.03 = ×1.154
FINAL COMPOSITE (NSW): ×0.87 (no positive narrative offsets)
```

---

## SportMind confidence output (pre-match)

```json
{
  "sportmind_output": {
    "generated_at": "2023-07-12T16:00:00Z",
    "event": {
      "sport": "rugby_league",
      "competition": "NRL State of Origin 2023 — Game 3",
      "home_team": "Queensland Maroons",
      "away_team": "NSW Blues",
      "kickoff_utc": "2023-07-12T09:50:00Z",
      "venue": "Suncorp Stadium, Brisbane"
    },
    "signal": {
      "base_score": 58.0,
      "adjusted_score": 66.9,
      "direction": "HOME",
      "confidence_tier": "HIGH",
      "confidence_pct": 66.9
    },
    "modifiers_applied": {
      "athlete_modifier": 1.12,
      "congestion_modifier": 0.97,
      "narrative_modifier": 1.03,
      "weather_modifier": 1.00,
      "macro_modifier": 1.00,
      "composite_modifier": 1.154
    },
    "layer_inputs": {
      "layer_5_macro_active": false,
      "layer_4_market_tier": 2,
      "layer_3_on_chain_loaded": false,
      "layer_2_athlete_loaded": true,
      "layer_1_domain_loaded": true
    },
    "flags": {
      "injury_warning": true,
      "congestion_warning": true
    },
    "reasoning": {
      "primary_signal_driver": "QLD home advantage + NSW congestion + Murray doubt",
      "supporting_factors": [
        "Suncorp Stadium historical QLD win rate in deciders",
        "NSW Blues carrying congestion without home advantage offset",
        "Cameron Murray doubt weakens NSW defensive structure"
      ],
      "risk_factors": [
        "State of Origin variance is always high — upsets frequent in deciders",
        "NSW Cleary/Luai combination can override structural disadvantages"
      ]
    },
    "sizing": {
      "recommended_action": "ENTER",
      "position_size_pct": 90.0,
      "note": "Prediction market only — no active tokens for this sport"
    },
    "token_signal": {
      "applicable": false,
      "note": "Rugby league is Tier 2 — no active fan tokens at this time"
    }
  }
}
```

---

## What actually happened — calibration

```
ACTUAL OUTCOME:
  Result: QLD 28–12 — comfortable Queensland victory

WHAT THE MODEL GOT RIGHT:
  ✅ Direction: HOME — QLD won by 16 points
  ✅ Confidence tier: HIGH — comfortable victory, not a close game
  ✅ Layer 3 correctly excluded: No token signals available or applicable
  ✅ Congestion warning flagged: Both teams carried NRL fatigue
  ✅ Home advantage correctly weighted: Suncorp was decisive factor
  ✅ Injury warning (Murray): NSW's defensive structure was compromised without him
  ✅ No macro override: Neutral crypto market correctly applied

WHAT THE MODEL MISSED / WOULD CALIBRATE:
  ⚠ Margin of victory (28–12) was larger than the 1.154 composite suggested.
    The congestion offset for QLD at home may be UNDERSTATED. Queensland's
    home recovery advantage is psychologically larger than the formula captures.
  ⚠ Nathan Cleary's kicking game: Was below his normal level — this wasn't
    flagged in the pre-match assessment. Weather was clear but Cleary's
    performance in the context of a Brisbane away fixture could have its
    own modifier (away kicking accuracy at Suncorp historically lower).

CALIBRATION TAKEAWAY FOR DEVELOPERS:
  State of Origin is the scenario that best demonstrates CONGESTION INTELLIGENCE
  specifically — the Layer 2 congestion modifier was the decisive differentiator
  here, not team form or individual player quality alone. Both teams had similar
  talent levels; the congestion asymmetry (QLD offset by home, NSW not offset)
  created the structural advantage that the framework correctly identified.
  
  Also demonstrates: When Layer 3 is not applicable (Tier 2 sport, no tokens),
  the framework still produces high-quality prediction market signals using
  only Layers 1, 2, 4, and 5.
```

---

## Key SportMind files used in this scenario

- `market/market-rugby-league.md` — Tier 2 commercial context
- `sports/rugby-league/sport-domain-rugby-league.md` — State of Origin playbook
- `athlete/rugby-league/athlete-intel-rugby-league.md` — PAS, Origin modifier
- `core/core-fixture-congestion.md` — State of Origin congestion framework
- `core/core-narrative-momentum.md` — must-win/elimination modifier
- `core/confidence-output-schema.md` — output with Layer 3 not applicable
