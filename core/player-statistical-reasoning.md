# Player Statistical Reasoning Framework — SportMind Core

**How to interpret player statistics correctly — by sport, position, and context.**

Raw statistics are not signals. A striker with 3 goals in 5 games may be in
excellent form or deeply out of form depending on xG, opposition quality, and
game state. A defensive midfielder with 92% pass completion may be a liability.
A bowler with 2 wickets may have been brilliant or fortunate.

This framework teaches agents what numbers mean — and crucially, what they do not.

---

## The core principle

```
WRONG APPROACH:
  "Player has 8 goals this season → positive form signal"

RIGHT APPROACH:
  "Player has 8 goals from 14.2 xG → underperforming expected output
   Finishing quality declining or facing harder defences?
   Context: 6 of 8 goals from inside 6-yard box (tap-ins)
   Remove tap-ins: 2 open-play goals from 10.8 xG → cold form signal"

THE RULE:
  Every statistic requires a denominator.
  Every counting stat requires a rate.
  Every rate requires a positional and competitive context.
  
  Context changes meaning. Position changes meaning. Format changes meaning.
  An agent that skips context is reasoning from noise.
```

---

## Football

### Attacking players — strikers and forwards

#### Goals and xG (expected goals)

```
WHAT xG MEASURES:
  Probability of scoring from a given shot position and type
  Range: 0.01 (30-yard speculative) to 0.96 (close-range one-on-one)
  
WHAT IT TELLS YOU:
  xG > actual goals: player underperforming expected output
  xG < actual goals: player overperforming (finishing above average)
  
WHAT THE OVERPERFORMANCE MEANS:
  Short-term (5 matches): hot finishing, may be sustainable
  Medium-term (10+ matches): genuine elite finishing ability OR regression incoming
  Threshold: >1.3 goals per xG over 10+ matches = elite finisher, sustain signal
  Threshold: >1.3 goals per xG over 3-5 matches = small sample, do not use
  
TRAP — HIGH GOAL COUNT FROM LOW-QUALITY CHANCES:
  Player with 6 goals from 3.8 xG is not in "red-hot form"
  They are variance-positive. Regression to xG likely within 5-7 matches.
  Agent rule: flag XG_OVERPERFORMANCE if goals/xG ratio > 1.4 over < 8 matches
  
TRAP — POSITION CONTEXT FOR xG:
  A striker's xG counts shots from typical striker positions
  A winger's xG may be lower structurally — they take harder shots
  Do not compare absolute xG across positions — use per-90 within position group
  
POSITIONAL MODIFIERS:
  Centre forward:     xG threshold for "good form" = 0.4+ per 90
  Wide forward:       xG threshold = 0.25+ per 90
  Attacking mid:      xG threshold = 0.15+ per 90 (xA more relevant)
```

#### Assists and xA (expected assists)

```
WHAT xA MEASURES:
  Probability that a key pass results in a goal (quality of chance created)
  
WHAT HIGH xA MEANS:
  Player consistently finding teammates in high-probability scoring positions
  Sustainable signal — creating chances is more repeatable than finishing them
  
TRAP — ASSISTS VS xA:
  Player with 6 assists from 3.1 xA: teammates finishing exceptionally for them
  If key contributors leave or regress, assist total drops without form change
  Agent rule: Use xA not assists as the primary chance-creation signal
  
POSITIONAL CONTEXT:
  Playmaking midfielder: xA 0.2+ per 90 = excellent
  Wide forward: xA 0.15+ per 90 = good
  Deep-lying midfielder: xA 0.08+ per 90 = good (different role expectation)
```

#### Progressive actions (passes, carries, dribbles)

