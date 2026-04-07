# Kabaddi (Pro Kabaddi League) — Athlete Intelligence

Player-level intelligence for kabaddi predictions and fan token signals.
Produces an `athlete_modifier` (0.55–1.25) that adjusts the base signal score.

**Applicable tokens / markets:** PKL prediction markets; Indian sports DFS platforms

---

## Overview

Kabaddi is the most individual-player-driven team sport in the library. A star raider (raid success rate >60%) can carry a match outcome. The All Out event is the key tactical catalyst — monitor raid/tackle balance.

---

## Commands

| Command | Description |
|---|---|
| `get_availability` | Player/athlete availability status |
| `get_form_score` | Recent performance score (last 5 events) |
| `get_sport_modifier` | Sport-specific key variable modifier |
| `get_athlete_signal_modifier` | Composite modifier — runs all sub-skills |

---

## Command reference

### `get_athlete_signal_modifier`

Master composite modifier for Kabaddi (Pro Kabaddi League). Combines availability, form, and sport-specific variables.

**Parameters:**
- `player_id` (required) — athlete identifier  
- `match_id` (optional) — specific event; defaults to next scheduled

**Returns:**
```json
{
  "athlete": "string",
  "availability": 1.0,
  "form_score": 0.85,
  "sport_specific_modifier": 1.05,
  "composite_modifier": 1.05,
  "adjusted_direction": "POSITIVE",
  "key_risks": ["string"],
  "modifier_reason": "Raider rating and tackle success rate is the primary driver"
}
```

---

## Modifier reference

| Condition | Modifier |
|---|---|
| Peak fitness, top recent form, ideal conditions | ×1.20 |
| Fit, good form | ×1.10 |
| Neutral | ×1.00 |
| Minor fitness concern | ×0.90 |
| Significant fitness doubt | ×0.80 |
| Key athlete confirmed unavailable | ×0.70 |

---

## Integration example

### Kabaddi (Pro Kabaddi League) pre-event workflow

```
# Step 1: Load domain context
Load sports/kabaddi/sport-domain-kabaddi.md

# Step 2: Athlete checks
get_availability athlete=[ATHLETE_ID]
get_form_score athlete=[ATHLETE_ID]
get_sport_modifier athlete=[ATHLETE_ID]

# Step 3: Get composite modifier
get_athlete_signal_modifier athlete=[ATHLETE_ID] event=[EVENT_ID]

# Step 4: Decision logic
# composite_modifier >= 1.10 AND signal >= 65 → ENTER
# composite_modifier < 1.00 OR injury_warning → WAIT or ABSTAIN
```

---

## Compatibility

**L1 domain:** `sports/kabaddi/sport-domain-kabaddi.md`
**L4 market:** `market/market-kabaddi.md`
**Core:** `core/core-athlete-modifier-system.md`


---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_raider_form` | Raid success rate, super raids, tackle avoidance | Yes |
| `get_defender_profile` | Tackle success rate, super tackles, zone defence | Yes |
| `get_all_out_tendency` | Team's historical all-out rate — tactical signal | Yes |
| `get_do_or_die_record` | Performance in do-or-die raids — pressure signal | Yes |
| `get_fatigue_profile` | PKL schedule density; back-to-back matches | Yes |
| `get_athlete_signal_modifier` | Composite kabaddi modifier | Yes |

---

## The raider primacy model

```
KABADDI IS THE MOST INDIVIDUAL-SPORT TEAM SPORT IN THE LIBRARY:

A star raider with a raid success rate above 60% can carry a team outcome.
Unlike any other team sport, one player takes the field alone to score,
creating the highest individual-to-team impact ratio in team sports.

RAID SUCCESS RATE:
  > 65%: elite raider — modifier × 1.25 (can win matches single-handedly)
  58-65%: very good — × 1.12
  50-58%: above average — × 1.05
  43-50%: average — × 1.00
  < 43%: struggle signal — × 0.90

SUPER RAID (3+ points in single raid):
  Rare but match-changing; indicates exceptional raiding form
  3+ super raids last 5 matches: × 1.10 additional modifier

