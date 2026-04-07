# Accuracy Tracking — SportMind Community

**How prediction accuracy is measured for leaderboard and calibration purposes.**
This file defines the methodology so contributors understand what "accurate" means.

---

## What counts as an accurate prediction

SportMind makes two types of prediction in every output:

```
1. DIRECTION PREDICTION:
   Did the signal point the right way?
   
   HOME | AWAY | LONG | SHORT → did that side outperform?
   POSITIVE token signal → did the token price rise 24h post-event?
   NEGATIVE token signal → did the token price fall 24h post-event?
   ABSTAIN → was abstaining the correct choice? (price moved <3% either way)

2. MODIFIER DIRECTION:
   Did the modifier adjust in the right direction?
   
   athlete_modifier < 1.00 → did athlete underperform expectation?
   macro_modifier ×0.75 → did token underperform vs non-macro period?
```

---

## Measurement windows

| Signal type | Measurement window | What we measure |
|---|---|---|
| Match result (team sport) | Full time result | Home/Away/Draw correct |
| Fan token movement | 24h post-event close | Direction correct |
| Prediction market | Market settlement | Outcome correct |
| Modifier effect | Match outcome vs base | Modifier direction correct |
| ABSTAIN recommendation | 24h token move | Did abstaining avoid a loss? |

---

## Accuracy submission format

```json
{
  "outcome_record": {
    "sport": "football",
    "event_id": "ucl_final_2026",
    "kickoff_utc": "2026-05-31T19:00:00Z",
    "recorded_at": "2026-05-31T17:30:00Z",
    "prediction": {
      "direction": "HOME",
      "adjusted_score": 71.4,
      "confidence_tier": "MEDIUM",
      "composite_modifier": 0.93,
      "skill_contributor": "@github-handle"
    },
    "outcome": {
      "result": "HOME_WIN",
      "direction_correct": true,
      "token_symbol": "PSG",
      "token_24h_change_pct": 12.4,
      "token_direction_correct": true,
      "result_source_url": "https://www.uefa.com/..."
    }
  }
}
```

*Submit via PR to: `community/calibration-data/{sport}/{year}/`*

*MIT License · SportMind · sportmind.dev*
