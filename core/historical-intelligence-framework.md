---
name: historical-intelligence-framework
description: >
  Framework for incorporating head-to-head records, historical meeting data,
  and form-based probability signals into SportMind pre-match analysis. Covers
  how to weight historical data relative to current form, how H2H relevance
  decays over time, sport-specific H2H weighting rules, win/draw/loss
  probability modelling from form and H2H combined, venue and surface effects
  on historical data, and tournament bracket prediction. The key design
  principle: historical data is a modifier, not a predictor. Current form,
  lineup quality, and structural signals take precedence. Use alongside
  core/lineup-quality-index.md and core/pre-match-squad-intelligence.md.
  Load when: H2H data is available AND the fixture has a meaningful meeting
  history. Do not load for first-time matchups or newly promoted clubs.
---

# Historical Intelligence Framework — SportMind

**How to use the past without being trapped by it.**

Historical data is valuable. It is also the most commonly misused signal in
sports prediction. A head-to-head record from three seasons ago, before either
manager was appointed, before key signings arrived, carries almost no predictive
weight for tonight's match — yet many analysts treat it as primary evidence.

This framework defines exactly how SportMind agents should incorporate
historical meeting data: as a time-decayed modifier that confirms or contradicts
current signals, never as a standalone predictor.

---

## The core principle: decay over recency

```
Historical data has a half-life. Its predictive value diminishes with:
  1. Time elapsed since the meeting
  2. Personnel changes (manager, key players)
  3. Tactical evolution (formation/system change)
  4. Competitive context changes (promotion/relegation)

DECAY IS FASTER IN:
  Team sports with frequent squad turnover (football, basketball)
  Sports with tactical innovation (MMA, esports)
  Competitions with format changes (T20 cricket, new competition structure)

DECAY IS SLOWER IN:
  Individual sports with same two competitors (tennis, boxing, MMA rematches)
  Sports where physical attributes dominate tactics (athletics, swimming)
  Rivalries with documented psychological dimension (India-Pakistan cricket)
```

---

## H2H relevance score — the decay formula

```
H2H_RELEVANCE = base_weight × recency_factor × personnel_continuity × context_factor

BASE_WEIGHT by number of recent meetings:
  10+ meetings in last 3 seasons:   1.00 (statistically meaningful)
  5–9 meetings:                     0.85 (usable with caution)
  3–4 meetings:                     0.65 (directional only)
  1–2 meetings:                     0.35 (barely meaningful)
  0 meetings:                       0.00 (ignore H2H entirely)

RECENCY_FACTOR (most recent meeting):
  Last 6 months:     1.00
  6–12 months:       0.85
  12–18 months:      0.70
  18–24 months:      0.55
  24–36 months:      0.40
  36+ months:        0.20 (historical context only — not a signal)

PERSONNEL_CONTINUITY (how much has each team changed?):
  Same manager + 7+ starters still present:   1.00
  Same manager + 4–6 starters present:        0.80
  New manager, same core players:             0.60
  Same manager, major squad rebuild:          0.55
  Both teams substantially changed:           0.35
  One team newly promoted (no prior meetings at this level): 0.10

CONTEXT_FACTOR:
  Same competition, same approximate league position:  1.00
  Same competition, very different circumstances:      0.80
  Different competition (e.g. league vs cup):          0.65
  Different era (pre-relegation vs post-promotion):    0.30

COMBINED:
  H2H_RELEVANCE = base × recency × personnel × context
  Clamp to [0.00, 1.00]

  Above 0.60: H2H is a meaningful modifier
  0.35–0.59:  H2H is directional context only — apply at half weight
  Below 0.35: Do not apply H2H as a signal modifier
```

---

## H2H modifier — converting record to signal adjustment

