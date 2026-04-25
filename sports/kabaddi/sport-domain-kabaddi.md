# Kabaddi (Pro Kabaddi League) — SportMind Domain Skill

Sport-specific intelligence for kabaddi. Primarily covers the PKL (Pro Kabaddi League)
— India's premier professional kabaddi competition and one of the most-watched
domestic sports leagues in the world.

---

## Overview

Kabaddi is a contact team sport native to South Asia and is among the most-watched
sports in the world by raw viewership numbers. The PKL consistently draws 300–400
million viewers per season in India, placing it in the same audience tier as major
European football leagues. The sport involves a single "raider" crossing into the
opposing team's half, tagging defenders, and returning to their own half — all
while chanting "kabaddi" continuously without taking a breath.

The PKL is the dominant professional kabaddi competition globally. It uses a
franchise model with 12 city-based teams, with the season running from July to
October. India's growing sports tech sector and massive social media fanbase make
kabaddi one of the highest-priority emerging token markets in the library.

---

## Domain Model

### PKL Season Calendar

```
PKL STRUCTURE (current format):
  12 teams in one division (no conferences)
  Each team plays 22 league phase matches
  Season duration: July–November (~4 months)
  
  League phase: Double round-robin (each team plays each opponent twice)
  Playoffs: Top 6 teams qualify
    Eliminator 1 and 2: 5th vs 6th, 3rd vs 4th (losers eliminated)
    Semi-Finals: 1st vs highest survivor, 2nd vs other survivor
    Final: two semi-final winners
    
POINTS SYSTEM:
  Win: 5 points | Tie: 3 points | Loss: 0 points
  Bonus: Extra point for winning by 7+ point margin
  
PKL TEAMS (Season 10, 2023-24):
  Bengaluru Bulls, Dabang Delhi, Haryana Steelers, Jaipur Pink Panthers,
  Patna Pirates, Puneri Paltan, Tamil Thalaivas, Telugu Titans,
  U Mumba, UP Yoddhas, Bengal Warriors, Gujarat Giants
```

---

## Understanding the Game

Kabaddi alternates between raiding (attacking) and defending phases. Each team
sends a raider into the opponent's court while 7 defenders try to stop them returning.

```
RAID:
  Raider enters opposition half
  Tags one or more defenders (touch points) and returns safely:
    1 touch = 1 point | 2 touches = 2 points | 3+ touches = 3 points
    If raider crosses the baulk line alone (no touch): must score or be tackled
  
  Raider tackled (stopped from returning): 1 point to defending team
  
SUPER RAID:
  Raider scores 3+ points in a single raid (touches 3+ defenders)
  Rare and high-impact — momentum shift event
  
ALL OUT:
  When all 7 defenders are eliminated (touchouts) in a set:
  Attacking team scores bonus points = number of players still in
  All out = typically +5 to +7 point swing; most decisive single event in kabaddi
  
TACKLE:
  Defenders stop raider from returning: 1 point to defenders
  Super tackle: only 3 defenders on court and they stop the raider = 2 points
```

---

## The Raider — kabaddi's dominant individual

The raider is the most critical individual position in kabaddi — the closest equivalent
to a quarterback in NFL or halfback in rugby league.

```
RAIDER QUALITY METRICS:
  Raid points per match: Elite 10+ | Good 8–9 | Average 6–7 | Poor < 5
  Raid strike rate: (successful raids / total raids) Elite 55%+ | Good 48%+
  Super raid rate: (raids with 3+ points) Elite 8%+ | Good 5%+
  
  HIGH-PROFILE RAIDERS (PKL history):
    Consistent elite raiders: Pardeep Narwal, Pawan Sehrawat, Rahul Chaudhari
    High-value auction picks signal team investment in the raid department
    
RAIDER INJURY / ABSENCE:
  Star raider out: × 0.72 on expected offensive output
  Team with no quality backup raider: × 0.62 (structural crisis)
  
  Note: Unlike most sports, many PKL teams rely on a single dominant raider.
  This creates high variance when that player is absent.
  
  SUPER 10:
    Raider scores 10+ raid points in a single match: Super 10 milestone
    Players chasing Super 10 milestones show elevated motivation
    Check: is the match a personal milestone opportunity for the star raider?
```

---

## The Defender — "Do or Die" tackle situations

