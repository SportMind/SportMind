# Master Reasoning Protocol

Domain: core/master-reasoning-protocol.md
Version: v4.6.50
Library Rule: Six-Month Test PASSES · Proper Noun Test PASSES
Scope: The foundational reasoning chain for any LLM or agent operating
SportMind intelligence. Governs loading order, source architecture,
HOLD gate discipline, citation chain, version-awareness, audience
calibration, and multi-LLM design. LLM-agnostic — the same chain
runs on Claude, Gemini, GPT-4, open-weight models, and any agent
runtime. Every session is a cold start. This protocol is
self-contained.

Companion to: core/compound-signal-framework.md ·
core/reasoning-audit-framework.md · core/calibration-methodology.md ·
core/audience-navigator.md · onboarding/welcome-prompt.md

---

RELATIONSHIP TO OTHER ENTRY POINTS

This protocol is the reasoning layer. It is not a copy-paste prompt.

onboarding/welcome-prompt.md — human-facing · copy-paste · casual
  entry point · any LLM · no setup required · sportmind.dev/start/

core/master-reasoning-protocol.md — LLM-facing · agent runtime ·
  full reasoning chain · powers sportmind.dev/agent/ · what a serious
  integration or builder loads before any analysis begins

Both are valid entry points. They serve different users. This protocol
does not replace the welcome prompt — it operates at a deeper layer.

---

SECTION 1 — What This Protocol Is

The Master Reasoning Protocol tells any LLM how to reason with
SportMind from a cold start. It is not a persona. It is not a system
prompt. It is a structured reasoning chain that, when followed,
produces SportMind-compliant intelligence output regardless of which
LLM is executing it.

WHAT IT GOVERNS:
  · The order in which information is loaded before any signal is produced
  · Which sources are authoritative and which are cross-checks only
  · When to HOLD and when to proceed
  · How every modifier must be traced to a source file
  · How to handle version mismatches between signal and library state
  · How to calibrate output framing for different audiences
  · How to operate without tool use, memory, or inter-session state

WHAT IT DOES NOT GOVERN:
  · Which specific files to load for a given sport or token — those
    rules live in the domain skill files (sports/ · fan-token/ · market/)
  · How to calculate specific modifiers — those live in the framework
    files this protocol orchestrates
  · UI or delivery format — those live in the platform layer

A LLM that loads this protocol and follows it will produce reasoning
that is auditable, traceable, and consistent across models and sessions.
A LLM that skips it may produce outputs that look correct but cannot
be verified or reproduced.

---

SECTION 2 — Loading Order

This is the spine of the protocol. Follow it in order. Never skip
a stage. Never reorder. If a layer cannot be loaded, apply partial
loading defaults from core/compound-signal-framework.md Section 6,
note the gap explicitly, and recalculate SMS before proceeding.

STAGE 1 — MACRO REGIME
  Load: macro/chz-tokenomics.md · macro/chz-market-cycle-framework.md
  Determine: CAPITULATION x0.70 / ANXIETY x1.00 / BULL x1.15
  Apply: to every token in scope before any token-specific layer loads
  Rule: macro regime is a shared layer — load once, apply to all tokens
  HOLD trigger: if regime is CAPITULATION and adjusted SMS < 80 → HOLD
  Never proceed past Stage 1 without confirming the active regime.

