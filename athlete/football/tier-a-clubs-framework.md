---
name: tier-a-clubs-framework
description: >
  Cross-club athlete intelligence reasoning framework for all Tier A fan token
  football clubs. Governs FTP PATH_2 athlete chain (AFC only), universal
  athlete modifiers, fan token demand athlete links, and position weight
  by club identity. Load before any club-specific file.
---

# Tier A Football Clubs — Cross-Club Athlete Intelligence Framework

**Universal framework governing athlete intelligence across all Tier A fan token clubs.**
Load this file before any club-specific athlete file.

> SportMind Library Rule: enduring reasoning framework. No named players,
> no current status. Applies to all future versions of these clubs.

---

## FTP PATH_2 athlete chain — $AFC only

```
PATH_2 ATHLETE CHAIN — SCOPE:

  ONE CLUB HAS CONFIRMED FTP PATH_2 MECHANICS:
    $AFC — Arsenal FC (see athlete/football/arsenal-afc.md for full chain)
    
  ALL OTHER TIER A CLUBS — DEMAND ONLY:
    $PSG  — Paris Saint-Germain
    $BAR  — FC Barcelona
    $JUV  — Juventus
    $ACM  — AC Milan
    $CITY — Manchester City
    [And all other fan token clubs not confirmed as PATH_2]
    
  THE DISTINCTION MATTERS CRITICALLY:
    $AFC athlete absence → adjusts match outcome probability AND expected supply event
    All other clubs → adjusts match outcome probability AND demand signal ONLY
    Never apply PATH_2 supply chain logic to non-confirmed clubs.
    
  HOW TO CHECK:
    Before any athlete intelligence analysis, confirm:
      Does this club have confirmed FTP PATH_2 mechanics?
      Source: fan-token/ftp-path2.md
    If PATH_2 confirmed: load arsenal-afc.md and propagate through supply chain
    If not confirmed: apply demand-only framework (this file)
```

---

## Universal athlete modifiers

These apply across ALL Tier A clubs regardless of system or league:

```
UNIVERSAL MODIFIERS — APPLY TO ALL TIER A CLUBS:

CAPTAIN ABSENCE:
  Modifier: ×0.97 cohesion modifier
  Rationale: captaincy provides squad cohesion, communication, and psychological
    leadership that cannot be fully replaced by tactical adjustment
  Applies to: ALL clubs regardless of whether captain is a first-choice player
  Duration: applies to every match the captain is absent
  Note: if the vice-captain has captained the team frequently, reduce modifier
    to ×0.99 (captaincy role already partially distributed)

MANAGER ABSENCE OR UNCERTAINTY:
  Modifier: ×0.95 system modifier
  Applies when: manager is:
    (a) absent (health, suspension, other)
    (b) confirmed leaving at season end (lame duck status)
    (c) facing strong public speculation about departure (uncertainty)
  Rationale: manager uncertainty creates squad psychological distraction and
    reduces tactical clarity — this is well-documented in sporting literature
  Duration: applies until manager status is resolved
  UCL context: apply ×0.95 across all competitions including European matches

THREE OR MORE KEY ABSENCES:
  Trigger: three or more first-team starters absent simultaneously
  Action: HOLD_RECOMMENDED = true
  Rationale: compound absences create unpredictable rotation patterns,
    formation changes, and cohesion disruption that make confident directional
    signals unreliable
  Exceptions:
    If the three absences are all in a single position group (e.g. three wingers)
    and the club has clear replacements in that group: reduce to CAUTION (not HOLD)
  Applies to: ALL Tier A clubs
  
INTERNATIONAL BREAK RETURN (first match):
  Modifier: ×0.97 for any player returning from long international duty (10+ days)
  Apply to: players who travelled long-haul for international fixtures
  Duration: first match back only; remove after
  
KEY PLAYER RETURNING FROM INJURY (first 2 matches):
  Modifier: ×0.97 (match 1) and ×0.99 (match 2) — graduated return
  Apply to: any key player returning from injury absence of 3+ weeks
  Do NOT apply to: suspensions (no physical reconditioning needed)
```

