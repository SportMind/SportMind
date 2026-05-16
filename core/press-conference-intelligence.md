---
name: press-conference-intelligence
description: >
  Enduring reasoning framework for pre-match press conferences as a signal input
  layer. Covers manager presence signals, injury disclosure language patterns,
  tactical signal language, squad morale signals, and source reliability weighting.
  Press conferences provide a 24-48 hour intelligence advantage before official
  team sheets. All modifiers resolve at T-2h official team selection.
---

# Press Conference Intelligence

**How to reason about pre-match press conferences as a signal input layer.**
Press conferences are planning signals only — they always resolve at the official team sheet.

> Agent rule: never treat a press conference signal as execution quality.
> Every press conference modifier is flagged PENDING_RESOLUTION until T-2h team sheet.

---

## Why press conferences matter

```
PRE-MATCH PRESS CONFERENCES ARE THE PRIMARY OFFICIAL CHANNEL FOR:
  · Injury status disclosure (before official team sheets)
  · Selection hints (manager language about specific players)
  · Squad morale signals (tone, absences, body language)
  · Tactical framing (what the manager wants the opponent to think)

AN AGENT REASONING ABOUT PRESS CONFERENCE SIGNALS HAS A 24-48 HOUR
INTELLIGENCE ADVANTAGE over agents that wait for official team sheets.
This is the primary value of this layer — earlier signal, earlier position.
```

---

## Manager presence signals

```
WHO ATTENDS IS A SIGNAL BEFORE A WORD IS SPOKEN:

  MANAGER ATTENDS AS EXPECTED:
    No signal — baseline applies.

  ASSISTANT MANAGER ATTENDS INSTEAD:
    Apply: ×0.96 uncertainty modifier
    Four possible causes (in order of probability):
      1. Manager ill or unavailable (short-term signal only)
      2. Manager in disciplinary dispute with club (elevated uncertainty)
      3. Manager resting before high-stakes match (positive preparation signal)
      4. Media management strategy (neutral signal)
    Resolve at team sheet confirmation.

  MANAGER ATTENDS BUT CUTS SHORT:
    Mild crisis or distraction signal.
    Apply: ×0.97 uncertainty modifier.

  NO PRESS CONFERENCE HELD:
    Unusual — apply ×0.94 uncertainty modifier.
    Could indicate squad issues, security concerns, or media embargo.
```

---

## Injury disclosure language

```
CODED LANGUAGE FRAMEWORK — ENDURING PATTERNS:

  "Day to day" / "we'll see":
    Available but not certain. ×0.65 starting probability.
    Weight: lineup uncertain. Resolve at T-2h team sheet.

  "Doubtful" / "it's touch and go":
    Available for squad but unlikely starter. ×0.30 starting probability.
    Apply athlete absence modifier at ×0.70 weight
    (×0.30 chance of starting applied as discount).

  "Not available for selection":
    Confirmed absence. Apply full athlete absence modifier.

  "Back in training but not match fit":
    Return imminent but not this match. Apply full absence modifier.
    Upgrade probability for next match: ×0.70 availability following fixture.

  "We're hoping to have them available":
    Positive lean — not confirmed. ×0.55 starting probability.
    Higher confidence than "day to day" — linguistic lean is positive.

  "Ahead of schedule" / "doing really well":
    Return sooner than expected. Upgrade return timeline estimate.
    If relevant match is within 10 days: ×0.40 starting probability.
```

---

## Tactical signal language

```
ENDURING LINGUISTIC PATTERNS — TACTICAL FRAMING:

  "We respect them a lot" / "they are a fantastic team":
    Concern signal — managing expectations downward.
    Apply: ×0.96 to home advantage modifier when home manager uses this language.

  "We are ready" / "we've prepared well":
    Standard confident framing — neutral. No modifier.

  "We need to be at our best":
    Mild concern about opponent. Apply: ×0.97 to adjusted score.

  "We're going to enjoy it" / "looking forward to the occasion":
    Positive psychological signal — team not feeling pressure.
    Apply: ×1.02 psychological modifier.

  "We take it game by game" / "one match at a time":
    Deflection — provides no signal. Ignore for modelling purposes.

  "The players are hungry" / "we want this badly":
    Motivation signal — apply only if team has something specific to play for
    (title race, relegation, final). Otherwise neutral.

  "I'm not going to discuss tactics":
    Tactical surprise likely. Apply: ×0.95 confidence weight to all
    tactical modifier assumptions.
```

