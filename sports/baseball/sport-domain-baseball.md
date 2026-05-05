# Baseball (MLB) — SportMind Domain Skill

Sport-specific intelligence for Major League Baseball. Covers the MLB regular season,
playoffs, and World Series. Also applicable to NPB (Japan), KBO (Korea), and international
competitions (WBC — World Baseball Classic).

---

## Why baseball in SportMind

Baseball currently has no active fan token on Chiliz. It is included in SportMind because:

1. **The library serves all sports AI agents** — prediction markets, fantasy baseball,
   analytics tools, and sports betting agents all benefit from structured baseball intelligence
2. **North American host market** — the 2026 FIFA World Cup hosts (USA, Canada, Mexico) are
   all major baseball markets; any expansion of fan token infrastructure in North America
   will likely include MLB teams
3. **The richest data suite in sport** — Statcast provides pitch-by-pitch tracking data
   for every MLB game; no sport has deeper publicly accessible performance data
4. **Token readiness** — MLB franchises have some of the most valuable sports brands globally
   (Yankees, Dodgers, Red Sox, Cubs); if MLB tokens launch, this skill is ready

---

## Overview

Baseball is a sport of **matchups, states, and accumulation**. Unlike most team sports where
form and momentum carry through continuous play, baseball resets with every pitch. The batter
vs pitcher matchup in each plate appearance is the fundamental unit of analysis — not the team,
not the inning, not the score. Agents that understand this matchup-first structure make
significantly better predictions than those applying generic team-level logic.

The 162-game regular season creates the deepest statistical sample in professional sport.
Sample size is rarely a concern after June. The playoffs, however, collapse all of that
to 5- and 7-game series where pitching matchups and bullpen management determine outcomes
far more than regular season form.

---

## Domain Model

### Season Calendar

| Phase | Dates (approx) | Signal character |
|---|---|---|
| Spring Training | Feb–Mar | Information only; no prediction value |
| Opening Day | late Mar/early Apr | First real signal; rotation revealed |
| April–May (early season) | Apr–May | High variance; small samples; caution |
| June–July (mid-season) | Jun–Jul | Statistical stability; form meaningful |
| Trade Deadline | 31 July | Roster construction signal; team direction |
| August–September | Aug–Sep | Playoff races; expanded rosters (Sep 1) |
| Wild Card Series | early Oct | Best-of-3; high variance; home field critical |
| Division Series (ALDS/NLDS) | Oct | Best-of-5; pitching matchup critical |
| Championship Series (ALCS/NLCS) | Oct | Best-of-7; team depth exposed |
| World Series | Oct–Nov | Best-of-7; maximum stakes |

**Agent rule:** Do not make strong predictions before June — sample sizes are too small.
The sweet spot for statistical reliability is July onwards, once ~90 games have been played.

### League Structure

```
AMERICAN LEAGUE (AL):               NATIONAL LEAGUE (NL):
  AL East: NYY, BOS, TBR, TOR, BAL    NL East: ATL, PHI, NYM, MIA, WSN
  AL Central: MIN, CLE, CHW, KCR, DET NL Central: MIL, CHC, STL, PIT, CIN
  AL West: HOU, LAA, SEA, OAK, TEX    NL West: LAD, SFG, ARI, SDP, COL

DESIGNATED HITTER (DH): Both leagues use DH — pitcher does not bat.
This is relevant because pitching substitution patterns differ from historical NL.

PLAYOFF FORMAT:
  Wild Card: 3 teams per league (best-of-3 series, home team hosts all games)
  Division Series: 4 teams per league (best-of-5, 2-2-1 format)
  Championship Series: 2 teams per league (best-of-7, 2-3-2 format)
  World Series: AL champion vs NL champion (best-of-7, 2-3-2 format)
```

---

## The Pitcher — baseball's dominant variable

In no other team sport does a single player determine so much of the outcome. The
starting pitcher touches every offensive plate appearance for 5–7 innings. Their ERA,
quality of stuff, and matchup vs the opposing lineup is the primary prediction input.

### Starting Pitcher Assessment

