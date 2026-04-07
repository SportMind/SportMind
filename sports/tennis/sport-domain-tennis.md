# Tennis — SportMind Domain Skill

Sport-specific intelligence for tennis. Covers the ATP and WTA tours,
all four Grand Slams, and the ATP/WTA Finals.

---

## Overview

Tennis is an individual sport with one of the clearest and most reliable
prediction frameworks in this library. The surface split — how a player performs
on clay versus grass versus hard court — is the single most predictive variable
in tennis, and it is extensively documented across thousands of matches.

Unlike team sports, there is no squad depth, no tactics board, and no formation
adjustments. The match comes down to two individuals, their current form, their
H2H record, and how they both perform on the specific surface that day.

---

## Domain Model

### Tournament Calendar and Tier Classification

**Tier 1 — Grand Slams (highest token and prediction impact)**

| Tournament | Surface | Date | Duration |
|---|---|---|---|
| Australian Open | Hard | Jan | 2 weeks |
| Roland Garros (French Open) | Clay | May–Jun | 2 weeks |
| Wimbledon | Grass | Jun–Jul | 2 weeks |
| US Open | Hard | Aug–Sep | 2 weeks |

Grand Slams are the only events in tennis where best-of-5 sets for men creates
the longest, most physically demanding format. Surface specialists may dominate
at their preferred Slam but struggle at others.

**Tier 2 — Masters 1000 (ATP) / WTA 1000**
Major events immediately below Grand Slams. Indian Wells, Miami, Madrid, Rome,
Canada, Cincinnati, Shanghai, Paris. 10–12 events per year across surfaces.

**Tier 3 — ATP 500 / WTA 500 and below**
Regular tour events; important for ranking progression but lower token impact.

**Special events:**
- ATP Finals / WTA Finals (Nov): Year-end championship of top 8. Tier 1.5
- Davis Cup / Billie Jean King Cup: National team format. Tier 2 nationally.
- Olympics (tennis): Every 4 years. Tier 1.5 — significant for national tokens.

---

## Surface Intelligence — the most predictive variable

Surface preferences are persistent, well-documented, and the single most important
input for any tennis prediction or token assessment.

### Clay (Roland Garros, Madrid, Rome, Monte Carlo)

```
CHARACTERISTICS:
  Ball slows significantly — longer rallies
  High bounce — rewards baseline players who can hit heavy topspin
  Physical: most demanding surface; requires endurance over explosive speed
  Slide technique: clay-specific footwork skill — not all players have it

CLAY SPECIALISTS THRIVE:
  Heavy topspin forehand players
  Strong legs and endurance (outlast opponents in long rallies)
  Tactical, patient baseline style
  South American and Spanish players historically dominant (grow up on clay)

CLAY-UNFAVOURABLE PLAYER TYPES:
  Serve-and-volley players (ball slows; volleys are attacked)
  Players who rely on flat pace (doesn't hurt as much on clay)
  Grass-court specialists (movement style doesn't transfer)

AGENT RULE: Never apply a player's hard-court or grass form to clay without
checking their specific clay record. A top-3 hard-court player can be
first-round clay fodder if they lack the clay-specific skillset.
```

### Grass (Wimbledon, Queen's, Halle)

```
CHARACTERISTICS:
  Ball stays low — short, compact swing required
  Serve is king — aces and service winners dominate
  Short rallies — explosive over endurance
  Historically disadvantages heavy topspin / clay specialists
  
GRASS SPECIALISTS THRIVE:
  Big servers (flat, wide serve is extremely difficult to return)
  Serve-and-volley players (approach on low ball)
  Players with flat, aggressive ball-striking
  Players with quick lateral movement (slice and low balls)

GRASS-UNFAVOURABLE PLAYER TYPES:
  Heavy topspin clay specialists (high-bouncing balls find the net on grass)
  Players who need time on the ball (grass gives less time)
  
WIMBLEDON-SPECIFIC:
  By Week 2, grass plays closer to hard court as surface wears
  Serve-volley advantage diminishes as grass becomes slicker
  This transition matters for Week 2 matchups vs Week 1
```

