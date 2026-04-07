# Community Calibration — Contribution Framework

**How external contributors submit outcome records to SportMind's calibration pipeline.**

This document defines the contribution process, quality standards, required fields,
and review criteria for community-submitted calibration records. It is the mechanism
by which SportMind's modifiers become empirically validated rather than theoretically
estimated.

---

## Why community calibration matters

SportMind currently has 126 outcome records — all submitted by `sportmind-core`
from historical events selected to validate framework behaviour. These records
confirmed the model works correctly but cannot validate modifier accuracy, because
seed records were chosen from known outcomes.

Real calibration requires records from the community — people who ran SportMind
analysis *before* a match and tracked whether the output was correct. This is the
only way to validate whether the athlete_modifier, dew_modifier, narrative_modifier,
and other key modifiers are correctly calibrated.

The minimum events required before any modifier can be recalibrated:
- dew_modifier, rivalry_form_discount: **50 events**
- athlete_modifier, narrative_modifier, qualifying_delta_modifier: **100 events**
- macro_modifier: **200 events**

Community records are the only path to reaching these thresholds.

---

## What makes a valid calibration record

A calibration record is valid if and only if:

```
VALIDITY REQUIREMENTS:

1. PRE-MATCH: The SportMind analysis was performed BEFORE the match.
   Records created after the result are not valid for calibration.
   We cannot verify this from the record itself — we rely on contributor honesty
   and cross-reference with submission timestamps.

2. DOCUMENTED: The analysis is recorded in the confidence output schema format.
   Minimum required: adjusted_score, confidence_tier, composite_modifier, flags.

3. OUTCOME: The actual result is cited with a verifiable official source URL.
   No unofficial sources, no recollection from memory.
   ESPN/BBC Sport/official league site/Wikipedia match page = acceptable.

4. PROVENANCE: submitted_by (GitHub handle), submission_timestamp, data_quality tier.

5. HONEST: A wrong prediction with full documentation is MORE valuable than a
   correct prediction without documentation. Do not cherry-pick your good predictions.
```

---

## Submission process

### Step 1 — Run SportMind analysis before the match

```python
# Example: generate and save a pre-match record

import json
from datetime import datetime, timezone

# Run your SportMind analysis (any method — MCP, Skills API, direct file loading)
analysis = {
    "sport": "football",
    "event": "UCL QF Leg 1 — PSG vs Arsenal",
    "kickoff_utc": "2026-05-07T19:00:00Z",
    "analysis_generated_at": datetime.now(timezone.utc).isoformat(),
    
    # SportMind outputs
    "adjusted_score": 68.4,
    "confidence_tier": "MEDIUM",
    "composite_modifier": 0.97,
    "sportmind_score": 76,
    "sms_tier": "GOOD",
    "layers_loaded": [1, 2, 3, 4, 5],
    
    "modifiers_applied": {
        "athlete_modifier": 0.97,
        "macro_modifier": 1.00,
        "narrative_modifier": 1.00
    },
    
    "flags_active": ["lineup_unconfirmed"],
    
    "prediction": {
        "direction": "HOME",
        "recommended_action": "ENTER",
        "sizing": "50%"  # reduced due to lineup_unconfirmed
    },
    
    # Your reasoning notes (optional but valuable)
    "analyst_notes": "PSG home UCL QF. Arsenal away form strong. Lineup unconfirmed at time of analysis — reduced to 50% size per protocol."
}

# Save before the match
with open(f"pre_match_{datetime.now().strftime('%Y%m%d_%H%M')}.json", "w") as f:
    json.dump(analysis, f, indent=2)
```

### Step 2 — Record the outcome after the match

```python
# After the match: add the outcome to your record

outcome = {
    "result": "HOME_WIN",           # HOME_WIN, AWAY_WIN, DRAW
    "direction_correct": True,       # Did SportMind predict the right direction?
    "final_score": "2-1",           # Optional but useful context
    
    # Which modifiers proved important?
    "key_modifier_validated": "athlete_modifier",
    "modifier_direction_correct": True,
    "modifier_magnitude_error": 0.04,   # How far off was the magnitude?
    
    # Token outcome (if you also tracked the fan token)
    "token_symbol": "PSG",
    "token_24h_change_pct": 8.4,        # Optional
    "token_direction_correct": True,    # Optional
    
    # Official source
    "result_source_url": "https://www.bbc.co.uk/sport/football/result/psg-arsenal-2026-05-07",
    
    # Learnings (optional but valuable)
    "calibration_notes": "lineup_unconfirmed flag was correct — Mbappé successor started. Athlete modifier direction validated. Narrative momentum not as strong as expected — reduce narrative_modifier weight for UCL away legs."
}
```

