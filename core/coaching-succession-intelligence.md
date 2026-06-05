---
name: coaching-succession-intelligence
description: >
  Enduring trajectory model for coaching succession events — from LEGACY_END
  through TRANSITION to STABILISATION. Covers SOFT_LANDING vs HARD_RESET
  classification, modifier values for each phase, the 10-year legacy amplifier,
  named successor signal timing, and $CITY reference case. Required companion
  to core/manager-intelligence.md when a succession event is confirmed.
---

# Coaching Succession Intelligence

**The trajectory model POST_LEGACY_LIMBO needs: LEGACY_END → TRANSITION → STABILISATION.**
POST_LEGACY_LIMBO identifies the state. This file provides the trajectory through it.

---

## The succession trajectory

```
THREE-PHASE MODEL:

  LEGACY_END:
    Trigger: manager of 5+ seasons departs or announces departure.
    Characteristics: era is closing. Successor may or may not be named.
    Duration: from announcement to successor's first competitive match.
    Key diagnostic: SOFT_LANDING or HARD_RESET? (see below)

  TRANSITION:
    Trigger: new manager takes charge.
    Characteristics: tactical identity uncertain. Squad may or may not suit new style.
    Duration: first 5-15 competitive matches under new manager.
    Key diagnostic: are results tracking SOFT_LANDING expectations?

  STABILISATION:
    Trigger: new tactical identity confirmed through results and observable patterns.
    Characteristics: modifier returns to standard framework. No succession discount.
    Duration: indefinite — until the next succession event.
    Key diagnostic: has the squad adapted? Are results consistent?

PHASE TRANSITIONS ARE NOT CALENDAR-BASED:
  Do not apply a fixed number of weeks to each phase.
  Transitions are triggered by observable evidence, not time elapsed.
```

---

## SOFT_LANDING vs HARD_RESET

```
SOFT_LANDING — CONDITIONS:
  1. Outgoing manager exits with UCL qualification for next season, AND
  2. Named incoming manager confirmed before or at transition start.

  SOFT_LANDING modifier: ×0.85 governance modifier during TRANSITION phase.
  Rationale: uncertainty is bounded. The club retains UCL status and community
    confidence is anchored by a named successor. The demand floor is preserved.
  Recovery to standard: after 5 competitive results under incoming manager.

  SOFT_LANDING subcategories:
    PLANNED_EXIT (manager announces in advance): ×0.88 governance (less uncertainty)
    UNPLANNED_BUT_CLEAN (sudden exit but named successor): ×0.85 governance
    MUTUAL_DEPARTURE: ×0.85 governance (same as UNPLANNED_BUT_CLEAN)

HARD_RESET — CONDITIONS:
  Either (or both):
  · Outgoing manager exits WITHOUT UCL qualification for next season.
  · No named successor at transition start — extended vacancy.

  HARD_RESET modifier: ×0.78 governance modifier during TRANSITION phase.
  Duration: until UCL status is clarified (current season trajectory) AND
    successor is named and officially confirmed.
  Community engagement modifier: ×0.90 (significant uncertainty effect).

  HARD_RESET extended vacancy rule:
    If no named successor after 14 days from LEGACY_END:
      Apply: additional ×0.95 confidence discount stacked on ×0.78.
      Effective governance: ×0.74.
    After 30 days: escalate to LEADERSHIP_VACUUM framework.
    Reference: core/trust-breakdown-intelligence.md if conduct questions emerge.
```

---

## Legacy amplifier

```
LEGACY TENURE DURATION AMPLIFIER:
  Longer tenures produce larger community psychological effects at departure.
  The legacy amplifier scales the baseline succession modifier.

  Under 3 seasons:    No amplifier. Standard transition modifiers apply.
  3-5 seasons:        ×1.05 amplifier to community sentiment effect.
  5-10 seasons:       ×1.10 amplifier. Community attachment is structural.
  10+ seasons:        ×1.15 amplifier. Era-defining tenure. Maximum effect.

  How to apply the amplifier:
    It multiplies the MAGNITUDE of community sentiment disruption — not the CDI directly.
    Apply to: community engagement modifier, governance vote participation weight,
      and social sentiment confidence weight for first 4-8 weeks of transition.
    It does NOT amplify the governance modifier itself (×0.85 or ×0.78).
    It amplifies how long and how intensely the community feels the transition.

  Example — SOFT_LANDING with 10-season legacy (×1.15 amplifier):
    Governance modifier: ×0.85 (SOFT_LANDING, unchanged by amplifier)
    Community engagement: ×0.96 × ×1.15 amplification = deeper effect.
    Duration of community effect: 6-8 weeks vs 4 weeks for a shorter tenure.
```

