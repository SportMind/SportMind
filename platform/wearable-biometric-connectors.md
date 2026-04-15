---
name: wearable-biometric-connectors
description: >
  Integration patterns for connecting wearable technology and biometric
  monitoring platform outputs into SportMind's athlete modifier chain.
  Covers five connector categories: (1) GPS and load tracking (Catapult,
  STATSports, Kinexon) producing distance, high-speed running, accelerations;
  (2) Recovery monitoring (Whoop, Oura, Garmin, Polar) producing HRV,
  sleep score, readiness score; (3) Force and biomechanics (Catapult
  Vector, Zebra Sports) producing impact loads and movement quality;
  (4) Physiological monitoring (Zephyr, Polar Team Pro) producing heart
  rate, oxygen saturation, live physiological state; (5) Match tracking
  data (Hawkeye, StatsBomb 360, Opta Vision) producing spatial and event
  data from video analysis. For each connector: what data is available,
  how to translate the vendor's native score into SportMind's ARI
  (Athlete Readiness Index) input format, and agent decision rules.
  Zero-dependency principle: this file is a connector TEMPLATE — it
  documents how to integrate third-party outputs, not how to build
  the tracking systems. All SportMind computations remain in-library.
  Applicable to elite sport performance teams, club analytics departments,
  and developers building performance intelligence agents.
---

# Wearable and Biometric Data Connectors — SportMind

**Wearables produce data. SportMind produces intelligence. This skill
is the bridge between them.**

Catapult knows how far a player ran. Whoop knows how well they slept.
SportMind knows what that means for Saturday's match. This skill documents
exactly how to translate the output of physical monitoring platforms into
inputs for SportMind's athlete readiness and signal chain computation.

The zero-dependency principle applies throughout: SportMind does not
call wearable APIs, process raw sensor data, or run ML models. You bring
the wearable output; SportMind tells you what to do with it.

---

## The connector model

```
ARCHITECTURE:
  [Wearable Platform] → [Raw Data] → [Vendor Score] → [SportMind Input]
                                           ↑
                              This is where this skill operates.
                              We translate vendor scores into
                              SportMind ARI component inputs.

THREE CONNECTOR LAYERS:

  Layer 1 — DIRECT SCORE BRIDGE:
    Vendor provides a readiness/recovery score (0–100 or similar).
    SportMind maps this directly to ARI component.
    Simplest integration. Most wearables provide this.

  Layer 2 — METRIC TRANSLATION:
    Vendor provides raw metrics (HRV, HRV score, sleep stages, distance).
    SportMind provides formulas to convert these to ARI components.
    More granular; useful when vendor score is not trusted.

  Layer 3 — RAW SIGNAL INTEGRATION:
    Vendor provides raw time-series data (GPS tracks, heart rate streams).
    Requires preprocessing before SportMind integration.
    Appropriate for analytics departments with data science capability.
    SportMind provides the intelligence framework; preprocessing is yours.
```

---

## Connector 1 — GPS and load tracking

