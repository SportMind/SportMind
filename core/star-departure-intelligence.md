---
name: star-departure-intelligence
description: >
  Intelligence framework for the commercial and fan token impact of a
  star athlete departing their club, team, or competition. Covers: departure
  type classification, the AELS void model (how engagement drops and recovers
  at the source club), LTUI reset triggers, FTP Path 2 win-probability
  impact (departing ATM players reduce supply reduction pace), replacement
  commercial quality timeline, search and social signal classification
  (departure mentions ≠ positive engagement), and the cross-token contagion
  effect. Applies to football, NBA, cricket, F1, rugby, MMA, and any team
  sport with commercially dominant athletes. The APS answers what value
  travels TO the destination. This skill answers what value is LOST at
  the source — the mirror the library was missing.
  Load when: a key player departure is confirmed or rumoured AND the
  source club has an active fan token OR is in a fan token readiness tier.
---

# Star Departure Intelligence — SportMind

**The other side of the APS. Not what travels with the player — what stays
behind. And what shape the void takes.**

`fan-token/transfer-signal/` computes the APS: how much of an athlete's
commercial value transfers to the destination club. That is the buying
club's question.

This skill answers the selling club's question: what do we lose, how
long does the void last, what does it do to our fan token, and when
does a replacement recover the lost signal?

---

## Departure type classification

```
Not all departures are equal. The type determines the duration and
shape of the commercial void.

TYPE 1 — CROSS-LEAGUE TRANSFER (rival or neutral)
  Example: Ronaldo to Al-Nassr, Mbappe to Real Madrid
  Characteristics:
    - Defined handover date (transfer confirmed → departure date)
    - Club receives fee (financial compensation, not commercial)
    - Replacement recruitment possible in same window
  Commercial void timeline: IMMEDIATE at transfer confirmation
  Recovery window: 12–24 months for full commercial rebuild
  Fan token initial impact: -10–25% (result impact matrices baseline)
  LTUI impact: Structural reset required if ATM score ≥ 0.65

TYPE 2 — RIVAL TRANSFER
  Example: Lewandowski to Barcelona (from Bayern), Salah hypothetical to Real
  Characteristics:
    - All Type 1 features PLUS fan sentiment damage from "betrayal" narrative
    - Social search volume spikes — but classified as distress signal, not positive
    - Some holder segment permanently exits (follows player to destination token)
  Commercial void timeline: IMMEDIATE + extended narrative damage period (6–12 weeks)
  Recovery window: 18–30 months
  Fan token initial impact: -15–30% (sentiment damage amplifier applied)
  LTUI impact: Structural reset + narrative damage modifier ×0.85

TYPE 3 — RETIREMENT
  Example: Messi retiring, Dhoni Test retirement, LeBron eventual retirement
  Characteristics:
    - No destination token gains at the expense of source
    - No replacement recruitment (role evolution, not direct replacement)
    - Global narrative: tribute arc (positive for sport, neutral-negative for token)
    - Long foreshadowing window — well-managed clubs pre-position
  Commercial void timeline: GRADUAL if well-managed (1–2 season wind-down)
                            IMMEDIATE if sudden/unexpected retirement
  Recovery window: 24–48 months — longest of all departure types
  Fan token initial impact: -8–20% (tribute sentiment cushions initial drop)
  LTUI impact: Major reset required — career-defining player anchored token identity

TYPE 4 — CAREER DECLINE DEPARTURE
  Example: Player sold as performance drops, released at contract end
  Characteristics:
    - Commercial signals already declining before departure
    - Market often anticipates; impact partially pre-priced
    - Replacement recruited with intent to upgrade
  Commercial void timeline: PRE-PRICED — gap is often smaller than expected
  Recovery window: 6–18 months (replacement upgrade case can be net positive)
  Fan token initial impact: -5–12% (partially anticipated)
  LTUI impact: Minimal if replacement is commercial upgrade; positive if so

TYPE 5 — SUSPENSION OR DISCIPLINARY REMOVAL
  Example: Player banned mid-season, sent on loan due to conduct
  Characteristics:
    - No replacement fee received; no planned departure
    - DSM framework applies (core/athlete-disciplinary-intelligence.md)
    - Social signal: bifurcated (some holders exit, some rally)
  Commercial void timeline: For ban duration; uncertain if indefinite
  Recovery window: Varies — disciplinary resolution is primary signal
  Fan token initial impact: Per DSM tier (Tier 1–4 modifiers already defined)
  Note: Use core/athlete-disciplinary-intelligence.md as primary skill;
        this framework applies to commercial void calculation only
```