---

## Named successor timing signal

```
NAMED SUCCESSOR CONFIRMED BEFORE LEGACY_END:
  Best case. Uncertainty window is minimal.
  Apply: ×0.90 governance (lighter than standard SOFT_LANDING ×0.85).
  Rationale: community can direct attention to the new era before the old one closes.

NAMED SUCCESSOR CONFIRMED AT LEGACY_END:
  Standard SOFT_LANDING case. Apply: ×0.85 governance.

NAMED SUCCESSOR: VERBAL_AGREEMENT ONLY:
  Agreement confirmed but contract not yet signed.
  Apply: ×0.88 governance (between NAMED and unsigned).
  Monitor for: confirmation vs collapse of the verbal agreement.
  If verbal agreement collapses: immediately re-assess as HARD_RESET.

NAMED SUCCESSOR CONFIRMED — DIFFERENT MANAGEMENT STYLE:
  If incoming manager's documented style is significantly different from outgoing:
  Apply: additional ×0.95 to tactical identity modifier for first 10 matches.
  Rationale: squad may not suit the new system. Transition risk is elevated.
  Reference: core/manager-intelligence.md for style assessment framework.
```

---

## Reference case: Manchester City 2026

```
$CITY SOFT_LANDING — SUCCESSION REFERENCE CASE

LEGACY_END:
  Tenure duration: 10 seasons (2016-2026) → ×1.15 legacy amplifier.
  Final position: 2nd — 78 points.
  UCL 2026/27: CONFIRMED — SOFT_LANDING condition 1 met.
  GUARDIOLA_TENURE: CLOSED.

TRANSITION:
  Successor: Enzo Maresca.
  Successor status at legacy end: VERBAL_AGREEMENT.
  SOFT_LANDING condition 2: MET (named successor confirmed).
  Classification: SOFT_LANDING — VERBAL_AGREEMENT subtype.

MODIFIERS APPLIED:
  Governance: ×0.85 (SOFT_LANDING standard)
  Community engagement amplifier: ×1.15 (10-season tenure)
  Duration of community effect: 6-8 weeks from season close.
  Recovery trigger: after 5 competitive results under Maresca.

$CITY FAN TOKEN IMPLICATIONS:
  SOFT_LANDING preserves the demand floor.
  UCL confirmation maintains ×1.15 CDI trajectory.
  Governance modifier ×0.85 applies during TRANSITION phase only.
  Post-STABILISATION: return to standard governance weight (×1.00).
  Compound (TRANSITION period): UCL ×1.15 × governance ×0.85 = ×0.98 effective.
  Compound (STABILISATION): UCL ×1.15 × governance ×1.00 = ×1.15 full.
```

---

## REASONING CHAIN — SUCCESSION EVENT

```
STEP 1 — Confirm LEGACY_END:
  Is the departing manager a legacy figure? (5+ seasons)
  If yes: apply legacy amplifier from tenure duration table.
  If no: apply standard manager change framework from manager-intelligence.md.

STEP 2 — Classify: SOFT_LANDING or HARD_RESET?
  Check condition 1: UCL qualification for next season?
  Check condition 2: named successor confirmed?
  Both met → SOFT_LANDING. Either missing → HARD_RESET.

STEP 3 — Apply phase modifier:
  SOFT_LANDING: ×0.85 governance during TRANSITION.
  HARD_RESET: ×0.78 governance during TRANSITION.
  Apply legacy amplifier to community engagement effects.

STEP 4 — Set TRANSITION recovery trigger:
  5 competitive results under new manager.
  Review at trigger: are results and tactical identity emerging?
  Yes → STABILISATION. No → extend TRANSITION with updated assessment.

STEP 5 — STABILISATION:
  Remove succession modifier. Return to standard framework.
  Apply new manager's documented style modifier from manager-intelligence.md.
  Reset community engagement to standard weight.
```

