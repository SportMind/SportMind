# Cricket Statistics Intelligence — SportMind Sub-Module

**Status: CORE** — Sub-module of `sport-domain-cricket.md`.
Dew factor already calibrated 5/5 in SportMind records — this module
extends that foundation across the full statistical framework.

Zero-dependency. Cricinfo and ESPNcricinfo provide comprehensive free data.

---

## Overview

Cricket statistics are uniquely format-dependent. A batting average of 45
means something entirely different in Tests vs T20s. A bowling economy of
7.5 is acceptable in T20 cricket and catastrophic in ODIs. The first step
before applying any cricket statistical modifier is confirming the format.

The three highest-value cricket statistics for fan token signal purposes:
1. **Economy rate vs target** — bowling efficiency in limited-overs cricket
2. **Run rate trajectory** — batting phase analysis in T20s
3. **Conditions × player statistics** — dew, pitch, weather interaction

Load `core/match-statistics-intelligence.md` for universal modifier framework.

---

## Domain Model

### Statistics by format

```
T20 FORMAT — STATISTICS HIERARCHY:

  TIER 1 — OUTCOME-CORRELATED:
    Economy rate (bowling): < 7.0 in Powerplay = elite. < 8.0 overall = above average.
      Economy < 7.0: × 1.10 bowling signal
      Economy 7.0–8.5: neutral modifier
      Economy > 9.5: × 0.92 bowling signal
      
    Strike rate (batting): > 150 = elite. > 135 = above average.
      SR > 150: × 1.10 batting signal (match-changing capability)
      SR 130–150: × 1.05
      SR < 115: × 0.90 (anchor role — limits scoring)
      
    Powerplay performance (overs 1–6):
      Batting average in Powerplay: > 30 = × 1.06 (explosive opener signal)
      Wickets per Powerplay (bowling): > 2.0 avg = × 1.08 (early breakthroughs)

    Death bowling economy (overs 17–20):
      < 8.0 economy in death: × 1.12 (hardest phase to bowl in)
      > 10.0 economy: × 0.88 (vulnerability in match-defining phase)

  TIER 2 — CONTEXTUAL:
    Batting position (where in the order — context changes all statistics)
    Average (T20-specific, minimum 20 innings for reliability)
    Dot ball percentage (bowling): > 40% = pressure indicator
    
  TIER 3 — DESCRIPTIVE:
    Total runs (without match context)
    Total wickets (without economy/conditions context)

---

ODI FORMAT — STATISTICS HIERARCHY:

  TIER 1 — OUTCOME-CORRELATED:
    Economy rate: < 5.0 = elite; < 5.5 = above average; > 6.5 = below average
    Average (batting): > 40 is meaningful in ODIs (min 30 innings)
    
    Middle overs dominance (overs 11–40):
      Economy < 5.0 in middle overs: × 1.08
      Batting average > 45 in middle overs: × 1.06 (anchor + acceleration)
      
  TIER 2 — CONTEXTUAL:
    Powerplay + death bowling separately (similar T20 logic but less extreme)
    Net Run Rate (NRR) in tournament context: tiebreaker only

---

TEST FORMAT — STATISTICS HIERARCHY:

  TIER 1 — OUTCOME-CORRELATED:
    Batting average: > 45 = consistent quality (min 20 Tests)
    Bowling average: < 28 = elite (min 20 Tests); < 32 = above average
    Bowling strike rate: < 55 = match-winner potential
    
  TIER 2 — CONTEXTUAL:
    Home vs Away differential: batting averages often 15–20 points lower away.
    Always split home/away statistics before applying Test modifiers.
    
    Pitch condition interaction (see Conditions Framework below):
      A spinner's statistics on spin-friendly pitches vs fast pitches differ vastly.
      Match spinner's historical stats on same pitch type first.
```

### Conditions framework — cricket's dominant variable

