# Worked Scenario 2 — UFC 281: Adesanya vs Pereira
## Madison Square Garden · New York · 12 November 2022

**Purpose:** MMA fight week signals, weight cut intelligence, narrative momentum
(revenge fixture), and how fighter-level modifiers interact with token signals.

---

## The event

Israel Adesanya (c) defending the UFC Middleweight Championship against Alex Pereira.
Pereira had defeated Adesanya twice in kickboxing — the revenge narrative was the
dominant story in the lead-up.

**Actual result:** Alex Pereira TKO5 — upset victory; Adesanya dethroned.

---

## Step 1 — Macro check

```
MACRO STATE (November 2022):
  Crypto market: EXTREME BEAR — FTX collapse happened November 8, 4 days before this fight
  BTC 200-day MA: Deeply below — this was the worst week of the 2022 crypto winter
  CHZ price: ~$0.062 (near cycle lows)
  
  MACRO MODIFIER: × 0.55 (crypto extreme bear / capitulation phase)
  
  CRITICAL CONTEXT: FTX collapsed on November 8.
  UFC 281 was November 12. The entire crypto ecosystem was in crisis.
  
  AGENT DECISION: Macro override ACTIVE. Apply ×0.55 to all token signals.
  Prediction market positions unaffected (not crypto-settled in traditional sense).
  Token position sizing: maximum 40% of standard regardless of other signals.
```

---

## Step 2 — Market context

```
LAYER 4: market/market-mma.md
  Fan token tier: TIER 1
  UFC token ecosystem: Most volatile in the library
  Crypto-native fanbase: Highest of any sport
  
  NOTE: FTX collapse makes this one of the worst possible token entry weeks.
  The macro modifier dominates. Signal quality is irrelevant for token sizing.
  Prediction market analysis proceeds normally.
```

---

## Step 3 — Sport domain (sports/mma)

```
FIGHT CARD POSITION:
  Main event, PPV: Maximum signal weight
  Venue: Madison Square Garden — highest-profile US venue
  
FIGHT IMPORTANCE:
  Championship defence: importance_score = 1.00
  
NARRATIVE CONTEXT (Category 1 — Revenge Fixture):
  Pereira defeated Adesanya TWICE in kickboxing:
    2016: KO victory
    2017: Decision victory
  This is their FIRST MMA meeting.
  
  Revenge narrative score: 3/3 (primary narrative — dominant media coverage)
  Modifier: +8% to Adesanya (underdog motivation boost; familiar rival)
  BUT: Pereira's historical dominance creates psychological weight
  Net narrative: Complex — apply BOTH sides
  
  core/core-narrative-momentum.md → Category 1 (revenge)
  AND Category 5 (rivalry intensity — documented historical outcomes exist)
```

---

## Step 4 — Athlete modifier (athlete/mma)

```
FIGHT CAMP SIGNALS:

Israel Adesanya:
  Camp duration: 8 weeks (full, optimal)
  Social activity: HIGH — promotional mode, MSG appearance, normal engagement
  Weight cut: Middleweight limit 185lb; Adesanya typically makes weight comfortably
  Weigh-in result: ON WEIGHT at 185.0lb
  Style profile: Elite kickboxer, excellent movement, ko power
  Form: Dominant title defences × 6 (Vettori, Costa, Romero, Brunson, Cannonier, Whittaker)
  
  ADESANYA PRE-FIGHT MODIFIER:
    Fight camp: Full (optimal) ×1.00
    Weigh-in (made weight cleanly): ×1.05
    Form: 6 consecutive title defences = HOT ×1.10
    Weight cut stress: None ×1.00
    Composite: ×1.155

Alex Pereira:
  Camp duration: 10 weeks (extended; treated as major challenge)
  Social activity: HIGH — aggressive promotional stance
  Weight cut: Career at Middleweight is relatively new; moved up from 185 kickboxing
  Weigh-in result: ON WEIGHT at 185.0lb
  Style profile: Elite kickboxer, known for power (Adesanya KO in their history)
  Form: 3-0 in UFC, all finishes
  
  PEREIRA PRE-FIGHT MODIFIER:
    Fight camp: Extended and focused ×1.02
    Weigh-in (made weight cleanly): ×1.05
    Form: 3-0 UFC all finishes = GOOD ×1.04
    Historical H2H vs Adesanya in kickboxing: × 1.12 (DOCUMENTED wins create confidence modifier)
    Composite: ×1.245

FIGHTER MODIFIER COMPARISON:
  Adesanya: ×1.155 (strong camp, clean weigh-in, excellent form)
  Pereira: ×1.245 (strong camp, historical advantage, finishing record)
  
  Modifier FAVOURS PEREIRA by 0.09 — significant for a fight analysis
  NOTE: This is counterintuitive vs the betting market which had Adesanya -250 favourite
```

---

## Step 5 — MMA token intelligence

```
FAN TOKEN PULSE:
  Token market severely impacted by FTX (macro override already applied)
  HAS for related tokens: SUPPRESSED — holders not engaging in bear market
  
  MACRO OVERRIDE DOMINATES LAYER 3: Apply ×0.55 to all token signals.
  Standard Layer 3 analysis not relevant this week — FTX crisis overrides everything.

FIGHTER TIS:
  Adesanya FighterTIS: 0.85 (one of the highest individual fighter token signals)
  Pereira FighterTIS: 0.42 (newer fighter, smaller token audience)
  
  Even with FTX crisis, this fight would generate some of the highest MMA engagement.
  But token position sizing is capped at 40% of standard due to macro override.

CRI (Career Risk Index):
  Adesanya CRI: LOW (peak career, 33 years old, no retirement signals)
  Pereira CRI: LOW (27 years old, ascending career)
```

