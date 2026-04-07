# Core Injury Intelligence — SportMind Master Framework

The shared injury intelligence layer for all SportMind skills. Establishes the taxonomy,
scoring methodology, modifier pipeline, and agent reasoning patterns that every sport-specific
injury module builds on.

Load this file alongside any athlete skill or sport domain skill when injury context is needed.
Sport-specific files in `core/injury-intelligence/` apply this framework to each sport's
unique injury dynamics.

---

## Why injury intelligence is a distinct layer

Injury information is the highest-frequency, highest-impact signal variable in sports
intelligence. It is also the most abused — surface-level availability checks miss the
nuance that determines whether an injury actually changes the prediction:

- A goalkeeper with a finger injury is available but functionally impaired in ways the
  official team sheet doesn't capture
- A striker returning from a 10-week hamstring tear will underperform their pre-injury
  metrics for 6–10 matches regardless of what the manager says publicly
- A team missing its starting centre-back loses more expected value when facing a tall
  striker than when facing a small, quick forward — the matchup matters
- The replacement quality delta is often more important than the injury itself

This framework moves beyond binary availability (fit / not fit) to a multi-dimensional
injury signal that agents can use to make calibrated decisions.

---

## The injury signal stack

```
LAYER 1 — Injury detection
  What happened? Type, severity, mechanism.

LAYER 2 — Timeline estimation
  How long is this player out? What is the recovery range?

LAYER 3 — Return-to-play curve
  When they come back, how impaired are they and for how long?

LAYER 4 — Replacement quality delta
  Who replaces them, and how much does the team lose?

LAYER 5 — Squad depth stress
  Can the team absorb this, or is it a structural problem?

LAYER 6 — Modifier output
  What number does all of this produce for the composite modifier?
```

---

## Injury type taxonomy

### Tier A — Catastrophic (career risk or season-ending)
Recovery: 6+ months. Team impact: severe and sustained.

| Type | Typical recovery | Recurrence risk | Notes |
|---|---|---|---|
| ACL rupture | 9–12 months | High (15–25%) | Most common career-altering injury |
| Achilles tendon rupture | 8–12 months | Moderate | Often changes playing style permanently |
| Multiple ligament (knee) | 10–14 months | Very high | Rare; near career-ending |
| Broken leg (fibula/tibia) | 4–8 months | Low | Timeline varies significantly |
| Spinal injury | Highly variable | — | Requires specialist assessment |
| Serious head trauma | Highly variable | — | Concussion protocol applies |

**Agent rule:** Any Tier A injury to a key player is a hard modifier floor event.
Do not attempt to estimate performance impact beyond "severe and sustained."
Exit or avoid positions until return-to-play is confirmed.

### Tier B — Significant (weeks to months, material impact)
Recovery: 4–12 weeks. Team impact: meaningful but recoverable.

| Type | Typical recovery | Recurrence risk | Notes |
|---|---|---|---|
| Hamstring (Grade 2–3) | 4–8 weeks | Very high (30–40%) | Most common in explosive sports |
| Hamstring (Grade 1) | 1–3 weeks | High (20–30%) | Often managed rather than rested |
| Knee ligament (MCL/LCL) | 4–8 weeks | Moderate | Depends on grade |
| Ankle ligament | 3–8 weeks | Moderate-high | Surface and playing style dependent |
| Calf strain (Grade 2) | 3–6 weeks | High | Often precedes hamstring |
| Hip flexor | 2–6 weeks | Moderate | Common in kicking sports |
| Groin / adductor | 2–6 weeks | High | Difficult to manage fully |
| Shoulder dislocation | 4–8 weeks | High (recurrent in contact sports) | |
| Fracture (non-weight bearing) | 4–10 weeks | Low | Foot/hand most common |

**Agent rule:** Tier B injuries to key players trigger the standard availability
modifier system. Cross-reference replacement quality and squad depth scoring.

### Tier C — Minor (days to weeks, limited impact)
Recovery: 1–14 days. Team impact: usually minimal.

| Type | Typical recovery | Notes |
|---|---|---|
| Hamstring (Grade 1, precautionary) | 1–2 weeks | Manager often conceals severity |
| Calf strain (Grade 1) | 1–2 weeks | Monitor for progression to Grade 2 |
| Ankle sprain (minor) | 3–7 days | Common; rarely reported accurately |
| Bruising / contusion | 2–5 days | Rarely game-changing |
| Minor knock (precautionary) | 1–3 days | Often rotation disguise |
| Illness | 2–5 days | Contagious risk in squad |