```
PROGRESSIVE PASS:
  A pass that advances the ball significantly toward the opponent's goal
  High progressive pass count + completion = ball-playing quality
  
PROGRESSIVE CARRY:
  A carry that advances the ball significantly — measures dribbling/driving quality
  
WHY THESE MATTER:
  Underlying quality metric — not dependent on teammates finishing
  More repeatable than goals and assists
  
CONTEXT RULE:
  Defensive midfielder with high progressive pass count = deep playmaker (positive)
  Striker with high progressive carry count = elite ball carrier (positive)
  Winger with low progressive carry count = may be struggling to beat defender
```

---

### Midfielders

#### Defensive midfielder / holding midfielder

```
PASS COMPLETION % — THE MOST MISREAD STAT IN FOOTBALL:

  95% pass completion for a holding midfielder CAN MEAN:
    A) Elite ball retention under pressure (positive signal)
    B) Only playing safe sideways/backwards passes (negative — not progressing play)
  
  HOW TO DISTINGUISH:
    High completion + high progressive passes = A (elite)
    High completion + low progressive passes = B (passive, hiding)
    
  BENCHMARK BY POSITION:
    Holding midfielder: 88-94% completion is normal range (large sample)
    Below 82%: struggling with basic retention (concerning)
    Above 95%: investigate pass type — are they progressive or safe?

PRESSURES AND PRESSURE SUCCESS RATE:
  Pressures: how often a player attempts to win the ball by closing opponent
  Pressure success %: how often the pressure forces a mispass or turnover
  
  Interpretation: High pressures + decent success % = high-energy defensive work
  Low pressures = either positional role (some systems use zone, not press) OR
               = player not tracking runners, poor work rate signal
  
  POSITIONAL CONTEXT ESSENTIAL:
    A 6 (anchor) has different pressure expectations than an 8 (box-to-box)
    Cannot compare across positional roles without role classification first
```

#### Box-to-box / central midfielder

```
KEY METRICS IN ORDER OF RELIABILITY:
  1. xA per 90 — chance creation quality (most repeatable)
  2. Progressive passes per 90 — advancing play
  3. Progressive carries per 90 — beating the press, carrying forward
  4. Pressures and success — defensive contribution
  5. Goals/assists — most volatile, least reliable in isolation

TRAP — TACKLES:
  High tackle count for a midfielder can mean:
    A) Excellent defensive reading (positive)
    B) Being caught out of position repeatedly (negative — they're having to tackle
       because they lost their man)
  
  HOW TO DISTINGUISH:
    High tackles + high interceptions = A (reading play well)
    High tackles + low interceptions = B (reacting, not anticipating)
    Interceptions require anticipation — tackles can be reactive
```

---

### Defenders

#### Centre-backs

```
AERIALS WON:
  Useful but context-dependent
  High aerial win % against a team that crosses heavily = different to same stat
  against a possession-based team that rarely crosses
  
  Agent rule: Aerial win % is only meaningful with opposition cross volume context
  
TACKLES AND INTERCEPTIONS:
  Same logic as midfielders — interceptions signal anticipation
  
PROGRESSIVE PASSES FROM DEFENCE:
  Increasingly important metric — ball-playing CBs add value from back
  Benchmark: 5+ progressive passes per 90 = quality ball-player at CB
  
TRAP — CLEARANCES:
  High clearance count is not a positive signal for a CB
  It means they are defending deep and under pressure
  Team context essential: a low-block team's CB will clear more than a high-line CB
  
DRIBBLES PAST (taken from FBref as "dribbled past"):
  Number of times player is beaten by opponent dribble
  Low = positive. High = defensive vulnerability
  Benchmark: >1.5 per 90 = defending with difficulty
```

#### Full-backs / wing-backs

```
CROSSES:
  Cross count alone is not a signal — cross accuracy is
  Cross accuracy benchmark: 25-35% = average; >35% = quality crosser
  
  BUT CROSS ACCURACY IS FORMAT-DEPENDENT:
    A winger cutting inside doesn't cross — raw count misleads
    Verify: is this player expected to cross in this system?
    
CARRIES INTO FINAL THIRD:
  Modern full-backs valued on attacking contribution
  5+ carries into final third per 90 = high attacking output
  
KEY PASS AND xA:
  Full-backs who generate xA = genuine attacking asset worth modifier
  xA 0.12+ per 90 for a full-back = top-tier attacking contribution
```

