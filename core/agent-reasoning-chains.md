---
name: agent-reasoning-chains
description: >
  Complete end-to-end reasoning chains for the most common SportMind scenarios.
  Shows explicitly how intelligence flows through layers to produce final output.
  Agents and developers follow these chains exactly. Load alongside
  core/agent-onboarding.md and core/signal-confidence-framework.md.
---

# Agent Reasoning Chains

**Complete end-to-end chains for the most common SportMind scenarios.**
Follow each chain step-by-step. No interpretation required.

> Load after: core/agent-onboarding.md (loading order)
> Load alongside: core/signal-confidence-framework.md (confidence assessment)

---

## Chain 1 — Key player absence signal

```
TRIGGER: Key player confirmed absent for upcoming match.

STEP 1 — SIGNAL RECEIVED AND CLASSIFIED:
  Confirm: is this a named player absence from a primary source?
    Official club confirmation (injury or unavailability) → proceed
    Rumour or unconfirmed → do NOT apply modifier; flag as UNCONFIRMED
  Classify: what position? What club? Is this club $AFC (PATH_2 active)?

STEP 2 — ATHLETE INTELLIGENCE LAYER:
  Load: athlete/football/[club].md or equivalent sport file
  Load: athlete/football/tier-a-clubs-framework.md (universal modifiers)
  Identify: position modifier weight for the absent player's position
  Apply: absence modifier to adjusted score
    Example: primary striker absent → ×0.93 on adjusted score
    Example: GK absent → ×0.90 on adjusted score
  Check: is squad depth discount applicable? (see club-specific file)

STEP 3 — SYSTEM REASONING:
  Load: core/coaching-intelligence.md
  Identify: manager tactical system identity (possession / counter / press / reactive)
  Identify: is the absent position system-critical for this manager's identity?
  Apply: system disruption modifier if applicable
    Possession manager + creative midfield absent → compound modifier ×0.95 on top
    Counter-attacking manager + striker absent → compound modifier ×0.95 on top
    High-press manager + pressing midfielder absent → ×0.92 pressing system degradation
  If manager has been in post 4+ seasons: apply ×0.15 reduction to disruption impact

STEP 4 — MATCH OUTCOME RECALCULATION:
  Multiply all modifiers together (never add):
    base_adjusted_score × athlete_modifier × system_modifier = revised_adjusted_score
  If revised_adjusted_score drops below 45 (from above 55): flag DIRECTION_SHIFT_POSSIBLE
  If revised_adjusted_score enters 45-55 range: flag HOLD_RECOMMENDED

STEP 5 — FTP PATH_2 CONTEXT ($AFC ONLY):
  If club is $AFC: load fan-token/ftp-path2.md and athlete/football/arsenal-afc.md
  Lower WIN probability → proportionally lower expected burn pool
  Pre-liquidation pool: circulating supply ÷ 400 (unchanged)
  Revised WIN probability × multiplier range (1.4× to 2.0×) = revised burn estimate
  Communicate: how the absence shifts the supply event probability distribution
  If HOLD_RECOMMENDED: PATH_2 pre-liquidation signal also HOLD — do not size

STEP 6 — FAN TOKEN DEMAND SIGNAL:
  Confirmed public absence → immediate demand decay begins
  Apply: star player absence decay (from tier-a-clubs-framework.md)
    High-profile player: −10-15% demand over 24-48h
    Standard key player: −5-10% demand over 24-48h
  Load: core/broadcast-media-intelligence.md — is media narrative amplifying the absence?
    Media concentration on the absent player → apply concentration_risk flag

STEP 7 — OUTPUT (structured):
  direction: [HOME/AWAY/DRAW]
  adjusted_score: [revised number]
  modifiers_applied: { athlete: [×], system: [×], compound: [×] }
  ftp_path2: { eligible: true/false, revised_win_prob: [%], revised_burn_estimate: [range] }
  demand_signal: { direction: negative, magnitude: [%], duration_hours: [24-48] }
  flags: { lineup_unconfirmed: false, hold_recommended: true/false }
  confidence_level: [check signal-confidence-framework.md]
```

---

## Chain 2 — Regulatory signal