---

## The AELS void model

```
AELS (Athlete Engagement Lift Score) measures how much a specific
athlete's content and activity lifts fan token holder engagement.
When that athlete departs, their AELS contribution goes to zero
at the source club. This creates a void.

STEP 1 — IDENTIFY AELS CONTRIBUTION
  If AELS has been computed: use the athlete's score directly.
  If not computed: estimate from ATM score and social following tier.
    ATM ≥ 0.75: Estimated AELS 70–85
    ATM 0.55–0.74: Estimated AELS 45–65
    ATM 0.35–0.54: Estimated AELS 25–40
    ATM < 0.35: Estimated AELS < 20

STEP 2 — COMPUTE AELS CONTRIBUTION SHARE
  Single departing player:
    AELS_share = athlete_AELS / (sum of all active ATM player AELS scores)
  
  Example (Arsenal, hypothetical Saka departure):
    Saka AELS:         82
    Rice AELS:         61
    Odegaard AELS:     74
    Martinelli AELS:   55
    Total squad AELS:  272
    Saka AELS share:   82/272 = 30.1%

STEP 3 — VOID MAGNITUDE
  AELS_void = AELS_share × current token HAS score
  
  Interpretation:
    AELS void 0–15%: MINOR — absorbed by remaining squad quickly
    AELS void 15–30%: SIGNIFICANT — 6–12 months to rebuild
    AELS void 30–50%: MAJOR — 12–24 months to rebuild; narrative void concurrent
    AELS void > 50%: CATASTROPHIC — token identity reconfiguration required
                      (player WAS the token's commercial identity)

  Arsenal/Saka example:
    AELS void = 30.1% × HAS 72 = 21.7% — SIGNIFICANT category

STEP 4 — RECOVERY CURVE
  AELS recovery follows a three-phase pattern:

  PHASE A — VOID (T+0 to T+3 months):
    Token AELS running at (100% - AELS_void%) of pre-departure baseline
    No replacement yet established; social engagement structurally lower
    Apply: composite_signal_modifier × (1 - AELS_void/100)

  PHASE B — TRANSITION (T+3 to T+12 months):
    Replacement player begins building AELS (typically 25–40% of departing
    player's score in first season — it takes time to build an audience)
    Partial recovery: modifier improves by 0.04–0.08 per quarter
    Accelerant: if replacement scores, wins titles, creates viral moments

  PHASE C — NEW EQUILIBRIUM (T+12 months+):
    New commercial identity established (or not)
    If replacement ATM ≥ departing ATM: full recovery
    If replacement ATM < departing ATM: permanent LTUI reset downward
    If no replacement found: structural plateau; lifecycle Phase 4 risk
```

---

## LTUI reset triggers