---

### Goalkeepers

```
SAVE % — THE MOST MISLEADING GK STAT:
  Save % depends on the quality of shots faced, not just saves made
  A GK facing mostly easy shots will have high save % without being excellent
  A GK facing a barrage of high-xG chances will have low save % even if excellent
  
USE INSTEAD: POST-SHOT xG AND GSAx (GOALS SAVED ABOVE EXPECTED):
  Post-shot xG: what were the chances the shots faced would go in?
  GSAx: actual goals conceded vs expected goals conceded
  Positive GSAx = GK saving shots they were not expected to save (elite signal)
  Negative GSAx = GK conceding shots they were expected to save (concern signal)
  
  Sources: FBref (PSxG), Money Puck equivalent for football
  
DISTRIBUTION:
  Long ball accuracy, short pass completion from GK
  Important in high-press systems where GK is first passer
  Under-used but increasingly available on FBref
  
TRAP — SHORT SAMPLE GK STATS:
  Goalkeepers face fewer meaningful events per match than outfield players
  10-match GSAx sample is minimum for signal reliability
  5-match window: directional only, do not treat as stable signal
  
BACKUP GOALKEEPER SIGNAL:
  First-choice GK missing → backup starts
  If backup's GSAx is unknown or negative: apply ×0.80 availability modifier
  If backup has positive career GSAx: apply ×0.92 (modest degradation)
```

---

## Rugby Union

### Kickers

```
CONVERSION % AND PENALTY GOAL %:
  Headline stats but zone-blind
  A kicker hitting 80% from in front of the posts may be missing the harder kicks
  
  USE INSTEAD: Zone performance (available via ESPN Scrum and specialist trackers)
  Central 0-22m: near-certainty zone (>95% expected)
  Wide 22-35m: skill zone (benchmark 70-80%)
  Central 35-50m: long-range (benchmark 60-70%)
  Wide 35-50m+: highest difficulty (benchmark 40-55%)
  
  AN ELITE KICKER:
    Hits benchmark in all zones, especially wide and long-range
    Does not inflate % by avoiding harder attempts
    
  WIND AND CROSSWIND CONTEXT:
    A kicker's accuracy in crosswind conditions is a separate signal
    Cannot apply standard zone benchmarks without weather context
    
  CLUTCH KICK SIGNAL:
    Last 5 minutes, score within 3 points: highest-signal kicks
    Track outcome separately — small sample but maximum game-impact
```

### Forwards — set piece

```
LINEOUT WIN % (OWN BALL):
  Benchmark: 85%+ = solid; 90%+ = dominant
  Below 80%: significant concern — lineout losing hurts territorial game severely
  
  HOOKER THROW ACCURACY IS DISTINCT:
    A hooker may throw accurately but jumpers/lifters may be disrupted
    Isolate throw accuracy from overall lineout success where possible
    
SCRUM SUCCESS %:
  Own-ball success: benchmark 92%+ (scrums should not fail on own ball)
  Below 88%: significant structural weakness — will be exploited
  Penalty concession rate from scrums: anything above 0.8/match is a concern
  
CARRYING METRICS:
  Metres per carry: 4+ = contributing carrier; 6+ = dominant
  Defenders beaten per carry: 0.3+ = breaking the line
  Dominant tackles (as ball-carrier): not standard but available in some elite data feeds
```

### Backs — attacking