```
TRIGGER: New regulatory development in a key fan token jurisdiction.

STEP 1 — SIGNAL RECEIVED:
  Source tier check: what is the source?
    Tier 1 (official government/regulator): proceed immediately
    Tier 2 (credible journalist): proceed with TIER_2_CONFIDENCE flag
    Tier 3 (community/social): do NOT apply; flag for monitoring only

STEP 2 — LIBRARY RULE TEST (mandatory):
  Ask: will this intelligence still be true and useful in six months?
    Enacted law / confirmed regulatory framework → ENDURING → proceed to Step 3
    Scheduled hearing date / process status → EXPIRING → briefing body only, stop here
    Rumoured regulatory change → EXPIRING → do not apply modifier, stop here

STEP 3 — MACRO INTELLIGENCE LAYER:
  Load: macro/macro-regulatory-sportfi.md
  Identify: which jurisdiction does this signal affect?
  Identify: which active fan tokens have significant holder bases in that jurisdiction?
  Classify signal direction:
    CLARITY / POSITIVE (framework enacted, market opened):
      apply: regulatory_clarity_modifier = ×1.10 for US market signals
      apply: ×1.05 for APAC positive clarity signals
      apply: ×1.03 for GCC framework signals (already generally positive)
    TIGHTENING / NEGATIVE (restriction, enforcement, grey listing):
      apply: regional_risk_modifier = ×0.92 for affected jurisdiction tokens
      apply: ×0.85 for enforcement action signals (immediate and acute)
      apply: ×0.94 for grey list / enhanced monitoring signals (FATF)

STEP 4 — FAN TOKEN DEMAND IMPACT:
  Map signal to affected tokens:
    Which tokens have primary or significant holder bases in this jurisdiction?
    US clarity signal: all tokens with US-accessible trading → ×1.10
    GCC tightening: tokens with GCC primary holder base → ×0.92
  Load: fan-token/fan-token-lifecycle/ for demand baseline reference
  Apply modifier for confirmed duration:
    Enacted regulatory framework: sustained modifier (no duration cap)
    Enforcement action: ×0.85 immediate; recovers over 2-4 weeks

STEP 5 — PORTFOLIO CORRELATION CHECK:
  If signal affects 3+ tokens simultaneously:
    Load: fan-token/portfolio-intelligence.md
    Flag: cross_token_correlation_elevated = true
    Apply: portfolio concentration modifier if 5+ tokens affected in same direction

STEP 6 — OUTPUT:
  macro_modifier: [× value]
  affected_tokens: [list]
  demand_signal: { direction: [positive/negative], magnitude: [%], duration: [sustained/weeks] }
  library_rule: [ENDURING/EXPIRING]
  source_tier: [1/2/3]
  flags: { portfolio_correlation_elevated: true/false }
```

---

## Chain 3 — FTP PATH_2 pre-match chain

```
TRIGGER: Upcoming match involving an FTP PATH_2 confirmed token ($AFC).

STEP 1 — CONFIRM TOKEN ELIGIBILITY:
  Check: fan-token/ftp-path2.md for confirmed PATH_2 tokens
  Currently confirmed: $AFC (Arsenal FC) only
  If token is NOT confirmed: demand-only signal → skip to Chain 4
  Document: path2_eligible = true

STEP 2 — PRE-LIQUIDATION CALCULATION:
  Obtain: current circulating supply from fantokens.com or chiliscan.com
  Calculate: pre_liquidation_pool = circulating_supply ÷ 400
  Timing: pre-liquidation occurs T-12h to T-2h before kickoff
  Monitor: chiliscan.com and fantokens.com/fan-token-play from T-12h
  Note the pool size — this is your supply event magnitude denominator

STEP 3 — WIN PROBABILITY ASSESSMENT:
  Load all applicable sport domain and modifier files:
    sports/football/sport-domain-football.md (or competition-specific)
    athlete/football/arsenal-afc.md (Arsenal-specific modifiers)
    core/venue-intelligence.md (home/away/neutral)
    core/weather-intelligence.md (if conditions are material)
    core/referee-intelligence.md (if referee confirmed)
    core/psychological-intelligence.md (if relevant pattern exists)
    macro/macro-regulatory-sportfi.md (macro override check)
  Apply all active modifiers → calculate revised WIN probability
  Check: is macro_override_active? If yes → HOLD entire chain

STEP 4 — SUPPLY EVENT MAGNITUDE ESTIMATE:
  WIN scenario:
    burn_pool = pre_liquidation_pool × multiplier
    Multiplier range: 1.4× (conservative) to 2.0× (strong demand)
    April 2026 reference calibration: 100k pre-liq → 159,025 burned (1.59×)
    Use 1.50× as the central estimate; range 1.40×–2.0×
  LOSS scenario:
    mint_estimate = approximately equal to pre-liquidation pool (to be confirmed
    against latest $AFC mint ratio; load ftp-path2.md for current mechanics)
  DRAW scenario: no supply change

STEP 5 — PROBABILITY-WEIGHTED NET SUPPLY CHANGE:
  net_supply_change =
    (win_probability × burn_estimate × −1) +
    (loss_probability × mint_estimate × +1) +
    (draw_probability × 0)
  Negative net = deflationary signal (net burns expected)
  Positive net = inflationary signal (net mints expected)
  Express as a range (low/central/high) based on multiplier uncertainty

STEP 6 — OUTPUT:
  path2_eligible: true
  pre_liquidation_pool: [number]
  win_probability: [%]
  burn_estimate_central: [number]
  burn_estimate_range: [low to high]
  net_supply_change_central: [deflationary/inflationary, magnitude]
  monitoring_window: T-12h to T-2h before kickoff
  flags: { lineup_unconfirmed: [bool], macro_override_active: [bool] }
```

---

## Chain 4 — Demand-only token chain

