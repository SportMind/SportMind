---
name: lineup-quality-index
description: >
  Bottom-up team strength model that aggregates individual player ratings
  into a composite Lineup Quality Index (LQI) for any confirmed or projected
  starting lineup. Covers football, basketball, rugby, cricket, hockey, and
  MMA fight cards. The LQI answers the question your friend asked: today's
  team with Martinelli starting, Lewis, Ben White, and Eze not starting is
  not a full-strength Arsenal — and that difference is measurable. Feeds
  directly into the composite_squad_modifier pipeline. Use alongside
  core/pre-match-squad-intelligence.md for the full squad picture.
  Load when: lineup is confirmed or projected and you need a strength
  score for the actual XI, not the theoretical best XI.
---

# Lineup Quality Index (LQI) — SportMind

**Rate each player. Aggregate to a team score. That score is the signal.**

The Lineup Quality Index is the quantitative answer to a simple question:
how strong is *today's actual team* compared to the team's theoretical best,
and compared to the opponent's team today?

SportMind already models individual player availability (CONFIRMED/DOUBT/OUT)
and individual RQD (Replacement Quality Delta). What it does not do — until
this skill — is aggregate those individual ratings into a single team-level
strength score that can be compared across matchups.

Your friend identified this gap precisely: Arsenal with Martinelli starting,
Lewis, Ben White and Eze not starting is not a full-strength Arsenal. The
question is: what score does that lineup get, and what does that mean for the
prediction?

---

## The LQI formula

```
LQI = Σ (player_rating × positional_weight × availability_factor) / baseline_XI_score

Where:

player_rating:        Position-normalised performance score (0–100)
                      Sources: Sofascore match ratings, WhoScored, TransferMarkt
                      Use: season average rating for that player in that role

positional_weight:    How much does this position affect match outcomes?
                      Sport-specific. See tables below.

availability_factor:  Accounts for fitness and return-curve impairment
                      CONFIRMED, fully fit:           1.00
                      CONFIRMED, return-curve match 1-3: 0.82–0.90
                      PROBABLE:                       0.95
                      DOUBT (playing):                0.80
                      STARTER replaced by backup:     replacement_rating / starter_rating

baseline_XI_score:    The team's full-strength first-choice XI score
                      Calculate once per season; update on transfers

LQI interpretation:
  1.00 = full-strength first-choice XI
  0.90–0.99: minor weakening (1-2 rotations or B-team players)
  0.80–0.89: moderate weakening (key absences, notable rotation)
  0.70–0.79: significant weakening (multiple key players absent)
  < 0.70:    severely weakened lineup — flag as LINEUP_DEGRADED
```

---

## Positional weight tables

### Football (11 players)

```
POSITIONAL WEIGHTS (sum to 11.0):

Goalkeeper:           1.8  — Highest single position; GK quality has disproportionate impact
Centre-back 1:        1.2
Centre-back 2:        1.2  — Partnership value (see injury-intel-football.md CB disruption)
Full-back (2×):       0.9 each  = 1.8 total
Holding midfielder:   1.1  — Defensive linchpin; loss disrupts structure significantly
Central midfielders:  0.9 each (×1 or 2 depending on formation)
Attacking mid/10:     1.1  — Creative hub; set piece taker dependency
Wingers (2×):         0.9 each = 1.8 total
Striker/CF:           1.2  — Goals are the scarcest resource; top scorer impact highest

FORMATION ADJUSTMENT:
  4-3-3 vs 4-2-3-1: redistribute CM weights accordingly
  3-5-2: wing-back weight increases to 1.1 (dual role)
  5-3-2: CB3 weight 1.0; both strikers 1.0

KEY MULTIPLIERS:
  Set piece specialist (corners/free kicks): ×1.15 for attacking set pieces
  Captain / senior leader: ×1.05 (morale and organisation)
  Goalkeeper playing behind organised defence: position weight ×0.95
  Goalkeeper playing behind disorganised emergency defence: position weight ×1.10
```

### Basketball (5 starters)

