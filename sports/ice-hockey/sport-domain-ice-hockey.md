# Ice Hockey (NHL) — SportMind Domain Skill

Sport-specific intelligence for ice hockey. Primarily covers the NHL (National Hockey
League) — the world's premier professional ice hockey competition. Also applicable to
international competitions (IIHF World Championship, Winter Olympics) and major European
leagues (SHL, Liiga, KHL, DEL).

---

## Overview

Ice hockey is one of the fastest team sports in the world. Unlike most sports, the game
is played on a surface that amplifies speed, making the difference between elite and
average athletes more physically pronounced than in field sports. The goaltender is the
single most critical positional player in any team sport — their save percentage variance
explains more game-level outcome variation than any other individual-level variable.

The NHL operates a gruelling 82-game regular season followed by four rounds of playoffs
(best-of-7 series). This structure creates a specific intelligence pattern: regular season
results are primarily useful for establishing team quality trends and playoff seeding;
the playoffs represent a fundamentally different competition where goaltending, defensive
structure, and special teams dominate over regular season offensive skill.

---

## Domain Model

### Season Calendar

| Phase | Dates (approx) | Signal character |
|---|---|---|
| Pre-season | Sep | Roster information; limited prediction value |
| Regular season | Oct–Apr | 82 games; trend establishment; standings race |
| Trade Deadline | Mar | Roster construction signal — deadline deals |
| Wild Card race (final month) | Mar–Apr | Elevated stakes; motivation signal |
| First Round Playoffs (R1) | Apr–May | Best-of-7; seeding advantage matters |
| Second Round (R2) | May | Best-of-7; fatigue and depth exposed |
| Conference Finals (R3) | May–Jun | Best-of-7; elite teams only |
| Stanley Cup Final | Jun | Best-of-7; maximum stakes |

### League Structure

```
EASTERN CONFERENCE:              WESTERN CONFERENCE:
  Atlantic Division (8 teams)      Central Division (8 teams)
  Metropolitan Division (8 teams)  Pacific Division (8 teams)

PLAYOFF FORMAT:
  16 teams qualify (top 3 per division + 2 wildcards per conference)
  Four rounds of best-of-7 series
  Home ice advantage: higher seed plays Games 1, 2, 5, 7 at home

POINTS SYSTEM (regular season):
  Win: 2 points | OT/SO loss: 1 point | Regulation loss: 0 points
  
  KEY INSIGHT: The overtime/shootout point system means a team can lose
  7 games in a row and still have a .500 record if all losses are in OT.
  Points percentage (not win-loss) is the correct regular season metric.
```

---

## The Goaltender — ice hockey's defining variable

No position in any team sport has more outcome determination than the NHL goaltender.
A hot goaltender in a playoff series can carry an average team to the Stanley Cup.
A struggling goaltender can eliminate a championship favourite. This is the first
and most important assessment in any ice hockey intelligence workflow.

### Goaltender quality metrics

```
SAVE PERCENTAGE (SV%):
  All situations: Elite .920+ | Good .910+ | Average .900+ | Poor < .895
  Even strength: More predictive than overall SV% (removes special teams noise)
  High-danger SV%: Best predictor of true goaltender quality
  
  CONTEXT MATTERS:
    A .920 SV% on a shot-suppressing defensive team ≠ a .920 on a leaky defensive team
    Always check shots against rate alongside SV%
    
GSAx (Goals Saved Above Expected):
  Best single metric — accounts for shot quality, not just shot quantity
  Elite: +15 per season | Good: +5 to +15 | Average: -5 to +5 | Poor: < -5
  
  GSAx > 0 = goaltender performing ABOVE expectations
  GSAx < 0 = goaltender a liability even if raw SV% looks passable

GOALS AGAINST AVERAGE (GAA):
  Less useful than SV% (team-dependent) but directionally informative
  Elite < 2.20 | Good < 2.60 | Average < 3.00 | Poor > 3.20
```

### Goaltender starter confirmation

```
STARTER IDENTIFICATION:
  Teams rarely announce starters publicly before game day
  Primary signals for who starts:
    1. Morning skate participation — starter typically skates in full gear last
    2. Beat reporter confirmation (fastest and most reliable source)
    3. Starting goaltender lines in betting markets (often known by afternoon)
    4. Head coach comments at morning media availability
    
  BACK-TO-BACK GAMES:
    Teams rarely start their #1 goaltender in both games of a back-to-back
    Backup goaltender starting in game 2 of B2B is the default assumption
    Exception: playoff-seeding critical games in final weeks of season
    
    BACK-TO-BACK MODIFIER:
      Backup goaltender starting vs opponent with quality starter: × 0.75 for team
      Even if backup is quality — rest of team is also on B2B (fatigue factor)
      
GOALTENDER INJURY / ILLNESS:
  Most impactful single injury event in any team sport
  Emergency backup (EBUG — Emergency Backup Goaltender): extreme negative signal
    → Team signs an amateur or minor leaguer to dress as backup
    → Primary goaltender clearly not available and #2 is also compromised
    → Apply × 0.55 if EBUG is confirmed active (not just dressed)
```

