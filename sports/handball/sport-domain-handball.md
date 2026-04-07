# Handball — SportMind Domain Skill

Sport-specific intelligence for handball. Primarily covers the EHF Champions League
and the IHF World Championship. Strong market relevance in Germany, France, Spain,
Scandinavia (Denmark, Sweden, Norway), and Eastern Europe.

---

## Overview

Handball is a high-scoring, fast-paced indoor team sport combining elements of
football (goal structure) and basketball (court dimensions, fast breaks). It is
the second most popular team sport in Europe by participation and has a deeply
engaged fan base in its core markets. The sport is dominated by a small number of
elite clubs in the EHF Champions League, creating predictable tier structures.

The EHF Champions League is the primary commercial and token-relevant competition.
The IHF World Championship (national teams, every two years) is the secondary
peak event. Handball's indoor, controlled environment makes it more statistically
predictable than outdoor sports.

---

## Domain Model

### Competition Calendar

```
EHF CHAMPIONS LEAGUE (club, highest level):
  Group phase: Oct–Feb (~14 matches per team)
  Knockout rounds: Feb–Apr (Round of 16, Quarter-Finals, Semi-Finals)
  EHF FINAL4 (Final weekend): May/Jun (Cologne, Germany — fixed venue)
  
  The FINAL4 format: Both semi-finals + final in one weekend, one venue
  Creates massive concentrated commercial window (3 days, 4 elite clubs)

IHF WORLD CHAMPIONSHIP (national teams):
  Every 2 years (odd years)
  January (2–3 weeks)
  Highest national team competition — World Cup equivalent for handball

EHF EURO (European Championship):
  Every 2 years (even years, alternating with World Championship)
  National teams; January
  
BUNDESLIGA (Germany) / LNH (France) / ASOBAL (Spain):
  Domestic leagues running Sep–Jun
  Primary feeder for Champions League places
```

### Power Structure — European Club Dominance

```
ELITE TIER (consistent CL contenders):
  Barcelona (ESP): most decorated club in EHF CL history
  Kiel / THW Kiel (GER): German powerhouse, consistent FINAL4 presence
  Paris Saint-Germain (FRA): recent investment; top European contender
  Magdeburg / SC Magdeburg (GER): EHF CL winners 2023
  Kielce / Vive Kielce (POL): consistent CL semifinalist
  Aalborg (DEN): Danish champions; growing European force
  
  BUDGET ADVANTAGE: Barcelona, PSG, Kiel operate at 2–3× the budget of
  mid-tier CL clubs. Financial superiority is more directly translatable
  to results in handball than most sports.

NATIONAL TEAM TIER 1:
  Denmark: World/European champions; defending standard
  France: Multiple World and Olympic titles
  Spain: Consistent World/European medalist
  Sweden, Norway, Germany: traditional powers
  
  Emerging: Croatia, Portugal, Slovenia (growing competitive level)
```

---

## Scoring and Tactical Framework

Handball is high scoring (typical match: 55–70 combined goals) with short
possession sequences. This creates specific prediction properties:

```
TYPICAL SCORES:
  High-scoring game: 35-30 total = 65 combined goals
  Standard game: 30-27 total = 57 combined goals
  Tight defensive game: 25-23 total = 48 combined goals

KEY TACTICAL VARIABLES:

FAST BREAK efficiency:
  Fast breaks (goals scored in transition before defence resets) score at ~70%
  Teams that generate 6+ fast breaks per game = significant attack advantage
  Fast break rate is the closest handball equivalent to counter-attack in football

GOALKEEPER QUALITY:
  Typical save percentage: 30–35% across a game (much lower than ice hockey)
  Elite performance: 40%+ (exceptional game)
  Save % < 25%: below-average performance; team disadvantage
  
  KEY INSIGHT: Goalkeeper hot streaks change game outcomes dramatically
  A goalkeeper at 45% saves for a 60-minute game is effectively worth
  ~5 additional goals prevented vs a poor-performing keeper
  
SEVEN-METRE THROW (penalty) conversion:
  Elite teams: 80%+ conversion
  Below average: < 70%
  Designated seven-metre specialist: check if playing — conversion drops
  without the specialist
  
6-0 vs 5-1 DEFENCE:
  6-0 (flat defensive line): compact, hard to break down
  5-1 (advanced player in front): disrupts build-up, creates turnovers
  Teams that switch effectively between systems are harder to predict
  and harder for opponents to read
```

