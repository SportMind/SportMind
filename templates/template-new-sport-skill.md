# [Sport Name] — SportMind Domain Skill

<!--
  INSTRUCTIONS FOR CONTRIBUTORS
  ─────────────────────────────
  Replace every [PLACEHOLDER] with real content.
  Delete all instruction comments before submitting.
  Every section is required — do not skip any.
  Minimum 4 playbooks. Minimum 5 agent reasoning rules.
  Read CONTRIBUTING.md before starting.
-->

Sport-specific intelligence layer for [sport name] fan tokens and prediction markets.
Teaches AI agents how to reason about [sport] events, timing, risk, and outcome probability.

---

## Overview

<!--
  2–4 sentences describing:
  - What makes this sport unique from an AI agent's perspective
  - What promotions / leagues are covered
  - The key difference in how this sport drives token/prediction price vs other sports
-->

---

## Domain Model

### Season Calendar

<!--
  Table showing the full annual cycle with approximate dates and token behaviour notes.
  Include: pre-season, regular season, peak events, off-season, international windows.
-->

| Phase | Dates (approx) | Token / Prediction Behaviour |
|---|---|---|
| [Phase name] | [Month range] | [What happens to price/sentiment] |

**Rule:** [1–2 sentences on the most important calendar-based agent rule.]

### Event Hierarchy

<!--
  How events are ranked in this sport — what constitutes a tier 1 vs tier 2 vs tier 3 event.
  Include the formula or scoring logic if applicable.
-->

### Result Impact Matrix

<!--
  Table of result scenarios with average price/outcome impact.
  Use % ranges, not point estimates.
  Source your estimates from historical data where possible — note when estimating.
-->

| Result scenario | Token / market impact |
|---|---|
| [Scenario] | [+X – Y%] |

---

## Competition Reference

### [Primary Competition Name]
- [Key facts: format, number of teams, season length]
- [Relevant tokens or prediction markets]
- [Highest-impact events within this competition]

### [Secondary Competition Name]
- [Key facts]
- [Token / market relevance]

### [Tier 3 — if applicable]
- [Lower impact events to monitor for sentiment only]

---

## Sport-Specific Risk Variables

<!--
  The risk variables that are UNIQUE to this sport — things that have no equivalent
  in football or any other sport. Each one needs a token/prediction impact table.
  Minimum 3 distinct risk variables.
-->

### [Risk Variable 1 — e.g., "Weigh-In Risk" for MMA]

[Brief explanation of what this is and why it matters for agents.]

| [Risk event] | Token / market impact |
|---|---|
| [Outcome A] | [+/- X%] |
| [Outcome B] | [+/- Y%] |

**Agent rule:** [One clear sentence on how agents should handle this risk.]

### [Risk Variable 2]

[Same structure.]

### [Risk Variable 3]

[Same structure.]

---

## Event Playbooks

<!--
  Minimum 4 playbooks. Each must have all 6 fields.
  Write playbooks as executable strategies an agent could follow directly.
-->

### Playbook 1: [Name]
```
trigger:  [What condition fires this playbook]
entry:    [When and how to enter]
exit:     [When and how to exit]
filter:   [Conditions that must be true before entry]
sizing:   [Position size relative to standard — e.g., 1.0×, 1.5×, 0.5×]
note:     [One important nuance or warning]
```

### Playbook 2: [Name]
```
trigger:  
entry:    
exit:     
filter:   
sizing:   
note:     
```

### Playbook 3: [Name]
```
trigger:  
entry:    
exit:     
filter:   
sizing:   
note:     
```

### Playbook 4: [Name]
```
trigger:  
entry:    
exit:     
filter:   
sizing:   
note:     
```

<!--
  Add more playbooks if the sport has important edge cases not covered above.
-->

---

## Signal Weight Adjustments

<!--
  How should agents weight the 5 signal components for this sport specifically?
  Explain why each weight is recommended.
-->

For [sport], agents should apply these interpretive weights to composite signal scores:

| Component | Recommended weight | Rationale |
|---|---|---|
| Market / whale flows | [X%] | [Why] |
| Social sentiment | [X%] | [Why] |
| Sports catalyst | [X%] | [Why] |
| Price trend | [X%] | [Why] |
| Macro | [X%] | [Why] |

---

## Key Commands

<!--
  Map the key agent actions for this sport to the commands available in the ecosystem.
  Reference real skill names from SportMind or Fan Token™ Intel.
-->

| Action | Skill | Command | Use case |
|---|---|---|---|
| [What the agent needs to do] | [Which skill] | [Command name] | [When to use it] |

---

## Agent Reasoning Prompts

<!--
  5–8 numbered rules an agent should follow when reasoning about this sport.
  Write these as if they are instructions in a system prompt.
  Be specific and actionable — avoid generic statements.
-->

```
You are a [sport] sports intelligence agent. Before evaluating any [sport] event:

1. [First and most important rule]
2. [Second rule]
3. [Third rule]
4. [Fourth rule]
5. [Fifth rule]
6. [Sixth rule — if applicable]
7. [Seventh rule — if applicable]
8. [Eighth rule — if applicable]
```

---

## Data Sources

<!--
  List the key data sources for this sport — where an agent or developer would
  find the data to power the signals referenced in this skill.
-->

- [Data type]: [Source name and URL if applicable]
- [Data type]: [Source]

---

## Compatibility

<!--
  Which other SportMind skills or external skills complement this one.
  Note which athlete skill pairs with this domain skill.
-->

**Pairs with athlete skill:** `athlete/[sport]`

**Recommended core skills:**
- `[skill-name]` — [why]
- `[skill-name]` — [why]

**Optional:**
- `[skill-name]` — [why]

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | [Date] | Initial release |

---

*Contributed by [Your GitHub handle] · MIT License · sportmind.dev*