**Agent rule:** Tier C injuries may be reported as "doubt" by managers without
real match risk. Weight source reliability heavily. Official team sheet is the
only reliable confirmation for Tier C.

### Tier D — Sport-specific existential injuries
Covered in sport-specific files. Examples: horse racing breakdown (career/life ending),
MMA weight cut collapse, NFL quarterback spine, boxing cut during fight.

---

## Injury modifier pipeline

### Step 1 — Classify the injury
Use the taxonomy above. If classification is uncertain, default to the more severe tier.

### Step 2 — Assess source reliability
```
Source reliability for injury reports:
  Official club medical bulletin:       0.95 (rare — treat as confirmed)
  Manager pre-match press conference:   0.70 (often deliberately vague)
  Club official social / website:       0.85
  Verified journalist (Tier 1 outlet):  0.75
  Training ground photographer sighting: 0.65 (indirect but often accurate)
  Fan account / unverified social:      0.25
  "Expected to be fit" language:        always discount — treat as doubt
```

### Step 3 — Compute availability modifier
```
availability_modifier:

CONFIRMED fit (key player, normal form):          1.00
CONFIRMED fit (key player, HOT form):             1.10–1.15
PROBABLE (80–99% fit):                            0.95–1.05
DOUBT (50–79% fit):                               0.80–0.90
DOUBT — played through injury (under 75% fit):    0.75–0.85
OUT — replaced by quality backup:                 0.80–0.90
OUT — replaced by weak backup / youth:            0.65–0.75
OUT — replaced by emergency / out-of-position:    0.55–0.65
OUT — multiple key players (2+):                  0.55 (floor)
OUT — key player, no direct replacement exists:   0.60
SUSPENDED (not injured but absent):               0.72
```

### Step 4 — Apply return-to-play curve adjustment
For players recently returned from Tier A or B injuries, apply impairment modifier
regardless of "available" status:

```
return_to_play_impairment:

Tier A return — matches 1–3 post-return:     × 0.75 (significant impairment)
Tier A return — matches 4–8 post-return:     × 0.85 (moderate impairment)
Tier A return — matches 9–15 post-return:    × 0.93 (near-baseline)
Tier A return — match 16+ post-return:       × 1.00 (baseline restored)

Tier B return — matches 1–2 post-return:     × 0.82 (cautious return)
Tier B return — matches 3–5 post-return:     × 0.90 (building sharpness)
Tier B return — match 6+ post-return:        × 1.00 (baseline restored)

Tier C return: no impairment modifier applied (minor injury, full recovery assumed)

High recurrence risk flag (hamstring, calf returning):
  Add × 0.95 for first 4 matches regardless of tier — statistical reinjury risk
```

### Step 5 — Compute replacement quality delta (RQD)
RQD measures how much quality is lost when the injured player is replaced.

```
RQD = (injured_player_rating - replacement_player_rating) / injured_player_rating

where rating = position-normalised performance score (0–100)

RQD interpretation:
  0.00–0.10:  Minimal loss — strong depth at this position
  0.11–0.20:  Moderate loss — noticeable quality drop
  0.21–0.35:  Significant loss — clear quality downgrade
  0.36–0.50:  Major loss — team is materially weakened
  0.51+:      Severe loss — structural degradation

replacement_quality_modifier:
  RQD 0.00–0.10:  × 0.95 (barely noticeable)
  RQD 0.11–0.20:  × 0.88
  RQD 0.21–0.35:  × 0.80
  RQD 0.36–0.50:  × 0.72
  RQD 0.51+:      × 0.62
```

### Step 6 — Squad depth stress index (SDSI)
Multiple injuries compound. SDSI tracks the cumulative squad degradation.