---

## The Goalkeeper — critical in close matches

```
GOALKEEPER DOMINANCE SIGNALS:
  Consecutive saves (3+ in a row): momentum shift signal
  Save % in first 20 minutes: sets psychological tone of game
  
  GOALKEEPER FATIGUE:
    Handball goalkeepers rarely rotate (unlike ice hockey)
    Long tournament runs (World Championship: 9+ games) = accumulated fatigue
    Watch: save % declining in knockout rounds vs group stage
    
  GOALKEEPER MATCHUP:
    Some goalkeepers have documented better performance against specific
    throwing styles (high, low, corner) — researchable in elite statistics databases
    
GOALKEEPER MODIFIER:
  Elite game (40%+ SV): × 1.15 on team win probability
  Average game (32–37% SV): × 1.00
  Below average game (< 28% SV): × 0.88
```

---

## Home Advantage and Crowd Factor

Indoor handball has pronounced home crowd effects — the sport is played in intimate
arenas (typically 5,000–15,000 capacity) where crowd noise has a direct impact.

```
HOME ADVANTAGE SIGNAL:
  Handball home win rate in Bundesliga: ~62–65%
  EHF CL home round: ~60%
  
  FORTRESS VENUES:
    Barclaycard Arena (Hamburg/HSV Handball): ~13,000; intense atmosphere
    LANXESS Arena (Cologne): used for EHF FINAL4; neutral but generates atmosphere
    Scandinavian arenas: notoriously loud relative to size
    
  CROWD AMPLIFICATION IN TIGHT GAMES:
    Close game (within 2 goals) in second half: home crowd effect measurable
    In matches decided by 1–2 goals: home advantage worth ~60% win probability
    
  NEUTRAL VENUE (EHF FINAL4):
    Both semi-finals played at single venue; neither team has home advantage
    Eliminate home advantage modifier for FINAL4 predictions
```

---

## Fatigue and Scheduling

Handball has among the most congested fixture schedules in European team sport:

```
CONGESTED SCHEDULE (EHF CL phase):
  Top clubs play: domestic league game + EHF CL game most weeks
  Some weeks: 2 domestic games + 1 EHF CL game
  
  FATIGUE MODIFIER:
    3 games in 7 days: × 0.92 on second and third game
    Second game of back-to-back (< 48h): × 0.88
    
  SQUAD DEPTH ADVANTAGE:
    Teams with 20+ quality players can rotate without significant quality drop
    Budget teams with 14–16 players: fatigue is a structural disadvantage
    Check: does the top club have meaningful rotation depth?
    
  JANUARY DOUBLE DUTY (national team months):
    World Championship and EHF Euro both run in January
    Club seasons pause but clubs resume at full intensity immediately after
    Players returning from long international campaigns: first 2 club games × 0.93
```

---

## Event Playbooks

### Playbook 1: EHF FINAL4 — Elite Club Concentration
```
trigger:  EHF FINAL4 weekend confirmed; 4 teams known
entry:    Day before semi-finals (sustained 3-day window)
exit:     Final completion (Sunday evening)
filter:   Token holder base includes European handball markets
          Elite tier club (Barcelona, Kiel, PSG) in the event
sizing:   1.25× — highest concentrated handball event; 3-day media focus
note:     The EHF FINAL4 is handball's equivalent of the Champions League Final
          in a compressed single weekend. No home advantage; pure quality test.
```

### Playbook 2: National Team Final (World Championship / EHF Euro)
```
trigger:  Semi-final or Final of IHF World Championship or EHF Euro
entry:    Day before semi-final
exit:     24h post-final
filter:   Nation has token holder community in relevant market
          Denmark, France, Spain, Germany as Tier 1 nations
sizing:   1.20× — national team success drives broader market engagement
```