```
CORE METRICS FOR STARTING PITCHERS:

ERA (Earned Run Average): 
  Runs allowed per 9 innings — basic but context-dependent
  Elite < 2.50 | Good < 3.50 | Average < 4.50 | Poor > 5.00
  
FIP (Fielding Independent Pitching):
  ERA-equivalent based only on K, BB, HR — removes defense and luck
  Better predictor of future performance than ERA
  Elite < 2.80 | Good < 3.50 | Average < 4.20
  
xFIP (Expected FIP):
  Normalises home run rate to league average — removes HR luck
  Most predictive single-game metric for starter quality
  
WHIP (Walks + Hits per Inning):
  Baserunner generation. Elite < 1.00 | Good < 1.20 | Average < 1.35
  
K% (Strikeout rate):
  Elite 28%+ | Good 22%+ | Average 18%+
  High K% = less reliance on defense; more predictable
  
BB% (Walk rate):
  Elite < 5% | Good < 7% | Average < 9%
  High walk rate = danger — free baserunners
  
Spin rate / pitch movement (Statcast):
  High spin rate on fastball = more movement and life
  Elite horizontal break on slider = high whiff rate
```

### Pitcher types — distinct prediction profiles

```
POWER PITCHER (fastball-dominant, high strikeout):
  High K%, high velocity (95mph+), predictable performance arc
  Weather impact: minimal (strikeouts not affected by conditions)
  Platoon splits: check if fastball works equally vs LHB and RHB
  
FINESSE PITCHER (command-dependent, movement-based):
  Lower K%, relies on weak contact and ground balls
  Weather impact: moderate (movement is wind-affected)
  Ballpark impact: significant (spacious parks favour finesse)
  Most sensitive to hot lineups — if batters are timing up, trouble
  
GROUND BALL PITCHER:
  Induces weak contact on ground; depends on infield defense
  Key metric: GB% (Ground ball rate). Elite 55%+ | Good 50%+
  Best in spacious parks; bad on turf (ball moves faster)
  
FLY BALL PITCHER:
  Induces pop-ups and fly outs; depends on outfield defense
  High risk in homer-friendly parks (Fenway, Coors, Great American)
  Key metric: HR/FB rate (home runs per fly ball hit)
  
OPENER / BULK PITCHER (modern):
  Opener pitches 1–2 innings first; bulk reliever follows
  Creates lineup matchup advantages vs power-batting orders
  Complicates standard prediction — no traditional starter assessment
```

### The Lineup Order Effect

Starting pitchers face the batting order multiple times. Performance degrades with each pass:

```
TIMES THROUGH ORDER PENALTY (TTOP):

First time through (batters 1-9):    Pitcher at full effectiveness
Second time through (batters 1-9):   -0.20 ERA equivalent degradation
Third time through (batters 1-9):    -0.55 ERA equivalent degradation
                                      (this is when most managers pull starter)

Agent rule: A starter with a high TTOP penalty (performs much worse 3rd time through)
should be assessed as effectively a 5-inning pitcher, not a 7-inning pitcher.
Many modern teams pull starters intentionally before the 3rd pass.
```

---

## The Bullpen — the modern game's critical variable

Baseball has fundamentally changed. The complete game starter is rare. Modern teams
use 3–6 relievers per game. Bullpen quality is as important as starter quality.

```
BULLPEN ASSESSMENT:

Team ERA (relief):
  Elite < 3.00 | Good < 3.50 | Average < 4.20

High-leverage reliever quality:
  The closer and 7th/8th inning specialists face highest-stakes situations
  SIERA (Skill-Interactive ERA) for relievers: most reliable metric
  
Bullpen availability (key variable):
  Yesterday's starter used 115+ pitches = likely unavailable today
  Closer used last 2 consecutive days = likely unavailable or limited
  
  BULLPEN FATIGUE FLAGS:
    Closer: unavailable after 2 straight days or 30+ pitches in last appearance
    Setup relievers: monitor usage; 4 appearances in 5 days = fatigue risk
    Bulk reliever: typically fresh regardless of team usage

SAVE SITUATION CONTEXT:
  Closing situation (3-run lead or less, 9th inning): elite closer enters
  Non-save situation: teams often use inferior relievers to protect elite arms
  This creates asymmetric quality — late-game defence is highest quality
```

---

## Batter vs Pitcher Matchups

The most granular and most predictive unit in baseball. Every plate appearance between
a specific batter and a specific pitcher has trackable historical data.

