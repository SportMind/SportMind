# Injury Intelligence — Boxing

Sport-specific injury intelligence for boxing. Applies the core framework from
`core/injury-intelligence/core-injury-intelligence.md` to boxing's unique dynamics.
Load both files for full boxing injury intelligence.

---

## What makes boxing injury intelligence different

Boxing shares MMA's binary event structure — one fighter can't compete, and the
event collapses or reshuffles. But boxing has distinct injury dynamics that MMA
doesn't share:

**Weight class culture** — Many boxing weight classes have traditionally required
more extreme cuts than MMA, with less medical oversight in some jurisdictions.
Weigh-in rehydration windows vary significantly by sanctioning body and jurisdiction.

**Cut injuries are a fight-ending mechanism** — In boxing, a cut from a punch
(as opposed to a clash of heads) can end a fight at any moment via TKO. A fighter
with a known cut scar or poor skin (a "bleeder") carries permanent structural risk.
This is an ongoing, event-specific risk that doesn't diminish between fights.

**Camp secrecy culture** — Boxing camps are among the most secretive in sport.
Promotional politics mean injury information is more suppressed than in MMA.
Fighters routinely compete with undisclosed injuries because: promoters have too
much financial exposure to cancel, fighters don't want to show vulnerability, and
the culture treats injury disclosure as weakness.

**Hand injuries are endemic and chronic** — Boxing is a sport where the primary
attacking tool (the fist) is also the primary injury point. Chronic hand injuries
affect almost every active professional fighter at the elite level. A fighter with
a known hand problem will punch differently without revealing it explicitly.

---

## Fight camp injury signals — boxing specific

### Promoter and manager language
Boxing promotion is highly financially motivated. Injury information is more likely
to be managed than disclosed. Learn to read between the lines:

```
PROMOTER LANGUAGE DECODER:

"He's had a fantastic camp"          → Standard; no specific information
"Best camp of his career"            → Often used BECAUSE there was an issue to overcome
"He's 100%" (pre-fight)             → Standard denial; weight no differently
"Minor injury but he's fine"         → Something happened; assess severity
"He had to modify his preparation"   → Real injury; severity unknown
"Medical reasons" (withdrawal)       → Could be anything; severity unknown
"Personal reasons" (withdrawal)      → Dispute / financial issue OR injury (disguised)
"We had to be careful in camp"       → Injury management confirmed; watch closely
"He's been champing at the bit"      → Often injury-recovery framing ("eager to return")
"He hasn't sparred in 3 weeks"       → Hand, rib, or eye injury; ask which
```

### Sparring partner signals
More valuable in boxing than MMA because boxing camps have looser social media behaviour:

```
POSITIVE SIGNALS:
  Sparring partners posting footage of hard rounds with fighter
  Fighter completing full rounds of sparring on public videos
  Trainer posting about "sharp" sessions late in camp
  
NEGATIVE SIGNALS:
  Fighter's gym doing heavy sparring but fighter absent from footage
  "Working on conditioning" posts when sparring should be happening (weeks 8–4)
  Sparring partners who normally post with fighter have gone quiet
  "Hand issues" or "had to take it easy" language from camp visitors
  
VERY CONCERNING:
  No sparring footage in final 4 weeks of camp
  Fighter posting only bag work and pad work (no contact with opponents)
  "Medically cleared" language that shouldn't be needed for a healthy fighter
```

---

## Hand injuries — the endemic boxing problem

Hand injuries are the most common and most suppressed injury in professional boxing.
The sport requires throwing thousands of punches in training and competition across
a career, making chronic hand problems almost universal at the elite level.

### Identifying hand injury signals

```
VISUAL SIGNALS:
  Unusually heavy taping on specific hand at open workouts
  Holding guard lower than usual (avoiding loading injured hand)
  Favoring jab (non-power hand) more than usual in combination work
  Reduced use of right hand (orthodox) or left hand (southpaw) in pad work
  Fighting with hand wrap that covers more of the wrist than usual
  
PERFORMANCE SIGNALS (during fight):
  Throwing right hand less frequently than established pattern
  Decreased velocity on power shots (protecting hand from impact jarring)
  Clinching immediately after connecting with power hand (pain response)
  Switching from tight fists to open-palm blocks (reduces impact on injured hand)
  Trainer adjusting corner advice away from power shots mid-fight
  
HISTORICAL SIGNALS (research before any fight):
  Check historical knockout wins — do they favour one hand?
  Check for fights where knockout power seemed absent vs historical norm
  Training footage showing glove changes (specific gloves for injured hands)
  Any medical suspension post-fight for hand fracture (public record in some commissions)
```

### Hand injury modifier table

| Injury | Severity | Power output | Combination speed | Modifier |
|---|---|---|---|---|
| Fracture (metacarpal) — confirmed | Tier B | -60% | -40% | × 0.72 |
| Fracture — fight proceeding | Tier B/C | -50% | -35% | × 0.75 |
| Hairline fracture — managed | Tier C | -25% | -15% | × 0.88 |
| Chronic arthritis — managing | Ongoing | -15% | -10% | × 0.92 |
| Sprain — confirmed | Tier C | -20% | -10% | × 0.90 |

---

## Cut injuries — the fight-ending mechanism

A cut in boxing can end a fight at any point. It is a continuous risk throughout
a fight, unlike most sports where injury risk is event-specific.

### Pre-fight cut risk assessment

