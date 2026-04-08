---
name: disciplinary-sentiment-intelligence
description: >
  Models the multi-axis sentiment cascade triggered by athlete and club disciplinary
  events — how offences, charges, bans, and legal proceedings affect fan sentiment,
  social sentiment, commercial value, competition standing, and fan token signals.
  Use this skill when a player has been cited, charged, banned, or faces legal
  proceedings. Use when a disciplinary event has occurred and you need to understand
  the commercial and sentiment implications beyond simple availability. Connects to
  core/athlete-disciplinary-intelligence.md for offence taxonomy and DSM values.
  Always run before generating fan token commercial recommendations when any
  disciplinary flag (CITING_ACTIVE, COMMERCIAL_RISK_ACTIVE, LEGAL_PROCEEDINGS_ACTIVE)
  is set. Produces DSM tier, active flags, and modified commercial signal.
---

# Disciplinary Sentiment Intelligence

Models how disciplinary events cascade across fan sentiment, commercial value,
and fan token signals — from red card to criminal charge.

## What this skill produces

- **DSM tier** — Disciplinary Sentiment Modifier level (MINIMAL / MODERATE / SEVERE / CATASTROPHIC)
- **Active flags** — CITING_ACTIVE, BAN_CONFIRMED, COMMERCIAL_RISK_ACTIVE, LEGAL_PROCEEDINGS_ACTIVE
- **Sentiment vector** — direction and magnitude across five axes
- **Commercial modifier** — adjusted commercial signal value
- **Timeline estimate** — expected resolution window
- **Recovery projection** — estimated sentiment recovery arc

---

## Prerequisites

Load before this skill:
1. `macro/macro-overview.md` — macro context
2. `core/athlete-disciplinary-intelligence.md` — offence taxonomy and DSM framework
3. `fan-token/fan-sentiment-intelligence/` — baseline fan sentiment model

---

## Workflow

### Step 1 — Classify the event
```
Input: [player name] + [event description]
Output: Tier (1/2/3/4) + Sport-specific framework

Classification guide:
  On-field → check Tier 1 vs Tier 2 (severity, intent, injury caused)
  Off-field → Tier 3 (conduct) or Tier 4 (criminal/legal)
  Unclear/unconfirmed → apply Tier 3 precautionary pending clarification
```

### Step 2 — Identify player prominence
```
KEY_ASSET:     Starting XI, significant commercial profile, high social following
REGULAR_XI:    Starting XI, limited commercial profile
SQUAD:         Regular squad member, not automatic starter
PERIPHERAL:    Fringe squad, minimal commercial impact

Prominence multiplier on token impact:
  KEY_ASSET:   ×1.5 on all token impact estimates
  REGULAR_XI:  ×1.0 (base estimates)
  SQUAD:       ×0.6
  PERIPHERAL:  ×0.3
```

### Step 3 — Determine process stage
```
PRE_CHARGE:           Incident occurred, no formal charge/citation yet (0–48h)
CITED_OR_CHARGED:     Formal process initiated, outcome unknown
HEARING_SCHEDULED:    Date set for judicial review
VERDICT_PENDING:      Hearing complete, awaiting announcement
VERDICT_CONFIRMED:    Outcome published and confirmed
APPEALING:            Verdict appealed — apply interim ban if any
RESOLVED:             Process complete, player returned/cleared

Uncertainty factor by stage:
  PRE_CHARGE:         Highest uncertainty — apply conservative DSM
  CITED_OR_CHARGED:   High uncertainty — DSM at stated level
  HEARING_SCHEDULED:  Moderate uncertainty — DSM sustained
  VERDICT_CONFIRMED:  Low uncertainty — apply definitive modifier
  RESOLVED:           Apply CONDUCT_RESIDUAL for defined recovery window
```

### Step 4 — Apply DSM and generate sentiment vector

