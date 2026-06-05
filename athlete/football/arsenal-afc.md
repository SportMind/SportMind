---
name: arsenal-afc
description: >
  Arsenal FC ($AFC) athlete intelligence reasoning framework. FTP PATH_2 confirmed —
  every key player availability decision carries both match outcome and supply
  mechanic implications. Position-specific modifier chains, compound absence logic,
  and PATH_2 athlete signal integration. Load alongside fan-token/arsenal.md
  and fan-token/ftp-path2.md for full signal chain.
---

# Arsenal FC ($AFC) — Athlete Intelligence

**FTP PATH_2 CONFIRMED. Every key player availability decision carries
both match outcome probability AND supply mechanic implications.
Agents must reason about both dimensions simultaneously.**

> SportMind Library Rule: no named players, no current injury status,
> no transfer rumours. This file teaches agents how to reason about
> Arsenal athlete signals — not what is true right now.

Load alongside: `fan-token/arsenal.md` · `fan-token/ftp-path2.md`

---

## FTP PATH_2 athlete signal chain

```
WHY ARSENAL ATHLETE INTELLIGENCE IS UNIQUE:

  $AFC is the only confirmed FTP PATH_2 club in the library.
  PATH_2 mechanics: WIN burns tokens, LOSS mints tokens.
  
  The athlete intelligence layer therefore affects TWO outputs simultaneously:
  
  OUTPUT 1 — Match outcome probability:
    Standard modifier pipeline applies.
    Key player absence → adjusted score shift → direction signal.
  
  OUTPUT 2 — Pre-match liquidation pool dynamics:
    PATH_2 pre-liquidation: ~1/400 of circulating supply per qualifying match.
    A key absence that shifts Arsenal's win probability downward ALSO shifts:
      → Expected burn magnitude (lower win probability = lower expected burn)
      → CDI demand signal (uncertainty = demand hesitation from sophisticated holders)
    
  AGENT RULE:
    Never evaluate Arsenal athlete intelligence as purely a match signal.
    Always propagate through the PATH_2 chain:
      Athlete availability → win probability → expected supply event magnitude → CDI impact
```

---

## Position reasoning frameworks

### Right winger — primary attacking threat

```
RIGHT WINGER / PRIMARY ATTACKING THREAT:

  ROLE IN SYSTEM:
    Arsenal's right wing position is their highest-frequency attacking outlet.
    The right winger drives chance creation, direct goal threat, and wide
    progression that sets up central overloads. No position has a higher
    individual modifier weight in Arsenal's system.
    
  MODIFIER FRAMEWORK:
    CONFIRMED AVAILABLE (right winger, first choice):
      attacking_output_modifier = ×1.10 | match outcome signal: FULL WEIGHT
      PATH_2 context: elevated win probability, full expected burn magnitude
    
    CONFIRMED ABSENT (right winger, first choice):
      adjusted_score_shift = −8 to −10 points
      attacking_output_modifier = ×0.85
      PATH_2 context: materially reduced win probability, reduced expected burn
      CDI signal: confirmed absence is a bearish demand signal for sophisticated holders
    
    STATUS UNKNOWN / UNCONFIRMED:
      Apply: lineup_unconfirmed_flag = true
      Reduce signal confidence: apply ×0.90 to directional weight
      Do not size pre-match position until T-2h confirmation
    
  PATH_2 COMPOUND NOTE:
    Right winger absence + any other key absence = compound modifier.
    See compound absence framework below.
```

### Captain / creative midfielder

```
CAPTAIN / CREATIVE MIDFIELDER:

  ROLE IN SYSTEM:
    Arsenal's captain anchors squad cohesion, set piece delivery, and creative
    output from deep or central positions. Captaincy carries a cohesion modifier
    beyond individual tactical contribution.
    
  MODIFIER FRAMEWORK:
    AVAILABLE:
      set_piece_modifier = ×1.05 (captain delivers key set pieces)
      cohesion_modifier = ×1.03 (captaincy presence)
      Path2 context: marginal positive win probability contribution
    
    ABSENT:
      adjusted_score_shift = −4 to −6 points
      set_piece_specialist_loss = true
      cohesion_modifier = ×0.97 (captain absent — small reduction)
      
  SET PIECE NOTE:
    If captain is the primary set piece taker, their absence removes a
    high-probability expected goal source from corners and free kicks.
    Apply: expected_goal_reduction = −0.15 xG per match (conservative estimate).
```

