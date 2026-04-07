# Ice Hockey (NHL) — Athlete Intelligence

Player-level intelligence for NHL fan tokens. Covers goaltender starts, special teams personnel, possession metrics, line combinations, and individual skater output.

---

## Commands

| Command | Description | Auth |
|---|---|---|
| `get_goaltender_start` | Confirmed starter, save %, high danger metrics | Yes |
| `get_special_teams_personnel` | PP unit composition, PK deployment | Yes |
| `get_possession_metrics` | Corsi, Fenwick, xGF% per player | Yes |
| `get_line_combinations` | Current confirmed lines, historical chemistry | Yes |
| `get_skater_output` | Goals, points, shots, physical metrics per 60 | Yes |
| `get_athlete_signal_modifier` | Composite NHL modifier | Yes |
| `get_injury_report` | IR list, day-to-day designations | Yes |

---

## Key metrics

### `get_goaltender_start`
```json
{
  "token": "NHL_TOKEN",
  "starter": {
    "name": "Juuse Saros",
    "status": "CONFIRMED",
    "save_pct_last_10": 0.921,
    "gaa_last_10": 2.42,
    "high_danger_save_pct": 0.847,
    "goals_saved_above_average": 8.2,
    "back_to_back_flag": false,
    "backup": "Kevin Lankinen",
    "backup_quality_delta": -14
  },
  "signal_modifier": 1.08
}
```

### `get_special_teams_personnel`
```json
{
  "token": "NHL_TOKEN",
  "power_play": {
    "pp1_unit": ["A. Matthews", "M. Marner", "W. Nylander", "J. Tavares", "M. Rielly"],
    "pp1_pct_season": 28.4,
    "key_player_available": true
  },
  "penalty_kill": {
    "pk_pct_season": 82.1,
    "key_penalty_killer_available": true
  },
  "special_teams_modifier": 1.06
}
```

---

## NHL modifier table

| Condition | Modifier |
|---|---|
| Starting GK confirmed, save% >0.920 | 1.10 |
| Backup GK starts | 0.80 |
| Star forward out | 0.85 |
| PP1 unit fully intact | 1.06 |
| Back-to-back (starting same GK) | 0.90 |


---

## Integration example

### NHL Ice Hockey pre-event workflow

```
# Step 1: Load domain context
Load sports/nhl/sport-domain-nhl.md

# Step 2: Check athlete availability and form
get_availability token=[NHL]
get_form_score token=[NHL]

# Step 3: Get composite modifier
get_athlete_signal_modifier token=[NHL]

# Step 4: Decision logic
# If composite_modifier >= 1.10 AND adjusted_score >= 65 → ENTER at standard size
# If composite_modifier 1.00–1.09 → ENTER at 70% size
# If composite_modifier < 1.00 OR injury_warning = true → WAIT or ABSTAIN
# Output: SportMind confidence schema (core/confidence-output-schema.md)
```

**See:** `core/confidence-output-schema.md` for full output format.

## Command reference

### `get_athlete_signal_modifier`

Master composite modifier. Combines all sport-specific sub-components into one multiplier.

**Parameters:**
- `player_id` (required) — player or team identifier
- `match_id` (optional) — specific event; defaults to next scheduled

**Returns:**
```json
{{
  "player": "string",
  "availability": 1.0,
  "form_modifier": 1.05,
  "sport_specific_modifier": 1.02,
  "composite_modifier": 1.07,
  "adjusted_direction": "POSITIVE",
  "confidence": 0.85,
  "key_risks": ["string"],
  "modifier_reason": "string"
}}
```

---

## GSAx — Goals Saved Above Expected (full model)

GSAx is the single most important individual statistic in NHL signal analysis.
It measures how many goals a goaltender prevented beyond what an average goaltender
would have saved against the same shot quality.

```
GSAx CALCULATION:
  GSAx = Actual_Goals_Saved - Expected_Goals_Saved
  Expected_Goals_Saved = sum of (1 - xG) for every shot faced

  Where xG (expected goals) accounts for:
    Shot location (distance + angle from net)
    Shot type (wrist, slap, backhand, deflection)
    Rush vs set play context
    Rebound vs first shot

GSAx INTERPRETATION:
  > +15 per season:    Elite — top 3-5 goalies in NHL
  +8 to +15:          Very good — clear starter quality
  +3 to +8:           Above average — solid starter
  -3 to +3:           League average — replacement level
  -3 to -8:           Below average — concern signal
  < -8:               Liability — strong negative signal

GSAx MODIFIER FORMULA:
  gsax_modifier = 1.00 + (GSAx_per_60_minutes × 0.012)

  Per-60 normalisation matters: a goalie who has played 15 games has less
  sample than one who has played 45. Apply per-60 for fair comparison.

MOMENTUM COMPONENT:
  Last 10 games GSAx vs season GSAx:
    Last 10 > season by 3+: form_modifier × 1.05 (hot goalie)
    Last 10 < season by 3+: form_modifier × 0.93 (cold goalie)

BACKUP QUALITY DELTA:
  If starter confirmed out and backup starts:
  quality_delta = starter_GSAx - backup_GSAx
  Modifier = 0.80 + max(0, quality_delta × -0.015)
  At delta -10: modifier 0.80 (backup is 10 GSAx worse — large negative)
  At delta -20: modifier 0.65 (severe quality drop)
```

