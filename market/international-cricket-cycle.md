# Cricket International Cycle — SportMind Intelligence Framework

**The perpetual cycle model for international cricket.**
Cricket has the most complex international competition structure of any sport in
the library — three formats, multiple governing bodies, a unique bilateral series
model, domestic T20 leagues running in parallel, and the single largest untapped
fan token market in the world sitting behind a regulatory wall.

---

## Cricket's structural complexity

Cricket's international cycle is not a simple tournament-then-rest pattern.
It is a permanently active competition environment where:

- **Three formats run simultaneously** — T20Is, ODIs, and Tests happen in the same window
- **Bilateral series** are as commercially important as ICC tournaments for some markets
- **Domestic T20 leagues** (IPL, BBL, PSL, CPL, SA20, ILT20) run throughout the year
  and their domestic signals interact with international signals
- **The same players** compete in all three environments, creating fatigue, rotation,
  and availability signals that affect every level simultaneously

```
CRICKET'S PARALLEL SIGNAL LAYERS:

Layer 1: ICC Major Tournaments (global competition)
  T20 World Cup (odd years), ODI World Cup (every 4 years), Champions Trophy,
  World Test Championship Final, ICC Under-19 World Cup

Layer 2: ICC Regional Tournaments
  Asia Cup, Caribbean Premier League qualifiers, regional T20 events

Layer 3: Bilateral Series (nation-vs-nation)
  India bilateral series (highest commercial value in cricket)
  England bilateral series (second highest for Test cricket)
  Ashes (England vs Australia, every 2 years alternating home/away)
  Border-Gavaskar Trophy (India vs Australia)

Layer 4: Domestic Leagues (club-level)
  IPL (India, March-May) — largest commercial league
  BBL (Australia, December-February)
  PSL (Pakistan, February-March) — active Chiliz tokens
  SA20 (South Africa, January-February)
  ILT20 (UAE, January-February)
  CPL (Caribbean, August-September)
  
  These layers run simultaneously. Agent rule: never analyse one layer
  without checking what is happening in the other three.
```

---

## The three-tier cricket NCSI hierarchy