```
DSM_MINIMAL (Tier 1):
  Fan sentiment delta:        0%
  Social sentiment delta:     0%
  Commercial delta:           0%
  Token impact:               None
  Flags:                      None (unless accumulation)
  Commercial modifier:        1.00

DSM_MODERATE (Tier 2):
  Fan sentiment delta:        -10 to -25% (duration: process length)
  Social sentiment delta:     -15 to -30% for 48-72h then decay
  Commercial delta:           -5 to -15% (sponsor watch mode)
  Token impact:               -2 to -8% KEY_ASSET, scaling by prominence
  Flags:                      CITING_ACTIVE or BAN_CONFIRMED
  Commercial modifier:        0.88

DSM_SEVERE (Tier 3):
  Fan sentiment delta:        -25 to -50% (duration: full process)
  Social sentiment delta:     -40 to -65% peak then sustained elevated
  Commercial delta:           -20 to -45% (sponsor activation hold)
  Token impact:               -5 to -20% KEY_ASSET
  Flags:                      COMMERCIAL_RISK_ACTIVE
  Commercial modifier:        0.72

DSM_CATASTROPHIC (Tier 4):
  Fan sentiment delta:        -40 to -75% (unresolved duration)
  Social sentiment delta:     Cross-media saturation — unmodelable
  Commercial delta:           -40 to -80% (morality clause review)
  Token impact:               -15 to -40% KEY_ASSET — ABSTAIN from recs
  Flags:                      LEGAL_PROCEEDINGS_ACTIVE
  Commercial modifier:        ABSTAIN
```

### Step 5 — Recovery projection
```
IF verdict = exoneration/dropped:
  Fan sentiment: 60-80% recovery within 2-4 weeks
  Commercial: 70-90% recovery within 4-8 weeks
  Token: 50-80% recovery within 2-6 weeks
  Residual: CONDUCT_RESIDUAL for 6 weeks post-resolution

IF verdict = ban confirmed (Tier 2):
  Fan sentiment: recovers on return to play
  Commercial: recovers within 4-8 weeks of return
  Token: priced in at verdict. Recovery follows playing return.
  CONDUCT_RESIDUAL: 4 weeks post-return

IF verdict = severe sanction (Tier 3):
  Fan sentiment: partial recovery only (6-18 months)
  Commercial: new lower baseline (some sponsors may not return)
  Token: new lower baseline — previous peak unlikely to return
  CONDUCT_RESIDUAL: 3-6 months post-verdict

IF verdict = criminal conviction (Tier 4):
  Fan sentiment: permanent reset for violent/serious offences
  Commercial: sponsor relationships likely severed
  Token: permanent baseline reset
  CONDUCT_RESIDUAL: may be indefinite
```

---

## Output schema

```json
{
  "disciplinary_signal": {
    "player":             "string",
    "club":               "string",
    "sport":              "string",
    "offence_type":       "string — description of incident",
    "tier":               "1 | 2 | 3 | 4",
    "process_stage":      "PRE_CHARGE | CITED_OR_CHARGED | HEARING_SCHEDULED | VERDICT_PENDING | VERDICT_CONFIRMED | APPEALING | RESOLVED",
    "dsm_level":          "MINIMAL | MODERATE | SEVERE | CATASTROPHIC",
    "commercial_modifier": "float or ABSTAIN",
    "player_prominence":   "KEY_ASSET | REGULAR_XI | SQUAD | PERIPHERAL"
  },
  "sentiment_vector": {
    "fan_sentiment_delta":        "% string e.g. '-15 to -30%'",
    "social_sentiment_delta":     "% string",
    "commercial_delta":           "% string",
    "token_impact_estimate":      "% string or ABSTAIN",
    "competition_sentiment":      "string — governing body posture",
    "broadcast_sentiment":        "string — media framing"
  },
  "flags": {
    "citing_active":              "boolean",
    "ban_confirmed":              "boolean",
    "commercial_risk_active":     "boolean",
    "legal_proceedings_active":   "boolean",
    "suspension_risk":            "boolean",
    "conduct_residual":           "boolean"
  },
  "timeline": {
    "process_stage_current":      "string",
    "expected_resolution":        "string — timeframe estimate or UNKNOWN",
    "return_to_play":             "string — date or UNKNOWN",
    "recovery_projection":        "string — sentiment recovery arc"
  },
  "agent_recommendation": "ENTER | WAIT | ABSTAIN",
  "generated_at": "ISO-8601 timestamp",
  "sportmind_version": "3.32.0"
}
```

