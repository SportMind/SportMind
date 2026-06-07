---
name: agent-failure-modes
description: >
  Verified cases where AI agents reasoning about sports without SportMind's
  framework produce incorrect or misleading outputs. All six cases are drawn
  from SportMind's calibration history and SMI operational record. Includes
  prevention framework. Library Rule: PASSES — failure modes are enduring
  patterns; specific cases are historical reference points for the patterns.
---

# Agent Failure Modes — Verified Cases

**Source:** SportMind calibration history and SMI operational record.
**Purpose:** An agent that knows how it fails is more reliable than one that does not.

---

## Overview

These are not theoretical failures. They are verified cases from SportMind's
operational history — documented precisely so agents and developers can
recognise and prevent each pattern before it propagates.

Each failure mode has three components:
- The error that occurred and what caused it
- The SportMind correction applied
- The lesson: the enduring reasoning principle the case demonstrates

The six cases below cover the highest-risk failure categories in sports
intelligence reasoning: venue misclassification, player hallucination, FTP
mechanics misapplication, stale gap state, proper noun leakage, and
confidence inflation.

---

## Failure Mode 1 — Neutral Venue Error

```
CASE:       UCL Final 2026 — PSG vs Arsenal
VENUE:      Puskás Aréna, Budapest (neutral ground)
UEFA LABEL: PSG designated HOME — administrative only

ERROR:
  Applying a home advantage modifier to PSG based on UEFA's administrative
  HOME designation for a neutral venue fixture.
  An agent without the neutral_venue flag would have inflated the signal
  beyond the correct 55 (T-48h) → 58 (T-2h).

WHAT AN AGENT WITHOUT THE FLAG WOULD DO:
  Apply home advantage modifier (×1.06–1.12) to PSG's adjusted score.
  Produce an inflated signal that overstates PSG structural advantage.
  Misrepresent "administrative HOME" as "structural home ground advantage."

SPORTMIND CORRECTION:
  neutral_venue: true flag set at Step 1 of pre-match signal framework.
  home_advantage_modifier = 0 (not ×1.00 — it is zero, not standard).
  Signal correctly assessed at MEDIUM confidence, adjusted score 55 → 58.
  Administrative HOME ≠ structural home. They are different signals.

LESSON:
  Always verify venue type before applying any home advantage modifier.
  Check: is this the club's registered home ground?
  If NO → neutral_venue = true → home_advantage_modifier = 0.
  Administrative designation and structural advantage are categorically
  different — treating them as equivalent inflates every neutral venue signal.
```

