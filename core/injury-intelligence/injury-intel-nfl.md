# Injury Intelligence — American Football (NFL)

Sport-specific injury intelligence for the NFL. Applies the core framework from
`core/injury-intelligence/core-injury-intelligence.md` to the NFL's unique and
highly structured injury reporting system.
Load both files for full NFL injury intelligence.

---

## What makes NFL injury intelligence different

The NFL has the most institutionalised injury reporting system in professional sport.
Federal gambling regulations and league rules legally mandate a structured injury
disclosure process across the week. This creates an intelligence advantage for agents
who understand how to read it — the designation system is highly predictive when
interpreted correctly.

Two things make NFL injury intelligence uniquely valuable:

**1. The designation system is structured and predictive** — Wednesday practice
participation is the most predictive single input for Sunday game availability,
more so than any statement from coaches or players.

**2. Position criticality is extreme and asymmetric** — An NFL starting quarterback
is the most positionally critical athlete in team sport. No other position carries as
much team outcome determination through one individual. A backup QB starting is not
a degraded version of the same system — it is a fundamentally different team.

---

## The NFL injury designation system

The NFL requires teams to submit injury reports on Wednesday, Thursday, and Friday
of each game week. Practice participation is categorised as:

```
PRACTICE PARTICIPATION DESIGNATIONS:

  Full Participant (FP):   Player participated fully in practice
  Limited Participant (LP): Player participated on a limited basis
  Did Not Participate (DNP): Player did not practice

GAME DESIGNATIONS (added Friday):

  Questionable (Q):    50% probability of playing
  Doubtful (D):        25% probability of playing (rare designation — usually means out)
  Out:                 Will not play this game
  IR (Injured Reserve): Out for remainder of season (or 4+ games — rules vary by year)
  PUP (Physically Unable to Perform): Season-long; set before season starts
  
Note: "Probable" designation was eliminated in 2016.
```

### Reading the weekly progression

```
WEDNESDAY:
  FP on Wednesday: almost certainly fine
  LP on Wednesday: typical — not significant alone
  DNP on Wednesday: yellow flag — watch Thursday
  
THURSDAY:
  FP after DNP Wednesday: improving — likely available
  LP after LP Wednesday: managed week — probable
  DNP after DNP Wednesday: red flag — significant risk
  
FRIDAY (most predictive day):
  FP on Friday: very likely playing (90%+)
  LP on Friday: likely playing with limitation (70–80%)
  DNP on Friday: very unlikely to play (5–20%)
  
  GAME DESIGNATION + FRIDAY PRACTICE:
    Questionable + FP Friday:  75–85% chance of playing
    Questionable + LP Friday:  50–65% chance of playing
    Questionable + DNP Friday: 15–30% chance of playing
    Doubtful + any practice:   10–20% chance of playing
    Out:                       0% (barring error)
```

---

## Quarterback — the NFL's unique critical position

No position in any team sport has the outcome dependency of the NFL quarterback.
The QB touches the ball on every offensive snap. The entire offensive system,
play-calling, protection schemes, route trees, and audible language are calibrated
to one player.

```
QUARTERBACK INJURY TIERS:

TIER 1: ELITE STARTER (top 5 in league by WAR / CPOE / EPA)
  Out → backup starts:
    If backup is experienced starter (previous starting record):  × 0.65
    If backup is a developmental QB (< 10 career starts):        × 0.55
    If backup is a practice squad emergency elevation:           × 0.45
    
TIER 2: QUALITY STARTER (top 6–15 in league)
  Out → backup starts:
    Experienced backup:    × 0.72
    Developmental backup:  × 0.60
    Emergency elevation:   × 0.50
    
TIER 3: AVERAGE/BACKUP STARTER (16–32 in league)
  Out → backup starts:
    Experienced backup:    × 0.80
    Developmental backup:  × 0.68
    
TIER 4: BACKUP ALREADY STARTING (starter already injured)
  QB3 elevation to QB2 role:
    × 0.85 if QB2 is healthy (team is already compensating)
    × 0.65 if QB2 is also limited
    
IMPORTANT: These are team-level output modifiers, not individual stats modifiers.
The team with a Tier 1 QB injury is not just missing that QB — they are running
a fundamentally different offensive system that the line, receivers, and play-caller
have not practised for this week.
```

### QB injury types and their specific impacts

```
THROWING ARM INJURIES (shoulder, elbow, wrist, finger):
  Affect: accuracy, arm velocity, throw distance
  Critical for: deep routes, out-breaking routes, receivers in tight coverage
  Watch for: altered throwing motion in practice video, shorter throws in warmup
  
LOWER BODY INJURIES (ankle, knee, foot):
  Affect: mobility, pocket movement, scramble threat
  Particularly damaging for: running/mobile QBs (Lamar Jackson archetype)
  Less damaging for: pocket passers (Tom Brady archetype — designed to be stationary)
  Watch for: limited mobility in Thursday/Friday practice videos
  
HEAD INJURIES (concussion protocol):
  NFL concussion protocol is strict and externally enforced
  Player cannot return to practice until cleared by independent neurologist
  "In protocol" = NOT available until official clearance
  Agent rule: Any QB "in concussion protocol" should be treated as OUT until
  official clearance is confirmed by independent doctor, not just team.
  
RIB/TORSO INJURIES:
  Affect: throwing mechanics, core rotation, pain on impact
  Hard to assess — QBs rarely admit rib injuries
  Watch for: limited follow-through on longer throws, guarded posture
```

