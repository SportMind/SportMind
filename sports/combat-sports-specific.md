---
name: combat-sports-specific
description: >
  MMA and combat sports extended reasoning framework. Covers weight class
  reasoning, fight style matchup matrix, venue and crowd modifiers,
  $UFC and $PFL token-specific demand reasoning. Extends sport-domain-mma.md.
  All demand-only tokens — no FTP PATH_2 confirmed for any combat sports token.
---

# Combat Sports — Extended Reasoning Framework

**Extends `sports/mma/sport-domain-mma.md`. Load base file first.**

---

## Fan token context

```
ACTIVE COMBAT SPORTS FAN TOKENS:
  $UFC — UFC Fan Token (demand-only)
  $PFL — Professional Fighters League (demand-only)

ALL DEMAND-ONLY:
  No confirmed FTP PATH_2 mechanic for any combat sports token.
  Athlete intelligence → fight outcome probability → demand signal only.
```

---

## Weight class reasoning

```
WEIGHT MISS SIGNAL:
  See: sports/mma/sport-domain-mma.md for the weight miss framework.
  Weight miss = preparation failure signal (most significant pre-fight signal in MMA).

WEIGHT CLASS TRANSITIONS:
  Fighters moving UP a weight class:
    Typical reason: maximal growth; cannot make lower weight any longer
    Signal: reduced speed and explosiveness relative to natural opponents at new weight
    reach_speed_modifier = ×0.96 for first 1-2 fights at new weight class
    
  Fighters moving DOWN a weight class:
    Typical reason: strength relative to opponents; seeking better matchups
    Signal: potentially elevated strength and power at new weight; reduced size
    reach_speed_modifier = ×1.03 (relatively larger vs opponents)
    endurance_modifier = ×1.05 (natural frame for this weight)
    
  FIRST FIGHT AT NEW WEIGHT CLASS:
    Apply: weight_transition_uncertainty_modifier = ×0.95 (outcome less predictable)
    Agent rule: weight class debut is a high-uncertainty event; widen confidence interval.

CHAMPIONSHIP ROUNDS (rounds 4-5):
  Three-round (non-title, non-main event) fights:
    Grappling advantage amplifies in shorter fights — less time for striker to
    survive and land strikes; grappler applies sustained pressure.
    Apply: grappling_3round_modifier = ×1.05 for confirmed grappling dominant fighters
    
  Five-round championship fights:
    Sustained cardio determines outcome more than any single attribute.
    Striker who can maintain output for 5 rounds vs grappler who tires:
      apply: championship_round_cardio_modifier = ×1.08 for elite cardio fighters
    Grappling: submission threat actually increases in later rounds as opponent tires.
    Apply: late_round_grappling_modifier = ×1.05 for submission specialists in R4-5.
```

---

## Fight style matchup matrix

```
STYLE MATCHUP — DIRECTIONAL SIGNAL FRAMEWORK:

  STRIKER vs GRAPPLER (the primary MMA matchup):
    Pure striker vs pure grappler: grappler_structural_advantage = ×1.05 in most contexts
    Reasoning: MMA gloves reduce knockout power vs boxing; grappler needs one takedown
    Modifier is directional — favour grappler slightly in pure style matchups
    
    EXCEPTIONS where striker wins this modifier:
      Elite knockout power confirmed (multiple early stoppages)
      Striker has excellent takedown defense (>75% recorded)
      Venue and referee known for early standups (see referee-intelligence.md)
      
  SOUTHPAW vs ORTHODOX:
    Southpaw fighters have a documented statistical edge against orthodox opponents.
    Most fighters are orthodox — southpaw stance creates unfamiliar angles.
    southpaw_advantage_modifier = ×1.04 for southpaw fighter vs orthodox opponent
    This does NOT apply if the orthodox fighter has extensive southpaw fight experience
    (check opponent's recent fight history — has opponent fought multiple southpaws?)
    
  REACH ADVANTAGE:
    Significant reach advantage (6 inches / 15cm+ above opponent):
      striking_output_modifier = ×1.03 for the longer-reach fighter
      long_range_striking = elevated; clinch and grappling = reach advantage reduced
    Moderate reach advantage (3-5 inches):
      reach_modifier = ×1.01 (marginal signal only)
    Apply only to stand-up striking output; grappling range is less affected by reach.
    
  WRESTLING vs JIU-JITSU:
    Both are ground-based but different signals:
      Wrestling advantage: takedown control, ground-and-pound, top position
        wrestler_dominance_modifier = ×1.04 in non-submission focused fights
      BJJ advantage: submission from guard, defensive guard retention
        bjj_submission_modifier = ×1.06 in championship rounds (5R fights; opponent tires)
```

