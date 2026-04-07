# Injury Intelligence — MMA

Sport-specific injury intelligence for MMA. Applies the core framework from
`core/injury-intelligence/core-injury-intelligence.md` to MMA's unique dynamics.
Load both files for full MMA injury intelligence.

---

## What makes MMA injury intelligence categorically different

MMA has the most binary injury consequence of any sport in this library.
A footballer missing with a hamstring is absorbed by the squad. A fighter
who can't compete eliminates the fight entirely — the event reshuffles,
the other fighter faces a replacement, and the entire prediction context changes.

But MMA injury intelligence goes far beyond "can they fight?". The sport has
a unique pre-fight injury signal ecosystem that agents can read **before** any
official announcement:

- Weight cut distress often signals underlying physical problems
- Fight camp reports leak through sparring partner social media
- Fighter social media posting patterns change measurably when camp is going badly
- Movement quality at open workouts reveals injury status that managers don't disclose
- Late scratches follow predictable patterns by injury type and fighter history

---

## The MMA injury signal timeline

Unlike team sports where injury news arrives in structured press conferences,
MMA injury intelligence is distributed across a 6–8 week fight camp window:

```
WEEK -8 to -5 (fight announced):
  Signals: Has fighter taken the fight? Unusual delay in acceptance = negotiation
  OR physical concern. Check social media for training posts.
  
WEEK -6 to -4 (deep camp):
  Signals: Training partner social posts, gym footage, public workout clips.
  Red flags: Unusual absence from social media, sparring partner posts WITHOUT fighter
  (they're training but fighter is absent/resting), "camp has been tough" language.
  
WEEK -3 to -2 (media week prep):
  Signals: Fighter appearance at media obligations. Late cancellations suggest issue.
  Weight cut: Is the fighter cutting excessive weight? Social posts showing dramatic
  weight loss (more than 10% body weight = extreme cut for the class).
  
WEEK -1 (fight week):
  Open workout (Day -5): Critical window. Watch for:
    - Limited movement drills (protecting an area)
    - Absence of sparring demonstrations
    - Wrapped hands/limbs beyond normal taping
    - Shortened workout without explanation
    
  Ceremonial weigh-in (Day -2): Physical appearance signal.
    - Drawn, pallid appearance despite weight made = severe cut or illness
    - Asymmetrical physical presentation
    - Visible protective taping on limbs
    
DAY -1 (weigh-in):
  Official weigh-in: The binary event. See weigh-in section below.
  
FIGHT DAY:
  Fighter walk-out and warm-up: final visual check.
  First round: injury often reveals itself in movement — protecting, limited extension.
```

---

## Weight cut as injury proxy

Extreme weight cuts are a form of self-inflicted physical distress that creates
measurable performance impairment even when the official weigh-in is made.

```
WEIGHT CUT SEVERITY CLASSIFICATION:

Standard cut (< 5% body weight):
  Common; well-managed; minimal performance impact
  Rehydration: 12–16h adequate
  Performance modifier: × 1.00 (no adjustment)

Moderate cut (5–8% body weight):
  Demanding but manageable for experienced fighters
  Rehydration: 24h needed for full recovery
  Performance modifier: × 0.95 (slight fatigue in later rounds)
  Round-specific: R1-R2 normal; R4-R5 slight decline

Severe cut (8–12% body weight):
  High risk; fighters often show physical distress at weigh-in
  Rehydration: 36h+ needed; often incomplete before fight
  Performance modifier: × 0.82 overall; × 0.70 in rounds 4-5
  Token modifier: × 0.88 (known risk; holders discount)

Extreme cut (12%+ body weight):
  Medical risk; fight may be cancelled; fighter may be visibly impaired
  If fight proceeds: × 0.72 overall
  Knockout/finish probability: increases for opponent (fatigued fighter = easier to finish)

CUT HISTORY MULTIPLIER:
  Fighter has missed weight before:          +2% to cut failure probability per miss
  Fighter moved up a class recently:         lower cut risk (positive signal)
  Fighter moving down a class:               higher cut risk
```

### Weigh-in outcome modifier table

| Weigh-in outcome | Own modifier | Opponent modifier | Token impact |
|---|---|---|---|
| Makes weight cleanly | × 1.00 | × 1.00 | Neutral / slight positive |
| Makes weight (visibly distressed) | × 0.88 | × 1.05 | Own: -5%; Opp: +3% |
| Misses by < 1lb (fight proceeds, title voided) | × 0.82 | × 1.08 | Own: -12%; Opp: +5% |
| Misses by 1–3lbs (fight proceeds, point deduction) | × 0.72 | × 1.12 | Own: -18%; Opp: +8% |
| Misses weight, fight cancelled | Both: N/A | — | Both: -15–30% |
| Medically pulled at weigh-in | × 0 (no fight) | Opponent wins by forfeit | Both: -20% |

---

## Fight camp injury signals

### Sparring partner behaviour
The most reliable early signal before any official announcement:

```
POSITIVE CAMP SIGNALS:
  Sparring partners posting alongside fighter in gym → camp proceeding normally
  Fighter demonstrating techniques at public workouts → physically comfortable
  Fighter completing full rounds of sparring in media footage → fit
  Multiple different sparring partners rotating → full camp, not babying fighter

NEGATIVE CAMP SIGNALS:
  Sparring partners active on social but not posting with fighter → absence
  Fighter cancels or shortens public media obligations → possible injury
  "Camp has been really tough this cycle" language → often injury management
  Fighters "going easy" at open workouts → protecting something
  Fighter's long-term training partner NOT on the trip for fight week → rift or injury
  Fighter "focusing on conditioning not sparring" → cannot spar (injury)
```

### Fighter social media analysis
```
NORMAL CAMP PATTERN: 4–6 posts per week, mix of training footage and lifestyle
CONCERNING PATTERN: Sudden reduction in training posts mid-camp (weeks -5 to -3)
                    Unusual motivational posts ("pushing through") mid-camp
                    Posts from gym but no training footage
                    Frequent rest/recovery focus posts (ice baths, therapy)
VERY CONCERNING: Complete social silence for 5+ days during fight camp
                 Posts showing non-fighting activities during expected training window
```

---

## Late replacement consequences

When a fighter withdraws and a replacement steps in, the entire fight intelligence
framework must be reset. Late replacements have documented lower performance:

```
REPLACEMENT FIGHTER PERFORMANCE BY NOTICE PERIOD:

> 6 weeks notice: Full camp possible; treat as normal fight
  Modifier: × 1.00 (no adjustment)
  
4–6 weeks notice: Shortened camp; adequate for experienced fighters
  Modifier: × 0.93
  RQD from original fighter: full recalculation required
  
2–4 weeks notice: Abbreviated camp; significant disadvantage
  Modifier: × 0.82
  Weight class expertise may be wrong (taking fight above/below their usual class)
  
< 2 weeks notice: Near-emergency; documented higher finish rate for original fighter
  Modifier: × 0.68
  Very high upset probability — original fight prediction is near-worthless
  
< 1 week notice: Emergency replacement
  Modifier: × 0.55
  Agent rule: recalibrate entirely; historical records for replacement are poor guide
  
ON DAY OF FIGHT: Do not enter positions pre-fight. Wait for round 1 assessment.
```

### Replacement fighter red flags
```
Additional modifiers apply to late replacements when:
  Fighter is moving up a weight class on short notice:   × 0.90 additional
  Fighter has recent loss (seeking comeback):            × 0.95
  Fighter is primarily a striker taking fight vs grappler (style mismatch): × 0.92
  Fighter is on a win streak but opponents were low-ranked: × 0.97 (inflated record)
```

---

## In-fight injury signals

Injuries that occur during a fight create mid-event intelligence opportunities:

```
VISIBLE INJURY SIGNALS DURING A FIGHT:
  Eye swelling (orbital area): Reduces vision; affects striking range
    → Opponent should target same side; fighter vulnerable to pressure
    
  Cut above the eye: Doctor stoppage risk increases each round
    → Injury increases with further strikes; position on "fight ending by TKO-cut" value
    
  Hand injury (holding guard low, avoiding specific punches):
    → Fighter will avoid power shots; may clinch more
    → Reduces knockout probability for that fighter
    
  Leg injury (knee/ankle — from kick or twist):
    → Movement impaired; distance management fails
    → Grappler gains advantage; striker loses footwork
    
  Body shot accumulation (bending, protecting ribs):
    → Very high probability of body shot finish in later rounds
    
  Shoulder dislocation (arm hanging):
    → Very high TKO probability; corner may stop between rounds
```

---

## Career stage and injury interaction

As a fighter ages, injury context changes significantly:

```
CAREER STAGE INJURY MODIFIERS:

Under 28 (early career):
  Recovery speed: × 1.00 (baseline)
  Recurrence risk: standard rates
  
28–32 (prime career):
  Recovery speed: × 0.95 (slightly longer)
  Accumulative damage: begin flagging brain health if 3+ knockouts in career
  
32–36 (veteran):
  Recovery speed: × 0.85
  Accumulative damage: significant — any head trauma in this period has career implications
  CRI elevation: +10 for any knockout loss at this stage
  
36+ (twilight):
  Recovery speed: × 0.72
  Any serious injury at this stage: CRI evaluation required immediately
  Brain health flag: mandatory after any knockout or concussive finish
```

---

## Injury intelligence for fan token agents

```
→ fan-token-pulse: injury news timing relative to token price
  Key fighter injured (confirmed): immediate TVI spike negative
  Replacement announced: price stabilises if replacement is known quantity
  
→ token-intelligence-mma: FTM recalculation
  Injured fighter has FTM 1.20+: ATM drops to 0 for duration
  CRI elevated by injury: assess using mma-fighter-risk-profiles.md
  
→ fan-token-performance-off-pitch: rehabilitation tracking
  Serious fight camp injury → rehabilitation phase applies
  Return timeline for CRI reassessment
```

---

## Data sources

- **Tapology**: Fighter injury history, withdrawal tracking
- **MMA Fighting**: Fight camp reports, withdrawal news
- **MMAjunkie**: Official weigh-in results and medical suspensions
- **UFC athletic commission suspensions**: Post-fight mandatory rest periods (public record)
- **Fighter social media**: Training camp monitoring (Instagram, X/Twitter)
- **ESPN MMA / The Athletic MMA**: Credible camp reports

---

*MIT License · SportMind · sportmind.dev*
