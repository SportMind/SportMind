# SportMind Score — Unified Cross-Sport Confidence Metric

**The single number that represents SportMind's aggregate confidence in any analysis,
comparable across all sports, all token types, and all agent use cases.**

---

## Why a unified score matters

The adjusted_score in the confidence output schema tells you how confident SportMind
is about a specific event with a specific sport's signal weights applied. It answers:
"For a football match, is this signal strong?"

The SportMind Score answers a different question: "Across all the intelligence
SportMind has applied — sport domain, athlete, on-chain, macro, liquidity — how
much of the available intelligence was loaded and what is the combined quality?"

```
ADJUSTED_SCORE (existing):
  How strong is the signal for this specific event?
  Bounded by: sport signal weights + modifier pipeline
  Comparable within: one sport, one analysis type

SPORTMIND SCORE (new):
  How complete and reliable is this analysis?
  Bounded by: all layers loaded + data freshness + flag states
  Comparable across: all sports, all event types, all token categories

Example:
  Football analysis with full 5 layers: SMS = 91
  Football analysis with L1 only (no athlete data, no on-chain): SMS = 48
  Same base signal (72) — very different reliability
```

---

## The SportMind Score formula

```
SMS = (Layer_Coverage × 0.35) + (Data_Freshness × 0.25)
    + (Flag_Health × 0.25) + (Modifier_Confidence × 0.15)

All components scored 0–100. SMS output: 0–100.

SMS ≥ 80: HIGH QUALITY — full intelligence; act with confidence
SMS 60–79: GOOD — most intelligence loaded; minor gaps
SMS 40–59: PARTIAL — significant gaps; results directionally useful
SMS < 40: INCOMPLETE — minimum intelligence only; treat as preliminary
```

### Component 1 — Layer Coverage (35% weight)

```
Measures: How many of the five layers were loaded for this analysis

SCORING:
  Layer 5 (macro) loaded:    +12 points
  Layer 4 (market) loaded:   +10 points
  Layer 1 (domain) loaded:   +30 points  ← always required
  Layer 2 (athlete) loaded:  +28 points
  Layer 3 (on-chain) loaded: +20 points  ← only if Tier 1 sport

Maximum for Tier 1 sport: 100 (all 5 layers)
Maximum for Tier 2-4 sport: 80 (layers 5,4,1,2 only; no active tokens)
Maximum for domain-only query: 30 (L1 only)

NORMALISE: divide raw score by maximum for this sport's tier
```

### Component 2 — Data Freshness (25% weight)

```
Measures: How current is the live signal data used in this analysis

SCORING:
  Macro state (BTC/CHZ check): < 6h old: 100 | 6-24h: 70 | >24h: 30
  Athlete availability:        Confirmed T-60min: 100 | T-3h: 80 | T-24h: 50 | Unknown: 20
  On-chain data (HAS/TVI):     < 1h old: 100 | 1-6h: 80 | >6h: 50
  DeFi pool data:              < 10min: 100 | 10-60min: 70 | >60min: 40
  Weather data:                < 3h of event: 100 | 3-24h: 70 | Unknown: 50

COMPOSITE: weighted average of applicable data types for this analysis

If data timestamps unknown: use conservative estimate (50 per applicable type)
```

### Component 3 — Flag Health (25% weight)

```
Measures: How many warning flags are active — flags reduce confidence

STARTING SCORE: 100
DEDUCTIONS per active flag:
  lineup_unconfirmed:       -25 points
  injury_warning:           -20 points
  macro_override_active:    -15 points
  liquidity_critical:       -20 points
  liquidity_warning:        -10 points
  weather_risk:             -10 points
  congestion_warning:       -8 points
  officiating_uncertainty:  -5 points
  narrative_active:         -3 points (narrative is signal, not always negative)

FLOOR: 0 (score cannot go negative)
Multiple flags stack: all deductions apply
```

### Component 4 — Modifier Confidence (15% weight)

```
Measures: How reliable are the modifiers that were applied

SCORING:
  Source reliability tier of athlete data:
    Official lineup / medical report: 100
    Training ground (verified): 85
    Manager press conference: 75
    Journalist (credible): 60
    Social media / rumour: 35
    Unknown / inferred: 20
    
  Modifier calculation completeness:
    All sub-modifiers computed with data: 100
    Some sub-modifiers used neutral default (1.00): 70
    Most sub-modifiers on neutral default: 40
    
  COMPOSITE: average of source reliability + calculation completeness
```

---

## SportMind Score in the confidence output schema

```json
{
  "sportmind_output": {
    "schema_version": "1.0",
    "sportmind_score": {
      "sms": 84.2,
      "sms_tier": "HIGH_QUALITY",
      "components": {
        "layer_coverage": 92.0,
        "data_freshness": 78.0,
        "flag_health": 77.0,
        "modifier_confidence": 85.0
      },
      "layers_loaded": [1, 2, 3, 4, 5],
      "analysis_completeness": "FULL_5_LAYER"
    },
    "signal": {
      "adjusted_score": 74.2,
      "confidence_tier": "HIGH"
    }
  }
}
```