**Reference:** `calibration/2026/ucl-final-psg-vs-arsenal-2026-05-30.md` (Record #130)

---

## Failure Mode 2 — Hallucinated Player

```
CASE:       UCL Final T-2h SMI briefing — 2026-05-30
ERROR TYPE: Named player hallucination

ERROR:
  SMI listed "Neymar (PSG): Doubtful — monitor" in the T-2h squad update.
  Neymar has not been a PSG player since August 2023.
  He plays for Santos FC in Brazil.
  The output was generated without verification against PSG's official squad.

ROOT CAUSE:
  Language model training data included Neymar as a PSG player for many years.
  Without primary source verification, the model surfaced this association
  as a current squad fact.

SPORTMIND CORRECTION:
  Standing instruction applied: never include a named player without verifying
  against the official club website (Tier 1 source).
  Named player signals require: official squad page, club social media, or
  pre-match press conference confirmation.
  No named player → no athlete modifier.

LESSON:
  Player existence in a squad must be verified from a primary source before
  any athlete modifier is applied.
  Confident-sounding hallucinations about named players are the highest
  risk category in athlete intelligence.
  Training data associations about players are not current squad facts.
  The LibraryRule equivalent for athlete signals:
  "Will this player still be at this club in six months?"
  If the answer requires a primary source check — check it.
```

**Reference:** `athlete/athlete-intelligence-framework.md` — Step 1 (availability verification)

---

## Failure Mode 3 — FTP LOSS/MINT Error

```
CASE:       UCL Final 2026 — $AFC PATH_2 outcome
ERROR TYPE: FTP mechanics misapplication

ERROR:
  SportMind and SMI both initially documented the UCL Final $AFC PATH_2
  outcome as: LOSS → MINT EVENT · ~111,500 $AFC minted to treasury.
  This was filed in the calibration record and distributed in SMI briefings.

ACTUAL OUTCOME: DRAW → NO CHANGE
  90-minute score: 1-1 (DRAW)
  FTP PATH_2 settles on the 90-MINUTE RESULT ONLY.
  Extra time, penalty shootouts, and golden goals are NOT included.
  PSG winning 4-3 on penalties is irrelevant to FTP mechanics.
  $AFC supply change: 0 burned, 0 minted.

ROOT CAUSE:
  The 90-minutes play rule was not documented in the library.
  The agent reasoned from the match outcome (PSG win) rather than
  the FTP settlement rule (90-minute score only).

SPORTMIND CORRECTION:
  90-MINUTES PLAY RULE added to fan-token/ftp-path2.md:
    "All match markets are based on the result at the end of a scheduled
    90 minutes of play unless otherwise stated. This includes any added
    injury or stoppage time but does NOT include extra time, time allocated
    for a penalty shootout, or a golden goal."
    Source: fantokens.com/fan-token-play (official primary source)
  Calibration record #130 corrected: LOSS/MINT → DRAW/NO CHANGE.
  Direction verdict (CORRECT ✓) unchanged — PSG was predicted, PSG won.

LESSON:
  FTP mechanics must always be verified against the official rule specification
  at fantokens.com/fan-token-play before any supply event outcome is documented.
  Penalty shootout results never affect FTP PATH_2 settlement.
  For knockout matches: ask "what is the 90-minute score?" not "who won?"
  The two questions have different answers in extra time matches.
```

**Reference:** `fan-token/ftp-path2.md` — 90-MINUTES PLAY RULE section

---

## Failure Mode 4 — Stale Gap State

```
CASE:       CONSORTIUM_COLLAPSE gap — May 2026
ERROR TYPE: Agent acting on a closed gap

ERROR:
  SMI repeatedly flagged the Sevilla consortium collapse as a library gap
  (labelled FILLS KNOWN GAP) across multiple briefings in May 2026.
  The CONSORTIUM_COLLAPSE framework had been built at v3.97.83 (L101)
  three weeks before the repeated gap recommendations.
  The agent's internal state of known gaps had not been updated after release.

CONSEQUENCE:
  Redundant processing on a closed gap.
  False gap recommendations consuming briefing attention.
  Reduced trust in gap detection overall.

SPORTMIND CORRECTION:
  Combined SMI state update sent after each major release cycle.
  Agent state update protocol: after every library release, refresh the
  list of known gaps before producing any gap recommendations.

LESSON:
  An agent's internal state about what gaps exist must be updated after
  every library release before producing gap recommendations.
  An agent acting on a closed gap wastes processing and produces
  redundant recommendations that reduce signal quality.
  The check: before flagging a gap, verify the gap is not already addressed
  in the current version of the library.
```

**Reference:** `CONTRIBUTING-GAPS.md` — gap intake and closure protocol

---

## Failure Mode 5 — Proper Noun Leakage

```
CASE:       Multiple SMI briefings — May–June 2026
ERROR TYPE: Expiring data proposed as library content

ERROR:
  SMI repeatedly recommended library additions whose primary value signal
  was a proper noun: specific player names, specific club current status,
  specific match scores, specific regulatory official names.
  Examples from the operational record:
    "Add Mbappe departure impact framework" (player-specific, expiring)
    "Add Arsenal PL Champions 2025/26 status" (season-specific, expiring)
    "Add this week's referee assignments" (match-specific, expiring)
  All fail the proper noun test.

SPORTMIND CORRECTION:
  Proper noun test applied to every signal before library recommendation:
    "Remove all proper nouns from the proposed addition.
    If no value remains — it is briefing content only, not a library addition."
  Enduring frameworks extracted where possible:
    "Player departure impact" → generic succession intelligence framework
    "Championship status CDI impact" → generalised CDI trajectory modifier
    "Referee pattern" → referee intelligence framework (not specific assignments)

LESSON:
  The most common failure mode in library curation is adding expiring data
  dressed as enduring intelligence.
  Proper noun test procedure:
    Step 1: Remove all named people, clubs, scores, and seasons.
    Step 2: Does the statement still contain value?
    Step 3: If YES → candidate for library. If NO → briefing only.
  Named players fail. Named clubs in current context fail.
  Reasoning patterns about player types, club situations, and competition
  contexts pass.
```

**Reference:** `core/SPORTMIND.md` — Library Rule and proper noun test

---

## Failure Mode 6 — Confidence Inflation

```
CASE:       General pattern — calibration records analysis
ERROR TYPE: Default HIGH confidence without earned conditions

ERROR:
  Agents without HOLD gate training assign HIGH confidence signals even
  when key inputs are missing:
    · Lineup unconfirmed at T-48h → HIGH confidence assigned anyway
    · Macro regime unclear (ANXIETY) → HIGH confidence assigned anyway
    · Athlete availability unknown → HIGH confidence assigned anyway
  This is more dangerous than a lower confidence signal because it
  suppresses the flags the downstream user needs to see.

VERIFIED PATTERN:
  Analysis of pre-v3.97.80 calibration records shows a systematic
  pattern of HIGH confidence assignments that were later downgraded
  when lineup confirmation arrived at T-2h and changed the signal.
  Confidence must be earned by the completeness of information loaded.

SPORTMIND CORRECTION:
  Explicit confidence tier system with defined downgrade conditions:
    HIGH:        SMS 100 · lineup confirmed · no unresolved flags
    MEDIUM-HIGH: SMS 100 · minor flags (one doubtful player)
    MEDIUM:      SMS 80–100 · lineup unconfirmed · or neutral venue
    LOW:         SMS < 80 · or multiple unresolved flags
  HOLD gate fires when: SMS < 80 · OR · MACRO_OVERRIDE_ACTIVE · OR
    critical flags unresolved.
  An INCOMPLETE output is returned rather than a low-quality HIGH signal.

LESSON:
  Confidence must be earned from the completeness of information loaded —
  not assigned by default.
  An agent that says HIGH confidence when lineup is unconfirmed is more
  dangerous than one that says MEDIUM and flags the gap.
  The user needs to know what is uncertain — confident-sounding outputs
  that conceal uncertainty are a failure mode, not a feature.
```

**Reference:** `core/pre-match-signal-framework.md` — Step 7, confidence level rules

---

## Prevention Framework

Six conditions that prevent the failure modes above. Apply before every signal.

```
CONDITION 1 — VERIFY VENUE TYPE
  Before applying any home advantage modifier:
  Is this the club's registered home ground? YES or NO.
  If NO: neutral_venue = true · home_advantage_modifier = 0.
  Never rely on administrative designation as structural advantage.
  Reference: Failure Mode 1

CONDITION 2 — VERIFY PLAYER EXISTENCE
  Before applying any athlete modifier:
  Is this player currently registered at this club?
  Verify from: official club website (Tier 1) or official squad list.
  No verification → no named player reference → no athlete modifier.
  Reference: Failure Mode 2

CONDITION 3 — VERIFY FTP RULE SPECIFICATION
  Before documenting any supply event outcome:
  What is the 90-minute score? (Not: who won the match.)
  Verify against fantokens.com/fan-token-play.
  Penalty shootout results never affect FTP PATH_2 settlement.
  Reference: Failure Mode 3

CONDITION 4 — UPDATE INTERNAL STATE
  Before producing any gap recommendations:
  Has the library been updated since the last gap list was generated?
  If YES: refresh the known gap list before recommending additions.
  Reference: Failure Mode 4

CONDITION 5 — APPLY PROPER NOUN TEST
  Before recommending any library addition:
  Remove all proper nouns (named people, clubs, seasons, scores).
  Does value remain? YES → library candidate. NO → briefing only.
  Reference: Failure Mode 5

CONDITION 6 — EARN CONFIDENCE
  Before assigning any confidence tier:
  Is SMS 100? Is lineup confirmed? Are flags resolved?
  Assign the confidence tier the evidence supports — not the one
  the output looks most authoritative at.
  When in doubt: downgrade confidence, not the flag.
  Reference: Failure Mode 6
```

---

## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Documents failure patterns in sports intelligence reasoning — the meta-intelligence layer |
| Reasoning | ACTIVE | Each failure mode includes the incorrect reasoning chain and the correct replacement |
| Context | ACTIVE | All six cases are contextualised with the specific match, briefing, or pattern that generated the failure |
| Memory | ACTIVE | Failure pattern recognition requires memory of prior errors — this file IS that memory |
| Judgment | ACTIVE | Prevention framework is a judgment checklist — six conditions applied before every signal |
| Attention | ACTIVE | Each failure mode identifies the specific attention failure: what the agent did not check |
| Communication | ACTIVE | Failure modes must be communicated clearly to developers and agents loading this file |
| Verification | ACTIVE | Primary purpose — all six prevention conditions are verification gates |
| Learning | ACTIVE | This file is the learning artefact from operational errors — calibration-driven improvement |
| Integration | ACTIVE | Integrates with athlete framework (FM2), ftp-path2 (FM3), pre-match framework (FM6), SPORTMIND.md (FM5) |
| Calibration | ACTIVE | All six cases drawn from verified calibration records — record-based, not theoretical |
| Adaptation | ACTIVE | Framework adapts as new failure modes are identified from operational history |
| Ethics | ACTIVE | Honest disclosure of library and SMI failures — transparency about errors is an ethics requirement |
| Transparency | ACTIVE | Failures are named, sourced, and visible — no failure is hidden or described as a feature |

---

## Compatibility

**Prevention conditions apply to:** all pre-match signal production (`core/pre-match-signal-framework.md`)
**Athlete verification:** `athlete/athlete-intelligence-framework.md` — Step 1
**FTP mechanics:** `fan-token/ftp-path2.md` — 90-MINUTES PLAY RULE
**Library Rule and proper noun test:** `core/SPORTMIND.md`
**Confidence tier system:** `core/signal-confidence-framework.md`
**Gap reporting:** `CONTRIBUTING-GAPS.md`

---

*SportMind v4.0.0 · MIT License · sportmind.dev*
*Six verified failure modes. Six prevention conditions. All drawn from the operational record.*
*All 14 Mind dimensions mapped.*