---

## Fan token demand — athlete link framework

```
KEY PLAYER SIGNING — DEMAND CURVE:

  ARRIVAL PREMIUM:
    Duration: 2-4 weeks post-announcement (signing, not arrival)
    Magnitude: proportional to global profile of signing
    
  ARRIVAL PREMIUM SCALE:
    Marquee signing (household global name): +20-40% demand spike
    Notable signing (well-known within sport but not globally): +8-15%
    Domestic signing (known within league but not globally): +3-5%
    
  DEMAND DECAY POST-ARRIVAL:
    Week 1-2: peak demand (announcement effect)
    Week 3-4: rapid decay toward new baseline
    Week 5+: settled at new structural baseline (slightly above pre-signing)
    
  PERMANENT BASELINE CHANGE:
    Marquee signing: permanent +5-10% baseline above pre-signing level
    (new global fans attracted and retained beyond the initial excitement)
    Notable signing: permanent +2-4% baseline
    
  AGENT RULE:
    Apply arrival premium for 2-4 weeks then remove.
    New baseline must be explicitly recalibrated after premium decays.

KEY PLAYER DEPARTURE — DEMAND DECAY CURVE:

  DEPARTURE DECAY:
    Duration: 4-8 weeks of active decay post-departure confirmation
    Magnitude: proportional to departed player's profile and system centrality
    
  DEPARTURE DECAY SCALE:
    Generational player (Ballon d'Or tier): -15 to -25% permanent baseline reduction
    Marquee player (regular national team starter, global profile): -8-15%
    Notable player (key squad member, domestic profile): -3-8%
    
  DECAY TIMELINE:
    Week 1-2: initial drop (announcement effect)
    Week 3-4: secondary decay as fans process the absence
    Week 5-8: stabilisation toward new baseline
    Week 8+: new structural baseline established
    
  PERMANENT BASELINE:
    Generational departure: permanent structural reduction (see psg-psg.md post-marquee-departure framework)
    The new baseline may be 15-25% below the player's presence baseline permanently
    
  IMPORTANT:
    If a comparable replacement signs simultaneously, arrival premium offsets departure decay
    Net demand effect = arrival premium + departure decay (can be net positive or negative)

PLAYER PERFORMANCE MILESTONE EFFECTS:

  MILESTONES THAT GENERATE DEMAND SPIKES:
    Club goals record broken: +5-10% demand spike (24-48h duration)
    Club appearance record: +3-7% spike
    Individual award (Ballon d'Or, FIFA Best, etc.): +10-20% spike (1 week duration)
    National team milestone (100 caps, World Cup final): +5-15% spike
    
  DURATION OF SPIKE:
    Performance milestones: 24-72h spike then returns to baseline
    Award milestones: 5-7 day elevated demand then returns
    These are NOT permanent baseline changes — transient spikes only
    
  AGENT RULE:
    Never carry milestone spikes beyond their duration.
    Always return to pre-milestone baseline after spike window.
```

---

## Position weight by club identity