---

## MIND DIMENSIONS

**Intelligence:** Teaches the three-phase succession trajectory (LEGACY_END → TRANSITION → STABILISATION) and the SOFT_LANDING vs HARD_RESET classification with associated modifier values.

**Reasoning:** Provides the five-step succession reasoning chain from legacy confirmation through STABILISATION, including the legacy amplifier calculation and named successor timing signal framework.

**Context:** Applies whenever a manager with 5+ seasons departs — essential companion to core/manager-intelligence.md for major succession events. Also triggers when verbal agreements collapse mid-transition.

**Memory:** Draws on the Manchester City 2026 SOFT_LANDING as the first documented succession reference case in SportMind. The ×1.15 legacy amplifier value for 10-season tenures is calibrated against this case.

**Judgment:** Do not apply SOFT_LANDING modifiers if verbal agreement collapses before contract signing — immediately reassess as HARD_RESET. Do not calendar-fix phase transitions — use observable evidence triggers, not week counts.

**Attention:** Succession events are high-attention Horizon 1-2 events during TRANSITION, shifting to Horizon 2-3 at STABILISATION. The recovery trigger (5 competitive results) should be actively monitored, not passively assumed.

**Learning:** Each succession case that completes STABILISATION provides a calibration record for the modifier values. Key question: did SOFT_LANDING ×0.85 correctly bound the demand floor? Record outcome as calibration data for future succession events.

**Integration:** Succession intelligence integrates with manager-intelligence.md (incoming manager style), trust-breakdown-intelligence.md (if conduct questions emerge), trajectory-intelligence.md (club trajectory continuity), and fan-token CDI frameworks (governance modifier effect on token demand). Load all four simultaneously for major succession events.

---

## Compatibility

**Manager intelligence:**      `core/manager-intelligence.md`
**Trust breakdown:**           `core/trust-breakdown-intelligence.md`
**Trajectory:**                `core/trajectory-intelligence.md`
**Man City reference:**        `athlete/football/tier-a-clubs-framework.md`
**POST_LEGACY framework:**     `core/psychological-intelligence.md`

---

---

## COACHING_STATUS three-state framework

*Extracted from athlete/football/lazio.md — enduring framework applicable to all clubs.*

```
COACHING_STATUS STATES:

  STABILIZED:
    Definition: confirmed head coach with 2+ year contract, tactical identity established.
    Signals: official appointment confirmed, contract duration ≥ 2 years, 5+ results
      completed under current manager, tactical pattern recognised by analysts.
    CDI modifier: ×1.04 (structural certainty premium — community confidence raised)
    Apply when: all three gates confirmed (appointment + contract + identity).

  TRANSITION:
    Definition: new coach confirmed but fewer than 5 results completed.
    Signals: appointment announced, but tactical patterns not yet established.
    CDI modifier: ×0.92 (tactical uncertainty — squad adaptation incomplete)
    Apply when: appointment confirmed but identity gate not yet cleared.

  LIMBO:
    Definition: no confirmed head coach. Caretaker or vacancy.
    Signals: manager departure confirmed, no successor announced, caretaker in charge.
    CDI modifier: ×0.88 (governance uncertainty — community confidence depressed)
    Apply when: incumbent departed and no permanent replacement confirmed.

TRANSITION RULES:
  LIMBO → TRANSITION: triggered by official permanent appointment announcement.
  TRANSITION → STABILIZED: triggered when 5+ results completed + tactical identity clear.
  STABILIZED → LIMBO: triggered if manager departs mid-season (immediate reassessment).
  STABILIZED → TRANSITION: triggered by coaching change even if replacement immediately named.

AGENT RULE:
  Check COACHING_STATUS before applying any manager-dependent signal modifier.
  LIMBO overrides all other coaching modifiers.
  STABILIZED does NOT override tactical matchup modifiers — a stabilised bad system
  is still a bad system vs a specific opponent.
```

*SportMind v3.97.84 · MIT License · sportmind.dev*
*SOFT_LANDING: ×0.85 governance. HARD_RESET: ×0.78. Recovery at 5 competitive results.*
*10-season legacy amplifier: ×1.15 community effect. First documented case: $CITY 2026.*