---

## Non-QB positional intelligence

### Offensive Line — the most underrated injury in NFL betting markets

Offensive line injuries are consistently underpriced by markets and consistently
impactful on outcomes. The reason: O-line quality is invisible in standard stats
but determines everything about the QB's performance and the running game.

```
LEFT TACKLE (LT — protects QB blind side):
  Loss of quality LT:
    Pocket QB against strong pass rush: × 0.85 (sack rate increases sharply)
    Mobile QB: × 0.90 (can escape pressure)
    Backup LT (experienced starter): × 0.92
    Backup LT (developmental):      × 0.80
    
RIGHT GUARD / CENTER (interior line):
  Loss affects: interior blitz pickup, short-yardage runs, snap-QB exchange
  Modifier: × 0.93 (less critical than tackle but meaningful)
  
MULTIPLE O-LINE INJURIES (2+ starters out):
  Running game: × 0.72 (cannot establish line surge)
  Pocket passing: × 0.78 (protection collapses)
  This is the highest-impact "invisible" team injury pattern in the NFL.
```

### Running backs

```
PRIMARY BALL-CARRIER out:
  Pass-catching RB backup:     RQD 0.10–0.20 (some teams use committee anyway)
  Pure runner backup:          RQD 0.20–0.35
  Practice squad elevation:    RQD 0.35–0.45
  
  Note: Many teams run a committee — RB injury is less impactful than equivalent
  skill position injury. Check team's RB committee approach first.
```

### Wide receivers

```
WR1 (top target — 25%+ of team's targets) out:
  Slot receiver moves outside:  RQD 0.25–0.35 (route tree narrows)
  Depth receiver:               RQD 0.30–0.40
  
  Special case: only red zone threat out:
    Team loses goal-line separation tool
    Scoring ability drops sharply inside 20 yards
    Additional × 0.92 for scoring output predictions
    
WR2 out: RQD 0.15–0.25 (target redistribution manageable)
```

### Defensive positions

```
PASS RUSHER (elite — 10+ sacks per season):
  Out: QB protection of opponent improves; passing game opens
  Team sack rate: -30–40% without elite edge rusher
  
  For opponent prediction: × 1.08 on passing output (QB has more time)
  For own team token: × 0.92 (defensive vulnerability increases)
  
CORNERBACK (shadow coverage specialist):
  Coverage of elite WR now falls to backup:
  CB quality drop × WR1 target rate = coverage disruption multiplier
  
MIDDLE LINEBACKER (defensive signal caller):
  Play communication breaks down; pre-snap adjustments slow
  Modifier: × 0.93 on defensive unit performance
```

---

## Practice squad promotion patterns

When injuries occur during the week, teams can promote players from the practice squad.
These players have specific risk profiles:

```
PRACTICE SQUAD PLAYER:
  Was on active roster but cut:    Likely adequate but below starter level
  Never on active roster:          Unknown quantity; high variance in performance
  Recently released by another team: Often carries own injury/form concerns (why released?)
  
  Agent rule: Any practice squad emergency promotion to key role:
    Apply minimum × 0.78 modifier until on-field performance confirms quality.
```

---

## Cumulative season injury — load management and wear

NFL players accumulate physical damage across a 17-game season plus playoffs.
By Week 14+, many starters are playing through Tier C and low Tier B injuries
that would sideline players in other sports.

```
LATE SEASON ADJUSTMENT (Weeks 13–18):
  Most key players are managing minor injuries by this point.
  "Full participant" in Week 15 does not mean the same as Week 3.
  
  Apply general late-season impairment: × 0.97 on skill positions (fatigue/wear)
  Exception: teams on bye in Weeks 9–14 reset to × 1.00 (rest benefit)
  
  High-collision positions (RB, DB, LB): × 0.95 by Week 14 (cumulative wear)
  QB on well-protected team: × 1.00 (protected position degrades slower)
  QB on high-sack-rate team: × 0.95 by Week 12 (accumulating physical toll)
```

---

## Weather and injury interaction

NFL weather is an additional injury risk and performance variable unique to outdoor stadiums:

```
COLD WEATHER (below 20°F / -7°C):
  Muscle injury probability: +15% (cold muscles, reduced elasticity)
  Wide receiver separation: -8% (routes tighter in cold/heavy gear)
  Kicker accuracy: -12% at 30+ yard attempts
  Ball handling: increased fumble probability
  
RAIN / WET FIELD:
  Receiver route running: -10% separation
  Ball handling: +15% fumble probability
  Kicker accuracy: -8%
  Rushing game: advantage (slower pursuit angles)
  
WIND (> 15mph):
  Passing game effectiveness: -15% per 10mph above 15mph
  Kicking (FG, XP, kickoffs): significant accuracy reduction
  Deep passing game: effectively eliminated at 25mph+
```

---

## Data sources

- **NFL official injury reports**: nfl.com/injuries (mandatory weekly publication)
- **Pro Football Reference**: Historical injury and game data
- **Rotoworld / RotoBaller**: Real-time injury news with practice reports
- **ESPN NFL Insider**: Beat reporter injury intelligence
- **Twitter/X beat reporters**: Fastest injury news (team-specific beat reporters)
- **Fantasy football platforms**: Often fastest aggregators for practice report news

---

*MIT License · SportMind · sportmind.dev*
