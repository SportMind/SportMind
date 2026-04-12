---
name: athlete-motivation-intelligence
description: >
  Unified framework for athlete and team motivation as a signal modifier.
  Consolidates motivation signals scattered across the library — contract
  year, career milestones, relegation/promotion, revenge fixtures, career
  stage, financial pressure, personal narrative context — into a single
  composable framework with a Motivation Index (MI) score and modifier
  range (0.88–1.18). Distinct from form (what an athlete is doing) and
  availability (whether they can play) — motivation addresses WHY effort
  and focus are elevated or depressed beyond what performance metrics show.
  Load when: a narrative, career, contractual, or competitive context
  exists that standard form analysis would miss. Applies to all sports.
  The highest motivation modifiers in the library (×1.15+) come from
  desperation scenarios — do not apply multiple desperation modifiers
  simultaneously; use the highest single modifier only.
---

# Athlete Motivation Intelligence — SportMind

**Why effort and focus deviate from statistical expectation —
and how to quantify it.**

Form tells you what an athlete has been doing. Availability tells you if they
can play. Motivation tells you how hard they are trying and why that might
differ from baseline right now.

Most pre-match models treat motivation as background noise or handle it
via indirect proxies (recent form, fixture importance). This skill makes
motivation explicit — a structured modifier that agents can apply with
confidence, trace to a verifiable source, and update as circumstances change.

---

## The Motivation Index (MI)

```
MI = base_motivation × highest_active_driver × career_stage_factor

OUTPUT: MI score 0.70–1.30 (maps to modifier below)
RULE: Never stack multiple desperation modifiers. When two apply,
      use the higher value only. Accumulation produces unrealistic signals.

MI MODIFIER SCALE:
  MI ≥ 1.25:  × 1.18  ELITE MOTIVATION   — career-defining context, maximum effort
  MI 1.15–1.24: × 1.12  HIGH MOTIVATION  — clear elevated driver, sustained
  MI 1.05–1.14: × 1.06  ELEVATED          — positive context, measurable uplift
  MI 0.95–1.04: × 1.00  BASELINE          — no special motivation context
  MI 0.85–0.94: × 0.96  REDUCED           — mild demotivation context
  MI 0.75–0.84: × 0.92  LOW               — contract uncertainty, personal issues
  MI < 0.75:    × 0.88  VERY LOW          — unresolved conflict, disengagement
```

---

## Driver Category 1 — Contract and financial motivation

```
These are the most reliably predictive motivation drivers because they
link directly to long-term personal financial outcomes.

CONTRACT YEAR (athlete in final year of contract):
  Why it matters: Elite athletes historically outperform expectations in
  contract years — the next deal is the largest of their career. Every
  game is an audition.
  
  Evidence base:
    NBA contract year: +8–12% performance above expected (documented in
    core library: athlete/nba/athlete-intel-nba.md)
    Football: 11% higher tackle rate, 9% higher sprint distance in studies
    MMA: no formal study — but fight camp quality and public statements
    provide proxy

  MI driver: +0.15 (applying × 1.12 MI modifier)
  
  Strongest when:
    - Player aged 24–30 (peak years, maximum deal value at stake)
    - Player quality is borderline for next-tier club (fighting for a step up)
    - Wage dispute with current club on record
    - Agent publicly "testing the market"
  
  Weakest when:
    - Veteran with legacy contract (next deal is likely their last anyway)
    - Player has already verbally agreed extension (not yet signed)
    - Player has sufficient financial security to prioritise fitness

RELEASE CLAUSE TRIGGER PROXIMITY:
  A release clause that is close to being triggered creates dual motivation:
    The club wants to keep the player's value below the clause threshold
    The player may want to trigger it to force a move
  
  MI driver: +0.10 to +0.20 depending on player intent
  Agent rule: Check Transfermarkt for release clause existence and proximity.
  
RELEGATION RELEASE CLAUSE:
  Common in Premier League promoted clubs. A player with a relegation clause
  approaching is motivated to prevent relegation (clause protects their exit).
  ALSO: their club's other players know some colleagues will leave — potential
  squad cohesion issue (see core/squad-cohesion-intelligence.md).
  
  MI driver for individual player: +0.12 (self-preservation motivation)
  
UNDERPAID RELATIVE TO PEERS:
  Publicly known wage disputes or confirmed underpayment create a chip-on-
  shoulder motivation pattern — particularly strong in individual sports and
  among players whose agents have publicly criticised their current deal.
  
  MI driver: +0.08 to +0.15 (higher when public dispute is active)
  Sources: L'Equipe (France), Calcio e Finanza (Italy) — wages often public
```

