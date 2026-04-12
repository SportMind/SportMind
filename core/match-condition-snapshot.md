---
name: match-condition-snapshot
description: >
  Condition fingerprint schema for match records — captures the full
  modifier and environmental context at the time of a prediction, enabling
  future case-based retrieval: "find me historical matches where conditions
  resembled today's." Extends the existing calibration record format with
  a structured condition_snapshot block. A condition snapshot is not just
  what happened (outcome) or what we predicted (direction, SMS) — it is
  the complete environmental state that produced the prediction. Two
  matches with the same result but different condition snapshots teach
  different lessons. Two matches with similar condition snapshots but
  different results reveal genuine uncertainty. The retrieval mechanism
  uses a structured Condition Similarity Score (CSS) calculated from
  modifier overlap — no vector database required. Designed for zero
  external dependencies in line with SportMind's maintenance philosophy.
  Load when: recording a post-match outcome for the calibration record,
  building historical memory for an agent, or running similarity-based
  scenario analysis. Cross-sport: sport-agnostic schema with sport-specific
  optional fields.
---

# Match Condition Snapshot — SportMind

**The outcome tells you what happened. The condition snapshot tells
you under what circumstances — so the next time conditions are similar,
you know what the library said and whether it was right.**

This is the missing link between the calibration record (what happened)
and historical intelligence (why, and what to expect when it happens again).

---

## The core insight

```
WHAT CALIBRATION RECORDS CURRENTLY STORE:
  ✓ Prediction: direction, SMS, modifiers applied, layers loaded
  ✓ Outcome: result, direction_correct
  ✓ Flags: key modifier validated, signal was actionable

WHAT THEY DO NOT STORE:
  ✗ Full macro environment at the time of prediction
  ✗ Squad state (key players available/absent, cohesion level)
  ✗ FTP PATH state (if fan token applicable)
  ✗ Trend phase for relevant active trends
  ✗ Spatial context (formation, pressing system, set piece dependency)
  ✗ Motivation context (contract year, milestone proximity, etc.)
  ✗ Manager stability at time of prediction

WITHOUT CONDITION SNAPSHOTS:
  All 126 calibration records contain direction outcomes.
  None can answer: "What were conditions like last time Arsenal played
  PSG at home in a knockout stage with a doubtful key winger and neutral
  macro?" That question has no historical answer in the current system.

WITH CONDITION SNAPSHOTS:
  An agent retrieves the most similar historical record.
  Conditions same, result same → confidence in current signal increases.
  Conditions same, result different → genuine uncertainty; widen signal.
  New condition type with no historical precedent → flag LOW_PRECEDENT.
```

---

## The condition_snapshot schema

```json
{
  "condition_snapshot": {

    "snapshot_version":   "1.0",
    "captured_at":        "ISO-8601 timestamp — time prediction was finalised",
    "sport":              "string",
    "event_type":         "league | cup_ko | cup_final | international | playoff | friendly",

    "macro_state": {
      "crypto_cycle_phase":   "bull | neutral | bear | extreme_bear",
      "macro_modifier":        1.00,
      "regulatory_environment":"stable | mica_active | sec_uncertainty | mifid_active | stable",
      "macro_flags":           []
    },

    "competition_context": {
      "competition_tier":      0.75,
      "match_importance_score": 0.80,
      "stage":                 "quarter_final | group | final | etc",
      "home_advantage_applicable": true,
      "neutral_venue":         false
    },

    "squad_state": {
      "lqi_score":              0.92,
      "lqi_label":              "STRONG | GOOD | REDUCED | DEPLETED",
      "key_absences":           ["player_name: position"],
      "lineup_confirmed":       true,
      "cohesion_sci":           78,
      "cohesion_label":         "GOOD",
      "manager_stability":      "STABLE | UNDER_PRESSURE | CARETAKER",
      "mgs_i_score":            0.82
    },

    "motivation_context": {
      "active_drivers":         ["contract_year", "milestone_proximity"],
      "mi_score":               1.15,
      "mi_modifier":            1.12,
      "relegation_zone":        false,
      "title_race_active":      false
    },

    "spatial_context": {
      "formation":              "4-3-3",
      "system_type":            "high_press | possession | low_block | counter | mixed",
      "pressing_intensity":     "HIGH | MEDIUM | LOW",
      "set_piece_dependency":   "HIGH | MEDIUM | LOW",
      "spatial_modifier":       1.04
    },

    "environmental_context": {
      "weather_signal":         "clear | rain | high_wind | extreme_heat | cold",
      "weather_modifier":       1.00,
      "venue_type":             "home | away | neutral",
      "home_crowd_factor":      "MAJOR | STANDARD | REDUCED | EMPTY",
      "dew_factor_applicable":  false,
      "altitude_applicable":    false,
      "travel_fatigue_applicable": false,
      "congestion_tier":        "SEVERE | HIGH | MODERATE | STANDARD | RESTED"
    },

    "fan_token_state": {
      "token_applicable":       true,
      "token_symbol":           "AFC",
      "lifecycle_phase":        3,
      "ltui_trajectory":        "IMPROVING | STABLE | DECLINING | UNCERTAIN",
      "ftp_path":               "PATH_2 | PATH_1 | NONE",
      "ftp_path2_win_count_season": 12,
      "macro_modifier_at_snapshot": 1.00,
      "dsm_flags_active":       []
    },

    "active_trends": [
      {
        "trend_id":    "T-02",
        "trend_name":  "Saudi Pro League player migration",
        "phase":       "acceleration",
        "modifier":    1.25
      }
    ],

    "negotiation_context": {
      "active_negotiations":    [],
      "raf_applicable":         false,
      "commercial_tier_status": "STABLE | UPGRADING | AT_RISK"
    },

    "signal_summary": {
      "direction":              "HOME",
      "sms":                    74,
      "adjusted_score":         68.4,
      "composite_modifier":     1.10,
      "recommended_action":     "ENTER",
      "layers_loaded":          [1, 2, 3, 4, 5],
      "analysis_completeness":  "FULL_5_LAYER"
    }
  }
}
```

