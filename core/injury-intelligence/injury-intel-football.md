# Injury Intelligence — Football / Soccer

Sport-specific injury intelligence for football. Applies the core framework from
`core/injury-intelligence/core-injury-intelligence.md` to football's unique dynamics.
Load both files for full football injury intelligence.

---

## What makes football injury intelligence different

Football has the largest squad depth variance of any team sport. The same injury
— losing a left back — is trivially absorbed by Manchester City and catastrophic
for a newly promoted side with one recognised left back and a converted midfielder
as cover. The injury is identical; the impact is completely different.

Three things make football injury intelligence uniquely complex:

**1. Positional depth asymmetry** — Clubs invest unevenly. A Champions League club
will have €50M centre-backs as cover; their left wing cover might be an academy player.
Injury impact cannot be assessed without knowing the specific depth at that position.

**2. Partnership disruption** — Centre-back pairings, holding midfield partnerships,
and striker-AM combinations take 10–20 matches to build coherent communication.
Breaking a partnership by injury is not equivalent to losing one player — it disrupts
two players' effectiveness simultaneously.

**3. Set piece dependency** — 25–30% of goals in top-division football come from set
pieces. If the club's corner and free-kick taker is injured, the team loses a disproportionate
amount of their attacking output relative to what basic stats suggest.

---

## Football-specific positional criticality

### Goalkeeper
The highest-criticality position in football. A single injury affects:
- The entire defensive structure (communication, organisation)
- Distribution (sweeper-keeper style vs traditional)
- Set piece organisation (both defensive and attacking)
- Penalty saves

```
Goalkeeper injury modifier:
  Starting GK out → first-choice backup starting:     × 0.80–0.88
  Starting GK out → third-choice / youth GK:          × 0.65–0.72
  Backup GK already established (5+ matches):         × 0.85–0.92
  
  Key question: has the backup GK played competitive minutes this season?
    Yes (5+): standard backup modifier
    No (0–4): apply additional × 0.93 (rust factor)
```

### Centre-backs
Partnership disruption is the critical variable. A well-established CB pair
(20+ matches together) that is split by injury loses more than just one player's rating.

```
CB partnership disruption modifier:
  Partnership 0–5 matches together:      no additional penalty (not yet established)
  Partnership 6–15 matches:              × 0.95 disruption penalty on remaining CB
  Partnership 16–30 matches:             × 0.92 disruption penalty
  Partnership 30+ matches (strong unit):  × 0.88 disruption penalty
  
  Emergency CB (midfielder / converted):  apply × 0.72 positional modifier
  Opposing team has target striker (aerial): amplify CB absence penalty × 1.15
```

### Strikers / forwards
Assessed primarily by goals-per-90 and xG contribution. Replacement quality delta
is most acute at striker because goals are the scarcest and most matchup-specific output.

```
Top scorer / main striker out:
  Replacement has similar goals-per-90:    RQD 0.10–0.15 (reasonable cover)
  Replacement is a secondary option:       RQD 0.25–0.35 (meaningful drop)
  Replacement is a converted midfielder:   RQD 0.40–0.55 (structural problem)
  No natural replacement exists:           RQD 0.55+ (severe loss)

  Special case: target man / aerial threat out vs opponent with aerial weakness:
    This matchup advantage disappears entirely → apply additional × 0.90
```

### Holding midfielders
Underrated in market impact but significant for defensive stability. The holding
midfielder is often the defensive spine — their absence creates exposure across
the entire back line.

```
Key holding midfielder out:
  Direct specialist replacement:     RQD 0.10–0.20
  Box-to-box cover (less defensive): RQD 0.25–0.35 + × 0.92 defensive transition
  Attacking midfielder covering:     RQD 0.40+ (defensive liability created)
```

### Full-backs
Modern full-backs are critical attacking outlets. An attacking full-back injury
removes both defensive coverage AND attacking width and crosses.

```
Attacking full-back out:
  Like-for-like replacement:              RQD 0.10–0.20
  Defensive specialist covering:          RQD 0.25–0.35 (attacking output lost)
  Youth player / emergency cover:         RQD 0.40+
  
  Opposition attacks down that flank specifically: amplify × 1.10
```

---

## Set piece specialist loss

Set pieces account for 25–30% of top-division goals. This is the most
underpriced injury effect in football.

```
IDENTIFY SET PIECE SPECIALISTS:
  Corner taker (in-swinger vs out-swinger — different threat to keeper)
  Direct free-kick threat (within 25m of goal)
  Penalty taker (primary and backup)
  Near-post attacker / aerial threat at corners
  Set piece defensive organiser

SET PIECE LOSS MODIFIERS:
  Primary corner/free-kick taker out:   × 0.95 (attacking output loss)
  Primary penalty taker out:            × 0.97 (penalty probability event only)
    — only material if penalty awarded is likely
  Aerial threat out (vs aerial-weak keeper): × 0.94
  
  Multiple set piece specialists out:   × 0.91 (compound)
  Defensive set piece organiser out:    × 0.94 on clean sheet probability
```

---

## International duty injury — the reverse spillover problem

Injuries sustained during international duty are the most damaging for club tokens:
- The club had no control over the training load or match intensity
- The injury often arrives mid-season with no preparation time for the manager
- Replacement options may already be depleted from pre-international injury list

