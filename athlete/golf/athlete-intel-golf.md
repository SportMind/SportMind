# Golf Athlete Intelligence — SportMind Skill

Player-level intelligence for golf prediction markets and fan tokens.
Produces an `athlete_modifier` that adjusts base golf signals with course-fit,
form, and conditions context.

**Applicable tokens / markets:** Individual golfer tokens, Major tournament markets, PGA/DP World Tour prediction markets.

---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_player_form_score` | Rolling form based on recent tournament finishes and strokes gained | Yes |
| `get_course_history` | Historical performance at a specific venue | Yes |
| `get_strokes_gained_profile` | SG: Off-the-Tee, Approach, Around-the-Green, Putting breakdown | Yes |
| `get_cut_line_status` | Current cut line position after round 2 | Yes |
| `get_major_record` | Career Major record — wins, top-5s, missed cuts | Yes |
| `get_ranking_trajectory` | World ranking trend and recent ranking events | Yes |
| `get_injury_status` | Current injury flags, withdrawal history | Yes |
| `get_athlete_signal_modifier` | Composite modifier — all sub-skills combined | Yes |

---

## Command reference

### `get_player_form_score`

Rolling form score based on last 8–12 tournament results, weighted by event tier and recency.

**Parameters:**
- `player_name` (required) — player name string
- `tournaments` (optional, default: 10) — number of tournaments to include
- `surface` (optional) — `links`, `parkland`, `all` — filter by course type

**Returns:**
```json
{
  "player": "Scottie Scheffler",
  "form_score": 91,
  "form_label": "HOT",
  "last_8_results": [
    { "event": "The Masters", "finish": 1, "score_to_par": -11, "sg_total": 4.2 },
    { "event": "Players Championship", "finish": 3, "score_to_par": -14, "sg_total": 2.8 },
    { "event": "Cognizant Classic", "finish": 1, "score_to_par": -20, "sg_total": 6.1 }
  ],
  "average_finish_position": 4.2,
  "cuts_made_pct": 0.92,
  "sg_total_avg": 3.4,
  "form_modifier": 1.18
}
```

### `get_course_history`

Historical performance at a specific venue — critical for Augusta, St Andrews, and other iconic courses.

**Parameters:**
- `player_name` (required)
- `course` (required) — course name or tournament name e.g. `"Augusta National"`, `"The Masters"`, `"St Andrews"`
- `years` (optional, default: 10)

**Returns:**
```json
{
  "player": "Tiger Woods",
  "course": "Augusta National",
  "appearances": 22,
  "wins": 5,
  "top_5s": 11,
  "made_cut_pct": 0.86,
  "avg_finish": 8.4,
  "avg_score_to_par_per_round": -1.8,
  "best_finish": 1,
  "worst_finish": "MC",
  "course_modifier": 1.22,
  "course_verdict": "ELITE — course suits player profile"
}
```

### `get_strokes_gained_profile`

Breaks down performance into the four SG categories. Identifies where a player gains or loses shots.

**Parameters:**
- `player_name` (required)
- `tournaments` (optional, default: 12)
- `surface` (optional)

**Returns:**
```json
{
  "player": "Scottie Scheffler",
  "strokes_gained": {
    "off_the_tee": 1.12,
    "approach_the_green": 1.84,
    "around_the_green": 0.62,
    "putting": 0.44,
    "total": 4.02
  },
  "tour_percentile": {
    "off_the_tee": 92,
    "approach": 98,
    "around_green": 78,
    "putting": 65
  },
  "profile_label": "BALL_STRIKER — elite from tee and approach, reliable short game",
  "course_fit_note": "Ball-strikers dominate Augusta and US Open setups — high course fit",
  "sg_modifier": 1.15
}
```

### `get_cut_line_status`

Real-time cut line position during tournaments. Critical post-round 2 signal.

**Parameters:**
- `player_name` (required)
- `tournament` (required) — current tournament name
- `round` (optional, default: 2) — which round to assess

**Returns:**
```json
{
  "player": "Rory McIlroy",
  "tournament": "The Masters 2026",
  "round": 2,
  "score_to_par": -4,
  "position": "T14",
  "cut_line_projection": -2,
  "margin_above_cut": 2,
  "cut_status": "SAFE",
  "cut_modifier": 1.05,
  "note": "Comfortable inside cut — weekend confirmed"
}
```

**Cut status values:** `SAFE` (3+ clear), `MARGINAL` (within 1), `MISSED` (below cut line), `PROJECTED_MISS`

### `get_major_record`

Career Major championship record — the single most important historical signal for Major week.

**Parameters:**
- `player_name` (required)

**Returns:**
```json
{
  "player": "Rory McIlroy",
  "major_record": {
    "wins": 4,
    "runner_up": 3,
    "top_5": 9,
    "top_10": 14,
    "missed_cuts": 4,
    "total_appearances": 62
  },
  "by_major": {
    "masters": { "wins": 0, "best": 4, "avg_finish": 18.2, "mc_count": 1 },
    "pga_championship": { "wins": 1, "best": 1, "avg_finish": 12.4 },
    "us_open": { "wins": 1, "best": 1, "avg_finish": 11.8 },
    "the_open": { "wins": 2, "best": 1, "avg_finish": 9.2 }
  },
  "clutch_round_4": 0.72,
  "major_modifier": 1.12,
  "note": "Strong Major record but Masters remains elusive — adjust Masters modifier down"
}
```

### `get_athlete_signal_modifier`

Composite modifier — runs all sub-skills.

**Parameters:**
- `player_name` (required)
- `tournament` (required) — current or upcoming tournament

**Returns:**
```json
{
  "player": "Rory McIlroy",
  "tournament": "The Open Championship 2026",
  "base_signal_score": 72,
  "composite_modifier": 1.18,
  "adjusted_signal_score": 85,
  "adjusted_direction": "STRONG_BULLISH",
  "modifier_breakdown": {
    "form": 1.08,
    "course_history": 1.22,
    "strokes_gained": 1.10,
    "major_record": 1.12,
    "injury_status": 1.00,
    "cut_status": 1.00
  },
  "confidence": 0.84,
  "recommendation": "STRONG ENTRY — Open Championship specialist with exceptional links record. Enter at draw announcement, add on cut confirmation.",
  "key_risks": ["No wins in last 6 weeks (form cooling)", "Open weather forecast: strong wind (links equaliser)"]
}
```

---

## Modifier reference

| Condition | Modifier |
|---|---|
| Major specialist — 3+ top-5 at this specific Major | ×1.22 |
| Strong course history (3+ wins or 5+ top-10s) | ×1.18 |
| HOT form (top-5 in 3 of last 5 events) | ×1.15 |
| Comfortable inside cut after R2 | ×1.05 |
| Average course history (1–2 top-10s) | ×1.00 |
| First time at venue | ×0.92 |
| Missed cut last visit | ×0.88 |
| Poor form (3+ MCs in last 8 events) | ×0.82 |
| Back injury concern | ×0.78 |
| Active withdrawal risk | ×0.70 |

### Knockout conditions

| Condition | Floor |
|---|---|
| Missed cut (confirmed) | 0.00 (exit — no more golf this week) |
| Confirmed withdrawal | 0.00 |
| DNF mid-round | 0.00 |

---

## Integration example

```
# Major Championship week workflow
get_player_form_score player="Rory McIlroy" tournaments=10
get_course_history player="Rory McIlroy" course="Carnoustie"
get_major_record player="Rory McIlroy"
get_strokes_gained_profile player="Rory McIlroy"