```
PASSES:
  Pass count alone meaningless — passing more does not mean playing better
  Pass accuracy (%): benchmark 88%+ for backs
  Long pass accuracy separately if player is a long-range passer (10/12)
  
CARRIES AND METRES:
  Metres per carry: backs 5+ = good; 8+ = exceptional
  Line breaks: number of times player beats defensive line = elite signal
  Line break creation vs line break carry: creation (assists for breaks) equally valuable
  
OFFLOADS:
  Offload completion %: some players offload frequently but inaccurately
  Successful offload per match: 1.5+ = genuine offloading threat
  
KICKING FROM HAND:
  Territory kick success (exits own half): directional, not detailed usually
  Box kick accuracy: specialist stat rarely available outside elite data
```

---

## Cricket

### Batters

```
BATTING AVERAGE VS BATTING AVERAGE IN FORMAT:
  A Test average of 45 says nothing about T20 ability
  Format-specific averages are mandatory
  
  BENCHMARK BY FORMAT:
    Test: 40+ = good international batter; 50+ = elite
    ODI: 35+ = good; 45+ = elite
    T20I: 25+ = good (fewer innings, more dismissals); 35+ = elite
    
STRIKE RATE (T20 AND ODI):
  For T20: strike rate is as important as average
  SR 130-149: good T20 batter
  SR 150+: match-winner tier
  SR below 120: liability in T20 (blocking in a run-chase format)
  
  BUT SR CONTEXT BY BATTING POSITION:
    Opening batter SR 135: excellent (facing new ball, harder conditions)
    Middle-order finisher SR 135: below expected (should accelerate at end)
    Cannot compare SRs across batting positions directly
    
AVERAGE × STRIKE RATE — THE COMBINED SIGNAL:
  Average 35 × SR 145 = T20 quality batter
  Average 50 × SR 100 = Test specialist, T20 liability
  
BATTER VS BOWLER HEAD-TO-HEAD:
  Most predictive stat in cricket for specific match context
  Available on ESPNcricinfo Statsguru
  Minimum 15 balls faced for signal reliability
  
  An elite average batter who averages 12 against a specific bowler
  type (e.g., left-arm pace) = genuine matchup vulnerability
  
RECENT FORM WINDOW:
  Last 5 innings in same format is the primary window
  Long-term average 45 + last 5 innings: 8, 3, 12, 0, 6 = cold signal
  Agent rule: weight last 5 innings at 60%, career average at 40% for form score
```

### Bowlers

```
BOWLING AVERAGE VS ECONOMY RATE — NOT THE SAME SIGNAL:
  Average: runs conceded per wicket (lower = better)
  Economy: runs conceded per over (lower = better)
  Strike rate: balls per wicket (lower = better)
  
  FORMAT PRIORITY:
    Tests: average and strike rate primary (wickets matter most)
    ODI: all three balanced
    T20: economy rate primary (containing runs often > taking wickets)
    
  AN IMPORTANT DISTINCTION:
    A T20 specialist spinner with economy 7.5 and no wickets
    may be more valuable than one with 2 wickets and economy 9.5
    
WICKETS IN CONTEXT:
  2 wickets in a low-scoring match (total 140) = very different signal
  to 2 wickets in a high-scoring match (total 200)
  
  Agent rule: wickets per match is a poor standalone signal — use bowling average
  
DEATH OVER BOWLING:
  Overs 16-20 in T20: hardest to bowl, most runs conceded
  Economy in death overs: separate signal from economy in powerplay/middle
  Benchmark: economy <10 in overs 17-20 = good death bowler; <9 = elite
  
PITCH AND CONDITIONS MODIFIER:
  Spin-friendly pitch: spin bowler strike rate and average become dominant signal
  Seam-friendly pitch: pace bowler metrics prioritised
  Dew (evening T20): spin bowling effectiveness significantly reduced
  Agent rule: pitch conditions are a modifier ON the bowler stats, not separate
```

---

## MMA / UFC

### Striking

