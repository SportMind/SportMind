# Curling — SportMind Domain Skill

> **Status: BASIC** — Core signal framework established.
> Full expansion needed — see [GOOD_FIRST_ISSUES.md](../../GOOD_FIRST_ISSUES.md).
> Use [templates/template-new-sport-skill.md](../../templates/template-new-sport-skill.md) to expand.

---

## Overview

Olympic and World Championship curling. Mixed doubles and four-player team formats.

**Fan token exposure:** No active Chiliz fan tokens as of v3.93.0.

---

## Domain Model

### Signal hierarchy

```
TIER 1 — PRIMARY SIGNAL:
  Steal percentage, force/blank ratio, hammer efficiency (scoring with last stone advantage)

TIER 2 — CONTEXTUAL:
  Ice conditions and pebble wear over game duration, skip experience at end position

EVENT CALENDAR:
  Olympic cycle (peak), World Men's/Women's Championship annual, Grand Slam circuit
```

---

## Event Playbooks

### Playbook 1: Olympic final or World Championship final — hammer advantage analysis
```
trigger: championship_event_confirmed
entry:   -24h window (pre-event analysis)
exit:    +2h post result
filter:  ranking_data_available, no_withdrawal_flag
sizing:  standard
```

### Playbook 2: Major championship medal event
```
trigger: olympic_or_world_championship_final
entry:   -6h window
exit:    +1h post result
filter:  signal_score > 55
sizing:  standard
```

### Playbook 3: Season ranking signal
```
trigger: ranking_affecting_competition
entry:   -12h window
exit:    +1h post result
filter:  qualification_context_active
sizing:  reduced
```

### Playbook 4: Athlete withdrawal
```
trigger: confirmed_withdrawal_tier1_source
entry:   immediate on confirmation
exit:    signal_reload_complete
filter:  tier1_source_confirmed
sizing:  hold_until_reload
```

---

## Signal Weight Adjustments

| Modifier | Weight | Notes |
|---|---|---|
| Tier 1 ranking differential | Primary | World ranking vs opponent |
| Conditions / surface match | Secondary | Apply when documented impact |
| Athlete availability | Binary | Withdrawal = signal reload |
| Championship pressure | Tertiary | Olympic final vs regular event |

---

## Key Commands

| Action | Skill | Notes |
|---|---|---|
| Pre-event signal | Load this file + `core/sportmind-score.md` | Ranking differential first |
| Athlete withdrawal | `core/breaking-news-intelligence.md` | Category 2 event |
| Olympic final | Playbook 2 | Peak event protocol |
| Season ranking impact | Playbook 3 | Qualification context |

---

## Agent Reasoning Prompts

- "Check Tier 1 ranking differential before any other modifier for this sport."
- "Conditions modifier — confirm documented impact before applying."
- "Athlete withdrawal confirmed: Category 2 — reload signal immediately."
- "Olympic final context: highest championship modifier applies."

---

## Fan Token Notes

No active Chiliz fan tokens as of v3.93.0.

**This sport is a candidate for future fan token coverage.** If a token launches,
load `fan-token/fan-token-lifecycle/fan-token-lifecycle.md` immediately and
establish CDI baseline within the first 72 hours (Phase 2 launch window).

---

## Data Sources

- Sport governing body official website (Tier 1 — rankings, results)
- Olympic Channel / OBS: official broadcast data (Tier 1)
- Athlete/team official accounts (Tier 2 — form and availability)

---

## Calibration

No calibration records — seeking first contributor.

---

## Compatibility

**Core:** `core/sportmind-score.md` · `core/athlete-modifier-system.md`
**Breaking news:** `core/breaking-news-intelligence.md`
**Macro:** `macro/macro-crypto-market-cycles.md`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Curling event playbook: draw weight, ice conditions, skip profile, and end strategy |
| Reasoning | ACTIVE | Curling reasoning chain from team profile and conditions to outcome prediction |
| Context | ACTIVE | Curling context: ice conditions, hammer advantage, draw weight reputation |
| Memory | ACTIVE | Historical curling outcome patterns and team profile baselines |
| Judgment | ACTIVE | Judgment on curling signal hierarchy — skip quality and hammer possession are primary |
| Attention | ACTIVE | Elevated attention during World Championships and Olympic qualification rounds |
| Communication | ACTIVE | Curling signal output with team profile and ice conditions modifier |
| Verification | ACTIVE | Curling data from World Curling Federation official sources |
| Learning | EMERGING | Curling calibration records are limited — stub sport |
| Integration | ACTIVE | Integrates with core sport domain framework |
| Calibration | EMERGING | Curling is a stub sport — limited calibration data |
| Adaptation | ACTIVE | Curling intelligence adapts as competitive landscape evolves |
| Ethics | NOT APPLICABLE | Curling sport domain is factual analysis — no ethical dimension |
| Transparency | ACTIVE | Stub status and limited calibration data disclosed in output |


---

> **Expand this skill:** See [GOOD_FIRST_ISSUES.md](../../GOOD_FIRST_ISSUES.md).
> This BASIC file covers core signal logic. A FULL file adds:
> calibration records, advanced modifiers, H2H framework, deeper playbooks.

*SportMind v3.93.0 · MIT License · sportmind.dev*
