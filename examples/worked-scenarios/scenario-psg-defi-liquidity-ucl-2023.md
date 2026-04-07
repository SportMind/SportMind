# Worked Scenario 6 — DeFi Liquidity Signal: $PSG Token Pre-UCL Quarter-Final 2023
## PSG vs Bayern Munich · Parc des Princes · 11 April 2023

**Purpose:** Demonstrates DeFi intelligence — liquidity check, LP activity as pre-signal,
and how thin liquidity changes execution even when signal quality is high.

---

## The event

PSG vs Bayern Munich, UEFA Champions League Quarter-Final first leg.
PSG had qualified through knockout stages; high commercial engagement expected.

**Actual result:** PSG 0–1 Bayern Munich (Choupo-Moting 60')

---

## Step 0 — DeFi pre-check (runs BEFORE other layers for token analysis)

```
LIQUIDITY CHECK (defi-liquidity-intelligence.md):

$PSG token primary venue: Binance (CEX) — primary
$PSG/CHZ pool on Chiliz DEX: Secondary but check TVL

Pool TVL check (11 April 2023):
  Binance order book depth (±2%): ~$420,000 on the bid side
  Chiliz DEX $PSG/CHZ pool TVL: ~$185,000
  
LIQUIDITY FLAGS:
  Chiliz DEX pool: TVL $185,000 → LIQUIDITY_CRITICAL flag active
  Binance depth: $420,000 within 2% → LIQUIDITY_WARNING threshold (< $500k)
  
SLIPPAGE ESTIMATE (for $10,000 position on Chiliz DEX):
  estimated_impact = $10,000 / ($185,000/2) × 100 = 10.8%
  → 10.8% slippage = ABSTAIN on DEX execution
  
EXECUTION DECISION:
  DEX execution: ABSTAIN (slippage 10.8% > 3% threshold)
  CEX execution (Binance): Feasible but warning-level depth
  → Maximum position size: 40% of standard (liquidity_warning active on CEX)
  
LP ACTIVITY SIGNAL:
  48h pre-match LP activity on Chiliz DEX: Large LP addition detected
  Wallet cluster of 3 wallets added ~$45,000 to $PSG/CHZ pool
  → This is pre-event accumulation signal: POSITIVE supplementary signal
  
DEFI CONTEXT OBJECT:
  primary_venue: CEX
  pool_tvl_usd: 185000 (DEX), ~420000 effective (CEX depth)
  estimated_slippage_pct: 10.8 (DEX), ~2.4 (CEX for $10k position)
  lp_activity_signal: ACCUMULATION (large LP addition 48h pre-match)
  lifecycle_phase: 3 (active utility but approaching plateau indicators)
```

---

## Step 1 — Macro check

```
MACRO STATE (April 2023):
  Crypto market: Neutral-to-recovering (post-winter recovery underway)
  BTC 200-day MA: Crossing above — early bull signal
  CHZ price: ~$0.118 (recovering)
  
  Macro modifier: × 1.00 (neutral)
  No macro override.
```

---

## Step 2 — Market context

```
LAYER 4: market/market-football.md
  $PSG: Tier 1 token (active, full Layer 3 applicable)
  PSG is also a Chiliz Chain VALIDATOR (see blockchain-validator-intelligence.md)
  → Apply validator-adjusted PHS: VSI = 1.0 (stable validator stake confirmed)
  → Validator-Adjusted PHS = 0.82 (above threshold for full Layer 3)
```

---

## Step 3 — Sport domain (sports/football)

```
COMPETITION TIER:
  UCL Quarter-Final: Tier 1, importance_score = 0.85
  
MATCH IMPORTANCE:
  base_weight: 1.00
  stakes_multiplier: 1.15 (UCL knockout; elimination risk)
  importance_score: 0.978

NARRATIVE:
  PSG vs Bayern: historical rivalry context
  PSG had been eliminated by Bayern in several recent UCL campaigns
  Narrative: Category 1 (revenge) + Category 7 (elimination pressure)
  Narrative modifier: +5% (PSG at home, revenge context)
```

---

## Step 4 — Athlete modifier

```
PRE-MATCH SQUAD STATUS:

PSG key players:
  Kylian Mbappé: CONFIRMED fit → ATM = 0.35 (highest single-player ATM at PSG)
  Neymar Jr: DOUBTFUL (ankle concern) → Availability ×0.85
  Marco Verratti: CONFIRMED fit → Midfielder ×1.02
  Gianluigi Donnarumma (GK): CONFIRMED fit → ×1.05
  
PSG COMPOSITE: ×1.04 (Mbappé confirmed offsets Neymar doubt partially)

Bayern key players:
  Thomas Müller: CONFIRMED fit
  Sadio Mané: CONFIRMED fit but lower form (difficult first season at Bayern)
  Manuel Neuer: OUT (season-ending injury in December — Sven Ulreich starting)
  
  Neuer absence is a KNOCKOUT CONDITION for goalkeeping:
  → Bayern goalkeeper modifier: ×0.80 (backup starting vs world-class regular)
  
BAYERN COMPOSITE: ×0.87 (Neuer out significantly weakens their modifier)

NOTE: This is interesting — Bayern's squad modifier was LOWER than PSG's
pre-match despite Bayern being the betting favourite.
```

---

## Step 5 — Fan token intelligence (Layer 3)

```
FAN TOKEN PULSE ($PSG):
  HAS: 72/100 — above average (UCL quarter-final driving engagement)
  TVI: Elevated — 48h trading volume above 30-day average by 2.4×
  Geographic: Concentrated France, Qatar, Southeast Asia
  LP activity: ACCUMULATION signal from Step 0 confirms on-chain conviction

ATHLETE SOCIAL LIFT:
  Mbappé AELS: 0.91 — highest in football at time of match
  Neymar AELS: 0.73 — but doubtful; uncertainty suppresses signal

FOOTBALL TOKEN INTELLIGENCE:
  FTIS (UCL Quarter-Final): 0.82
  ATM (Mbappé): 0.35 → Mbappé availability is critical for token signal
  NCSI: French national team spillover adds +0.04

BLOCKCHAIN VALIDATOR CONTEXT:
  PSG is a Chiliz Chain validator (blockchain-validator-intelligence.md)
  VSI = 1.0 (stable stake; no withdrawal activity detected)
  Validator-Adjusted PHS = 0.82 × 1.10 = 0.902 → HEALTHY (full Layer 3 applicable)
  
  This means: even in UCL exit scenario, PSG's validator stake suggests
  continued institutional commitment to Chiliz Chain.
  Token lifecycle: Phase 3 (active utility, healthy partnership)
```

---

## Step 6 — Core modifiers

```
CONGESTION:
  PSG last match: Ligue 1 (8 April) — 3 days prior
  Tier 2 MODERATE congestion: ×0.97

OFFICIATING: Standard modifier ×1.00 (no specific referee data)

WEATHER: Parc des Princes April: ~15°C, light rain possibility
  Mild rain modifier: ×0.98 for both teams

NARRATIVE: +5% PSG (revenge + home)

COMPOSITE (PSG signal): ×1.04 × 0.97 × 0.98 × 1.05 × 1.00 = ×1.047
```

---

## SportMind confidence output (pre-match)

```json
{
  "sportmind_output": {
    "generated_at": "2023-04-11T17:00:00Z",
    "event": {
      "sport": "football",
      "competition": "UEFA Champions League Quarter-Final",
      "home_team": "PSG",
      "away_team": "Bayern Munich",
      "kickoff_utc": "2023-04-11T19:00:00Z",
      "venue": "Parc des Princes, Paris"
    },
    "signal": {
      "base_score": 62.0,
      "adjusted_score": 64.9,
      "direction": "HOME",
      "confidence_tier": "MEDIUM",
      "confidence_pct": 64.9
    },
    "modifiers_applied": {
      "athlete_modifier": 1.04,
      "congestion_modifier": 0.97,
      "weather_modifier": 0.98,
      "narrative_modifier": 1.05,
      "macro_modifier": 1.00,
      "composite_modifier": 1.047
    },
    "flags": {
      "injury_warning": true,
      "liquidity_warning": true,
      "liquidity_critical": false,
      "narrative_active": true
    },
    "defi_context": {
      "primary_venue": "CEX",
      "pool_tvl_usd": 185000,
      "estimated_slippage_pct": 10.8,
      "lp_activity_signal": "ACCUMULATION",
      "yield_apr_pct": 2.1,
      "lifecycle_phase": 3
    },
    "reasoning": {
      "primary_signal_driver": "PSG home advantage + Mbappé confirmed + Bavaria GK weakness",
      "supporting_factors": [
        "LP accumulation signal: informed wallets buying exposure pre-match",
        "PSG validator status: institutional commitment remains strong",
        "Narrative: revenge fixture vs Bayern gives PSG motivation edge"
      ],
      "risk_factors": [
        "Neymar doubt — reduces PSG attacking options",
        "Liquidity warning: thin pool limits token position execution",
        "Thin order book depth on Binance (< $500k) — max 40% standard position"
      ]
    },
    "sizing": {
      "recommended_action": "ENTER",
      "position_size_pct": 40.0,
      "entry_condition": "CEX execution only — DEX slippage 10.8% makes DEX ABSTAIN",
      "note": "liquidity_warning active: max 40% of standard position regardless of signal"
    },
    "token_signal": {
      "applicable": true,
      "token_direction": "POSITIVE",
      "token_signal_strength": "MODERATE",
      "relevant_tokens": ["$PSG", "$CHZ"],
      "note": "LP accumulation signal is supplementary positive; thin liquidity caps execution"
    }
  }
}
```

---

## What actually happened — calibration

```
ACTUAL OUTCOME:
  Result: PSG 0–1 Bayern (Choupo-Moting 60')
  PSG lost despite home advantage and perceived squad strength
  $PSG token response: −9.2% over 24h post-match
  
WHAT THE MODEL GOT RIGHT:
  ✅ Liquidity warning correctly applied: Position was capped at 40%
     → The actual $PSG decline of −9.2% was painful but halved in impact
     by the reduced position size. Correct execution saved significant loss.
  ✅ LP accumulation signal noted but correctly weighted as supplementary only
     → LP additions don't predict match outcomes; they predict conviction to hold
     → The accumulation wallets likely held through the loss (prediction market use)
  ✅ Neymar injury_warning was correct: He did not play; PSG attack was impaired
  ✅ Validator status correctly noted: PSG stake remained stable post-match
     → Institutional commitment unaffected by UCL result

WHAT THE MODEL MISSED / WOULD CALIBRATE:
  ⚠ Direction was wrong (said HOME but away Bayern won)
    The model's moderate confidence (64.9%) was appropriate — this was not
    a high confidence call. MEDIUM confidence + injury_warning + liquidity_warning
    should signal caution even when direction indicator is positive.
  ⚠ Bayern's tactical setup without Neuer: Despite GK weakness, their
    outfield organisation negated PSG's attack. The goalkeeper knockout
    condition (×0.80) should not fully negate Bayern's overall tactical quality.
    A team-level tactical modifier (separate from individual availability)
    would have refined this.

KEY DEFI LESSON FOR DEVELOPERS:
  The DeFi liquidity check SAVED THE POSITION from being a full-size loss.
  Even when a signal is wrong (PSG lost), having capped the position at 40%
  due to liquidity_warning is the correct risk management response.
  
  DeFi intelligence is NOT about improving signal accuracy.
  It is about PROTECTING capital when signals turn out to be wrong.
  This is its correct role in the SportMind framework.
  
  The LP accumulation signal was also instructive: it showed ON-CHAIN CONVICTION
  from sophisticated wallets — but on-chain conviction ≠ match outcome prediction.
  Those wallets may have been providing liquidity for prediction market use,
  not betting on PSG to win.
```

---

## Key SportMind files used in this scenario

- `fan-token/defi-liquidity-intelligence/` — liquidity check, TVL, slippage
- `fan-token/blockchain-validator-intelligence/` — PSG validator status, VSI
- `fan-token/fan-token-partnership-intelligence/` — Validator-Adjusted PHS
- `fan-token/football-token-intelligence/` — FTIS, ATM (Mbappé), NCSI
- `core/core-fixture-congestion.md` — 3-day turnaround congestion
- `core/core-narrative-momentum.md` — revenge + elimination narrative
- `core/confidence-output-schema.md` — defi_context object output