### Step 3 — Create the full outcome record

Use this template:

```json
{
  "outcome_record": {
    "record_id": "football-ucl-qf-2026-05-07-psg-arsenal-001",
    "sport": "football",
    "event_id": "ucl-qf-leg1-2026-psg-arsenal",
    "event_name": "UCL Quarter-Final Leg 1 — PSG vs Arsenal",
    "kickoff_utc": "2026-05-07T19:00:00Z",
    "recorded_at": "2026-05-07T18:30:00Z",
    "submitted_by": "@your-github-handle",
    "submission_timestamp": "2026-05-08T09:00:00Z",
    
    "source": "community — pre-match analysis",
    
    "prediction": {
      "direction": "HOME",
      "base_score": 65.0,
      "adjusted_score": 68.4,
      "confidence_tier": "MEDIUM",
      "composite_modifier": 0.97,
      "sportmind_score": 76,
      "modifiers_applied": {
        "athlete_modifier": 0.97,
        "macro_modifier": 1.00
      },
      "flags_active": ["lineup_unconfirmed"],
      "layers_loaded": [1, 2, 3, 4, 5],
      "skill_contributor": "sportmind-core",
      "pre_match_note": "PSG home UCL QF. Arsenal away form. Lineup unconfirmed."
    },
    
    "outcome": {
      "result": "HOME_WIN",
      "direction_correct": true,
      "token_symbol": "PSG",
      "token_24h_change_pct": 8.4,
      "token_direction_correct": true,
      "result_source_url": "https://official-source.com/result"
    },
    
    "calibration_flags": {
      "key_modifier_validated": "athlete_modifier",
      "modifier_direction_correct": true,
      "modifier_magnitude_error": 0.04,
      "signal_was_actionable": true,
      "notes": "Your learning notes here."
    },
    
    "data_quality": {
      "source_tier": "community",
      "manually_verified": true,
      "official_result_confirmed": true
    }
  }
}
```

### Step 4 — Submit via Pull Request

```
FILE NAMING CONVENTION:
  community/calibration-data/{sport}/{year}/{month}/{event}-{date}-outcome.json

EXAMPLES:
  community/calibration-data/football/2026/05/ucl-qf-psg-arsenal-2026-05-07-outcome.json
  community/calibration-data/cricket/2026/03/ipl-mi-csk-2026-03-28-outcome.json
  community/calibration-data/mma/2026/04/ufc-302-pereira-prochazka-2026-04-12-outcome.json

PR TITLE: "Calibration record: [sport] [event] [date]"
PR LABEL: "calibration-record"

The PR will be reviewed by SportMind maintainers for:
  - Valid provenance fields (submitted_by, submission_timestamp)
  - Official result source URL
  - Pre-match timestamp (analysis must predate kickoff)
  - Security scan (scripts/security_validator.py --calibration)
```

---

## Quality tiers for community records

| Tier | Description | Acceptance criteria |
|---|---|---|
| Gold | Pre-match analysis with full modifier documentation + verified outcome | All fields present; official source URL; submission within 48h of match |
| Silver | Pre-match analysis with direction and basic modifiers | Direction, adjusted_score, at least one modifier; official source |
| Bronze | Post-match reconstruction from documented analysis | Clear evidence analysis preceded match; all provenance fields present |
| Rejected | No pre-match evidence, no official source, or missing provenance | Not accepted |

---

## Prioritised sports and modifiers

Community contributions are most valuable in these areas:

```
HIGHEST PRIORITY (modifiers closest to threshold):

1. CRICKET DEW FACTOR (need 50 records):
   T20 evening matches in South Asia
   Record: toss result + dew forecast + batting second advantage
   Target: 20+ records from IPL/T20I season
   
2. RUGBY LEAGUE STATE OF ORIGIN (need 50 records):
   Record: Origin game result + downstream NRL congestion signal
   Target: Records from all 3 Origin games per year
   
3. FOOTBALL NARRATIVE MODIFIER (need 100 records):
   Championship clinch, relegation deciders, cup finals
   Record: narrative_active flag + outcome + whether narrative amplified result
   
4. MMA WEIGH-IN (need 50 records for weight_miss specifically):
   Any MMA event where a fighter missed weight
   Record: weight_miss flag + fight outcome
   Most valuable: proving the ×0.72 modifier is correctly calibrated

SECOND PRIORITY (valuable but further from threshold):

5. FOOTBALL ATHLETE MODIFIER (need 100 records)
6. F1 QUALIFYING DELTA MODIFIER (need 100 records)
7. MACRO MODIFIER (need 200 records — longest path but highest impact)
```