```
INTERNATIONAL INJURY RISK WINDOWS:
  International break (every ~2 months): highest risk window for club injury
  
  Pre-break club action: check which players are travelling to high-risk fixtures
    High-risk: competitive internationals, long-haul travel (jet lag + game)
    Lower risk: local friendlies, training camp only
    
  Post-break monitoring: check every player on return
    Any player not training day 1 of return = flag as potential injury
    
INTERNATIONAL INJURY MODIFIER ON CLUB TOKEN:
  Key player injured on international duty:
    Minor injury (Tier C, 1 week):     × 0.95 (short window, recovers quickly)
    Moderate injury (Tier B, 4–8 wks): × 0.80 (mid-season hole)
    Serious injury (Tier A):           × 0.65 (season-altering, club had no say)
    
  Apply additional sentiment penalty: fan frustration at club having no control
  amplifies negative token sentiment by estimated × 0.95 beyond pure performance impact.
```

---

## Congested fixture list — cumulative injury risk

When clubs play 3 matches in 7 days, soft-tissue injury probability rises significantly.
This is a predictive signal, not just a reactive one.

```
INJURY PROBABILITY ELEVATION BY FIXTURE DENSITY:
  1 match per 7 days (normal):           Baseline injury probability
  2 matches per 7 days:                  +15% soft-tissue injury probability
  3 matches per 7 days:                  +35% soft-tissue injury probability
  3 matches in 5 days:                   +55% (emergency congestion)
  
  Highest risk players in congested periods:
    Hamstring: explosive players (wingers, strikers)
    Calf: players who cover most distance (fullbacks, box-to-box midfielders)
    Groin: players with recent adductor history
    
  Agent rule: entering a position ahead of a congested fixture block → apply
  pre-emptive × 0.95 to account for elevated unplanned injury risk.
```

---

## Manager injury language decoder

Football managers routinely obscure injury information. This decoder translates
common press conference phrases to actual probability assessments:

| Manager quote | Actual meaning | Availability probability |
|---|---|---|
| "He'll be fine, just a knock" | Minor issue, almost certainly playing | 85–95% |
| "We'll assess him in the morning" | Genuine doubt, probably 50/50 | 40–60% |
| "He won't be available for selection" | Definite out | 0% |
| "He's working hard in training" | Not fully fit, not playing | 5–15% |
| "We'll make a late decision" | Manager doesn't know / keeping opponent guessing | 40–65% |
| "He's not quite ready" | Returning from injury, won't be rushed | 0–20% |
| "We have to be careful with him" | Recurrence risk concern | 15–30% |
| "He's back in training with the group" | Weeks away from match fitness | 20–40% |
| "He's back in full training" | Close — probably 1–2 weeks | 50–70% |
| "He looked sharp in training today" | Likely playing | 70–85% |
| "It's up to him to prove his fitness" | Player wants to play but staff are cautious | 35–55% |

---

## Return-to-play curve — football specific

Beyond the core framework curves, football has position-specific recovery patterns:

```
GOALKEEPER return from Tier B:
  Reflexes and shot-stopping return quickly (physical)
  Positional organisation / communication: -8% below baseline for 4 matches
  Distribution / sweeping: -5% below baseline for 3 matches
  Apply: × 0.92 for first 3 matches even if "fully fit"

STRIKER return from Tier B (lower body):
  Explosive movement (shooting, turning): -15–20% for first 4 matches
  Hold-up play / linking: recovers faster
  Apply: × 0.82 (matches 1–3), × 0.90 (matches 4–6)

CENTRE-BACK return from any injury (aerial/physical):
  Physical confidence in aerial duels takes 4–6 matches to rebuild
  Subconscious protection of injured area changes positioning
  Apply: × 0.88 (matches 1–4), × 0.95 (matches 5–8)
```

---

## Squad depth scoring — practical guide

To compute RQD for a football club, estimate the quality gap at the injured position:

```
QUALITY TIER SYSTEM (0–100 rating by position in league context):
  Elite (85–100): Top-5 in position in their league
  Premium (70–84): Top-15 in position
  Quality (55–69): Regular starter at mid-table
  Average (40–54): Fringe / rotation player
  Below average (<40): Youth / emergency cover
  
EXAMPLE:
  Injured: First-choice GK rated 82 (Premium)
  Replacement: Backup GK rated 65 (Quality)
  RQD = (82 - 65) / 82 = 0.207 → Moderate loss (× 0.88 modifier)
  
  Injured: First-choice striker rated 88 (Elite)
  Replacement: Converted winger rated 55 (Quality)
  RQD = (88 - 55) / 88 = 0.375 → Major loss (× 0.72 modifier)
```

---

## Injury intelligence integration with fan-token skills

Football injuries feed directly into Layer 3 fan token skills:

```
→ fan-token-pulse: injury to key player within 48h of match
  Expected: HAS decline begins within 12h of confirmed injury news
  TVI goes negative as holders sell on negative narrative
  
→ token-intelligence-football: ATM of injured player
  High-ATM player injured (1.20+): apply ATM loss to FTIS calculation
  ATM × 0 while injured + partial ATM restoration on return
  
→ fan-token-performance-on-pitch: PI recalculation
  Return-to-play curve applies directly to PI predictions
  Valuation multiplier should be adjusted down for returning players
  
→ fan-token-performance-off-pitch: rehabilitation tracking
  This skill handles the full rehab phase — load this for detailed rehab intel
```

---

## Data sources

- **Transfermarkt injury history**: `https://transfermarkt-api.fly.dev/players/{id}/injuries`
- **PhysioRoom.com**: Historical injury records (public)
- **Sofascore**: In-match injury events
- **BBC Sport / Sky Sports**: Manager press conference injury quotes
- **Official club websites**: Team news section (most reliable but latest)
- **Twitter/X club accounts**: Pre-match squad announcements

---

*MIT License · SportMind · sportmind.dev*
