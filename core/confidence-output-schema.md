# Confidence Output Schema — SportMind

The standard output format for any AI agent using SportMind. Defining what an
agent produces makes every SportMind integration composable — any system that
consumes SportMind intelligence knows exactly what fields to expect.

---

## Why a standard output schema matters

```
WITHOUT A SCHEMA:
  Every SportMind agent produces a different output format
  Integrations cannot be reused or compared
  Confidence levels are expressed inconsistently
  Decisions cannot be automated reliably
  Prediction accuracy cannot be tracked over time

WITH THIS SCHEMA:
  Any SportMind consumer (dashboard, API, trading system) reads the same fields
  Confidence levels map directly to position sizing decisions
  Output can be stored, compared, and used to calibrate modifier weights over time
  Agents can be tested against historical scenarios using consistent output
```

---

## The SportMind standard output object

```json
{
  "sportmind_output": {
    "schema_version": "1.0",
    "generated_at": "ISO-8601 timestamp",
    "sportmind_score": {
      "sms": 84.2,
      "sms_tier": "HIGH_QUALITY | GOOD | PARTIAL | INCOMPLETE | INSUFFICIENT",
      "components": {
        "layer_coverage": 92.0,
        "data_freshness": 78.0,
        "flag_health": 77.0,
        "modifier_confidence": 85.0
      },
      "layers_loaded": [1, 2, 3, 4, 5],
      "analysis_completeness": "FULL_5_LAYER | PARTIAL | DOMAIN_ONLY"
    },
    "event": {
      "sport": "string",
      "competition": "string",
      "match_id": "string or null",
      "home_team": "string",
      "away_team": "string",
      "kickoff_utc": "ISO-8601 timestamp",
      "venue": "string or null"
    },
    "signal": {
      "base_score": 0.0,
      "adjusted_score": 0.0,
      "direction": "HOME | AWAY | DRAW | OVER | UNDER | LONG | SHORT",
      "confidence_tier": "HIGH | MEDIUM | LOW | ABSTAIN",
      "confidence_pct": 0.0
    },
    "modifiers_applied": {
      "athlete_modifier": 1.00,
      "congestion_modifier": 1.00,
      "officiating_modifier": 1.00,
      "weather_modifier": 1.00,
      "narrative_modifier": 1.00,
      "macro_modifier": 1.00,
      "composite_modifier": 1.00
    },
    "layer_inputs": {
      "layer_5_macro_active": false,
      "layer_4_market_tier": 1,
      "layer_3_on_chain_loaded": true,
      "layer_2_athlete_loaded": true,
      "layer_1_domain_loaded": true
    },
    "flags": {
      "injury_warning": false,
      "congestion_warning": false,
      "lineup_unconfirmed": false,
      "weather_risk": false,
      "officiating_uncertainty": false,
      "macro_override_active": false,
      "narrative_active": false,
      "liquidity_warning": false,
      "liquidity_critical": false
    },
    "defi_context": {
      "primary_venue": "CEX",
      "pool_tvl_usd": 0,
      "estimated_slippage_pct": 0.0,
      "lp_activity_signal": "NEUTRAL",
      "yield_apr_pct": 0.0,
      "lifecycle_phase": 1
    },
    "reasoning": {
      "primary_signal_driver": "string — the single most important factor",
      "supporting_factors": ["string", "string"],
      "risk_factors": ["string", "string"],
      "abstain_reason": "string or null"
    },
    "sizing": {
      "recommended_action": "ENTER | REDUCE | WAIT | ABSTAIN",
      "position_size_pct": 0.0,
      "entry_condition": "string or null",
      "exit_condition": "string or null"
    },
    "token_signal": {
      "applicable": true,
      "token_direction": "POSITIVE | NEGATIVE | NEUTRAL | N/A",
      "token_signal_strength": "STRONG | MODERATE | WEAK | NONE",
      "relevant_tokens": ["string"]
    }
  }
}
```

---

## Field definitions

### `signal` object

```
base_score (float, 0–100):
  The raw signal score from the upstream data platform before any SportMind
  modifiers are applied. If no upstream platform, set to 50.0 (neutral).

adjusted_score (float, 0–100):
  base_score × composite_modifier, bounded to [0, 100].
  This is the primary output number that drives all downstream decisions.

direction (enum):
  The recommended direction of the position.
  HOME / AWAY / DRAW: Standard match outcome
  OVER / UNDER: Total points/goals/runs positions
  LONG / SHORT: Token/asset positions

confidence_tier (enum):
  HIGH:    adjusted_score ≥ 70 AND no critical flags active
  MEDIUM:  adjusted_score 55–69 OR one non-critical flag active
  LOW:     adjusted_score 45–54 OR multiple flags active
  ABSTAIN: adjusted_score < 45 OR critical flag active (lineup unconfirmed,
           macro override active, memorial match, extreme weather)

confidence_pct (float, 0–100):
  Human-readable confidence percentage derived from adjusted_score.
  Not a probability — a relative conviction level.
  Maps to position sizing (see sizing.position_size_pct below).
```

