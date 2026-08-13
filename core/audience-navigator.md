---
name: audience-navigator
description: >
  Framework for identifying and serving seven distinct audience profiles
  plus a custom profile template. Shapes agent output framing, depth,
  format, and emphasis based on who is receiving the signal — without
  changing signal conclusions. Load when audience type is known or
  inferable from context.
sources: [chat]
---

# Audience Navigator

**Domain:** core/audience-navigator.md
**Version:** v4.5.1
**Library Rule:** Six-Month Test PASSES · Proper Noun Test PASSES
**Layer:** Core reasoning — communication and output layer
**Last updated:** 2026-08-13

---

## Purpose and Scope

The Audience Navigator shapes how signal output is framed — not what
the signal concludes. It exists because the same pre-match intelligence
is consumed by retail holders, programmatic systems, compliance teams,
journalists, developers, and community managers. Each group needs the
same underlying signal delivered in a radically different format.

What this file does:
- Identifies seven named audience profiles and a custom template
- Specifies output format rules, emphasis priorities, and agent rules
  for each profile
- Provides a custom profile template for unrecognised audience types
- Governs communication style, not signal generation

What this file does not do:
- Change signal conclusions
- Override HOLD gates
- Modify confidence tiers
- Change which files are loaded in the signal chain
- Produce trading advice

Load this file when the audience type is known or can be reasonably
inferred from context. When audience type is genuinely ambiguous,
default rules apply (see Section 3).

---

## Core Principle — Signal Integrity

Signal conclusions are never audience-dependent.

Direction, confidence tier, macro regime modifier, HOLD gate status,
and recommended action (ENTER/HOLD/AVOID) are determined entirely by
the signal framework. They do not change based on who is receiving
the output.

This is non-negotiable. AN-1 encodes this principle.

What changes across profiles:
- Output format (prose vs structured vs JSON)
- Emphasis priorities (what is surfaced first)
- Language register (plain language vs technical)
- Depth of explanation (mechanics assumed vs mechanics explained)
- Which contextual layers are foregrounded vs backgrounded

What never changes:
- Signal direction
- Confidence tier
- HOLD gate status and its hard gate nature
- Macro regime modifier values
- Recommended action values
- Fraud risk warnings (always surfaced, never suppressed — AN-7)

---

## How to Use This File

```
STEP 1 — IDENTIFY AUDIENCE TYPE:
  From explicit context: user states their role or profile.
  From inferable context: message framing, question type, platform.
  From direct question: "who will be receiving this output?"
  If unknown: apply default rules (Step 3 defaults).

STEP 2 — LOAD THE CORRESPONDING PROFILE:
  Match audience type to named profile (Profiles 1–7).
  If no match: use Custom Profile Template (Section 11).
  If partial match: state which profile is closest and note the gap.
    Better to note partial fit explicitly than silently mismatch (AN-11).

STEP 3 — APPLY PROFILE OUTPUT RULES:
  Profile rules are applied on top of standard signal output.
  They do not replace the signal generation process.
  Signal conclusions are produced first; framing is applied second.

DEFAULT RULES (when audience type is unknown):
  Consumer context (retail, public): Profile 1 — Fan/Holder
  Technical context (build, integration): Profile 3 — Builder/Developer
  Unrecognised type: Custom Profile Template
```

---

## Profile 1 — Fan / Holder

**Who:** Retail participant holding fan tokens via Socios, KayenFi,
or a DEX. May have limited technical knowledge of on-chain mechanics.

**Goal:** Understand what is happening with their token and what their
holding position means in the current signal context.

**Emphasis:** Supply event impact in plain language · Burn to Glory
tournament cycle context · HOLD gate with plain language reason ·
governance windows · fraud risk during tournament periods.

**Format:** Plain language prose. Mechanics explained, not assumed.
No modifier values without explanation of what they mean.

```
OUTPUT RULES:
  HOLD gate:
    Always include plain language reason — not just modifier value.
    Example: "The signal says HOLD because the CHZ market is in a
    downturn phase that reduces confidence across all fan token signals."
    NOT: "HOLD — CAPITULATION ×0.70 applied."

  Treasury burns:
    Never affect holder wallets — always state this explicitly.
    Example: "Burns remove tokens from the team treasury, not from
    your wallet. Your holding is unaffected."

  Tournament cycle:
    Always include when BTG is active — where in the tournament,
    what happens next, what the burn mechanics mean for this token.

  Fraud risk:
    Always flag during major tournament windows. Plain language.
    "Watch out for unofficial channels claiming to offer burn bonuses —
    these are fraudulent. All official supply events are on-chain."

  Modifier stack:
    Summarise in plain language, not as a numeric stack.
    "The signal is in HOLD territory because [reason], not ENTER."

  Technical terms:
    Define on first use in this output. Do not assume knowledge of
    SMS, CDI, CHZ regime, APS, or TFM codes.
```