# After round 2
get_cut_line_status player="Rory McIlroy" tournament="The Open 2026" round=2

# Composite
get_athlete_signal_modifier player="Rory McIlroy" tournament="The Open 2026"

# Decision: if adjusted_score >= 72 AND cut status SAFE → maintain/add position
#           if MISSED CUT → exit immediately
```


---

## Strokes Gained — the primary golf signal

```
STROKES GAINED (SG) IS THE MOST PREDICTIVE INDIVIDUAL GOLF STATISTIC:

SG measures how many strokes better or worse a player performed vs the field
from a given situation. Unlike scorecards, SG isolates each component of the game.

FOUR COMPONENTS AND THEIR COURSE-TYPE RELEVANCE:

SG: Off-the-Tee (OTT):
  Measures driving distance and accuracy combined
  Most important at: US Open (narrow fairways), courses with rough
  Least important at: Links courses (wide fairways, firm ground — driver optional)
  
  OTT > +1.50 per round: elite driver — × 1.10
  OTT 0.50-1.50: above average — × 1.04
  OTT < -0.50: driving weakness — × 0.94

SG: Approach-the-Green (APP):
  Measures iron/approach shot quality
  MOST UNIVERSALLY PREDICTIVE of all four components
  Important at: every course type — approach play determines birdie opportunities
  
  APP > +1.50: elite ball-striker — × 1.14 (the most valuable SG component)
  APP 0.50-1.50: above average — × 1.06
  APP < -0.50: approach weakness — × 0.93