### `modifiers_applied` object

```
Each modifier is a float multiplier (0.50–1.25).
composite_modifier = product of all individual modifiers.

Standard neutral value for each modifier: 1.00
  (no modifier applied when no relevant information exists for that dimension)

Modifier sources:
  athlete_modifier:      core/core-athlete-modifier-system.md + athlete/{sport}/
  congestion_modifier:   core/core-fixture-congestion.md
  officiating_modifier:  core/core-officiating-intelligence.md
  weather_modifier:      core/core-weather-match-day.md
  narrative_modifier:    core/core-narrative-momentum.md
  macro_modifier:        macro/macro-overview.md
```

### `flags` object

```
Flags are boolean signals that change agent behaviour regardless of score.

injury_warning:
  Set TRUE when a key player (top-3 impact) has doubt status unconfirmed
  → Triggers: Wait for lineup confirmation before entering

congestion_warning:
  Set TRUE when Tier 1 or Tier 2 congestion detected (see core-fixture-congestion.md)
  → Triggers: Apply congestion modifier; note in reasoning

lineup_unconfirmed:
  Set TRUE when fewer than 2h to kickoff AND official lineup not released
  → Triggers: Reduce position size by 30% OR wait for lineup
  CRITICAL FLAG: If lineup_unconfirmed AND injury_warning both TRUE → ABSTAIN

weather_risk:
  Set TRUE when abandonment probability > 15% OR extreme weather modifier active
  → Triggers: Reduce position size or abstain for outdoor sports

officiating_uncertainty:
  Set TRUE when assigned official is unknown or has < 25 match sample
  → Triggers: Apply zero officiating modifier (no signal without reliable data)

macro_override_active:
  Set TRUE when Layer 5 macro event is active with direct impact on this sport
  → CRITICAL FLAG: Always triggers position size reduction

liquidity_warning:
  Set TRUE when primary pool TVL < $500k
  → Triggers: position size reduction to max 40% of standard; applies regardless of signal confidence

liquidity_critical:
  Set TRUE when primary pool TVL < $100k OR estimated slippage > 3%
  → CRITICAL FLAG: Position size max 20% of standard; ABSTAIN if slippage > 5%
  → Check defi_context.pool_tvl_usd and defi_context.estimated_slippage_pct

narrative_active:
  Set TRUE when a narrative modifier (positive or negative) has been applied
  → Informational: Surfaces the narrative for human review
```

### `sizing` object

```
POSITION SIZE MAPPING (recommended_action + position_size_pct):

ENTER:
  HIGH confidence + no critical flags: 100% of standard position
  HIGH confidence + non-critical flag: 75% of standard position
  MEDIUM confidence + no flags: 60% of standard position
  MEDIUM confidence + non-critical flag: 40% of standard position

REDUCE:
  LOW confidence: 20–30% of standard position
  Any critical flag active: Reduce by 50% from whatever size was calculated

WAIT:
  lineup_unconfirmed = TRUE: Wait until lineup confirmed, then re-evaluate
  Event within 30 minutes and high uncertainty: Wait for live signal

ABSTAIN:
  confidence_tier = ABSTAIN
  macro_override_active = TRUE (unless specific sport/position justified)
  lineup_unconfirmed + injury_warning both TRUE
  Memorial match (from core-narrative-momentum.md)
  Event cancellation risk > 30%

entry_condition (string or null):
  Conditional entry: "Enter if home lineup confirmed with [player]"
  Set to null for unconditional entry

exit_condition (string or null):
  "Exit at half-time if home team trailing by 2+"
  "Exit if [player] substituted before 60 min"
  Set to null for hold-to-result
```

### `token_signal` object

```
applicable (boolean):
  TRUE for Tier 1 sports with active tokens
  FALSE for sports without active tokens (Tier 2–4)

token_direction:
  POSITIVE: Match outcome expected to be positive for referenced tokens
  NEGATIVE: Match outcome expected to be negative
  NEUTRAL:  Match expected to have minimal token price impact
  N/A:      No active tokens for this sport

token_signal_strength:
  STRONG:   Expected token move > ±8%
  MODERATE: Expected token move ±4–8%
  WEAK:     Expected token move ±1–4%
  NONE:     No expected token market impact

relevant_tokens (array of strings):
  List of token symbols expected to be affected (e.g., ["$BAR", "$RMFC"])
```