---

## Profile 2 — Signal Consumer

**Who:** Anyone making decisions based on SportMind signal output.
May be an individual, an automated system, or a third party consuming
signal outputs.

**Goal:** Receive the most complete, precisely structured signal output.
No interpretation. No editorialising. All fields named and present.

**Emphasis:** Full modifier stack front and centre · HOLD gate status
and reason · confidence tier with explicit upgrade/downgrade conditions ·
all flags raised and resolved · SMS score · recommended action only.

**Format:** Structured signal output. No prose narrative unless
explicitly requested. All fields named.

```
OUTPUT RULES:
  Recommended action:
    ENTER / HOLD / AVOID only — per framework.
    Never add qualitative commentary ("this looks promising").
    Never produce trading advice.

  Confidence tier:
    Always paired with upgrade and downgrade conditions.
    "MEDIUM — upgrades to HIGH if lineup confirmed and SMS > 80.
     Downgrades to LOW if CAPITULATION deepens or H2H gate fails."

  Files loaded:
    Always state which library files were loaded in this signal chain.

  Library version:
    Always state. SMI version always stated.

  HOLD gate:
    Hard gate — always explicit. Never softened to "lean toward holding."
    "HOLD gate: ACTIVE. No ENTER position warranted."

  Flags:
    All flags raised in pre-match signal always shown.
    All flags resolved post-match always shown.
    Never embedded in prose — always as discrete named items.

  SMS:
    Always included with tier label.
    "SMS: 100.0 · HIGH_QUALITY · 5/5 layers loaded"
```

---

## Profile 3 — Builder / Developer

**Who:** Anyone building on SportMind — MCP integrations, agent pipelines,
standalone applications, community contributions, skill extensions.

**Goal:** Understand correct library usage, file loading sequences,
applicable agent rules, and failure modes that could affect the build.

**Emphasis:** File loading sequence · relevant agent rules (numbered) ·
failure modes (FM1-8 · MMA-FM1-4 · TFM1-6) · MCP tool sequence ·
library gaps that could affect the build.

**Format:** Structured with file paths as plain text. Agent rules
numbered. Failure modes named and coded explicitly.

```
OUTPUT RULES:
  Library files:
    Always state which library files are directly relevant to
    the build task. File paths as plain text (no backtick formatting
    that could be misread as code).

  Failure modes:
    Always surface applicable failure modes proactively.
    "FM1 (Price-Signal Conflation) applies when integrating
     live exchange data — ensure price signal and demand signal
     remain separate outputs."

  Library gaps:
    Always note gaps that could affect the build.
    "No $[TOKEN] CDI file exists — sport domain framework applies.
     CDI-level signals for this token are not available."

  Library version:
    Always state. Builders need to know which version of the
    library their build is calibrated against.

  MCP tool sequence:
    Always include when build involves live signals or MCP integration.
    Reference platform/sportmind-mcp-server.md for current tool list.

  Agent rules:
    Never assume builder has read every relevant file.
    Surface the numbered rules that directly constrain the build.
```

---

## Profile 4 — Researcher / Journalist / Analyst

**Who:** Anyone investigating, reporting on, or producing analysis of
the fan token ecosystem, SportMind methodology, or related markets.

**Goal:** Structural story, verified claims, enduring patterns,
citation-ready output. What the framework confirms, what it cannot
confirm, and what the evidence base looks like.

**Emphasis:** Structural narrative first · verification chain explicit ·
historical precedent · confirmed vs emerging vs unconfirmed · calibration
status of any modifier or framework claim.

**Format:** Prose narrative with verification sources inline. Key
claims structured for citation. Calibration status of each claim noted.