```
SIGNIFICANT STRIKES LANDED PER MINUTE (SLpM):
  Volume of meaningful strikes landed
  Benchmark: 3+ SLpM = active striker; 5+ = high-volume
  
  BUT VOLUME WITHOUT ACCURACY IS NOT A SIGNAL:
    Always pair with: significant strike accuracy %
    Benchmark accuracy: 43%+ = average; 50%+ = accurate
    
  THE COMBINED SIGNAL:
    High SLpM + high accuracy = elite striker — positive form signal
    High SLpM + low accuracy = wild, may get countered — mixed signal
    Low SLpM + high accuracy = selective, patient — may be read as defensive
    
SIGNIFICANT STRIKES ABSORBED PER MINUTE (SApM):
  How many significant strikes the fighter absorbs
  Lower = better defensive output
  High SApM = getting hit a lot = chin/defence concern over time
  
  TRAP: Some fighters absorb more because they press forward constantly
    (higher exposure = more absorbed)
  PAIR WITH: knockout rate — if absorbing a lot but not getting stopped = good chin
  
STRIKING DIFFERENTIAL:
  SLpM minus SApM
  Positive = landing more than absorbing
  Best single-number striking signal
```

### Grappling

```
TAKEDOWN ACCURACY VS TAKEDOWN DEFENCE:
  Takedown accuracy: how often takedown attempts succeed
  Benchmark: 40%+ = good grappler; 55%+ = elite
  
  Takedown defence: how often opponent's takedown attempts are stopped
  Benchmark: 65%+ = good; 78%+ = elite
  
  THE MATCHUP SIGNAL:
    High takedown accuracy fighter vs high takedown defence opponent
    = contested grappling domain — do not assign strong advantage to either
    
SUBMISSION ATTEMPT RATE:
  Tells you whether a fighter looks for submissions when on the ground
  High attempt rate + low finishing rate = telegraphing, being defended
  High attempt rate + high finishing rate = genuine submission threat
  
CONTROL TIME:
  Minutes controlling opponent per fight
  2+ minutes = ground control dominant; 4+ = overwhelming grappler
  Useful for predicting decisions — high control fighters win decisions
```

### The style matchup dimension

```
THIS IS THE MOST IMPORTANT REASONING STEP IN MMA STATISTICS:

  Raw stats become signals only when filtered through style matchup.
  
  A wrestler's stats against strikers are different to their stats against grapplers.
  A striker's stats against grapplers are different to their stats against strikers.
  
  Agent rule: Always segment statistical analysis by opponent type:
    "vs strikers" / "vs grapplers" / "vs mixed"
    Available on Tapology and UFC Stats with manual segmentation
    
  EXAMPLE:
    Fighter A: takedown accuracy 55% overall
    Fighter A: takedown accuracy vs elite wrestlers: 28%
    Fighter A: takedown accuracy vs strikers: 71%
    
    Opponent is an elite wrestler → use 28%, not 55%
    This changes the modifier significantly
```

---

## Formula 1

### Qualifying delta

```
THE MOST PREDICTIVE STAT IN F1:
  Qualifying gap between driver and teammate on same equipment
  Removes car advantage — isolates driver performance
  
  BENCHMARK:
    Within 0.1s: competitive pairing
    0.1-0.2s deficit: clear second driver
    0.2s+ deficit: significant underperformance
    
  CIRCUIT TYPE MODIFIER:
    High-downforce, technical circuits: smaller deltas (less opportunity to express gap)
    Power circuits (Monza, Spa): larger deltas more meaningful
    Street circuits (Monaco): one lap, mistakes amplified
    
  SAMPLE SIZE:
    Single qualifying: one-event signal (tyre gamble, traffic, yellow flags)
    Season qualifying average: reliable driver quality indicator
    
  RULE: Never use a single qualifying result as a signal.
    Use rolling 5-race qualifying average vs teammate.
```

### Race pace vs qualifying pace

