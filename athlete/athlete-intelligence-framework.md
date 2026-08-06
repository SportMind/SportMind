---
name: athlete-intelligence-framework
description: >
  Master entry point for the SportMind athlete intelligence layer. Covers what
  the athlete intelligence layer does, the APS composite modifier range (0.55–1.25×),
  the six-step athlete reasoning chain, and routing to all 47 sport-specific
  athlete intelligence files. Load this file before any sport-specific athlete file.
  All 14 Mind dimensions mapped.
---

# Athlete Intelligence Framework — Master Entry Point

**APS composite modifier range: 0.55–1.25×**
**Sport-specific files:** 47 across 29 sports
**Calibration anchor:** 130 records — athlete signals are the most material single-layer modifier

---

## What the athlete intelligence layer does

```
PURPOSE:
  The athlete intelligence layer translates player-level information into
  a single composite modifier (APS — Athlete Performance Signal) applied
  to the base adjusted score from the sport domain layer.

  It does NOT predict individual player performance.
  It DOES assess the probability-weighted impact of current athlete state
  on the team's collective performance output.

SCOPE:
  Covers: availability (injured/suspended/doubtful), form, fitness,
    psychological readiness, fatigue load, and position-specific impact.
  Does NOT cover: current specific injury reports, named player current status
    (these are fetched from primary sources by the agent — they are inputs,
    not library content).
  Library Rule: No named current player status in this file. Enduring
    frameworks only.
```

---

## APS composite modifier

```
APS COMPOSITE MODIFIER RANGE: 0.55–1.25×

  FULL STRENGTH (1.00–1.10×):
    Key players available and confirmed. No significant absences.
    Form: stable or improving. No psychological flags.
    Typical baseline for a well-prepared Tier A club.

  ENHANCED (1.10–1.25×):
    Key player(s) in peak form. Confirmed fit after injury concern resolved.
    Psychological momentum positive. System functioning above baseline.
    Apply ×1.25 only when multiple independent positive signals align.

  REDUCED (0.85–0.99×):
    One or two rotation or depth players absent.
    Mild form concerns. Minor fatigue signals.
    No critical position affected.

  SIGNIFICANT REDUCTION (0.70–0.84×):
    Tier A player absent (key position). Team in poor form (3+ losses).
    Manager under significant pressure. Squad cohesion signals negative.

  CRITICAL REDUCTION (0.55–0.69×):
    Multiple Tier A absences. Key position(s) uncovered.
    Goalkeeper, starting centre-back, or primary striker absent.
    Reserve goalkeeper starting. Apply only when multiple
    independent critical signals confirmed.

COMPOSITE CALCULATION:
  APS = availability_modifier × form_modifier × fitness_modifier
  Where each sub-modifier has its own range:
    availability_modifier: 0.70–1.00 (confirmed OUT = 0.70–0.88 by tier)
    form_modifier:         0.90–1.10 (recent performance direction)
    fitness_modifier:      0.92–1.05 (load, fatigue, travel, psychological)

  Never add sub-modifiers. Always multiply.
  ×0.88 × ×0.95 × ×1.00 = ×0.836 (not ×0.83 by addition).
```

---

## Six-step athlete reasoning chain