```
B/P MATCHUP ASSESSMENT:

Sample size threshold:
  < 10 plate appearances (PA): ignore historical H2H entirely
  10–25 PA: slight signal; don't overweight
  25–50 PA: meaningful signal; apply moderate weight
  50+ PA: strong signal; historical H2H is predictive

Platoon advantage (handedness):
  Right-handed pitcher vs Left-handed batter: LHB has platoon advantage
  Left-handed pitcher vs Right-handed batter: RHB has platoon advantage
  
  Platoon splits (typical): .020–.030 OPS advantage for favoured side
  Some players have extreme platoon splits (check before any single game prediction)

STATCAST MATCHUP SIGNALS:
  Does pitcher's best pitch match batter's weakness?
    High breaking ball — does batter chase below the zone?
    Inside fastball — does batter have low xBA on inside pitch?
  
  Exit velocity allowed vs batter's typical exit velocity:
    If pitcher's allowed EV is above batter's typical EV = batter may be overmatched
    
Lineup stacking:
  Same-handed batters vs pitcher with extreme platoon split:
    5+ left-handed batters vs a pitcher with .300+ OPS split vs lefties = stack exploit
```

---

## Ballpark Intelligence — the Coors Field problem

No other sport has the venue variability of baseball. The field dimensions, altitude,
humidity, and playing surface materially affect outcomes.

```
PARK FACTOR CLASSIFICATION:

HITTER'S PARKS (above-average run environment):
  Coors Field (Colorado): extreme — altitude reduces pitch movement dramatically
                           All pitching statistics at Coors must be heavily discounted
                           Even elite pitchers allow 15–25% more runs at Coors
  Great American Ballpark (Cincinnati): homer-friendly
  Fenway Park (Boston): Green Monster boosts doubles significantly
  Yankee Stadium: short right field porch amplifies left-handed power
  
PITCHER'S PARKS (below-average run environment):
  Oracle Park (San Francisco): marine layer; cold air; suppresses home runs
  Petco Park (San Diego): spacious; marine layer
  Dodger Stadium: pitcher-friendly; consistent conditions
  Target Field (Minnesota): large outfield gaps
  
NEUTRAL PARKS: Most others — use standard prediction without adjustment

PARK FACTOR APPLICATION:
  Always adjust ERA and offensive statistics for home vs away context
  A pitcher with 3.80 ERA at Coors is better than their number shows
  A pitcher with 3.80 ERA at Petco may be mediocre
```

### Weather at outdoor stadiums

```
WIND DIRECTION:
  Blowing out (toward outfield): +15–20% home run probability increase
  Blowing in (toward infield): -15–20% home run probability decrease
  Crosswind: minimal direct effect on run environment
  
TEMPERATURE:
  Cold (below 50°F / 10°C): ball doesn't carry as far; pitcher-friendly
  Hot (above 85°F / 29°C): ball carries further; hitter-friendly
  
HUMIDITY:
  High humidity: ball doesn't carry as far (contrary to common belief)
  Low humidity (dry heat): ball carries further — Coors field effect
  
RAIN:
  Game delay risk; check forecast for potential postponement
  5-inning rule: official game after 5 innings; betting implications
  Wet baseball: more grip issues; pitchers may lose command; wild pitches increase
```

---

## The Rotation Cycle

Starting pitchers pitch every 5th day. Rotation management is a predictable intelligence signal.

```
ROTATION TRACKING:

Standard rotation order:
  Ace (#1) → Second starter (#2) → Third (#3) → Fourth (#4) → Fifth (#5) → Ace again
  
  Knowing who pitches next is public information. Track the rotation.
  
REST DAYS:
  Extra rest (6+ days): may improve or may disrupt rhythm — mixed signal
  Short rest (3–4 days): significant performance decline; playoffs only
    Short rest performance: ERA increases by ~1.20 on average
  
ROTATION DISRUPTIONS (signal events):
  Starter skipped: injury concern or mechanical issue; flag for monitoring
  Opener used instead of rotation starter: bullpen-driven strategy day
  Relief day (no starter planned): heavy bullpen usage day; team conserving starter
  
PLAYOFF PITCHING ADJUSTMENTS:
  Teams compress rotation in playoffs (Ace → #2 → Ace → #2)
  Starters often used in relief in elimination games
  Bullpen usage increases dramatically in playoffs
```

---

## Event Playbooks