```
PLATFORMS: Catapult Sports (Vector, Edge), STATSports (Apex, Viper),
           Kinexon, Statsports, GPSports

KEY METRICS PRODUCED:
  Total Distance (m or km)
  High-Speed Running (HSR) distance: typically > 5.5 m/s
  Sprint distance: typically > 7.0 m/s
  Accelerations / Decelerations: number of efforts > threshold
  Player Load: proprietary composite (Catapult: ~1500–2000 per 90 min football)
  Explosive Distance: high-acceleration bursts

SPORTMIND INTEGRATION — FATIGUE TRAJECTORY COMPONENT:

  Load vs Baseline Method:
    Calculate: today_load / player_season_average_load
    0.90–1.10× baseline → fatigue_component = 1.00 (normal)
    1.10–1.25× baseline → fatigue_component = 0.96 (elevated load)
    > 1.25× baseline    → fatigue_component = 0.90 (high load — flag)
    < 0.80× baseline    → fatigue_component = 1.03 (light session, rested)
    < 0.60× baseline    → fatigue_component = 1.02 (very light — may indicate
                          managed session due to fatigue or tactical choice)

  HSR Decline Signal:
    Week-over-week HSR decline > 15%: early_fatigue_flag = true
    → Apply additional −0.03 to fatigue_component
    → This is the library's implementation of "invisible fatigue" detection

  Acute:Chronic Workload Ratio (ACWR):
    ACWR = (7-day average load) / (28-day average load)
    ACWR > 1.50: injury_risk_elevated = true; apply to ARI injury_risk component
    ACWR 1.30–1.50: load_spike_flag = true
    ACWR 0.80–1.30: optimal training zone
    ACWR < 0.80: underload (detraining risk in extended periods)

  AGENT RULE:
    If GPS data shows ACWR > 1.50 AND ARI injury_risk_threshold > 0.12:
    → Compound risk — raise INJURY_RISK_ELEVATED flag and escalate to human

CONNECTOR TEMPLATE:
  // Input: Catapult/STATSports session summary
  const session = {
    player_load_today:    1650,
    player_load_28d_avg:  1580,
    hsr_today_m:          892,
    hsr_28d_avg_m:        1050,
    acwr:                 1.04
  };

  const load_ratio = session.player_load_today / session.player_load_28d_avg;
  const hsr_decline = (session.hsr_28d_avg_m - session.hsr_today_m) / session.hsr_28d_avg_m;
  const fatigue_component = load_ratio > 1.10 ? 0.96 :
                             load_ratio > 1.25 ? 0.90 :
                             load_ratio < 0.80 ? 1.02 : 1.00;
  // Pass fatigue_component to ARI calculation
```

---

## Connector 2 — Recovery monitoring

```
PLATFORMS: Whoop (4.0, 5.0), Oura Ring (3, 4), Garmin (Body Battery),
           Polar Team Pro, Firstbeat Analytics, Catapult Recovery

KEY METRICS PRODUCED:
  HRV (Heart Rate Variability): ms RMSSD; higher = better recovered
  Resting Heart Rate: lower than baseline = better recovered
  Sleep Score / Quality: 0–100 or sleep stage hours
  Readiness Score: vendor composite (Whoop: 0–100%, Oura: 0–100)
  Recovery Score: Whoop; Body Battery: Garmin

SPORTMIND INTEGRATION — RECOVERY COMPONENT → ARI INPUTS:

  WHOOP RECOVERY SCORE BRIDGE:
    Whoop 0–33% (red):    recovery_component = 0.82 (poor recovery)
    Whoop 34–66% (yellow): recovery_component = 0.95 (moderate)
    Whoop 67–100% (green): recovery_component = 1.02 (well recovered)

  OURA READINESS SCORE BRIDGE:
    Oura 0–59:   recovery_component = 0.83
    Oura 60–69:  recovery_component = 0.93
    Oura 70–84:  recovery_component = 1.00
    Oura 85–100: recovery_component = 1.04

  GARMIN BODY BATTERY BRIDGE:
    0–25:   recovery_component = 0.80
    26–50:  recovery_component = 0.92
    51–75:  recovery_component = 1.00
    76–100: recovery_component = 1.05

  RAW HRV METHOD (if vendor score not available):
    Calculate % deviation from athlete's personal HRV baseline (30d average)
    HRV 10%+ above baseline:   recovery_component = 1.05
    HRV at baseline (±10%):    recovery_component = 1.00
    HRV 10–20% below baseline: recovery_component = 0.94
    HRV 20–30% below baseline: recovery_component = 0.88
    HRV 30%+ below baseline:   recovery_component = 0.82 (significant fatigue)

  MATCH-DAY APPLICATION:
    Use recovery score from the MORNING OF MATCH (T-8h to T-4h optimal window).
    Pre-training scores are less predictive than match-morning scores.

  AGENT RULE:
    Recovery component < 0.85 for two consecutive match-morning readings:
    → CHRONIC_FATIGUE_FLAG: raise to medical staff; do not suppress signal
    Recovery component < 0.82 on match morning for ATM-tier player:
    → Apply to ARI fatigue_trajectory component (compounds with schedule load)

  FAN TOKEN APPLICATION:
    Recovery data is typically private and not publicly available.
    When available via club data access: apply directly.
    When unavailable: use fatigue_trajectory from schedule data as proxy.
    Never fabricate recovery scores — absent data defaults to 1.00.
```