```
SDSI = sum of RQD values for all currently injured key players

SDSI bands:
  0.00–0.15:  Squad intact — minor injuries only
  0.16–0.30:  Moderate stress — one significant absence
  0.31–0.50:  High stress — multiple or one catastrophic absence
  0.51–0.70:  Severe — team is playing with structural holes
  0.71+:      Crisis — agent should heavily reduce or exit

SDSI modifier on composite:
  0.00–0.15:  × 1.00 (no adjustment)
  0.16–0.30:  × 0.92
  0.31–0.50:  × 0.82
  0.51–0.70:  × 0.70
  0.71+:      × 0.58 (floor approaches knockout condition)
```

---

## Positional criticality by sport

Not all positions are equally critical when injured. This table guides RQD weighting.

| Sport | Most critical position | Criticality note |
|---|---|---|
| Football | Goalkeeper | Single position; no rotation; backup gap is largest |
| Football | Striker (top scorer) | Goals dry up immediately; replacements rarely equivalent |
| Football | CB partnership | Disruption compounds — two CBs need 20+ games together |
| NFL | Quarterback | Entire system runs through one player; starter out = -0.65 floor |
| NFL | Left tackle | Protects QB's blind side; loss often not covered by stats |
| NBA | Primary ball-handler | Playmaking collapses when orchestrator is out |
| MMA | Either fighter | Binary — one fighter out = event collapses or reshuffles entirely |
| Cricket | Wicket-keeper batter | Dual role; no true replacement |
| Cricket | Lead spinner (turning pitch) | Conditions amplify positional criticality |
| Horse racing | The horse | IS the athlete — any physical issue is the injury |
| Boxing | Either fighter | Binary — one fighter out = event collapses |
| Cycling | GC leader | DNF removes entire team strategy; domestiques become irrelevant |
| Tennis | Either player | Individual sport — withdrawal = bracket collapse |
| F1 | Champion / Elite DTM driver | Reserve driver is -0.30 DTM by default |
| Esports | In-game leader (IGL) | Strategy collapses without the tactical orchestrator |

---

## Injury signal sources by reliability

### Tier 1 — Most reliable (act on immediately)
- Official club medical bulletin (rare but definitive)
- Player appears on official team sheet / starting 11
- Manager names player in pre-match press conference as "available"
- Official withdrawal from international duty (confirmed)

### Tier 2 — Reliable with corroboration
- Manager says "doubt" or "we'll assess" (usually means 40–60% chance of playing)
- Credible journalist reports specific injury type and timeline
- Player absent from open training session (corroborated by multiple photographers)
- Player spotted in protective boot / on crutches post-match

### Tier 3 — Directional only
- Social media reports from fan photographers
- Unconfirmed training ground rumours
- Player's own social media (absence of posts ≠ injury)
- Betting market movement on player-specific markets (sometimes leads news)

### Tier 4 — Noise
- Fan speculation without visual evidence
- "X looks unfit" commentary
- Historical injury pattern extrapolation without current evidence

---

## Injury timing and market implications

When an injury is confirmed relative to the event determines the market opportunity:

```
TIMING:
  > 72h before event:
    Market has time to reprice fully.
    Modifier still applies but alpha from the information has been absorbed.
    
  24–72h before event:
    Prime window — market knows but hasn't fully repriced.
    Apply full modifier. Standard to elevated sizing.
    
  < 24h before event:
    Highest information value. Market likely still adjusting.
    Apply full modifier. Consider elevated sizing (1.25×) if high conviction.
    
  Announced < 2h before event (very late):
    Maximum information value but minimum time for confirmation.
    Apply modifier at 0.90× confidence (late news sometimes wrong or managed).
    
  Discovered mid-event (in-play injury):
    Different signal class. Covered in sport-specific files.
```

---

## Recurrence risk — the hidden multiplier

Certain injury types have high documented recurrence rates. When a player returns
from one of these injuries, apply a recurrence risk premium to all future assessments
for 12 months post-return:

```
HIGH RECURRENCE INJURIES (flag for 12 months post-return):
  Hamstring (any grade):         30–40% reinjury within 12 months
  Calf strain:                   25–35% within 12 months
  Groin / adductor:              25–30%
  Ankle ligament:                20–30%
  Shoulder dislocation:          25–40% (contact sport specific)
  ACL (post-return):             15–25% (either knee — contralateral risk)

Recurrence risk modifier:
  Add × 0.95 to any match where physical load is high (high-intensity fixture,
  congested schedule, artificial surface, or within 72h of previous match).
  
  Add × 0.90 if the player has had the same injury twice before.
  Add × 0.85 if three or more times (chronic — systemic issue).
```