```
PITCH × PLAYER STATISTICS INTERACTION:

  This is cricket's most important statistical concept. A player's raw statistics
  are meaningless without conditions context. Always apply conditions first.

  PACE-FRIENDLY PITCH (hard, bouncy, grass cover):
    Seam/swing bowling economy and average improve by 15–20%.
    Batting averages for front-foot players decline 10–15%.
    Confirm pitch type from official ground reports (Tier 1) before applying.

  SPIN-FRIENDLY PITCH (dry, dusty, bare):
    Spin bowling economy improves dramatically in final 2 innings.
    Front-foot batters with weak footwork vs spin: apply × 0.88.
    Spinners with > 60% of career wickets on turning pitches: × 1.12.

  NEUTRAL PITCH (batters' paradise):
    Raw statistics apply without conditions adjustment.
    High-scoring matches expected: batting-dominant modifiers apply.
    Bowling economy modifiers are less predictive.

DEW FACTOR — CALIBRATED 5/5 IN SPORTMIND:

  The dew factor in evening T20s is already documented in sport-domain-cricket.md.
  This module adds the statistical grounding:
  
  STATISTICAL IMPACT OF DEW:
    Bowling economy in 2nd innings (dew active): increases 0.8–1.2 runs/over
    for spin bowlers specifically. Seam bowling less affected.
    
    Dew modifier application:
      Evening T20 match (> 20:00 local start), humidity > 70%:
        Apply × 0.88 to spin bowling economy in 2nd innings
        Apply × 1.06 to batting chasing team in 2nd innings
        
    This modifier is already calibrated — applying it is the correct action.
    The 5/5 calibration record confirms it: APPLY DEW MODIFIER when conditions
    match (evening T20, high humidity, team batting second).

WEATHER — DLS INTERACTION:
  Rain and DLS (Duckworth-Lewis-Stern) create artificial targets.
  When DLS is invoked: all pre-match batting statistics carry 0.70× weight.
  DLS targets and statistics are not comparable to clean match data.
  
  If rain is forecast (> 60% probability): flag WEATHER_DLS_RISK in signal.
  Reduce signal confidence to MEDIUM regardless of form statistics.

TOSS SIGNAL:
  Already documented in domain skill. Statistical grounding:
    Toss winner choosing to field (T20 evening): historically 52–58% win rate
    on pitches where dew is active. The advantage is real and measurable.
    Apply × 1.05 to team fielding second when dew is confirmed/likely.
```

### Individual performance statistics

```
BATTING MATCHUP STATISTICS:
  Batter vs specific bowler type (pace vs spin, right-arm vs left-arm):
    Some batters have documented weaknesses vs specific delivery types.
    When the opposition has a specialist who exploits that weakness:
    Apply × 0.92 to that batter's expected contribution.
    Apply × 1.08 to that specialist bowler's expected impact.
    
  Home vs Away batting differential:
    Most reliable individual cricket modifier outside conditions.
    If a batter's home average > 45 but away average < 30:
    Apply × 0.75 to their batting signal in away matches.

BOWLING MATCHUP STATISTICS:
  Specific bowling style vs team batting strengths:
    A team averaging 40+ vs spin on home pitches may have weakness overseas.
    A team's record vs left-arm pace vs right-arm pace may diverge significantly.
    Load these matchup statistics when available — they are Tier 2 at minimum.

INDIA VS PAKISTAN — SPECIAL CASE:
  Already documented in domain skill with × 2.00 commercial multiplier.
  Statistical note: standard form statistics carry REDUCED weight in this fixture.
  The × 2.00 multiplier is a CDI/commercial signal, not a match outcome predictor.
  For match outcome: conditions, toss, and current form take precedence over
  the historical significance modifier.
```

### Historical statistics framework — cricket specific

```
RECENCY IN CRICKET — FORMAT AND PHASE CONSIDERATIONS:

  Unlike most sports, cricket form statistics should be filtered by:
  1. Format (T20 form does not transfer to Test predictions)
  2. Phase of innings (Powerplay specialist vs middle-over anchor)
  3. Conditions type (hard pitch vs turning pitch)
  4. Opposition tier (top-10 ranked nations vs lower-ranked)

  SAMPLE SIZE — CRICKET MINIMUM:
    T20 batting: 15 innings minimum for individual modifier
    ODI batting: 25 innings minimum
    Test batting: 20 Tests minimum (career) + 5 recent for form
    Bowling (any format): 20 wickets minimum at format level

  IPL STATISTICS — LEAGUE CONTEXT:
    IPL statistics are valid predictors for T20 international performance
    but carry 0.85× weight vs international statistics.
    Reason: IPL batting conditions differ (smaller boundaries, flat pitches).
    Apply IPL statistics as supporting evidence, not primary Tier 1 signal.
```

---

## Event Playbooks

### Playbook 1: T20 match — conditions pre-assessment
```
trigger:  T20 match confirmed for monitored token team
timing:   T-4h
protocol:
  1. Check venue, start time, humidity forecast
  2. If evening match + humidity > 70%: activate dew modifier
  3. Obtain pitch report (Tier 1: local ground staff, match referee report)
  4. Apply pitch type to relevant bowler/batter statistics
  5. Check toss intention if available (fielding = dew advantage signal)
  6. Generate pre-match signal with conditions_modifier noted
output:   T20 signal with dew_active flag if applicable
note:     This playbook has a calibrated foundation (5/5 dew factor records)
```

### Playbook 2: Test series signal — form and conditions
```
trigger:  Test series match (any test in the series)
timing:   T-24h
protocol:
  1. Check pitch preparation (grass cover, moisture content — Tier 1 source)
  2. Split home/away statistics for all key players
  3. Apply conditions-specific statistics (spinner on turning pitch, etc.)
  4. Check series context — does any team have a must-win situation?
  5. Generate signal — Test cricket has highest CDI weight per result
output:   Test match signal with conditions_type and series_context noted
```