### Centre back partnership

```
CENTRE BACK PARTNERSHIP — DEFENSIVE SOLIDITY:

  ROLE IN SYSTEM:
    Arsenal's defensive shape depends on an established centre back pairing.
    When the first-choice pair is available, Arsenal concede at a lower
    expected goals rate than when either is absent.
    
  MODIFIER FRAMEWORK:
    BOTH FIRST-CHOICE CBs AVAILABLE:
      defensive_modifier = ×1.05
      aerial_duel_modifier = ×1.05 (partnership coordination established)
      
    ONE CB ABSENT:
      defensive_modifier = ×0.95
      adjusted_score_shift = −3 to −4 points (defensive weakening)
      
    BOTH CBs ABSENT:
      defensive_modifier = ×0.85
      adjusted_score_shift = −6 to −8 points
      PATH_2 context: significant win probability reduction; expect reduced burn
      
  PARTNERSHIP COHESION NOTE:
    A new pairing requires time to build coordination. If both CBs are absent
    and the replacement pairing has limited shared match time, apply an
    additional coordination_penalty = ×0.97 for the first 2 matches of the pairing.
```

### Defensive midfielder — pressing engine

```
DEFENSIVE MIDFIELDER / PRESSING ENGINE:

  ROLE IN SYSTEM:
    Arsenal's pressing system requires a defensive midfielder who covers ground,
    wins back possession, and protects the defensive line. This position is the
    engine of the pressing system — without it, pressing intensity drops measurably.
    
  MODIFIER FRAMEWORK:
    AVAILABLE:
      pressing_intensity_modifier = ×1.05
      transition_signal_weight = FULL (rapid counter-press is live)
      
    ABSENT:
      pressing_intensity_modifier = ×0.90
      adjusted_score_shift = −3 to −4 points
      Note: absence affects TRANSITIONS more than possession play;
        apply higher modifier weight for high-tempo opponents who exploit transitions
        
  PRESSING NOTE:
    Pressing intensity modifier interacts with opponent style:
      vs fast transitioning opponent + DM absent = compound vulnerability signal
      Apply: transition_vulnerability_flag = true when DM absent and opponent
        is identified as a high-tempo, fast counter-attacking team.
```

### Left centre back / defensive versatility

```
LEFT CENTRE BACK / DEFENSIVE VERSATILITY:

  ROLE IN SYSTEM:
    Arsenal's back four requires a left-sided centre back who is comfortable
    in possession, capable of progressive carrying, and able to play in a
    high defensive line. This position is often filled by players with
    hybrid left back / centre back profiles.
    
  MODIFIER FRAMEWORK:
    AVAILABLE (first-choice left CB / defensive versatility player):
      defensive_modifier = ×1.04
      progressive_carry_modifier = ×1.03 (contributes to build-up out wide)
      
    ABSENT:
      adjusted_score_shift = −3 to −5 points
      defensive_modifier = ×0.94
      Note: positional versatility loss — backup may be pure CB without
        the progressive carrying that Arsenal's system depends on from
        the left side
      Apply: positional_fit_discount = ×0.97 if replacement is a
        right-footed CB filling the left side

  ARRIVAL PREMIUM (new left CB signing):
    When a new quality left CB joins Arsenal, apply the standard arrival
    framework from tier-a-clubs-framework.md, PLUS:
    PATH_2 uplift: improved defensive cover → improved clean sheet probability
      → marginally elevated win probability → apply path2_arrival_uplift
    Position note: CB arrival affects defensive solidity more durably than
      a winger arrival — PATH_2 signal persists across multiple matches
      (vs winger whose impact is more match-specific)
```



