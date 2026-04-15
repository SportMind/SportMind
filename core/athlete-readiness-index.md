---
name: athlete-readiness-index
description: >
  Unified pre-match readiness framework producing an Athlete Readiness
  Index (ARI: 0.60–1.10) that combines five components: fatigue trajectory
  (from fixture congestion and schedule density), motivation state (from
  athlete-motivation-intelligence), travel and timezone penalty (from
  travel-timezone-intelligence), injury risk accumulation (predictive load
  threshold model, not just current availability), and physical availability
  confidence (lineup certainty × source reliability). ARI replaces the
  need to load five separate modifier files for a single athlete — it is
  the single pre-match readiness signal that feeds directly into the
  composite athlete modifier chain. Cross-sport: football, basketball,
  cricket, MMA, rugby, Formula 1, tennis, and any sport where individual
  athlete state materially affects match outcome. Fan token impact: ARI
  below 0.80 for a team's top-3 ATM-tier athletes is a direct FTIS
  dampener — the signal magnitude of a match result is lower when key
  players are operating below readiness threshold. Non-fan-token use:
  direct input to pre-match SMS computation for any sport.
---

# Athlete Readiness Index — SportMind

**A player's name on the team sheet is not the same as that player being
ready to perform. The ARI separates the two.**

Standard pre-match analysis treats availability as binary: playing or not
playing. The Athlete Readiness Index replaces that binary with a continuous
score that models what every experienced observer already knows — a 70%
fit striker playing through pain is a different proposition from a fully
rested one, and an athlete returning from a long-haul flight the night
before is not the same as one who slept in their own bed.

---

## The ARI formula

```
ARI = weighted_product([
    fatigue_trajectory     × 0.30,
    motivation_state       × 0.20,
    travel_penalty         × 0.20,
    injury_risk_threshold  × 0.20,
    availability_confidence× 0.10
])

ARI RANGE: 0.60 → 1.10
  1.10: Peak readiness (full rest, high motivation, home, no injury history)
  1.00: Standard baseline (normal preparation, no flags)
  0.90: Mild concern (one minor factor active)
  0.80: Significant concern (one major factor OR two minor factors)
  0.70: Serious concern (multiple factors; consider rotation or role change)
  0.60: Floor (minimum confidence; lineup uncertainty high)

APPLICATION TO SIGNAL CHAIN:
  composite_athlete_modifier = existing_modifier_components × ARI
  ARI does NOT replace the existing athlete modifier — it acts as a
  final readiness gate applied after all other modifier components.
  This preserves backward compatibility with all existing patterns.

FAN TOKEN APPLICATION:
  For a club's top-3 ATM-tier players:
    ARI < 0.80 for any one: FTIS dampener −5 points
    ARI < 0.80 for two or more: FTIS dampener −10 points
    ARI < 0.70 for any one: raise LINEUP_CONCERN flag; agent escalates
  The dampener reflects reduced commercial signal magnitude — a muted
  performance from key players limits the engagement arc regardless
  of the result.
```

---

## Component 1 — Fatigue trajectory (weight: 0.30)

```
INPUTS: days_since_last_match, minutes_last_match, matches_last_14_days,
        position_type (high_intensity vs low), age

SCORING:
  7+ days rest, low recent load:               1.05
  4–6 days rest, normal load:                  1.00  ← baseline
  3 days rest (standard mid-week/weekend):     0.97
  2 days rest (B2B equivalent):                0.92
  1 day rest or played >80 min yesterday:      0.85
  3 matches in 7 days (Tier 1 congestion):     0.88
  4+ matches in 10 days (severe congestion):   0.80

POSITION MULTIPLIERS (apply to fatigue score):
  High intensity (pressing winger, box-to-box mid, prop):  ×1.00 (full sensitivity)
  Medium intensity (centre-back, point guard, hooker):     ×0.95 (slightly protected)
  Low intensity (goalkeeper, setter, specialist bowler):   ×0.90 (most protected)

AGE MULTIPLIERS:
  Under 23: ×0.97 (faster recovery)
  23–28:    ×1.00 (baseline)
  29–32:    ×1.03 (slower recovery)
  33+:      ×1.06 (significantly slower; rotation risk elevated)

CROSS-SPORT NOTES:
  Football: minutes threshold for fatigue signal = 75+ min last match
  Basketball: B2B games apply regardless of minutes (travel + game = load)
  Cricket: bowling overs matter more than batting innings for fast bowlers
  MMA: fight camp load (sparring intensity) matters as much as fight frequency
  Rugby: tackle count is the primary load metric, not time on field
  Tennis: tie-break sets count as full-match load for fatigue purposes
  Formula 1: driver fatigue is secondary to car/team state — apply ×0.90 weight
```

---

## Component 2 — Motivation state (weight: 0.20)

