# Rugby League — Athlete Intelligence

Player-level intelligence for rugby league. Covers NRL (National Rugby League),
Super League, and international competitions (Rugby League World Cup, State of Origin).
Load alongside `sports/rugby-league/sport-domain-rugby-league.md` for full coverage.

---


---

## Commands

| Command | Description |
|---|---|
| `get_pas` | Player Availability Score (0–1.0) for NRL/Super League player |
| `get_form_rating` | Last 6 matches form rating with position-specific metrics |
| `get_pis` | Positional Impact Score — criticality modifier for this position |
| `get_origin_modifier` | State of Origin disruption modifier (NRL window periods) |
| `get_athlete_signal_modifier` | Composite modifier combining PAS, form, PIS, Origin |

## Command reference

### `get_athlete_signal_modifier`

Master composite modifier for rugby league. Combines all sub-components into one multiplier.

**Parameters:**
- `player_id` (required) — NRL or Super League player identifier
- `match_id` (optional) — upcoming match; defaults to next scheduled

**Returns:**
```json
{
  "player": "string",
  "team": "string",
  "pas": 0.90,
  "form_rating": 0.85,
  "pis": 1.10,
  "origin_modifier": 1.00,
  "composite_modifier": 1.05,
  "adjusted_direction": "NEUTRAL_POSITIVE",
  "key_risks": ["State of Origin selection pending"],
  "modifier_reason": "Strong form with full availability"
}
```


## What this skill produces

- **Player Availability Score (PAS)** — Current fitness and selection status
- **Form Rating** — Rolling performance over last 4–6 matches
- **Positional Impact Score (PIS)** — Position-weighted contribution metric
- **Key Player Modifier** — Composite modifier for the athlete modifier pipeline
- **State of Origin flag** — Player's representative status and camp impact

---

## Positional Framework

Rugby league has 13 positions split into forwards (1–8) and backs (9–13 plus
interchange). Positional criticality varies significantly.

```
MOST CRITICAL POSITIONS (injury impact highest):
  Halfback (7):   Primary playmaker — controls all attacking structure
                  Passing, kicking game, line breaks initiated here
                  Absence = entire attack must restructure
                  
  Five-eighth (6): Second playmaker — creates off the halfback
                   Attack width and short-side options run through this position
                   
  Hooker (9):     Dummy half — controls ruck speed and short-range attack
                  Also the primary short-side dummy half runner
                  
  Fullback (1):   Last line of defence + attacking weapon from deep
                  Kick returns, counter-attack, and sweeping
                  
IMPORTANT BUT REPLACEABLE:
  Props (8, 10):  Carry metres and fatigue opposition — interchangeable
  Wingers (2, 5): Try scorers; effectiveness dependent on ball supply
  Centres (3, 4): Defence and outside attack; more replaceable than halves

INTERCHANGE (bench 14–17):
  Modern NRL/Super League: 4 interchange players; 8 interchanges allowed per game
  Prop depth is the most managed via interchange
  Fresh props in second half is a structural team advantage
```

---

## Player Availability Score (PAS)

```
PAS classification:

CONFIRMED (named in 17, no injury concern):      1.00
PROBABLE (named but carrying minor knock):        0.95
LATE CALL / GAME-TIME DECISION:                   0.85
DOUBT (named in extended squad, not confirmed):   0.75
OUT (ruled out, replacement named):               0.00

REPLACEMENT QUALITY:
  When a key player (halfback, hooker, five-eighth) is out:
    Like-for-like quality replacement:    × 0.88
    Step-up from lower grade:             × 0.75
    Out-of-position emergency coverage:   × 0.62

SQUAD NAMING CONVENTIONS (NRL):
  Named Tuesday: extended squad (up to 24 players)
  Confirmed Thursday: 17-man squad
  Final team: 60 minutes before kick-off
  
  Agent rule: Wait for Thursday confirmation for key player status.
  Tuesday extended squads often include players who won't play.
```

---

## Form Rating — Last 6 Matches

```
FORM INPUTS (collect for last 6 matches):
  For forwards: carries, metres per carry, tackle breaks, tackle efficiency
  For backs: try involvements, line break assists, kick return metres
  For halves: try assists, line breaks created, kicking game (metre gained)
  For fullback: kick return metres, line breaks, try contributions

FORM RATING BANDS:
  85–100: Elite form — player operating at top of their game
  70–84:  Good form — consistent above-average contribution
  55–69:  Average form — standard contribution for grade
  40–54:  Below average — mistakes or reduced influence
  < 40:   Poor form — selection pressure likely; below grade

CONSISTENCY METRIC:
  Player rated 70+ in 5 of last 6: Consistent — reliable form signal
  Player with wide variance (2× 85+, 2× 40–): Streaky — high uncertainty
  
RECENT INJURY RETURN:
  First match back from 4+ weeks: × 0.85 form modifier (ring rust)
  Second match back: × 0.93
  Third match back: × 1.00 (baseline restored)
```

---