---

## Confidence tier → action mapping quick reference

```
┌─────────────────────────────────────────────────────────────────┐
│  Confidence Tier  │  Adjusted Score  │  Recommended Action      │
├─────────────────────────────────────────────────────────────────┤
│  HIGH             │  70–100          │  ENTER at 75–100% size   │
│  MEDIUM           │  55–69           │  ENTER at 40–60% size    │
│  LOW              │  45–54           │  REDUCE to 20–30% size   │
│  ABSTAIN          │  < 45 / critical │  Do not enter            │
└─────────────────────────────────────────────────────────────────┘

CRITICAL FLAG OVERRIDE (always applies regardless of confidence tier):
  macro_override_active + HIGH confidence → reduce to 50% of HIGH sizing
  lineup_unconfirmed + injury_warning → ABSTAIN regardless of score
  Event cancellation risk > 30% → ABSTAIN
```

---

## Implementation examples

### Minimal output (Layer 1 only, no modifiers)

```json
{
  "sportmind_output": {
    "schema_version": "1.0",
    "generated_at": "2026-05-15T18:00:00Z",
    "event": {
      "sport": "football",
      "competition": "UEFA Champions League",
      "home_team": "FC Barcelona",
      "away_team": "Bayern Munich",
      "kickoff_utc": "2026-05-20T19:00:00Z"
    },
    "signal": {
      "base_score": 65.0,
      "adjusted_score": 65.0,
      "direction": "HOME",
      "confidence_tier": "MEDIUM",
      "confidence_pct": 65.0
    },
    "modifiers_applied": {
      "athlete_modifier": 1.00,
      "congestion_modifier": 1.00,
      "officiating_modifier": 1.00,
      "weather_modifier": 1.00,
      "narrative_modifier": 1.00,
      "macro_modifier": 1.00,
      "composite_modifier": 1.00
    },
    "sizing": {
      "recommended_action": "ENTER",
      "position_size_pct": 55.0
    }
  }
}
```

### Full output (all five layers + modifiers)

```json
{
  "sportmind_output": {
    "schema_version": "1.0",
    "generated_at": "2026-05-15T18:00:00Z",
    "event": {
      "sport": "football",
      "competition": "UEFA Champions League",
      "home_team": "FC Barcelona",
      "away_team": "Bayern Munich",
      "kickoff_utc": "2026-05-20T19:00:00Z",
      "venue": "Camp Nou"
    },
    "signal": {
      "base_score": 68.0,
      "adjusted_score": 72.4,
      "direction": "HOME",
      "confidence_tier": "HIGH",
      "confidence_pct": 72.4
    },
    "modifiers_applied": {
      "athlete_modifier": 1.12,
      "congestion_modifier": 0.97,
      "officiating_modifier": 1.04,
      "weather_modifier": 1.00,
      "narrative_modifier": 1.05,
      "macro_modifier": 1.00,
      "composite_modifier": 1.064
    },
    "layer_inputs": {
      "layer_5_macro_active": false,
      "layer_4_market_tier": 1,
      "layer_3_on_chain_loaded": true,
      "layer_2_athlete_loaded": true,
      "layer_1_domain_loaded": true
    },
    "flags": {
      "injury_warning": false,
      "congestion_warning": false,
      "lineup_unconfirmed": false,
      "weather_risk": false,
      "officiating_uncertainty": false,
      "macro_override_active": false,
      "narrative_active": true
    },
    "reasoning": {
      "primary_signal_driver": "Strong home form + key player availability confirmed",
      "supporting_factors": [
        "Home team kicker/set-piece specialist confirmed in XI",
        "Revenge narrative active — lost to this opponent in last edition"
      ],
      "risk_factors": [
        "Away team has 3-day rest advantage from earlier fixture",
        "Home team played 3 matches in 10 days"
      ],
      "abstain_reason": null
    },
    "sizing": {
      "recommended_action": "ENTER",
      "position_size_pct": 85.0,
      "entry_condition": null,
      "exit_condition": "Review if home team trails at half-time"
    },
    "token_signal": {
      "applicable": true,
      "token_direction": "POSITIVE",
      "token_signal_strength": "STRONG",
      "relevant_tokens": ["$BAR"]
    }
  }
}
```

---

## Schema validation

