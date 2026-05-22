---
name: financial-fair-play-intelligence
description: >
  Enduring reasoning framework for Financial Fair Play (FFP) and successor rules
  as signals affecting squad building, transfer activity, and fan token demand.
  Covers UEFA FSFP, Premier League PSR, and La Liga salary cap with CDI modifiers
  for constraint, headroom, violation, and compound signals. Framework only —
  no specific club PSR positions logged.
---

# Financial Fair Play Intelligence

**How regulatory financial frameworks constrain or enable squad building and CDI signals.**
FFP/PSR signals are Horizon 2-3 context — they set the environment for transfer signals.

---

## The regulatory landscape

```
UEFA FINANCIAL SUSTAINABILITY AND FAIR PLAY (FSFP):
  Successor to UEFA FFP — same underlying principle, updated parameters.
  Clubs must not spend materially more than they earn over a rolling 3-year period.
  Allowable deviation: €60m over 3 years (with investor funding conditions).
  Sanction options: transfer ban, points deduction, competition exclusion.

PREMIER LEAGUE PROFIT AND SUSTAINABILITY RULES (PSR):
  More restrictive than UEFA FSFP in key respects.
  Maximum allowable loss: £105m over 3 consecutive seasons.
  Key difference: academy costs and infrastructure excluded from PSR calculation.
  Sanction: points deduction (applied to current or following season).
  Most significant sanction mechanism in European club football.

LA LIGA FINANCIAL CONTROL (SALARY CAP SYSTEM):
  Each club assigned a spending limit based on projected income.
  Hard cap — clubs cannot exceed their assigned limit.
  La Liga's system is the most restrictive in Europe.
  Implication: La Liga clubs have the least transfer market flexibility of any
    major European league when financially constrained.

MONITORING NOTE:
  All three frameworks evolve — UEFA FSFP replaced FFP, and further revisions
  are possible. When framework changes are confirmed:
  Apply ×0.90 confidence weight to all financial constraint signals for 12 months
  while clubs adapt and new enforcement patterns become clear.
```

---

## Signal framework

```
CLUB OPERATING NEAR PSR/FFP LIMIT:
  Transfer activity is constrained — sales required before purchases.
  Apply: ×0.92 squad quality trajectory (Horizon 2).
  Apply: ×0.88 transfer window ambition signal (Horizon 1-2).
  Observable signals: few incomings without outgoings, loan activity over purchases.

CLUB WITH SIGNIFICANT FINANCIAL HEADROOM:
  Transfer market is active — squad investment is feasible.
  Apply: ×1.05 squad quality trajectory signal (Horizon 2).
  Observable signals: large transfer fees paid, multiple signings, low sale activity.

PSR/FFP VIOLATION CONFIRMED (points deduction):
  ACUTE competitive impact — apply ×0.78 competitive trajectory modifier.
  Duration: for the remainder of the affected season.
  Recovery: begins in following season if financial position stabilised.

TRANSFER EMBARGO (via FFP/FSFP sanction):
  SUSTAINED constraint — apply ×0.85 squad quality modifier for embargo duration.
  Embargo prevents squad replenishment — attrition degrades quality over time.
  Duration modifier: escalates if embargo extends beyond one full transfer window.

RULE CHANGE SIGNAL:
  When UEFA FSFP, PSR, or La Liga system parameters change materially:
  Apply ×0.90 confidence weight to all financial constraint signals for 12 months.
  Rationale: clubs, agents, and analysts all need time to understand new limits —
    transfer market behaviour is uncertain during transition.
```

---

## Fan token interaction

