---
name: referee-intelligence
description: >
  Enduring reasoning framework for officiating intelligence as a pre-match
  signal modifier. Covers football, rugby union, MMA, and cricket. Defines
  how to identify, weight, and cap officiating signals across all sports.
  Officiating is a probability range modifier — not a direction signal.
---

# Referee and Officiating Intelligence

**Enduring framework for AI agents reasoning about officiating assignment
as a pre-match signal modifier. Applies to every future match across all sports.**

> SportMind Library Rule: every element is true and useful beyond six months.
> No named referees, current appointments, specific match dates, or expiring data.
> This file teaches agents how to think about officiating — not who is officiating today.

---

## Core principle — officiating as probability range modifier

```
FUNDAMENTAL RULE:

  Officiating intelligence is a PROBABILITY RANGE MODIFIER.
  It is NEVER a direction signal on its own.

  What this means:
    Officiating narrows or widens the probability range around the existing signal.
    A card-heavy referee does not make a team more or less likely to win —
    it changes HOW the match is likely to be played, which then interacts
    with each team's playing style to produce a probability adjustment.

  MODIFIER CAP:
    Officiating intelligence alone never shifts adjusted score by more than
    ±5 points without additional corroborating signal.
    If an officiating modifier would shift score by >5 points — flag for
    human review. Do not apply automatically.

  WHEN OFFICIATING BECOMES A DIRECTION SIGNAL:
    Only when BOTH of the following are true:
    1. The officiating profile is extreme (top/bottom 5% of tracked referees)
    2. The playing styles strongly favour one team under that officiating profile
    Example: a penalty-liberal referee assigned to a match where Team A draws
    significantly more penalties than Team B — now a direction nudge is valid,
    but still capped at ±5 points.
```

---

## Football — referee reasoning framework

### Card-tendency profiles

```
CARD TENDENCY CLASSIFICATION:

  STRICT (card-heavy):
    Definition: yellow card rate >30% above sport average per 90 minutes
    Signal implications:
      Aggressive pressing teams: increased booking risk → fatigue and suspension risk
      Fouling defensive units: elevated risk of playing with reduced numbers
      Match tempo: elevated aggression leads to more stoppages; slower pace
    Modifier: strict_referee_modifier — applied when both teams' styles
      are significantly affected. Range: 0.92–1.08 depending on style mismatch.

  PERMISSIVE (low-card):
    Definition: yellow card rate >30% below sport average per 90 minutes
    Signal implications:
      Physical teams rewarded: more contact allowed → physical dominance valued
      Technical teams: less protected; skillful players face more unchecked fouling
      Match tempo: faster, fewer stoppages
    Modifier: permissive_referee_modifier — Range: 0.94–1.06

  NEUTRAL:
    Definition: within 20% of sport average card rate
    Modifier: none applied — standard signal weights

  AGENT RULE:
    Card tendency modifies style-advantage calculations.
    Always check BOTH teams' styles before applying:
    A strict referee assigned to two defensive, low-card teams → no modifier.
    Tendency only matters where it creates a differential between the teams.
```

### Home and away bias

```
HOME-AWAY BIAS IN FOOTBALL OFFICIATING:

  Research consensus: home teams receive measurable officiating advantages
  in crowd-influenced officiating. The mechanism is crowd noise and pressure
  on referee psychology — not deliberate bias.

  BIAS DETECTION PRINCIPLES:
    Home penalty award rate vs away rate (historical, same referee)
    Home vs away foul call differential
    Injury time added: consistently longer when home team is losing?
    Card differential: do away teams receive more cards on average?

  APPLICATION:
    Do not apply home bias as a universal modifier — most referees show
    some home bias, making it already priced into standard home advantage.
    Apply home bias modifier ONLY when a specific referee shows statistically
    extreme home or away bias patterns.
    Home bias modifier: ±0.02 to adjusted score (marginal — already in base)

  HIGH-CROWD ENVIRONMENTS:
    Stadiums with >95% passionate home crowds amplify referee bias risk.
    Neutral venue (World Cup Final, Champions League Final): home bias reduced.
    Apply: neutral_venue_bias_reduction when match is confirmed neutral.
```