### Hard Court (Australian Open, US Open, most Masters)

```
CHARACTERISTICS:
  Most common surface — most players have their best records here
  Medium pace (varies by court: Aus Open slower, US Open faster)
  Predictable bounce — rewards consistent ball-striking
  Favours all-round players; fewer extreme specialists

KEY VARIABLES:
  Indoor hard vs outdoor hard: indoor is faster, lower bounce
  US Open hardcourt is faster than Australian Open hardcourt
  Night sessions (US Open): cool air = faster ball; serves more effective

AGENT RULE: Hard court is the baseline surface — use a player's overall
ranking and recent form as the primary input; surface adjustment is less
dramatic than clay or grass transitions.
```

---

## Head-to-Head (H2H) Records

H2H records in tennis carry more predictive weight than in most sports because:
- Individual matchup styles persist (one player's game may always trouble another's)
- Mental edge from H2H dominance is documented and persistent
- Specific surface H2H is more predictive than overall H2H

```
H2H ASSESSMENT FRAMEWORK:
  Surface-specific H2H > overall H2H
  Recent H2H (last 3 years) > career H2H
  Same tournament H2H (e.g. Wimbledon specifically) > general surface H2H

  H2H dominance modifier:
    One player leads H2H 70%+ on this surface:     × 1.12 for dominant player
    H2H split 60/40 on this surface:               × 1.05 for leader
    Competitive split (50/50 or close):            × 1.00 — H2H not informative
    H2H reversed recently (last 3 matches differ): use recent trend, not career record

  KEY H2H PATTERN: Style matchups persist.
    A heavy topspin player who hits high to an opponent's backhand creates
    a permanent structural advantage regardless of ranking. Always check if
    there is a known tactical vulnerability in H2H.
```

---

## Serve and Return Intelligence

Tennis is fundamentally determined by service games. Understanding serve quality
and return quality separately from overall performance is essential.

```
SERVE METRICS:
  First serve %: Elite 60–70% | Good 55–65%
  First serve win %: Elite 75%+ | Good 68%+
  Second serve win %: Elite 55%+ | Good 48%+
  Ace rate: varies by surface (higher on grass)
  Double fault rate: below 3% per match is controlled; above 5% is a liability

RETURN METRICS:
  Return points won (1st serve): Elite 35%+ | Good 28%+
  Return points won (2nd serve): Elite 58%+ | Good 52%+
  Break point conversion: Elite 45%+ | Good 38%+

KEY INSIGHT: Matches are decided by break points.
  A player who rarely breaks serve (low return stats) must hold serve every game.
  One break is often enough to win a set. Pressure on serve = match tension.

INJURY IMPACT ON SERVE:
  Shoulder, elbow, or wrist injury: serve velocity and placement directly affected
  (See core injury framework + injury signals section below)
  Lower body injury: movement affects serve action and follow-through
```

---

## Physical Stamina — the 5-set factor

For men's Grand Slams (best-of-5), physical condition has a compounding effect
that doesn't exist in best-of-3 formats:

```
5-SET CONSIDERATIONS:
  Players who struggle with 5-sets: those managing chronic physical issues,
  older players (30+), players with compressed recent schedule
  
  5-SET ADVANTAGE PATTERNS:
    Players known for fitness and endurance (documented via stat databases)
    Players who have won deep in a tournament recently (match fitness)
    Players with better rest between rounds
    
  5-SET DANGER PATTERNS:
    Players who have played 4-5 hour matches recently (fatigue accumulation)
    Players who went 5 sets in previous round (more fatigue than 3-set winner)
    Players managing lower body injury on hard court (knee, hip, ankle)

  AGENT RULE: In deep tournament rounds, check recent match duration.
  A player who played a 5-hour match yesterday is at a structural disadvantage
  to an opponent who won in straight sets.
```

---

## Tournament Progression Signals