---

## Example outputs

### Example 1 — Rugby Union: citing confirmed (Tier 2, Key Asset)
```json
{
  "disciplinary_signal": {
    "player":             "Starting loosehead prop",
    "club":               "Top-4 Premiership club",
    "sport":              "rugby_union",
    "offence_type":       "Dangerous play — contact with head/neck area",
    "tier":               2,
    "process_stage":      "CITED_OR_CHARGED",
    "dsm_level":          "MODERATE",
    "commercial_modifier": 0.88,
    "player_prominence":   "KEY_ASSET"
  },
  "sentiment_vector": {
    "fan_sentiment_delta":       "-15 to -25% pending verdict",
    "social_sentiment_delta":    "-20 to -35% for 48-72h post-citation",
    "commercial_delta":          "-5 to -12% sponsor watch mode",
    "token_impact_estimate":     "-3 to -8% KEY_ASSET prominence multiplier",
    "competition_sentiment":     "Judicial hearing scheduled — formal process active",
    "broadcast_sentiment":       "Incident on pundit rotation — ban length speculation"
  },
  "flags": {
    "citing_active":             true,
    "ban_confirmed":             false,
    "commercial_risk_active":    false,
    "legal_proceedings_active":  false,
    "suspension_risk":           false,
    "conduct_residual":          false
  },
  "timeline": {
    "process_stage_current":     "Cited — judicial hearing within 7-10 days",
    "expected_resolution":       "7-14 days",
    "return_to_play":            "UNKNOWN pending verdict",
    "recovery_projection":       "Sentiment recovers on return if first offence + lenient verdict"
  },
  "agent_recommendation": "WAIT",
  "generated_at": "2026-04-08T10:00:00Z",
  "sportmind_version": "3.32.0"
}
```

### Example 2 — Football: off-field social media charge (Tier 3, Key Asset)
```json
{
  "disciplinary_signal": {
    "player":             "First-choice striker",
    "club":               "Top-6 Premier League",
    "sport":              "football",
    "offence_type":       "Discriminatory social media post — FA E1(b) charge",
    "tier":               3,
    "process_stage":      "CITED_OR_CHARGED",
    "dsm_level":          "SEVERE",
    "commercial_modifier": 0.72,
    "player_prominence":   "KEY_ASSET"
  },
  "sentiment_vector": {
    "fan_sentiment_delta":       "-30 to -50% — majority condemnation",
    "social_sentiment_delta":    "-50 to -70% cross-media viral — non-sports pick-up",
    "commercial_delta":          "-25 to -45% — sponsor activation hold active",
    "token_impact_estimate":     "-8 to -20% KEY_ASSET — COMMERCIAL_RISK_ACTIVE",
    "competition_sentiment":     "FA investigation active — squad suspension likely pending",
    "broadcast_sentiment":       "Dominates sports news cycle — pundit condemnation majority"
  },
  "flags": {
    "citing_active":             false,
    "ban_confirmed":             false,
    "commercial_risk_active":    true,
    "legal_proceedings_active":  false,
    "suspension_risk":           false,
    "conduct_residual":          false
  },
  "timeline": {
    "process_stage_current":     "FA charge issued — hearing in 3-6 weeks",
    "expected_resolution":       "3-8 weeks",
    "return_to_play":            "Pending verdict — may be suspended from squad",
    "recovery_projection":       "Partial commercial recovery 6-18 months if no repeat"
  },
  "agent_recommendation": "ABSTAIN",
  "generated_at": "2026-04-08T10:00:00Z",
  "sportmind_version": "3.32.0"
}
```

---

*SportMind v3.32 · MIT License · sportmind.dev*
*Part of Layer 2 Athlete Intelligence + Layer 3 Fan Token Commercial*
*See: core/athlete-disciplinary-intelligence.md for full taxonomy and DSM values*
