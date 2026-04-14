# Calibration Framework — SportMind

**How SportMind improves over time.** The framework for tracking prediction outcomes,
measuring modifier accuracy, and systematically improving the weights that produce
the adjusted_score.

The modifier pipeline currently uses expert-defined static ranges. This file defines
how those ranges become data-calibrated — trained against actual outcomes rather than
set by intuition.

---

## The calibration principle

```
CURRENT STATE (v2.x):
  Modifier ranges are expert-defined starting points.
  Example: "Key player OUT → ×0.70 modifier"
  This is calibrated by domain knowledge, not outcome data.

TARGET STATE (v3.x+):
  Modifier ranges are recalibrated against observed outcomes.
  Example: "In 847 tracked matches where key player was OUT,
  the actual signal degradation was ×0.72 ± 0.08 (95% CI)"
  Ranges tighten as more outcomes are tracked.

THE CYCLE:
  1. Agent produces output → logs SportMind prediction
  2. Event resolves → log actual outcome
  3. Compare prediction to outcome → measure modifier accuracy
  4. Aggregate across many events → identify systematic bias
  5. Update modifier ranges where bias is consistent and significant
  6. Community vote on proposed updates → merge if consensus
```

---

## Outcome tracking schema

Every SportMind analysis that is acted upon should produce an outcome record.
This record links the prediction to the actual result for calibration.

```json
{
  "outcome_record": {
    "record_id": "uuid",
    "recorded_at": "ISO-8601",
    "event": {
      "sport": "string",
      "competition": "string",
      "event_id": "string",
      "kickoff_utc": "ISO-8601"
    },
    "prediction": {
      "base_score": 72.0,
      "adjusted_score": 63.4,
      "composite_modifier": 0.88,
      "confidence_tier": "MEDIUM",
      "recommended_action": "WAIT",
      "sportmind_score": 84.2,
      "modifiers_applied": {
        "athlete_modifier": 0.87,
        "congestion_modifier": 1.00,
        "macro_modifier": 1.00,
        "weather_modifier": 1.00,
        "narrative_modifier": 1.04
      },
      "flags_active": ["injury_warning", "lineup_unconfirmed"],
      "layers_loaded": [1, 2, 3, 4, 5]
    },
    "outcome": {
      "result": "HOME_WIN | AWAY_WIN | DRAW | N/A",
      "margin": 0,
      "prediction_correct": true,
      "token_movement_24h_pct": 8.4,
      "token_direction_correct": true,
      "notes": "string or null"
    },
    "calibration_flags": {
      "key_modifier_validated": "athlete_modifier",
      "modifier_direction_correct": true,
      "modifier_magnitude_error": 0.06,
      "signal_was_actionable": true
    }
  }
}
```

---

## Modifier accuracy measurement

For each modifier type, calibration tracks accuracy across three dimensions:

### 1. Direction accuracy
*Did the modifier push the signal the right way?*

```
DIRECTION ACCURACY:
  For athlete_modifier < 1.00 (negative modifier):
    Was the outcome worse than base signal predicted? → CORRECT
    Was outcome same or better than base signal? → INCORRECT
    
  For athlete_modifier > 1.00 (positive modifier):
    Was the outcome better than base signal predicted? → CORRECT
    Was outcome same or worse? → INCORRECT
    
TARGET: ≥ 70% direction accuracy per modifier type
ALERT: < 60% direction accuracy over 50+ events → modifier needs review
```

### 2. Magnitude calibration
*Was the modifier value too large, too small, or about right?*

```
MAGNITUDE ERROR = |actual_degradation - predicted_degradation|
  Where:
    actual_degradation = (actual_outcome_score - base_signal) / base_signal
    predicted_degradation = composite_modifier - 1.00

Well-calibrated: |magnitude_error| < 0.05 (5% error)
Overestimating: modifier too aggressive (e.g. ×0.70 when ×0.85 was correct)
Underestimating: modifier too gentle (e.g. ×0.90 when ×0.70 was correct)

CALIBRATION TARGET:
  Mean absolute magnitude error < 0.08 over 100+ events
```

### 3. Confidence tier calibration
*When SportMind says HIGH confidence, does it win at the rate HIGH confidence should?*

```
TIER CALIBRATION (target win rates):
  HIGH confidence:   ≥ 72% correct direction
  MEDIUM confidence: ≥ 58% correct direction
  LOW confidence:    ≥ 48% correct direction (barely above coin flip — correct for LOW)
  
CALIBRATION FAILURE:
  HIGH tier showing < 62% → confidence tier is overestimated; adjust thresholds
  MEDIUM tier showing > 68% → these could be HIGH; adjust thresholds up
```

---

## Calibration data by modifier type

### Athlete modifier calibration targets

| Modifier scenario | Current range | Target accuracy | Min events for calibration |
|---|---|---|---|
| Key player OUT (team sport) | ×0.70 | ≥ 72% dir. accuracy | 100 |
| Key player DOUBT | ×0.85 | ≥ 65% dir. accuracy | 150 |
| HOT form (5-match) | ×1.10 | ≥ 68% dir. accuracy | 200 |
| COLD form | ×0.82 | ≥ 66% dir. accuracy | 150 |
| MMA weigh-in miss (>1 lb) | ×0.72 | ≥ 78% dir. accuracy | 50 |
| GK sub (football) | ×0.80 | ≥ 74% dir. accuracy | 75 |
| Starter QB out (NFL) | ×0.65 | ≥ 76% dir. accuracy | 40 |

