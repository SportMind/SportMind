# Australian Rules Football (AFL) — SportMind Domain Skill

Sport-specific intelligence for the AFL (Australian Football League) —
the premier domestic competition for Australian rules football.

---

## Overview

Australian rules football is Australia's most-watched domestic sport and one of
the most unique team sports in the world. An oval field, 18 players per side,
no offside, continuous flow, and a dual scoring system (goals worth 6, behinds
worth 1) create prediction dynamics unlike any other sport in this library.

The AFL currently has no active Chiliz fan token, but the Australian sports market
is one of the most engaged and tech-forward in the world. Token infrastructure
expansion toward AFL is a credible near-term scenario, particularly given the
AFL's existing digital product ambitions and its dominant cultural position in
Victoria, South Australia, Western Australia, and Queensland.

---

## Domain Model

### Season Calendar

| Phase | Dates (approx) | Signal character |
|---|---|---|
| Pre-season (AAMI) | Feb–Mar | Roster intel; limited prediction value |
| Regular season (H&A) | Mar–Aug | 22 rounds; 17 home and away games per club |
| Finals Series | Sep | Top 8; elimination bracket |
| AFL Grand Final | Last Sat in Sep | MCG; largest Australian sporting event |

### Competition Structure

```
18 CLUBS (as of 2024):
  Victorian clubs (10): Collingwood, Carlton, Richmond, Hawthorn,
                        Geelong, Essendon, Melbourne, North Melbourne,
                        St Kilda, Western Bulldogs
  Interstate clubs (8): Adelaide, Port Adelaide (SA), West Coast, 
                        Fremantle (WA), Brisbane, Gold Coast (QLD),
                        GWS, Sydney (NSW)

FINALS SYSTEM (top 8):
  Week 1: 1v2 (winner straight to prelim), 3v4 (winner straight to prelim),
          5v8 (loser eliminated), 6v7 (loser eliminated)
  Week 2: Elimination finals + Qualifying final losers vs week 1 winners
  Week 3: Preliminary finals (4 teams, 2 games)
  Grand Final: MCG (neutral venue, always Melbourne)
  
HOME GROUND ADVANTAGE:
  Significantly stronger than most football codes — oval grounds vary enormously
  in size, surface, and crowd density
  Interstate travel is a documented performance penalty in the AFL
```

---

## The Scoring System — AFL's unique prediction challenge

The dual scoring system (goals + behinds) makes AFL prediction more complex than
single-score sports and requires a distinct analytical framework.

```
SCORING:
  Goal (ball through tall posts): 6 points
  Behind (ball through short posts or off post): 1 point
  
  Final score example: 14.9 (93) = 14 goals × 6 + 9 behinds × 1 = 93 points
  
SCORE MARGINS:
  Typical winning margin: 15–40 points
  Close games (< 1 goal / < 7 points): ~25% of matches
  Blowouts (> 50 points): ~20% of matches
  
KICKING ACCURACY — KEY PREDICTIVE VARIABLE:
  A team with 20 goals from 30 scoring shots = 66% accuracy
  A team with 20 goals from 40 scoring shots = 50% accuracy (wasting opportunities)
  
  Inaccurate teams often lose games they should win — inaccuracy is exploitable
  Check: team kicking accuracy % over last 5 matches
  
  Kicking accuracy modifier:
    Team accuracy 65%+: × 1.08 (converting opportunity into scores)
    Team accuracy 45-54%: × 0.92 (wasting significant chances)
    Team accuracy < 45%: × 0.82 (structural scoring inefficiency)
    
  Wind is the primary driver of in-game accuracy variance — see weather section
```

---

## Key Positional Intelligence

### The Midfield — AFL's engine room

AFL has no fixed positions in the traditional sense, but the midfield group
(typically 3–4 players) controls possession and clearance — the single most
important statistical correlate with winning.

```
CLEARANCE DOMINANCE:
  Clearances (ball won from stoppages): Elite team 40+ per game vs opponent
  Clearance differential: winning by 5+ clearances → win ~70% of matches
  
  Key clearance players:
    Contested ball specialist: wins ball at stoppages, in traffic
    Running midfielder: links play, contributes to inside 50s
    
  LOSS OF KEY MIDFIELDER:
    Top clearance player injured: × 0.88 on clearance output
    If second-best clearance player also out: × 0.80
```