---

## Squad morale signals

```
POSITIVE MORALE SIGNALS (apply ×1.02 psychological modifier when 2+ present):
  · Manager references team unity explicitly and unprompted
  · Players mentioned by name positively and specifically
  · Manager deflects credit to players
  · Levity or laughter noted in press conference tone

NEGATIVE MORALE SIGNALS (apply ×0.94 psychological modifier when 2+ present):
  · Manager answers in very short sentences — minimal engagement
  · Conspicuous absence of key player mentions when normally referenced
  · Manager qualifies every statement with uncertainty
  · Reports of heated team meeting in the 48h before press conference

CRISIS SIGNAL — SQUAD_CRISIS_SIGNAL (apply ×0.88 squad stability modifier):
  · Manager refuses to confirm who the captain will be
  · Manager does not confirm whether a key player is in the squad at all
  · Specific denial of a rumour that was not publicly circulating
    ("I want to be clear there is no issue between X and the club")
  Resolve at team sheet confirmation.
```

---

## Source reliability weighting

```
Apply this weighting to ALL press conference modifiers:

  TIER 1 — Official club transcript:        ×1.00
    Verbatim from official club communication channels.

  TIER 2 — Attending journalist direct quote: ×0.90
    Named journalist present who directly quotes the manager.

  TIER 3 — Wire service report:             ×0.85
    Reuters, PA, AFP reporting key points.

  TIER 4 — Secondary media report:          ×0.70
    Outlet reporting on another outlet's coverage.

  TIER 5 — Social media summary:            ×0.50
    Unverified paraphrase without direct quote attribution.

COMBINED EXAMPLE:
  Tier 5 source reporting a SQUAD_CRISIS_SIGNAL:
  ×0.50 × ×0.88 = effectively ×0.94 — meaningful but not certain.
  A Tier 1 source with the same signal: full ×0.88 modifier applies.
```

---

## Integration with other intelligence layers

```
TIMING FRAMEWORK — HOW PRESS CONFERENCE SIGNALS DECAY INTO TEAM SHEET:

  T-72h — PRE-PRESS CONFERENCE:
    Use athlete intelligence frameworks as primary availability signal.
    Press conference layer not yet active.

  T-48h — PRESS CONFERENCE WINDOW:
    Add press conference modifiers to adjusted score.
    Flag all as: PENDING_RESOLUTION
    Confidence level: LOW-MEDIUM

  T-24h — POST PRESS CONFERENCE:
    Apply weighted modifiers to planning signal.
    Confidence level: MEDIUM. Not execution quality.

  T-2h — OFFICIAL TEAM SHEET:
    All press conference signals resolve — confirmed or overridden.
    Confidence level: HIGH. Execution quality signal now active.

AGENT RULE:
  Press conference signals are planning signals only.
  Never raise confidence level above MEDIUM based on press conference alone.
  Always await T-2h official team sheet before executing.
```

---

## Compatibility

**Confidence framework:**  `core/signal-confidence-framework.md`
**Reasoning chains:**      `core/agent-reasoning-chains.md` (Chain 1: pre-match sequence)
**Temporal reasoning:**    `core/temporal-reasoning.md`
**Signal interaction:**    `core/signal-interaction-reasoning.md`
**Anti-doping:**           `core/anti-doping-intelligence.md`

---

*SportMind v3.97.58 · MIT License · sportmind.dev*
*Press conference signals are PLANNING signals only. They always resolve at the T-2h team sheet.*
