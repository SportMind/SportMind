# [Sport] Athlete Intelligence — SportMind Skill

<!--
  INSTRUCTIONS FOR CONTRIBUTORS
  ─────────────────────────────
  Athlete skills document the player-level intelligence layer.
  Every command needs full parameter and return value documentation.
  Return value examples must be valid JSON.
  Modifier values must align with core/core-athlete-modifier-system.md.
  Read CONTRIBUTING.md before starting.
-->

Player-level intelligence for [sport] predictions and fan token signals.
Produces an `athlete_modifier` (0.55–1.25) that adjusts the base signal score.

**Applicable tokens / markets:** [List relevant tokens or market types]

---

## Overview

<!--
  2–3 sentences on what makes athlete-level data uniquely valuable for this sport.
  What is the single most predictive player variable?
-->

---

## Commands

| Command | Description | Auth required |
|---|---|---|
| `get_[command_name]` | [What it returns] | Yes/No |
| `get_athlete_signal_modifier` | Composite modifier — runs all sub-skills | Yes |

---

## Command reference

<!--
  Full documentation for every command.
  Each command needs: purpose, parameters, and a real JSON return example.
-->

### `get_[command_name]`

[One sentence on what this command does and when to use it.]

**Parameters:**
- `[param_name]` (required/optional) — [description, valid values if constrained]
- `[param_name]` (optional, default: [value]) — [description]

**Returns:**
```json
{
  "[field]": "[value]",
  "[field]": 0.00,
  "signal_modifier": 1.05,
  "modifier_reason": "[explanation of why this modifier was computed]"
}
```

**Notes:** [Any important caveats or edge cases.]

---

### `get_athlete_signal_modifier`

Master composite modifier — runs all applicable sub-commands and returns one multiplier.

**Parameters:**
- `token` (required) — fan token symbol or market identifier
- `match_id` (optional) — specific event ID; defaults to next upcoming event

**Returns:**
```json
{
  "token": "[TOKEN]",
  "event": "[Event name]",
  "base_signal_score": 70,
  "composite_modifier": 1.12,
  "adjusted_signal_score": 78,
  "adjusted_direction": "BULLISH",
  "modifier_breakdown": {
    "[component_1]": 1.08,
    "[component_2]": 1.05,
    "[component_3]": 0.97
  },
  "confidence": 0.82,
  "key_risks": ["[Risk 1]", "[Risk 2]"],
  "recommendation": "[Plain language action directive]",
  "re_evaluate_at": "[ISO8601 datetime]"
}
```

---

## Modifier reference

<!--
  Table of sport-specific modifier scenarios with values.
  Must be consistent with core/core-athlete-modifier-system.md ranges.
-->

| Condition | Modifier |
|---|---|
| [Best case scenario] | ×1.20 |
| [Good scenario] | ×1.10 |
| [Neutral] | ×1.00 |
| [Minor concern] | ×0.92 |
| [Significant concern] | ×0.82 |
| [Severe — knockout condition] | ×0.70 |

### Knockout conditions

These conditions immediately floor the composite modifier regardless of other inputs:

| Condition | Floor modifier |
|---|---|
| [Worst case — e.g., star player out] | 0.70 |
| [Critical risk — e.g., backup GK] | 0.80 |

---

## Integration example

<!--
  Show a realistic agent workflow using this skill alongside Layer 1.
-->

### [Sport] pre-event workflow

```
# Step 1: Get base signal
[base_signal_command] token=[TOKEN]

# Step 2: Check athlete layer
get_[availability_command] token=[TOKEN]
get_[form_command] token=[TOKEN] [params]

# Step 3: Get composite modifier
get_athlete_signal_modifier token=[TOKEN]

# Step 4: Decision logic
# If adjusted_score >= [threshold] AND [condition] → entry
# If adjusted_score < [threshold] → skip
```

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | [Date] | Initial release |

---

*Contributed by [Your GitHub handle] · MIT License · sportmind.dev*