---

## Driver Category 2 — Career milestone motivation

```
Milestone proximity is the best-documented motivation driver in sports.
Athletes approaching records show elevated performance in the window
immediately before and at the milestone.

EVIDENCE BASE:
  Football: Strikers approaching 100/200 league goals show elevated
  finishing rates in the proximity window (FBref historical analysis)
  NBA: players approaching 20,000 points show peak efficiency in milestone
  window; historic context of the milestone amplifies the effect
  Cricket: Test batsmen approaching 10,000 runs show elevated focus in
  sessions after the milestone becomes newsworthy (ESPNcricinfo)
  Snooker: players approaching 1,000 century breaks show elevated shot
  selection quality (World Snooker stats)

MILESTONE TYPES AND PROXIMITY WINDOWS:

  CAREER RECORD (all-time landmark):
    Examples: 100 international goals, surpassing a legend's record
    Window: Final 3 fixtures approaching the milestone
    Peak: The fixture immediately preceding the milestone (final hurdle)
    MI driver: +0.20 → × 1.18 modifier in peak window
    
  SEASONAL RECORD (season-level milestone):
    Examples: 30 league goals in a season, highest ever batting average
    Window: Final 5 fixtures of the season when approaching
    Peak: Last 2 fixtures in chase window
    MI driver: +0.15 → × 1.12 modifier

  CLUB RECORD (club-specific, not all-time):
    Examples: Club's all-time appearance record, most goals for the club
    Window: Final 2 fixtures approaching
    MI driver: +0.10 → × 1.06 modifier
    Less powerful than career record — smaller personal narrative

  NICE ROUND NUMBER (100 goals, 500 wickets, 1000 points):
    These carry cultural weight even when not formally a "record"
    MI driver: +0.08 → × 1.04 modifier
    
  MILESTONE FATIGUE — the post-milestone dip:
    In the 1–3 fixtures AFTER a milestone is reached, performance
    sometimes dips. The goal has been achieved; subconscious focus shifts.
    Not universal, but documented. Apply: × 0.97 for 1–2 fixtures post-major-milestone.
    
VERIFIABLE SIGNAL:
  Most milestone proximity narratives are publicly covered by:
  - The Athletic, ESPN, BBC Sport (1–2 weeks before the milestone fixture)
  - Manager press conference: "He's close to history" = confirmed awareness
  When the manager references the milestone publicly, the motivation signal
  is confirmed and at maximum weight.
```

---

## Driver Category 3 — Competitive context motivation