| Competition | NCSI weight | Format | Notes |
|---|---|---|---|
| ICC T20 World Cup Final | 1.00 | T20 | Maximum; 2-year cycle |
| ICC ODI World Cup Final | 1.00 | ODI | Maximum; 4-year cycle |
| WTC Final (Mecca: Lord's) | 0.85 | Test | 2-year WTC cycle climax |
| ICC T20 WC (SF/Final) | 0.85–0.95 | T20 | Knockout escalation |
| ICC ODI WC (knockout rounds) | 0.80–0.95 | ODI | Quarter-final onwards |
| India-Pakistan (any format) | 1.00 modifier | Any | ×2.00 — overrides tier |
| Asia Cup Final | 0.75 | ODI/T20 | India usually involved |
| Champions Trophy Final | 0.80 | ODI | 50-over prestige |
| Ashes (decisive Test) | 0.75 | Test | Alternates home/away |
| Border-Gavaskar Trophy | 0.70 | Test | India vs Australia |
| ICC tournaments (group stage) | 0.45–0.60 | Various | Format-dependent |
| Major bilateral series (final) | 0.50–0.65 | Various | India bilateral premium |
| IPL Qualifier/Final | 0.70 | T20 | Domestic but highest-profile |
| Standard IPL match | 0.35 | T20 | High volume; individual match lower |
| PSL Final | 0.60 | T20 | Active Chiliz token market |
| Standard bilateral Test | 0.40 | Test | Series-specific |
| T20I (standalone) | 0.25 | T20 | Low if no tournament context |

---

## The India premium — permanent override

```
INDIA FACTOR (applies to all layers):

Every India match: base signal × 1.40
India vs Pakistan: base signal × 2.00 (overrides all tier weights)

WHY THIS NEVER CHANGES:
  India = 1.4 billion population, 200M+ cricket viewers per match
  India-Pakistan = 400-500M viewers — global highest single sporting event
  No other cricket signal comes close to this scale

INDIA AT EACH LAYER:

Layer 1 (ICC Tournaments):
  India in knockout stage: all competing tokens see NCSI spike
  India eliminated: significant negative signal for all cricket tokens
  India-Pakistan at ICC tournament: ×2.00 regardless of match type (pool or knockout)

Layer 3 (Bilateral):
  India bilateral at home: highest bilateral signal in cricket
  India in England/Australia: significant international bilateral signal
  India vs smaller nations: elevated vs standard but no special modifier

Layer 4 (IPL):
  IPL = India's flagship; separate IPL NCSI framework (see below)
  India players unavailable for national duty during IPL = conflict monitoring
```

---

## ICC Tournament Calendar (perpetual)

```
ODD YEARS (T20 World Cup):
  T20 WC 2026: India + Sri Lanka hosting (PEAK — India hosting = maximum engagement)
  T20 WC 2028: TBD
  Duration: 3-4 weeks | Teams: 20 | Format: group + Super 8 + knockout

EVEN YEARS (ODI World Cup alternates with Champions Trophy):
  ODI World Cup: every 4 years (2023 India ✅, 2027 South Africa)
  Champions Trophy: alternating years (2025 Pakistan, 2029 TBD)
  
WORLD TEST CHAMPIONSHIP (WTC):
  2-year cycle; top 9 Test nations
  WTC Final at Lord's (June): highest-profile single Test match
  2023: Australia won ✅ | 2025 cycle | 2027 cycle
  
  WTC Final signal: NCSI 0.85 — sustained 2-year narrative resolution
  India in WTC Final: apply India premium (×1.40)

SIGNAL CALENDAR RULE:
  Every June: Check if WTC Final is scheduled (even years — matches Champions Trophy)
  Every alternate June: ICC knockout events (T20 WC or ODI WC)
  
  Cricket has an ICC major event almost every year — it never goes dormant.
```

---

## Bilateral series model

```
WHY BILATERALS MATTER IN CRICKET:

Unlike football (where domestic leagues are primary and bilaterals are secondary),
cricket bilateral series are often the primary scheduled competition between
nations for 1-2 year stretches.

THE BILATERAL HIERARCHY:

Tier A — India bilateral (home or away):
  India hosting England: highest bilateral engagement globally
  India hosting Australia: NCSI 0.65 per match; sustained series signal
  India touring England: elevated English market signal
  India touring Australia: Border-Gavaskar context (Test series)
  
Tier B — Ashes:
  England vs Australia, alternating home/away every 2 years
  5-Test series; most historic bilateral series in cricket
  Series-deciding Test: NCSI 0.75
  
Tier C — Other major bilaterals:
  Australia vs South Africa, Pakistan vs England, etc.
  NCSI 0.35-0.55 per match depending on format and stakes

SERIES MOMENTUM (bilateral-specific):
  Unlike ICC tournaments with eliminations, bilateral series have a series score.
  Team leading 2-0 in a 5-Test series: reduced urgency for individuals
  Team trailing 0-2: maximum urgency; potential series-saving matches
  
  AGENT RULE: Apply series_score_momentum to bilateral analysis.
  Trailing team at 0-2 in Test series: apply narrative_active flag.
  This is the bilateral equivalent of elimination pressure in tournaments.
```

---

## Domestic T20 leagues — the parallel universe

```
THE DOMESTIC LEAGUE CALENDAR:

IPL (India) — March to May:
  32 group matches + playoffs (Qualifier 1, Eliminator, Qualifier 2, Final)
  Signal weight: per match 0.35; Qualifier/Final 0.70
  10 franchises; 74 matches total
  
  IPL REGULATORY GAP (see also i18n/hi/sports/cricket/):
    India VDA framework doesn't yet support fan tokens clearly
    SEBI regulatory clarity = library's biggest potential commercial event
    Monitor: Finance Ministry, SEBI, BCCI announcements monthly
    
  WHEN IPL CONFLICTS WITH NATIONAL DUTY:
    IPL schedule sometimes overlaps with ICC events or bilateral series
    Player withdrawal from IPL for national duty = franchise token negative
    Player withdrawal from national duty for IPL = controversy signal
    
BBL (Australia) — December to February:
  Over the Australian summer; overlaps Boxing Day Test
  Domestic signal; limited fan token relevance currently
  
PSL (Pakistan) — February to March:
  Active Chiliz token market — highest cricket token signal currently active
  PSL Final: NCSI 0.60; series highest for active cricket tokens
  
SA20 (South Africa), ILT20 (UAE), CPL (Caribbean):
  Growing leagues; limited current token relevance
  Monitor: SA20 commercial announcements (South Africa = Tier 2 cricket market)

AGENT RULE FOR OVERLAPPING LAYERS:
  When IPL and international cricket run simultaneously (rare but happens):
  Apply the higher NCSI weight; do not double-apply both weights
  Note the conflict in reasoning_summary
```

---

## Post-tournament transition (cricket-specific)

```
CRICKET'S UNIQUE POST-TOURNAMENT BEHAVIOUR:

Unlike football, cricket doesn't have a concentrated transfer window.
Player movement between countries for T20 leagues is ongoing.
The "transfer" equivalent is: which T20 leagues does a player participate in?

POST-ICC TOURNAMENT TRANSITION:

Week 1-2: Tournament narrative completes
  ICC T20 WC winner: token signal holds for 3-5 days then decays
  Losing finalist: modest negative; eliminated in group stage: stronger negative
  
Week 3-8: Domestic league recruitment
  Auction/draft for next T20 league season begins or continues
  Player value at auction = direct function of ICC tournament performance
  A breakout ICC tournament = elevated auction price for next IPL/BBL/PSL
  
  AGENT RULE: After any ICC tournament, recalculate ATM scores for standout players
  before next domestic league auction. Tournament performance directly shifts
  auction value and therefore club token NCSI impact.

Month 2+: Bilateral series resumes
  National team players return to bilateral schedule
  Return to pre-tournament NCSI framework
  No sustained post-tournament drag (unlike football's narrative retention)

ASHES YEAR POST-SERIES:
  Post-Ashes (August): England domestic cricket winds down
  Australian domestic BBL begins December
  Very different timeline from football's continuous season model
```

---

## The Ashes — bilateral series as sustained narrative

```
THE ASHES (England vs Australia, every 2 years):

Structure: 5 Tests (best-of-5), alternating home/away
Away team context: 5-7 weeks of tour; visiting team in unfamiliar conditions

HOME ADVANTAGE IS EXTREME IN ASHES:
  Subcontinental pitches: heavily favour spin; visiting teams struggle
  English conditions: pace and swing; Australian batters historically struggle
  
  AGENT RULE: In the Ashes, condition-specific advantage > form advantage.
  Apply home conditions modifier more aggressively than in other cricket contexts.

ASHES SIGNAL CALENDAR:
  Series opening Test: NCSI 0.60
  Decisive Test (urn won or retained): NCSI 0.75
  5th Test (live series): NCSI 0.75
  Series whitewash completion: NCSI 0.65 (final result inevitable but narrative closure)
  
ASHES NARRATIVE ARC:
  England at home (even years): 3-match narrative arc for series control
  England in Australia (odd years): typically higher individual match stakes
  (Australia historically stronger at home; England comebacks are narrative events)
```

---

## Agent loading instruction

```
WHEN TO LOAD THIS DOCUMENT:

Load for:
  Any cricket token or prediction market analysis
  IPL franchise token intelligence (despite no active tokens — monitoring)
  PSL token signal analysis (active Chiliz tokens)
  India-Pakistan match analysis (always load — ×2.00 override)
  Post-ICC tournament APS/transfer intelligence
  Bilateral series signal weighting

Load alongside:
  fan-token/cricket-token-intelligence/ (cricket bridge)
  market/world-cup-2026.md (NCSI model reference)
  market/international-football-cycle.md (structural comparison)
  i18n/hi/sports/cricket/ (Hindi cricket market context)
  macro/macro-geopolitical.md (India-Pakistan geopolitical context)

Template note:
  This document follows the same framework as international-football-cycle.md
  and international-rugby-cycle.md. The cycle concept is the standard SportMind
  template for all tournament-structured sports.
```

---

*MIT License · SportMind · sportmind.dev*