```
OUTPUT RULES:
  Confirmation status:
    Always distinguish: CONFIRMED / EMERGING / UNCONFIRMED.
    "The CAPITULATION modifier (×0.70) is confirmed at v4.5.1.
     The FORTRESS venue tier threshold is preliminary — calibration
     pass planned post-WC2026."

  Source chain:
    Always name the Tier 1 source for structural claims.
    On-chain supply events: chiliscan.com.
    Regulatory claims: the specific law or regulation.

  Calibration records:
    Never present calibration records as predictive.
    "This record documents what the signal said before the match
     and what the result was — it is not a claim about future outcomes."

  Library gaps:
    When specific data is absent because of the Library Rule or
    Club Intelligence Gate, offer the reason if asked.
    "Named player data is not available — the Club Intelligence Gate
     excludes individual player signings from library files."

  Proper noun handling:
    The Proper Noun Test is implicit. Do not name specific individuals
    in signal context. Structural claims do not depend on named players.

  Calibration status:
    Always note when citing modifier values whether they are calibrated
    (10+ records), emerging (3-4 records), or uncalibrated (0 records).
```

---

## Profile 5 — Integration Consumer

**Who:** Programmatic system, third-party tool, API consumer, or
automated pipeline receiving SportMind signal output.

**Goal:** Clean, structured, machine-parseable output with full
provenance. Every field named. No ambiguity.

**Emphasis:** Structured data format consistent with MCP output schema ·
all fields typed · library and SMI version as metadata · files loaded
as array · flags as discrete named items.

**Format:** Structured data format. Prose is opt-in only. Booleans
as true/false. Modifiers as decimals. Confidence tier as both label
and numeric equivalent.

```
OUTPUT RULES:
  Default format:
    Structured output — prose only if explicitly requested.
    Consistent schema across every call.

  Metadata:
    Library version and SMI version always included.
    "library_version": "v4.5.1", "smi_version": "[current]"

  Files loaded:
    Always as array.
    "files_loaded": ["core/h2h-framework.md", "sports/football/...", ...]

  Flags:
    Always as discrete named items — never embedded in prose.
    "flags": ["CHZ_CAPITULATION_ACTIVE", "H2H_RECENCY_FLAG", ...]

  Confidence tier:
    Always paired with numeric equivalent.
    "confidence": {"tier": "MEDIUM", "numeric": 0.60}

  HOLD gate:
    Never omitted. Always as hard boolean.
    "hold_gate": {"active": true, "reason": "SMS 38.5 below threshold"}

  Modifiers:
    Always as decimals.
    "chz_modifier": 0.70, "composite_modifier": 0.70

  Recommended action:
    "action": "HOLD" — one of ENTER / HOLD / AVOID only.
```

---

## Profile 6 — Community Manager

**Who:** Someone managing official or semi-official fan token community
communications — Telegram supergroups, X accounts, Discord servers,
club social channels, Socios community hubs.

**Goal:** Community health signals, governance timing, supply event
communication framing, fraud risk context — actionable for community
communication decisions.

**Emphasis:** Community health indicators · governance vote windows ·
supply event communication framing · fraud risk warnings with
communication guidance · tournament cycle timing and engagement peaks.

**Format:** Actionable community context. Plain language. Timing
guidance relative to match windows and governance periods.

```
OUTPUT RULES:
  Treasury burns:
    Always make clear burns do not affect holder wallets.
    Frame for community communication:
    "For your post: 'Treasury burn confirmed. This removes [X]%
     from the team treasury — your tokens are not affected.'"

  Governance windows:
    Always surface participation patterns when governance is active.
    Include timing context relative to vote deadlines.

  Fraud risk:
    Always flag during major tournaments with communication guidance.
    Provide example language community managers can post directly.
    "Reminder to pin: SportMind does not run giveaways or bonus burn
     schemes. All official supply events are verifiable on-chain."

  CHI (Community Health Indicator):
    Surface when available. Plain language translation of indicator.

  Tournament cycle:
    Always include — where in the tournament, next fixture date,
    what engagement peaks are expected and when.

  Timing:
    Always relative to match kickoff windows per TFM6.
    "Post governance reminder at T-48h relative to the next home
     fixture — highest community engagement window."
```

---

## Profile 7 — Regulator / Compliance Professional

**Who:** Regulator, lawyer, compliance officer, exchange compliance
team, or legal practitioner engaging with fan token classification,
holder obligations, or enforcement timelines.

**Goal:** Regulatory classification, jurisdiction framework, holder
obligations, enforcement signals, citation chain. Precision over
narrative.

**Emphasis:** Jurisdiction-specific classification first · TFM4 flags ·
holder tax regime · enforcement status with days remaining · Tier 1
regulatory sources only · explicit gap notation.

**Format:** Structured regulatory summary. Jurisdiction stated first.
All claims sourced. No speculation on unresolved questions.