---

## Connector 3 — Biomechanics and force monitoring

```
PLATFORMS: Catapult Vector (inertial measurement unit), Zebra Sports (NFL),
           Dorsavi, IMeasureU, force plate systems (Vald, ForceDecks)

KEY METRICS PRODUCED:
  Asymmetry Index: left/right load imbalance (%)
  Ground Contact Time: ms (lower = better mechanical efficiency)
  Jump Height / Force: CMJ (countermovement jump) — reliable fatigue marker
  Acceleration Pattern Quality: smoothness of acceleration curve
  Impact Load: bone stress metric for high-impact positions

SPORTMIND INTEGRATION:

  COUNTERMOVEMENT JUMP (CMJ) METHOD — most validated fatigue marker:
    CMJ vs athlete's personal baseline (10+ test history required):
    > 5% above baseline:        biomech_component = 1.03 (peak physical state)
    ±5% of baseline:            biomech_component = 1.00
    5–10% below baseline:       biomech_component = 0.95
    10–15% below baseline:      biomech_component = 0.90
    > 15% below baseline:       biomech_component = 0.83 (significant fatigue)
    Agent flag: CMJ > 15% below → PHYSICAL_FATIGUE_CONFIRMED

  ASYMMETRY INDEX:
    < 10% asymmetry: within normal range, no signal
    10–15% asymmetry: mild flag — soft-tissue injury risk elevated slightly
    > 15% asymmetry: ASYMMETRY_FLAG = true
      → Add to ARI injury_risk component: +0.08 injury risk penalty
      → Common precursor to hamstring / adductor issues
      → Raise to physio immediately; do not suppress

  SPORT-SPECIFIC BIOMECHANICS:
    Football: CMJ primary; sprint mechanics secondary
    Basketball: CMJ critical (70+ games per season; CMJ highly sensitive)
    MMA: grip strength testing (functional indicator of fight-camp quality)
    Cricket fast bowlers: shoulder load asymmetry (key injury precursor)
    Rugby props: scrum force output vs baseline (position-specific)
```

---

## Connector 4 — Match tracking (video / spatial)

```
PLATFORMS: Hawkeye (ball and player tracking), StatsBomb 360 (pressure maps),
           Opta Vision, Second Spectrum, ChyronHego TRACAB

KEY METRICS PRODUCED:
  Player tracking: x/y coordinates at 25Hz (position at any moment)
  Pressure events: percentage of actions under active pressure
  PPDA (Passes Allowed per Defensive Action): pressing intensity metric
  xT (Expected Threat): spatial threat value of ball positions
  Off-ball runs: quantity and quality of movement without the ball

SPORTMIND INTEGRATION:

  PPDA → SPATIAL SIGNAL (from core/spatial-game-intelligence.md):
    PPDA < 7: high press — spatial system is aggressive
    PPDA 7–12: moderate press
    PPDA > 12: low block — spatial system is passive/reactive
    Use to calibrate core/spatial-game-intelligence.md inputs

  PRESSURE EVENTS → DECISION QUALITY:
    % actions under pressure (from StatsBomb 360):
    Use to calibrate core/athlete-decision-intelligence.md DQI inputs
    High pressured_pass_completion → DQI Dimension 2 (Possession Decision) input

  TRACKING DATA → FATIGUE DETECTION:
    Distance in final 15 min vs first 15 min of match:
    Decline > 20%: late_match_fatigue_confirmed = true
    → Apply to ARI fatigue_trajectory for next match prediction
    → Key signal for rotation probability

  AGENT RULE:
    Tracking data provides the most reliable load signals available.
    When tracking data is available for the previous match, it supersedes
    schedule-based fatigue estimates.
    When unavailable: use schedule-based fatigue_trajectory (default).

COST AND ACCESS REALITY:
  StatsBomb 360 / Opta Vision: club / analyst subscription; not free
  Hawkeye: broadcasted matches; limited API access
  Free proxy: match time played (available from most public sources)
  Open data: StatsBomb provides historical open datasets for research
```