### Playbook 3: India vs Pakistan — commercial signal protocol
```
trigger:  India vs Pakistan confirmed (any format, any tournament)
timing:   T-48h to T-12h
protocol:
  1. Apply × 2.00 commercial multiplier to CDI calculation
  2. Run standard form and conditions analysis separately
  3. Load macro/macro-broadcast-disruption.md for broadcast window context
  4. Toss result (when known): apply conditions modifier if dew likely
  5. Do NOT rely on historical H2H for match prediction — conditions dominate
output:   Dual signal: commercial CDI signal (×2.00) + match prediction separately
note:     These are two distinct outputs. CDI is commercial. Match prediction is sporting.
```

### Playbook 4: Dew factor confirmation — in-match update
```
trigger:  Match started, dew conditions confirmed in-match (ball gets wet)
timing:   During second innings (overs 12–14 typically when dew peaks)
protocol:
  1. Dew confirmed by commentary / pitch-side reports
  2. Recalculate bowling economy expectations for spin bowlers
  3. Update CDI calculation — chasing team advantage confirmed
  4. Flag: "DEW_CONFIRMED_IN_MATCH" in signal output
output:   Updated in-match signal with dew confirmation
note:     This is a live update — relevant for agents with live data feeds
```

---

## Signal Weight Adjustments

For cricket statistics sub-module:

| Statistical modifier | Weight | Cap |
|---|---|---|
| Economy rate differential (Tier 1) | 12% additional weight | ±8 pts |
| Dew factor (calibrated) | 10% additional weight | ±6 pts |
| Batting SR / average (Tier 1) | 10% additional weight | ±6 pts |
| Conditions × specialist matchup | 8% additional weight | ±5 pts |
| Home/away differential | 6% additional weight | ±4 pts |

**Combined cricket statistical modifier cap: ±12 points on adjusted_score.**

---

## Autonomous Execution

**Trigger conditions:**
- Toss result confirmed for monitored T20 match
- Evening T20 match with humidity > 70% (dew protocol activation)
- Rain interruption begins (DLS risk)
- Match result confirmed for CDI update

**Execution at autonomy Level 2:**
- Toss + field elected + evening + humidity: auto-apply dew modifier. Notify.
- Rain interruption: flag WEATHER_DLS_RISK. Reduce confidence. Notify.
- Match result: recalculate CDI. Notify operator.

**Execution at autonomy Level 3–4:**
- Auto-check humidity forecast at T-6h for all evening T20 matches
- Auto-apply dew modifier when conditions match (calibrated trigger)
- Auto-dispatch post-match CDI update within 20 min of confirmed result
- Dew confirmed in-match: auto-update signal with DEW_CONFIRMED flag

**Hard boundaries:**
- Dew modifier requires BOTH: (a) evening match > 20:00 local AND (b) humidity > 70%.
  Neither condition alone is sufficient — both must be present.
- DLS scenario: all pre-match batting statistics carry 0.70× weight only.
  Never apply full weight statistics to a DLS-affected match.
- India vs Pakistan × 2.00 multiplier: CDI/commercial signal ONLY.
  Never apply it to match outcome prediction — they are separate calculations.
- IPL statistics: 0.85× weight when predicting international performance.
  This discount cannot be waived even for players with large IPL sample sizes.

---

## Key Commands

| Action | Command | Notes |
|---|---|---|
| T20 pre-match | Load this + sport-domain-cricket.md | Dew check required |
| Test series | Playbook 2 | Conditions and home/away split |
| India vs Pakistan | Playbook 3 | Dual output: CDI + match |
| Live dew confirmation | Playbook 4 | Agents with live data feed |

---

## Agent Reasoning Prompts

- "Format first: T20, ODI, or Test? Statistics are not transferable across formats."
- "Evening T20, humidity > 70%: dew modifier is calibrated 5/5. Apply it."
- "Spinner on turning pitch: multiply their historical stats by pitch-type match."
- "India vs Pakistan: two outputs required. Commercial CDI (×2.00) separate from match signal."
- "DLS active: all batting statistics carry 0.70× weight only. Flag WEATHER_DLS_RISK."

---

## Data Sources

- ESPNcricinfo (free): cricinfo.com — comprehensive statistics all formats (Tier 1)
- CricketArchive (free): cricketarchive.com — historical records (Tier 2)
- ICC official: icc-cricket.com — rankings, official results (Tier 1)
- Pitch reports: ground staff official + match referee reports (Tier 1 only for dew)
- Weather: local meteorological service for the venue city (Tier 2)

---

## Compatibility

**Load alongside:** `sports/cricket/sport-domain-cricket.md`
**Universal framework:** `core/match-statistics-intelligence.md`
**Market:** `market/international-cricket-cycle.md`
**Breaking news:** `core/breaking-news-intelligence.md` (key player injury)
**Conditions already calibrated:** dew factor 5/5 in SportMind calibration records

---

*SportMind v3.90.0 · MIT License · sportmind.dev*