SG: Around-the-Green (ARG):
  Measures chipping, pitching, and bunker play
  Most important at: Augusta National (heavily penalised short game)
  Links courses: often less critical (fewer penalty areas near greens)
  
  ARG > +0.80: elite short game — × 1.06
  ARG < -0.50: short game weakness — × 0.94

SG: Putting:
  Measures putting performance vs expected for same distance and conditions
  HIGHEST VARIANCE of all four components — week-to-week putting varies
  For prediction purposes: weight putting 25% less than approach
  (putting is real-time hot/cold; approach is more structural)
  
  Putting > +1.00: elite on this week's greens — × 1.08
  Putting < -0.80: struggling on greens — × 0.92

COMPOSITE SG TOTAL (sum of all four):
  > +3.00 per round: elite week — × 1.18
  +1.50 to +3.00: strong — × 1.10
  +0.50 to +1.50: above average — × 1.04
  -0.50 to +0.50: field average — × 1.00
  < -0.50: below average — × 0.94

COURSE-FIT MATCHING:
  Match the player's strongest SG component to what the course rewards.
  Augusta National → heavy approach and short game premium
  US Open (thick rough) → OTT accuracy + approach
  The Open Championship (links) → approach + wind management
  PGA Championship → often parkland, balanced; OTT important
  
  COURSE-FIT MODIFIER:
    Player's strongest component matches course requirement: × 1.08 additional
    Player's weakest component is course's primary requirement: × 0.92 additional
```

---

## The Four Majors — specific intelligence

```
THE MASTERS (Augusta National, April):
  Par 72 · 7,510 yards (approx) · Parkland
  
  KEY SIGNALS:
    Course history is THE primary variable at Augusta — the course is
    famously skill-specific. Players who understand the slopes win here repeatedly.
    
  AUGUSTA SPECIALIST MARKERS:
    Previous Masters win: course_modifier × 1.25
    3+ top-10 finishes at Augusta: course_modifier × 1.18
    SG: Approach > +1.0 career at Augusta: × 1.10 (approach play at Augusta decisive)
    Poor Augusta record (5+ appearances, no top-20): × 0.88
    
  FIRST-TIME PARTICIPANT: × 0.85 (Augusta demands course knowledge)
  
  WEEK-SPECIFIC: Par 3 contest Wednesday — track putting surface speed

THE OPEN CHAMPIONSHIP (Rota of links courses, July):
  Venues: St Andrews, Royal Liverpool, Carnoustie, Muirfield, Royal Troon,
           Royal Birkdale, Royal Portrush
  
  KEY SIGNALS:
    Wind is the primary equaliser — removes the SG: APP advantage of US-based players
    Links specialists (grew up on seaside courses): × 1.12
    Players who own venue (McIlroy at Hoylake, Nicklaus at St Andrews): × 1.18
    US/inland specialists playing links for first time: × 0.90
    
  WIND PROTOCOL:
    Wind > 25 mph: apply wind_penalty × 0.93 for non-links specialists
    Wind > 35 mph: apply wind_penalty × 0.87; field equalisation active
    
  WEATHER WINDOW: Check Met Office forecast at T-48h and T-24h

US OPEN (Various venues, June):
  Typically: tight fairways, thick rough, slow greens
  
  KEY SIGNALS:
    OTT accuracy is mandatory — penalised rough removes long hitters' advantage
    SG: Approach most important (approach from rough = penalty)
    Patience: US Open rewards conservative play → steady temperament × 1.06
    
  SETUP-FIT MODIFIER:
    OTT accuracy top-30 on tour: × 1.08
    Long hitter without accuracy (driver > 310yd but OTT < 0): × 0.90

PGA CHAMPIONSHIP (Various venues, May):
  Typically: parkland, demanding rough, not as extreme as US Open
  
  KEY SIGNALS:
    Most balanced of the four Majors — all four SG components relevant
    Venue rotation means course history is less predictive than Masters/Open
    World ranking is more predictive here than at Masters — the best players win
    
  RANKING MODIFIER: WR #1-5: × 1.06 base (strongest correlation with WR at PGA Championship)
```

---

## LIV Golf and tour landscape intelligence

```
PGA TOUR vs LIV GOLF — SIGNAL IMPLICATIONS (2024 onwards):

LIV Golf players are restricted/excluded from most PGA Tour events.
This creates a bifurcated talent pool that matters for signal analysis.

