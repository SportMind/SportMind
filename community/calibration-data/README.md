# Calibration Data — SportMind Community

This directory holds community-submitted outcome records that power
SportMind's modifier calibration process.

---

## Structure

```
calibration-data/
├── README.md           (this file)
├── football/
│   ├── 2026/
│   │   ├── 01/         (January 2026)
│   │   └── ...
│   └── ...
├── mma/
├── basketball/
├── cricket/
└── {sport}/            (any sport covered by SportMind)
```

---

## How to submit an outcome record

1. Find or create the directory: `calibration-data/{sport}/{year}/{month}/`
2. Create a file named: `{event-id}-outcome.json`
3. Use the schema from `community/accuracy-tracking.md`
4. Submit a PR with label: `calibration-data`

**Example filename:** `ucl-final-2026-05-30-outcome.json`

---

## Schema

```json
{
  "outcome_record": {
    "record_id": "unique-uuid",
    "sport": "football",
    "event_id": "ucl-final-2026-05-30",
    "kickoff_utc": "2026-05-30T19:00:00Z",
    "recorded_at": "2026-05-30T17:00:00Z",
    "prediction": {
      "direction": "HOME",
      "adjusted_score": 71.4,
      "confidence_tier": "MEDIUM",
      "composite_modifier": 0.93,
      "sportmind_score": 84.2,
      "skill_contributor": "@github-handle"
    },
    "outcome": {
      "result": "HOME_WIN",
      "direction_correct": true,
      "token_symbol": "PSG",
      "token_24h_change_pct": 8.4,
      "token_direction_correct": true,
      "result_source_url": "https://www.uefa.com/..."
    }
  }
}
```

---

## Data requirements

- Result must be from an official source (URL required)
- Prediction must be the unmodified SportMind output
- No personal data, wallet addresses, or trade sizes
- Minimum 10 records per sport before calibration analysis begins

See `community/accuracy-tracking.md` for full methodology.
See `core/calibration-framework.md` for how data feeds into modifier updates.

*MIT License · SportMind · sportmind.dev*
