---
name: sports-trend-intelligence
description: >
  Framework for detecting, classifying, and applying the commercial and
  competitive impact of sports industry trends across SportMind's five
  intelligence layers. Answers: what is trending, why is it trending,
  what phase is the trend in, and how does it modify Layer 1–5 signals?
  Covers three trend categories: sport-level commercial trajectory (rising,
  maturing, declining), suite trends (Chiliz/RWA/fan token industry
  shifts), and competitive structure trends (new leagues, format changes,
  player migration patterns). Produces a trend_modifier per layer and a
  trend_context block for the plain-English brief. Use when: evaluating
  a sport whose commercial trajectory has changed materially in the last
  12–24 months, or when a major industry-level shift is underway that
  affects multiple sports simultaneously.
---

# Sports Trend Intelligence — SportMind

**What is trending, why it is trending, what phase it is in, and how it
changes what the five layers should say.**

SportMind's five layers are structured intelligence about how sports work,
what athletes are doing, what fan tokens signal, what markets show, and
what macro forces are active. All of that intelligence is grounded in
calibrated, verified data.

What it does not automatically capture is **trajectory** — the direction
a sport or suite is moving, and whether the current signal should be
amplified or dampened based on where things are heading. A sport in rapid
commercial ascent (women's football, Saudi Pro League in 2022–2025) has
different signal dynamics than a sport in plateau or decline. A fan token
ecosystem in its first major bull cycle has different behaviour than one
in its third.

This skill provides the trend context layer that sits above the five
layers and modifies how agents should weight them.

---

## The three trend categories

```
CATEGORY 1 — SPORT-LEVEL COMMERCIAL TRAJECTORY
  Is this sport's commercial ecosystem growing, stable, or contracting?
  Affects: Layer 4 (market), Layer 3 (fan token commercial), Layer 1 (signal weights)
  
  Examples:
    Women's football:   rapid growth phase (2022–2026+)
    Saudi Pro League:   rapid growth phase (2022–2026, athlete migration driving it)
    Pickleball:         emergence phase (US-centric, token ecosystem not yet viable)
    Horse racing:       contraction phase (declining youth audience, streaming gaps)
    Traditional esports leagues: maturation/contraction (viewership plateau post-COVID peak)

CATEGORY 2 — SUITE TRENDS
  What is shifting in the Chiliz/fan token/RWA suite specifically?
  Affects: Layer 3 (fan token commercial), Layer 5 (macro), Layer 4 (market tiers)
  
  Examples:
    Fan Token™ Play Path 2 ($AFC):     Phase rollout trend — watching for club expansion
    RWA tokenisation:                  near-term arrival trend (2026-2027)
    Prediction market growth (Azuro):  volume growth trend (signal confidence improvement)
    Regulatory clarity (MiCA):         structural positive trend for EU tokens
    US regulatory uncertainty:         structural risk trend (affects all non-EU tokens)

CATEGORY 3 — COMPETITIVE STRUCTURE TRENDS
  How is the competitive landscape of a sport changing?
  Affects: Layer 1 (sport domain), Layer 2 (athlete intelligence), Layer 4 (market)
  
  Examples:
    Saudi Pro League player migration:  elite talent redistribution trend
    UEFA expansion (36-team UCL):       fixture inflation trend (dilutes NCSI per match)
    Women's Champions League growth:    competition quality rising trend
    Cricket T20 league proliferation:   fixture congestion + player availability trend
    NBA expansion (Las Vegas, Seattle): new market commercial trend
    F1 calendar expansion (24 races):   congestion + fatigue trend for drivers
```

---

## Trend phase classification

```
Every trend has a phase. The phase determines how aggressively to modify signals.

PHASE 1 — EMERGENCE (0–18 months from trigger event)
  Definition: Trend is newly active; uncertainty is high; direction is clear
              but magnitude and duration are unknown
  Characteristics:
    - Rapid movement in one direction
    - High media coverage, often speculative
    - Commercial data lagging the actual change
  Signal impact: Apply trend modifier cautiously (×0.50 of full modifier)
  Examples: Saudi league first elite signings (mid-2023), FTP Path 2 launch (Apr 2026)

PHASE 2 — ACCELERATION (18 months–3 years)
  Definition: Trend confirmed and strengthening; commercial ecosystem adapting
  Characteristics:
    - Multiple confirming data points across independent sources
    - Commercial deals being restructured to reflect the new reality
    - Other actors entering the space (competitors, sponsors, broadcasters)
  Signal impact: Apply full trend modifier
  Examples: Women's football commercial growth (2023–2026), MiCA implementation

PHASE 3 — MATURATION (3–6 years)
  Definition: Trend becoming the new normal; growth rate slowing
  Characteristics:
    - Commercial tier has reset to reflect the trend
    - Media narrative has moved on from the trend itself
    - Signal impact now baked into baseline (remove trend modifier)
  Signal impact: Reduce to ×0.30 of full modifier; prepare to sunset
  Examples: UCL streaming shift (streaming > broadcast), social media as primary fan channel

PHASE 4 — REVERSAL OR PLATEAU
  Definition: Trend has stopped or reversed; new baseline is established
  Characteristics:
    - Growth rate has returned to historical norm or below
    - Commercial tier recalibrated; trend modifier should be removed
  Signal impact: Remove trend modifier entirely; update market file baseline
  Examples: Traditional esports league viewership (peaked 2020-2021), post-COVID plateau
```

---

## Active trends inventory (April 2026)

These are the trends SportMind agents should be aware of right now.
Update this inventory when new trends are confirmed or phases change.

```
TIER A — HIGH IMPACT (modify signals materially)

T-01: Women's football commercial ascent [PHASE 2]
  Trigger: 2023 Women's World Cup viewership records
  What: Broadcasting deals, sponsorships, and club valuations rising rapidly
  Why: Demographic shift — Gen Z engagement in women's sport outpacing men's
  Phase confirmation: UEFA Women's CL deal value grew 3× between 2022-2025
  Layer impact:
    L4 (market): raise commercial tier for women's football tokens from Tier 3 → Tier 2
    L3 (fan token): AELS metrics for women's athletes need upward baseline adjustment
    L1 (sport domain): derbies and international fixtures carrying higher NCSI weight
  Trend modifier: L4 ×1.20 | L3 ×1.15 | L1 NCSI ×1.10 (high-stakes fixtures)
  Source: UEFA.com revenue reports, Deloitte Annual Review of Football Finance
  Review: Quarterly — if growth rate confirmed above 20% YoY, move to full Phase 2 max

T-02: Saudi Pro League elite player migration [PHASE 2]
  Trigger: Ronaldo Al-Nassr signing (January 2023)
  What: Serial signing of top-40 global players by Saudi PIF-backed clubs
  Why: Sovereign wealth fund investment; sportswashing strategy; player financial peak
  Phase confirmation: 8 of top-50 Transfermarkt-valued players now in Saudi league
  Layer impact:
    L2 (athlete): APS recalibration needed — Saudi signings have lower AELS portability
                  because Saudi league has smaller global social audience than EPL/LaLiga
    L4 (market): Saudi Pro League token readiness upgrades from Tier 3 → Tier 2
    L1 (sport domain): fixture importance signals for Saudi league should be adjusted upward
  Trend modifier: L4 ×1.25 (Saudi tokens) | L2 APS reduction for Saudi-bound athletes ×0.85
  Source: Transfermarkt, Saudi Pro League official, Reuters sports desk
  Review: Semi-annual — if marquee signings continue, Phase 3 by end 2027

T-03: Fan Token Play Path 2 suite expansion [PHASE 1]
  Trigger: $AFC PATH_2 confirmed 07 April 2026 (first public trial)
  What: Performance-linked supply mechanics rolling out to more tokens
  Why: Chiliz Vision 2030 roadmap — FTP is the core utility differentiator
  Phase confirmation: Single confirmed token ($AFC). PATH_1 pending.
  Layer impact:
    L3 (fan token): gamified_tokenomics_intelligence mandatory for any FTP-active token
    L5 (macro): CHZ virtuous cycle amplifier active for FTP events
  Trend modifier: Apply at ×0.50 (Phase 1 caution) — expand when 3+ tokens confirmed
  Source: platform/chiliz-chain-address-intelligence.md, Chiliz official announcements
  Review: Monthly until PATH_1 confirmed

T-04: MiCA regulatory clarity for EU fan tokens [PHASE 2]
  Trigger: MiCA implementation 2024
  What: Clear legal framework for utility tokens in EU — reduces regulatory risk
  Why: EU covers majority of Chiliz's top club tokens (Barcelona, PSG, Juventus, etc.)
  Phase confirmation: First MiCA-compliant token structures announced by major clubs
  Layer impact:
    L5 (macro): regulatory_risk_modifier improves for EU tokens specifically
    L4 (market): Tier 1 EU-club tokens gain stability modifier
    L3 (fan token): governance votes now have clearer legal standing in EU
  Trend modifier: L5 EU tokens ×1.10 (risk reduction) | Non-EU tokens: no change
  Source: macro/macro-regulatory-sportfi.md, EUR-Lex MiCA documentation
  Review: Annual — monitor ECB guidance updates

TIER B — MODERATE IMPACT (directional context only)

T-05: RWA sports tokenisation approaching [PHASE 1]
  Trend: Stadium naming rights, media rights, player performance bonds near-term (2026-2027)
  Layer impact: L3 signal interpretation — look for early RWA launch announcements
  Trend modifier: ×1.05 for tokens where parent club has announced RWA intent
  Source: fan-token/rwa-sportfi-intelligence/

T-06: UCL format expansion (36-team group phase) [PHASE 2]
  Trend: More matches per club, diluted match importance at early stages
  Layer impact: L1 NCSI — UCL group stage matches carry less weight than before
  Trend modifier: UCL group stage NCSI ×0.88 (was higher in 32-team format)
  Source: UEFA.com official format documentation

T-07: T20 cricket league proliferation [PHASE 2]
  Trend: ILT20, SA20, MLC, CPL etc. creating fixture congestion
  Layer impact: L2 athlete availability — more rest decisions, more rotation
  Trend modifier: L2 fast bowler availability ×0.92 (elevated load risk across leagues)
  Source: ESPNcricinfo league calendar, ICC fixture schedule

T-08: Prediction market volume growth [PHASE 2]
  Trend: Azuro, Polymarket sports volume increasing — improving divergence signal quality
  Layer impact: prediction-market-intelligence.md — lower minimum TVL threshold for use
  Trend modifier: Reduce TVL minimum from $10k to $5k for established sports
  Source: Azuro.org, Polymarket volume stats

TIER C — WATCH LIST (emerging, not yet modifier-worthy)

T-09: Pickleball global expansion
  Status: US Phase 1; international Phase 0. No token viability yet.
  Watch for: International federation formation, broadcast deal announcement
  
T-10: NBA global expansion (Las Vegas, Seattle franchises)
  Status: Phase 1. New markets creating new fan token opportunities.
  Watch for: Official franchise announcements, Chiliz NBA partnership update

T-11: Women's cricket commercial growth
  Status: Phase 1. ICC Women's events growing faster than men's in some markets.
  Watch for: Broadcast deal values, standalone women's league valuations
```

---

## How to apply trend modifiers to the five layers

```
STEP 1 — IDENTIFY ACTIVE TRENDS for this sport/token
  Check the active trends inventory above.
  Filter to: trends that affect this sport AND are in Phase 1 or Phase 2.
  Discard Phase 3+ trends (already baked into baseline).

STEP 2 — DETERMINE PHASE CONFIDENCE
  Phase 1 (emergence): Apply trend modifier × 0.50
  Phase 2 (acceleration): Apply trend modifier × 1.00
  Phase 3 (maturation): Apply trend modifier × 0.30 or remove
  
STEP 3 — APPLY TO RELEVANT LAYERS
  Each trend specifies which layers it affects and by how much.
  Layer modifiers are cumulative but capped:
    Maximum trend boost per layer: ×1.30
    Maximum trend reduction per layer: ×0.75
    Never let trend modifiers alone flip a signal direction.

STEP 4 — ADD TREND CONTEXT TO BRIEF
  For Prompt 21/22 (fan-facing and build-up): include a "TREND CONTEXT" line
  explaining the active trend in plain English.
  
  Example:
  "Context: Women's football is in a significant commercial growth phase.
  This means the commercial signals for this token should be read as
  somewhat stronger than the underlying metrics alone would suggest —
  the market is catching up to where the trend is heading."

STEP 5 — REVIEW TRIGGER
  Agents should re-check trend phases when:
    - A new major event in the trend's category occurs
    - Source data shows phase transition signals
    - Quarterly calendar trigger (set review dates)
```

---

## Sport-level opponent quality weighting — GFR integration

```
Global Football Rankings (globalfootballrankings.com) provides Elo-based
team and league strength ratings (0–100 scale, updated weekly).

HOW THIS CONNECTS TO HISTORICAL INTELLIGENCE FRAMEWORK:
  core/historical-intelligence-framework.md calculates H2H_RELEVANCE using
  base_weight, recency_factor, personnel_continuity, and context_factor.
  The base_weight currently only considers number of meetings.
  
  ENHANCEMENT: Opponent quality multiplier on H2H wins.
  
  A team with 7W 1D 2L vs GFR-rated opponent 75 has a stronger H2H signal
  than the same record vs GFR-rated opponent 45. The wins carry more weight.
  
  OPPONENT_QUALITY_MULTIPLIER:
    Opponent GFR rating 80+:   H2H win weight ×1.25 (beating elite teams)
    Opponent GFR rating 65-79: H2H win weight ×1.10 (beating good teams)
    Opponent GFR rating 50-64: H2H win weight ×1.00 (baseline — average teams)
    Opponent GFR rating 35-49: H2H win weight ×0.90 (beating weaker teams)
    Opponent GFR rating <35:   H2H win weight ×0.75 (limited predictive value)
  
  APPLICATION in historical-intelligence-framework.md:
    quality_adjusted_h2h = raw_h2h_win_rate × opponent_quality_multiplier
    Then apply to existing H2H_RELEVANCE formula as normal.
  
  DATA SOURCE:
    Live: https://globalfootballrankings.com/rankings/teams
    Weekly update. Football only.
    For other sports: use FIFA World Rankings (national), Elo ratings
    (clubelo.com for club football), ATP/WTA (tennis), UFC rankings (MMA).

  SCOPE: Football primarily. Equivalent rating sources by sport:
    Club football:      clubelo.com (Elo), GFR (True Elo)
    International:      FIFA World Rankings (fifa.com/ranking)
    Tennis:             ATP/WTA official rankings
    MMA:                UFC official rankings + Tapology
    Basketball (NBA):   SRS (Simple Rating System) via basketball-reference.com
    Cricket (national): ICC rankings (icc-cricket.com)
    F1 (driver):        F1 season standings (FIA)
```

---

## Trend detection signals — what to monitor

```
SIGNAL TYPE 1 — BROADCAST DEAL CHANGES
  Why it matters: Broadcast revenue is the primary commercial signal for Layer 4.
                  A new deal >30% above previous = tier upgrade signal.
  How to detect:  The Athletic, SportsPro Media, SportBusiness.com
  Trigger:        New deal announced → check magnitude → update tier if warranted

SIGNAL TYPE 2 — GOVERNING BODY DIGITAL ANNOUNCEMENTS
  Why it matters: Official digital/token partnerships move sports from Tier 3 → 2 or 2 → 1
  How to detect:  Official governing body press releases, SportsPro, SportBusiness
  Trigger:        Partnership announcement → classify tier upgrade level

SIGNAL TYPE 3 — VIEWERSHIP AND ATTENDANCE TRAJECTORY
  Why it matters: Fan base size is the leading indicator for commercial tier
  How to detect:  Sportcal, SportsPro, Nielsen Sports annual reports
  Trigger:        YoY growth >15% for 2+ years = rising trend; decline >10% = contraction

SIGNAL TYPE 4 — MARQUEE PLAYER / TEAM MIGRATION
  Why it matters: Elite player arrival in a league changes its commercial tier rapidly
                  (Saudi Pro League is the definitive example)
  How to detect:  Transfermarkt, Fabrizio Romano, league official announcements
  Trigger:        Top-10 global player moves to non-traditional market → Phase 1 trend

SIGNAL TYPE 5 — CHILIZ ECOSYSTEM ANNOUNCEMENTS
  Why it matters: New token launches, FTP expansion, RWA pilots directly affect Layer 3
  How to detect:  Chiliz.com/blog, Socios.com announcements, @ChilizOfficial
  Trigger:        New token confirmed → add to registry; FTP expansion → update modifier

SIGNAL TYPE 6 — REGULATORY DEVELOPMENTS
  Why it matters: MiCA, SEC, CFTC, FCA decisions structurally affect token viability
  How to detect:  EUR-Lex (EU), SEC.gov (US), FCA.org.uk (UK), macro/macro-regulatory-sportfi.md
  Trigger:        Regulation passed → update macro_regulatory_modifier per region
```

---

## Trend intelligence output schema

```json
{
  "trend_assessment": {
    "sport":          "football",
    "token":          "AFC",
    "assessed_at":    "2026-04-11T00:00:00Z"
  },

  "active_trends": [
    {
      "trend_id":     "T-03",
      "name":         "Fan Token Play Path 2 suite expansion",
      "phase":        "PHASE_1",
      "phase_confidence": 0.50,
      "affected_layers": ["L3", "L5"],
      "layer_modifiers": {
        "L3": 1.05,
        "L5": 1.03
      },
      "plain_english": "Arsenal are the first club on Fan Token Play. The supply mechanics are new and the suite is still proving itself — watch for more clubs joining before treating this as a confirmed structural feature."
    }
  ],

  "composite_trend_modifier": 1.08,
  "trend_context_for_brief": "Two active trends affect $AFC: FTP Path 2 is in early rollout phase (Phase 1, modest positive) and women's football growth is not directly relevant to this token. Net trend signal: mild positive — FTP mechanics are live and proving.",

  "watch_list": [
    "PATH_1 rollout timeline — watch Chiliz official announcements",
    "Next club to confirm PATH_2 — will validate the trend as structural"
  ],

  "skill_connections": [
    "fan-token/gamified-tokenomics-intelligence/",
    "macro/macro-crypto-market-cycles.md",
    "macro/macro-regulatory-sportfi.md",
    "market/market-overview.md (tier upgrade signals)",
    "core/historical-intelligence-framework.md (opponent quality)"
  ]
}
```

---

## Integration with SportMind patterns and prompts

```
PATTERN 2 (Pre-Match Chain):
  Load this skill at T-48h alongside sport domain skill.
  Apply trend modifiers to Layer 4 and Layer 3 inputs.
  Include trend_context_for_brief in Prompt 21/22 output.

PATTERN 1 (Portfolio Monitor):
  Check active_trends for each token in portfolio every 4h cycle.
  Alert if trend phase changes (Phase 1 → Phase 2 is a position review trigger).

PATTERN 11 (Post-Match Analysis):
  After unexpected results: check if an active trend was not properly weighted.
  Unexpected loss in rising sport = revisit trend modifier calibration.

PROMPT 21 (Fan-Facing Brief):
  Include plain_english trend note when any Tier A trend is active.
  Example: "Context: Women's football is growing fast commercially —
  this token's signals should be read as slightly more positive than
  the underlying numbers suggest."

PROMPT 22 (Build-Up Agent):
  Include trend_context in the CONTEXT section (first section of build-up).
  Frame competition significance in light of the sport's current trend phase.
```

---

*SportMind v3.53 · MIT License · sportmind.dev*
*See also: macro/macro-overview.md · market/market-overview.md (tier upgrade signals)*
*core/historical-intelligence-framework.md · core/core-narrative-momentum.md*
*fan-token/rwa-sportfi-intelligence/ · macro/macro-regulatory-sportfi.md*

### Trend 8b — Women's sports commercial maturity (EMERGING, 2025–2028)

```
SIGNAL: Women's sports has crossed the commercial viability threshold.
  Revenue: $2.4 billion projected 2025 (CAGR 50% since 2022)
  Viewership: nearly tripled since 2020 (>3% of all live sports audiences)
  Ad spend: +139% year-over-year to $244 million
  Sponsorship: growing 12% p.a. — nearly 50% faster than men's leagues

FAN TOKEN IMPLICATION:
  Women's sports fan tokens are approaching commercial viability
  Key threshold: sustained viewership + sponsorship = token programme viable
  WNBA: most advanced US women's league for potential fan token programme
  Women's Super League (WSL): European football women's tier — watch for Chiliz
  
AGENT SIGNAL:
  First women's league fan token launch = ×1.50 CDI modifier at launch
  (higher than men's league equivalent due to novelty premium)
  
STATUS: No women's sport fan tokens confirmed on Chiliz as of April 2026
MONITOR: WNBA expansion, WSL commercial partnerships

Source: Houlihan Lokey Sports Market Update (Fall 2025);
Apollo Sports Capital white paper (December 2025)
```