```
OUTPUT RULES:
  Jurisdiction:
    Always stated explicitly at the top of output.
    Never assumed from context alone — confirm before proceeding.

  TFM4 (Regulatory Deadline Blindness):
    Always check TFM4 status before producing regulatory output.
    Active enforcement windows stated with days remaining.
    Known active flags to check:
      SARS T-30 · Russia daily · UK FCA T-60 · Brazil MP 1.303/2025

  Sources:
    Tier 1 regulatory sources only — no aggregators.
    Law number · regulation reference · official government publication.

  Classification:
    Confirmed or explicitly UNCONFIRMED — no inference.
    "Fan token classification in [jurisdiction]: UNCONFIRMED —
     regulatory authority has not issued guidance as of [date]."

  Library gaps:
    Explicitly note when regulatory framework for a jurisdiction
    is not yet in the SportMind library.
    "No [jurisdiction].md file exists. Classification cannot be
     confirmed from SportMind regulatory layer."

  Supply events:
    Never speculate on tax treatment of supply events where not
    confirmed. State UNRESOLVED explicitly.
    "PTG burn tax treatment in Italy: UNRESOLVED as of v4.5.1."

  PTG burn tax treatment by jurisdiction (known):
    Italy: UNRESOLVED · Brazil: UNRESOLVED · Turkey: UNRESOLVED
    For confirmed status, load the relevant regulatory file.
```

---

## Custom Profile Template

When the audience type does not match any named profile, use this
template. Complete all five fields before applying output rules.

```
CUSTOM PROFILE — COMPLETION REQUIRED:

Audience Type:
  [Describe who is receiving this output — role, context, platform]

Primary Goal:
  [What does this audience need to do or understand from this output?]

Signal Consumption Pattern:
  Select one: Decision-making · Communication · Research ·
  Integration · Education · Compliance · Other

Output Format Preference:
  Select one: Prose narrative · Structured signal stack ·
  JSON · Bullet points · Regulatory citation format · Other

Known Constraints:
  [Any known limitations on what can be included — e.g. no technical
   terms, specific word count, restricted to confirmed facts only]

AFTER COMPLETING TEMPLATE:
  1. Check for named profile overlap — does this audience partially
     match a named profile? State the closest match and the gap.
  2. State any rules inherited from the closest named profile.
  3. Apply inherited rules plus any additional rules required.
  4. If this custom profile type appears repeatedly across sessions,
     flag it as a candidate for named profile status (AN-8).
```

---

## Future Profiles

**ATHLETE / AGENT REPRESENTATIVE — PLANNED**

Planned for when the athlete/national-teams/ and athlete/meta/
directories reach sufficient depth to support a distinct profile.

Will cover:
- Fan token partnership considerations from an athlete/representative
  perspective
- Demand signal interaction with athlete availability signals
- Commercial modifier logic (CDI + APS + demand floor)
- APS framework context and how it affects fan token demand
- Long-term absence reasoning framework interaction with signal output

Not yet defined — escalate to Strategy & Brainstorm before creating
this profile when athlete intelligence layer reaches sufficient depth.

---

## Agent Rules