```
Once H2H_RELEVANCE is established, convert the win/draw/loss record
into a modifier:

H2H_WIN_RATE = wins / total_meetings (for the team being analysed)

H2H modifier table:
  Win rate ≥ 75%:   ×1.08  (dominant H2H record)
  Win rate 60–74%:  ×1.04  (positive H2H edge)
  Win rate 45–59%:  ×1.00  (no meaningful H2H advantage)
  Win rate 30–44%:  ×0.96  (slight H2H disadvantage)
  Win rate < 30%:   ×0.92  (significant H2H disadvantage)

WEIGHTED H2H MODIFIER:
  weighted_h2h_mod = 1.00 + ((h2h_raw_mod - 1.00) × H2H_RELEVANCE)

  Example:
    Arsenal vs Bournemouth H2H: Arsenal 8W 2D 1L in last 11 (win rate 73%)
    Raw modifier: ×1.04
    H2H_RELEVANCE: 0.72 (recent meetings, some squad change)
    Weighted: 1.00 + (0.04 × 0.72) = ×1.029

  The 1.029 modifier reflects Arsenal's H2H advantage, dampened
  by the relevance score. It does not override the structural signals
  but adds modest confidence to the HOME direction.

AGENT RULE:
  H2H modifier maximum impact: ±0.08 to the adjusted_score.
  Never allow H2H alone to flip a signal direction.
  If H2H says one thing and LQI says another, LQI takes precedence.
```

---

## Sport-specific H2H weighting rules

### Football

```
WHAT DECAYS FASTEST:
  Manager tactics (formation, pressing intensity, set piece routines)
  Set piece routines specifically — these are manager-designed
  Squad chemistry and partnership combinations

WHAT PERSISTS LONGER:
  Psychological dimension in derbies (El Clásico, NW Derby, Arsenal-Spurs)
  Venue effects — some teams genuinely perform worse at specific grounds
  Fan atmosphere effects on specific opponents

SPECIAL CASES:
  Derby/rivalry matches:
    Psychological factor (panic, over-arousal, referee impact) adds
    an additional ×1.05–1.15 multiplier to the rivalry team's H2H record
    See core/core-narrative-momentum.md for full rivalry model

  Title/relegation deciders between frequent opponents:
    High-stakes H2H records weight at 1.5× standard
    "This team always rises to the big occasion" is real in football
    Requires: 3+ high-stakes meetings with consistent pattern

  Home record vs specific opponents:
    Some teams are categorically harder to beat at home for certain opponents
    Flag if: opponent has lost last 4+ at this venue regardless of form
    Apply venue-specific H2H sub-modifier (separate from overall H2H)
```

### Tennis

```
TENNIS IS THE SPORT WHERE H2H MATTERS MOST.
The same two players compete repeatedly. Decay is slowest here.

SURFACE-CONDITIONAL H2H (always split H2H by surface):
  Overall H2H:           Lowest weight (0.50 of surface-adjusted)
  Clay H2H:              Full weight on clay matches
  Grass H2H:             Full weight on grass matches
  Hard court H2H:        Full weight on hard court matches

  Example: Djokovic vs Alcaraz
    Overall H2H: Djokovic +1 (6-5)  → neutral signal
    Clay H2H:    Alcaraz dominant (3-1) → ×0.94 for Djokovic on clay
    Hard court:  Djokovic slightly ahead (3-2) → ×1.02 for Djokovic on hard

  The surface split reveals what the aggregate conceals.

RECENCY IN TENNIS:
  Tennis players evolve rapidly (coaching changes, physical development)
  Apply full recency decay as standard
  Exception: psychological dominance patterns
    If one player has never beaten another in 8+ attempts,
    apply ×0.90 psychological disadvantage modifier regardless of form
    (documented in Federer vs Djokovic patterns, Nadal vs Djokovic on clay)

RETIREMENT RISK INTERACTION:
  If player has physical concerns AND poor H2H at this tournament:
    Combine retirement_risk modifier with H2H disadvantage
    Maximum combined penalty: ×0.75
```

### Cricket

```
BATTER VS BOWLER H2H:
  Most precise H2H data in any sport — individual matchup level
  Already covered in athlete/cricket/athlete-intel-cricket.md
  Apply directly; this framework provides the context layer

TEAM H2H:
  Test cricket: team H2H decays moderately (5-year window meaningful)
  ODI/T20: team H2H decays faster (format evolution is rapid)

INDIA-PAKISTAN SPECIAL CASE:
  H2H data for India-Pakistan is structurally unreliable as a predictor
  because the psychological multiplier (NCSI ×2.00) overwhelms historical
  form differences. Apply NCSI signal; reduce H2H weight to 0.20.
  See fan-token/world-cup-2026-intelligence/ for ICC tournament context.

VENUE EFFECT:
  Home subcontinent vs away is the primary structural factor in cricket
  Historical records in home conditions weight at 1.30×
  Test series in England: England home advantage is well-documented
  India in England: historically struggles (apply context-conditional H2H)
```