### Penalty award rate

```
PENALTY AWARD RATE AS MODIFIER:

  PENALTY-LIBERAL referees:
    Definition: penalty award rate >50% above sport average
    Benefits: teams that play in penalty-attracting style
      (box entries, dribbling, striker movement in the box)
    Disadvantages: teams defending with high defensive line
      (higher exposure to penalty-attracting situations)
    Modifier: liberal_penalty_modifier = ×1.04 for penalty-attracting team
              liberal_penalty_modifier = ×0.96 for exposed defensive team

  PENALTY-CONSERVATIVE referees:
    Definition: penalty award rate >50% below sport average
    Benefits: physical defensive teams (less exposure to awarded penalties)
    Modifier: conservative_penalty_modifier = ×0.97 for attacking-style team

  PLAYING STYLE INTERACTION:
    Only apply penalty modifiers when the assigned team's playing style
    strongly correlates with drawing or conceding penalties.
    Never apply penalty modifier without checking style compatibility first.
```

### VAR reasoning

```
VAR — HOW IT CHANGES REFEREE TENDENCY WEIGHTING:

  VAR modifies which referee tendencies still matter.
  Some on-field referee tendencies are neutralised by VAR.
  Others are amplified.

  TENDENCIES NEUTRALISED BY VAR:
    Clear penalty misses: VAR reviews obvious penalties the referee misses
    Off-ball incidents (red cards): VAR can add retrospective dismissals
    Offside goals: VAR removes most goal-line offside errors
    Result: extreme on-field referee card and penalty tendencies are moderated

  TENDENCIES AMPLIFIED BY VAR:
    VAR threshold for intervention: referees who are reluctant to change
      decisions on review tend to preserve their on-field mistakes
    DOGSO vs yellow: VAR reframes red card situations as DOGSO-or-not
    Penalty check triggers: VAR creates more penalty reviews than pre-VAR,
      benefiting teams whose style generates more marginal contact

  MODIFIED WEIGHTING IN VAR COMPETITIONS:
    Reduce card-tendency modifier by 40% (VAR moderates extreme card bias)
    Preserve penalty-tendency modifier (VAR amplifies penalty review triggers)
    Preserve style-interaction modifiers (playing style still matters)

  NO-VAR COMPETITIONS:
    Apply full referee tendency modifiers without reduction.
    On-field officiating has maximum signal weight without VAR safety net.

  AGENT RULE:
    Always check: is this competition VAR-equipped?
    YES → reduce card tendency weight by 40%
    NO  → apply full tendency modifier
```

### UCL Final and high-stakes appointment reasoning

```
HIGH-STAKES REFEREE APPOINTMENT REASONING (UCL Final example):

  For high-stakes matches (finals, major cup ties), referee selection is itself
  a signal. Governing bodies deliberately select referees with specific profiles
  for high-profile matches.

  WHAT HIGH-STAKES APPOINTMENTS SIGNAL:
    Governing bodies tend to appoint referees with:
      Clean records in recent major matches
      Experience at previous high-stakes fixtures
      Lower controversy history
    This pre-selects for NEUTRAL referees — reducing the variance that
    extreme card or penalty tendencies would introduce.

  IMPLICATION:
    For finals and high-stakes matches: apply reduced referee modifier weighting.
    The appointment process itself biases toward neutral officiating profiles.
    Default: apply ±50% of the standard referee modifier for confirmed finals.

  TIMING — T-2H CONFIRMATION:
    Referee assignment for major matches is typically confirmed at T-2h with
    the official lineup. This is when officiating intelligence becomes actionable.
    Before T-2h: do not apply referee modifier to pre-match signal.
    After T-2h confirmation: apply modifier within ±5 point cap.

  AGENT RULE:
    For any final or major cup tie: reduce referee modifier by 50%.
    High-stakes = deliberate selection toward neutral profiles.
    Apply: finals_referee_reduction = ×0.50 applied to base modifier.
```

---

## Rugby union — referee reasoning framework