```
A star departure does not automatically drop LTUI — but it triggers
a recalculation that may produce a lower baseline.

LTUI RESET IS REQUIRED WHEN:

Trigger 1 — ATM departure (ATM score ≥ 0.60):
  The departing player's ATM contribution was material to the token's
  commercial events. Governance votes about that player, commercial
  partnerships featuring them, or fan sentiment anchored to them
  now need to be removed from the LTUI calculation.
  Action: Recalculate LTUI without the departed player's ATM contribution.
  
Trigger 2 — APS departure (APS score ≥ 0.70):
  High APS means a significant portion of the token's social audience
  came with that athlete. Those holders may migrate to the destination token.
  Action: Apply holder_migration_factor to projected holder count.
  holder_migration = APS × 0.25 (expected holder % who follow the athlete)

Trigger 3 — AELS void > 25%:
  The token's engagement engine has lost a quarter of its social lift.
  Future utility events will generate less engagement until the void is filled.
  Action: Reduce LTUI projection by AELS_void × 0.40 for next 12 months.

Trigger 4 — Commercial partnership specifically featuring the player:
  If active sponsorship / partnership was player-specific (shirt deal, etc.)
  and sponsor has option to exit: LTUI at risk of partnership termination.
  Action: Flag fan-token/fan-token-lifecycle partnership termination risk.
  Check: fan-token/fan-token-partnership-intelligence/ for termination signals.

LTUI RESET CALCULATION:
  adjusted_LTUI = current_LTUI
    - (ATM_contribution_removed × 8)     # loss of ATM-driven utility events
    - (AELS_void × 0.40 × 12_month_weight)  # engagement engine reduction
    - (holder_migration × 15)             # expected holder reduction

  If adjusted_LTUI represents a > 20-point drop from current:
    Flag: LTUI_STRUCTURAL_RESET = True
    Action: Notify agent that lifecycle phase review required
            (may signal Phase 3 → Phase 4 transition risk)
```

---

## Fan Token™ Play (Path 2) — supply mechanics impact

```
This is the most important fan token-specific implication of a star
departure that is not covered anywhere else in the library.

THE CONNECTION:
  FTP Path 2 supply mechanics depend on wins.
  Wins depend on squad quality.
  Squad quality drops when a key ATM player departs.
  Therefore: star departure → lower win probability → slower supply reduction.

CALCULATING THE FTP IMPACT:

STEP 1 — LQI impact of departure
  Compute the Lineup Quality Index change using core/lineup-quality-index.md.
  Identify the LQI delta: LQI_post_departure / LQI_pre_departure.

  Example (Arsenal, Saka departure, RW position weight 0.9):
    Pre-departure LQI: 1.00 (full strength)
    Saka contribution: 91 × 0.9 × 1.00 = 81.9
    Replacement (Martinelli at RW): 82 × 0.9 × 0.95 = 70.1
    LQI delta: -11.8 points → LQI 0.919 (matches actual observed)

STEP 2 — Win probability adjustment
  SportMind does not produce explicit win probabilities, but the adjusted_score
  reflects the signal strength. Lower LQI → lower adjusted_score → lower
  estimated win probability.
  
  Win_prob_adjustment = LQI_delta × 0.15
  (Each 0.10 LQI reduction ≈ 1.5% lower estimated win probability)
  
  Example: LQI 1.00 → 0.919 (delta -0.081)
    Win_prob_adjustment = -0.081 × 0.15 = -1.2% per match

STEP 3 — Season supply trajectory impact
  If the departure is permanent (transfer/retirement) for the full season:
  
  expected_wins_before = season_matches × win_probability_baseline
  expected_wins_after  = season_matches × (win_probability_baseline + win_prob_adjustment)
  wins_lost = expected_wins_before - expected_wins_after
  
  For each win lost:
    supply_reduction_lost = 0.24% (typical PATH_2 burn per win)
  
  Example (38-match Premier League season, Saka departure):
    Baseline win prob: 65% → expected wins: 24.7
    Adjusted win prob: 63.8% → expected wins: 24.2
    Wins lost: ~0.5 per season
    Supply reduction lost: 0.5 × 0.24% = 0.12% of supply per season
    
    This is small per season but compounds over multiple seasons:
    3 seasons × 0.12% = 0.36% less supply reduction than projected

STEP 4 — FTP modifier adjustment for agent chains
  When a confirmed high-ATM player departs from an FTP PATH_2 token:
  
  ftp_departure_modifier = 1.00 - (wins_lost / season_matches × 0.50)
  Apply to: gamified_path2_win_modifier trajectory projections only.
  
  DO NOT apply to match-level FTP mechanics (burn/mint per match is
  unchanged by who plays — the mechanism is the same regardless of squad).
  The adjustment is to the EXPECTED FREQUENCY of wins over the season,
  not to the per-win burn amount.

AGENT RULE:
  Always distinguish:
    Per-match FTP mechanic: UNCHANGED by departure
    Season supply trajectory: ADJUSTED downward by departure
    Plain English: "The burns still happen on wins. There will just
    be fewer wins than projected."
```