---

## Special Teams — the highest-leverage situation

Power plays and penalty kills account for a disproportionate share of NHL outcomes.
A team that is excellent on the power play and penalty kill wins close games at a
higher rate regardless of 5-on-5 play quality.

```
POWER PLAY (PP%) — scoring on man advantages:
  Elite 25%+ | Good 20%+ | Average 18%+ | Poor < 15%

PENALTY KILL (PK%) — defending shorthanded:
  Elite 83%+ | Good 80%+ | Average 78%+ | Poor < 75%

COMBINED SPECIAL TEAMS INDEX (STI):
  STI = PP% + PK%
  Elite 105%+ | Strong 100%+ | Average 97%+ | Weak < 95%
  
PENALTY DIFFERENTIAL:
  Teams that draw more penalties than they take have structural advantage
  Disciplined teams (low penalty minutes) have PK advantage by taking fewer
  Undisciplined teams (high PIM) give up more power plays — significant weakness
  
AGENT RULE: In any game where both teams have comparable 5-on-5 quality,
the special teams matchup often determines the result. Always check PP% vs PK%
of the opposing team as a primary pre-game input.
```

---

## Line Matching and Deployment

NHL coaches actively deploy lines to create favourable matchups. Unlike most sports,
this creates a predictable and researchable tactical variable.

```
LINE DEPLOYMENT:
  4 forward lines (3 forwards each) + 3 defensive pairs
  Top line: highest-skilled offensive forwards
  Fourth line: physical / energy / defensive role
  Top defensive pair: used against opposition's top line
  
  Coaches deploy specific lines in specific situations:
    Offensive zone faceoff → offensive line deployed
    Defensive zone → checking line + top defensive pair
    Power play → specialist unit (often different from even-strength top line)
    Penalty kill → specialist PK unit
    
MATCHUP EXPLOITATION:
  When a team's top line faces the opponent's 3rd defensive pair → significant mismatch
  This happens when:
    - Team with home ice can choose last in line matching
    - Opponent has injuries to top defensive pair
    
HOME ICE ADVANTAGE IN LINE MATCHING:
  Home team can put their preferred line on ice LAST in each zone draw
  This is a structural home advantage unique to hockey
  Strong home teams with deep top lines exploit this consistently
```

---

## Competition Tier Classification

**Tier 1 — Maximum signal:**
- Stanley Cup Final
- Conference Finals (Eastern / Western)
- Playoffs in general (all rounds significantly elevated vs regular season)
- Winter Olympics (national team; every 4 years when NHL participates)

**Tier 2:**
- Regular season divisional rivalries (heightened stakes)
- Trade deadline week (roster change signals)
- Wild card race (final 10 games of regular season for bubble teams)
- IIHF World Championship (when NHL players participate post-season)

**Tier 3:**
- Standard regular season games
- Pre-season

---

## Event Playbooks

### Playbook 1: Confirmed #1 Goaltender vs Backup
```
trigger:  Starting goaltender confirmed for both teams; significant quality mismatch
entry:    Post-morning skate confirmation
exit:     Game completion
filter:   #1 goaltender confirmed (not B2B/rest situation)
          Opponent confirmed starting backup (injury, B2B, or load management)
          Quality gap: GSAx difference > 10 per season
sizing:   1.25× — goaltender quality is the strongest single-game signal in hockey
note:     Starter confirmation is the LAST step, not the first. Assess line quality,
          special teams, and recent form first — then confirm with starter identity.
```

### Playbook 2: Playoff Series — Goaltender Runs Hot
```
trigger:  Goaltender records 3+ consecutive above-average playoff performances
          (SV% .930+ in each game, high-danger SV% elite)
entry:    Start of next series (momentum into next round)
exit:     First sub-.900 performance or series end
filter:   Team has legitimate defensive structure supporting the goaltender
          Not facing an extreme offensive team (which will eventually break hot streaks)
sizing:   1.10× — hot playoff goaltenders are among the most sustained signals in sport
note:     A goaltender on a playoff run is the closest thing to a persistent
          momentum signal in any sport in this library. It is not luck — it is
          confidence, timing, and defensive structure combining.
```

### Playbook 3: Special Teams Mismatch
```
trigger:  Clear PP%/PK% mismatch (one team STI 103+, opponent STI < 97)
entry:    Pre-game
exit:     Game completion
filter:   Both teams have similar 5-on-5 shot quality (close regular season matchup)
          No significant starter quality mismatch (which would override this)
sizing:   1.0× — secondary signal; best as confirming factor
note:     Special teams advantage matters most in close games. In mismatches
          (clear favourite), it is a secondary signal. In toss-ups, it can be decisive.
```