---

## Connector 5 — Integration with ARI

```
COMPLETE INTEGRATION EXAMPLE:
  A performance analyst at a football club has access to:
    - Catapult GPS (available)
    - Whoop recovery (available for some players)
    - StatsBomb 360 (available for last match)
    - No force plate data

  For a player ahead of Saturday's match:

  Step 1 — GPS → fatigue_trajectory:
    ACWR = 1.08 (optimal zone), HSR decline = −8% (mild)
    fatigue_component = 1.00 (normal), no flags

  Step 2 — Whoop → recovery_component:
    Match morning reading: 71% (green)
    recovery_component = 1.02

  Step 3 — Tracking → injury_risk:
    Late-match fatigue confirmed in last match (−18% distance decline)
    Recurrence flag: returned from hamstring 5 weeks ago
    injury_risk_penalty = 0.08 (5wk return) + 0.03 (late fatigue) = 0.11
    injury_risk_component = 0.89

  Step 4 — Combine with ARI standard components:
    ARI components now have wearable-augmented inputs for:
      fatigue_trajectory = 1.00 (GPS-validated, not schedule-estimated)
      injury_risk_threshold = 0.89 (tracking + return history)
    Standard components used for: motivation, travel, availability

  RESULT: ARI is more precise, with wearable data replacing estimates
  where available. Components with no wearable data still use standard
  SportMind calculations. Mixed input is explicitly supported.

OUTPUT FLAG:
  "ari_data_sources": {
    "fatigue_trajectory":     "GPS (Catapult) — validated",
    "recovery_component":     "Whoop — match morning reading",
    "injury_risk_threshold":  "tracking + history — calculated",
    "motivation_state":       "standard — no wearable input",
    "availability_confidence":"standard — pre-match report"
  }
```

---

## Non-fan-token application

```
PERFORMANCE TEAMS (no fan token context):
  All five connectors apply directly to pre-match squad intelligence.
  ARI informs selection decisions, rotation planning, and injury prevention.
  Output: pre-match readiness brief per player + team-level readiness index

MEDIA AND RESEARCH:
  Wearable data (when club-released) provides the most objective basis
  for assessing player condition in public commentary.
  StatsBomb open data enables research-grade tracking analysis.

BETTING INTELLIGENCE AGENTS:
  Wearable-augmented ARI provides materially better pre-match signals
  than schedule-only fatigue estimation.
  Key signal: CMJ > 15% below baseline = significant underperformance risk
  not yet priced in the market (when data is available before market moves)

FAN TOKEN APPLICATION:
  Wearable-augmented ARI feeds into FTIS precisely:
  A key player with confirmed biomechanical fatigue reduces the expected
  performance quality, reducing the expected win probability, reducing
  the PATH_2 WIN burn probability for that match.
  Clubs that share athlete readiness data (rare but growing) provide
  the most commercially precise fan token pre-match signals available.
```

---

*SportMind v3.66 · MIT License · sportmind.dev*
*See also: core/athlete-readiness-index.md · core/core-fixture-congestion.md*
*core/travel-timezone-intelligence.md · core/injury-intelligence/*
*core/athlete-decision-intelligence.md · platform/api-providers.md*