STAGE 2 — REGULATORY OVERLAY
  Load: fan-token/holder-tax-framework.md
  Then load: macro/regulatory/[jurisdiction].md for each primary
    holder population in scope
  Determine: jurisdiction type (A/B/C/D/E · UNKNOWN · CONDITIONAL)
  Apply: friction modifier to demand stack — never omit
  Rule: if jurisdiction file does not exist, state UNKNOWN · apply
    conservative default · flag for Strategy Chat escalation
  For dual-token fixtures: regulatory overlay may differ per token
    (each token's holder population has its own jurisdiction) —
    load independently unless explicitly shared (e.g. Italian derby)
  Never assume regulatory overlay is the same for both tokens.

STAGE 3 — CDI GATE
  Load: market/club-intelligence/[token].md for each token in scope
  Determine: CONSOLIDATION / TRANSITION / GROWTH / EMERGING / DORMANT
  Apply: CDI gate classification governs confidence tier ceiling
  Rule: TRANSITION cap is unconditional — directional output only
    regardless of occasion weight tier, rivalry prestige, or
    any other modifier. No exception.
  Rule: if no CDI file exists for a token, apply domain framework
    from the relevant sport intelligence file · note gap explicitly ·
    do not fabricate CDI gate classification
  DORMANT: treat as single-token fixture — DORMANT token produces
    no compound output.

STAGE 4 — FORM SIGNAL
  Load: recent results · squad health · coaching stability
  Source: intelligence/source-registry.md sport section for
    appropriate data sources per sport
  Determine: winning run / mixed / poor form / insufficient data
  Apply: positive / neutral / negative form modifier
  Rule: never fabricate form signal — if data is unavailable,
    state FORM: UNCONFIRMED · apply neutral modifier · note in output
  Rule: coaching succession is a CDI-level signal, not a form signal —
    encode in CDI gate, not here

STAGE 5 — H2H
  Load: core/h2h-framework.md
  Apply: five-condition relevance gate before any H2H modifier applies
  Conditions: competitive fixture · same tier or higher · minimum 3
    meetings · dual-token eligibility · continuity check
  Rule: if gate fails → H2H: INSUFFICIENT SAMPLE — never state 50/50
    as a substitute for a failed gate
  Rule: H2H is the most fabrication-prone layer in SportMind — apply
    the gate rigorously · never invent match history

STAGE 6 — VENUE
  Load: core/venue-intelligence-framework.md
  Determine: HOME / AWAY / NEUTRAL / SHARED / TEMPORARY
  Apply: venue modifier to compound stack
  Rule: SHARED venue (e.g. San Siro) = x0.5 mandatory · never apply
    full home advantage to a shared stadium
  Rule: NEUTRAL venue = zero home advantage · apply crowd composition
    modifier only

STAGE 7 — COMPOUND SYNTHESIS
  Load: core/compound-signal-framework.md
  Apply: five-layer dominance hierarchy — Tier 1 Macro never
    overridden · Tier 2 Regulatory access restriction · Tier 3 CDI ·
    Tier 4 Form and contextual · Tier 5 Occasion weight (final only)
  Calculate: SMS (Signal Maturity Score) 0–100
  HOLD gate: SMS < 80 → HOLD — non-negotiable · no override
  For dual-token fixtures: load market/dual-fan-token-match-dynamics.md
    Complete Steps 1–6 of the dual-token sequencing before producing
    any output. RELATIONSHIP TYPE classification is mandatory.

STAGE 8 — OUTPUT FRAMING
  Load: core/audience-navigator.md
  Determine: audience profile (Fan/Holder · Signal Consumer ·
    Builder/Developer · Researcher · Integration Consumer ·
    Community Manager · Regulator/Compliance)
  Apply: framing calibration — signal conclusions never change by
    audience · only output format and depth change
  Rule: HOLD gate is always a hard gate regardless of audience —
    never soften or omit a HOLD for a non-technical audience
  Rule: financial advice is never produced for any audience profile

---

SECTION 3 — Source Architecture

Three tiers. Priority order is absolute. Never treat a lower tier
as authoritative when a higher tier source is available.

TIER 1 — PRIMARY SOURCES (authoritative):
  docs.chiliz.com — token registry · contract addresses · partnerships
  chiliscan.com — on-chain verification · token status · supply events
  chiliz.com/blog — official announcements · product launches
  club official channels — squad health · coaching decisions
  UEFA.com · CONMEBOL.com · sport governing body sites — fixtures · results
  Regulatory body sites — enacted law · published guidance only
  intelligence/source-registry.md — full canonical source list

TIER 2 — CROSS-CHECKS ONLY (never primary):
  FanTokens.com · Socios.com · Chiliz.com aggregator pages
  Use to cross-check Tier 1 findings — never as sole source
  BLACK/GREYSCALE LOGO SIGNAL: if a fan token logo appears in
    black or greyscale on any aggregator, treat as potential
    terminated or dormant partnership — verify via Tier 1 before
    using that token in any analysis. Do not assume active status.

TIER 3 — CONTEXT ONLY (never cite for modifiers):
  Social media · fan forums · unofficial aggregators · price trackers
  Useful for sentiment context · never as source for factual claims
  or modifier values

FABRICATION PREVENTION:
  Never invent a source. Never attribute a modifier value to a file
  that does not exist. If a source cannot be confirmed as Tier 1,
  state the tier and note the limitation explicitly in the output.
  This is the single most important rule in the source architecture.

TOKEN VERIFICATION RULE:
  Always verify fan token tickers from docs.chiliz.com first.
  Never infer tickers from club names.
  $ASR not $ROM · $CITY not $MCI · confirm each token explicitly.
  $AFC is the only confirmed FTP PATH_2 token — never generalise.
  $BJK (Besiktas) is on Ethereum — NOT Chiliz Chain.
  $SPAIN ≠ $SNFT — different tokens, different chains.

---

SECTION 4 — HOLD Gate Discipline

The HOLD gate is the most important single concept in SportMind
reasoning. It exists because a low-quality signal that produces a
directional output is worse than no output at all.

THE RULE:
  SMS < 80 → HOLD — no directional output produced
  This is non-negotiable. It cannot be overridden by:
  · Occasion weight (UCL Final · World Cup · Tier 1 derby)
  · Rivalry prestige
  · User request or pressure
  · High CDI gate classification
  · Trophy premium
  · Any combination of the above

LAYER 4 HOLD GATE IN AUDIT CONTEXT:
  If a reasoning audit is being conducted and Layer 4 (Judgment/
  HOLD gate) receives a FAIL verdict, the overall audit verdict
  is RED — regardless of all other layer verdicts.
  A FAIL at Layer 4 overrides every other layer.

HOLD IS A VALID OUTCOME:
  HOLD is not a failure. HOLD is the correct output when signal
  quality is insufficient. A HOLD that prevents an incorrect
  directional call is the optimal gate outcome.
  State explicitly: HOLD gate active · SMS [score] · missing
  layers: [list] · do not produce directional output.

DUAL-TOKEN HOLD:
  HOLD gate applies per token in a dual-token fixture.
  One token HOLD + one token PASS = PARTIAL dual-token output.
  Both tokens HOLD = no dual-token output produced.
  RELATIONSHIP TYPE: INDETERMINATE when one or both tokens on HOLD.

CAPITULATION AND HOLD:
  Under CAPITULATION x0.70, base scores that pass the raw SMS
  threshold may fall below 80 after the regime suppressor applies.
  Always recalculate SMS after applying the CAPITULATION multiplier.
  Never use the pre-CAPITULATION SMS to determine HOLD gate status.

---

SECTION 5 — Citation Chain

Every modifier, weight, and signal in a SportMind output must be
traceable to a specific source file and, where relevant, a library
version. This is what makes SportMind outputs auditable.

MANDATORY CITATION FIELDS IN EVERY OUTPUT:
  · Macro regime: state source (macro/chz-tokenomics.md or
    macro/chz-market-cycle-framework.md) and regime confirmed
  · CDI gate: state source file (market/club-intelligence/[token].md)
    or domain framework if no CDI file exists
  · Occasion weight: state source (market/rivalry-intelligence.md
    or fan-token/competition-calendar-framework.md) and tier
  · Regulatory overlay: state source file and jurisdiction type
  · H2H modifier: state whether gate passed or failed and why
  · Trophy premium: state tier, decay stage, and source file
  · Supply events: state PATH_2 or PTG status per token —
    always report for both tokens, even when neither is active

PARTIAL LOADING:
  If a layer could not be loaded, state explicitly:
  [LAYER]: NOT LOADED — [reason] — applying partial loading default
  Then apply the default from core/compound-signal-framework.md
  Section 6 and recalculate SMS. Never silently omit a layer.

NO FABRICATED MODIFIERS:
  If a modifier value cannot be traced to a SportMind source file,
  it does not enter the compound stack. State the gap. Apply the
  nearest documented default. Flag for library update if recurring.

VERSION CHAIN:
  When a calibration record is produced, the library version at
  signal time must be recorded in the YAML frontmatter. This enables
  retroactive audit — an auditor can reconstruct what files existed
  at signal time and evaluate accordingly.

---

SECTION 6 — Version Awareness

SportMind is a versioned library. Modifiers change. CDI gates change.
Regulatory frameworks update. A signal produced at v4.1.x may not
reflect v4.6.x library state.

THE RULE:
  Always state the library version in every output.
  Always flag if operating on a version that is materially behind
  the current library state when that gap affects the signal.

VERSION-AWARE REASONING RULES:

RULE V1 — STATE VERSION IN OUTPUT:
  Every calibration record, signal output, and reasoning audit
  must state the library version at time of signal production.
  Format: Library version: v[X.X.XX] at signal time.

RULE V2 — NEVER BACKFILL SILENTLY:
  If a signal was produced at an earlier version and is being
  reviewed at a later version, state the version delta explicitly.
  Do not apply modifiers from the current version to a historical
  signal without flagging the version gap.

RULE V3 — REGIME PRESERVATION:
  The CHZ regime at signal time must be preserved in calibration
  records and audits. A signal produced under ANXIETY x1.00 must
  not be evaluated as if CAPITULATION x0.70 applied, even if
  CAPITULATION is now the active regime. State the regime at signal
  time explicitly and note the current regime for context only.

RULE V4 — REGISTRY GAP HANDLING:
  If a fan token was not in the registry at signal time, this is a
  REGISTRY-GAP. Flag it explicitly. Apply HOLD on dual grounds if
  CAPITULATION is also active. Document the version at which the
  token entered the registry. Resolved REGISTRY-GAPs must be
  documented in four locations: YAML frontmatter · Pre-Match Signal ·
  Flags Resolved · Post-Match Notes.

RULE V5 — CDI FILE EXISTENCE:
  If no CDI file existed for a token at signal time (even if one
  exists now), the signal must be evaluated using the domain
  framework that was available at signal time. State which framework
  was applied and note the CDI file gap explicitly.

---

SECTION 7 — Audience Calibration

Load: core/audience-navigator.md before producing any output.

THE CORE PRINCIPLE:
  Signal conclusions are never audience-dependent.
  Output framing and depth are audience-dependent.
  A HOLD is a HOLD for every audience. A POSITIVE compound signal
  is POSITIVE for every audience. Only how it is communicated changes.

SEVEN AUDIENCE PROFILES:
  Fan/Holder · Signal Consumer · Builder/Developer ·
  Researcher/Journalist/Analyst · Integration Consumer ·
  Community Manager · Regulator/Compliance Professional

DEFAULT PROFILE:
  If no audience is specified, apply Fan/Holder framing — accessible
  language, no raw modifier values, signal direction with confidence
  tier, HOLD gate stated plainly.

NEVER SUPPRESS FOR ANY AUDIENCE:
  · HOLD gate output — always state explicitly
  · Fraud risk warnings — never omit
  · Regulatory uncertainty — never downplay
  · Source limitations — always acknowledge

For full profile rules, load core/audience-navigator.md.
Do not reproduce the full routing guide here — it lives in that file.

---

SECTION 8 — Multi-LLM Design

This protocol is LLM-agnostic by design. The same reasoning chain
produces consistent SportMind-compliant output on Claude, Gemini,
GPT-4, Mistral, open-weight models, and any agent runtime.

DESIGN PRINCIPLES:

NO TOOL-USE ASSUMPTIONS:
  The protocol does not assume tool use, web search, or real-time
  data access. Any LLM following this protocol produces valid output
  from the loaded library files alone. Tool use enhances quality
  but is never a prerequisite for compliant reasoning.

NO MEMORY ASSUMPTIONS:
  Every session is a cold start. The protocol is self-contained.
  No inter-session state is assumed. An agent that loads this
  protocol and the relevant skill files has everything it needs.

NO MODEL-SPECIFIC SYNTAX:
  The loading order, citation chain, and HOLD gate rules are
  expressed in plain structured text — not in prompt engineering
  patterns specific to any model family.

CONSISTENT OUTPUT:
  Two different LLMs following this protocol on the same fixture
  with the same loaded files should produce outputs that agree on:
  · Macro regime and its suppressor value
  · CDI gate classification for each token
  · HOLD gate outcome (pass or hold)
  · Relationship type in dual-token fixtures
  · Occasion weight tier and source
  They may differ in framing, depth, and prose style — but not
  in the factual signal chain.

ORCHESTRATION LAYER (FUTURE — PHASE 3):
  A future orchestration layer will route each stage of this protocol
  to the best available LLM for that task — macro regime assessment
  to one model, CDI reasoning to another, output framing to a third.
  That design is not scoped here. This protocol is the foundation
  that the orchestration layer will build on.

---

SECTION 9 — Agent Rules

10 rules. Apply without being asked. Never skip.

RULE 1 — LOAD THIS PROTOCOL FIRST:
  Before loading any sport domain file, CDI file, or regulatory file,
  confirm this protocol is loaded. The loading order in Section 2
  governs all subsequent file loading. Never begin signal production
  without confirming Stage 1 (macro regime) is complete.

RULE 2 — VERIFY TOKENS BEFORE PROCEEDING:
  Confirm active fan token status via docs.chiliz.com (Tier 1) before
  any analysis. Never infer token tickers from club names. Black or
  greyscale logo on any aggregator = potential inactive status —
  verify via Tier 1 before proceeding.

RULE 3 — HOLD GATE IS ABSOLUTE:
  SMS < 80 → HOLD. No override. No exception. No matter the occasion
  weight, rivalry tier, or user expectation. State HOLD explicitly
  with SMS score and missing layers. Layer 4 FAIL in a reasoning
  audit = RED overall verdict regardless of all other layers.

RULE 4 — CITE EVERY MODIFIER:
  Every modifier value in every output must be traceable to a named
  SportMind file. If a modifier cannot be cited, it does not enter
  the compound stack. State the gap explicitly. Never fabricate
  modifier values.

RULE 5 — STATE LIBRARY VERSION:
  Every output — signal, calibration record, audit — states the
  library version at time of production. Version mismatches between
  signal time and current library state are flagged explicitly.
  Regime at signal time is preserved — never retroactively updated.

RULE 6 — DUAL-TOKEN REQUIRES DUAL-TOKEN PROTOCOL:
  Any fixture with two confirmed active Chiliz fan tokens loads
  market/dual-fan-token-match-dynamics.md before any analysis.
  Two independent single-token analyses presented side by side is
  not compliant dual-token output. RELATIONSHIP TYPE classification
  is mandatory and never optional.

RULE 7 — NEVER FILL GAPS WITH ASSUMPTIONS:
  If a regulatory file does not exist for a jurisdiction, state
  UNKNOWN. If a CDI file does not exist, apply domain framework
  and note the gap. If H2H gate fails, state INSUFFICIENT SAMPLE.
  Never fabricate context. Never assume what is not documented.

RULE 8 — AUDIENCE DOES NOT CHANGE SIGNAL:
  Load core/audience-navigator.md before producing output. Adapt
  framing and depth for the audience. Never adapt the signal itself.
  HOLD is HOLD for every audience. Fraud warnings are never suppressed.

RULE 9 — SUPPLY EVENTS ARE TOKEN-SPECIFIC:
  PATH_2 applies to $AFC only. PTG applies to confirmed national
  tokens only. Never transfer supply event mechanics across tokens.
  Always report supply event status for both tokens in dual-token
  output — even when neither token has an active supply event.

RULE 10 — COLD START EVERY SESSION:
  Every session is a cold start. No inter-session state is assumed.
  This protocol is self-contained. Load it, follow the loading order,
  and produce compliant output regardless of what any previous
  session produced.

---

SECTION 10 — Mind Dimensions

| Dimension | Sub-dimensions engaged | Status |
|---|---|---|
| 1. Intelligence | 1a Domain Knowledge · 1b Signal Awareness · 1c Pattern Recognition · 1d Gap Awareness | ACTIVE |
| 2. Reasoning | 2a Causal · 2b Probabilistic · 2c Multi-Signal · 2d Temporal | ACTIVE — PRIMARY |
| 3. Context | 3a Macro Context · 3b Event Context · 3c Historical Context | ACTIVE |
| 4. Memory | 4a Episodic Memory · 4b Semantic Memory · 4c Working Memory | ACTIVE |
| 5. Judgment | 5a Uncertainty Weighting · 5b Risk Assessment · 5c Conflict Resolution · 5d Priority Judgment | ACTIVE — PRIMARY |
| 6. Attention | 6a Signal Detection · 6b Urgency Detection · 6c Noise Filtering | ACTIVE |
| 7. Communication | 7a Output Clarity · 7b Confidence Expression · 7c Format Compliance | ACTIVE |
| 8. Verification | 8a Source Tier Assessment · 8b Cross-Verification · 8d Recency Validation | ACTIVE — PRIMARY |
| 9. Learning | 9a Modifier Updating · 9b Error Attribution · 9c Pattern Reinforcement | ACTIVE |
| 10. Integration | 10a Cross-Layer Synthesis · 10b Tool Coordination | ACTIVE |
| 11. Calibration | 11a Direction Accuracy · 11b Confidence Calibration · 11c Modifier Validation · 11d Coverage Tracking | ACTIVE |
| 12. Adaptation | 12a Regime Detection · 12b Context Switching · 12c Signal Reweighting | ACTIVE |
| 13. Ethics | 13a Fabrication Prevention · 13b User Safety · 13d Representation Accuracy | ACTIVE — PRIMARY |
| 14. Transparency | 14a Reasoning Chain Visibility · 14b Modifier Disclosure · 14c Source Attribution · 14d Limitation Acknowledgement | ACTIVE — PRIMARY |
| 15. Execution | 15a Entry Discipline · 15b Exit Discipline · 15d Playbook Adherence | ACTIVE |
| 16. Collaboration | 16a Task Delegation · 16b Context Handoff · 16c Output Coordination · 16d Conflict Arbitration | ACTIVE |

Primary dimensions: Reasoning (2) · Judgment (5) · Verification (8) ·
Ethics (13) · Transparency (14). These five dimensions are the
load-bearing structure of the protocol. Every other dimension
supports them.

---

COMPATIBILITY

Compatible with: Claude · GPT-4 · Gemini · Mistral · any LLM ·
any agent runtime · sportmind_pre_match · sportmind_signal ·
core/compound-signal-framework.md ·
core/reasoning-audit-framework.md ·
core/calibration-methodology.md ·
core/h2h-framework.md ·
core/venue-intelligence-framework.md ·
core/audience-navigator.md ·
core/contradiction-resolution-framework.md ·
market/dual-fan-token-match-dynamics.md ·
market/rivalry-intelligence.md ·
market/trophy-premium-framework.md ·
market/fan-base-intelligence.md ·
fan-token/holder-tax-framework.md ·
fan-token/registry/complete-registry.md ·
fan-token/competition-calendar-framework.md ·
fan-token/burn-to-glory-framework.md ·
intelligence/source-registry.md ·
market/club-intelligence/ (all CDI files) ·
macro/regulatory/ (all regulatory files) ·
sports/ (all sport domain files) ·
onboarding/welcome-prompt.md

© 2026 SportMind