```
SOME DRIVERS QUALIFY WELL, RACE POORLY — AND VICE VERSA:
  Hamilton (historically): races better than qualifying position suggests
  Leclerc (historically): qualifying specialist, race pace occasionally drops
  
  HOW TO IDENTIFY:
    Average qualifying position vs average race finishing position over season
    If average race position better than average qualifying: race-day performer
    If average race position worse: qualifying specialist
    
  THIS MATTERS FOR:
    Wet races: qualifying advantage can disappear (different skills)
    Safety cars: compress field, reduce qualifying advantage
    Race starts: some drivers gain positions at start consistently
```

### Tyre management

```
SIGNAL: Consistent ability to manage tyre degradation
  Harder to measure — available via sector time analysis in late stints
  
  Practical proxy: finishing position vs predicted pit stop pace
  If consistently finishing higher than tyre strategy suggests → tyre manager
  
  WHEN IT MATTERS: High-degradation tracks (Barcelona, Bahrain, Silverstone)
  When it does not: Low-deg circuits where tyres last regardless
```

---

## Ice Hockey (NHL)

### Corsi and Fenwick (shot attempt metrics)

```
CORSI FOR % (CF%):
  Shot attempts for / total shot attempts (for + against) while player on ice
  Benchmark: 50%+ = neutral; 53%+ = possession-dominant; 47%- = struggle
  
  THE INTERPRETATION:
    High CF% = team controls play and puck when this player is on ice
    
  TRAP — ZONE STARTS:
    Players deployed mostly in offensive zone will have inflated CF%
    Players deployed mostly in defensive zone will have lower CF%
    ALWAYS check offensive zone start % alongside CF%
    
  Adjusted CF% (zone-start adjusted) is the correct metric — available on
  Natural Stat Trick and Hockey Reference
  
FENWICK:
  Same as Corsi but excluding blocked shots
  Slightly purer measure of shot quality opportunities
  Generally preferred by analytics community
```

### Goaltending — GSAx

```
GOALS SAVED ABOVE EXPECTED (GSAx):
  How many more goals saved than expected given shot quality faced
  Positive = elite; negative = below average; near zero = average
  
  SAMPLE SIZE:
    Minimum 500 shots faced for season-level reliability
    50 shots = directional only (one or two hot/cold games)
    
  THE MOST RELIABLE SINGLE GK SIGNAL IN ANY SPORT:
    Because it controls for shot quality, team defence, and volume
    Preferred over save % in all SportMind applications
    Source: Money Puck (moneypuck.com)
```

---

## Basketball (NBA)

### True shooting % (TS%)

```
THE CORRECT EFFICIENCY METRIC:
  Accounts for 2-pointers, 3-pointers, and free throws
  Benchmark: 55%+ = average; 60%+ = good; 65%+ = elite
  
  FIELD GOAL % ALONE IS MISLEADING:
    A player shooting 45% from 2 and 35% from 3 may have same FG% as
    a player shooting 50% from 2 only — but very different value
    TS% correctly weights the three-point efficiency premium
    
  POSITION CONTEXT:
    Centre: TS% 60%+ expected (closer shots)
    Guard: TS% 55%+ good (longer shots, harder looks)
```

### Usage rate and efficiency interaction

```
USAGE RATE (USG%):
  % of team plays that end with the player shooting, fouled, or turning over
  High usage (28%+) = primary offensive option
  
  THE CRITICAL INTERACTION:
    High USG% + high TS% = elite offensive player (rare and valuable)
    High USG% + average TS% = normal for primary options (volume efficiency)
    Low USG% + high TS% = efficient role player (may understate impact)
    
  DO NOT compare TS% without noting USG%:
    A player with 65% TS% on 12% USG is taking easy shots
    A player with 60% TS% on 32% USG is being exceptional under heavy usage
```

### On/off splits

```
NET RATING ON/OFF:
  Team point differential per 100 possessions with player on vs off court
  Most comprehensive single player impact metric
  
  +8 net rating on = team is significantly better with this player
  Near zero = average contribution
  Negative = team better without player (concerning)
  
  TRAP — LINEUP QUALITY:
    Player may have strong on/off because they always play with elite teammates
    Check: lineup net ratings with various teammate combinations
    Source: Cleaning the Glass (cleaningtheglass.com)
```