```
STEP 1: CHECK AVAILABILITY
  Source: official squad announcement, club social media (Tier 1),
    training ground observation (Tier 2), press conference hedging (Tier 3).
  Question: Is the athlete confirmed available, doubtful, or confirmed OUT?

  IF CONFIRMED OUT:
    Apply ABSENCE modifier immediately.
    Tier A position (GK, primary CB, primary CDM, primary striker): ×0.78–0.88
    Tier B position (second striker, wide forward, fullback): ×0.88–0.95
    Tier C (rotation player, fringe squad): ×0.97–1.00 (system absorbs)
    Do not proceed further for this player — absence is confirmed.

  IF DOUBTFUL:
    Apply probability-weighted modifier (50% available × full modifier +
      50% absent × absence modifier).
    Flag as lineup_unconfirmed = true in output.

  IF AVAILABLE:
    Proceed to Step 2.

STEP 2: ASSESS FORM
  Window: last 5 competitive appearances (not friendly matches).
  Question: What is the direction of the form curve?

  IMPROVING:    3+ of last 5 above baseline. Apply ×1.05–1.10.
  STABLE:       Mixed or consistent at baseline. Apply ×1.00.
  DECLINING:    3+ of last 5 below baseline. Apply ×0.90–0.95.
  CONCERNING:   5 of last 5 below baseline. Apply ×0.85–0.90.

  Form modifier is directional, not absolute. A strong player in declining
  form is still likely to perform — the modifier adjusts, not replaces, the
  baseline expectation.

STEP 3: CHECK FITNESS FLAGS
  Three primary fitness flags:

  DSM (DISCIPLINARY STATUS MODIFIER):
    Suspended or accumulating yellow cards near ban threshold?
    Suspension confirmed → treated as OUT (Step 1).
    One yellow card from ban → flag SUSPENSION_RISK, apply ×0.97.

  INJURY HISTORY FLAG:
    Returning from significant injury (ACL, muscle tear, fracture)?
    Apply RETURN_FROM_INJURY modifier: ×0.90–0.95 for first 3 appearances.
    Reasoning: statistical pattern of performance reduction on return.

  COMMERCIAL_RISK_ACTIVE FLAG:
    Contract dispute, public club-player conflict, transfer request reported?
    Apply COMMERCIAL_RISK modifier: ×0.92–0.97.
    Flag immediately in output: COMMERCIAL_RISK_ACTIVE = true.
    This is a SOFT signal — requires multi-source confirmation.

STEP 4: APPLY SPORT-SPECIFIC FILE
  Route to: athlete/{sport}/athlete-intel-{sport}.md
  Purpose: sport-specific position weights, role modifiers, and
    calibrated absence values for this sport domain.

  ROUTING TABLE:
    Football:     athlete/football/athlete-intel-football.md
    Cricket:      athlete/cricket/athlete-intel-cricket.md
    Basketball:   athlete/nba/athlete-intel-nba.md
    MMA:          athlete/mma/athlete-intel-mma.md
    Formula 1:    athlete/formula1/athlete-intel-formula1.md
    Tennis:       athlete/tennis/athlete-intel-tennis.md
    Ice Hockey:   athlete/nhl/athlete-intel-nhl.md
    Rugby Union:  athlete/rugby/athlete-intel-rugby-union.md
    Rugby League: athlete/rugby-league/athlete-intel-rugby-league.md
    AFL:          athlete/afl/athlete-intel-afl.md
    Athletics:    athlete/athletics/athlete-intel-athletics.md
    MotoGP:       athlete/motogp/athlete-intel-motogp.md
    NASCAR:       athlete/nascar/athlete-intel-nascar.md
    NHL:          athlete/nhl/athlete-intel-nhl.md
    NFL:          athlete/nfl/athlete-intel-nfl.md
    Boxing:       athlete/boxing/athlete-intel-boxing.md
    Kabaddi:      athlete/kabaddi/athlete-intel-kabaddi.md
    Handball:     athlete/handball/athlete-intel-handball.md
    Golf:         athlete/golf/athlete-intel-golf.md
    Snooker:      athlete/snooker/athlete-intel-snooker.md
    Darts:        athlete/darts/athlete-intel-darts.md
    Swimming:     athlete/swimming/athlete-intel-swimming.md
    Cycling:      athlete/cycling/athlete-intel-cycling.md
    Winter sports: athlete/winter-sports/athlete-intel-winter-sports.md
    Rowing:       athlete/rowing/athlete-intel-rowing.md
    Netball:      athlete/netball/athlete-intel-netball.md
    Baseball:     athlete/baseball/athlete-intel-baseball.md
    Horse Racing: athlete/horse-racing/athlete-intel-horse-racing.md
    Esports:      athlete/esports/athlete-intel-esports.md

STEP 5: CALCULATE APS MODIFIER
  Combine Step 1 (availability) × Step 2 (form) × Step 3 (fitness).
  Apply sport-specific position weighting from Step 4.
  Output: single APS modifier value between 0.55 and 1.25.

  CALCULATION EXAMPLE:
    Confirmed available (×1.00) × improving form (×1.07) ×
    no fitness flags (×1.00) × Tier A midfielder position weight = ×1.07
    
    Confirmed OUT, Tier A position (×0.82) × N/A × N/A = ×0.82

  APS modifier feeds directly into:
    Pre-match adjusted score calculation (multiplicative)
    FTP PATH_2 WIN probability estimate (lower APS = lower WIN probability)
    Fan token demand signal (key player news affects demand independently)

STEP 6: FLAG UNCERTAINTY
  Four uncertainty flags that must be set explicitly:

  lineup_unconfirmed:
    True if official squad has not been announced at time of signal.
    Applies to all pre-T-2h signals for all competitions.
    Effect: reduce confidence tier by one level (HIGH → MEDIUM-HIGH, etc.)

  injury_doubtful:
    True if availability is reported as doubtful without official confirmation.
    Effect: apply probability-weighted modifier (Step 1 doubtful pathway).

  commercial_risk_active:
    True if Step 3 COMMERCIAL_RISK flag was triggered.
    Effect: flag in output, apply ×0.92–0.97 modifier.

  return_from_injury:
    True if athlete is returning from significant injury (Step 3).
    Effect: apply ×0.90–0.95 for first 3 appearances.
```