```
POSITIONAL WEIGHTS (sum to 5.0):

Point guard (PG):    1.2  — Offensive system control; assists and decision-making
Shooting guard (SG): 0.9  — Scoring volume; varies by system
Small forward (SF):  0.9  — Versatility; two-way value
Power forward (PF):  1.0  — Rebounding, pick-and-roll; system dependent
Centre (C):          1.0  — Paint presence; rim protection

STAR PLAYER ADJUSTMENT:
  Net rating > +8:  positional weight ×1.30 (star premium)
  Net rating +4-8:  positional weight ×1.15
  Net rating 0-4:   standard weight
  Net rating < 0:   positional weight ×0.90

LOAD MANAGEMENT:
  Player on REST designation: availability_factor = 0.00 (not playing)
  GTD player: availability_factor = 0.50 until confirmed
```

### Rugby Union (15 players)

```
POSITIONAL WEIGHTS (sum to 15.0):

Front row (props ×2, hooker): 1.0 each = 3.0
  (Scrum quality is primary forward battle metric)
Locks (×2):          0.9 each = 1.8  (lineout and carrying)
Flankers (×2):       1.0 each = 2.0  (breakdown; crucial in modern game)
Number 8:            1.0
Scrum-half:          1.2  — Service quality affects backline timing
Fly-half (10):       1.5  — Highest criticality; kicking, decision-making, tactical control
Centres (×2):        0.9 each = 1.8
Back three (×3):     0.8 each = 2.4  (finishing; kick-chase)

KICKER ADJUSTMENT:
  Primary kicker absent: −5 to −8 points per match expected (penalty/conversion loss)
  Apply as separate signal, not just positional weight
```

### Cricket (playing XI)

```
CRICKET LQI — distinct from other sports because roles overlap:

BATTING ORDER WEIGHTS:
  Openers (×2):      1.1 each = 2.2  (set tone; face new ball)
  Top order (3-5):   1.2, 1.1, 1.0   (key run-scoring positions)
  Middle order (6-7): 0.9 each = 1.8  (recovery and acceleration)
  Lower order (8-11): 0.7 each = 2.8  (minimal batting contribution expected)

BOWLING WEIGHTS (all formats):
  Lead pacer:        1.3  — Wicket-taking primary weapon
  Secondary pacer:   1.0
  Lead spinner:      1.2  — Format dependent (T20: lower; Test: higher)
  Part-time bowler:  0.7  — Overs must be completed

FORMAT ADJUSTMENT:
  Test match:    Batting weight × 1.2; top-order loss more damaging
  ODI:           Balanced batting/bowling weights as shown
  T20:           Powerplay batting × 1.3; death-over specialist × 1.2

SPECIAL NOTE — INDIA:
  Kohli/Rohit presence in batting lineup: apply NCSI ×2.0 flag (commercial signal)
  Their absence: LQI degradation AND separate NCSI signal reduction
```

### Ice Hockey (6 skaters + GK)

```
POSITIONAL WEIGHTS (sum to 7.0):

Goaltender:          2.0  — Single most impactful position in hockey
                           (GSAx differential is primary game-level predictor)
Top line forward (×3): 0.9 each = 2.7
Second line (×3):    0.7 each = 2.1  (abbreviated; third/fourth lines less critical)
Top pairing D (×2):  0.9 each = 1.8
Second pairing D (×2): 0.7 each = 1.4

POWER PLAY UNIT:
  PP1 specialist absent: −15% power play efficiency estimate
  Apply as modifier to expected goals, not just LQI
```

### MMA Fight Card

```
MMA LQI — card-level quality, not team-level

MAIN EVENT WEIGHT:  0.60 of total card signal
CO-MAIN EVENT:      0.25
PRELIMS (×N):       0.15 total

FIGHT QUALITY SCORE (per bout):
  Both fighters ranked top 10: 1.20
  One fighter ranked top 10:   1.05
  Both ranked 11-25:           1.00
  Unranked fighters:           0.80
  Late replacement:            0.70
  Unranked vs late replacement: 0.55

CARD LQI:
  Sum of weighted fight quality scores.
  Main event replacement: card LQI drops by 0.30–0.50 immediately.
  Co-main replacement: card LQI drops by 0.12–0.20.
```

---

## Worked example: Arsenal vs Bournemouth (11 April 2026)