```
PERMANENT SCAR TISSUE RISK:
  Identify: Has this fighter had significant cuts in previous fights?
  Old cut sites: around eyebrows, bridge of nose, cheekbones
  Scar tissue tears more easily than healthy skin
  
  "Known bleeder" profile:
    2+ cuts in career requiring medical attention → High cut risk (× 0.93 fight completion)
    3+ cuts → Very high (× 0.85 fight completion probability)
    Recent cut (last 2 fights) → Healing skin: very high risk if in same area
    
OPPONENT HEAD-BUTT TENDENCY:
  Review opponent's fight history for clashes of heads
  Some fighters consistently cause cuts through aggressive inside work
  
  Agent rule: High-cut-risk fighter vs head-butt-prone opponent:
    Fight completion probability: × 0.80
    Consider: doctor stoppage due to cut is a TKO win for opponent
```

### In-fight cut modifier

```
FIGHT PROGRESSING WITH CUT VISIBLE:
  Small cut, not affecting vision:  No immediate modifier; monitor
  Cut above eye, blood entering vision: Escalating risk; doctor check next round
  Significant cut (2+ inches, deep): Doctor stoppage risk this round or next
  Fighter wiping eye frequently:    Vision affected; accuracy and defense declining
  
  Agent rule: visible cut on token-holder's fighter = hold position only if fighter
  is winning decisively. If even or losing, cut risk amplifies negative outcome probability.
```

---

## Weight cut — boxing specific considerations

Boxing weight cuts differ from MMA in several important ways:

```
REHYDRATION WINDOW DIFFERENCES BY SANCTIONING BODY:
  WBC, IBF, WBO, WBA major fights: 
    Typically 24–30h between weigh-in and fight
    Fighters can rehydrate 3–5lbs (modest recovery)
    
  State athletic commission variations:
    Some jurisdictions allow only 4h rehydration window
    Shorter window = more impairment on fight night
    
  Hydration testing (newer protocols):
    Some commissions now test for hydration at fight time
    "IV drip" rehydration being phased out in some jurisdictions
    
WEIGHT MANIPULATION DETECTION:
  Fighters appearing much larger than opponent on fight night = extreme cut
  "Ballooned up" look at fight time despite making weight cleanly:
    Strong signal of extreme rehydration that stresses the cardiovascular system
    Associated with fatigue in middle-to-late rounds
    Modifier: × 0.88 for rounds 7–12 performance
```

---

## Chin durability as injury history factor

Unlike other sports, "chin" durability is a progressive physical characteristic
that deteriorates with accumulated knockdowns and knockouts. This is a unique
injury-adjacent factor in boxing.

```
CHIN DURABILITY ASSESSMENT:

Career knockdown history:
  0 knockdowns (20+ professional fights):  Strong chin → × 1.05 (resilience premium)
  1–2 knockdowns (from power punchers):    Average → × 1.00
  3–5 knockdowns (various opponents):      Declining → × 0.92
  1+ knockout losses (in last 3 fights):   Significantly degraded → × 0.82
  2 knockout losses (last 3 fights):       Severely degraded → × 0.72 (CRI elevated)
  
AGE + CHIN INTERACTION:
  Under 28, 1 knockout loss: Can rebuild with careful matching
  28–33, 1+ knockout losses: Permanent vulnerability established
  33+, any knockout loss: Career reassessment required; × 0.70 for all future fights
  
  Agent rule: A fighter with a degraded chin matched against a puncher in their
  power range is the highest single-fight variance situation in boxing. The expected
  value of any position is lower because the fight is one punch from being over at
  any moment.
```

---

## Postponement and withdrawal patterns

Boxing has a higher fight withdrawal rate than MMA due to camp culture and
the individual (non-team) financial structure. Understanding why fights fall apart
helps assess the remaining fighter's state.

```
WHY BOXING FIGHTS FALL APART (and what it signals):

Withdrawal due to injury:
  If disclosed: genuine physical problem
  If "undisclosed medical": often more serious than stated; may reoccur
  
Withdrawal due to contract dispute:
  Financial, not physical — no injury implications for either fighter
  
Fight postponement (not cancelled):
  Higher probability of injury involvement than cancellation
  Postponement language: "needs more time to prepare" often = injury healing
  
Opponent withdrawal → replacement opponent:
  Run full late-replacement framework (core + MMA file for reference)
  Boxing replacement fighters have same late-notice disadvantages as MMA
```

---

## Pre-fight medical examinations

Most state commissions require pre-fight medical exams. These create a paper trail
of injury disclosures that agents can sometimes access:

```
COMMISSION MEDICAL RECORDS (public in some US states):
  Medical holds (suspension from last fight): public record
  Pre-fight ophthalmology exam: sometimes disclosed
  Brain scan requirements: Tier A head injury history
  
  Agent rule: Any fighter with a medical hold from their last fight is flagged.
  Commission cleared them, but reason for hold is informative.
  Eye injury holds: particularly concerning (vision is irreversible)
  Brain scan required: elevated CRI regardless of cleared status
```

---

## Data sources

- **ESPN Boxing / The Athletic Boxing**: Fight camp reports, withdrawal news
- **BoxRec**: Complete professional record including knockdowns, medical suspensions
- **State Athletic Commission records**: Medical holds, pre-fight examination results
- **Seconds Out / Boxing Scene**: Camp reports and insider news
- **Fighter social media**: Training footage analysis
- **The Ring Magazine**: In-depth fighter profiles with injury history context

---

*MIT License · SportMind · sportmind.dev*