```
RUGBY UNION OFFICIATING INTELLIGENCE:

RUCK AND BREAKDOWN INTERPRETATION:
  Rugby referees vary significantly in how they interpret ruck legality.
  Key variance dimensions:
    Sealing-off tolerance: does the referee allow sealing, or penalise strictly?
    Ball availability pressure: does the referee apply "use it" quickly?
    Jackaling standards: how much tolerance for jackaling before a penalty?

  Signal implications:
    Strict breakdown referees benefit ball-carrying teams (penalise sealing = faster ball)
    Permissive breakdown referees benefit defensive sides (more time to compete)
    Quick "use it" referees compress attack time → benefit defences
    
  Modifier: breakdown_style_match_modifier = ±0.03 when style strongly interacts

PENALTY COUNT TENDENCIES:
  High-penalty referees:
    Kicking teams benefit disproportionately (more penalty-kick opportunities)
    Apply: kicking_team_penalty_modifier = ×1.04 (for confirmed kicking-dominant teams)
  Low-penalty referees:
    Rolling maul and power play teams favoured (fewer stoppages, play continues)
    Kicking teams disadvantaged: fewer penalty kicks awarded

SCRUM INTERPRETATION VARIANCE:
  Referees vary significantly in scrum tolerance.
    Strict scrum referees: weak-scrum teams exposed more often
    Permissive scrum referees: collapsed scrums not penalised → nullifies scrum advantage
  Modifier: scrum_dominance_modifier = ±0.03 for confirmed scrum-dominant/weak teams
    Apply only when one team has clear scrum superiority vs weakness.
```

---

## MMA — referee reasoning framework

```
MMA OFFICIATING INTELLIGENCE:

STANDING-UP TENDENCY:
  MMA referees vary in how quickly they stand up grappling exchanges.
    Early stand-up referees: benefit wrestlers and grapplers LESS
      (their advantage in control is cut short by standup)
      Benefit strikers MORE (reset to standing means more striking exchanges)
    Late stand-up referees: benefit wrestlers MORE
      (more time to control from top position, grind out rounds)
    
  MODIFIER FRAMEWORK:
    For a grappler vs striker matchup:
      Early stand-up referee: striker_advantage_modifier = ×1.05
      Late stand-up referee: grappler_advantage_modifier = ×1.05
    
    For evenly matched styles: no modifier.
    Only apply when styles strongly diverge (grappler vs striker, not balanced MMA).

STOPPAGE THRESHOLD VARIANCE:
  Early stoppage referees:
    Benefit: fighters who are likely to be in compromised positions
      (reduces damage from late stoppages)
    Signal: slightly reduces advantage of fighters whose style involves
      grinding through adversity (warriors who absorb punishment to come back)
    Modifier: early_stoppage_modifier = applied when fighter is known
      to fight through adversity vs early stoppage referee
    
  Late stoppage referees:
    Benefit: fighters who have proven "never stopped" records
    Slightly benefits come-from-behind finishers who need time
    Modifier: late_stoppage_modifier = applied for "iron chin" fighters

  CAP REMINDER: MMA officiating modifiers are capped at ±5 points combined.
    Late stoppage + grappler vs striker: maximum combined modifier ±5 points.
```

---

## Cricket — umpire reasoning framework

```
CRICKET UMPIRE INTELLIGENCE:

DRS USAGE PATTERNS:
  In DRS-enabled matches: umpire tendencies interact with DRS usage.
    Conservative umpires (not-out default): batters benefit initially;
      but teams burn reviews faster → changes match strategy
    Aggressive umpires (wicket-positive): bowlers benefit on LBW/caught behind;
      DRS becomes more valuable to batting teams
    
  Agent rule: Always check if DRS is available for this match/series.
    DRS present: umpire LBW tendency moderated (overturnable)
    DRS absent:  umpire LBW tendency has full weight

LBW TENDENCY VARIANCE:
  LBW-prone umpires (high LBW rate):
    Spinners benefit: LBW dismissals are more available for turning deliveries
    Apply: spinner_lbw_modifier = ×1.04 for identified spinning attacks
    
  LBW-conservative umpires (low LBW rate):
    Fast bowlers benefit relatively (caught-behind, bowled still available)
    Spinners disadvantaged: rely on LBW more than pacemen
    Apply: spinner_lbw_modifier = ×0.96 for spinning attacks

SPINNER VS SEAMER SIGNAL WEIGHT:
  Umpire assignment can shift the relative signal weight of bowling attacks.
  LBW-prone umpire + spinning-heavy attack = amplify spin attack signal weight
  LBW-conservative + pace attack = standard signal; no adjustment needed
  
  Apply: bowling_attack_weight_adjustment when umpire profile strongly
    interacts with the dominant bowling type.
```