```
POSITION MODIFIER WEIGHTING BY CLUB IDENTITY:

  Modifier weight is not uniform across all positions at all clubs.
  Club identity determines which positions carry the highest individual weight.

  ATTACKING IDENTITY CLUBS (goal-scoring system as primary identity):
    Primary goal threat (striker/forward): ×1.15 individual modifier weight
    Secondary attack (winger, shadow striker): ×1.10
    Midfield: ×1.00 (standard)
    Defence: ×0.90 (below standard — less system-critical for attacking clubs)
    
    Clubs in this category: PSG (typically), Milan (trequartista system variant)

  DEFENSIVE IDENTITY CLUBS (defensive solidity as primary identity):
    Goalkeeper: ×1.15 individual modifier weight
    Centre backs: ×1.10
    Midfield: ×1.00 (standard)
    Attack: ×0.90 (below standard — attack is secondary to defensive function)
    
    Clubs in this category: Juventus historically

  POSSESSION IDENTITY CLUBS (midfield control as system centre):
    Central midfield: ×1.15 individual modifier weight
    Full backs: ×1.10 (integral to possession and width)
    Attack: ×1.05 (important but fed by the midfield system)
    Goalkeeper: ×0.90 (standard — less exposed in possession-dominant system)
    
    Clubs in this category: Barcelona (consistently)

  BALANCED / HIGH-PRESS SYSTEM CLUBS:
    No single position group carries large individual weight premium
    Pressing midfielder: ×1.08 (pressing engine)
    All other positions: ×1.00 to ×1.05
    
    Clubs in this category: Arsenal (pressing system), Manchester City (positional)

  AGENT RULE:
    Before calculating any athlete modifier, identify the club's system identity.
    Apply the appropriate position weight multiplier to individual modifiers.
    System identity can evolve with manager changes — reassess each season.
```

---

## Summary modifier table

```
QUICK REFERENCE — UNIVERSAL MODIFIERS:

  SIGNAL                       MODIFIER       APPLIES TO
  Captain absent               ×0.97          All Tier A clubs
  Manager uncertain/absent     ×0.95          All Tier A clubs
  3+ key absences              HOLD           All Tier A clubs
  International break return   ×0.97 match 1  Long-haul travellers only
  Injury return (wk 1)         ×0.97          3+ week absences only
  Injury return (wk 2)         ×0.99          3+ week absences only
  
  Marquee signing (weeks 1-4)  +20-40% spike  Demand only
  Notable signing (weeks 1-4)  +8-15% spike   Demand only
  Departure (weeks 1-8 decay)  -8-25%         Demand only
  Milestone (24-72h)           +3-20% spike   Demand only — transient
  
  PATH_2 chain                 Apply fully    $AFC ONLY
  PATH_2 chain                 DO NOT APPLY   All other clubs
```

---

## Compatibility

**Club files:**       `athlete/football/arsenal-afc.md`
                      `athlete/football/psg-psg.md`
                      `athlete/football/barcelona-bar.md`
                      `athlete/football/juventus-juv.md`
                      `athlete/football/acmilan-acm.md`
                      `athlete/football/mancity-city.md`
**Base athlete:**     `athlete/football/athlete-intel-football.md`
**FTP mechanics:**    `fan-token/ftp-path2.md`
**Core modifier:**    `core/core-athlete-modifier-system.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Tier A football clubs framework: cross-club APS baseline structure for top-tier clubs |
| Reasoning | ACTIVE | Tier A framework defines the reasoning standard for applying APS across top football clubs |
| Context | ACTIVE | Tier A context: UCL participation, financial resources, squad depth — all above standard threshold |
| Memory | ACTIVE | Tier A baseline APS values for comparable club profiles |
| Judgment | ACTIVE | Judgment framework for Tier A clubs: higher bar for signal materiality vs lower-tier clubs |
| Attention | ACTIVE | Tier A attention standard: fixture congestion and European competition signals are primary |
| Communication | ACTIVE | Tier A framework defines output format consistency across all Tier A club files |
| Verification | ACTIVE | Tier A claims require multi-source verification — club complexity warrants higher standard |
| Learning | ACTIVE | Tier A framework updated as calibration data accumulates across top clubs |
| Integration | ACTIVE | Integrates with all individual club files in athlete/football/ directory |
| Calibration | ACTIVE | Tier A APS baseline values calibrated from historical top-club outcome data |
| Adaptation | ACTIVE | Tier A framework adapts as club profiles and UCL participation change |
| Ethics | NOT APPLICABLE | Tier A framework is analytical — no ethical dimension |
| Transparency | ACTIVE | Tier A classification criteria and APS baseline values explicit in framework |


---

*SportMind v3.97.26 · MIT License · sportmind.dev*
*Load this file before any Tier A club-specific athlete file*
