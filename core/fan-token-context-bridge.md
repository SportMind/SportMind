---
name: fan-token-context-bridge
description: >
  How every SportMind intelligence layer connects to fan token demand signals,
  supply event probability, and holder behaviour. The bridge between sport
  intelligence and fan token intelligence. Load alongside sport domain files
  for any fan token application.
---

# Fan Token Context Bridge

**How every SportMind layer connects to fan token signals.**
Load this file in any session where sport intelligence must translate to
fan token demand or supply event reasoning.

> This file is a connection layer — it references other files; it does not
> duplicate them. Each layer has its own detailed file.

---

## Sport domain → fan token connection

```
MATCH RESULT SIGNALS:

  WIN:
    demand surge estimate: +15-30%
    duration: 24-72 hours depending on competition tier and match importance
    Path: sport domain match outcome → match result signal → demand surge
    
  LOSS:
    demand decline: −10-20%
    duration: 12-48 hours (decay is faster than surge recovery — asymmetric)
    Path: match outcome → loss signal → accelerated demand decay
    
  DRAW:
    demand movement: minimal ±3-5%
    Path: draw outcome → neutral signal → minor directional movement
    
  MAJOR TROPHY WIN:
    extended demand premium beyond standard WIN signal
    +2-4 weeks of elevated demand above pre-win baseline
    New permanent baseline: +5-10% above pre-trophy baseline
    Path: see core/psychological-intelligence.md post-trophy section
    
  RELEGATION:
    sustained demand collapse — not a temporary WIN/LOSS signal
    Month 1: −25 to −40% from pre-relegation baseline
    Settled: 60-70% of pre-relegation baseline
    Path: see core/financial-sustainability-intelligence.md relegation section

COMPETITION TIER DEMAND MULTIPLIERS:

  Competition              Demand amplifier
  ─────────────────────────────────────────
  UCL / World Cup Final    ×2.0
  UCL / WC Semi-final      ×1.50
  UCL / WC Quarter-final   ×1.25
  Domestic cup final       ×1.20
  Top domestic league      ×1.00 (baseline)
  Lower division match     ×0.75

  Apply: multiplier × base demand signal = amplified demand signal
  Source: macro/tournament-macro.md for full competition tier framework
```

---

## Athlete intelligence → fan token

```
PLAYER AVAILABILITY DEMAND IMPACT:

  Confirmed fit (key player):
    demand premium: ×1.05 (minor; availability is expected not special)
    
  Confirmed absent (key player):
    demand discount: ×0.90 (immediate; absence is unexpected and negative)
    Severity scaling: see tier-a-clubs-framework.md for position weights
    
  Season-ending injury:
    demand reset: −20 to −30%
    Timeline: months-long sustained depression until return
    
  Return from long absence (6+ weeks):
    demand surge: ×1.10 at confirmed return
    Graduated: first match ×1.05 (performance uncertainty); second match ×1.08
    
TRANSFER ACTIVITY DEMAND IMPACT:

  Marquee arrival (+€50M or international quality):
    demand surge: +15-25% over 2-4 weeks
    New baseline: +5-10% permanently above pre-signing baseline
    Source: core/transfer-window-intelligence.md
    
  Marquee departure:
    demand decay: −10-20% over 4-8 weeks
    New baseline: −5-10% below pre-departure baseline
    
  $AFC PATH_2 SPECIFIC:
    Any squad quality change propagates through the PATH_2 chain:
      Arrival → improved WIN probability → larger expected burn event
      Departure → lower WIN probability → smaller expected burn, elevated mint risk
    Apply ×0.60 conversion factor: squad quality change × 0.60 = PATH_2 signal magnitude
    Source: athlete/football/arsenal-afc.md FTP PATH_2 transfer section
```

---

## Macro intelligence → fan token

```
REGULATORY SIGNALS:

  New jurisdiction opened (regulatory clarity enacted):
    US clarity: ×1.10 on US-accessible token demand signals
    GCC framework: ×1.03 sustained for newly regulated GCC markets
    EU MiCA compliance: ×1.05 for EU-accessible tokens
    
  Jurisdiction tightened (restriction, enforcement):
    Regional restriction: ×0.92 for tokens with affected jurisdiction holder base
    Enforcement action: ×0.85 immediate; recovers over 2-4 weeks
    FATF grey listing: ×0.94 sustained for tokens with significant exposure
    
  Source: macro/macro-regulatory-sportfi.md for full jurisdiction framework

CRYPTO MARKET SIGNALS:

  Bitcoin bull market confirmed (sustained uptrend, above 200-day MA):
    ×1.15 applied to all fan token demand signals
    
  Bitcoin bear market confirmed:
    ×0.85 applied to all fan token demand signals
    
  Altcoin season confirmed (alts significantly outperforming BTC, 30-day):
    ×1.20 applied to fan tokens specifically (fan tokens outperform in alt seasons)
    
  Source: macro/macro-crypto-market-cycles.md for cycle phase framework
  Application order: crypto cycle overlay applied FIRST, before all other modifiers
```