```
COMPOUND ABSENCE FRAMEWORK ($AFC SPECIFIC):

  Multiple key absences compound in Arsenal's match outcome probability
  AND in PATH_2 expected supply event magnitude.

  COMPOUND ABSENCE LEVELS:

  LEVEL 1 — Single key absence:
    Apply: individual position modifier (see above)
    PATH_2: apply standard win probability reduction; size burn expectation accordingly
    Signal: PROCEED with modified confidence

  LEVEL 2 — Two key absences:
    Apply: compound_modifier = product of individual modifiers (multiply, not add)
    Example: right winger absent (×0.85) × CB absent (×0.95) = ×0.8075 combined
    PATH_2: materially reduced expected burn magnitude; flag for holder awareness
    Signal: PROCEED with reduced confidence; note compound modifier in output

  LEVEL 3 — Three or more key absences:
    apply: HOLD_RECOMMENDED = true
    Do not generate directional signal until lineups confirmed at T-2h
    PATH_2: very low win probability; expected supply event = DRAW or LOSS scenario
      → PATH_2 burn probability low; mint probability elevated
    Signal: HOLD — confirm at T-2h before generating signal

  COMPOUND MODIFIER RULE:
    Never add modifiers — always multiply.
    Never apply >3 separate modifiers without flagging for human review.
```

---

## Squad depth evolution reasoning

```
SQUAD DEPTH AS A FORWARD SIGNAL:

  Arsenal's squad depth affects how much individual player absences matter.
  As squad depth increases over seasons, the modifier weight per individual
  absence decreases progressively.

  DEPTH SIGNAL FRAMEWORK:
    SHALLOW SQUAD (≤16 quality first-team players):
      Individual absence modifiers apply at FULL WEIGHT
      Single key absence: full modifier
      Two absences: full compound modifier
      
    STANDARD SQUAD (17-20 quality first-team players):
      Individual absence modifiers apply at ×0.90 weight
      Depth reduces but does not eliminate individual modifier impact
      
    DEEP SQUAD (21+ quality first-team players):
      Individual absence modifiers apply at ×0.80 weight
      Club-level depth premium: apply squad_depth_discount = ×0.80 to all
      individual modifiers
      PATH_2 note: even with depth, right winger absence retains FULL modifier
        weight (no replacement at that quality threshold)

  HOW TO ASSESS CURRENT DEPTH:
    Count first-team players who can start without significant quality drop.
    Include youth graduates only if they have demonstrated first-team readiness.
    Update depth assessment at start of each season transfer window conclusion.
```

---

## Compatibility

**FTP mechanics:**     `fan-token/ftp-path2.md`
**$AFC supply data:**  `fan-token/arsenal.md`
**Base framework:**    `athlete/football/athlete-intel-football.md`
**Tier A framework:**  `athlete/football/tier-a-clubs-framework.md`
**Core athlete:**      `core/core-athlete-modifier-system.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Arsenal ($AFC) athlete intelligence: squad depth, key player form, and FTP PATH_2 context |
| Reasoning | ACTIVE | AFC reasoning chain from squad/player signals to APS and FTP PATH_2 modifier |
| Context | ACTIVE | AFC context: PL Champions 2025/26, UCL Final 2026, FTP PATH_2 active — match results trigger supply events |
| Memory | ACTIVE | Historical Arsenal player form patterns — Ben White OUT, Havertz UCL final scorer |
| Judgment | ACTIVE | Judgment on AFC signal hierarchy — FTP PATH_2 means all results have supply event implications |
| Attention | ACTIVE | Maximum attention for Arsenal match results — all trigger $AFC supply events via PATH_2 |
| Communication | ACTIVE | AFC athlete output with APS modifier, squad state, and PATH_2 supply event type |
| Verification | ACTIVE | Arsenal squad data from official Arsenal announcements and training observations |
| Learning | ACTIVE | AFC APS calibration enriched by UCL Final record 130 and three April 2026 PATH_2 records |
| Integration | ACTIVE | Integrates with fan-token/arsenal.md, ftp-path2.md, and core athlete modifier system |
| Calibration | ACTIVE | AFC APS modifier calibrated — PATH_2 supply event calibration: WIN -159,025 / LOSS +100,000 |
| Adaptation | ACTIVE | AFC intelligence adapts as FTP PATH_2 pool sizes and squad composition evolve |
| Ethics | NOT APPLICABLE | AFC athlete intelligence is sports/crypto analysis — no ethical dimension |
| Transparency | ACTIVE | APS modifier, PATH_2 status, and supply event type always explicit in Arsenal outputs |


---

*SportMind v3.97.26 · MIT License · sportmind.dev*
*FTP PATH_2 confirmed — dual-dimension reasoning required for all $AFC signals*