```
AN-1 — SIGNAL CONCLUSIONS NEVER AUDIENCE-DEPENDENT:
  Direction, confidence tier, macro regime modifier, HOLD gate status,
  and recommended action are fixed by the signal framework. They do
  not change based on audience. This rule has no exceptions.

AN-2 — DEFAULT PROFILE SELECTION:
  Consumer context (retail, public, fan-facing): Profile 1 — Fan/Holder.
  Technical context (build, integration, development): Profile 3 — Builder.
  Unrecognised audience type: Custom Profile Template.
  When in doubt: apply Profile 1 defaults (most conservative framing).

AN-3 — CUSTOM PROFILE OVERLAP — STATE INHERITANCE EXPLICITLY:
  When a custom profile partially matches a named profile, state:
  "Closest named profile: [name]. Inheriting rules: [list].
   Additional rules for this audience: [list]."
  Silent mismatch is always worse than explicit partial fit.

AN-4 — HOLD GATE ALWAYS HARD GATE:
  Regardless of audience profile, the HOLD gate is never a suggestion.
  It is never softened, contextualised away, or presented as discretionary.
  Plain language explanation is required for Fan/Holder.
  Hard field is required for Integration Consumer.
  The gate is never omitted for any profile.

AN-5 — NEVER PRODUCE TRADING ADVICE:
  Signal Consumer profile receives ENTER / HOLD / AVOID only.
  No qualitative commentary on what to do with the output.
  No position sizing guidance beyond HOLD gate status.
  No market timing advice.

AN-6 — LIBRARY AND SMI VERSION ON REQUEST; PROACTIVE FOR BUILDER AND INTEGRATION:
  For Builder/Developer and Integration Consumer profiles: always
  include library version and SMI version proactively.
  For all other profiles: always available on request.
  Version is never withheld.

AN-7 — FRAUD WARNINGS NEVER SUPPRESSED:
  Regardless of audience profile, fraud risk is always surfaced.
  Fan/Holder: plain language fraud warning with community-ready language.
  Community Manager: fraud warning with communication guidance.
  All profiles: fraud risk is never withheld to simplify output.

AN-8 — REPEATED CUSTOM PROFILE = NAMED PROFILE CANDIDATE:
  When the same custom profile type appears more than twice across
  sessions, flag it as a candidate for named profile status.
  Escalate to Strategy & Brainstorm with profile details.

AN-9 — REGULATORY OUTPUT REQUIRES EXPLICIT JURISDICTION:
  Regulatory output for Profile 7 always starts with jurisdiction stated.
  Never produce regulatory output before confirming jurisdiction.
  Never infer jurisdiction from context alone.

AN-10 — AUDIENCE NAVIGATOR DOES NOT CHANGE FILES LOADED IN SIGNAL CHAIN:
  The signal generation file loading sequence is determined by the
  signal framework, not by the audience profile. This file governs
  output framing only. It does not add or remove files from the chain.

AN-11 — PARTIAL FIT NOTED EXPLICITLY IS BETTER THAN SILENT MISMATCH:
  When a custom profile partially overlaps with a named profile,
  state the partial fit and the gap explicitly. Never silently apply
  the wrong profile. Explicit partial fit serves the audience better
  than a silently mismatched format.

AN-12 — CALIBRATION PRIORITY UNCHANGED BY AUDIENCE TYPE:
  The calibration methodology (core/calibration-methodology.md) applies
  regardless of which audience profile is active. Confidence tiers are
  not inflated for any audience. Uncalibrated modifiers are disclosed
  to all profiles — the language of disclosure changes, not the fact.
```

---

## MIND DIMENSIONS

| Dimension | Sub-dimensions engaged | Status |
|---|---|---|
| 1. Intelligence | 1b Signal Awareness · 1d Gap Awareness | ACTIVE |
| 2. Reasoning | 2a Causal · 2c Multi-Signal | ACTIVE |
| 3. Context | 3d Cultural/Market Context | ACTIVE |
| 4. Memory | 4b Semantic Memory | ACTIVE |
| 5. Judgment | 5c Conflict Resolution · 5d Priority Judgment | ACTIVE |
| 6. Attention | 6c Noise Filtering | ACTIVE |
| 7. Communication | 7a Output Clarity · 7b Confidence Expression · 7c Format Compliance | ACTIVE — PRIMARY |
| 8. Verification | 8a Source Tier Assessment | ACTIVE |
| 9. Learning | 9c Pattern Reinforcement | ACTIVE |
| 10. Integration | 10a Cross-Layer Synthesis · 10b Tool Coordination | ACTIVE |
| 11. Calibration | 11b Confidence Calibration | ACTIVE |
| 12. Adaptation | 12b Context Switching · 12c Signal Reweighting | ACTIVE |
| 13. Ethics | 13a Fabrication Prevention · 13b User Safety | ACTIVE |
| 14. Transparency | 14a Reasoning Chain Visibility · 14b Modifier Disclosure · 14d Limitation Acknowledgement | ACTIVE |
| 15. Execution | 15a Entry Discipline · 15d Playbook Adherence | ACTIVE |
| 16. Collaboration | 16a Task Delegation · 16c Output Coordination | ACTIVE |

---

## COMPATIBILITY

Compatible with: Claude · GPT-4 · Gemini · any LLM ·
sportmind_pre_match · sportmind_macro · sportmind_fan_token_lookup ·
fan-token/fan-holder-behaviour.md ·
fan-token/holder-tax-framework.md ·
macro/fan-adoption-intelligence.md ·
macro/regulatory/ (all jurisdiction files) ·
core/signal-classification-framework.md ·
core/temporal-reasoning-framework.md ·
core/agent-failure-modes.md ·
fan-token/agent-failure-modes-fan-token.md ·
platform/sportmind-mcp-server.md ·
community/calibration-data/football/CALIBRATION-RECORD-TEMPLATE.md

© 2026 SportMind

---

*SportMind v4.5.1 · MIT License · sportmind.dev*
*All 16 Mind dimensions mapped.*
*Signal conclusions are never audience-dependent — only output framing changes.*
*Custom Profile Template available for audience types not covered by named profiles.*
