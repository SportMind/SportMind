# Rugby Union — SportMind Domain Skill

Sport-specific intelligence for rugby union. Covers the international calendar
(Six Nations, Rugby Championship, Rugby World Cup) and major domestic competitions
(Premiership, URC, Top 14, Super Rugby).

---

## Overview

Rugby union is a territory and set piece dominated sport. Unlike football where
individual brilliance can determine outcomes, rugby union outcomes are heavily
influenced by structural factors: set piece dominance (scrum, lineout), kicker
accuracy, physicality at the breakdown, and territorial control. These structural
factors are measurable, persistent across matches, and highly predictive.

The sport has a clear annual international calendar that creates defined peak signal
windows, particularly the Six Nations (February–March) which is the highest-profile
rugby union tournament and the primary driver of fan token movement.

---

## Domain Model

### Season Calendar

| Phase | Dates (approx) | Token behaviour |
|---|---|---|
| Six Nations | Feb–Mar (annual) | Tier 1 — 5-week sustained window; Grand Slam narrative builds |
| Rugby Championship | Jul–Sep (Southern Hemisphere) | Tier 1 for ARG, AUS, NZL, RSA tokens |
| Rugby World Cup | Sep-Nov (every 4 years) | Maximum — highest single-tournament event |
| Autumn Internationals | Nov | Tier 2 — short series, directional signal |
| Domestic season (Premiership/URC/Top 14) | Sep–Jun | Tier 2–3 depending on context |
| Super Rugby | Feb–Jun | Tier 2 for Super Rugby clubs and SH nations |

### Competition Tier Classification

**Tier 1 — Maximum token impact:**
- Rugby World Cup (every 4 years)
- Six Nations (annual) — especially Grand Slam clinch matches
- Rugby Championship (annual, Southern Hemisphere)

**Tier 2:**
- Autumn Internationals / November Tests
- Six Nations — standard round matches (non-clinching)
- Premiership / URC / Top 14 finals and semi-finals

**Tier 3:**
- Regular domestic league matches
- Pre-season tours and warm-up internationals

---

## The Set Piece — rugby's structural foundation

Set piece dominance (scrum and lineout) is the most predictive structural variable
in rugby union. Teams that dominate the set piece control territory and possession,
which in turn creates scoring opportunities and reduces defensive exposure.

### Scrum dominance

```
SCRUM QUALITY ASSESSMENT:
  Dominant scrummage:
    Win 70%+ of own scrum ball — clean platform for backs
    Earn penalties from opposition (scrum penalty = 3 points or territory)
    Scrum dominance creates +8–12% win probability premium in tight matches

  SCRUM PERSONNEL SIGNALS:
    All 8 starting forwards available (tight five especially):
      Tighthead prop (position 3): most technical; loss = × 0.92 scrum quality
      Hooker (position 2): lineout throwing accuracy + scrum binding
    One key tight forward out: -10–15% scrum dominance
    Two tight forwards out: -20–30% scrum dominance; structural problem

  AGENT RULE: Check the tight five (props 1+3, hooker 2, locks 4+5) for injuries
  before any match assessment. This is the equivalent of checking the O-line in NFL.
```

### Lineout dominance

```
LINEOUT QUALITY ASSESSMENT:
  Own lineout retention rate: Elite 90%+ | Good 80–89% | Poor <75%
  Lineout steal rate (opposition ball): Elite >15% | Good 8–14%

  KEY LINEOUT PERSONNEL:
    Lineout jumpers (locks, flankers): loss disrupts calling patterns
    Lineout caller (usually hooker or lock): losing the caller = systematic disruption
    Established lineout partnership: 10+ matches together significantly better
      than new combinations

  LINEOUT AT THE BACK:
    Maul from lineout is a primary rolling forward platform
    Team with dominant lineout maul near opposition try line = high scoring probability
    Against a team that struggles to stop the maul: amplify × 1.15
```

---

## Kicker Intelligence — the single most influential individual in rugby

In tight rugby matches (within 6 points at the 60-minute mark), the goal kicker
determines outcomes more than any other individual. Kicking accounts for 60–75%
of all points scored in top-level rugby union.

