# Fan Sentiment Intelligence

**The framework for modelling the emotional arc of sports fans through
sporting outcomes — how wins, losses, trophies, and failures affect fan
engagement, token holder behaviour, and commercial duration.**

SportMind's existing commercial intelligence models the *moment* of a sporting
outcome — the immediate HAS spike, the NCSI delta, the LTUI change. This skill
models what happens *after* that moment: how long does the emotion last, how
deeply does it decay, and what is the commercial value of that sustained engagement
compared to the initial spike?

This matters because fan token commercial value is not just about peak moments —
it is about sustained engagement across a whole season, a full tournament arc, or
a multi-year dynasty. A club that wins the league title has a different emotional
profile three weeks after the final whistle than three months after. Understanding
that profile is what separates a short-term signal from a long-term commercial plan.

---

## The Emotional Arc Model

```
FAN EMOTIONAL ARC — six phases after a significant outcome:

PHASE 1 — PEAK (0-24 hours)
  Maximum emotional intensity
  Token price spike: +8-25% depending on outcome significance
  Social engagement: 300-500% above baseline
  New holder acquisition: highest rate in any post-event window
  Governance participation: if vote is active, highest turnout
  Duration: 12-24 hours
  
PHASE 2 — CELEBRATION / PROCESSING (1-7 days)
  Sustained elevated engagement
  Token price: +3-10% above pre-event baseline (decay from peak)
  Social engagement: 150-250% above baseline
  Content consumption: highlight reels, post-match analysis
  New holder acquisition: 40-60% of peak-day rate
  Duration: 3-7 days (shorter for regular wins; longer for trophies)

PHASE 3 — NARRATIVE SUSTAIN (1-4 weeks)
  Engagement driven by ongoing narrative (title race, tournament progression)
  Token price: +2-5% above pre-event baseline
  Social engagement: 110-140% above baseline
  Key driver: is there a NEXT significant event to look forward to?
  Without upcoming event: decay accelerates significantly
  Duration: 1-4 weeks depending on competition calendar

PHASE 4 — NORMALISATION (1-3 months)
  Return toward baseline
  Token price: at or near pre-event baseline
  Social engagement: 100-110% above pre-event baseline
  Key driver: off-season vs in-season determines decay rate
  Off-season: faster decay (no events to sustain narrative)
  In-season: slower decay (regular matches maintain engagement)
  Duration: 4-12 weeks

PHASE 5 — MEMORY NARRATIVE (3-12 months)
  Outcome becomes part of club identity / fan identity
  Token engagement: baseline or slightly above
  Activation: anniversary content, next season preview
  Commercial value: brand equity, not short-term signal
  Duration: indefinite (trophies enter permanent narrative)

PHASE 6 — LEGACY (12+ months)
  Outcome is now historical context
  ATM and LTUI incorporate outcome as baseline uplift
  New token holders attracted by club identity (dynasty clubs)
  Trophy-winning clubs command permanent ATM premium vs non-trophy clubs
```

---

## Outcome-specific arc profiles

```
WIN — STANDARD LEAGUE MATCH (non-decisive):
  Peak: +3-8% token, +200% social (24h)
  Phase 2: +1-3%, +120% social (2 days)
  Phase 3: None — regular match does not sustain narrative
  Normalisation: within 48-72 hours
  Commercial duration: SHORT (2-3 days)

WIN — DECISIVE MATCH (title clinched, relegation avoided):
  Peak: +12-22% token, +400-600% social (24h)
  Phase 2: +5-10%, +200% social (5-7 days)
  Phase 3: +2-4%, +130% social (2-3 weeks — season end processing)
  Normalisation: 6-8 weeks
  Commercial duration: EXTENDED (6-8 weeks)

WIN — TROPHY (Cup Final, Champions League, World Cup):
  Peak: +15-30% token, +500-800% social (24h)
  Phase 2: +8-15%, +250% social (7-14 days)
  Phase 3: +4-8%, +150% social (3-6 weeks)
  Normalisation: 8-16 weeks
  Legacy uplift: LTUI +8-12 (permanent; trophy enters club identity)
  Commercial duration: LONG (2-4 months + permanent legacy)
  
  NOTE: First trophy in long drought has amplified arc:
  Leicester City 2016, Wrexham promotion, USA NWSL expansion:
  Phase 3 extends 2-3× longer; Legacy uplift LTUI +15-20

LOSS — STANDARD:
  Immediate: -2-5% token, -negative sentiment spike (24h)
  Recovery: baseline within 48-72 hours for mid-table clubs
  Exception: consecutive losses → fatigue signal → Phase 3 decline extends
  Commercial duration: SHORT NEGATIVE (1-3 days)

LOSS — ELIMINATION (Cup exit, relegation confirmed):
  Immediate: -8-15% token, strong negative sentiment (24h)
  Phase 2: -4-8% below previous baseline (5-10 days)
  Phase 3: fan engagement drop-off; Phase 3 lifecycle signal activated
  Normalisation: 3-6 weeks
  Lifecycle impact: potential Phase 3 → Phase 4 transition
  
  RELEGATION SPECIFIC:
    Phase 2 negative: -10-20% token, -50-60% social engagement sustained
    Lifecycle: Championship/lower league = Phase 3 certain, Phase 4 likely
    Recovery condition: promotion back to top flight
    Recovery arc: equivalent to trophy win (return narrative)

DRAW — DECISIVE CONTEXT:
  Grand Slam attempt denied: negative (fan disappointment)
  Draw securing title: positive (mission accomplished)
  Derby draw: neutral-positive for both clubs (engagement maintained)
  Commercial duration: SHORT (1-2 days) — draws rarely sustain narrative
```

