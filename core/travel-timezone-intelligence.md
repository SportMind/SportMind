---
name: travel-timezone-intelligence
description: >
  Intelligence framework for travel fatigue and timezone disruption as
  pre-match performance signal variables. Covers jet lag (eastward worse
  than westward, circadian disruption quantified), long-haul travel tiers,
  timezone crossing impact by magnitude (1–3 zones, 4–6, 7+), recovery
  timelines, and sport-specific travel patterns. Produces a Travel Impact
  Score (TIS: 0.80–1.00, lower = more impaired) applied to the athlete
  modifier chain. Cross-sport: football (Champions League away legs,
  pre-season tours, international breaks), basketball (NBA cross-country
  trips, FIBA tournaments), cricket (Ashes tours, ICC tours), rugby
  (Lions tours, Rugby World Cup travel), MMA (fighter relocation camps),
  F1 (flyaway races). Distinct from core/core-fixture-congestion.md which
  models performance degradation from too many matches — this models
  degradation from the journey itself, independent of match frequency.
  Load when: team has crossed 4+ timezones in last 48h, team played
  in antipodal timezone within last 5 days, or international break
  returnees have long-haul origin.
---

# Travel and Timezone Intelligence — SportMind

**Getting there is half the problem. A team that flew 17 hours and crossed
11 timezones to play a match is not the same team as one that took a 45-minute
bus from Manchester to Liverpool.**

The fixture congestion framework covers too many matches in too little time.
This skill covers a different failure mode: one match, at the wrong time, after
the wrong journey. The physiological and psychological impact of long-haul travel
and timezone disruption is well-documented in sports science and is consistently
underweighted by standard pre-match models.

---

## The Travel Impact Score (TIS)

```
TIS = 1.00 − travel_penalty

WHERE:
  travel_penalty = timezone_penalty + haul_penalty + recovery_penalty − adaptation_bonus

TIS RANGE: 0.80 → 1.00
  1.00: No meaningful travel impact (domestic, same timezone, adequate rest)
  0.95: Minor impact (1–3 timezone crossing, adequate rest)
  0.90: Moderate impact (4–6 timezone crossing, or long-haul within 48h)
  0.85: Significant impact (7+ timezone crossing, or long-haul within 24h)
  0.80: Severe impact (antipodal travel, first match within 24h of arrival)

APPLICATION:
  athlete_modifier_adjusted = athlete_modifier × TIS
  Apply per-player if individual travel history known
  Apply team-wide if squad travelled together (most common case)

WHEN TIS = 1.00 (do not apply penalty):
  Both teams have equivalent travel burden → cancel out, apply to neither
  Only apply TIS advantage when ONE team has significantly more travel burden
  Example: Arsenal hosting Atletico (both at Emirates) → no TIS differential
  Example: Arsenal travelling to Club Brugge after Asian tour → apply TIS to Arsenal
```

---

## Timezone crossing penalty

```
DIRECTIONAL RULE — THE EASTWARD PENALTY:
  Eastward travel disrupts the circadian rhythm more severely than westward.
  Going east: body clock runs "short" — feels like staying up past bedtime
  Going west: body clock runs "long" — feels like extended day
  
  Practical impact:
    London → Dubai (east, +3h):  harder to adapt than Dubai → London
    London → New York (west, -5h): easier to adapt than New York → London
    London → Sydney (east, +10h): severe; Sydney → London slightly less so

PENALTY TABLE (applied to TIS):

  MINOR (1–3 timezone zones):
    Eastward:  −0.01 (negligible with normal preparation)
    Westward:  −0.01 (negligible)
    Example: London → Paris (same), London → Istanbul (+2)

  MODERATE (4–6 zones):
    Eastward:  −0.05
    Westward:  −0.03
    Example: London → Dubai (+3, classified moderate for performance)
    Example: London → New York (−5, westward moderate)
    Example: London → Moscow (+3, cold + timezone compound)

  SIGNIFICANT (7–9 zones):
    Eastward:  −0.10
    Westward:  −0.07
    Example: London → Bangkok (+7)
    Example: London → Los Angeles (−8, westward significant)

  SEVERE (10+ zones, antipodal):
    Eastward:  −0.15
    Westward:  −0.12
    Example: London → Sydney (+10/11)
    Example: London → Tokyo (+9)
    Example: Madrid → Seoul (+9)

RECOVERY TIMELINE:
  General rule: 1 day of adaptation per timezone crossed
  Eastward: 1.5 days per zone (harder)
  Westward: 1 day per zone
  
  If team arrived 7+ days before the match: penalty → 0 (full adaptation)
  If team arrived 4–6 days before: reduce penalty by 50%
  If team arrived 2–3 days before: reduce penalty by 25%
  If team arrived < 24h before: full penalty applies
```

---

## Long-haul travel penalty (independent of timezone)