```
KICKER QUALITY ASSESSMENT:
  Conversion rate from in front (within 30m): Elite 95%+ | Good 85%+
  Penalty kick rate (all positions): Elite 85%+ | Good 78%+
  Long range (40m+) success rate: Elite 70%+ | Good 60%+

KICKER INJURY / ABSENCE:
  Primary kicker out:
    Replacement has similar accuracy: RQD 0.10–0.15
    Replacement has lower accuracy (5–10% drop): RQD 0.25–0.35
      → In a 3-point match, one missed kick = match result
    No specialist kicker (outfield player kicking): RQD 0.45+
      → Structural scoring problem

PRESSURE KICKS:
  Final 10 minutes, within 3 points: kicker quality is the most critical variable
  Track: does this kicker have a record of making high-pressure kicks?
  Some elite kickers have documented better records under pressure
  (Jonny Wilkinson archetype); others deteriorate. This is researchable data.

AGENT RULE: Always check kicker availability and form before any Tier 1/2 match.
The kicker is the single most outcome-determining individual in close games.
```

---

## Breakdown and Ruck Dominance

```
BREAKDOWN QUALITY:
  Teams that win breakdown contests control ball availability and tempo
  Key metrics: penalty concession rate at the ruck (below 4 per match = disciplined)
               turnover rate won (above 8 per match = disruptive)

  BREAKDOWN SPECIALISTS (openside flanker — position 7):
    The best opensiders (turnovers, jackaling) are the most irreplaceable non-kicker
    Loss of a world-class openside: × 0.93 on breakdown quality
    Replacement openside with different skill set (scrummager vs jackal): structural shift

  PENALTY DISCIPLINE:
    Teams conceding 10+ penalties per match give opposition ~8 kickable chances
    Indiscipline under pressure is a consistent team trait — not random
    Yellow cards: 10-minute numerical disadvantage
      First yellow in a match: -15% win probability during sin bin period
      Second yellow to same player: red card risk — permanent disadvantage
```

---

## Weather and Surface

Rugby union is significantly weather-affected in a different way to most sports:

```
HEAVY RAIN / WET BALL:
  Ball handling errors increase significantly
  High-ball kicking strategy becomes more viable (opponent handling pressure)
  Teams with strong kicking game gain relative advantage
  Try-scoring probability decreases; kicking game becomes primary
  
  Wet weather adjusts team style:
    Kicking-dominant teams: relative advantage (their preferred style)
    Running/handling teams: relative disadvantage (skill set suppressed)

STRONG WIND:
  Kicking into wind: range and accuracy reduced significantly
  Kicking with wind: range advantage of up to 15m
  Field position and try zone more valuable than kicking points
  Look at which way each team will be kicking in each half

FROZEN / HARD GROUND:
  Sprint speed and agility are unchanged
  Contact injuries increase (hard surface)
  Ball bounce more unpredictable (high kicks less reliable)
```

---

## Result Impact Matrix

| Result / Event | Token impact |
|---|---|
| Six Nations match win (expected) | +4–8% |
| Six Nations match win (upset) | +8–18% |
| Six Nations Grand Slam clinch | +15–30% |
| Six Nations Championship win | +12–22% |
| Rugby World Cup win | +25–50% |
| Rugby World Cup Semi-Final win | +15–28% |
| Autumn International win (home) | +5–10% |
| Key kicker miss (decisive loss) | -5–12% |
| Star player injury (key position) | -8–18% |

---

## Sport-Specific Risk Variables

**Fatigue and schedule congestion** — International rugby players often play
for club and country in overlapping windows. Player release disputes and congested
fixture lists are a structural risk unique to the game's calendar.

**Referee impact** — Rugby union referee interpretations of the breakdown and
offside line are the highest variance officiating factor in any team sport.
A referee with a track record of penalising specific techniques (e.g., strict
on the offside line) can systemically disadvantage certain teams' playing styles.
This is researchable through referee assignment data.

**Home advantage** — Rugby union has the highest home advantage of any team sport
in this library. Home teams win approximately 65–70% of Test matches.
At Six Nations venues specifically, the crowd noise and physicality differential
for home vs away games is measurable.

---

## Signal Weight Adjustments

| Component | Weight | Rationale |
|---|---|---|
| Sports catalyst | 35% | Match result is dominant driver |
| Market / whale | 25% | Rugby has informed, engaged bettor community |
| Social sentiment | 15% | Passionate but smaller social footprint than football |
| Price trend | 15% | Between-series windows create trend opportunities |
| Macro | 10% | Moderate correlation during major tournaments |

---

## Agent Reasoning Prompts