### Playbook 4: Back-to-Back — Backup Goaltender Starting
```
trigger:  Team on second game of back-to-back (confirmed backup starting)
entry:    Post-morning skate confirmation of starter
exit:     Game completion
filter:   Opponent starting their #1 goaltender (fresh)
          Backup quality gap meaningful (GSAx difference)
sizing:   1.10× for opponent — elevated confidence on opposing team
note:     B2B backup starts are the most predictable quality degradation event
          in the NHL regular season. They occur ~80-90 times per season league-wide
          and are consistently exploitable.
```

---

## Result Impact Matrix

| Result / Event | Signal impact |
|---|---|
| Playoff series win (any round) | +8–20% (scales with round) |
| Stanley Cup win | +25–50% |
| Regular season win (standard) | Low — 1 of 82 |
| Top goaltender injured (IR) | -15–30% immediate |
| Elite goaltender acquired (trade) | +10–20% |
| Back-to-back backup starting | Opponent +8–15% |
| Power play specialist acquired | +5–10% |

---

## Sport-Specific Risk Variables

**Goaltender hot/cold streaks** — More pronounced than any other sport. A goaltender
in the zone can stop 95%+ of shots for weeks; a cold streak can be .880 level. Unlike
field sport form, this can flip within a single game.

**Puck luck** — Ice hockey has the highest inherent variance of any major team sport.
Expected goals models suggest a .500 team wins any given game at ~50–55% regardless
of quality differentials. Short series are genuinely noisy. The best team wins a
7-game series approximately 60–65% of the time — significantly lower than public perception.

**Injuries and the IR** — The NHL Injured Reserve is the primary injury signal.
Unlike NFL, teams do not disclose injury details (just "upper body" or "lower body").
This creates information asymmetry that sharp bettors exploit via morning skate observation.

---

## Signal Weight Adjustments

| Component | Weight | Rationale |
|---|---|---|
| Sports catalyst | 35% | Game results and matchup quality dominant |
| Market / whale | 25% | Sharp hockey betting community; informed money |
| Social sentiment | 15% | Passionate fan base; regional concentration |
| Price trend | 20% | Playoff runs create sustained momentum signals |
| Macro | 5% | Minimal |

---

## Agent Reasoning Prompts

```
1. CONFIRM GOALTENDER STARTER FIRST. Everything else is secondary.
   Never finalise an ice hockey prediction without knowing who starts in goal.

2. CHECK BACK-TO-BACK STATUS. If a team played last night, assume backup
   goaltender until proven otherwise. This is one of the most reliable
   regular season edges in professional hockey.

3. SPECIAL TEAMS MATCHUP. In close games, PP% vs PK% often determines
   the result more than 5-on-5 quality. Always check before any game.

4. PLAYOFF HOCKEY IS DIFFERENT. Regular season offensive skill compresses.
   Goaltending, defensive structure, and team depth determine outcomes.
   Do not apply regular season offensive metrics directly to playoff predictions.

5. HOME ICE LINE MATCHING. The home team has structural line deployment
   advantage. This matters most when one team has a dominant top line
   and the other has weak defensive pairs.

6. PUCK LUCK IS REAL. The single noisiest major sport in the library.
   Never overconfide in any single-game ice hockey prediction.
   Even the best teams lose 30+ games in a season.
```

---

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` for the full framework.
Ice hockey-specific notes:
- NHL teams disclose only "upper body" or "lower body" injury — never specific diagnosis
- Morning skate observation is the primary injury detection signal
- Goaltender injury is categorically more impactful than any skater injury
- Concussion protocol: player removed immediately; return timeline unpredictable


---

## Key Commands

| Action | Skill | When to use |
|---|---|---|
| Domain intelligence | `sports/ice-hockey/sport-domain-ice-hockey.md` | Every analysis |
| Athlete modifier | `athlete/nhl/` | After domain load |
| Injury check | `core/injury-intelligence/core-injury-intelligence.md` | Injury concern |
| Market context | `market/market-ice-hockey.md` | Commercial decisions |

## Data Sources

- **Official:** NHL.com
- **Advanced:** Natural Stat Trick (naturalstattrick.com), MoneyPuck (moneypuck.com)
- **Historical:** Hockey Reference (hockey-reference.com)
- **Odds and prediction:** Betfair Exchange, Oddschecker

## Compatibility

**Athlete intelligence:** `athlete/nhl/athlete-intel-nhl.md`
**Injury intelligence:** `core/injury-intelligence/core-injury-intelligence.md`

---

*MIT License · SportMind · sportmind.dev*