```
TRIGGER: Upcoming match for a demand-only fan token (no confirmed PATH_2).

STEP 1 — CONFIRM DEMAND-ONLY STATUS:
  Check: fan-token/ftp-path2.md — confirm no PATH_2 mechanic
  All modifiers in this chain affect demand signal only.
  No supply mechanics to calculate or communicate.
  Document: demand_only = true

STEP 2 — MATCH OUTCOME PROBABILITY:
  Apply full SportMind modifier stack as appropriate:
    Sport domain base signal → adjusted score and direction
    Athlete modifiers → from club-specific athlete file
    Venue modifier → from core/venue-intelligence.md
    Weather modifier → from core/weather-intelligence.md (if material)
    Referee modifier → from core/referee-intelligence.md (if confirmed and material)
  Produce: direction, adjusted_score, SMS

STEP 3 — DEMAND SIGNAL MAPPING:
  Map expected outcome to demand signal using fan-token-context-bridge.md:
  
    Projected WIN:
      demand surge estimate: +15-30% sustained 24-72 hours
      Scale with match importance amplifier (see Step 4)
    Projected LOSS:
      demand decline: −10-20% decay 12-48 hours
      (Decay faster than surge recovery — asymmetric)
    Projected DRAW:
      demand movement: ±3-5% (minimal)
      
  Weight these scenarios by their probability from Step 2.
  Net expected demand signal = probability-weighted combination

STEP 4 — MATCH IMPORTANCE AMPLIFIER:
  Load: macro/tournament-macro.md for competition tier
  Apply amplifier to demand estimates:
    UCL/WC Final: ×2.0 amplifier on all demand signal magnitudes
    UCL/WC Semi-final: ×1.50
    UCL/WC Quarter-final: ×1.25
    Domestic cup final: ×1.20
    Top league match: ×1.00 (no amplifier)
    Lower division: ×0.75

STEP 5 — OUTPUT:
  demand_only: true
  direction: [HOME/AWAY/DRAW]
  adjusted_score: [0-100]
  demand_signal: {
    win_scenario: { surge: [%], duration_hours: [24-72] },
    loss_scenario: { decay: [%], duration_hours: [12-48] },
    draw_scenario: { movement: [%] },
    probability_weighted_net: [% direction],
    importance_amplifier: [×]
  }
  confidence_level: [check signal-confidence-framework.md]
```

---

## Chain 5 — Weather and environmental

```
TRIGGER: Material weather conditions confirmed for upcoming match.

STEP 1 — CONDITIONS CONFIRMED:
  Fetch: weather data for venue at kickoff time (not forecast time)
  Source: weather service at T-6h for best accuracy; confirm at T-2h
  Parameters: temperature (°C), precipitation (type and intensity),
    wind speed and direction, humidity (%), pitch condition
  Confirm: is any parameter at a threshold requiring a modifier?
    Temperature >30°C or <5°C: yes
    Rain: heavy or persistent: yes
    Wind >30mph: yes (especially for kicking sports)
    Humidity >80%: yes

STEP 2 — SPORT-SPECIFIC APPLICATION:
  Load: core/weather-intelligence.md (systematic modifiers)
  Load: core/core-weather-match-day.md (sport-by-sport reference)
  Apply relevant modifiers for this sport:
    Football heavy rain: technical team ×0.94 | physical team ×1.04
    Cricket humidity >70% evening T20: dew factor → batting second ×1.08
    Cricket overcast: swing bowling ×1.20
    Rugby wind >30mph: kicking team ×0.88 against wind | ×1.10 with wind
    F1 rain: safety car probability ×2.5; wet specialist modifier ×1.20
    MotoGP rain: wet specialist ×1.20; intermediate conditions widen interval ×1.50

STEP 3 — COMPOUND MODIFIER:
  If multiple weather conditions apply: multiply modifiers (never add)
  Cap: compound modifier floor at ×0.75 — flag EXTREME_CONDITIONS if exceeded
  Stack weather modifier with existing adjusted score from prior chains
  If weather modifier exceeds ±0.10 in either direction:
    Flag: WEATHER_OVERRIDE_ACTIVE = true
    This flag reduces the weight of non-weather modifiers
    (weather dominates when conditions are extreme)

STEP 4 — CONFIDENCE INTERACTION:
  Weather confirmed at T-2h: HIGH confidence weather modifier — apply fully
  Weather forecast at T-48h: MEDIUM confidence — apply ×0.60 of modifier
  Weather forecast at T-72h: LOW confidence — note as risk factor only, do not apply

STEP 5 — OUTPUT:
  conditions: { temp_c: [n], precip: [type], wind_mph: [n], humidity_pct: [n] }
  modifiers_applied: { weather: [×], compound: [×] }
  revised_adjusted_score: [n]
  flags: { weather_override_active: [bool], extreme_conditions: [bool] }
  confidence_note: [based on T-Xh confirmation]
```

---

## Compatibility

**Loading order:**      `core/agent-onboarding.md`
**Confidence check:**   `core/signal-confidence-framework.md`
**Layer conflict:**     `core/signal-confidence-framework.md` (hierarchy section)
**Context bridge:**     `core/fan-token-context-bridge.md`

---

*SportMind v3.97.38 · MIT License · sportmind.dev*
*Follow each chain step by step — do not skip steps or reorder*