## State of Origin — Critical Intelligence Variable

State of Origin (NSW Blues vs QLD Maroons) is the most disruptive event in the
NRL calendar and creates unique intelligence requirements.

```
STATE OF ORIGIN IMPACT ON NRL CLUBS:

ORIGIN PERIOD (typically 3 Wednesday nights across May–July):
  Origin players train with state squads Sunday–Wednesday
  Return to NRL clubs Thursday for Friday/Saturday/Sunday games
  
  Origin player in NRL match after Origin game:
    Day after Origin: × 0.88 (physically and mentally drained)
    2 days after Origin: × 0.93
    3+ days after Origin: × 1.00 (recovered)
    
  SELECTION MANAGEMENT:
    Some clubs rest Origin players in the NRL match following Origin
    Check: has the club indicated they'll manage Origin players?
    If rested: treat as OUT for that NRL match
    
MAROON vs BLUE DOMINANCE PERIODS:
  QLD dominated 2006–2013 (8 consecutive series wins)
  NSW resurgence post-2018
  Current form matters more than historical dominance for individual match prediction
  
  Agent rule: Always check if an NRL match falls within 48h of an Origin game.
  This is the single most common form disruption in the NRL calendar.
  
INTERNATIONAL DUTY (Rugby League World Cup, Test matches):
  Similar disruption to Origin but less frequent
  Southern Hemisphere players: Kangaroos (AUS), Kiwis (NZ)
  Northern Hemisphere: England, Samoa, Tonga, Fiji
  Check international window dates before any NRL/Super League match prediction
```

---

## Positional Impact Score (PIS)

```
PIS = (form_rating × positional_weight × availability_modifier) / 100

POSITIONAL WEIGHTS for PIS calculation:
  Halfback (7):       1.35 — highest individual impact
  Five-eighth (6):    1.25
  Hooker (9):         1.20
  Fullback (1):       1.15
  Prop (8 or 10):     0.90 (pairs — one absence less critical)
  Lock (13):          1.05
  Second-row (11,12): 0.95
  Centres (3,4):      1.00
  Wingers (2,5):      0.90

SQUAD PIS:
  Sum of PIS for all 13 starting players
  Baseline squad PIS ~100 (average NRL squad in average form)
  Strong squad in good form: 108–115
  Depleted squad with injuries: 85–95

AGENT RULE: Compare squad PIS for both teams.
  PIS differential > 10: meaningful quality advantage
  PIS differential > 18: significant favourite signal
  PIS differential < 5: treat as even; look to other factors
```

---

## Key Player Composite Modifier

For the Layer 2 athlete modifier pipeline:

```
key_player_modifier = availability × form × fatigue × Origin_adjustment

availability:   See PAS table above
form:           0.82–1.20 (mapped from form rating bands)
fatigue:        1.00 standard | 0.92 post-Origin (within 48h) | 0.95 third game in 8 days
Origin:         0.88 if playing NRL within 24h of Origin match
                1.00 if not in Origin squad or sufficient recovery time

KNOCKOUT CONDITIONS:
  Both halves (6+7) confirmed out:     floor 0.55 — attack collapses
  Halfback AND hooker out:             floor 0.58
  3+ key players out (any position):   floor 0.62
```

---

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` for the full framework.
Rugby league-specific notes:
- High-contact sport: shoulder, knee (ACL), and ankle injuries most common
- ACL injuries are career-disrupting at same rate as football (9–12 month recovery)
- Concussion protocols: strict in NRL post-2020; player withdrawn same day
- "Managed" props: often rotated even when fit — check if absence is load management
- Interchange: a player listed as interchange may be managing a knock — not fully fit

## Data Sources

- **NRL official (nrl.com)**: Team lists, injury updates, interchange tracking
- **Super League (superleague.co.uk)**: Squad announcements, match previews
- **Zero Tackle**: NRL injury and team news aggregator
- **League Unlimited**: NRL player statistics and form data
- **Rugby League Project**: Historical statistics database

## Integration example

### NRL / Super League pre-match workflow

```
# Step 1: Load domain context
Load sports/rugby-league/sport-domain-rugby-league.md

# Step 2: Check availability and form
get_pas player=[PLAYER_ID]
get_form_rating player=[PLAYER_ID]

# Step 3: Check State of Origin window
get_origin_modifier team=[TEAM_ID] — applies during May–July NRL window

# Step 4: Get composite modifier
get_athlete_signal_modifier player=[PLAYER_ID] match=[MATCH_ID]

# Step 4: Decision logic
# If composite_modifier >= 1.10 AND adjusted_score >= 65 → ENTER
# If origin_modifier active AND 3+ key players affected → REDUCE or ABSTAIN
# Output: SportMind confidence schema
```


## Compatibility

**Sport domain:** `sports/rugby-league/sport-domain-rugby-league.md`
**Injury intelligence:** `core/injury-intelligence/core-injury-intelligence.md`

---

*MIT License · SportMind · sportmind.dev*