---

## Step 6 — Core modifiers

```
FIGHT CAMP CONGESTION:
  Adesanya: Last fight August 2022 (3 months prior) — full rest
  Pereira: Last UFC fight October 2022 (6 weeks prior) — some congestion
  Congestion modifier Pereira: ×0.97

VENUE NARRATIVE:
  MSG main event: elevated narrative, NYC crowd, historically significant venue
  Narrative modifier (MSG factor): ×1.03 for both fighters (event prestige)

HISTORICAL MATCHUP MODIFIER:
  Pereira's 2 KO/W over Adesanya in kickboxing is the defining variable.
  In MMA, the kickboxing record has PARTIAL transferability.
  Apply 60% transfer rate: full kickboxing advantage is ×1.20, transfer = ×1.12
  This is captured in the H2H modifier above.

PREDICTION MARKET SIZING (different from token sizing):
  Macro does NOT override prediction market positions in the same way
  Prediction market sizing: STANDARD (not affected by FTX crypto crisis)
  Signal for prediction market: Pereira × 1.245 > Adesanya × 1.155
  → This was a VALUE POSITION on Pereira at +210 underdog odds
```

---

## SportMind confidence output (pre-fight)

```json
{
  "sportmind_output": {
    "generated_at": "2022-11-12T20:00:00Z",
    "event": {
      "sport": "mma",
      "competition": "UFC 281 — Middleweight Championship",
      "home_team": "Alex Pereira",
      "away_team": "Israel Adesanya (champion)",
      "kickoff_utc": "2022-11-13T03:00:00Z"
    },
    "signal": {
      "base_score": 45.0,
      "adjusted_score": 56.1,
      "direction": "PEREIRA",
      "confidence_tier": "MEDIUM",
      "confidence_pct": 56.1
    },
    "modifiers_applied": {
      "athlete_modifier": 1.245,
      "congestion_modifier": 0.97,
      "narrative_modifier": 1.05,
      "macro_modifier": 1.00,
      "composite_modifier": 1.247
    },
    "flags": {
      "macro_override_active": true,
      "narrative_active": true,
      "token_sizing_override": true
    },
    "reasoning": {
      "primary_signal_driver": "Pereira historical H2H advantage; superior modifier",
      "supporting_factors": [
        "Pereira 2-0 over Adesanya in kickboxing with KO",
        "Extended 10-week camp suggests Pereira team takes H2H seriously",
        "Pereira 3-0 UFC record all by finish — finishing ability present"
      ],
      "risk_factors": [
        "Adesanya MMA form dominant — 6 consecutive title defences",
        "MMA vs kickboxing transferability uncertain",
        "Betting market strongly favours Adesanya (-250)"
      ]
    },
    "sizing": {
      "recommended_action": "ENTER",
      "position_size_pct": 50.0,
      "entry_condition": "Prediction market only — NOT token market (FTX crisis)"
    },
    "token_signal": {
      "applicable": true,
      "token_direction": "NEUTRAL",
      "token_signal_strength": "NONE",
      "relevant_tokens": ["$UFC"],
      "note": "FTX macro override active — max 40% token sizing regardless of signal"
    }
  }
}
```

---

## What actually happened — calibration

```
ACTUAL OUTCOME:
  Result: Pereira TKO5 — Pereira won in the final round

WHAT THE MODEL GOT RIGHT:
  ✅ Direction: Identified Pereira as having the stronger modifier
  ✅ Macro override: FTX collapse correctly applied ×0.55 / cap to token signals
  ✅ Narrative active: Revenge fixture narrative correctly flagged
  ✅ Prediction market value: Pereira at +210 with the model showing 56% probability
     was genuine value (expected value positive)
  ✅ Token separation: Correctly separated prediction market signal from token signal

WHAT THE MODEL MISSED / WOULD CALIBRATE:
  ⚠ Method of victory: Pereira won by TKO in round 5. The model correctly identified
    Pereira's finishing ability (CRI low, finishing rate 100%) but the specific
    late-fight TKO is hard to predict at the modifier level.
  ⚠ Adesanya was WINNING the fight going into round 5. An in-fight recalibration
    would have shown Adesanya pulling ahead through rounds 1-4. SportMind's
    pre-fight framework doesn't model in-fight reversal probability — this is
    a genuine gap for live prediction applications.

CALIBRATION TAKEAWAY FOR DEVELOPERS:
  The macro override correctly capped token positions — this would have protected
  from the FTX-devastated token market. The prediction market signal (Pereira value)
  was correct. The separation between token signals and prediction market signals
  is a critical operational feature of SportMind, and this scenario demonstrates why.
  
  The FTX example also shows: external macro events can completely override internal
  sport signals. A technically correct fight analysis was irrelevant for token sizing
  in November 2022 because the macro context dominated everything else.
```

---

## Key SportMind files used in this scenario

- `macro/macro-crypto-market-cycles.md` — FTX/extreme bear modifier
- `macro/macro-governance-scandal.md` — FTX as crypto governance event
- `market/market-mma.md` — UFC commercial tier
- `sports/mma/sport-domain-mma.md` — fight card hierarchy, event playbooks
- `athlete/mma/athlete-intel-mma.md` — fight camp signals, weight cut, H2H
- `fan-token/mma-token-intelligence/` — FighterTIS, CRI
- `core/core-narrative-momentum.md` — revenge fixture modifier
- `core/confidence-output-schema.md` — output format with macro override flag
