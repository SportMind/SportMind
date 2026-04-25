# Taekwondo — SportMind Domain Skill

> **Status: BASIC** — Core signal framework established.
> Full expansion needed — see [GOOD_FIRST_ISSUES.md](../../GOOD_FIRST_ISSUES.md).
> Use [templates/template-new-sport-skill.md](../../templates/template-new-sport-skill.md) to expand.

---

## Overview

Olympic taekwondo by weight category. WT World Tour.

**Fan token exposure:** No active Chiliz fan tokens as of v3.93.0.

---

## Domain Model

### Signal hierarchy

```
TIER 1 — PRIMARY SIGNAL:
  Kick variety and scoring frequency, weight category ranking differential

TIER 2 — CONTEXTUAL:
  Head kick vs body kick scoring ratio, penalty accumulation pattern

EVENT CALENDAR:
  Olympic cycle (peak), WT Grand Prix, World Championships annual
```

---

## Event Playbooks

### Playbook 1: Olympic taekwondo final by weight category
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

---

> **Expand this skill:** See [GOOD_FIRST_ISSUES.md](../../GOOD_FIRST_ISSUES.md).
> This BASIC file covers core signal logic. A FULL file adds:
> calibration records, advanced modifiers, H2H framework, deeper playbooks.

*SportMind v3.93.0 · MIT License · sportmind.dev*