```
1. CHECK THE TIGHT FIVE before any match. Props and hooker availability determines
   scrum quality, lineout reliability, and overall forward dominance.

2. CHECK THE KICKER. In matches decided by 1–2 penalties, kicker quality and
   current form determines the result more than team quality differences.

3. SIX NATIONS is the highest-profile annual rugby event. Grand Slam narratives
   build across the 5-week tournament — position sizing should scale with each
   successive win if a Grand Slam is on the line.

4. HOME ADVANTAGE in rugby is the strongest of any sport in the library.
   Away teams face a genuine, quantifiable disadvantage — always adjust.

5. WEATHER matters more in rugby than any other team sport in the library.
   Rain and wind change the entire style of play — teams with strong kicking
   games gain advantage; handling-focused teams are disadvantaged.

6. THE BREAKDOWN is an officiating-sensitive area. Check referee assignment
   and their historical penalty patterns before major matches.
```

---

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` for the full injury
framework. Rugby union-specific notes:
- Tight five (props, hooker, locks) injuries are structurally critical — treat as NFL O-line
- Kicker injuries require immediate RQD calculation (see kicker section above)
- Contact sport: bruising and minor injuries are routinely played through
- Concussion protocols are strict in professional rugby — comply flag is real

## Compatibility

**Athlete intelligence:** `athlete/rugby/athlete-intel-rugby-union.md`
**Injury intelligence:** `core/injury-intelligence/core-injury-intelligence.md`

---

*MIT License · SportMind · sportmind.dev*

---

## Event Playbooks

### Playbook 1: Six Nations home match (Tier 1)
```
trigger:  Six Nations home match at Twickenham/Cardiff/Murrayfield/Aviva/Stade de France/Olimpico
entry:    48h before kickoff once confirmed lineup available
exit:     Full time — not position-held beyond 80 minutes
filter:   Home team kicker confirmed fit; starting XV confirmed; no macro override active
sizing:   1.3× standard (Six Nations home advantage among strongest in library)
note:     Home advantage in Six Nations is historically 58–62% win rate regardless of form;
          apply extra weight to kicker accuracy data — margin of victory often 1–2 penalties
```

### Playbook 2: World Cup knockout match
```
trigger:  Rugby World Cup quarter-final onwards
entry:    72h before kickoff; reassess at 24h on lineup confirmation
exit:     Full time
filter:   Tier A or B set piece confirmed via press conference or historical data;
          injury list for front row checked; referee assignment loaded
sizing:   1.0× standard — variance is highest; no outsized position
note:     World Cup knockout eliminates form trends; tournament momentum matters more.
          Southern hemisphere teams historically perform better in neutral venues.
          Load core-officiating-intelligence.md for referee assignment.
```

### Playbook 3: Derby / rivalry match (away underdog)
```
trigger:  Historical derby where away team is underdog by >10% on form metrics
entry:    24h before kickoff; lineup confirmed
exit:     Full time
filter:   Both teams healthy at key positions (kicker, halfbacks, loose forwards);
          no extreme weather forecast (if heavy rain/wind, reconsider)
sizing:   0.7× standard — derby effect reduces form differential predictability by ~40%
note:     Rugby derbies (England vs Wales, Leinster vs Munster) compress predicted margins.
          Kicker form more predictive than attacking form in derbies.
```

### Playbook 4: Weather-impacted match (wind/rain forecast)
```
trigger:  Wind forecast >20mph OR rain probability >70% for outdoor rugby union match
entry:    Morning of match once weather confirmed; adjust in-game if conditions worsen
exit:     Full time
filter:   Check which team has stronger territorial kicking game and which relies on handling;
          both team styles assessed for weather resilience
sizing:   0.8× standard — weather variance is genuine; reduce size to account for uncertainty
note:     Teams with established aerial/territory game (Exeter, Ulster, Ulster, Stormers)
          gain vs teams relying on high-ball wide game in heavy conditions.
          Load core-weather-match-day.md — rugby section.
```

## Key Commands

For rugby union token and prediction signals, load these SportMind skills in order:

| Action | Skill | When to use |
|---|---|---|
| Domain intelligence | `sports/rugby/sport-domain-rugby-union.md` | Every analysis |
| Athlete modifier | `athlete/rugby/athlete-intel-rugby-union.md` | After domain load |
| Injury check | `core/injury-intelligence/core-injury-intelligence.md` | Key player doubt |
| Weather modifier | `core/core-weather-match-day.md` | Outdoor match |
| Officiating | `core/core-officiating-intelligence.md` | Major matches |
| Market context | `market/market-rugby-union.md` | Token decisions |

## Data Sources

- **Match results and stats:** ESPN Rugby (espnrugby.com), Opta Rugby, BBC Sport Rugby
- **Six Nations official:** sixnationsrugby.com
- **World Rugby official:** world.rugby
- **Player data:** ESPN Rugby profiles, World Rugby player rankings
- **Weather:** Met Office (UK), meteo-rugby fan tools
- **Odds:** Oddschecker rugby section, Betfair Exchange
