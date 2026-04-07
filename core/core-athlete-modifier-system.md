# The SportMind Modifier System

The athlete modifier system is the quantitative core of SportMind's Layer 2. It converts athlete-level intelligence — who is playing, how fit they are, what form they're in — into a single numeric multiplier that adjusts a base prediction signal.

---

## The formula

```
adjusted_signal_score = base_signal_score × composite_modifier

composite_modifier = PRODUCT of all applicable sub-modifiers, clamped to [0.40, 1.40]
```

---

## Sub-modifier components

Every athlete skill computes one or more of these components. The `athlete/meta` skill orchestrates them all into a single composite.

| Component | Inputs | Range | Sports it applies to |
|---|---|---|---|
| Availability | Player status, fit%, source reliability | 0.62–1.15 | All |
| Form | Rolling N-match score, trend direction | 0.82–1.20 | All |
| Goalkeeper | Save%, post-shot xG, backup delta | 0.78–1.10 | Football, Hockey |
| Fatigue | Minutes last 7d, travel km, rest days | 0.88–1.02 | All |
| Weather | Wind, rain, temperature, surface | 0.87–1.00 | Outdoor sports |
| H2H matchup | Head-to-head advantage score | 0.88–1.18 | All |
| Psychological | Win/loss streak, controversy, morale | 0.78–1.12 | All |
| Lineup confirmation | Confirmation status, source reliability | 0.90–1.15 | Team sports |
| Set piece | Specialist availability, dependency | 0.95–1.08 | Football, Rugby |
| Meta readiness | Patch alignment (esports only) | 0.78–1.10 | Esports |
| Weight cut | Severity, history of issues (MMA only) | 0.75–1.00 | MMA |
| Surface | Surface win rate (tennis only) | 0.80–1.18 | Tennis |

---

## Availability status mapping

| Status | Fit% | Modifier |
|---|---|---|
| CONFIRMED (key player, HOT form) | 100 | ×1.15 |
| CONFIRMED (key player, AVERAGE form) | 100 | ×1.00 |
| PROBABLE | 80–99 | ×1.05 |
| DOUBT | 50–79 | ×0.85 |
| OUT (key player) | 0 | ×0.70 |
| OUT → backup GK / stand-in | 0 | ×0.80 |
| OUT (multiple key players) | 0 | ×0.55 |
| SUSPENDED | 0 | ×0.72 |

---

## Form score → modifier mapping

| Form score | Label | Modifier |
|---|---|---|
| 85–100 | DOMINANT | ×1.20 |
| 70–84 | HOT | ×1.10 |
| 55–69 | GOOD | ×1.04 |
| 40–54 | AVERAGE | ×1.00 |
| 25–39 | POOR | ×0.92 |
| 0–24 | COLD | ×0.82 |

---

## Composite modifier interpretation

| Composite | Meaning | Recommended agent action |
|---|---|---|
| ≥ 1.20 | Elite conditions | High conviction, full sizing |
| 1.10–1.19 | Strong conditions | Normal sizing |
| 1.00–1.09 | Neutral | Follow base signal |
| 0.90–0.99 | Minor concerns | Reduce size or wait |
| 0.80–0.89 | Significant concerns | Strong caution |
| 0.70–0.79 | Major degradation | Skip unless base signal very strong |
| < 0.70 | Severe | Do not enter |

---

## Knockout conditions

Certain conditions immediately floor the composite modifier, overriding all other components:

| Condition | Sport | Floor |
|---|---|---|
| 3+ key players confirmed out | All | 0.55 |
| Backup goalkeeper starting | Football / Hockey | 0.80 |
| Stand-in player (any role) | Esports | 0.80 |
| Late replacement (< 3 weeks notice) | MMA | 0.75 |
| Starter QB ruled out | NFL | 0.65 |
| Star player net rating +15, now out | NBA | 0.62 |
| Fighter misses weight | MMA | 0.72 |
| Major patch within 10 days of tournament | Esports | 0.78 |

---

## Source reliability tiers

The confidence of the composite modifier degrades when inputs come from unreliable sources.

| Source | Reliability score | Lineup confirmation modifier |
|---|---|---|
| Official team sheet / lineup | 1.00 | ×1.15 |
| Official medical report | 0.95 | ×1.10 |
| Training ground report (verified) | 0.85 | ×1.02 |
| Manager press conference (direct quote) | 0.75 | ×0.98 |
| Journalist report (credible outlet) | 0.60 | ×0.95 |
| Social media rumour | 0.35 | ×0.92 |
| Unverified / inferred | 0.20 | ×0.90 |

---

## Implementing a new modifier component

When building a new athlete skill, any new modifier component must:

1. Be bounded within [0.55, 1.25] at the component level
2. Document inputs and output value in the skill's command reference
3. Include a modifier table showing at least 5 distinct conditions with values
4. Add sport-specific form metrics to `core/core-athlete-record-schema.json`
5. Be consistent with the knockout conditions table above

New components are reviewed by maintainers for mathematical consistency before merging.

---

## Injury intelligence integration

The modifier system handles availability at a binary/tiered level. For full injury
intelligence — injury type taxonomy, replacement quality delta, squad depth stress
index, return-to-play performance curves, and sport-specific signals — load:

- `core/injury-intelligence/core-injury-intelligence.md` — master framework
- `core/injury-intelligence/injury-intel-[sport].md` — sport-specific files available
  for football, MMA, NFL, boxing, horse racing, and cycling