```
The physical fatigue of long-duration travel exists separately from timezone
disruption. A 4-hour flight within a timezone is still fatiguing.

FLIGHT DURATION TIERS:

  SHORT HAUL (< 3 hours):
    Penalty: −0.01 (minimal; standard European club travel)
    Example: Manchester → Munich, Madrid → Lisbon, New York → Chicago

  MEDIUM HAUL (3–7 hours):
    Penalty: −0.02
    Example: London → Dubai, Madrid → Doha, Los Angeles → Miami
    Note: Compound with moderate timezone crossing if applicable

  LONG HAUL (7–11 hours):
    Penalty: −0.04
    Example: London → Singapore, Madrid → São Paulo, Munich → Toronto
    Recovery: Minimum 48h rest recommended before competitive performance

  ULTRA LONG HAUL (11+ hours):
    Penalty: −0.06
    Example: London → Sydney, Madrid → Tokyo, New York → Dubai
    Recovery: Minimum 72h recommended; most clubs schedule 5–7 days
    Agent flag: LONG_HAUL_TRAVEL_RISK if first match within 48h of arrival

COMPOUND RULE:
  Apply BOTH timezone penalty AND haul penalty when applicable
  Cap combined penalty at −0.20 (TIS floor: 0.80)
  
  Example: Arsenal fly London → Tokyo (ultra long haul −0.06, eastward 9 zones −0.10)
  Combined: −0.16 → TIS = 0.84 (if match within 48h of arrival)
```

---

## Recovery penalty

```
TIME SINCE ARRIVAL AT DESTINATION:

  < 24h since arrival (first-night effect, worst stage):
    Modifier: apply full combined penalty
    Note: "First-night effect" — even without jet lag, first night away
    produces measurable sleep quality reduction

  24–48h (acute adjustment phase):
    Modifier: apply 90% of combined penalty

  48–72h (partial adaptation):
    Modifier: apply 60% of combined penalty

  72h–5 days (active adaptation):
    Modifier: apply 30% of combined penalty

  5–7 days (near-full adaptation):
    Modifier: apply 10% of combined penalty

  7+ days (full adaptation):
    Modifier: penalty → 0

PRACTICAL SHORTCUTS:
  Pre-season tour (club in destination for 7+ days):    TIS = 1.00
  Champions League away leg (flew previous day):        TIS = 0.97–0.98
  World Cup (team based in host country for weeks):     TIS = 1.00
  International break (players returning from 4+ TZ):  TIS = 0.92–0.95
  Athletes returning to club from >7 TZ away:           TIS = 0.87–0.90
```

---

## Sport-specific travel patterns

