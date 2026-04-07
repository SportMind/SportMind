# Baseball (MLB) — Athlete Intelligence

Player-level intelligence for Major League Baseball. Covers starting pitchers,
relief pitchers, and position players using Statcast and sabermetric frameworks.
Load alongside `sports/baseball/sport-domain-baseball.md` for full baseball intelligence.

---

## What this skill produces

- **Pitcher Quality Score (PQS)** — Current form composite for starting pitchers
- **Batter Quality Score (BQS)** — Current offensive form for position players
- **Platoon Split Assessment** — Handedness advantage/disadvantage for each matchup
- **Injury and IL Status** — Current availability and return timeline
- **Statcast Profile** — Pitch movement, exit velocity, launch angle for key players
- **Season Trajectory** — Is this player improving, declining, or stable?

---

## Starting Pitcher Assessment

### Pitcher Quality Score (PQS)

```
PQS = (
  xFIP_score        * 0.30 +   # quality-adjusted ERA (removes luck)
  K%_score          * 0.25 +   # strikeout rate (predictable)
  BB%_score         * 0.20 +   # walk rate (control)
  recent_form_score * 0.15 +   # last 3 starts trend
  TTOP_score        * 0.10     # times through order penalty
) → normalised to 0–100

xFIP scoring (lower is better):
  xFIP < 2.80: 100 | 2.80–3.20: 88 | 3.20–3.60: 74 | 3.60–4.00: 60
  4.00–4.50: 45 | 4.50–5.00: 30 | > 5.00: 15

K% scoring (higher is better):
  K% 30%+: 100 | 27–29%: 90 | 24–26%: 78 | 21–23%: 65
  18–20%: 50 | 15–17%: 35 | < 15%: 20

BB% scoring (lower is better):
  BB% < 4%: 100 | 4–5.5%: 88 | 5.5–7%: 72 | 7–9%: 55 | > 9%: 30

PQS bands:
  85–100: Ace / Elite — maximum confidence start
  70–84:  Quality — reliable prediction input
  55–69:  Average — use with lower confidence
  40–54:  Below average — high variance start
  < 40:   Poor — fade this starter where possible
```

### Statcast Pitcher Profile

```
FASTBALL:
  Velocity (mph):   Elite 97+ | Good 94–96 | Average 91–93 | Below 88–90
  Spin rate (rpm):  High spin = more movement and "rise" effect
  
BREAKING BALL (slider, curveball):
  Horizontal break (inches): High break = harder to square up
  Vertical break (drop): Curveball 50+ inches of vertical drop = elite
  Whiff rate: Slider whiff% elite 40%+ | Curveball 35%+
  
CHANGEUP:
  Velocity gap (vs fastball): Elite 10+ mph gap
  Horizontal movement: Arm-side fade = most deceptive
  
PITCH MIX:
  Fastball-heavy pitchers: high velocity predicts performance better
  Breaking ball-heavy pitchers: grip and conditions affect movement
  
CALLED STRIKE% / ZONE%:
  Low zone% but high called strike%: elite command — batters chasing out of zone
  High zone% but low called strike%: batters comfortable — pitcher is hittable
```

### Recent Form — Last 5 Starts

```
RECENT FORM TREND:

For each of the last 5 starts, record:
  IP (innings pitched), ER (earned runs), K, BB, HR

Compute:
  recent_ERA = (sum of ER across 5 starts / sum of IP) × 9
  recent_K%  = sum of K / (sum of IP × ~4.3 batters faced per IP)
  recent_BB% = sum of BB / (same denominator)

TREND DIRECTION:
  Compare starts 1–2 vs starts 4–5 (most recent):
  Improving: recent ERA lower, recent K% higher → rising PQS modifier × 1.08
  Declining: recent ERA higher → falling PQS modifier × 0.90
  Stable:    no significant directional change → × 1.00
  
DOME EFFECT ON RECENT FORM:
  Some pitchers have dramatically different home/road splits due to park factor
  Always check: does this pitcher's ERA look better at home (pitcher's park) vs road?
  If so, road starts should be assessed with road ERA, not season ERA
```

### Pitcher Injury Signals