---

## Search and social signal classification

```
Your observation about Ronaldo leaving Manchester United and Google Trends
is precisely correct — and it reveals a signal classification problem the
library does not address anywhere.

THE PROBLEM:
  When a star athlete departs, search volume and social mention counts SPIKE.
  Standard interpretation in the library: high volume = positive signal.
  Actual classification for departure context: depends on sentiment type.

DEPARTURE SIGNAL CLASSIFICATION:

POSITIVE VOLUME SIGNALS (apply standard elevated engagement modifier):
  - Tributes and retrospectives from fans
  - Appreciation posts celebrating the player's time at the club
  - Historical goals/moments resurface
  Duration: Typically 1–2 weeks immediately following departure confirmation
  Effect on source token: Brief positive HAS spike (tribute arc)

NEGATIVE VOLUME SIGNALS (apply distress modifier, not engagement modifier):
  - Transfer controversy or fan protest coverage
  - "Betrayal" narrative (Type 2 — rival transfer)
  - Questions about the club's direction or commercial ambitions
  - Player criticism of club management
  Duration: 2–8 weeks (shorter for clean departures, longer for contested ones)
  Effect on source token: Holder exit pressure, negative CDI

MIXED/NEUTRAL VOLUME (apply no modifier — monitor for direction):
  - Future speculations and rumours about the club's replacement targets
  - Tactical analysis of how the club will line up without the player
  - Transfer fee debate (did the club get enough?)
  Duration: Throughout the transfer window period
  Effect on source token: Window uncertainty signal (already in transfer-window-intelligence)

SOCIAL SEARCH VOLUME CLASSIFICATION RULES FOR AGENTS:
  1. Volume spike in first 72h of departure: classify as TRIBUTE (positive)
     unless rival transfer confirmed (then DISTRESS)
  2. Volume spike 3–8 weeks post-departure: classify as VOID_SEARCHING
     (fans looking for news of replacement — NEUTRAL signal)
  3. Volume still elevated at 3+ months with no replacement: STRUCTURAL_DECLINE
     signal — holder attrition risk elevated
  
  Key check: what is the SENTIMENT of the volume, not just the volume?
  Use LunarCrush Galaxy Score direction (rising vs falling) as proxy.
  platform/social-intelligence-connector.md — Galaxy Score section.
```

---

## Replacement commercial quality timeline

```
The commercial void is temporary only if the replacement builds commercial
value. The timeline varies significantly by replacement type.

REPLACEMENT TYPES AND COMMERCIAL REBUILD TIMELINES:

COMMERCIAL UPGRADE (replacement > departing player commercially):
  Example: Club replaces aging star with younger high-AELS rising player
  Timeline: 3–9 months for new player to match or exceed predecessor AELS
  Token effect: Net positive within 12 months; CDI boost from signing narrative
  LTUI projection: POSITIVE — upgrade trend signal

COMMERCIAL EQUIVALENT (similar APS and AELS profile):
  Example: Club-to-club transfer at similar commercial tier
  Timeline: 9–18 months to rebuild same engagement level
  Token effect: Neutral to slightly positive over 18 months
  LTUI projection: STABLE — no reset required

SPORTING UPGRADE / COMMERCIAL DOWNGRADE:
  Example: Club prioritises tactical fit over star power
           (common in elite clubs: positional purchase, not commercial)
  Timeline: 18–36 months if commercial rebuild intentional; indefinite if not
  Token effect: Short-term negative; depends on whether replacement becomes star
  LTUI projection: RESET REQUIRED — commercial rebuild is uncertain

NO DIRECT REPLACEMENT (squad restructure, tactical shift):
  Example: Club moves away from the departed player's role type
  Timeline: Indefinite — token narrative must rebuild around different identity
  Token effect: Structural negative for 12–24+ months
  LTUI projection: MAJOR RESET — lifecycle Phase 4 risk within 24 months

QUANTIFYING REPLACEMENT COMMERCIAL VALUE:
  replacement_commercial_score = (APS × 0.40) + (AELS_estimated × 0.35) + (DTS × 0.25)
  
  Compare to: departing_player_commercial_score (same formula)
  
  If replacement score ≥ departing score × 0.90: EQUIVALENT or better
  If replacement score 0.70–0.89 of departing: PARTIAL RECOVERY (12–24 months to close gap)
  If replacement score < 0.70 of departing:    STRUCTURAL DOWNGRADE (reset required)
```