```
DRAW ANALYSIS:
  Seeded players are separated to ensure they only meet in later rounds
  A strong player in a weaker section of the draw = lower path to semis
  "Soft draw" signal: top seed avoids all other top-10 players until the Final
  
  Agent rule: Assess draw difficulty as well as player form.
  A 5th seed with a clear draw path can outperform a 2nd seed who must beat
  the 3rd and 4th seeds en route to the Final.

TOURNAMENT FATIGUE (for deep-running players):
  Round 4 onward: players have played 3+ matches in compressed schedule
  Best-of-5 sets: fatigue compounds sharply
  Watch for: increasing double fault rates, slower first set play (saving legs)
  
  Fatigue adjustment: × 0.93 for players on 5+ hours of court time in the week
                      × 0.88 for players on 7+ hours in the week (heavy accumulation)
```

---

## Result Impact Matrix

| Result / Event | Token impact |
|---|---|
| Grand Slam win | +15–30% |
| Grand Slam Final loss (runner-up) | -3–8% (sentiment — near miss) |
| Grand Slam upset win (vs top-3) | +10–20% |
| Grand Slam withdrawal before event | -10–25% |
| Injury retirement mid-match | -12–28% |
| World No. 1 ranking achieved | +8–18% |
| Career Grand Slam completed | +20–40% (one-time narrative) |
| Masters 1000 win | +5–12% |

---

## Sport-Specific Risk Variables

**Retirement (mid-match withdrawal)** — The most common "injury" event in tennis.
Players who feel unable to continue can retire at any point. Risk is highest when:
a player entered with a known injury, or when a player has been managing a chronic
condition. Pre-match retirement (scratch) vs mid-match retirement carry different
sentiment signals.

**Weather delays** — Outdoor courts are interrupted by rain (Wimbledon, Roland
Garros, US Open — covered courts help but limited). Long delays can cool down
a player who has built momentum; can also help an injured player rest between sets.

**Scheduling** — The night session (US Open) creates different conditions (faster,
cooler). Early morning first match vs late afternoon match can affect serve rhythm.

---

## Signal Weight Adjustments

| Component | Weight | Rationale |
|---|---|---|
| Sports catalyst | 30% | Match result and tournament progress key |
| Social sentiment | 25% | Individual players drive strong social signals |
| Market / whale | 20% | Well-traded sport with sophisticated market |
| Price trend | 20% | Between-tournament form trends are reliable |
| Macro | 5% | Minimal |

---

## Agent Reasoning Prompts

```
1. SURFACE FIRST. Always check the surface-specific record before applying
   any general form data. A player ranked 3rd in the world may be a first-round
   exit at Roland Garros if they lack clay-specific technique.

2. SURFACE-SPECIFIC H2H is more predictive than career H2H.
   Check if there is a documented tactical mismatch between the two players.

3. GRAND SLAMS are 5-set formats (men). Check recent match durations —
   a player who spent 5 hours on court yesterday is a different proposition
   to one who won in 75 minutes.

4. THE SERVE is the most important single skill. Check first serve percentage
   and second serve win rate before assessing match probability.

5. RETIREMENT RISK: If a player entered the tournament with a known physical
   concern, apply a non-completion modifier to any prediction.

6. DRAW ANALYSIS: The path to the Final matters. A weaker draw section can
   take a player further than their ranking suggests.
```

---

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` for the full injury
framework. Tennis-specific notes:
- Shoulder/elbow/wrist injuries directly impair serve — the most critical skill
- Lower body injuries (knee, hip, ankle) affect movement and serve follow-through
- Tennis elbow (lateral epicondylitis) is chronic and persistent in professional players
- Mid-match retirement is the most common injury manifestation in tennis
- Pre-tournament withdrawal is a strong signal of severity — managed injuries play through

## Compatibility

**Athlete intelligence:** `athlete/tennis/athlete-intel-tennis.md`
**Injury intelligence:** `core/injury-intelligence/core-injury-intelligence.md`

---

*MIT License · SportMind · sportmind.dev*

---

## Event Playbooks

### Playbook 1: Grand Slam final (surface specialist confirmed)
```
trigger:  Grand Slam final where one player has dominant surface record (>70% win rate)
entry:    24h before match on lineup confirmation (both players confirmed fit)
exit:     Match completion — do not trade in play unless retirement risk materialises
filter:   Both players confirmed fit; no fatigue flags from 5-set previous round;
          surface match confirmed via Tennis Abstract surface splits