```
FOOTBALL / SOCCER:

  CHAMPIONS LEAGUE AWAY LEGS:
    European away (1–3 TZ, short/medium haul): TIS = 0.98–1.00
    Most UCL away trips: London → Madrid, Munich → Rome
    Meaningful penalty cases:
      Arsenal → Kyiv (Ukraine): medium haul, 2TZ → TIS 0.97
      Any European team → Istanbul: 2–3 TZ → TIS 0.97
      Any team → Baku: 3–4 TZ → TIS 0.94–0.96

  INTERNATIONAL BREAKS — RETURNEE PROBLEM:
    Players returning from South America (5–8 TZ west):     TIS 0.90–0.93
    Players returning from Australia/Asia (8–11 TZ east):   TIS 0.85–0.90
    Players returning from Africa (0–2 TZ, minimal):        TIS 0.98
    Key rule: apply per-player, not team-wide, for returnees
    Flag: INTERNATIONAL_BREAK_RETURNEE if player crossed 5+ TZ

  PRE-SEASON TOURS (if first competitive match soon after):
    US tour (London club): 5 TZ west. If played within 48h → TIS 0.88
    Asia/Australia tour: 8–11 TZ east. If played within 48h → TIS 0.84
    Standard pre-season: team has 7+ days in location → TIS = 1.00


BASKETBALL (NBA):

  WEST COAST ROAD TRIP (3–4 timezone crossings for East teams):
    New York → Los Angeles (3 TZ west, 5.5 hour flight):
    First game of trip: TIS = 0.95
    After 3+ days on West Coast: TIS = 1.00 (adapted)
    
  B2B CROSS-COUNTRY:
    Team plays Monday East Coast, Tuesday West Coast: double penalty
    Haul penalty + short recovery: TIS = 0.90 compound with B2B modifier

  NBA EARLY SLOT GAMES (late arrival previous night):
    1pm games after overnight travel: TIS = 0.93–0.95
    Agent rule: check game notes for "back of B2B + early slot"


CRICKET:

  ASHES / MAJOR TOURS:
    England → Australia: 10 TZ east (ultra severe)
    Typical tour preparation: 7–10 days in Australia before first match
    With standard preparation: TIS = 1.00 by first Test
    If first game within 3 days of arrival: TIS = 0.85–0.88

  IPL FRANCHISES / HOME VENUES:
    Players arriving from Europe for IPL: TIS issue first 3–5 days
    IPL auction buys who travel at short notice: flag ADAPTATION_PENDING

  ICC TOURNAMENTS (centralised venue):
    Teams based in same country throughout: TIS = 1.00 by day 3
    Knockout stage travel between venues: assess case by case


FORMULA 1:

  FLYAWAY RACE CALENDAR (Asian + Americas):
    European teams to Singapore, Japan, USA, Mexico: 7–15 TZ range
    F1 schedule mandates arrival days before practice: standard is 4–5 days
    With standard preparation: TIS impact minimal by race day
    Key risk: compressed back-to-back flyaway weekends
    Example: Singapore GP + Japan GP (same week): compound fatigue
    Apply haul penalty even with adequate TZ adaptation: −0.03

  DRIVER NOTE:
    F1 drivers are highly adapted to travel — career-long conditioning
    Apply 50% of standard penalty for professional F1 grid drivers
    Apply full penalty for rookies (first full F1 season)


MMA / COMBAT SPORTS:

  FIGHTER RELOCATION CAMPS:
    Fighter moves training camp to different country/timezone for preparation
    This is POSITIVE for performance (full adaptation, purpose-built prep)
    If fighter has trained in match timezone for 4+ weeks: TIS bonus +0.02
    
  WEIGHT CLASS TRAVEL:
    Championship fighters at major events typically arrive 1–2 weeks early
    Standard: TIS = 1.00 by fight night
    
  LATE-REPLACEMENT FIGHTERS (short notice, different continent):
    Short-notice fight with <5 days notice and 5+ TZ crossing: TIS = 0.88
    Flag: SHORT_NOTICE_TRAVEL_RISK


RUGBY:

  LIONS TOURS (every 4 years):
    British & Irish Lions to South Africa/Australia/NZ: 8–12 TZ
    First 2 provincial matches of tour: TIS = 0.90–0.92
    By Test series (4–5 weeks in): TIS = 1.00

  RUGBY WORLD CUP:
    Centralised tournament, teams based in host nation
    TIS = 1.00 for all RWC matches after first week
    
  AUTUMN INTERNATIONALS (November):
    Southern hemisphere teams travelling north: 10–13 TZ
    First match of November tour: TIS = 0.88–0.91
    Key: All Blacks first game of Northern tour historically volatile
```

---

## Agent integration rules

```
WHEN TO LOAD THIS SKILL:
  1. Team has crossed 4+ timezones in last 72h
  2. International break returning players from Americas/Asia/Pacific
  3. First match of a pre-season tour (check preparation window)
  4. "Flyaway" F1/MotoGP race weekend
  5. Short-notice replacement in combat sports

WHEN NOT TO LOAD:
  Standard European club football (< 3 TZ, short haul) → haul penalty ≈ 0
  Both teams have equivalent travel burden → TIS cancels out
  Team has been in destination 7+ days → TIS = 1.00

AGENT CALCULATION STEPS:
  1. Identify: where did the team depart from and when did they arrive?
  2. Calculate: timezone zones crossed (count hour difference, note direction)
  3. Apply: timezone penalty (directional) + haul penalty (duration)
  4. Adjust: recovery modifier based on time since arrival
  5. Output: TIS score to athlete modifier chain

DATA SOURCES:
  Team travel confirmed via:
  - Official club pre-match press conference ("we arrived yesterday")
  - Social media (club Instagram/X often posts travel photos with timestamps)
  - Tier 1 journalists covering the club's travel
  - Wikipedia / competition fixture databases (scheduled venue locations)
  Never assume: always verify where team departed from before applying penalty
```

---

## TIS output schema

```json
{
  "travel_brief": {
    "team":          "Arsenal",
    "match":         "Arsenal vs Atletico Madrid",
    "assessed_at":   "2026-04-14T00:00:00Z"
  },

  "travel_context": {
    "departure_city":   "London",
    "destination_city": "Madrid",
    "flight_duration_h": 2.5,
    "timezones_crossed": 1,
    "direction":        "westward",
    "arrival_h_before_match": 24
  },

  "penalties": {
    "timezone_penalty":  0.01,
    "haul_penalty":      0.01,
    "recovery_modifier": 0.90,
    "combined_penalty":  0.018
  },

  "tis_score":  0.98,
  "tis_label":  "MINIMAL IMPACT",

  "note": "Standard European away trip. Madrid is only 1 timezone west of London and a 2.5h flight. Minimal travel impact on performance signal.",

  "flag":  null,

  "sportmind_version": "3.64.0"
}
```

---

*SportMind v3.64 · MIT License · sportmind.dev*
*See also: core/core-fixture-congestion.md (match frequency fatigue)*
*core/contextual-signal-environment.md · core/athlete-motivation-intelligence.md*
*core/perceptual-pressure-intelligence.md · core/pre-match-squad-intelligence.md*