DO-OR-DIE RAID RECORD:
  When a team's raider is forced to raid (2+ consecutive failed raids trigger this)
  Elite raider under do-or-die pressure: × 1.08 (mental strength signal)
  Average raider under do-or-die: × 0.92 (pressure disadvantage)
```

## Defender and All Out intelligence

```
ALL OUT — THE KEY TACTICAL EVENT IN KABADDI:

An All Out occurs when all opposition players are eliminated from the mat.
The team causing an All Out scores bonus points and revives eliminated players.
All Out patterns define match outcomes more than any other tactical signal.

ALL OUT TENDENCY:
  Team that forces All Outs at > 2.5 per match: defensive dominance signal × 1.10
  Team that allows All Outs frequently (> 2 allowed per match): × 0.90

DEFENDER PROFILES:
  Tackle success rate > 55%: elite defender — × 1.08
  Ankle hold specialist (most common super tackle method): premium for ankle-hold accuracy
  Corner position defenders vs left/right edge: different skill profiles
  
  SUPER TACKLE (tackle when 3 or fewer defenders on mat):
    Elite super-tackle rate > 40%: × 1.12 (controls match in critical moments)

MATCH MOMENTUM SIGNAL:
  First All Out in a match historically favours the forcing team by 72%
  Apply: first_all_out_leader flag during live match analysis
```

## PKL (Pro Kabaddi League) market intelligence

```
PRO KABADDI LEAGUE — WORLD'S MOST WATCHED KABADDI COMPETITION:

PKL Season: October-March (Indian domestic sporting calendar)
12 franchises; each plays 22 matches in group stage
Playoffs: Eliminators + Final

PKL FRANCHISE SIGNAL:
  Patna Pirates: 3× champions; historically dominant; high ATM
  U Mumba: Mumbai fan base; commercial crossover with cricket
  
ATM TIERS:
  Tier 1 — PKL icons (Pardeep Narwal, Pawan Sehrawat tier):
    ATM 0.60-0.70; massive following in Hindi-speaking belt
    Social: 5M+ combined; appearing on national TV advertising
    
  Tier 2 — Regular PKL starters with national team caps:
    ATM 0.40-0.55
    
  INDIA DOMESTIC MARKET NOTES:
    Kabaddi's addressable token market: Bihar, Haryana, Punjab, UP
    These are the highest-engagement kabaddi demographics
    When PKL tokens launch (architecture ready): regional activation × 1.25
```

## Integration: Full kabaddi pre-match workflow

```
Step 1: Load domain context
  Load sports/kabaddi/sport-domain-kabaddi.md

Step 2: Star raider check FIRST
  get_raider_form — raid success rate and do-or-die record
  > 60% success: positive; < 43%: significant concern

Step 3: All Out tendency
  get_all_out_tendency — who forces more All Outs?
  All Out forcing team wins 72% — strong signal

Step 4: Composite modifier
  get_athlete_signal_modifier
```

## Command reference

### `get_athlete_signal_modifier`
```json
{
  "player": "string",
  "role": "raider|defender|all-rounder",
  "raid_success_modifier": 1.12,
  "all_out_tendency_modifier": 1.10,
  "do_or_die_modifier": 1.05,
  "composite_modifier": 1.15,
  "adjusted_direction": "POSITIVE",
  "key_risks": ["High opponent tackle success rate at corners"],
  "modifier_reason": "Elite raider (62% success) + team forces 2.8 all-outs/match"
}
```

## Modifier reference

| Modifier | Source | Range |
|---|---|---|
| `raid_success_modifier` | `get_raider_form` | 0.90–1.25 |
| `all_out_modifier` | `get_all_out_tendency` | 0.90–1.10 |
| `pressure_modifier` | `get_do_or_die_record` | 0.92–1.08 |
| `fatigue_modifier` | `get_fatigue_profile` | 0.92–1.00 |
| `composite_modifier` | Product of all applicable | 0.80–1.30 |


*MIT License · SportMind · sportmind.dev*