## Morning skate protocol

```
MORNING SKATE INTELLIGENCE (NHL-specific):

The morning skate (typically 10-11am on game day) is the primary goaltender
confirmation window. It is the NHL equivalent of football's T-2h lineup.

MORNING SKATE SIGNALS:
  Starter confirmed on the ice: lineup_unconfirmed = False → standard analysis
  Starter absent from skate: lineup_unconfirmed = True → apply backup modifier
  Starter skates but looks limited: flag for monitoring → partial confidence reduction
  No morning skate (team's choice, rare): no information → maintain lineup_unconfirmed

TIMING:
  Morning skate: ~T-8h before puck drop
  Some teams post official lineup ~1-2h before game
  NHL mandates lineup submission ~1h before game

AGENT RULE: Never confirm goaltender start until morning skate report.
  Apply lineup_unconfirmed until morning skate confirms starter on ice.
  This is the most important single timing rule in NHL signal analysis.
```

## Special teams intelligence

```
POWER PLAY (PP) SIGNAL MODEL:

PP1 Unit composition is a team-level variable, not just a player variable.
A power play requires 5 players — the departure or absence of any one changes
the unit's effectiveness.

PP TIER CLASSIFICATION (by season PP%):
  Elite PP:    >28% — PP1 activations are positive signal amplifiers
  Good PP:     24-28% — solid; standard weighting
  Average PP:  20-24% — no special modifier
  Weak PP:     <20% — negative signal; team over-reliant on even-strength

PP1 unit fully intact + elite PP: modifier × 1.08
PP1 unit missing key player:      modifier × 0.94
Team entering game with PP deficit (playing in heavy foul trouble): × 0.92

PENALTY KILL (PK) SIGNAL:
  Elite PK:   >85% — allows more physical play; positive modifier
  Poor PK:    <78% — negative; opponent will seek penalties
  
COMBINED SPECIAL TEAMS MODIFIER:
  combined_modifier = (PP_modifier + PK_modifier) / 2

  Top PP + top PK: × 1.07
  Top PP + poor PK: × 1.02 (benefits offset)
  Poor PP + poor PK: × 0.90
```

## Canadian market signal intelligence

```
CANADA — 30% OF NHL REVENUE FROM 7 FRANCHISES:

Canadian market characteristics:
  Per-capita viewership: 3× US average
  Crypto adoption in sports: ~12-15% of hockey fans
  Top fan token readiness: Toronto Maple Leafs, Montreal Canadiens
  
TORONTO MAPLE LEAFS:
  Largest English-speaking Canadian hockey market
  Last Stanley Cup: 1967 — 50+ year drought creates enormous narrative
  Any deep playoff run: maximum NCSI Canada × 1.25
  
MONTREAL CANADIENS:
  24 Stanley Cups (most in NHL)
  French-Canadian market + passionate diaspora
  Bilingual (French/English) token engagement profile
  
EDMONTON OILERS / CALGARY FLAMES:
  Alberta oil economy + hockey culture = high-spending fan demographic
  
PLAYOFF SIGNAL MULTIPLIERS (Canadian teams):
  First round: × 1.10 (expected but fans engaged)
  Second round: × 1.20
  Conference Final: × 1.35 (near the Cup — national media surge)
  Stanley Cup Final: × 1.50 (50+ year wait narrative at peak)
```

## Draft and trade deadline intelligence

```
NHL DRAFT (June):
  First overall pick: franchise-defining; token signal peak for that franchise
  Top-5 pick: significant positive signal
  Top-10 pick: moderate positive
  Later rounds: minimal token signal

TRADE DEADLINE (March 3):
  Buyer deadline additions:
    Top-6 forward added: × 1.08 for acquiring team
    Elite goaltender rental: × 1.10 (significant upgrade signal)
    
  Seller signals:
    Rental player traded away: neutral to × 0.95 (not retaining talent)
    Core player traded: negative × 0.85 (rebuild signal)
    
  AGENT RULE: Any trade involving a top-pairing defenceman or elite goaltender
  → reload analysis immediately for both clubs involved
  
WAIVERS:
  Player put on waivers: always check — either team is trying to assign
  to AHL (depth signal) or actively shopping (trade signal)
  High-profile waiver: negative signal for placing team
```

## Integration: Full NHL pre-game workflow

```
Step 1: Load domain context
  Load sports/nhl/sport-domain-nhl.md

Step 2: MORNING SKATE CHECK (most important step)
  get_goaltender_start — confirmed starter or backup?
  If backup: apply quality_delta modifier; adjust position size to 65%
  
Step 3: GSAx assessment
  get_goaltender_start → GSAx season, GSAx last 10
  Apply gsax_modifier and momentum component
  
Step 4: Special teams check
  get_special_teams_personnel
  PP1 unit intact? Elite/weak PP%?
  Apply combined_modifier
  
Step 5: Back-to-back flag
  get_injury_report → is this B2B second game?
  If yes AND same goalie starting: apply × 0.90
  
Step 6: Composite modifier
  get_athlete_signal_modifier (combines all above)
  
Step 7: Decision
  GSAx > +8 + PP intact + no B2B: ENTER standard size
  GSAx < 0 OR backup starts: REDUCE or WAIT
  B2B second game with elite GSAx starter: ENTER at 65%
```


*MIT License · SportMind · sportmind.dev*