```
DEFENDER QUALITY METRICS:
  Tackle points per match: Elite 4+ | Good 3+ | Average 2+
  Tackle strike rate: (successful tackles / total tackle attempts) Elite 60%+
  Super tackle rate: Elite 15%+ | Good 10%+
  
  HIGH FIVE:
    Defender scores 5+ tackle points in a single match: High Five milestone
    Elite defenders: Saurabh Nandal, Fazel Atrachali, Surender Nada
    
DEFENSIVE UNIT STRENGTH:
  Corners and covers (wide and central defensive positions) must coordinate
  Left corner + right corner + cover: the defensive trio
  Loss of any two of these three: × 0.80 on defensive output
  
TACKLE STRATEGY TYPES:
  Ankle hold: grab raider's ankle at return line — most common
  Chain tackle: multiple defenders in coordinated hold
  Waist hold: high risk, high reward
  
  Teams with diverse tackle strategies are harder to predict (and harder to raid against)
```

---

## All Out — the Game-Changing Event

```
ALL OUT PROBABILITY ASSESSMENT:
  All out occurs when all 7 defenders (or all 6 players still in) are eliminated
  
  PRE-ALL OUT SIGNALS:
    Team has 3 or fewer players left: all out probability elevated
    Opposition raider is in super form (3 consecutive successful raids): danger
    Team on defensive fatigue (3rd quarter, high raid frequency against them)
    
  ALL OUT IMPACT ON MOMENTUM:
    All out swings momentum decisively to raiding team
    Typically worth +5 to +8 point swing in the period following
    Second consecutive all out in same half: near-certain win signal
    
  AGENT RULE: In close matches (within 5 points in second half), all out
  probability is the highest-variance event. Track player count on court
  as a leading indicator.
```

---

## Home Ground Advantage — PKL

```
HOME ADVANTAGE:
  PKL plays in a round-robin home/away format at designated city arenas
  Home team win rate: ~55–58% (moderate; lower than European football)
  
  CROWD IMPACT:
    Passionate home support for city franchises
    Notable home crowd venues: Patna (Patna Pirates), Delhi (Dabang Delhi)
    
  HOME/AWAY SPLITS MATTER LESS THAN PLAYER FORM IN PKL:
    The individual star raider effect dominates home advantage in most matches
    Unless the crowd impact is extreme, form and squad quality are primary inputs
    
  NEUTRAL VENUE (playoffs in PKL):
    Playoffs typically played at a single pre-selected venue
    Neither team has systematic home advantage — form and squad quality primary
```

---

## Auction and Squad Building

The PKL operates an annual player auction that is a significant intelligence event:

```
PKL AUCTION SIGNALS:
  High auction price for a player: team commits significant resources
  Most expensive players are typically elite raiders
  Check: did the team retain their star raider, or are they rebuilding?
  
  SQUAD BALANCE:
    All-round squad (balanced raid and defence): more consistent
    Raid-heavy squad (expensive raider, cheap defence): high ceiling, high floor risk
    Defence-heavy squad: lower scoring but more resilient to raider injuries
    
  NEW TEAM (expansion or major rebuild):
    High auction squad + new coach: Tier 3 prediction confidence
    Retained core + targeted additions: more predictable
```

---

## Event Playbooks

### Playbook 1: Star Raider vs Weak Defence
```
trigger:  Elite raider (10+ raid points average) faces team ranked bottom-3 in defence
entry:    Pre-match (after team lineups confirmed)
exit:     Match completion
filter:   Star raider confirmed playing (no injury concern)
          Opponent has not specifically prepared a raider-specific defence
sizing:   1.15× — raider vs defence mismatch is the clearest signal in kabaddi
note:     Kabaddi is more individual-dominant than any other team sport in this
          library. One exceptional raider can carry a team to victory.
```

### Playbook 2: PKL Final — Star Raider Milestone Match
```
trigger:  PKL Final; star raider approaching season milestone (Super 10 record etc)
entry:    Week of final (narrative building)
exit:     24h post-final
filter:   Token/fan engagement in Indian sports market is active
          Star raider's team is in the final (confirmed)
sizing:   1.25× — PKL Final is the highest domestic kabaddi event
```

### Playbook 3: Eliminator — Lower Seed Momentum
```
trigger:  6th-seeded team enters eliminator on 3+ match winning streak
entry:    Pre-eliminator match
exit:     Match completion
filter:   Top-seeded team in semi-final has played more matches (fatigue)
          Underdog has momentum and quality star raider
sizing:   0.90× — meaningful upset signal but playoffs are unpredictable
```