---

## Position tier table

```
POSITION TIERS (cross-sport framework):

  TIER A — SYSTEM CRITICAL:
    Football: Goalkeeper, primary centre-back, primary CDM, primary striker
    Basketball: Primary point guard, primary centre
    Ice hockey: Starting goaltender, primary defensive pair
    MMA: The fighter (single athlete — maximum tier)
    Cricket: Primary opener, primary fast bowler, primary spinner
    Absence modifier: ×0.78–0.88

  TIER B — HIGH IMPACT:
    Football: Second striker, wide forward, fullback, attacking midfielder
    Basketball: Secondary scorer, secondary playmaker
    Cricket: Middle-order batter, secondary bowler
    Absence modifier: ×0.88–0.95

  TIER C — ROTATIONAL:
    All sports: depth squad players whose absence does not disrupt system
    Absence modifier: ×0.97–1.00 (system absorbs — no meaningful signal)
```

---

## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Master athlete intelligence framework — APS calculation, position tiers, routing to 29 sport-specific files |
| Reasoning | ACTIVE | Six-step athlete reasoning chain from availability check through APS composite output |
| Context | ACTIVE | Context determines position tier weight — same absence has different impact by sport and system |
| Memory | ACTIVE | Historical form window (last 5 appearances), injury history, return-from-injury pattern data |
| Judgment | ACTIVE | Judgment gates at Steps 1-3 — confirmed OUT vs doubtful vs available require different reasoning paths |
| Attention | ACTIVE | Elevated attention for Steps 1 and 3 — availability confirmation and fitness flags are highest-priority athlete signals |
| Communication | ACTIVE | APS modifier output is a single decimal value — all six steps contribute to that one number |
| Verification | ACTIVE | Step 1 explicitly requires source tier verification — Tier 1 official vs Tier 3 press conference differ |
| Learning | ACTIVE | APS calibration improves from calibration records — modifier values are empirically derived |
| Integration | ACTIVE | Athlete layer integrates with sport domain (Step 4), pre-match signal framework, and FTP PATH_2 |
| Calibration | ACTIVE | APS modifier range (0.55–1.25×) calibrated from historical player absence-to-outcome correlation |
| Adaptation | ACTIVE | Routing table adapts as new sports and athlete files are added to the library |
| Ethics | ACTIVE | No named current player status in this file — Library Rule compliance, athlete privacy respected |
| Transparency | ACTIVE | APS modifier components (availability × form × fitness) always explicit in output |
| Execution | ACTIVE | Six-step pre-match workflow, event playbooks, and command references defined |
| Collaboration | ACTIVE | Integrates with core frameworks, sport domain layer, fan token registry, and macro intelligence |

---

## Compatibility

**Pre-match orchestration:** `core/pre-match-signal-framework.md`
**Agent entry point:**       `core/agent-onboarding.md`
**Master architecture:**     `core/master-reasoning-architecture.md`
**Injury intelligence:**     `core/injury-intelligence/injury-reasoning-framework.md`
**Disciplinary signals:**    `core/athlete-disciplinary-intelligence.md`

---

*SportMind v3.97.111 · MIT License · sportmind.dev*
*APS composite modifier range: 0.55–1.25×. Six steps. One output number.*
*All 14 Mind dimensions mapped.*