### MMA and Boxing

```
REMATCH CONTEXT:
  In MMA/boxing, the first fight is the primary H2H signal.
  But it decays rapidly based on:
    Time since fight (6+ months: apply full recency decay)
    Physical development (both fighters may be materially different)
    Camp quality change (new coach, weight class move)

  REMATCH MODIFIER:
    If fighter won first fight by KO/TKO: ×1.05 psychological advantage
    If fighter lost first fight by decision: ×0.96 (learning opportunity)
    If fight went to contested decision: neutral on rematch (50/50)
    If second fight in trilogy: independent context — do not chain

  STYLE MATCHUP > OVERALL H2H:
    A grappler who lost to a wrestler is not in a poor H2H pattern —
    it is a style pattern. Distinguish:
      Style matchup (structural): persists regardless of squad changes
      H2H record (contextual): decays with time and form changes

  See athlete/{sport}/athlete-intel-mma.md for full style matchup model
```

### Formula 1

```
CIRCUIT-SPECIFIC HISTORICAL PERFORMANCE:
  The F1 equivalent of H2H is driver/team vs specific circuit.
  Decays moderately (car regulations change every few years).

  CIRCUIT PERFORMANCE INDEX:
    Average qualifying position at this circuit (last 3 seasons): primary
    Average finishing position relative to qualifying: secondary
    Technical circuit type fit (power vs downforce): structural signal

  SEASON REGULATION BREAK:
    New technical regulations reset circuit histories significantly.
    After major reg change: weight historic circuit data at 0.40 only.
    Within stable regulations: weight at 0.80.

  MONACO SPECIAL CASE:
    Monaco is the single circuit where historical data has highest weight.
    Pole position → ~75% race win probability (already in F1 sport domain).
    Historical Monaco performance is genuinely predictive beyond other circuits.
    Recency decay is slower here: 3-season window at full weight.
```

### Basketball (NBA)

```
REGULAR SEASON H2H:
  Teams play each other 2-4 times per season.
  Regular season H2H has LOW predictive value for individual game.
  Teams rest players, experiment, and manage load in regular season.
  Apply H2H at 0.50 weight in regular season.

PLAYOFF H2H:
  Same series H2H is HIGHLY predictive.
  Team that wins Games 1-2 wins the series 80%+ historically.
  Series H2H is the most meaningful H2H in any team sport.
  Apply: if team is 2-0 up in a series, ×1.15 for next game prediction.

HISTORICAL PLAYOFF MATCHUPS:
  If teams have met in playoffs before in recent seasons:
    Psychological patterns are real in NBA playoffs
    "This team always beats us when it matters" narrative
    Apply at 0.70 weight (relevant but fades with roster changes)
```

---

## Form-based probability model

```
This is not a Elo or Poisson model. SportMind does not generate
win probabilities as output — it produces directional signals (HOME/AWAY/DRAW)
with SMS confidence scores. This section teaches agents how to convert
SportMind signals into probability estimates when needed.

CONVERTING SMS TO PROBABILITY RANGE:

SMS 80-100: HIGH QUALITY signal
  HOME direction → P(home win): 65-75%
  AWAY direction → P(away win): 60-70%
  (high quality signal = high confidence, not certainty)

SMS 60-79: GOOD signal
  HOME direction → P(home win): 55-65%
  AWAY direction → P(away win): 50-60%

SMS 40-59: MODERATE signal
  HOME direction → P(home win): 48-58%
  AWAY direction → P(away win): 44-54%
  (moderate SMS with direction = slight lean, not strong prediction)

SMS < 40: LOW QUALITY — do not convert to probability
  Signal quality insufficient for probability estimation
  Output: INSUFFICIENT_SIGNAL

ADDING H2H AND LQI TO PROBABILITY:
  base_probability = SMS_to_probability(sms, direction)
  h2h_adjustment  = (h2h_win_rate - 0.50) × H2H_RELEVANCE × 0.20
  lqi_adjustment  = (LQI - 1.00) × 0.15

  adjusted_probability = base + h2h_adjustment + lqi_adjustment
  Clamp to [0.10, 0.90] — never express certainty

  Draw probability (football/rugby/cricket):
    base_draw = 0.25 for football standard
    Reduce if: strong SMS signal (×0.80)
    Increase if: very similar LQI + neutral H2H (×1.20)
    High-stakes match: draw probability reduces (both teams playing to win)

AGENT RULE:
  Express probability ranges, not point estimates.
  "Arsenal 58-66% probability" not "Arsenal 62% probability."
  Precision is false confidence. Ranges reflect genuine uncertainty.
```