---

## Result Impact Matrix

| Result / Event | Signal impact |
|---|---|
| PKL match win (regular season) | +3–6% |
| PKL Playoff qualification | +8–15% |
| PKL Final win (championship) | +25–45% |
| Star raider records Super 10 | +5–10% same-day social signal |
| Star raider injury (season-ending) | -20–35% |
| Star raider transfer between teams | Significant fan token portability signal |

---

## Signal Weight Adjustments

| Component | Weight | Rationale |
|---|---|---|
| Sports catalyst | 35% | Match results and individual performance dominant |
| Social sentiment | 30% | Extremely high social media engagement in India |
| Market / whale | 15% | Indian sports market developing; lower institutional |
| Price trend | 15% | Season narrative builds across 22 league matches |
| Macro | 5% | Minimal direct macro correlation |

---

## Agent Reasoning Prompts

```
1. STAR RAIDER IS THE PRIMARY INPUT. Confirm the star raider is playing
   before any prediction. Their absence changes the team's expected points
   by more than any other variable in the sport.

2. PKL IS AN INDIVIDUAL-DOMINANT SPORT. The best raider in a match
   often determines the result regardless of team quality differentials.
   Track the raider matchup above team-level analysis.

3. SOCIAL SENTIMENT IS HIGHER HERE than any other sport in the library.
   Indian kabaddi fandom is intense, young, and mobile-first. The
   social component deserves 30% weight — higher than any other sport.

4. ALL OUT PROBABILITY in second half of close matches is the most
   important live variable. Track player count on court as a leading
   indicator when the match is within 5 points.

5. AUCTION RESULTS shape the entire season. A team that lost their
   star raider at auction starts the season structurally weaker
   regardless of their previous year's performance.

6. NEUTRAL VENUE PLAYOFFS: Remove home advantage modifier for all
   PKL playoff predictions. Both teams play on neutral ground.
```

---

## Fan Token™ Notes

No active kabaddi fan token on Chiliz as of Q1 2026. The Indian market represents
one of the highest-priority token expansion opportunities globally given: audience
size (300–400M PKL viewers), young demographic, mobile-first engagement, and India's
existing crypto-adjacent culture. PKL franchise tokens (Patna Pirates, Jaipur Pink
Panthers, Dabang Delhi) would be the natural launch candidates.

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` for the full framework.
Kabaddi-specific notes:
- Contact injuries are endemic: ankle, knee, shoulder from tackling and tag attempts
- Star raider injury is categorically more impactful than any other player injury
- PKL season is 4 months — accumulated contact leads to managed injuries by playoffs

## Data Sources

- **PKL official (prokabaddi.com)**: Match results, squad lists, standings
- **Kabaddi Adda**: News, player statistics, match previews
- **Sports18 / Star Sports**: Broadcast statistics and match analysis
- **Cricbuzz / ESPNcricinfo kabaddi section**: PKL coverage
- **Player auction results**: Annual PKL auction data

## Key Commands

| Action | Skill | Notes |
|---|---|---|
| Pre-match signal | Load this file + `core/sportmind-score.md` | Raider primacy modifier applies |
| Star raider absent | `core/breaking-news-intelligence.md` | Category 2 — apply ×0.78 |
| PKL Final / Eliminator | Playbook 2 or 3 | High-stakes modifier active |
| All Out event | `## All Out — the Game-Changing Event` | Score reset signal |
| Auction intelligence | `## Auction and Squad Building` | Pre-season team strength signal |

---

## Compatibility

**Injury intelligence:** `core/injury-intelligence/core-injury-intelligence.md`

---

*MIT License · SportMind · sportmind.dev*

### Playbook 4: PKL rivalry match (top-tier teams, home crowd)
```
trigger:  Pro Kabaddi League match between top-3 teams with significant home support
entry:    Day of match once lineup confirmed (rosters announced ~2h before)
exit:     Match completion — kabaddi is rapid; no half-time repositioning needed
filter:   Star raider confirmed fit and starting; check team's home venue record;
          load recent form (last 4 PKL matches)
sizing:   1.1× standard — PKL home advantage is among the strongest in league sport
note:     Home crowd in PKL creates measurable raider confidence effect.
          Patna Pirates, Jaipur Pink Panthers, U Mumba home records are significantly
          above neutral. Star raider presence is the non-negotiable entry condition.
```