### The Key Forward — goals determine results

```
KEY FORWARD (tall forward who marks and kicks goals):
  Most important individual scoring position
  Elite: 60+ goals per season (roughly 3+ per game)
  
  FORWARD INJURY IMPACT:
    Elite key forward out: RQD 0.30–0.45 (extremely hard to replace)
    Replacement with different style (small, mobile): team must restructure attack
    × 0.78 on expected score output when key forward is out
    
  Note: AFL teams with two quality key forwards are significantly more
  resilient to injury than teams relying on a single target
```

### The Ruckman — contested ball starts here

```
RUCKMAN (tall player who contests ball at centre bounces):
  The starting point for clearance chains
  Elite ruckman wins 55%+ of hitouts (touches at the bounce)
  
  Ruckman dominance modifier:
    Elite ruckman vs weaker opponent: × 1.08 on midfield clearances
    Loss of ruckman: × 0.88 (ruck substitute is significantly inferior)
```

---

## Home Ground and Travel Dynamics

AFL has the most pronounced home ground advantage of any Australian sport, and
interstate travel has a documented performance impact.

```
HOME GROUND ADVANTAGE:
  Standard home ground advantage: +8–12% win probability premium
  
  FORTRESS GROUNDS (crowd + familiarity amplification):
    MCG for Collingwood, Richmond, Carlton: largest crowd venues
    Kardinia Park (Geelong): historically strongest home advantage in AFL
    Marvel Stadium: less crowd advantage (shared venue)
    
  HOME DEBUT EFFECT:
    Clubs playing first game at new stadium or season opener: crowd factor elevated
    
INTERSTATE TRAVEL PENALTY:
  Western Australian clubs (West Coast, Fremantle) travelling east:
    Time zone: WA is 2–3 hours behind eastern states
    Travel: ~4h flight
    Performance penalty: approximately -6% win probability on eastern travel
    
  Queensland clubs (Brisbane, Gold Coast) to WA or SA: similar penalty
  
  Victorian clubs travelling interstate: moderate penalty
  
  Cross-country (WA to QLD / NSW to WA): maximum travel penalty
    Apply: × 0.88 for travelling team (before other adjustments)
    
  BACK-TO-BACK INTERSTATE:
    Club playing two interstate games in one week: × 0.85 additional
```

---

## Weather and the Oval Field

```
WIND:
  Most AFL grounds have prevailing wind direction
  Teams that kick with wind in a quarter have kicking advantage:
    Accuracy improves: + 8–12% goals from scoring shots
    Distance of marks and kicks increases significantly
    
  WIND DIRECTION CHANGES (swirling wind):
    Nullifies systematic wind advantage
    Increases inaccuracy for both teams
    Tighter, lower-scoring game likely
    
RAIN:
  Wet ball: marking (catching) becomes harder
  Reducing high marks — less aerial contests, more contested ball
  Favours: defensive, contested-ball oriented teams
  Hurts: teams that rely on clean hands and high marking forward structure
  
  Rain modifier:
    Heavy rain: × 0.90 on expected score total (both teams)
    Light rain: × 0.95
    
MCG-SPECIFIC:
  Largest ground in the AFL (~160m long oval)
  Favours teams with fast running patterns and ball use
  Punishes teams that rely on contested pack football (too much open space)
```

---

## Event Playbooks

### Playbook 1: Finals — Elimination Game (Loser Out)
```
trigger:  Elimination final or semi-final (loser eliminated)
entry:    Pre-game (after team lists confirmed)
exit:     Game completion
filter:   Team with significantly better finals record (experience signal)
          Home state advantage (MCG or interstate travel context)
sizing:   1.15× — finals are significantly more predictable than regular season
note:     Finals football is more defensive and lower-scoring than regular season.
          Teams with strong defensive structures outperform their regular season
          rankings more often than attacking teams.
```

### Playbook 2: Clearance Dominance Mismatch
```
trigger:  One team ranks top-5 in clearances; opponent ranks bottom-5
entry:    Pre-game
exit:     Game completion
filter:   No significant injury to key clearance players (check teams)
          Standard weather (heavy rain reduces clearance dominance signal)
sizing:   1.10× — clearance differential is the strongest team-level signal in AFL
```