---

**Academic grounding: Ante, Schellinger & Demir (2024), *Journal of Business Economics* — documents outcome-specific engagement duration following match results. Demir, Ersan & Popesko (2022), *Finance Research Letters* — UCL match outcomes generate abnormal returns with different duration profiles by outcome type. These empirical findings inform the CDI decay constants below.**

## Commercial duration index (CDI)

```
CDI measures how many days of commercially valuable fan engagement
an outcome generates above baseline.

CDI = Base_Duration × Outcome_Tier × Competition_Weight × Club_Drought_Factor

BASE_DURATION (outcome type):
  Standard win:      3 days
  Decisive win:      15 days
  Trophy win:        45 days
  Standard loss:     2 days (negative)
  Elimination loss:  10 days (negative sustained)

OUTCOME_TIER (significance):
  World Cup / CL Final: × 2.50
  Domestic cup final:   × 1.80
  League title:         × 1.60
  Top 4 / qualification: × 1.20
  Regular match:         × 1.00

COMPETITION_WEIGHT:
  Same as NCSI weight:
  UCL Final: 1.00, QF: 0.75, Group: 0.40
  Premier League title: 0.95
  Domestic cup final: 0.75

DROUGHT_FACTOR:
  No major trophy in > 10 years: × 1.50
  No major trophy in > 25 years: × 2.00
  No major trophy in > 50 years: × 3.00 (Leicester 2016, Wrexham model)

EXAMPLES:
  Standard PL win (Man City): 3 × 1.00 × 0.35 × 1.00 = 1 day CDI
  PL title (Man City):        15 × 1.60 × 0.95 × 1.00 = 22.8 day CDI
  CL Final win (PSG first):   45 × 2.50 × 1.00 × 2.00 = 225 day CDI (!)
  Long-awaited trophy (Everton FA Cup): 45 × 1.80 × 0.75 × 1.50 = 91 day CDI

CDI IN PRACTICE:
  CDI < 5:   Short-term signal only; standard monitoring continues
  CDI 5-20:  Elevated engagement window; schedule marketing activations
  CDI > 20:  Extended commercial opportunity; LTUI uplift confirmed
  CDI > 90:  Structural commercial event; recalibrate LTUI baseline
```

---

## Decay curve modelling

```
POST-PEAK ENGAGEMENT DECAY:

The decay follows a modified exponential curve with two inflection points:

Engagement(t) = Baseline + (Peak_Delta × e^(-λt)) + Calendar_Boost(t)

Where:
  t           = days since outcome
  λ           = decay constant (outcome-specific; see below)
  Peak_Delta  = maximum engagement above baseline (day 0)
  Calendar_Boost = step function activated by subsequent events (next match,
                   trophy parade, season opener)

DECAY CONSTANTS (λ) BY OUTCOME TYPE:
  Standard win:     0.69 (half-life: ~1 day — rapid decay)
  Decisive win:     0.14 (half-life: ~5 days)
  Trophy win:       0.05 (half-life: ~14 days)
  World Cup trophy: 0.03 (half-life: ~23 days)
  Elimination loss: 0.10 (half-life: ~7 days — negative sustained)

CALENDAR BOOST:
  Next match (3-7 days): engagement reset to 40% of post-outcome peak
  Trophy parade (1-3 days post-win): engagement spike to 60% of day-0 peak
  Season opener (pre-season if outcome was end-of-season): 30% boost

PRACTICAL EXAMPLE — PSG CL Final Win:
  Day 0:   +28% token, +700% social (peak)
  Day 1:   +21% token, +450% social (Phase 2 — celebration)
  Day 3:   +14% token, +220% social (still elevated)
  Day 7:   +9% token, +150% social (Phase 3 sustain — trophy parade)
  Day 14:  +5% token, +120% social (Narrative sustain — summer window)
  Day 30:  +2% token, +108% social (Normalisation)
  Day 90:  +0.5% token, +101% social (Legacy begins)
  Day 365: ATM +0.05 permanent (trophy enters identity; LTUI +8)

NEGATIVE DECAY (Elimination/Relegation):
  Negative emotion typically decays faster than positive (psychological asymmetry)
  Exception: RELEGATION — negative engagement sustained 4-8 weeks
  because the material consequences (matches against lower clubs) continue
  for the rest of the season or the following year
```