---

## Recognition and leaderboard

Contributors are acknowledged in `community/leaderboard.md` with:

- Total records submitted
- Direction accuracy rate across their records
- Sports expertise badges (Gold tier submissions per sport)
- Calibration impact badge (when their records contribute to a modifier recalibration)

SportMind explicitly does not offer financial incentives for calibration records —
the quality of the library is the reward. Incentivised submissions produce biased
data. The leaderboard is recognition only.

---

## What happens when thresholds are reached

When a modifier reaches its minimum event threshold:

```
CALIBRATION REVIEW PROCESS:

Step 1: calibration_aggregate.py generates updated modifier accuracy report
Step 2: Maintainer reviews — is direction accuracy within target range?
  Within range: no change required; document as validated
  Outside range: propose modifier adjustment (requires community review)
Step 3: Community review period (7 days) — any contributor can comment
Step 4: If 70% consensus: maintainer updates modifier in relevant skill file
Step 5: New modifier value is version-controlled and documented in CHANGELOG

WHAT CAN CHANGE:
  Modifier magnitude (e.g., dew_modifier changes from +10% to +12%)
  Modifier threshold (e.g., >35% save rate → >40% for the GK_MODIFIER)
  
WHAT CANNOT CHANGE from community calibration:
  The loading order of skills
  The confidence output schema structure
  The SportMind Score calculation methodology
  These require maintainer decision, not community vote
```

---


---

## External contributor quick-start

**You do not need to be a developer to contribute.** If you used SportMind
to analyse a match before it happened and kept a record of your analysis
and the outcome, you have everything needed to submit a calibration record.

### Step 1 — Run SportMind before a match

Load the appropriate skill stack for your sport. Generate a signal. Record:
- The date and time you ran the analysis
- The sport, event, and teams involved
- The key modifiers SportMind applied (macro, athlete, competition tier)
- The SMS score and recommended action

### Step 2 — Record the actual outcome

After the match: note the result. Did SportMind get the direction right?
Which specific modifier did you test? What did you learn?

### Step 3 — Submit the record

Copy the JSON template from this file. Fill in your data. Submit via:
- GitHub Pull Request to `community/calibration-data/{sport}/{year}/{month}/`
- File name format: `{sport}-{event}-{date}-outcome.json`
- Or email to: calibration@sportmind.dev (we will handle the PR)

### What makes a good calibration record

**Do:** Submit records where you ran the analysis BEFORE the match.
**Do:** Include wrong-direction predictions — they are equally valuable.
**Do:** Note which specific modifier you were testing.
**Do not:** Submit records where you already knew the outcome.
**Do not:** Invent data or estimate modifiers retrospectively.

### Reviewer criteria

Every submitted record is reviewed by the SportMind community for:
1. Pre-match timestamp is credible (was analysis actually run before the match?)
2. Modifier values are plausible (no extreme values without explanation)
3. Official result is verifiable (result_source_url must resolve)
4. Learning notes are honest (including for wrong-direction records)

Records that pass review are merged within 7 days.

---

## Calibration milestones and recalibration triggers

Current status: **126 records** across 21 sports — first recalibration complete (see `core/modifier-recalibration-v3.md`)

```
RECALIBRATION THRESHOLDS:
  50 records for a specific modifier: Initial recalibration possible
  100 records for a specific modifier: Full recalibration with confidence
  200 records for macro_modifier: Macro threshold recalibration

CURRENT PROGRESS TOWARD THRESHOLDS:
  dew_modifier: 4 records → need 46 more for initial recalibration
  athlete_modifier (football): 8 records → need 42 more
  india_pakistan_modifier: 3 records → need 47 more
  weight_miss_modifier (MMA): 3 records → need 47 more
  derby_active (compression): 4 records → need 46 more
  
  The community can reach these thresholds. Each record matters.
  When thresholds are reached, the SportMind team runs the recalibration
  and publishes updated modifier values with the evidence base.
```


*MIT License · SportMind · sportmind.dev*