---

## Cross-sport application

```
FOOTBALL (primary — most detailed coverage)
  Key departure types: all five apply
  FTP connection: PATH_2 win probability impact (above)
  Key metric: ATM departure threshold ≥ 0.60

NBA / BASKETBALL
  Primary departure type: Free agency (Type 1/3 hybrid — player chooses,
  club loses, no replacement fee received)
  Key star departure patterns:
    LeBron Cavaliers departures (2010, 2018): AELS void > 50% — catastrophic
    Durant Warriors departure (2019): AELS void ~35% — major
    KD Brooklyn departure: ~25% — significant
  FTP connection: No active NBA FTP. When NBA tokens launch: same model applies.
  Key metric: Net rating contribution (core/lineup-quality-index.md NBA section)

CRICKET (national team context — Test/ODI/T20 split)
  Primary departure type: Retirement (Dhoni, Kohli eventual)
  Complexity: Same player may retire from one format but continue in another.
    Dhoni retired from Tests → India Test token LTUI reset
    Dhoni continued in T20I → India T20 token LTUI stable
  Key metric: Format-specific AELS (computed separately per format)
  Recovery: Slower than football — national team commercial identity
  is harder to rebuild than club identity

FORMULA 1
  Primary departure type: Team change or retirement
  ATM equivalent: Driver media mentions per race weekend vs team average
  Key departure effect: Constructor token loses the driver's fan following
    and the narrative (Schumacher leaving Ferrari, Hamilton leaving Mercedes)
  Recovery: 2–3 seasons typically to rebuild around successor driver
  Special case: Historic champion retiring = career CDI event (positive narrative)
    but sustained LTUI reset (commercial anchor gone permanently)

RUGBY (national and club)
  Primary departure type: Retirement (McCaw, Carter, O'Driscoll)
  Complexity: National team retirements affect national tokens more than club
  Commercial rebuild: Slower than football; rugby token ecosystems smaller
  Key indicator: World Rugby player ranking + commercial following split

MMA / BOXING (individual sport — departure = promotion exit or retirement)
  Conor McGregor UFC: Promotion's primary commercial anchor
    Extended absences create card quality drops (LQI fight card impact)
    AELS void when main event fighter absent from promoted events
  Retirement: Even harder to model — no squad to absorb the void
  Key metric: Event gate value and PPV buyrate with vs without fighter
```

---

## Departure impact output schema