---

## Tournament and bracket prediction

```
TOURNAMENT PREDICTION DIFFERS FROM SINGLE-MATCH PREDICTION:
  Each round is an independent event with compounding uncertainty.
  The probability of winning a tournament is the product of probabilities
  of winning each individual match — error compounds.

  A team with 65% win probability per match:
    Quarter-final: 65%
    Semi-final (if won QF): 65%
    Final (if won SF): 65%
    Tournament win: 0.65 × 0.65 × 0.65 = 27%

  This is why tournament prediction requires much wider probability ranges
  than single-match prediction.

SPORTMIND TOURNAMENT FRAMEWORK:

ROUND-BY-ROUND SIGNALS:
  Generate a fresh pre-match signal for each fixture as it approaches.
  Do not attempt to predict tournament bracket outcomes more than 1 round ahead.
  Exception: seeding-based markets (who reaches the final) — use NCSI multipliers.

NCSI AMPLIFICATION BY ROUND (already in tournament-specific skills):
  Group stage:     NCSI × 1.00
  Round of 16:     NCSI × 1.25
  Quarter-final:   NCSI × 1.50
  Semi-final:      NCSI × 1.75
  Final:           NCSI × 2.00
  Championship win: NCSI × 2.50+

H2H IN TOURNAMENT CONTEXT:
  Knockout format amplifies H2H psychological effects.
  "Never lost to this opponent in knockouts" is a real pattern.
  Weight tournament-specific H2H at 1.30× standard H2H weight.

FORMAT-SPECIFIC NOTES:
  World Cup / Euros: Group stage draws reset between rounds. Fresh signal each match.
  Tennis slams: Surface is the primary structural factor for H2H.
  UFC title fights: Championship rounds (4-5) change fight dynamics significantly.
  NBA playoffs: Series momentum is the primary signal (see basketball section above).
  Cricket tournaments: Pitch conditions at specific venue often matter more than H2H.
```

---

## Applying historical intelligence in the agent chain

```
WHEN TO LOAD THIS SKILL:

✅ Load when:
  Meaningful H2H history exists (5+ meetings in last 3 seasons)
  Rivalry/derby fixture (H2H psychological dimension)
  Tennis surface-specific H2H available
  MMA rematch or trilogy fight
  Tournament knockout stage

⚠️  Load with caution:
  Only 2-3 historical meetings (use directional only)
  Major personnel changes since last meeting
  Competition format recently changed

❌ Do not load:
  First-ever meeting between competitors
  Newly promoted club with no top-division H2H history
  Post-major-regulation-change F1 seasons (first 3 races)

POSITION IN AGENT CHAIN:
  1. macro/macro-overview.md
  2. sports/{sport}/sport-domain-{sport}.md
  3. THIS SKILL — historical-intelligence-framework.md
     → Calculate H2H_RELEVANCE
     → Compute weighted H2H modifier
  4. core/lineup-quality-index.md
     → LQI for today's actual lineup
  5. core/pre-match-squad-intelligence.md
     → Full squad brief
  6. athlete/{sport}/athlete-intel-{sport}.md
     → Form and availability modifiers
  7. Final signal assembly

COMBINED MODIFIER OUTPUT:
{
  "h2h_relevance":      0.72,
  "h2h_win_rate":       0.73,
  "h2h_raw_modifier":   1.04,
  "h2h_weighted_mod":   1.029,
  "lqi":                0.919,
  "direction":          "HOME",
  "adjusted_score":     42.4,
  "probability_range":  "52-60%",
  "plain_english":      "Arsenal have a good head-to-head record against Bournemouth but are significantly weakened today. The historical edge is modest; today's lineup quality is the bigger variable."
}
```

---

*SportMind v3.50 · MIT License · sportmind.dev*
*See also: core/lineup-quality-index.md · core/pre-match-squad-intelligence.md*
*core/core-athlete-modifier-system.md · core/player-statistical-reasoning.md*
*core/core-narrative-momentum.md · athlete/meta/athlete-intel-cross-sport-orchestrator.md*