```
ARSENAL FIRST-CHOICE XI (baseline LQI = 1.00):
  GK:     Raya        rating 82  weight 1.8  avail 1.00  contribution: 147.6
  CB:     White       rating 80  weight 1.2  avail 1.00  contribution:  96.0
  CB:     Gabriel     rating 79  weight 1.2  avail 1.00  contribution:  94.8
  LB:     Zinchenko   rating 75  weight 0.9  avail 1.00  contribution:  67.5
  RB:     Timber      rating 77  weight 0.9  avail 1.00  contribution:  69.3
  DM:     Rice        rating 87  weight 1.1  avail 1.00  contribution:  95.7
  CM:     Odegaard    rating 89  weight 1.1  avail 1.00  contribution:  97.9
  LW:     Saka        rating 91  weight 0.9  avail 1.00  contribution:  81.9
  RW:     Martinelli  rating 82  weight 0.9  avail 1.00  contribution:  73.8
  AM:     Trossard    rating 77  weight 0.9  avail 1.00  contribution:  69.3
  ST:     Jesus       rating 78  weight 1.2  avail 1.00  contribution:  93.6
  ─────────────────────────────────────────────────────────────────────
  BASELINE SCORE: 987.4  →  LQI = 1.00

ACTUAL LINEUP (11 April 2026):
  GK:     Raya        rating 82  weight 1.8  avail 1.00  contribution: 147.6
  CB:     Gabriel     rating 79  weight 1.2  avail 1.00  contribution:  94.8
  CB:     Kiwior      rating 68  weight 1.2  avail 1.00  contribution:  81.6  ← Ben White absent
  LB:     Zinchenko   rating 75  weight 0.9  avail 1.00  contribution:  67.5
  RB:     Lewis       rating 72  weight 0.9  avail 1.00  contribution:  64.8  ← Timber out
  DM:     Rice        rating 87  weight 1.1  avail 0.90  contribution:  86.1  ← return curve ×0.90
  CM:     Jorginho    rating 70  weight 1.1  avail 1.00  contribution:  77.0  ← Partey suspended
  LW:     Martinelli  rating 82  weight 0.9  avail 1.00  contribution:  73.8
  RW:     Gyokeres    rating 74  weight 0.9  avail 1.00  contribution:  66.6  ← Saka absent; unexpected
  AM:     Trossard    rating 77  weight 0.9  avail 1.00  contribution:  69.3
  ST:     Nwaneri     rating 66  weight 1.2  avail 1.00  contribution:  79.2  ← Jesus long-term out
  ─────────────────────────────────────────────────────────────────────
  ACTUAL SCORE: 907.3

  LQI = 907.3 / 987.4 = 0.919

INTERPRETATION:
  LQI 0.919 → MODERATE WEAKENING (0.90–0.99 tier)
  But note: this is an aggregate. The attacking end is heavily affected.
  Striker (Jesus out → Nwaneri): RQD 0.154 — significant
  Right wing (Saka out → Gyokeres): RQD 0.132 — significant
  Together these two positions represent 2.1 combined weight
  and a combined rating shortfall of ~42 points.

  PRE-MATCH SIGNAL ADJUSTMENT:
  Base signal: HOME (adjusted_score 55.0)
  Squad modifier from pre-match-squad-intelligence: ×0.84
  LQI modifier: ×0.919
  Combined: 55.0 × 0.84 × 0.919 = 42.4

  → Signal now sits in MEDIUM confidence territory.
  → Saka absence alone from 91 → 74 at RW is the largest single degradation.
  → This explains the result: Bournemouth's defensive block held against a
    weakened Arsenal attack that lacked their primary creative threat.
```

---

## LQI vs opponent LQI — the matchup score

```
The LQI becomes most powerful when compared against the opponent.

MATCHUP SCORE = home_LQI - away_LQI  (normalised to same baseline scale)

Interpretation:
  +0.15 or more:   Strong home quality advantage
  +0.05 to +0.14:  Moderate home advantage
  -0.05 to +0.04:  Quality parity — other factors dominate
  -0.05 to -0.14:  Away team quality advantage (upset risk elevated)
  -0.15 or more:   Strong away quality advantage — consider against home signal

AGENT RULE:
  If MATCHUP_SCORE contradicts the primary direction signal:
    → Reduce adjusted_score by 8-15%
    → Flag: LQI_SIGNAL_CONFLICT = True
    → Do not flip direction from LQI alone — it is one input, not the model

  If MATCHUP_SCORE confirms the primary direction signal:
    → Confidence boost: adjusted_score +3-8%
    → Note as CONFIRMING signal in reasoning chain
```