```json
{
  "departure_brief": {
    "athlete":          "Bukayo Saka",
    "source_club":      "Arsenal",
    "source_token":     "AFC",
    "departure_type":   "TYPE_1_CROSS_LEAGUE",
    "destination":      "Real Madrid",
    "confirmed_at":     "2026-07-01T00:00:00Z"
  },

  "aels_void": {
    "athlete_aels":         82,
    "athlete_aels_share":   0.301,
    "void_magnitude":       "SIGNIFICANT",
    "void_pct":             30.1,
    "phase_a_modifier":     0.699,
    "phase_b_recovery_months": 9,
    "phase_c_timeline_months": 18
  },

  "ltui_impact": {
    "reset_triggered":      true,
    "reset_reason":         "ATM score 0.78 exceeds 0.60 threshold",
    "holder_migration_est": "7.5% of holders may follow athlete to destination",
    "adjusted_ltui_delta":  -18,
    "lifecycle_phase_risk": "Phase 3 stable — monitor for Phase 4 at T+18 months"
  },

  "ftp_impact": {
    "applies":              true,
    "path":                 "PATH_2",
    "lqi_delta":            -0.081,
    "win_prob_adjustment":  -0.012,
    "season_wins_lost_est": 0.5,
    "supply_reduction_lost": "0.12% per season",
    "agent_rule":           "Per-match burn unchanged. Season win frequency reduced."
  },

  "social_signal": {
    "volume_type":          "TRIBUTE_ARC → VOID_SEARCHING",
    "initial_72h":          "POSITIVE (tribute) — do not apply standard ENTER signal",
    "weeks_3_to_8":         "NEUTRAL (replacement speculation)",
    "galaxy_score_watch":   "Declining Galaxy Score at 3+ months = structural decline signal"
  },

  "replacement_assessment": {
    "replacement_found":    false,
    "commercial_score_est": null,
    "timeline":             "Pending recruitment — reassess when replacement confirmed",
    "current_verdict":      "STRUCTURAL_DOWNGRADE risk until replacement confirmed"
  },

  "composite_signal": {
    "source_token_modifier": 0.78,
    "recommended_action":    "WAIT — departure confirmed, void period active",
    "reentry_trigger":       "Replacement confirmed AND Galaxy Score returning to pre-departure baseline"
  },

  "plain_english": "Saka has left Arsenal. This is a significant commercial loss for $AFC — he was responsible for about 30% of the token's social engagement lift. Expect the token to trade lower for the next 6–18 months while a replacement builds their profile. The Fan Token Play supply mechanics don't change per match, but Arsenal are likely to win slightly fewer games this season, which means slightly less supply reduction than expected. The initial social media buzz around the departure is tribute-driven — it doesn't mean the signal is positive. Watch the official Arsenal account for replacement signing news.",

  "sportmind_version": "3.54.0"
}
```

---

## Integration with SportMind patterns and skills

```
FEEDS FROM:
  fan-token/transfer-signal/          — APS (mirror: this skill models the inverse)
  fan-token/athlete-social-lift/      — AELS scores for departing player
  core/lineup-quality-index.md        — LQI delta calculation
  core/athlete-disciplinary-intelligence.md  — Type 5 (disciplinary) departures
  fan-token/gamified-tokenomics-intel — FTP PATH_2 mechanics

FEEDS INTO:
  fan-token/fan-token-lifecycle/      — LTUI reset trigger
  core/sports-trend-intelligence.md   — player migration trend signal
  core/core-result-impact-matrices.md — departure impact baseline (validate/extend)
  agent-prompts/agent-prompts.md      — Prompt 21/22 source token brief
  Pattern 6 (Athlete Commercial Tracker) — monitor replacement commercial build

WHEN TO LOAD:
  ✅ Transfer window open AND source club has active fan token
  ✅ Star player retirement announced (any sport)
  ✅ FTP PATH_2 token AND key ATM player confirms departure
  ✅ Agent receives outgoing TSI spike (fan resistance = departure risk signal)
  ⚠️  Type 5 (disciplinary): load alongside athlete-disciplinary-intelligence.md
  ❌ Rumour only (Tier 4 source) — wait for Tier 1/2 confirmation

PLAIN ENGLISH RULE (Prompt 21/22):
  Never describe high social volume around a departure as a positive signal.
  Always classify: tribute arc (first 72h) vs void searching (3–8 weeks) vs
  structural decline (3+ months still elevated with no recovery).
```

---

*SportMind v3.54 · MIT License · sportmind.dev*
*See also: fan-token/transfer-signal/ (APS — destination perspective)*
*core/lineup-quality-index.md · fan-token/gamified-tokenomics-intelligence/*
*fan-token/fan-token-lifecycle/ · core/sports-trend-intelligence.md*
*core/athlete-disciplinary-intelligence.md (Type 5 departures)*