**SMS tiers:**

| SMS | Tier | Meaning |
|---|---|---|
| 80–100 | HIGH_QUALITY | Full intelligence loaded; results highly reliable |
| 60–79 | GOOD | Most intelligence loaded; act normally |
| 40–59 | PARTIAL | Significant gaps; results directional only |
| 20–39 | INCOMPLETE | Minimum intelligence; use for orientation only |
| < 20 | INSUFFICIENT | Do not act on this analysis |

---

## How SMS and adjusted_score work together

```
COMBINED DECISION MATRIX:

adjusted_score HIGH + SMS HIGH:    Full entry — maximum conviction
adjusted_score HIGH + SMS LOW:     WAIT — signal looks good but analysis is incomplete
adjusted_score MEDIUM + SMS HIGH:  Reduced entry — reliable analysis; uncertain signal
adjusted_score MEDIUM + SMS LOW:   ABSTAIN — not enough to go on
adjusted_score LOW + SMS HIGH:     Reliable negative signal — confirmed avoid
adjusted_score LOW + SMS LOW:      ABSTAIN — both signal and analysis are weak

AGENT RULE: Never enter on HIGH adjusted_score alone.
  If SMS < 60, reload missing layers before acting regardless of adjusted_score.
  The SMS tells you whether to trust the adjusted_score.
```

---

## Cross-sport comparability

The SMS enables comparison across sports that was previously impossible:

```
Example analysis batch (same day):
  Football (Man City vs Arsenal), full 5 layers: SMS = 89
  MMA (UFC fight, full fight-week stack): SMS = 91
  Cricket (IPL T20, no weather data): SMS = 71
  Basketball (NBA B2B, L1+L2 only): SMS = 54

Agent interpretation:
  The football and MMA analyses are both highly reliable — act on them.
  The cricket analysis has a gap (weather data missing) — proceed with reduced size.
  The NBA analysis is incomplete — load macro and market context before acting.

Without SMS, an agent comparing a 72 football signal to a 72 NBA signal
has no way to know one is based on full intelligence and one on partial.
```

---

## SMS calculation helper (Python)

```python
def calculate_sms(output: dict) -> float:
    """Calculate SportMind Score from a confidence output object."""
    sm = output.get("sportmind_output", {})
    layers = sm.get("layer_inputs", {})
    flags = sm.get("flags", {})
    
    # Component 1: Layer Coverage
    sport_tier = sm.get("layer_inputs", {}).get("layer_4_market_tier", 4)
    layer_points = 0
    if layers.get("layer_5_macro_active") is not None: layer_points += 12
    if layers.get("layer_4_market_tier"): layer_points += 10
    if layers.get("layer_1_domain_loaded"): layer_points += 30
    if layers.get("layer_2_athlete_loaded"): layer_points += 28
    if layers.get("layer_3_on_chain_loaded") and sport_tier == 1: layer_points += 20
    max_points = 100 if sport_tier == 1 else 80
    layer_coverage = min(100, (layer_points / max_points) * 100)
    
    # Component 2: Data Freshness (simplified — use 70 as default if unknown)
    data_freshness = sm.get("data_freshness_score", 70)
    
    # Component 3: Flag Health
    flag_deductions = {
        "lineup_unconfirmed": 25, "injury_warning": 20,
        "macro_override_active": 15, "liquidity_critical": 20,
        "liquidity_warning": 10, "weather_risk": 10,
        "congestion_warning": 8, "officiating_uncertainty": 5,
        "narrative_active": 3
    }
    flag_score = 100
    for flag, deduction in flag_deductions.items():
        if flags.get(flag):
            flag_score -= deduction
    flag_health = max(0, flag_score)
    
    # Component 4: Modifier Confidence (simplified — use 75 as default)
    modifier_confidence = sm.get("modifier_confidence_score", 75)
    
    # Composite SMS
    sms = (layer_coverage * 0.35) + (data_freshness * 0.25) + \
          (flag_health * 0.25) + (modifier_confidence * 0.15)
    
    return round(sms, 1)

SMS_TIERS = {
    range(80, 101): "HIGH_QUALITY",
    range(60, 80): "GOOD",
    range(40, 60): "PARTIAL",
    range(20, 40): "INCOMPLETE",
    range(0, 20): "INSUFFICIENT"
}
```

---

## Integration with platform contracts

```
CONTRACT: signal.full now returns sportmind_score object
CONTRACT: All modifier contracts contribute to SMS calculation

AGENT USAGE:
  sms = response["sportmind_output"]["sportmind_score"]["sms"]
  if sms < 60:
      # Load missing layers before acting
      missing = [l for l in [1,2,3,4,5] 
                 if l not in response["sportmind_output"]["sportmind_score"]["layers_loaded"]]
      # Reload with additional layers
  elif sms >= 60:
      # Proceed with adjusted_score
      action = response["sizing"]["recommended_action"]
```

---

*MIT License · SportMind · sportmind.dev*