### Macro modifier calibration targets

| Macro scenario | Current modifier | Target | Min events |
|---|---|---|---|
| Crypto bear (BTC < 200-day MA) | ×0.75 | ≥ 70% return preservation | 200 |
| Crypto bull | ×1.20 | ≥ 68% outperformance | 200 |
| Active geopolitical event | ×0.60 | ≥ 72% dir. accuracy | 25 |

### DeFi modifier calibration targets

| Scenario | Current threshold | Target accuracy |
|---|---|---|
| Slippage > 3% → ABSTAIN recommendation | 3% | ≥ 80% of ABSTAIN recommendations outperformed by waiting |
| TVL < $100k → max 20% size | $100k | ≥ 75% of positions benefited from size reduction |

---

## Sport-specific calibration data

### Football (most data-rich)

```
CURRENT CALIBRATION STATUS:
  Events tracked (community): 0 (framework launch)
  Events needed for first recalibration: 200
  
KNOWN SYSTEMATIC BIASES (from expert knowledge, pre-data):
  Derby effect may be underweighted — consider ×0.85 form discount vs current ×0.80
  UCL home advantage appears overweighted vs Liga
  Narrative modifier for record proximity: currently +3-5%; possibly too conservative
  
RECALIBRATION TRIGGER: 200 tracked events with direction accuracy < 65%
```

### MMA

```
CURRENT CALIBRATION STATUS:
  Events tracked: 0 (framework launch)
  
KNOWN SYSTEMATIC BIASES:
  Weigh-in miss modifier (×0.72) based on UFC data 2015-2022; needs refresh
  Submission specialist vs striker matchup modifier potentially underweighted
  
RECALIBRATION TRIGGER: 50 tracked events per modifier scenario
```

---

## Calibration workflow

```
STEP 1 — LOG PREDICTIONS (agent-side):
  When an agent produces a SportMind output and takes action:
  → Save outcome_record.prediction fields immediately
  → Record to: community/calibration-data/{sport}/{year}/{month}/

STEP 2 — LOG OUTCOMES (community-side):
  After event resolves:
  → Complete outcome_record.outcome fields
  → Submit via GitHub PR or API endpoint
  → Automated validation: checks result matches official source

STEP 3 — AGGREGATE (monthly):
  → Run calibration_aggregate.py (see scripts/)
  → Produces: calibration_report.json per modifier type
  → Flags modifiers below accuracy thresholds

STEP 4 — PROPOSE UPDATES (quarterly):
  → Maintainer reviews calibration_report.json
  → Opens GitHub Discussion with proposed modifier range changes
  → Community votes — open window, closes at consensus or 30 days inactivity; minimum 3 responses from contributors with validated records
  → Changes require 70%+ consensus

STEP 5 — MERGE UPDATES:
  → Update core/core-athlete-modifier-system.md with new ranges
  → Document change in CHANGELOG with calibration evidence
  → Update core/core-signal-weights-by-sport.md if signal weights shift
  → Bump minor version (e.g. v3.0 → v3.1)
```

---

## Calibration examples: before and after

```
EXAMPLE: Football athlete modifier recalibration

BEFORE (v2.x static):
  Key player OUT → ×0.70

AFTER (500 events tracked):
  Key player OUT (striker/CF): ×0.72 (less impact than assumed — teams adapt)
  Key player OUT (GK): ×0.78 → stays at v2.x value (confirmed)
  Key player OUT (midfield orchestrator): ×0.68 (more impact than assumed)
  Key player OUT (fullback): ×0.82 (less impact than assumed)

CHANGE: Position-specific breakdown replaces single value
EVIDENCE: 500 events, direction accuracy 74% across all positions
CHANGELOG: "Athlete modifier: key player OUT now position-specific (v3.1)"
```

---

## Contributing calibration data

```
WHO CAN CONTRIBUTE:
  Any developer or agent operator who tracks SportMind predictions against outcomes.
  Data does not require personal information. No financial data required.
  Just: what did SportMind predict + what actually happened.

HOW TO CONTRIBUTE:
  1. Log predictions using outcome_record schema above
  2. After event resolves, complete the outcome fields
  3. Submit via: GitHub PR to community/calibration-data/
     OR via future platform API endpoint (v3.x)
  4. Label PR: calibration-data, sport-{name}

DATA QUALITY STANDARDS:
  Result must be from official source (not estimated)
  Prediction must be unmodified SportMind output (no post-hoc edits)
  Modifier values must match what was actually applied (not reconstructed)
  
DATA PRIVACY:
  No personal data, no wallet addresses, no trade sizes.
  Only: prediction values, modifier values, actual outcome.
```

---

*Calibration data powers SportMind's improvement over time.
The framework is the infrastructure. The data comes from the community.*

*MIT License · SportMind · sportmind.dev*
