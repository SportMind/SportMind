# SportMind Benchmark

**Does loading SportMind intelligence actually improve an AI agent's reasoning?**

This benchmark answers that question with a reproducible, public test.

It compares two configurations on identical sports scenarios:

- **SportMind + LLM** — the LLM receives the correct SportMind skill stack for the scenario
- **Vanilla LLM** — the same LLM receives no SportMind context, only the raw question

Both configurations are asked to predict the same outcomes. Results are compared
against verified historical results. The accuracy difference is the measured
value SportMind adds.

---

## Methodology

### Why this approach is valid

The comparison is fair because:

- Both configurations use the same LLM (Claude Sonnet by default)
- Both receive identical scenario descriptions
- Neither has access to the outcome at prediction time
- All scenarios use completed historical events with verified results
- Scenarios were selected before running any tests (no cherry-picking)

### What is measured

**Direction accuracy** — did the signal point the right way?
For match outcomes: HOME/AWAY/DRAW correct.
For fan token signals: ENTER/WAIT/ABSTAIN against 24h post-event price move.

**Modifier identification** — did the model identify the key signal variable?
SportMind teaches specific named modifiers (dew_factor, qualifying_delta, etc.).
Vanilla LLM is scored on whether it identifies the same variable unprompted.

### Scenario selection criteria

Scenarios were chosen to test SportMind's specific claimed advantages:

1. **Domain-specific knowledge** — does SportMind know what vanilla LLMs don't?
   (e.g. MMA weight miss implications, cricket dew factor, F1 qualifying delta)

2. **Multi-layer reasoning** — does combining layers improve over single-layer?
   (e.g. macro + athlete + domain together vs any one alone)

3. **Counter-intuitive outcomes** — cases where naive analysis gets it wrong
   (e.g. favourite loses due to SportMind-modelled risk variable)

4. **Fan token signals** — commercial intelligence not present in general training
   (e.g. tokenomics lifecycle phase, supply mechanics)

Scenarios are distributed across 8 sports, 3 difficulty tiers, and multiple
signal types to prevent any single sport or scenario type dominating the results.

### Avoiding bias

- All scenarios use completed events from 2023–2026
- Outcomes are publicly verifiable via the source URLs in each scenario file
- Scenarios include SportMind **incorrect** predictions (the 5 wrong records)
  to prevent the test set from being accuracy-inflated
- The test harness is open source — anyone can re-run it and verify results

---

## Test set structure

```
community/benchmark/
  README.md                    This file
  scenarios/                   40 test scenarios across 8 sports
    football/                  12 scenarios
    cricket/                   8 scenarios
    mma/                       6 scenarios
    formula1/                  6 scenarios
    basketball/                3 scenarios
    ice-hockey/                2 scenarios
    tennis/                    2 scenarios
    rugby-union/               1 scenario
  scripts/
    run_benchmark.py           Main runner — calls Claude API for both configs
    score_results.py           Scoring logic and accuracy table generation
    generate_report.py         Produces the results markdown report
  results/
    latest.json                Most recent full run results
    latest-report.md           Human-readable results table
    history/                   Previous run archives
```

---

## Running the benchmark

### Prerequisites

```bash
pip install anthropic aiohttp python-dotenv
export ANTHROPIC_API_KEY=your_key_here
```

### Run

```bash
cd community/benchmark/scripts
python run_benchmark.py --sport all --config both
```

Options:
```
--sport     football|cricket|mma|formula1|basketball|all  (default: all)
--config    sportmind|vanilla|both                         (default: both)
--model     claude-sonnet-4-20250514                      (default)
--output    path/to/results.json                          (default: results/latest.json)
--scenarios path/to/custom/scenarios/dir
```

### Expected runtime

~15–25 minutes for the full 40-scenario run (both configs).
Per-sport runs take 3–8 minutes.

---

## Current results

See `results/latest-report.md` for the most recent run.

### Summary table (last run)

| Sport | SportMind accuracy | Vanilla accuracy | Delta |
|---|---|---|---|
| Football | — | — | — |
| Cricket | — | — | — |
| MMA | — | — | — |
| Formula 1 | — | — | — |
| Basketball | — | — | — |
| Ice Hockey | — | — | — |
| Tennis | — | — | — |
| Rugby Union | — | — | — |
| **Overall** | **—** | **—** | **—** |

*Run the benchmark to populate this table.*

---

## Scenario format

Each scenario is a JSON file with this structure:

```json
{
  "scenario_id": "football-ucl-final-2023",
  "sport": "football",
  "difficulty": "standard",
  "signal_type": "match_outcome",
  "event": {
    "name": "UEFA Champions League Final 2023 — Manchester City vs Inter Milan",
    "date": "2023-06-10",
    "competition": "UEFA Champions League Final",
    "venue": "Atatürk Olympic Stadium, Istanbul"
  },
  "context": {
    "home_team": "Manchester City",
    "away_team": "Inter Milan",
    "pre_match_notes": "Man City treble bid. Guardiola's fourth UCL final. Haaland 36 goals in debut season. Inter organised but Tier 2 opponent in this context."
  },
  "sportmind_skills": [
    "macro/macro-overview.md",
    "sports/football/sport-domain-football.md",
    "athlete/football/athlete-intel-football.md",
    "core/confidence-output-schema.md"
  ],
  "question": "Predict the match direction (HOME/AWAY/DRAW) and explain the key signal variables.",
  "verified_outcome": {
    "result": "HOME_WIN",
    "direction": "HOME",
    "score": "1-0",
    "source_url": "https://www.uefa.com/uefachampionsleague/match/2031146",
    "key_variable": "narrative_modifier — treble bid momentum at maximum"
  },
  "scoring": {
    "direction_correct_if": "HOME",
    "key_variable_identified_if": ["narrative momentum", "treble", "Guardiola", "momentum"]
  }
}
```

---

## Contributing scenarios

Scenarios must meet these criteria to be added:

1. **Completed event** — outcome publicly verifiable
2. **Pre-2026** — older events reduce LLM training data recency advantage
3. **Clear direction** — outcome maps to HOME/AWAY/DRAW or ENTER/WAIT/ABSTAIN
4. **SportMind-relevant** — tests a specific SportMind modifier or layer
5. **No data contamination** — do not use events from the calibration records set

Submit via PR to `community/benchmark/scenarios/`.

---

*MIT License · SportMind · sportmind.dev*
*See also: community/calibration-data/ · community/accuracy-tracking.md*