sizing:   1.1× standard — Grand Slam final surface specialist has reliable edge
note:     Clay specialist at Roland Garros is the strongest single-surface signal in tennis.
          H2H record is secondary to surface record when they conflict.
          Djokovic/Nadal/Alcaraz era: load H2H surface-specific, not overall H2H.
```

### Playbook 2: Upset alert — top seed vs. low-ranked opponent after 5-set match
```
trigger:  Top-10 seed plays within 48h of a 5-set match vs. opponent ranked 30+
entry:    Morning of match once confirmed schedules available
exit:     End of second set — reassess if top seed drops first set
filter:   Check if top seed is known poor recoverer; check opponent's surface form last 6;
          load athlete fatigue modifier
sizing:   0.6× standard — fatigue in best-of-5 format is the highest variance in the sport
note:     Masters 1000 and Slam schedules compress for lower seeds; top seeds get byes.
          The fatigue differential is most pronounced in 5-set formats (Slams, Davis Cup).
```

### Playbook 3: Surface switch — clay to grass (May–June transition)
```
trigger:  Clay season ends; grass season begins (Roland Garros → Queen's → Wimbledon)
entry:    Apply grass surface adjustments to all signals from grass tournament day 1
exit:     End of Wimbledon — then hard court adjustments apply
filter:   Load player-specific grass records from Tennis Abstract; note historical
          grass specialists vs clay specialists; update H2H surface splits
sizing:   1.0× standard — surface switch is systematic adjustment, not directional signal
note:     The clay-to-grass transition is where the most surface-prediction errors occur.
          Players who excelled on clay 2 weeks prior may be 20–30% less effective on grass.
          Highest-value signal: previous Wimbledon results vs current form.
```

### Playbook 4: Long-match withdrawal risk (5-set, late tournament)
```
trigger:  Quarterfinal or later, player has played 4+ sets in previous 2 rounds
entry:    Flag risk pre-match; if injury was mentioned post-match, increase flag severity
exit:     Through-match monitoring; reassess at 2 sets each
filter:   Check post-match interview from previous round; check serve speed data trend
          (declining serve speed is the earliest measurable injury signal in tennis)
sizing:   0.5× standard — withdrawal possibility creates binary outcome risk
note:     Mid-match retirement is the single highest-variance event in tennis prediction.
          Cannot be reliably predicted but can be risk-managed through reduced sizing.
          Chronic shoulder, knee injuries in known players should always be flagged.
```

## Key Commands

| Action | Skill | When to use |
|---|---|---|
| Domain intelligence | `sports/tennis/sport-domain-tennis.md` | Every analysis |
| Athlete modifier | `athlete/tennis/athlete-intel-tennis.md` | After domain load |
| Injury check | `core/injury-intelligence/core-injury-intelligence.md` | Injury concern |
| Weather modifier | `core/core-weather-match-day.md` | Outdoor courts only |
| Market context | `market/market-tennis.md` | Token decisions |

## Data Sources

- **Primary statistics:** Tennis Abstract (tennisabstract.com) — surface splits, H2H, serve stats
- **Official rankings:** ATP (atptour.com), WTA (wtatennis.com)
- **Historical results:** Ultimate Tennis Statistics (ultimatetennisstatistics.com)
- **Live scoring:** FlashScore, LiveScore tennis
- **Match Charting Project:** github.com/JeffSackmann (detailed shot data)
- **Odds:** Pinnacle tennis section, Betfair Exchange (deepest liquidity)