```
INPUTS: from core/athlete-motivation-intelligence.md (MI score)
        Simplified bridge for ARI computation:

MI SCORE → MOTIVATION COMPONENT:
  1.20–1.30 (peak):          1.08  (contract year, revenge match, redemption)
  1.10–1.19 (elevated):      1.04
  0.90–1.09 (baseline):      1.00
  0.80–0.89 (suppressed):    0.95
  0.70–0.79 (low):           0.90  (end-of-contract drift, post-trophy hangover)
  Below 0.70 (disengaged):   0.85  (confirmed departure, disciplinary issue)

KEY TRIGGERS (load from athlete-motivation-intelligence.md):
  CONTRACT_YEAR_ACTIVE:        +0.08
  REVENGE_MATCH:               +0.06
  DEBUT_OR_RETURN:             +0.05
  CONFIRMED_DEPARTURE:         −0.10
  DISCIPLINARY_SUSPENSION_RET: −0.08
  POST_TROPHY_HANGOVER:        −0.04

AGENT RULE: If athlete-motivation-intelligence.md is not loaded,
  default motivation component to 1.00 (neutral — do not penalise
  for missing data, do not reward either).
```

---

## Component 3 — Travel and timezone penalty (weight: 0.20)

```
INPUTS: from core/travel-timezone-intelligence.md (TIS score)

TIS → TRAVEL COMPONENT (direct bridge):
  TIS 0.98–1.00:   1.00  (standard domestic travel, no penalty)
  TIS 0.95–0.97:   0.98  (minor haul, minimal impact)
  TIS 0.90–0.94:   0.95  (international break returnee, moderate haul)
  TIS 0.85–0.89:   0.90  (long haul within 48h, or 7+ TZ crossing)
  TIS 0.80–0.84:   0.85  (ultra long haul, antipodal travel)
  Below TIS 0.80:  0.82  (floor — extreme cases)

INTERNATIONAL BREAK RETURNEE RULE:
  Player returning from 5+ timezone away:
    If returning < 72h before match: travel_component = 0.90
    If returning < 48h before match: travel_component = 0.86
    If returning < 24h before match: travel_component = 0.82
    Flag: INTERNATIONAL_RETURNEE_SHORT_PREP

AGENT RULE: If travel-timezone-intelligence.md is not loaded,
  default travel component to 1.00 for domestic fixtures,
  0.97 for European away trips, 0.93 for intercontinental.
```

---

## Component 4 — Injury risk accumulation (weight: 0.20)

```
THIS IS THE PREDICTIVE COMPONENT — not just current availability.

CONCEPT: Injury risk is not binary (fit/injured). It accumulates non-linearly
over load periods. A player who has played 55+ matches in a season, recently
returned from a soft-tissue injury, and is entering a third match in seven
days is not "fit" in any meaningful sense — their injury probability is
materially elevated even if they appear in training.

LOAD ACCUMULATION SCORE (LAS):
  Season matches played (by position sensitivity):
    High-intensity position:
      0–25 matches:     LAS = 0.00  (fresh)
      26–35 matches:    LAS = 0.05
      36–45 matches:    LAS = 0.12
      46–50 matches:    LAS = 0.18
      51+ matches:      LAS = 0.25  (maximum seasonal load penalty)
    Low-intensity position:
      Scale at 70% of above values

RECURRENCE MULTIPLIER:
  No recent injury history:              ×1.00
  Returned from injury < 4 weeks ago:    ×1.40 (recurrence risk elevated)
  Returned from injury < 8 weeks ago:    ×1.20
  Two soft-tissue injuries this season:  ×1.35 (chronic risk pattern)

INJURY_RISK_COMPONENT:
  injury_risk_penalty = LAS × recurrence_multiplier
  injury_risk_component = 1.00 − min(injury_risk_penalty, 0.25)

EXAMPLES:
  First 30 matches, no injury history:   component = 1.00 (no penalty)
  48 matches, returned 3 weeks ago:      LAS 0.15 × 1.40 = 0.21 → component 0.79
  53 matches, clean bill of health:      LAS 0.25 × 1.00 = 0.25 → component 0.75
  38 matches, second soft-tissue injury: LAS 0.12 × 1.35 = 0.16 → component 0.84

CROSS-SPORT LOAD EQUIVALENTS:
  Football:   match count as above
  Basketball: NBA regular season (82 games); flag at 65+, severe at 75+
  Cricket:    Test match day-count is the primary load metric (not match count)
  MMA:        Fights per 12 months; flag at 4+, severe at 6+
  Tennis:     Grand Slam weeks + ATP tour events; flag at 35+ weeks
  Rugby:      Tackle count accumulated is more predictive than match count
  F1:         Race weekend count (physical demand); rarely the limiting factor
```

---

## Component 5 — Availability confidence (weight: 0.10)

```
INPUTS: lineup_confirmed (boolean), fit_percentage_reported,
        source_reliability (Tier 1/2/3)

SCORING:
  Official lineup confirmed, listed as starter:    1.00
  Manager confirmed in press conference:           0.98
  Reliable Tier 1 journalist confirms starter:     0.95
  Tier 2 source, training participation seen:      0.90
  Tier 3 source only, or "expected to play":       0.82
  Fit percentage reported < 100%:                  × (fit_pct / 100)
  Lineup unconfirmed 2h before match:              0.85
  Injury doubt reported, no confirmation:          0.72
  Ruled out confirmed:                             0.00 (remove from ARI calc)

MANAGER LANGUAGE SHORTCUTS (from pre-match-squad-intelligence.md):
  "Fit and available" → 0.95
  "We'll see how he trains" → 0.82
  "Touch and go" / "50-50" → 0.72
  "Not risking him" → treat as ruled out
  "Trained fully yesterday" → 0.95
  "Carrying a knock but playing" → fit_pct = 0.80
```