```
These drivers derive from the competitive situation — where the team or
athlete stands in a competition and what is at stake.

ELIMINATION / MUST-WIN:
  Single-elimination format or team/individual must win to survive.
  MI driver: +0.15 → × 1.12 modifier
  Strong when: player has clear agency (can personally affect the result)
  Weaker when: player is peripheral (substitute, less influential)
  
  DESPERATION CEILING:
  When elimination is combined with trailing in a series or match:
    0-3 in a best-of-7 series: maximum desperation × 1.15
    This is one of the highest motivation modifiers in the library.
    (Source: athlete/nba/athlete-intel-nba.md)
  
RELEGATION BATTLE:
  Final 6–10 matches of a season with team in or near the relegation zone.
  MI driver: +0.12 for players who would be seriously career-affected by relegation
  Weakest for: players with release clauses (they will leave anyway)
  Strongest for: club legends, players under long contracts at that club
  
  RELEGATION CONFIRMATION (negative desperation):
  When relegation is mathematically confirmed, motivation collapses for
  some players — especially those with relegation clauses or seeking moves.
  Apply × 0.90 for the final fixtures after relegation is confirmed.
  Exception: Players competing for Golden Boot, Golden Glove, personal records
  may maintain motivation despite team outcome.

TITLE DECIDER / FINAL MATCH:
  Championship decided in a single match or final game of season.
  MI driver: +0.12 for team players; +0.18 for acknowledged leaders
  
  FINAL / TROPHY MATCH:
  Cup finals, playoff deciders, promotion/relegation play-offs.
  MI driver: +0.10 standard; +0.18 if player is appearing in their first final
  Venue factor: First appearance at iconic venue amplifies driver
  (Wembley, Madison Square Garden, Melbourne Cricket Ground, The Masters)
  
RANKING PRESSURE (individual sports):
  A player at a ranking boundary (16 in snooker, top-100 in tennis, PGA tour
  card threshold) is fighting to maintain or improve their professional status.
  MI driver: +0.10 to +0.15 depending on proximity to the boundary
  (Already documented in: athlete/snooker/athlete-intel-snooker.md,
  athlete/darts/athlete-intel-darts.md — this framework unifies them)

HOME CROWD:
  The home crowd creates a motivational uplift separate from tactical home
  advantage. Crowd response to effort rather than just results.
  MI driver: +0.06 standard; +0.10 for a player returning to a former club
  as home team; +0.12 if player has a celebrated relationship with the crowd
  
  AGAINST THE CROWD (away player motivation from hostile crowd):
  Some players perform better under hostility — the crowd amplifies their drive.
  Identifier: player known to "feed off" hostile crowds (press conference history,
  historical stats in hostile away environments)
  MI driver: +0.08 for confirmed crowd-responders
```

---

## Driver Category 4 — Personal narrative motivation

```
These drivers are harder to quantify but verifiable through journalism
and press conference signals. Do not apply without a Tier 1/2 source.

REVENGE FIXTURE (already in core/core-narrative-momentum.md):
  Player facing former club, coach who sold them, or opponent who disrespected them.
  MI driver: +0.10 to +0.15 (retain core-narrative-momentum.md values)
  This file documents the underlying mechanism; that file quantifies it.

FAREWELL MATCH:
  Player's final match at a club, final international appearance, or retirement.
  MI driver: +0.12 in farewell season overall; +0.20 in confirmed final match
  Note: Farewell narrative amplifies FAN token engagement signal beyond player's
  own performance (see core/star-departure-intelligence.md — tribute arc)

RETURN FROM MAJOR INJURY:
  First match back after significant injury absence (6+ months).
  MI driver: +0.08 (desire to prove fitness, relief at return)
  Caution: Pair with injury recurrence risk modifier — elevated motivation
  + recent injury history = higher performance variance, not guaranteed upside

PERSONAL LOSS OR DIFFICULT CIRCUMSTANCES:
  Documented bereavement or personal difficulty that has received media coverage.
  Direction of effect: genuinely uncertain — some athletes perform at peak
  (channelling grief), others underperform.
  Rule: DO NOT apply a directional modifier for personal loss/difficulty.
  Instead: flag the UNCERTAINTY (increase variance in signal, reduce confidence).
  Apply: confidence score reduction × 0.85, wider signal range, recommend WAIT
  or reduced position size.

DEBUT / CAREER FIRST:
  First match at this level, first international cap, first major final.
  Direction: uncertain — debut nerves vs debut adrenaline are genuinely balanced.
  Rule: Same as personal loss — flag uncertainty rather than apply direction.
  Exception: Player with documented debut excellence record (some players
  specifically perform better in debut contexts — check historical record).
  If documented debut excellence: +0.08 modifier (verifiable pattern)
  Otherwise: flag variance, reduce confidence score.

INTERNATIONAL BREAK RETURN:
  Player returning from international duty — carried across to club sport.
  If international went well (goals, team won): small motivational carryover +0.04
  If international went badly (team eliminated, individual poor form): risk of
  psychological overhang — no modifier but note in brief.
```

---

## Driver Category 5 — Career stage motivation