---

## Psychological intelligence → fan token

```
WIN STREAK COMMUNITY SIGNAL:

  Win streak amplifies demand beyond pure match result signal:
  
  3+ consecutive wins:
    community_momentum_modifier: ×1.03 sustained between matches
    (additive to each individual match result signal)
    
  5+ consecutive wins:
    community_momentum_modifier: ×1.06 sustained
    
  7+ consecutive wins:
    ceiling: ×1.08 sustained
    
LOSS STREAK COMMUNITY SIGNAL:

  Loss streak accelerates demand decay beyond pure match result signal:
  
  3+ consecutive losses:
    community_fragility_modifier: ×1.30 on standard loss impact
    (loss decay is 30% larger than standard)
    
  5+ consecutive losses:
    community_fragility_modifier: ×1.50
    
  7+ consecutive losses:
    community_fragility_modifier: ×1.70
    
TROPHY WIN PSYCHOLOGICAL PREMIUM:

  Extended demand premium beyond standard match WIN signal:
  Peak: +15-25% in first 48h (above standard WIN surge)
  Sustained: +8-12% for weeks 2-4
  New baseline: +5-10% permanently above pre-trophy baseline
  Source: core/psychological-intelligence.md post-trophy section
```

---

## Governance → fan token

```
GOVERNANCE ENGAGEMENT SIGNALS:

  Active governance vote announced:
    engagement_signal: ×1.05 demand during voting window (48-72h)
    
  Governance result announced (any outcome):
    post_vote_signal: ×1.02 for 24h normalisation period
    
  High voter turnout (>20% of holders):
    sustained_community_health: ×1.03 for 2 weeks post-vote
    
  Failed quorum:
    community_disengagement: ×0.96 for 1 week
    
  Source: fan-token/governance-intelligence.md for full governance framework
```

---

## Seasonal patterns → fan token

```
ANNUAL DEMAND CYCLE CONNECTOR:

  Summer window (June-August):         ×1.20 baseline amplifier
  Winter window (January):             ×1.10 baseline amplifier
  End of season (April-May):           ×1.10-1.15 (title/relegation narrative)
  Dead period (June-July off-season):  ×0.85 baseline floor
  
  Match day:                           ×1.08 pre-match demand
  Day after WIN:                       ×1.05 sustained (48h)
  Day after LOSS:                      ×0.92 decay begins immediately
  
  Full framework: core/seasonal-intelligence.md

COMPETITION CALENDAR IMPACT:

  Fixture congestion third match:      ×0.94 squad quality signal
  International break (first match back): ×0.97 reassembly signal
  Early cup exit:                      ×1.03 league focus signal (season-long)
```

---

## Venue and weather → fan token

```
INDIRECT CONNECTION ONLY:

  Venue and weather primarily affect match outcome probability, which then
  affects fan token demand through the match result connection above.
  
  DIRECT FAN TOKEN CONNECTION (limited):
  
  New stadium opening: ×1.20 spike (48-72h) → ×1.08 first season
    (see core/crowd-intelligence.md new stadium section)
    
  Stadium naming rights (fan token ecosystem connection):
    naming_rights_modifier: ×1.05 sustained for contract duration
    
  These are structural demand signals, not match-day modifiers.
  Do not apply venue modifiers directly to match-day demand — route through
  the match outcome probability chain first.
```

---

## FTP PATH_2 connection summary

```
FOR $AFC ONLY — SUPPLY EVENT CHAIN:

  Sport domain signal → WIN probability assessment
  WIN probability → pre-liquidation burn estimate (supply ÷ 400 × multiplier)
  Match result → actual supply event (BURN on WIN | MINT on LOSS | NONE on DRAW)
  
  Every layer that affects WIN probability also affects PATH_2 expected magnitude:
    Athlete absence → lower WIN probability → smaller expected burn
    Home advantage → higher WIN probability → larger expected burn
    Psychological momentum → WIN probability adjustment → supply event adjustment
    
  Convert: [WIN probability change in %] × 0.60 = [PATH_2 signal magnitude]
  
  All other tokens: demand-only signal. No supply chain applies.
  Check: fan-token/ftp-path2.md before assuming PATH_2 status for any token.
```

---

## Compatibility

**Full signal chain:**  `core/agent-reasoning-chains.md`
**Loading order:**      `core/agent-onboarding.md`
**Confidence check:**   `core/signal-confidence-framework.md`
**Seasonal detail:**    `core/seasonal-intelligence.md`
**Governance detail:**  `fan-token/governance-intelligence.md`
**PATH_2 mechanics:**   `fan-token/ftp-path2.md`

---

*SportMind v3.97.38 · MIT License · sportmind.dev*
*This file bridges sport intelligence to fan token signals — load alongside sport domain files*