---

## ARI computation — worked examples

```
EXAMPLE 1 — Bukayo Saka, Arsenal vs PSG, UCL QF (Wednesday)
  Fatigue:     3 days since last match (sat 3pm), 82 min played: 0.97
  Motivation:  UCL knockout = peak motivation: 1.08
  Travel:      Home fixture, no travel: 1.00
  Injury risk: 38 matches, no recent injury: LAS 0.10, component 0.90
  Availability:Official lineup out T-2h, confirmed starter: 1.00

  ARI = (0.97×0.30) + (1.08×0.20) + (1.00×0.20) + (0.90×0.20) + (1.00×0.10)
      = 0.291 + 0.216 + 0.200 + 0.180 + 0.100
      = ARI 0.987 → round to 0.99
  LABEL: PEAK READY
  Fan token effect: No FTIS dampener. Key player at near-full readiness.

EXAMPLE 2 — Same player, but Saka returned from international duty 36h ago
  Fatigue:     3 days since PL match, but international match 2 days ago: 0.92
  Motivation:  UCL knockout: 1.08
  Travel:      International returnee, 5 TZ west, 36h ago: 0.90
  Injury risk: 45 matches including internationals: LAS 0.12, component 0.88
  Availability:Confirmed starter but "raring to go" comment (Tier 2): 0.92

  ARI = (0.92×0.30) + (1.08×0.20) + (0.90×0.20) + (0.88×0.20) + (0.92×0.10)
      = 0.276 + 0.216 + 0.180 + 0.176 + 0.092
      = ARI 0.940
  LABEL: READY — MINOR CONCERNS
  Fan token effect: No FTIS dampener (above 0.80 threshold). Flag for monitoring.

EXAMPLE 3 — NBA star, back-to-back road game, 3 weeks post hamstring
  Fatigue:     B2B, played 38 min last night: 0.85
  Motivation:  Mid-season, team in playoff hunt: 1.04
  Travel:      West Coast road trip, third game: 0.95
  Injury risk: 52 games + hamstring return 3 weeks ago: LAS 0.20 × 1.30 = 0.26 → 0.74
  Availability:Listed as "probable" by team: 0.88

  ARI = (0.85×0.30) + (1.04×0.20) + (0.95×0.20) + (0.74×0.20) + (0.88×0.10)
      = 0.255 + 0.208 + 0.190 + 0.148 + 0.088
      = ARI 0.889
  LABEL: CONCERN — MONITOR
  Fan token effect: If ATM-tier player, apply −5 FTIS dampener.
```

---

## ARI labels and agent actions

```
ARI ≥ 1.05: PEAK READY
  Agent action: Full weight in signal chain. No flags.

ARI 0.95–1.04: READY
  Agent action: Standard processing. No flags.

ARI 0.85–0.94: MINOR CONCERNS
  Agent action: Note in signal brief. No modifier change. Monitor T-2h lineup.

ARI 0.75–0.84: CONCERN — MONITOR
  Agent action: Apply ARI as modifier gate. If ATM-tier: −5 FTIS dampener.
  Set WATCH flag. Confirm availability at latest possible point.

ARI 0.65–0.74: SIGNIFICANT CONCERN
  Agent action: Apply ARI modifier. If ATM-tier: −10 FTIS dampener.
  Raise INJURY_RISK_ELEVATED flag. Consider whether to reduce signal confidence.

ARI < 0.65: HIGH CONCERN — ESCALATE
  Agent action: Escalate to human. Do not produce ENTER signal without
  human confirmation. Likely rotation or limited-role outing.
```

---

## ARI output schema

```json
{
  "ari_brief": {
    "athlete":      "Bukayo Saka",
    "club":         "Arsenal",
    "match":        "Arsenal vs PSG",
    "assessed_at":  "2026-04-14T18:00:00Z"
  },

  "components": {
    "fatigue_trajectory":     0.97,
    "motivation_state":       1.08,
    "travel_penalty":         1.00,
    "injury_risk_threshold":  0.90,
    "availability_confidence":1.00
  },

  "ari_score":   0.99,
  "ari_label":   "PEAK READY",

  "flags":       [],
  "ftis_impact": "none",

  "plain_english": "Saka is as ready as he's likely to be at this stage of the season. Home game, strong motivation, no travel concerns, well within safe load parameters, confirmed in the XI. Full weight in the signal chain.",

  "sportmind_version": "3.66.0"
}
```

---

*SportMind v3.66 · MIT License · sportmind.dev*
*See also: core/athlete-motivation-intelligence.md · core/travel-timezone-intelligence.md*
*core/core-fixture-congestion.md · core/injury-intelligence/core-injury-intelligence.md*
*core/pre-match-squad-intelligence.md · core/core-athlete-modifier-system.md*