```python
# Minimal Python validation example
import json
from datetime import datetime

VALID_DIRECTIONS = {"HOME", "AWAY", "DRAW", "OVER", "UNDER", "LONG", "SHORT"}
VALID_TIERS = {"HIGH", "MEDIUM", "LOW", "ABSTAIN"}
VALID_ACTIONS = {"ENTER", "REDUCE", "WAIT", "ABSTAIN"}

def validate_sportmind_output(output: dict) -> tuple[bool, list[str]]:
    """Returns (is_valid, list_of_errors)"""
    errors = []
    sig = output.get("sportmind_output", {}).get("signal", {})
    
    if sig.get("direction") not in VALID_DIRECTIONS:
        errors.append(f"Invalid direction: {sig.get('direction')}")
    if sig.get("confidence_tier") not in VALID_TIERS:
        errors.append(f"Invalid confidence_tier: {sig.get('confidence_tier')}")
    if not (0 <= sig.get("adjusted_score", -1) <= 100):
        errors.append("adjusted_score must be 0–100")
    
    sizing = output.get("sportmind_output", {}).get("sizing", {})
    if sizing.get("recommended_action") not in VALID_ACTIONS:
        errors.append(f"Invalid recommended_action: {sizing.get('recommended_action')}")
    
    return len(errors) == 0, errors

# See examples/langchain/ for full integration
```

---

## Changelog

| Version | Change | Notes |
|---|---|---|
| 1.0 | Initial schema — signal, modifiers, flags, reasoning, sizing, token_signal | Current stable version |
| 1.1 | Added defi_context object; liquidity_warning and liquidity_critical flags | Backward compatible — existing agents receive new fields and can ignore them |
| 1.2 | Added sportmind_score object with SMS metric | Backward compatible — new object, no fields changed |
| Future 2.0 | Any breaking field changes | 6-month deprecation notice; migration guide will be published |

## Version migration guide

### v1.0 → v1.1 (current)

```
NEW FIELDS ADDED (all optional to existing agents):
  flags.liquidity_warning:    bool — set TRUE when pool TVL < $500k
  flags.liquidity_critical:   bool — set TRUE when TVL < $100k or slippage > 3%
  defi_context:               object — pool_tvl_usd, slippage, lp_activity, yield, phase

MIGRATION REQUIRED: No
  Existing agents that don't declare defi_context simply receive the new fields.
  If your agent ignores unknown fields (standard practice), no code changes needed.
  If your agent validates against a strict schema, add the two new flag fields
  and the defi_context object to your schema definition.

HOW TO CONSUME NEW FIELDS:
  if response["flags"]["liquidity_critical"]:
      position_size = min(position_size, standard_size * 0.20)
  elif response["flags"]["liquidity_warning"]:
      position_size = min(position_size, standard_size * 0.40)
```

## Schema validation (Python)

```python
import json

REQUIRED_FIELDS = {
    "signal": ["base_score", "adjusted_score", "direction", "confidence_tier"],
    "modifiers_applied": ["composite_modifier"],
    "flags": ["injury_warning", "lineup_unconfirmed", "macro_override_active"],
    "sizing": ["recommended_action", "position_size_pct"]
}

def validate_sportmind_output(output: dict) -> tuple[bool, list[str]]:
    """Returns (is_valid, list_of_errors). Works for both v1.0 and v1.1."""
    errors = []
    sm = output.get("sportmind_output", {})
    
    # Version check
    version = sm.get("schema_version", "MISSING")
    if version == "MISSING":
        errors.append("schema_version field missing")
    
    # Required field check
    for section, fields in REQUIRED_FIELDS.items():
        section_data = sm.get(section, {})
        for field in fields:
            if field not in section_data:
                errors.append(f"Missing required field: {section}.{field}")
    
    # Value validation
    sig = sm.get("signal", {})
    if not (0 <= sig.get("adjusted_score", -1) <= 100):
        errors.append("adjusted_score must be 0–100")
    if sig.get("confidence_tier") not in {"HIGH", "MEDIUM", "LOW", "ABSTAIN"}:
        errors.append(f"Invalid confidence_tier: {sig.get('confidence_tier')}")
    if sig.get("direction") not in {"HOME","AWAY","DRAW","OVER","UNDER","LONG","SHORT"}:
        errors.append(f"Invalid direction: {sig.get('direction')}")
    
    sizing = sm.get("sizing", {})
    if sizing.get("recommended_action") not in {"ENTER","REDUCE","WAIT","ABSTAIN"}:
        errors.append(f"Invalid recommended_action: {sizing.get('recommended_action')}")
    
    return len(errors) == 0, errors
```

## Platform contract reference

This schema is the guaranteed output of all SportMind platform contracts.
See `platform/api-contracts.md` for the full skill call specifications.

*MIT License · SportMind · sportmind.dev*
