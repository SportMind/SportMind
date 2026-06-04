---
name: referee-pool-intelligence
description: >
  Competition-specific referee pool frameworks extending core/referee-intelligence.md.
  Covers how referee pools differ structurally by competition — UCL, Premier League,
  La Liga, Ligue 1, Bundesliga — with confidence weights by competition tier and
  key pool characteristics agents must account for.
---

# Referee Pool Intelligence

**How referee pools differ by competition — structural differences beyond individual tendencies.**
Load alongside `core/referee-intelligence.md` for individual referee profiles.

---

## Why competition pools matter

```
Individual referee tendencies (core/referee-intelligence.md) are necessary but
not sufficient. The pool from which a referee is drawn determines:

  · The threshold at which cards are issued (pool culture)
  · The likelihood of VAR use and overturns
  · The degree to which home advantage affects decisions
  · The confidence weight to apply to individual tendency data

A referee who appears lenient in a domestic pool may appear standard in UCL.
Always assess the pool, then the individual within it.
```

---

## UEFA Champions League referee pool

```
SELECTION CRITERIA:
  UEFA Elite category only — top tier from national associations.
  Nationality rotation: same referee rarely officiates the same club
    twice in a season. Neutral nationality mandatory — neither club's
    national federation represented.

KEY POOL CHARACTERISTICS:
  Advantage play: UCL referees more likely to play advantage than stop play.
  Card threshold: higher than equivalent domestic league matches.
    UCL yellow card rate approximately 12% lower than equivalent domestic.
  VAR: standard across all UCL matches — reduces howlers, increases stoppage time.
  Decision pace: UCL referees given more time to manage the game — less pressure
    to make decisive calls to manage clock.

NATIONALITY BIAS:
  UCL avoids same-country appointment. Genuinely neutral in nationality.
  However: neutral nationality ≠ neutral in playing style preference.
  Assess individual referee tendency within the pool framework.

CONFIDENCE WEIGHT: ×1.00 (full confidence in tendency data)
  UCL produces high volumes of high-quality data for individual profiling.
```

---

## Premier League referee pool

```
POOL SIZE AND STRUCTURE:
  14 Select Group 1 referees rotating across 380 matches per season.
  High familiarity between referees and clubs — tendency data is more
  reliable and consistent than in UCL (same pool, same clubs, all season).
  Oversight: PGMOL (Professional Game Match Officials Limited).

KEY POOL CHARACTERISTICS:
  Interventionist: Premier League referees stop play more readily than UCL officials.
  Card rate: higher than UCL — lower threshold for card issuance.
  VAR: standard since 2019/20 season.
  Home advantage in decisions:
    Statistical analysis confirms approximately 15% more penalties awarded to home teams.
    Crowd noise influence is documented and measurable.

HOME ADVANTAGE NOTE:
  This is a pool-level structural tendency — not individual referee bias.
  Apply: ×1.03 home team advantage modifier specific to penalty/foul decisions.
  This stacks on top of general home field advantage.

CONFIDENCE WEIGHT: ×1.00 (full confidence — high data volume, consistent pool)
```

---

## La Liga referee pool

```
OVERSIGHT: RFEF (Real Federación Española de Fútbol)
  
KEY POOL CHARACTERISTICS:
  Card rate: higher than Premier League — one of the highest in Europe.
  El Clásico protocol: RFEF carefully manages referee selection for
    high-profile derbies — additional scrutiny and selection criteria apply.
  VAR: standard since 2018/19.
  Tendency toward stopping play for technical fouls vs playing advantage.

CONFIDENCE WEIGHT: ×0.95
  Slightly reduced vs PL/UCL — individual tendency data is reliable but pool
  is less extensively profiled in SportMind's calibration base.
```

---

## Bundesliga referee pool

```
OVERSIGHT: DFB (Deutscher Fußball-Bund)

KEY POOL CHARACTERISTICS:
  Fitness: Bundesliga referees among the best-conditioned in Europe.
  Fewer late-match errors — high fitness standards reduce fatigue-related decisions.
  Card rate: below European average — one of the lowest in major leagues.
  VAR: standard since 2017/18 (first major league to implement).
  Consistency: high — well-managed pool with clear standards.

CONFIDENCE WEIGHT: ×1.00 (full confidence — consistent, well-documented pool)
```