### Playbook 3: Goalkeeper Elite Performance
```
trigger:  Goalkeeper records 40%+ save percentage in consecutive matches
entry:    Following match (form continuation signal)
exit:     First match below 33% save percentage
filter:   Team has quality outfield system (not relying solely on GK)
sizing:   0.95× — secondary signal; harder to predict continuation
note:     Hot goalkeeper stretches are real but shorter duration than ice hockey.
          Handball scoring rate is too high for a single goalkeeper to
          carry a team the way a hockey goaltender can.
```

---

## Result Impact Matrix

| Result / Event | Signal impact |
|---|---|
| EHF FINAL4 win (Champions League) | +20–40% |
| EHF CL Semi-Final win | +10–20% |
| World Championship win | +25–45% |
| World Championship Final | +12–22% (finalist) |
| Domestic league title | +8–15% |
| Key player (GK or key attacker) injury | -10–22% |

---

## Signal Weight Adjustments

| Component | Weight | Rationale |
|---|---|---|
| Sports catalyst | 35% | Match results and tournament progress dominant |
| Social sentiment | 20% | Strong community in core European markets |
| Market / whale | 20% | Established European betting market |
| Price trend | 15% | Tournament progression creates sustained trends |
| Macro | 10% | Moderate European market correlation |

---

## Agent Reasoning Prompts

```
1. GOALKEEPER PERFORMANCE is the highest-variance single-game variable.
   A game where the goalkeeper is 10% above average save rate changes
   expected margin by ~5–7 goals. Always check recent GK form.

2. FAST BREAK EFFICIENCY tells you about transition quality — the highest
   efficiency scoring opportunity in handball. Dominant fast break teams
   win at a higher rate than their defensive metrics suggest.

3. EHF FINAL4 IS DIFFERENT from regular EHF CL rounds. No home advantage,
   compressed schedule, maximum media pressure. Pure quality test.

4. JANUARY SCHEDULING: World Championship months are the most congested
   in the handball calendar. Players returning to clubs after 2–3 week
   international campaigns face fatigue and rhythm disruption.

5. FINANCIAL TIER MATTERS MORE IN HANDBALL than most sports. Barcelona and
   PSG's budget advantage is more directly translatable to results.
   Consistent upset prediction against these clubs requires specific signals.
```

---

## Fan Token Notes

No active handball fan token on Chiliz as of Q1 2026. Core European markets
(Germany, France, Spain, Denmark) represent a credible token audience.
EHF FINAL4 weekend in Cologne would be the primary activation event.

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` for the full framework.
Handball-specific notes:
- Finger and hand injuries are endemic (blocking and ball-catching)
- Knee injuries (ACL) are the most season-disrupting — high-jump landing landings
- Goalkeeper hand injuries are most critical (affects catching and throwing)

## Data Sources

- **EHF official (eurohandball.com)**: Results, standings, player data
- **Handball-Planet.com**: News, previews, player statistics
- **IHF official (ihf.info)**: International competition results
- **Sofascore / Flashscore**: Live stats including save percentages

## Compatibility

**Injury intelligence:** `core/injury-intelligence/core-injury-intelligence.md`

---

*MIT License · SportMind · sportmind.dev*

### Playbook 4: EHF Final4 / Men's Champions League Final4 (Budapest)
```
trigger:  EHF Champions League Final4 weekend (early June, Budapest)
entry:    Semifinal results loaded; 24h before final
exit:     Final whistle
filter:   Goalkeeper form loaded from last 3 matches; top scorer fitness confirmed;
          financial tier of club confirmed (Tier 1 clubs: Barcelona, PSG handball,
          Kiel, Montpellier)
sizing:   1.2× standard — highest single handball event; outsized social and token signal
note:     The EHF Final4 in Budapest is the Champions League final equivalent for handball.
          Goalkeeper performance in these matches is the single most predictive variable.
          Barcelona and PSG handball have dominated recent editions — tier gap is real.
```