```
COMMON PITCHER INJURIES AND IMPLICATIONS:

UCL (Ulnar Collateral Ligament) — the critical one:
  Tommy John surgery (UCL reconstruction): 12–18 month recovery
  UCL sprain (managed non-surgically): 4–8 weeks; high recurrence risk
  Signals: reduced velocity, changed arm slot, avoiding specific pitches
  Early warning: velocity drop of 2+ mph without explanation = investigate
  
Forearm tightness / strain:
  Common precursor to UCL issues — treat seriously
  "Forearm tightness" language = significant concern; may IL soon
  Recovery: 2–6 weeks if minor; can cascade to UCL
  
Shoulder (rotator cuff, labrum):
  Rotator cuff strain: 4–8 weeks; often recurring
  Labrum tear: often requires surgery; 6–12 months
  Signal: reduced velocity + poor command together
  
Blister (hand/finger):
  Common; affects grip and spin rate; usually 7–14 days
  Significant for pitchers who rely on breaking balls (grip-dependent)
  
Oblique strain:
  Particularly damaging for pitchers (rotational movement)
  Recovery: 3–6 weeks; high recurrence risk
  Often becomes chronic with repeated pitching load

VELOCITY MONITORING:
  Current game velocity vs season average:
    -1 mph: normal variation — nothing
    -2 mph: possible fatigue or early injury — monitor
    -3 mph: significant — likely injury or mechanics issue — flag
    -4+ mph: injury event — check IL immediately after game
```

---

## Position Player Assessment

### Batter Quality Score (BQS)

```
BQS = (
  wOBA_score          * 0.35 +   # weighted on-base average (best all-around metric)
  xwOBA_score         * 0.25 +   # expected wOBA (removes luck from BABIP)
  hard_contact_score  * 0.20 +   # exit velocity / hard hit %
  recent_form_score   * 0.15 +   # rolling 30-day performance
  platoon_score       * 0.05     # current platoon context
) → normalised to 0–100

wOBA scoring (context: league average ~.310–.320):
  wOBA .400+: 100 | .380–.399: 90 | .360–.379: 80 | .340–.359: 68
  .320–.339: 55 | .300–.319: 42 | .280–.299: 30 | < .280: 18

BQS bands:
  85–100: Star offensive player — weight heavily in game predictions
  70–84:  Above-average — reliable contribution
  55–69:  Average — standard inclusion
  40–54:  Below average — consider platoon situation
  < 40:   Weak — may be platoon-specific or in bad form
```

### Statcast Batter Profile

```
EXIT VELOCITY:
  Avg exit velocity (mph): Elite 92+ | Good 89–91 | Average 86–88 | Poor < 84
  
LAUNCH ANGLE:
  Sweet spot (8–32 degrees): percentage of batted balls in optimal range
  Elite 40%+ | Good 35%+ | Average 28%+
  
HARD HIT %:
  Balls hit at 95+ mph: Elite 48%+ | Good 42%+ | Average 35%+
  
BARREL %:
  Batted balls with high exit velocity AND optimal launch angle
  Elite 12%+ | Good 8%+ | Average 5%+
  This is the purest measure of power contact quality
  
CHASE RATE:
  Percentage of pitches outside zone swung at
  Low chase = disciplined; high chase = exploitable by breaking balls
  Elite < 20% | Good < 25% | Average 30%+
  
WHIFF RATE:
  Swings and misses / total swings
  Low whiff = contact ability; high whiff = strikeout risk
  Good < 22% | Average < 28% | High-risk 30%+
```

### Platoon Splits — the handedness matchup

```
PLATOON ADVANTAGE ASSESSMENT:

Check OPS split: batter vs same-handed pitcher (same) vs opposite-handed pitcher (opposite)
Most batters: .030–.060 OPS advantage vs opposite-handed pitcher

EXTREME PLATOON SPLITS (significant — affect game decisions):
  Batter with OPS split > .080: strongly platoon-dependent
    These batters are often benched vs same-handed pitching
    If they're in the lineup vs a same-handed starter: facing a disadvantage
    
  Left-handed batters in lineup vs left-handed starter:
    Even moderate platoon split (.040 OPS) creates team-level disadvantage
    If 4+ lefties starting vs LHP: flag as structural batting order weakness
    
SWITCH HITTERS:
  No platoon disadvantage by design; always hitting from advantageous side
  Check L/R splits anyway — some switch hitters have clear stronger side
```

### Batting Order Position

```
LINEUP POSITION AND TOKEN INTELLIGENCE:

Top of order (1–2): High OBP, set the table; fewer RBI, more runs scored
  Key stats: OBP, speed, plate discipline
  
Middle of order (3–5): Power hitters; highest RBI context
  Key stats: wOBA, barrel%, HR production
  If middle-order star is injured: run production drops significantly
  
Bottom of order (7–9): Often weakest hitters; can create double switch vs NL rules
  In AL: DH is typically 3–5 slot; 9th spot is weakest position player

ORDER DISRUPTION SIGNAL:
  Manager moves a regular top-5 hitter to 7–9: possible injury management
  Star hitter missing from lineup entirely: check IL or injury report
  Lineup card released without regular starter: significant — investigate
```