---

## Ligue 1 referee pool

```
OVERSIGHT: FFF (Fédération Française de Football)

KEY POOL CHARACTERISTICS:
  UCL appointments: historically fewer than PL, Bundesliga, La Liga referees.
    Lower international profile means less independently validated tendency data.
  Data availability: less external profiling available for individual referees.
  VAR: standard since 2018/19.

CONFIDENCE WEIGHT: ×0.85
  Reduced confidence — less calibration data. Apply this discount to all
  Ligue 1 individual referee tendency signals.
```

---

## Serie A referee pool

```
OVERSIGHT: AIA (Associazione Italiana Arbitri) / FIGC

KEY POOL CHARACTERISTICS:
  Historically complex relationship with clubs — scrutiny is high.
  Card rate: moderate — between PL and Bundesliga.
  VAR: standard since 2017/18 (alongside Bundesliga as early adopters).
  Offside calls: Italian VAR culture is particularly rigorous on offside.

CONFIDENCE WEIGHT: ×0.95
  Slightly reduced — pool dynamics and historical controversy introduce
  additional uncertainty in individual tendency profiling.
```

---

## Competition confidence weights — quick reference

```
WHEN LOADING REFEREE INTELLIGENCE, ADJUST BY COMPETITION:

  UCL:                    ×1.00 — full confidence
  Premier League:         ×1.00 — full confidence
  Bundesliga:             ×1.00 — full confidence
  La Liga:                ×0.95
  Serie A:                ×0.95
  Ligue 1:                ×0.85
  Lower tier domestic:    ×0.75
  International (FIFA):   ×0.90
    (Neutral pool, less regular work together, variable data)
  International (UEFA):   ×0.95
    (Quality standard but smaller sample per referee)

HOW TO APPLY:
  Load core/referee-intelligence.md for individual tendency.
  Multiply individual tendency confidence by competition weight above.
  This produces the adjusted confidence weight for that specific appointment.

  Example: Referee with ×0.85 tendency confidence in individual file,
    appointed to a Ligue 1 match:
    Adjusted confidence: ×0.85 × ×0.85 = ×0.72
    Agent should apply ×0.72 weight to any tendency-based modifier from that referee.
```

---

## Compatibility

**Individual tendencies:**  `core/referee-intelligence.md`
**VAR intelligence:**       `core/core-officiating-intelligence.md`
**Sport domain:**           `sports/football/sport-domain-football.md`
**Venue intelligence:**     `core/venue-intelligence.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Referee pool intelligence: pool composition, assignment patterns, and pool-level signals |
| Reasoning | ACTIVE | Pool-level reasoning chain from pool characteristics to competition-wide modifier |
| Context | ACTIVE | Pool context: competition tier, pool quality, appointment rotation patterns |
| Memory | ACTIVE | Historical referee pool patterns by competition and season |
| Judgment | ACTIVE | Judgment on pool-level signal vs individual referee signal — which is more predictive |
| Attention | ACTIVE | Elevated attention for pool changes (new appointments, retirements, suspensions) |
| Communication | ACTIVE | Pool signal output with pool quality assessment and appointment pattern |
| Verification | ACTIVE | Pool composition verified from official competition/federation sources |
| Learning | ACTIVE | Pool-level pattern learning from historical decision and outcome data |
| Integration | ACTIVE | Integrates with referee intelligence and core officiating intelligence |
| Calibration | EMERGING | Pool-level calibration requires more cross-competition data |
| Adaptation | ACTIVE | Pool intelligence adapts as referees are promoted, demoted, or retired |
| Ethics | ACTIVE | Pool analysis is statistical — no individual misconduct allegations |
| Transparency | ACTIVE | Pool composition source and appointment pattern basis explicit in output |


---

*SportMind v3.97.71 · MIT License · sportmind.dev*
*Always load core/referee-intelligence.md alongside this file.*
*Ligue 1 pool confidence weight ×0.85 — apply to all Ligue 1 referee tendency signals.*