---

## Condition Similarity Score (CSS)

```
PURPOSE:
  Given a new match to analyse, retrieve the historical record whose
  condition snapshot most closely resembles current conditions.
  "Most similar past scenario to this one."

CSS FORMULA:
  CSS = (macro_match × 0.20)
      + (competition_match × 0.15)
      + (squad_match × 0.25)
      + (motivation_match × 0.10)
      + (environmental_match × 0.10)
      + (fan_token_match × 0.10)
      + (spatial_match × 0.10)

  Each component returns 0.0 (no match) → 1.0 (exact match).
  CSS range: 0.0 → 1.0

COMPONENT CALCULATIONS:

  macro_match:
    crypto_cycle_phase same: 1.0
    adjacent phase: 0.6
    opposite phase (bull vs extreme_bear): 0.0
    modifier within ±0.05: add 0.2 bonus (cap at 1.0)

  competition_match:
    same competition_tier (±0.1): 1.0
    same event_type: add 0.3 bonus (cap at 1.0)
    neutral_venue same: add 0.1 bonus

  squad_match:
    lqi_label same: 0.6
    lqi_score within ±0.05: 1.0
    same lineup_confirmed status: add 0.2
    cohesion_label same: add 0.2

  motivation_match:
    same active_driver categories: 1.0
    one driver matches: 0.5
    no drivers match: 0.0

  environmental_match:
    weather_signal same: 0.5
    venue_type same: 0.3
    congestion_tier same: 0.2

  fan_token_match (only when token_applicable):
    lifecycle_phase same: 0.4
    ftp_path same: 0.4
    ltui_trajectory same: 0.2

  spatial_match:
    system_type same: 0.5
    pressing_intensity same: 0.3
    set_piece_dependency same: 0.2

CSS INTERPRETATION:
  CSS ≥ 0.80: STRONG MATCH — historical record highly relevant
  CSS 0.60–0.79: GOOD MATCH — historical record informative, weight at 0.7
  CSS 0.40–0.59: PARTIAL MATCH — use with caution
  CSS < 0.40: WEAK MATCH — different enough that historical record may mislead
  No records with CSS ≥ 0.40: LOW_PRECEDENT flag — genuinely novel scenario

RETRIEVAL OUTPUT:
  Most similar record + CSS score + what the outcome was + whether SportMind
  was correct + what the key modifier overlap was.
```

---

## Case-based reasoning integration

