# Judo — SportMind Domain Skill

> **Status: BASIC** — Core signal framework established.
> Full expansion needed — see [GOOD_FIRST_ISSUES.md](../../GOOD_FIRST_ISSUES.md).
> Use [templates/template-new-sport-skill.md](../../templates/template-new-sport-skill.md) to expand.

---

## Overview

Olympic judo by weight category. IJF World Tour and Olympic Games.

**Fan token exposure:** No active Chiliz fan tokens as of v3.93.0.

---

## Domain Model

### Signal hierarchy

```
TIER 1 — PRIMARY SIGNAL:
  IJF World Ranking by weight category, technique repertoire vs opponent style

TIER 2 — CONTEXTUAL:
  Weight category management (cutting weight), home nation advantage (referee patterns)

EVENT CALENDAR:
  Olympic cycle (peak), IJF Grand Slam/Grand Prix monthly, World Championships annual
```

---

## Event Playbooks

### Playbook 1: Olympic judo final by weight category
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
| Intelligence | ACTIVE | Judo event playbook: weight category signals, ranking, technique preference, and draw |
| Reasoning | ACTIVE | Judo reasoning chain from ranking and head-to-head to bout outcome prediction |
| Context | ACTIVE | Judo context: weight category, IJF Grand Slam vs World Championship, Golden Score rules |
| Memory | ACTIVE | Historical judo championship patterns and weight category baselines |
| Judgment | ACTIVE | Judgment on judo signal hierarchy — IJF ranking and head-to-head are primary |
| Attention | ACTIVE | Elevated attention during World Championships and Olympic qualification |
| Communication | ACTIVE | Judo signal output with weight category, ranking context, and direction |
| Verification | ACTIVE | Judo data from IJF official sources |
| Learning | EMERGING | Judo calibration records are limited — stub sport |
| Integration | ACTIVE | Integrates with core sport domain framework |
| Calibration | EMERGING | Judo is a stub sport — limited calibration data |
| Adaptation | ACTIVE | Judo intelligence adapts as IJF ranking and rule changes evolve |
| Ethics | NOT APPLICABLE | Judo sport domain is factual analysis — no ethical dimension |
| Transparency | ACTIVE | Stub status and weight category context disclosed in output |
| Execution | ACTIVE | Six-step pre-match workflow, event playbooks, and command references defined |
| Collaboration | ACTIVE | Integrates with core frameworks, athlete intelligence, macro layer, and fan token registry |


---

> **Expand this skill:** See [GOOD_FIRST_ISSUES.md](../../GOOD_FIRST_ISSUES.md).
> This BASIC file covers core signal logic. A FULL file adds:
> calibration records, advanced modifiers, H2H framework, deeper playbooks.

*SportMind v3.93.0 · MIT License · sportmind.dev*