---

## General officiating principles

```
OFFICIATING SIGNAL FRAMEWORK — SUMMARY:

  STEP 1: IDENTIFY OFFICIATING PROFILE TYPE
    Sources: historical match data, sport-specific statistical databases
    Classification: card tendency | penalty tendency | style tendency
    Tier: extreme (top/bottom 10%) | notable (top/bottom 25%) | neutral

  STEP 2: IDENTIFY STYLE INTERACTION
    Does the officiating profile create a differential between the two teams?
    If NOT (both teams equally affected): no modifier applied
    If YES (one team benefits/suffers): proceed to modifier calculation

  STEP 3: CALCULATE MODIFIER
    Apply style-specific modifier within sport framework above
    Always check: does VAR apply? (reduce card modifier by 40%)
    Always check: is this a final? (reduce by 50%)

  STEP 4: APPLY CAP
    Sum all officiating modifiers
    Cap at ±5 points adjusted score shift
    If >5 points: flag for human review; apply 5 point maximum only

  STEP 5: DOCUMENT
    Note officiating modifier in signal output as:
      officiating_modifier_applied: [value] | [rationale]
    Never apply without documenting the reasoning

WHEN NOT TO APPLY:
  Referee assignment unknown or unconfirmed → no modifier
  Match is a final (without specific extreme profile) → use reduced modifier
  Both teams' styles are similar (modifier creates no differential) → no modifier
  Database is insufficient for reliable classification → no modifier

WHEN OFFICIATING INTELLIGENCE IS STRONG ENOUGH TO SHIFT DIRECTION:
  The signal direction may shift (not just range widen) when ALL of these apply:
    1. Officiating profile is extreme (top/bottom 5% of tracked referees)
    2. One team's style has strong documented positive interaction with this profile
    3. Corroborating signal (e.g. home crowd amplification, key player fitness) aligns
    4. Combined modifier exceeds 3 points in the same direction as existing signal
  This is RARE — most officiating intelligence only widens/narrows probability range.
```

---

## Compatibility

**Football:**   `sports/football/sport-domain-football.md`
**Rugby:**      `sports/rugby/sport-domain-rugby-union.md`
**MMA:**        `sports/mma/sport-domain-mma.md`
**Cricket:**    `sports/cricket/sport-domain-cricket.md`
**Related:**    `core/core-signal-architecture.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Referee intelligence: individual referee profiles, decision tendencies, VAR behaviour |
| Reasoning | ACTIVE | Referee reasoning chain from assignment to match condition modifier |
| Context | ACTIVE | Referee context: competition tier, home/away patterns, card frequency, VAR usage |
| Memory | ACTIVE | Historical referee decision data and calibration against known patterns |
| Judgment | ACTIVE | Judgment on referee signal weight — well-established patterns vs small sample claims |
| Attention | ACTIVE | Elevated attention when a high-profile or unusual referee is assigned |
| Communication | ACTIVE | Referee signal output with historical pattern data and modifier value |
| Verification | ACTIVE | Referee assignment from official competition source — not media speculation |
| Learning | ACTIVE | Referee pattern calibration from accumulated decision and outcome data |
| Integration | ACTIVE | Integrates with core officiating intelligence and match conditions |
| Calibration | ACTIVE | Referee modifiers calibrated against historical pattern-to-outcome data |
| Adaptation | ACTIVE | Referee profiles updated as decision patterns evolve over career |
| Ethics | ACTIVE | Referee patterns are statistical observations — not allegations of misconduct |
| Transparency | ACTIVE | Referee pattern sample size and historical basis explicit in output |


---

*SportMind v3.97.24 · MIT License · sportmind.dev*
*Enduring framework — applies to all sports, all future matches*