---

## Injury and load management

Some absences are not injuries but are managed rest — especially important in:
- NBA (load management on back-to-backs)
- Cricket (rotation across T20/ODI/Test formats)
- Cycling (protecting GC leader in early Grand Tour stages)
- Tennis (withdrawal from smaller tournaments to peak for Slams)

```
LOAD MANAGEMENT vs INJURY distinction:

Signals suggesting load management (not injury):
  Player withdrew from non-critical fixture / format
  No physical reports or pain language in manager quotes
  Player trained normally in preceding days
  Club has upcoming fixture of higher importance
  Player is 30+ and has history of rotation management

Signals suggesting genuine injury:
  Physical language from manager ("took a knock", "felt something")
  Player absent from training (not just match)
  Protective equipment visible
  Medical staff involved publicly
  Timeline given (days/weeks language)
  
Modifier impact:
  Load management: × 0.95 (minor only — player is fit but rusty)
  Genuine injury: apply full modifier pipeline above
```

---

## Cascading injury effects

When a key player is injured, secondary effects follow that agents must model:

**Tactical disruption** — The team's system may depend on the injured player's specific
ability (a pressing trigger, a specific passing pattern, a set piece routine). This is
impossible to fully quantify but is most acute in:
- Teams with a single creative hub (the "key man" system)
- Set piece specialists (dead ball situations account for 25–30% of goals in football)
- Teams with low squad depth at multiple positions simultaneously

**Psychological effect** — Documented but difficult to quantify. Strongest when:
- The injured player is the captain or undisputed leader
- The injury occurred in a high-profile match with negative circumstances
- Multiple injuries compound (squad morale effect)

**Tactical recalibration** — Manager changes system to accommodate the absence.
A team that shifts from a pressing 4-3-3 to a defensive 4-5-1 due to an injury is
a different tactical entity, not just a weakened version of the original.

```
Cascading effect modifier:
  Set piece specialist out (football/rugby):    × 0.95 additional
  Captain / leader psychological signal:        × 0.97 additional
  System-change due to absence:                 × 0.93 additional
  Multiple cascading effects (2+):              × 0.90 additional (compound)
```

---

## Integrating injury intelligence into agent chains

```
STANDARD AGENT CHAIN WITH INJURY INTELLIGENCE:

1. Check injury status of key players (source: official team sheet, press conference)
2. Classify each injury using this framework (Tier A / B / C)
3. Estimate replacement quality delta (RQD) for each absence
4. Compute squad depth stress index (SDSI) across all absences
5. Apply return-to-play curve if any player is recently returned
6. Check recurrence risk history for recently returned players
7. Assess timing: how long before event was injury confirmed?
8. Check for cascading effects (set piece, captain, tactical change)
9. Produce composite injury modifier and feed into Layer 2 modifier pipeline

KNOCKOUT CONDITIONS (override all other modifiers):
  → Load sport-specific file for knockout conditions unique to that sport
  → Core knockout conditions: OUT × 3+ key players → floor 0.55
                              Genuine Tier A injury to undisputed #1 → floor 0.62
```

---

## Sport-specific files

Each file below applies this framework to the unique injury dynamics of that sport.
Load alongside this file for full injury intelligence.

| File | Sport | Key additions |
|---|---|---|
| `core/injury-intelligence/injury-intel-football.md` | Football / Soccer | Squad depth by position, set piece specialist loss, CB partnership disruption |
| `core/injury-intelligence/injury-intel-mma.md` | MMA | Fight camp signals, weight cut collapse, late replacement consequences |
| `core/injury-intelligence/injury-intel-nfl.md` | American Football | Designation system (Wed/Thu/Fri), QB tiers, O-line blind spot |
| `core/injury-intelligence/injury-intel-boxing.md` | Boxing | Weigh-in distress, cut injuries, camp signals, hand wrap issues |
| `core/injury-intelligence/injury-intel-horse-racing.md` | Horse Racing | Pre-race signals, paddock observation, trainer language patterns |
| `core/injury-intelligence/injury-intel-cycling.md` | Cycling | Crash probability, cumulative fatigue, Grand Tour degradation curve |

---

*MIT License · SportMind · sportmind.dev*