```
HOW AN AGENT USES CONDITION SNAPSHOTS:

Step 1: Generate current condition snapshot (before running full analysis)
Step 2: Calculate CSS against all stored snapshots in calibration-data/
Step 3: Retrieve top 3 most similar records (CSS sorted descending)
Step 4: Integrate historical outcomes as prior:

  If top match CSS ≥ 0.80 AND SportMind was correct:
    Confidence uplift: SMS + 3 points, add historical_validation: true

  If top match CSS ≥ 0.80 AND SportMind was WRONG:
    Confidence reduction: SMS − 5 points, add historical_caution: true
    Add note: "Similar conditions previously produced incorrect signal.
    Review which modifier was wrong before proceeding."

  If top match CSS 0.60–0.79:
    Informative prior. Note in brief. Do not adjust SMS.

  If CSS < 0.40 or LOW_PRECEDENT:
    Flag: "Genuinely novel scenario — no close historical precedent.
    Analysis is based on framework only, not historical validation."

PLAIN ENGLISH OUTPUT:
  "The closest match in SportMind's calibration records is [event_name]
  from [date] (similarity: [CSS]). In that scenario SportMind called
  [direction] and was [correct/incorrect]. The key shared conditions
  were [2-3 matching factors]."
```

---

## Adding condition snapshots to calibration records

```
UPDATED CALIBRATION RECORD STRUCTURE:
  The existing schema (community/calibration-data/) remains unchanged.
  The condition_snapshot block is ADDED as a new optional field.
  Backward compatible — existing records without snapshots still valid.

  {
    "record_id": "...",
    "sport": "...",
    "prediction": { ... },      // existing
    "outcome": { ... },          // existing
    "calibration_flags": { ... }, // existing
    "condition_snapshot": { ... } // NEW — this skill defines the schema
  }

MINIMUM VIABLE SNAPSHOT (when full data is not available):
  Not all fields are required. Minimum for CSS calculation:
    macro_state.crypto_cycle_phase
    macro_state.macro_modifier
    competition_context.competition_tier
    squad_state.lqi_label
    squad_state.lineup_confirmed
    signal_summary (direction, SMS, recommended_action)

  Partial snapshots still improve retrieval vs no snapshots.
  Agents should capture at minimum these six fields.

STORAGE:
  No external database required.
  Snapshots stored inline in calibration record JSON files.
  CSS calculation is a simple arithmetic loop over stored records —
  ~0.01 seconds for 200 records, no ML or vector search needed.
```

---

## World Cup 2026 connection

```
The World Cup 2026 module (fan-token/world-cup-2026-intelligence/) is
the highest-value use case for condition snapshots in the near term.

Every national team match during the tournament is a condition snapshot
opportunity:
  - Macro phase at the time of the tournament
  - Squad state (key player availability, cohesion under tournament pressure)
  - NCSI weight (World Cup = ×3.5–4.0 on fan token signals)
  - Knockout stage vs group stage (competition_context.event_type)
  - Tournament fatigue (congestion_tier as tournament progresses)

Building condition snapshots throughout the tournament creates the most
valuable historical dataset the library has had — World Cup conditions
recur every four years, and the 2026 dataset will directly inform
agents analysing the 2030 tournament.

AGENT RULE: During World Cup 2026, capture a condition snapshot for
every prediction submitted to the calibration record. The World Cup
is the single highest-leverage period for historical memory building.
```

---

## Integration with SportMind patterns

```
PATTERN 2 (Pre-Match Chain):
  Step 1: Generate condition snapshot
  Step 2: Run CSS against stored records
  Step 3: Include historical_match note in signal output if CSS ≥ 0.60

PATTERN 11 (Post-Match Agent):
  At T+0: Record outcome in calibration record
  At T+2h: Capture full condition snapshot with retrospective accuracy
  Store: condition_snapshot + accuracy_assessment for future retrieval

PATTERN 8 (FTP Monitor):
  Condition snapshots with fan_token_state populated build the PATH_2
  historical dataset — over time enabling "what happened to supply in
  similar macro/squad/match conditions?"

MEMORY MCP INTEGRATION:
  Condition snapshots stored via Memory MCP persist across sessions.
  See platform/memory-integration.md for token memory schema.
  The condition_snapshot complements but does not replace the signal
  history — signal history tracks outcomes, snapshots track context.

BENCHMARK CONNECTION:
  community/benchmark/scenarios/ — each benchmark scenario should
  include a condition_snapshot for reproducibility and comparison.
  An agent that scores well on benchmark scenarios with full snapshots
  provides more reliable evidence than one tested on outcome-only records.
```

---

*SportMind v3.59 · MIT License · sportmind.dev*
*See also: community/calibration-data/CONTRIBUTING.md*
*core/historical-intelligence-framework.md · platform/memory-integration.md*
*core/reasoning-patterns.md · fan-token/world-cup-2026-intelligence/*