---

## Key Metrics Reference Table

| Metric | What it measures | Elite | Good | Average | Poor |
|---|---|---|---|---|---|
| ERA | Pitcher runs allowed/9 | < 2.50 | < 3.50 | < 4.50 | > 5.00 |
| FIP | Pitcher quality (luck-removed) | < 2.80 | < 3.50 | < 4.20 | > 5.00 |
| xFIP | Pitcher quality (HR-normalised) | < 2.80 | < 3.50 | < 4.30 | > 5.00 |
| K% | Strikeout rate | 28%+ | 22%+ | 18%+ | < 15% |
| BB% | Walk rate (lower better) | < 5% | < 7% | < 9% | > 10% |
| WHIP | Baserunners per inning | < 1.00 | < 1.20 | < 1.35 | > 1.50 |
| wOBA | Batter overall value | .400+ | .360+ | .320+ | < .290 |
| xwOBA | Batter quality (luck-removed) | .390+ | .350+ | .310+ | < .280 |
| Exit Velocity | Contact quality | 92+ mph | 89+ | 86+ | < 84 |
| Barrel % | Elite contact | 12%+ | 8%+ | 5%+ | < 3% |
| Hard Hit % | Hard contact rate | 48%+ | 42%+ | 35%+ | < 28% |
| Chase % | Plate discipline (lower better) | < 20% | < 25% | < 30% | > 33% |

---

## Season Trajectory Assessment

```
PLAYER TRAJECTORY SIGNALS:

RISING (form improving):
  Statcast metrics improving vs season average (last 30 vs full season)
  Hard hit % trending up | Whiff % trending down for batters
  Velocity holding or increasing | K% rising for pitchers
  Return from IL with no velocity loss (mechanical issue resolved)
  
DECLINING (form deteriorating):
  Statcast metrics declining
  Velocity dropping across recent starts (pitcher)
  Chase % increasing with declining hard contact (batter — slump or injury)
  BABIP significantly above .380 (likely declining soon — unsustainable)
  BABIP significantly below .220 (likely improving soon — luck turning)
  
STABLE:
  Statcast metrics consistent with season average
  No significant trend in either direction
  
AGE CURVE ADJUSTMENT:
  Players age 27–30: peak performance; no adjustment
  Players 31–33: slight decline expected; apply × 0.97 projection modifier
  Players 34+: meaningful decline risk; apply × 0.93; monitor Statcast carefully
  Players 35+: acceleration of decline; apply × 0.88; prioritise recent data
  Players under 25: upside projection; can improve significantly mid-season
```

---

## Catcher Intelligence — the underrated position

Catchers are often overlooked but have unique impact on pitching performance:

```
FRAMING (pitch receiving quality):
  Elite framers "steal" 15–25 called strikes above average per season
  Each stolen strike = ~0.15 runs saved
  Poor framers cost their team 10–20 strikes per season
  Check: called strikes above average (CSAA on Baseball Savant)
  
GAME-CALLING:
  Harder to quantify but catchers who know pitcher arsenals well
  produce better results from their starters than new pairings
  Monitor: when a catcher changes teams, starter performance may adjust
  
CATCHER FATIGUE (162-game season):
  Catchers face the most physical wear of any position
  September performance for catchers often degrades vs April
  Body contact, crouch repetition, and foul ball impacts accumulate
  
BACKUP CATCHER EFFECT:
  When starting catcher is injured/resting, backup catcher starting
  impacts pitcher performance: -0.25 to -0.50 ERA equivalent expected
```

---

## Agent Reasoning Prompts for Player-Level Decisions