---

## Cross-sport statistical reasoning rules

### Rule 1 — Always use rates, not counts

```
WRONG: "Player made 45 tackles this season"
RIGHT: "Player averages 3.2 tackles per 90 minutes — above position benchmark of 2.8"

Counts are a function of minutes played. Rates are a function of performance.
Exception: counts matter when the question is volume (e.g., pitcher innings count)
```

### Rule 2 — Position context is mandatory

```
Stats mean different things by position. Apply before interpreting:
  Football: striker xG vs midfielder xG are not comparable
  Rugby: prop carries vs winger carries are not comparable
  Basketball: centre TS% vs guard TS% are not comparable
  
An agent that compares raw stats across positions is reasoning incorrectly.
```

### Rule 3 — Minimum sample sizes

```
Sport          Minimum sample for reliable signal
Football       5 matches (form); 15 matches (season benchmark)
Rugby          6 matches
Cricket        8 innings per format (batters); 30 overs (bowlers)
MMA            5 fights (career totals)
F1             5 races (qualifying delta)
NHL            500 shots faced (GK); 20 games (skaters)
NBA            20 games
Tennis         20 matches on surface

Below minimum: flag as SMALL_SAMPLE — directional signal only.
Do not apply full modifier weight to small samples.
```

### Rule 4 — Opposition quality adjustment

```
Stats against top-10 opposition vs bottom-10 opposition differ significantly.
When available, weight recent performance:
  vs strong opposition: full signal weight
  vs weak opposition: 0.7x signal weight (easier to produce strong numbers)
  Mixed: standard weight
  
If competition quality is unknown: use standard weight with note
```

### Rule 5 — Recency weighting

```
Last 5 matches / last 30 days: 60% weight
Previous 10 matches / 60 days: 25% weight
Season average: 15% weight

Exception: for form reversals (injury return, new manager, format change)
reset to last 5 matches only — longer history is not relevant post-reset event
```

### Rule 6 — The "lying statistic" flags

```
These statistics frequently mislead. Flag for human review before using as signal:

FLAG: HIGH_CLEARANCES (football CB) — team defending deep, not individual quality
FLAG: HIGH_TACKLES_LOW_INTERCEPTIONS — reactive defending, not reading play
FLAG: HIGH_PASS_COMPLETION_LOW_PROGRESSIVE — safe passing, not progressing play
FLAG: GOALS_ABOVE_XG_SMALL_SAMPLE — variance, not form
FLAG: HIGH_KO_RATE_AGING_FIGHTER — may reflect chin deterioration, not power
FLAG: HIGH_SAVE_PCT_WITHOUT_GSAX — shot quality unknown, misleading
FLAG: HIGH_BATTING_AVG_ONE_FORMAT — format specialist not format generalist
```

---

## Integration with SportMind modifier system

```
This framework feeds into:
  core/core-athlete-modifier-system.md — form sub-modifier calculation
  athlete/{sport}/athlete-intel-{sport}.md — per-sport stat interpretation
  core/athlete-disciplinary-intelligence.md — performance context alongside conduct

The reasoning steps:
  1. Retrieve statistics from source (core/verifiable-sources-by-sport.md)
  2. Apply position context (this file, position sections)
  3. Apply sample size check (Rule 3)
  4. Apply opposition quality adjustment (Rule 4)
  5. Apply recency weighting (Rule 5)
  6. Check lying statistic flags (Rule 6)
  7. Convert to form score → modifier (core/core-athlete-modifier-system.md)
  8. Combine with availability, disciplinary, and other sub-modifiers
```

---

*SportMind v3.33 · MIT License · sportmind.dev*
*Connects to: core/core-athlete-modifier-system.md · core/verifiable-sources-by-sport.md*
*core/data-sources.md · athlete/{sport}/athlete-intel-{sport}.md*