### Playbook 3: Grand Final — MCG
```
trigger:  AFL Grand Final (last Saturday in September)
entry:    Week of final (sustained narrative)
exit:     48h post-match
filter:   Victorian club competing (home state advantage at MCG)
          Token holder base includes Australian fan community
sizing:   1.50× — largest Australian sporting event of the year
note:     AFL Grand Final is the Super Bowl equivalent for Australian audiences.
          Weekend-long event; attendance 100,000+; public holiday in Victoria.
```

### Playbook 4: Interstate Travel Back-to-Back
```
trigger:  Club playing second interstate game in 7 days (confirmed schedule)
entry:    Pre-game
exit:     Game completion
filter:   Opponent is playing at home (no travel)
          Teams have similar regular season form
sizing:   1.10× on home team — travel fatigue signal is reliable in AFL
```

---

## Result Impact Matrix

| Result / Event | Signal impact |
|---|---|
| Regular season win (standard) | +3–7% |
| Finals win (any round) | +8–18% (scales with round) |
| Grand Final win | +30–55% |
| Preliminary Final win (one game from GF) | +15–28% |
| Key forward injury (season-ending) | -15–30% |
| Interstate travel game win | +5–10% (upset premium if away) |
| Top-of-ladder round (unbeaten run) | +10–20% narrative signal |

---

## Signal Weight Adjustments

| Component | Weight | Rationale |
|---|---|---|
| Sports catalyst | 35% | Match result and finals position dominant |
| Social sentiment | 20% | Extremely passionate supporter bases |
| Market / whale | 20% | Mature AFL betting market in Australia |
| Price trend | 15% | Finals runs create sustained signals |
| Macro | 10% | Higher than average — Australian market correlation |

---

## Agent Reasoning Prompts

```
1. CHECK TEAM LISTS (Tuesday/Thursday naming). AFL has a team list system
   similar to NRL — always wait for official confirmation before prediction.
   
2. KICKING ACCURACY is highly variable and underpriced. A team that is
   25% less accurate than average is losing ~2 goals worth of scoring.
   Check last 5 matches accuracy before any game.

3. CLEARANCE DIFFERENTIAL is the strongest team-level statistical predictor.
   Teams that win the contested possession battle win ~70% of AFL games.

4. INTERSTATE TRAVEL is real and measurable. WA clubs travelling east and
   eastern clubs travelling to Perth face documented performance penalties.

5. WIND DIRECTION at game time changes the structure of the game entirely.
   Strong consistent wind creates systematic advantage for teams kicking
   with it; swirling wind reduces team quality differentials.

6. AFL FINALS are different from regular season. More defensive, lower scoring,
   more dependent on experience. Teams with finals experience outperform
   regular season form in elimination games.

7. THE MCG FOR THE GRAND FINAL is the most significant single venue factor
   in Australian sport. Victorian clubs have a proven home-state advantage
   at this game even before other factors are considered.
```

---

## Fan Token Notes

No AFL fan token is currently active on Chiliz (as of Q1 2026). The AFL is
included for prediction market, analytics agent, and future token readiness.
When AFL tokens launch, the highest-value franchises will likely be:
Collingwood (largest membership), Richmond, Carlton, Geelong, and Essendon.
Grand Final week is the primary token activation window.

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` for the full framework.
AFL-specific notes:
- ACL injuries are the most season-disrupting (8–12 month recovery)
- Hamstring injuries are endemic in AFL (explosive sprinting on large oval)
- "Managed" players: AFL clubs frequently rest players 1 game for load management
- Team lists released Tuesday (extended) and Thursday (final) — check both

## Data Sources

- **AFL official (afl.com.au)**: Team lists, injury news, results
- **Champion Data**: Advanced AFL statistics (subscription)
- **The Arc (thearcfooty.com)**: Free advanced analytics and expected scores
- **footywire.com**: Player statistics, historical records
- **AFL Player Ratings**: Official ratings by position

## Compatibility

**Injury intelligence:** `core/injury-intelligence/core-injury-intelligence.md`

---

*MIT License · SportMind · sportmind.dev*