---

## Data sources for player ratings

```
TIER 1 — Use as primary:
  Sofascore (sofascore.com):
    Real-time match ratings after each game.
    Algorithm-generated 1-10 scale (normalise to 0-100 for LQI).
    Available for football, basketball, hockey, cricket.
    Best for: in-season current form ratings.

  WhoScored (whoscored.com):
    Algorithmic match ratings for football.
    More conservative than Sofascore; useful for cross-check.

  NBA.com advanced stats:
    Net rating per player — use as rating proxy for basketball LQI.
    Season average net rating maps to 0-100 after normalisation.
    Normalise: net_rating_normalised = 50 + (net_rating × 3.5), clamped to [0,100]

  Hockey Reference / Natural Stat Trick:
    GSAx (Goals Saved Above Expected) for goaltenders.
    Normalise GSAx to 0-100 for LQI GK rating.

TIER 2 — Use when Tier 1 unavailable:
  TransferMarkt market value as proxy rating:
    market_value_rating = log10(market_value_EUR) × 10, clamped to [40, 95]
    Use only when no performance rating available.
    Less accurate but usable for lower-profile leagues and tournaments.

  FIFA/EA FC ratings:
    Reasonable proxy for baseline player quality.
    Lag real form by 6-12 months — adjust downward for declining players.
    Use only for baseline_XI_score calculation, not match-day form.

AGENT INSTRUCTION:
  Load fresh ratings within 7 days of match.
  Do not use ratings older than one month without applying
  form trend adjustment (improving × 1.05; declining × 0.95).
```

---

## Integration with SportMind modifier pipeline

```
POSITION IN THE PIPELINE:

  1. macro/macro-overview.md                    → macro_modifier
  2. sports/{sport}/sport-domain-{sport}.md     → base_signal + context
  3. core/pre-match-squad-intelligence.md       → composite_squad_modifier
  4. THIS SKILL — lineup-quality-index.md       → LQI modifier
  5. athlete/{sport}/athlete-intel-{sport}.md   → form + availability sub-mods
  6. core/injury-intelligence/                  → RQD per absence
  7. fan-token/ stack                           → commercial signal
  8. macro/                                     → final macro gate

LQI FEEDS INTO:
  composite_squad_modifier:
    Replace the availability-only modifier with:
    adjusted_squad_modifier = composite_squad_modifier × LQI_delta
    where LQI_delta = (LQI - 1.00) × 0.60 + 1.00
    (0.60 dampening factor prevents LQI from dominating the composite)

  adjusted_score:
    adjusted_score = base_score × composite_modifier × LQI_delta

  plain_english_brief (Prompt 21 / 22):
    Add LQI interpretation to the squad status section:
    "Arsenal are at about 92% of full strength today — the attacking
    positions are most affected."

WHEN TO APPLY LQI:
  ✅ Confirmed lineup available (T-2h or official announced)
  ✅ Rotation expected (manager signalled changes, cup tie)
  ✅ Multiple key players absent (2+ key positions weakened)
  ⚠️  Use with caution for projected lineups (T-24h) — weight LQI at 0.70
      until officially confirmed
  ❌ Do not apply LQI when all 11 starters are confirmed first-choice
     (LQI = 1.00, no modifier needed)
```

---

## Season baseline — maintaining the first-choice XI score

```
WHEN TO UPDATE THE BASELINE:
  Transfer window close (Jan/Aug): recalculate full baseline
  Major injury to first-choice player (Tier A/B): update that position
  Manager change: recalculate positional weights (new formation)

BASELINE STORAGE (Memory MCP schema):
{
  "team": "Arsenal",
  "season": "2025-26",
  "baseline_calculated": "2026-01-01",
  "baseline_lqi_score": 987.4,
  "formation": "4-3-3",
  "first_choice_xi": {
    "GK": {"player": "Raya", "rating": 82, "weight": 1.8},
    "CB1": {"player": "White", "rating": 80, "weight": 1.2},
    ...
  }
}
```

---

*SportMind v3.50 · MIT License · sportmind.dev*
*See also: core/pre-match-squad-intelligence.md · core/injury-intelligence/*
*core/core-athlete-modifier-system.md · core/player-statistical-reasoning.md*
*agent-prompts/agent-prompts.md Prompt 21/22*