---

**Academic grounding: Manoli, Dixon & Antonopoulos (2024), *Leisure Studies* — 60-participant qualitative study (10 focus groups) documenting the identity-investment duality in fan token holders. The four holder archetypes in `fan-token/fan-holder-profile-intelligence.md` are derived from this empirical work. Fan type segmentation below aligns with their identity-first vs investment-first classification.**

## Fan type segmentation

```
NOT ALL FANS RESPOND THE SAME WAY:

CORE HOLDERS (high token balance, long-term):
  Most resistant to negative decay
  Most engaged with governance events
  Trophy wins: deepest and longest engagement arc
  Losses: relatively resilient (identity-based, not outcome-based)
  CDI multiplier: × 1.30 (sustained engagement longer than average)

SEASONAL FANS (buy tokens at season start, hold through season):
  Respond to cumulative performance, not individual results
  Trophy wins: strongest new holder acquisition signal
  Poor season: Phase 3 risk; holder attrition accelerates
  CDI multiplier: × 0.85 (shorter engagement windows)

EVENT-DRIVEN FANS (buy for specific events, may sell after):
  Highest buying activity at peak (trophy wins, cup finals)
  Fastest decay back to baseline or below
  CDI multiplier: × 0.60 (engagement is the event itself)

NEW MARKET FANS (from DTS effect, Drive to Survive, etc.):
  Attracted by narrative, not deep club identity
  Long initial engagement if narrative sustains (documentary → live match)
  Trophy wins: moderate engagement (less identity investment)
  CDI multiplier: × 0.75 initially; rises to × 1.00 with 1+ season of engagement

AGENT APPLICATION:
  Without holder segmentation data: use blended CDI baseline
  With segmentation data: weight by holder type composition
  Most fan token platforms have wallet-level data to identify core vs event holders
```

---

## LTUI integration

```
HOW SENTIMENT ARCS AFFECT LTUI:

POSITIVE ARCS (wins, trophies):
  Standard win:              LTUI + 0.5 to + 1 (quickly normalises)
  Decisive win (title, etc): LTUI + 3 to + 5 (sustained 4-8 weeks)
  Trophy win:                LTUI + 8 to + 12 (permanent legacy component)
  First trophy in long drought: LTUI + 15 to + 20 (structural identity shift)

NEGATIVE ARCS (losses, eliminations):
  Standard loss:             LTUI - 0.5 to - 1 (quickly normalises)
  Cup exit:                  LTUI - 2 to - 4 (short sustained negative)
  Relegation:                LTUI - 15 to - 25 (structural negative)
  Administration:            LTUI → Phase 6 (Dormant) — see lifecycle model

COMPOUNDING EFFECTS:
  Consecutive trophies (dynasty):
    Each additional trophy in 3-year period: +3 to LTUI above standard trophy value
    Dynasty clubs (3+ trophies in 5 years): LTUI floor rises permanently
    
  Consecutive failures (drought + near-misses):
    Reaching final but losing: CDI slightly negative (expected outcome not achieved)
    3+ consecutive near-misses: narrative fatigue signal; LTUI risk

GOVERNANCE INTERACTION:
  Trophy wins increase governance participation (fans more engaged)
  Losses increase governance criticism (fans want change)
  Both are useful — positive engagement and critical feedback both
  signal an engaged holder base (better than silence)
```

---

## Agent loading instructions

```
LOAD THIS DOCUMENT WHEN:
  Projecting LTUI after a significant match outcome
  Assessing commercial activation window post-event
  Modelling holder retention after a poor season
  Evaluating long-term token value of a trophy-hunting club
  Building post-event marketing or governance event timing

LOAD ALONGSIDE:
  fan-token/fan-token-lifecycle/ — phase model (sentiment drives phase transitions)
  fan-token/sports-governance-intelligence/ — governance participation arc
  core/autonomous-agent-framework.md — for agents that monitor continuous sentiment
  market/broadcaster-media-intelligence.md — DTS effect (narrative sustain)

KEY OUTPUTS FROM THIS SKILL:
  CDI (Commercial Duration Index): how many days of above-baseline engagement
  Decay curve parameters: λ value for modelling engagement trajectory
  Phase classification: which arc phase is the club currently in?
  LTUI adjustment: permanent legacy impact on token lifetime utility
```

---

*MIT License · SportMind · sportmind.dev*