```
Career stage is a background factor that modifies how other drivers apply.
It does not generate a modifier on its own — it scales other drivers.

EMERGING (ages 17–22, early career):
  Motivation for: establishing reputation, proving worth, earning first major deal
  Scale other drivers: × 1.15 amplifier on contract and milestone drivers
  Watch for: debut nerves; inconsistency is normal and part of the baseline

PEAK (ages 23–29):
  Standard baseline — career stage factor: × 1.00
  Contract year effect is strongest in this window (peak deal value at stake)

ESTABLISHED ELITE (ages 30–33):
  Legacy motivation begins to dominate over financial motivation
  Title-chasing and farewell narratives become relevant
  Scale contract drivers: × 0.85 (next contract less career-defining)
  Scale legacy/farewell drivers: × 1.15

VETERAN (ages 34+):
  Survival and legacy dominate; financial motivation largely settled
  Performance variance increases — elevated on good days, lower floor on bad
  High motivation signals still apply for: farewell matches, title chases,
  records within reach, playing for current contract extension (one more year)
  Scale contract drivers: × 0.70
  Scale legacy/farewell drivers: × 1.30 (these matter most now)

DECLINING (any age, confirmed decline phase):
  Motivation can be elevated (fighting the decline) or depressed (giving up)
  Identifier: publicly acknowledged by manager, journalist, or statistically clear
  If fighting — MI driver from defiance: +0.08
  If passive decline — MI driver: -0.15
  Agent rule: Do not assume direction. Check press conference tone and
  recent statistical trend before applying either.
```

---

## Motivation output schema

```json
{
  "motivation_brief": {
    "athlete":      "Player name",
    "sport":        "football",
    "match":        "Arsenal vs PSG",
    "assessed_at":  "2026-04-12T00:00:00Z"
  },

  "active_drivers": [
    {
      "category":       "contract",
      "driver":         "contract_year",
      "strength":       "HIGH",
      "mi_contribution": 0.15,
      "source":         "Contract confirmed expiring June 2027 — Transfermarkt",
      "note":           "Age 26, prime deal window — maximum career financial stake"
    }
  ],

  "career_stage":         "peak",
  "career_stage_factor":  1.00,

  "MI_score":         1.15,
  "MI_modifier":      1.12,
  "modifier_label":   "HIGH MOTIVATION",

  "plain_english": "Bukayo Saka is in the final year of his contract and playing the biggest games of his career so far. He has more reason than usual to perform tonight — not just for the club, but for himself.",

  "confidence":        0.80,
  "source_tier":       "Tier 2 (verified journalism)",

  "skill_connections": [
    "core/core-narrative-momentum.md (revenge, milestone drivers)",
    "core/athlete-financial-intelligence.md (contract detail)",
    "core/squad-cohesion-intelligence.md (team motivation context)",
    "core/star-departure-intelligence.md (farewell arc signal)"
  ]
}
```

---

## Integration with SportMind patterns

```
PATTERN 2 (Pre-Match Chain):
  Apply MI modifier alongside athlete form and availability.
  MI modifier is ADDITIONAL to the LQI and composite_squad_modifier.
  Do not double-count: if narrative momentum already includes a revenge
  modifier, do not re-apply from Category 4 above.

PATTERN 6 (Athlete Commercial Tracker):
  Career milestones approaching = CDI-equivalent positive commercial event.
  High MI context = elevated social engagement expected.

PROMPT 21/22 (Fan-facing and build-up briefs):
  Always include the plain_english motivation note if MI ≥ 1.10.
  Example: "This is a contract year for [player] — he has extra reason to
  perform tonight."

ANTI-PATTERN:
  Never apply × 1.15+ modifier without a verifiable Tier 1/2 source.
  Motivation is the easiest modifier to over-apply. The discipline is:
  can you cite a specific verifiable reason? If not, baseline applies.
```

---

*SportMind v3.56 · MIT License · sportmind.dev*
*See also: core/core-narrative-momentum.md · core/athlete-financial-intelligence.md*
*core/squad-cohesion-intelligence.md · core/star-departure-intelligence.md*
*core/manager-intelligence.md · core/lineup-quality-index.md*