```
1. xFIP OVER ERA. ERA contains luck (BABIP, strand rate); xFIP does not.
   A pitcher with 2.80 ERA but 4.00 xFIP is likely to regress — do not
   overweight a hot streak if the underlying quality doesn't support it.

2. STATCAST FOR BATTERS. Batting average is the worst metric to use for
   single-game predictions. Exit velocity, barrel%, and xwOBA are more
   predictive of true quality than traditional stats.

3. VELOCITY CHECK. For every starting pitcher, check current game velocity
   vs season average early in the game. A drop of 3+ mph is a significant
   injury or fatigue signal that often precedes IL placement.

4. PLATOON CONTEXT. Always identify the starter's handedness and check the
   opposing team's lineup handedness balance. A team with 5+ same-handed
   batters vs a starter with extreme platoon split is structurally weaker
   than their lineup would suggest.

5. BABIP REGRESSION. A batter hitting .180 on balls in play is due to
   improve; one hitting .430 is due to decline. Statcast xwOBA corrects
   for this — always use it over raw batting average for predictions.

6. SEPTEMBER CATCHERS. By September, catchers have absorbed 130+ games
   of physical punishment. Their defensive metrics and pitcher support often
   decline. Account for this in late-season assessments.

7. RECENT FORM WINDOW. For pitchers, 5-start rolling window is most
   predictive. For batters, 30-day rolling is the sweet spot — long enough
   for sample size, short enough to reflect current form.
```

---

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` for the full framework.

Baseball-specific injury additions:
- **UCL / Tommy John**: Most severe pitcher injury. 12–18 month recovery. Career-defining.
  Early signal: velocity drop + reduced pitch spin rate.
- **Oblique strain**: Pitcher and batter both. Rotational movement dependent.
  Often recurring. 3–6 week recovery; watch for re-injury on first return game.
- **Hamstring**: Common in outfielders and fast runners. 2–4 weeks. Re-injury rate high.
- **Plantar fasciitis**: Catchers and first basemen especially. Managed through season
  with injections; affects mobility and plate discipline.
- **Hand / finger injuries**: Grip-dependent — affects both pitchers (spin rate) and
  batters (bat speed and exit velocity).

---

## Data Sources

- **Baseball Savant (savant.mlb.com)**: Official Statcast data — free, comprehensive
- **FanGraphs (fangraphs.com)**: Advanced metrics, projections, park factors
- **Baseball Reference (baseball-reference.com)**: Historical data, splits, WAR
- **Rotowire**: Real-time injury news, lineup cards
- **MLB Transaction Wire**: Official IL placements and activations

---

---

## Commands

| Command | Description |
|---|---|
| `get_pqs` | Pitcher Quality Score composite for starting pitcher |
| `get_bqs` | Batter Quality Score composite for position player |
| `get_platoon_split` | Batter vs LHP/RHP performance differential |
| `get_park_factor` | Ballpark factor for today's venue |
| `get_athlete_signal_modifier` | Composite modifier combining PQS/BQS, park factor, matchup |

## Command reference

### `get_athlete_signal_modifier`

Master composite modifier for MLB. Combines PQS (pitchers) or BQS (batters) with park factor and platoon splits.

**Parameters:**
- `player_id` (required) — MLB player ID
- `game_id` (optional) — specific game; defaults to next scheduled start

**Returns:**
```json
{
  "player": "string",
  "role": "pitcher|batter",
  "pqs_or_bqs": 0.78,
  "park_factor": 1.05,
  "platoon_advantage": 1.02,
  "composite_modifier": 1.04,
  "adjusted_direction": "NEUTRAL_POSITIVE",
  "key_risks": ["Second start in 5 days", "Facing opposite-hand heavy lineup"],
  "modifier_reason": "Above-average pitcher with slight park and platoon advantage"
}
```

## Modifier reference

| Condition | Modifier |
|---|---|
| Ace pitcher (ERA <2.50, high K/9) vs weak lineup | ×1.20 |
| Above-average starter with platoon advantage | ×1.10 |
| Neutral matchup — league average stats | ×1.00 |
| Pitcher on short rest (4 days) | ×0.90 |
| Pitcher returning from IL — first start | ×0.82 |
| Bullpen game (no starter named) | ×0.75 |

## Integration example

### MLB pre-game workflow

```
# Step 1: Load domain context
Load sports/baseball/sport-domain-baseball.md

# Step 2: Get pitcher and batter assessments
get_pqs pitcher=[PLAYER_ID]          # Starting pitcher quality
get_bqs batter=[KEY_BATTER_ID]       # Opposing lineup key batter
get_park_factor venue=[VENUE_ID]     # Today's ballpark

# Step 3: Get composite modifier
get_athlete_signal_modifier player=[PITCHER_ID] game=[GAME_ID]

# Step 4: Decision logic
# If pitcher PQS >= 0.75 AND park_factor <= 1.05 → ENTER
# If pitcher on short rest OR bullpen game → REDUCE to 0.5× or ABSTAIN
# Output: SportMind confidence schema
```


---

*MIT License · SportMind · sportmind.dev*