---

## Venue and crowd reasoning

```
UFC PPV vs FIGHT NIGHT:
  PPV (Pay-Per-View) events:
    Higher commercial signal weight — more viewers, higher stakes perception
    Championship fights almost exclusively PPV
    Apply: ppv_commercial_weight_modifier = ×1.20 for demand signal calculations
      (PPV fight outcomes carry 20% more demand weight than Fight Night equivalents)
    
  FIGHT NIGHT (ESPN+, fight-night only):
    Standard commercial weight — solid but lower profile than PPV
    Apply: standard demand weight (×1.00 baseline)

HOME COUNTRY FIGHTER ADVANTAGE:
  Fighter competing in their home country (not just home city):
    crowd_support_modifier = ×1.05
    Mechanism: crowd creates psychological pressure on opponent;
      referee may be slightly more conservative on stoppages (protecting home fighter);
      fighter feeds off energy
    Note: does not apply if fight is in a neutral country, only home country.

ARENA CAPACITY AND ATMOSPHERE:
  MMA crowd effect is lower than most team sports but not negligible.
  Typical MMA crowd: ×1.03 home country advantage (relatively small vs rugby ×1.12)
  Reason: fighters cannot hear crowd during exchanges; effect is primarily psychological.
```

---

## $UFC token reasoning

```
UFC FAN TOKEN ($UFC) — DEMAND SIGNAL FRAMEWORK:

  EVENT HIERARCHY (demand by event type, highest to lowest):
    1. Title fights (undisputed championship) — maximum demand signal
    2. Interim title fights — elevated demand signal
    3. PPV main events (non-title) — high demand signal
    4. PPV co-main events — moderate-high signal
    5. Fight Night main events — moderate signal
    6. Fight Night prelims — low demand signal
    
  CHAMPION PERFORMANCE EFFECT:
    Dominant champion title defense: demand_premium = +5-10% (confirms dominance narrative)
    Champion upset (title changes hands): demand_spike = +15-25% (new narrative ignites demand)
    Title change is the single highest demand event for combat sports tokens.
    
  DEMAND CALENDAR:
    UFC schedules events year-round. Demand peaks concentrate around:
      International Fight Week (annual Las Vegas summer card): peak demand
      End of year (December): lower event frequency; demand slightly suppressed
      Post-interim title unification fights: demand elevated (narrative clarity)
      
  TOKEN DEMAND — FIGHTER IDENTITY:
    UFC token demand is driven by the UFC brand, not individual fighters.
    Unlike club tokens, no individual fighter "owns" $UFC demand.
    Champion level fighters influence demand collectively — the sport's health matters.
    Apply: ufc_brand_health_modifier based on belt activity and fighter quality,
      not on any single fighter's status.
```

---

## $PFL token reasoning

```
PFL FAN TOKEN ($PFL) — SEASON STRUCTURE SIGNAL:

  PFL UNIQUE STRUCTURE:
    PFL operates with a regular season → playoff system, unlike UFC's event-by-event model.
    This creates a distinct demand trajectory through the year.
    
  SEASON DEMAND TRAJECTORY:
    Regular season matches: standard demand (×1.00)
    Playoff rounds begin: elevated demand (×1.15)
    PFL Championship night: peak demand (×1.35)
    Off-season: reduced demand; token enters low-activity period
    
  REGULAR SEASON STAKES:
    PFL regular season fights determine playoff qualification via points system.
    Late regular season with playoff position at stake: apply stakes_modifier = ×1.08
    
  COMPARISON TO UFC:
    $PFL demand is more seasonally concentrated than $UFC demand.
    PFL Championship night is analogous to a league final — single peak event.
    Apply: pfl_championship_demand_multiplier = ×1.35 vs PFL's standard ×1.00 baseline
```

---

## Compatibility

**Base MMA file:**      `sports/mma/sport-domain-mma.md`
**Referee framework:**  `core/referee-intelligence.md`
**Athlete modifiers:**  `core/core-athlete-modifier-system.md`
**Venue:**              `core/venue-intelligence.md`

---

*SportMind v3.97.27 · MIT License · sportmind.dev*
*All combat sports tokens are demand-only — no PATH_2 mechanic confirmed*