```
COMPOUND SIGNALS — financial constraint × competitive performance:

PSR-LIMITED CLUB + RELEGATION RISK:
  PSR limit constrains squad investment.
  Relegation risk compounds — cannot strengthen to avoid relegation.
  Compound: ×0.88 (PSR-limited transfer ambition) × ×0.82 (relegation CDI)
  = ×0.72 effective CDI — severe constraint.
  This is one of the most negative compound signals in SportMind.

PSR HEADROOM + UCL PARTICIPATION:
  Headroom enables squad investment.
  UCL participation amplifies commercial revenue and CDI.
  Compound: ×1.05 (headroom signal) × ×1.15 (UCL CDI)
  = ×1.21 effective CDI — significant premium.

POINTS DEDUCTION + RELEGATION ZONE:
  Points deduction may push a club into relegation zone directly.
  Apply full relegation modifier immediately if deduction causes drop:
  ×0.72 competitive trajectory + standard relegation CDI modifiers.
  This is an acute compound event — not a gradual signal.

FINANCIAL CONSTRAINT + GOVERNANCE VOTE:
  Clubs under financial constraint may use governance votes to engage the community.
  Increase in vote frequency during financial difficulty: potential LEGACY_CONTRACT
  risk signal — club is extracting value from the token without investing.
  Apply: ×0.92 trust signal if vote frequency increases without corresponding
  club promotion or squad investment during sustained financial constraint.
```

---

## Observable proxies

```
AGENT RULE — DO NOT CALCULATE SPECIFIC PSR POSITION:
  Club accounts are complex, often delayed, and subject to accounting interpretation.
  Do not attempt to calculate a club's specific current PSR headroom or deficit.

USE OBSERVABLE PROXIES INSTEAD:
  Transfer activity pattern:       high buy-to-sell ratio → headroom signal
  Player sales urgency:            fire-sale pattern → constraint signal
  Public statements:               CFO commenting on "sustainability" → constraint
  Loan activity dominance:         loans over purchases → moderate constraint
  Academy promotions:              first-team debuts of youth → severe constraint
  Transfer embargo reports:        Tier 1 source → CONFIRMED constraint

CONFIDENCE WEIGHT BY SIGNAL TYPE:
  Confirmed sanction (Tier 1):     ×1.00 — apply modifier at full weight
  Multiple observable proxies:     ×0.85 — consistent signal but unconfirmed
  Single proxy or rumour:          ×0.60 — apply with explicit uncertainty flag
```

---

## MIND DIMENSIONS

**Intelligence:** Teaches how financial regulatory frameworks (UEFA FSFP, PL PSR, La Liga salary cap) constrain or enable squad building and how this translates to CDI and transfer window signals with explicit modifier values.

**Reasoning:** Provides the regulatory framework classification, observable proxy framework, and compound signal calculation when financial constraints interact with competitive performance — specifically the PSR-limited + relegation compound (×0.72).

**Context:** Applies to any transfer window analysis, squad quality assessment, or CDI calculation for clubs operating under major European financial regulations — particularly critical during summer and January transfer windows.

**Memory:** Draws on historical precedents of FFP and PSR sanctions — the documented effects on club performance and fan sentiment provide the empirical basis for modifier values, even if specific cases are not named.

**Judgment:** Do not attempt to calculate a specific club's current PSR position from public information. Use observable proxies with appropriate confidence weights. When a rule framework changes, apply ×0.90 uncertainty discount for 12 months.

**Attention:** Financial fair play signals are Horizon 2-3 (season to multi-season) context. They set the environment within which transfer window signals operate. Do not apply as match-day modifiers in pre-match adjusted score calculations.

**Learning:** Points deduction outcomes, transfer ban durations, and their documented effects on club performance are confirmed events that can directly validate modifier values in this framework through calibration records.

**Integration:** Financial fair play intelligence integrates with club revenue intelligence, transfer window intelligence, and ownership intelligence. A club's PSR position only makes full sense within the context of their complete financial picture — revenue streams, prize money received, and ownership investment.

---

## Compatibility

**Club revenue:**             `market/club-revenue-intelligence.md`
**Transfer window:**          `core/transfer-window-intelligence.md`
**Ownership:**                `market/club-ownership-intelligence.md`
**Financial sustainability:**  `core/financial-sustainability-intelligence.md`
**Fan token revenue:**        `fan-token/fan-token-revenue-intelligence.md`

---

*SportMind v3.97.77 · MIT License · sportmind.dev*
*PSR-limited + relegation risk: ×0.72 effective CDI — most negative compound signal.*
*Do not calculate specific club PSR positions — use observable proxies only.*