### Playbook 1: Ace vs Weak Rotation Spot
```
trigger:  Team's ace (ERA < 3.00, xFIP < 3.20) faces opposition's 4th or 5th starter
entry:    Morning of game (after lineup and rotation confirmed)
exit:     Game completion
filter:   Ace has 4+ days rest (not on short rest)
          Opposing lineup not stacked with same-handed batters vs ace's platoon split
          Neutral or pitcher-friendly park (avoid Coors-equivalent)
sizing:   1.25× — quality pitching mismatch is the highest-conviction single-game
          signal in baseball
note:     Ace starts are the most predictable positive signals in baseball.
          The key variable is the bullpen after the ace exits.
```

### Playbook 2: Bullpen Game (Opener Strategy)
```
trigger:  Team announces opener for a game (1-2 inning starter, then bulk reliever)
entry:    After opener identity is confirmed
exit:     Game completion
filter:   Assess opposing team's platoon matchups vs likely bulk reliever
          Identify if opener strategy creates platoon advantage
sizing:   0.85× — higher variance; harder to predict 7 innings of bullpen use
note:     Opener strategies are often employed against power-batting lineups.
          The bulk reliever's platoon split vs the opposing order is the key variable.
```

### Playbook 3: Playoff Series — Game 1 Starting Pitching
```
trigger:  First game of any playoff series
entry:    Morning of Game 1 (rotation confirmed)
exit:     After Game 1 result
filter:   Identify each team's ace for Game 1
          Check rest days (both starters)
          Check home field advantage
sizing:   1.0× — playoff series are individual game analyses, not season trend
note:     Playoff series are decided by pitching, not regular season form.
          A team that scores 5+ runs per game in the regular season may score 2–3
          when facing playoff-calibre starters. Re-calibrate all offensive expectations.
```

### Playbook 4: Trade Deadline Acquisition
```
trigger:  Team acquires starting pitcher or elite reliever at trade deadline (July 31)
entry:    First home start post-acquisition (crowd familiarity factor)
exit:     3 starts post-acquisition (assess integration)
filter:   Pitcher ERA sub-3.50 at previous team
          Acquiring team has playoff contention (motivation intact)
sizing:   0.90× — adjustment period; new environment
note:     The trade deadline is the biggest mid-season signal in baseball.
          Elite arms acquired before the deadline demonstrably improve team outcomes
          in August-September. The first start post-trade carries adjustment uncertainty.
```

---

## Result Impact Matrix

| Result / Event | Signal impact |
|---|---|
| Regular season win (standard) | Low — 1 of 162; never overweight |
| Winning streak (7+ games) | Elevated form signal; starter rotation healthy |
| Division clinch | Milestone narrative; rotation rested for playoffs |
| Wild Card Series win (sweep) | +significant — Ace available for ALDS/NLDS Game 1 |
| Division Series win (4-1 or better) | Strong — ace preserved; bullpen fresh |
| Division Series win (7 games) | Weaker — bullpen depleted for next series |
| World Series win | Maximum narrative event |
| No-hitter / perfect game | Extraordinary individual event; viral signal |
| Ace injured (IL placement) | Most significant negative single event for team prediction |

---

## Sport-Specific Risk Variables

### The 162-game season — small sample noise

```
SAMPLE SIZE THRESHOLDS FOR STATISTICAL RELIABILITY:
  Individual pitcher ERA: reliable after 80+ innings (~40 starts if normal)
  Individual batter batting average: reliable after 300 plate appearances
  Team ERA: reliable after 50 games (~May)
  Team OPS: reliable after 40 games
  
  Agent rule: Before June, treat any individual game prediction with 
  greater uncertainty. Team-level predictions are more reliable than 
  individual player predictions in April/May.
```

### Injuries and the IL (Injured List)

```
IL DESIGNATIONS:
  10-day IL: Minor injuries; player eligible to return after 10 days
  15-day IL (pitchers): Pitcher-specific minimum
  60-day IL: Significant injury; out for substantial portion of season
  
  Key signal: When an ace goes on 60-day IL, the team's playoff probability
  drops sharply. This is the highest-impact single injury event in baseball.
  
  ACE ON IL: Check FIP of replacement starter — the quality gap is usually
  0.80–1.50 FIP points, which translates to ~1.5 additional runs per 9 innings.

SEPTEMBER ROSTER EXPANSION:
  From September 1, teams can carry 28 active players (up from 26)
  This adds fresh bullpen arms and pinch-hitting options
  Teams with deeper farm systems gain advantage in September
```

### The DH Rule and Pinch Hitting

With universal DH (both leagues), pitchers no longer bat. This eliminates a major
tactical element but creates a new one — DH platoon management. Teams with an elite
DH vs an opponent's starter handedness is a targeted lineup advantage.

