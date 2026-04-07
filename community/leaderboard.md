# Community Leaderboard — SportMind

**Tracks contributor accuracy over time.** The leaderboard rewards contributors
whose skills produce correct agent reasoning — not just well-formatted files.

---

## How the leaderboard works

```
CONTRIBUTION SCORE = (Skill Quality Score × 0.40)
                   + (Prediction Accuracy × 0.40)
                   + (Community Impact × 0.20)

SKILL QUALITY SCORE:
  Validator pass rate: 0–30 points (based on skill file quality)
  Completeness: 0–30 points (all sections, no stubs)
  Peer review rating: 0–40 points (community rating after merge)

PREDICTION ACCURACY:
  Based on outcome_records submitted for skills you contributed
  Direction accuracy ≥ 70%: 40 points
  Direction accuracy 60–69%: 25 points
  Direction accuracy 50–59%: 10 points
  Direction accuracy < 50%: 0 points (skill flagged for review)
  Minimum 50 tracked events required to qualify

COMMUNITY IMPACT:
  Citations: other contributors referencing your skill: +2 per citation
  Issues resolved: skills you improved that were flagged: +5 per resolution
  Translations contributed: +8 per language per skill
  Calibration data submitted: +1 per validated outcome record
```

---

## Leaderboard tiers

| Tier | Points | Badge | Privileges |
|---|---|---|---|
| **SportMind Expert** | 500+ | 🏆 | Direct merge rights for Tier 2-4 skills |
| **Senior Contributor** | 250–499 | ⭐⭐⭐ | Reviewer on PRs; calibration proposal rights |
| **Contributor** | 100–249 | ⭐⭐ | Claim Tier 1 skill contributions |
| **Member** | 25–99 | ⭐ | Claim Tier 2-4 skill contributions |
| **New** | 0–24 | — | Good First Issues only |

---

## Current leaderboard (v3.28)

*126 calibration records submitted by founding team across 21 sports.*
*Modifier accuracy thresholds require 50+ records per modifier to qualify.*
*All current contributors show N/A for full modifier accuracy — threshold not yet reached.*
*First external contributor records will be the library's first non-seed entries.*

| Rank | Contributor | Points | Calibration records | Accuracy | Tier |
|---|---|---|---|---|---|
| 1 | `@sportmind-core` | 500+ | 126 (all 21 sports) | 96% overall (N/A per modifier — threshold pending) | Expert 🏆 |

**You are not on this leaderboard yet — be the first external contributor.**

See `FIRST-RECORD-CHALLENGE.md` — submit one calibration record before a real match.
The first 10 external contributors receive permanent Founding Calibrator recognition.

**How to appear on this leaderboard:**
1. Submit a calibration record → `community/calibration-data/` PR with label `calibration-record`
2. Contribute a skill (sports/, athlete/, fan-token/, i18n/) → merged PR
3. Fix a flagged issue (GOOD_FIRST_ISSUES.md) → merged PR + maintainer confirms

*See [community/accuracy-tracking.md](accuracy-tracking.md) for the full
accuracy measurement methodology.*

---

## Submitting for leaderboard credit

```
1. Merged PR to sports/, athlete/, fan-token/, or i18n/ directories
   → Automatic: validator runs; quality score calculated
   → Manual: maintainer assigns peer review rating within 14 days

2. Calibration data submitted (community/calibration-data/)
   → Automatic: outcome_record validated against official result
   → Points awarded: +1 per validated record

3. Translation submitted (i18n/{lang}/)
   → Manual: language reviewer validates accuracy
   → Points awarded: +8 per skill per language on merge

4. Issue resolution (skill flagged for review, you fix it)
   → Manual: maintainer confirms fix resolves the flagged issue
   → Points awarded: +5 per resolved flag
```

*MIT License · SportMind · sportmind.dev*