ACTIVE LIV PLAYERS (as of 2026):
  Playing LIV full-time: Dustin Johnson, Brooks Koepka, Phil Mickelson,
                         Cameron Smith, Joaquin Niemann, Louis Oosthuizen (and others)
  
  LIV SIGNAL IMPLICATIONS:
    Form tracking: LIV events are valid form data; use for SG trajectory
    Major eligibility: LIV players remain eligible for Majors (all 4)
    World Ranking: LIV events now contribute to OWGR (from late 2024)
    
  ATM IMPACT:
    LIV top stars retain ATM (Johnson, Koepka, Smith: ATM 0.65-0.78)
    Commercial reach: LIV's global TV deal means sustained visibility
    Saudi/Gulf market: LIV events in Saudi Arabia create regional ATM premium

DP WORLD TOUR (European Tour):
  Stronger international field than LIV for non-Majors
  Co-sanctioned events with PGA Tour count toward both eligibility structures
  European players: DP World Tour form is primary for non-US events

QUALIFICATION SIGNAL:
  Player in danger of losing PGA Tour card: maximum motivation modifier × 1.10
  (Same principle as NASCAR playoff bubble — survival creates urgency)
  FedEx Cup leader: conservative play signal × 0.92 in later rounds
```

---

## ATM framework for golf

```
GOLF ATM TIERS:

Tier 1 — Global icons (Tiger Woods legacy; current: Rory McIlroy, Scottie Scheffler):
  ATM 0.78-0.88; universally recognised; non-golf audiences engage
  Rory McIlroy: highest active ATM (Grand Slam quest narrative permanent)
  Scottie Scheffler: dominant #1 ranking elevates ATM continuously
  
  GRAND SLAM NARRATIVE:
    Rory McIlroy seeking career Grand Slam (all 4 Majors):
    Apply: grand_slam_narrative_active = True during any of his Major appearances
    ATM multiplier when contending Sunday: × 1.20 (most-watched storyline in golf)

Tier 2 — Multiple Major winners:
  ATM 0.65-0.75; well-known within golf; moderate crossover
  
Tier 3 — Tour winners, top-50 OWGR:
  ATM 0.45-0.58; golf-audience recognition

MAJOR WEEK ATM PEAKS:
  Any player 36-hole leader at a Major: ATM spike regardless of tier
  Final round Sunday at Augusta: maximum global golf viewership
  Sunday leader at Augusta: ATM × 1.18 for the leading contender
```

---

## Integration: Full golf Major week workflow

```
THURSDAY (Round 1 — opening):
  1. Load course intelligence (Augusta/links/parkland profile)
  2. get_course_history for top-20 OWGR players
  3. get_strokes_gained_profile — identify course-fit matches
  4. Signal: form × course-fit × major_record → pre-tournament modifier
  5. Note: R1 has highest variance of any round (no cut pressure, weather randomness)

FRIDAY (Round 2 — cut day):
  1. Morning: update form with R1 scores
  2. Afternoon: get_cut_line_status as cut approaches
  3. CRITICAL: players making/missing cut changes the analysis entirely
  4. MISSED CUT → exit signal immediately (0.00 — no more tournament for this player)

SATURDAY (Round 3 — moving day):
  1. Leaderboard established — field has narrowed
  2. get_strokes_gained_profile using this week's tournament data (if available)
  3. Players 5+ behind with 1 round to play: apply deficit_modifier × 0.85
  4. Players within 3 shots of lead: apply contention_modifier × 1.08

SUNDAY (Round 4 — final round):
  1. Load Grand Slam narrative if applicable (Rory at Masters, etc.)
  2. Pairing check: back-marker pairs (final group) have crowd pressure advantage
  3. Wind forecast: Open Championship specifically — final round wind can change everything
  4. Clutch_round_4 metric: get_major_record → clutch_round_4 field for pressure
  5. Composite final-round modifier

LIVE IN-ROUND (if monitoring during play):
  Significant events that change the signal:
  - Double bogey on a par 5: -2 to adjusted_score
  - Eagle: +3 to adjusted_score
  - Injury withdrawal mid-round: exit signal immediately
```

---

## Modifier reference (updated)

| Modifier | Source | Range |
|---|---|---|
| `sg_total_modifier` | `get_strokes_gained_profile` | 0.94–1.18 |
| `course_history_modifier` | `get_course_history` | 0.85–1.25 |
| `major_record_modifier` | `get_major_record` | 0.88–1.22 |
| `form_modifier` | `get_player_form_score` | 0.82–1.18 |
| `cut_modifier` | `get_cut_line_status` | 0.00–1.05 |
| `course_fit_modifier` | SG profile + course type | 0.88–1.12 |
| `wind_modifier` | Weather forecast (Open only) | 0.87–1.00 |
| `composite_modifier` | Product of all applicable | 0.65–1.35 |


*MIT License · SportMind · sportmind.dev*