---

## Signal Weight Adjustments

| Component | Recommended weight | Rationale |
|---|---|---|
| Sports catalyst | 40% | Pitching matchup and park factor dominate |
| Market / whale | 20% | Baseball has sophisticated sharp bettor community |
| Price trend | 20% | 162-game season creates reliable trends by mid-year |
| Social sentiment | 10% | Lower than contact sports; more analytical fanbase |
| Macro | 10% | Moderate; World Series has national broadcast reach |

---

## Agent Reasoning Prompts

```
You are a Major League Baseball sports intelligence agent. Before evaluating any game:

1. IDENTIFY THE STARTING PITCHERS FIRST. This is the most important input.
   ERA alone is insufficient — use FIP or xFIP for quality assessment.
   Check rest days. Check times-through-order penalty if available.

2. CHECK THE PARK FACTOR. Never assess a Coors Field game the same as a
   Petco Park game. Altitude and park dimensions are structural, not random.

3. CHECK WIND DIRECTION AND TEMPERATURE for outdoor stadium games.
   Wind blowing out increases home run probability by 15-20%.

4. BEFORE JUNE: Apply uncertainty discount to all predictions.
   Sample sizes are too small for reliable statistical inference in April-May.

5. BULLPEN AVAILABILITY matters as much as starter quality.
   A great ace followed by an exhausted bullpen is not a quality pitching game.
   Check each team's relief usage over the last 3 days.

6. PLATOON MATCHUPS: Check starting pitcher handedness vs opposing lineup.
   Stacked same-handed lineups vs a pitcher with extreme platoon split is a
   significant structural disadvantage for that pitcher.

7. PLAYOFFS RESET ALL REGULAR SEASON LOGIC.
   Offensive statistics compress dramatically against playoff-calibre starters.
   Bullpen usage and matchup management determine playoff series more than
   any regular season statistic.

8. THE TRADE DEADLINE (July 31) is the most significant mid-season event.
   Monitor acquisitions — elite pitching acquisitions demonstrably improve
   playoff probability and August-September outcomes.
```

---

## Fan Token™ Notes

No MLB fan token is currently active on Chiliz (as of Q1 2026). This skill is
included for completeness and future readiness. When MLB tokens launch:

- The highest-value tokens will likely be: Yankees (NYY), Dodgers (LAD), Red Sox
  (BOS), Cubs (CHC), Mets (NYM) — largest global fan bases
- World Series outcome will be the primary token impact event
- Trade deadline acquisitions of star players will be secondary signal events
- Load `fan-token/fan-token-pulse` when token data becomes available

---

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` for the full injury
framework. Baseball-specific notes:
- Starting pitcher IL placement (especially 60-day) is the highest-impact single injury
- Tommy John surgery (UCL reconstruction): 12–18 month recovery; career-altering
- Oblique and hamstring strains: common; often recurring; track history carefully
- Catchers accumulate wear over 162-game season; September performance often degraded
- Load `athlete/baseball/athlete-intel-baseball.md` for player-level injury tracking

## Data Sources

- **Baseball Reference (b-ref.com)**: Comprehensive historical statistics, splits, park factors
- **FanGraphs**: Advanced metrics (FIP, xFIP, SIERA, WAR, Statcast data)
- **Baseball Savant (savant.mlb.com)**: MLB's official Statcast database — pitch tracking, exit velocity, spin rate
- **Rotowire / Baseball Prospectus**: Injury updates, lineup projections
- **MLB official**: Confirmed lineups, transaction wire, official IL designations

## Key Commands

| Action | Skill | Notes |
|---|---|---|
| Pre-game signal | Load this file + `core/sportmind-score.md` | Pitching matchup first |
| Starting pitcher | `## Starting Pitcher — the dominant variable` | ERA, WHIP, recent starts |
| Injury response | `core/breaking-news-intelligence.md` | Ace absent = Category 1 |
| Bullpen signal | `## Bullpen intelligence` | Late-game leverage |
| Weather check | `## Environmental factors` | Wind direction at each park |

## Compatibility

**Athlete intelligence:** `athlete/baseball/athlete-intel-baseball.md`
**Injury intelligence:** `core/injury-intelligence/core-injury-intelligence.md`
**Fan token layer:** No active token — `fan-token/fan-token-pulse` when available

---

*MIT License · SportMind · sportmind.dev*
