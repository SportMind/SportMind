# SportMind × Fan Token Intel — Integration Example

SportMind is the reasoning layer. Fan Token Intel is the data layer.
Together they form a complete sports prediction intelligence stack.

```
Fan Token Intel provides:          SportMind provides:
─────────────────────────          ───────────────────
Live signal scores (0–100)    →    How to interpret them by sport
Whale flows & sell ratios     →    When whale signals matter most
Prematch alpha packets        →    What athlete data to overlay
Match calendar & results      →    How to weight each event type
Historical price correlation  →    Expected ranges by result type
```

---

## The integration pattern

```
tokenintel_signals_active(token)          ← FTI: base signal
  → sportmind/sports/[sport]/sport-domain-[sport].md     ← SportMind: domain context
  → sportmind/athlete/[sport]/athlete-intel-[sport].md    ← SportMind: athlete modifier
  → athlete/meta/apply_athlete_modifier   ← SportMind: adjusted score
  → tokenintel_analytics(sell_ratio_brackets) ← FTI: whale validation
  → decision
```

---

## Example: Football token pre-match workflow

```python
# Step 1 — FTI: get base signals
calendar   = fti.sports_calendar(days_ahead=2)
signal     = fti.signals_active(token="BAR", min_confidence=0.6)
whale      = fti.whale_flows(token="BAR", timeframe_hours=4)
brackets   = fti.analytics(metric="sell_ratio_brackets", token="BAR")

# Step 2 — SportMind Layer 1: domain context (system prompt)
# Agent already has sports/football/sport-domain-football.md in context.
# It knows: BAR vs ATM is a derby (importance ×1.6 minimum),
# La Liga title run-in phase = elevated stakes.

# Step 3 — SportMind Layer 2: athlete modifier
modifier   = sportmind.apply_athlete_modifier(token="BAR")
# Returns: composite_modifier=0.87 (Gavi DOUBT, De Jong OUT)

# Step 4 — Compute adjusted score
base_score      = signal.score           # e.g. 72
adjusted_score  = base_score * modifier  # 72 × 0.87 = 62.6 → NEUTRAL

# Step 5 — Whale gate (always validate before entry)
# brackets.bracket = "0.68–0.70" → 75% historical WR → VALID
# adjusted_score = 62.6 → below BULLISH threshold (68)

# Step 6 — Decision
# Domain skill: derby context justifies attention but not full size
# Athlete modifier: two key midfielders out/doubtful → significant reduction
# Whale: bracket is valid but score is borderline
# → HOLD. Wait for lineup confirmation webhook at −1h.
#   If full strength confirmed: modifier rises, re-evaluate.
#   If Gavi confirmed out: skip entirely.
```

---

## Athlete modifier as a FTI signal adjuster

The core integration insight is simple:

```
FTI signal score:     72  (team-level, whale-adjusted, social-adjusted)
Athlete modifier:     ×0.87  (key players absent/doubtful)
Adjusted score:       63  (drops from BULLISH to NEUTRAL)
Agent action:         HOLD → re-evaluate at lineup confirmation
```

Without SportMind, the agent acts on 72 (bullish).
With SportMind, the agent correctly waits at 63 (neutral).

This is the edge SportMind adds — not new data, but correct interpretation
of data the agent already has.

---

## Mapping FTI tools to SportMind skills

| FTI tool | SportMind complement | What SportMind adds |
|---|---|---|
| `tokenintel_sports_calendar` | `sports/[sport]/sport-domain-[sport].md` | Match importance scoring, competition tier context |
| `tokenintel_signals_active` | `core/core-signal-weights-by-sport.md` | Sport-specific weighting of signal components |
| `tokenintel_whale_flows` | `sports/[sport]/sport-domain-[sport].md` | When whale signals are most reliable for this sport |
| `tokenintel_prematch_alpha` | `athlete/[sport]/athlete-intel-[sport].md` | Athlete modifier to overlay on alpha packets |
| `tokenintel_match_results` | `core/core-result-impact-matrices.md` | Expected impact ranges to validate actual moves |
| `tokenintel_historical_patterns` | Event playbooks | Strategy context for backtest interpretation |
| `tokenintel_autopilot_start` | Athlete modifier pipeline | athlete_aware_matchday template (see below) |

---

## Autopilot template: athlete_aware_matchday

When deploying an autonomous agent using FTI's autopilot with SportMind context:

```json
{
  "template_id": "athlete_aware_matchday",
  "description": "Matchday momentum with SportMind athlete modifier gate",
  "params": {
    "sport": "football",
    "sportmind_layer1": "sports/football",
    "sportmind_layer2": "athlete/football",
    "entry_timing": "-2h",
    "exit_timing": "fulltime",
    "min_athlete_adjusted_score": 68,
    "require_lineup_confirmed": true,
    "max_fatigue_index": 0.85,
    "min_key_player_availability_pct": 75,
    "whale_bracket_required": ["0.68-0.70", "0.75-0.80"],
    "position_size_pct_at_2h": 60,
    "position_size_pct_at_lineup": 40
  }
}
```

---

## Getting started

1. Get a Fan Token Intel API key: https://fantokenintel.com
2. Clone SportMind: `git clone https://github.com/SportMind/SportMind`
3. Install the relevant sport skills into your agent context
4. Use FTI for live data, SportMind for interpretation

Full agent implementation: see `athlete/meta/athlete-intel-cross-sport-orchestrator.md` for the master modifier pipeline
and the reference agent in the original fan-token-athlete-skills repository.
