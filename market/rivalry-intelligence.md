# Rivalry Intelligence

**Domain:** market/rivalry-intelligence.md
**Version:** v4.5.21
**Library Rule:** Six-Month Test PASSES · Proper Noun Test PASSES
**Scope:** Canonical framework for rivalry and derby fixture
intelligence as a structural demand modifier for fan token
pre-match signal generation. Covers rivalry classification,
single-token vs dual-token rules, canonical rivalry register,
and compound signal interaction rules. Companion to
core/h2h-framework.md (historical match record) and
core/compound-signal-framework.md (signal synthesis).
Rivalry intelligence is structural — not form-based.
Loading order: load before compound synthesis layer.

---

## Critical Distinction — Rivalry vs H2H

Rivalry intelligence and H2H intelligence are complementary
but distinct layers. Never conflate them.

RIVALRY INTELLIGENCE (this file):
  What it captures: structural demand characteristics of a
  fixture — how the emotional and commercial intensity of
  a rivalry affects token holder behaviour, regardless of
  recent form or historical match record.
  When it applies: always, for any fixture in the rivalry
  register. Independent of current form.
  What it is NOT: a prediction of match outcome.
  What it is NOT: a substitute for H2H historical record.

H2H INTELLIGENCE (core/h2h-framework.md):
  What it captures: decay-weighted historical match record
  between two clubs. Directional signal based on who has
  won more recent competitive meetings.
  When it applies: after passing the five-condition
  relevance gate.

AGENT RULE: always load both files for a confirmed derby
fixture. Never substitute one for the other. They address
different questions:
  Rivalry: "How intense is this fixture for token holders?"
  H2H: "Who has the better recent competitive record?"

---

## Section 1 — Rivalry Classification System

Four tiers. Apply the highest applicable tier when multiple
tiers could apply. State tier explicitly in every output.

### TIER 1 — SUPER DERBY
City derby with maximum holder emotional intensity.
Long competitive history. High media amplification.

  Weight (dual-token): ×1.80
  Weight (single-token): ×1.50
  Condition: city or metropolitan rivalry with 10+ seasons
    of competitive history and confirmed cultural significance.
  Examples:
    Derby della Madonnina ($INTER/$ACM · Serie A · UCL)
    Kıtalararası Derbi ($GAL — single-token · Fenerbahçe absent)

### TIER 2 — MAJOR DERBY
National or strong regional rivalry. High cultural
significance. Both tokens frequently active.

  Weight (dual-token): ×1.65
  Weight (single-token): ×1.35
  Condition: national or strong regional rivalry with
    cross-city or cross-region fan base tension.
  Examples:
    Derby d'Italia ($INTER/$JUV · Serie A)
    North London Derby ($AFC/$SPURS · Premier League)
    El Clásico variant ($BAR/$ATM · La Liga dual-token)

### TIER 3 — SIGNIFICANT RIVALRY
Historical or regional rivalry with meaningful but
lower holder intensity than Tier 1-2. May be
single-token.

  Weight (dual-token): ×1.50
  Weight (single-token): ×1.35
  Named exceptions (intensity justifies premium above
    Tier 3 default):
    Derby della Capitale ($ASR · Rome derby · ×1.70):
      Rome derby intensity justifies premium. Canonical
      weight for $ASR fixtures vs Lazio: ×1.70.
      Single-token — Lazio has no active Chiliz token
      as of v4.5.21. Dual-token reclassification pending
      if Lazio token confirmed.
  Examples:
    Derby della Capitale ($ASR · ×1.70 canonical)
    PSG vs Monaco ($PSG/$ASM · Ligue 1 · ×1.50)

### TIER 4 — STRUCTURAL RIVALRY
Competition-defined rivalry. Recurring opponents in
continental competition or repeated cup meetings.
Lower holder intensity than geographic derbies.

  Weight (dual-token): ×1.20
  Weight (single-token): ×1.10
  Condition: recurring fixture pattern in continental
    or domestic cup competition — not a geographic derby.
  Examples:
    EL dual-token watch ($ACM/$JUV — only if drawn
    in Europa League 2026-27 · verify draw before applying)
    UCL recurring opponent pairs (verify 3+ meetings
    in same competition before applying Tier 4)

---

## Section 2 — Single-Token vs Dual-Token Rules

### Dual-Token Fixtures

Both clubs have confirmed active Chiliz fan tokens.
Full dual-token weight applies from the relevant tier.

  Agent rule: verify BOTH tokens active at
  fan-token/registry/complete-registry.md before applying
  dual-token weight. Black logo = potentially inactive —
  verify before proceeding.

### Single-Token Fixtures

One club has an active Chiliz fan token. The rival
club has no active Chiliz fan token.

  Single-token weight applies (see tier table above).
  Apply the weight to the active token only.
  Never apply dual-token amplification to a single-token
  fixture — the rival club's absence from Chiliz does not
  reduce holder intensity for the active token.
  Flag: "SINGLE-TOKEN DERBY — [rival club] no active
  Chiliz token as of [version date]."

### Escalation Rule — Rival Token Launch

Any confirmed rival club fan token launch immediately
reclassifies the fixture as dual-token.

  ESCALATE IMMEDIATELY to Strategy & Brainstorm:
  · Update this file with new dual-token classification
  · Update CDI file for affected club(s)
  · Update complete-registry.md
  · Recalibrate rivalry weight for new dual-token pairing
  Known monitoring flags:
    Lazio — monitor for Chiliz token confirmation
      (reclassifies Derby della Capitale to dual-token)
    Fenerbahçe — monitor for Chiliz token confirmation
      (reclassifies Kıtalararası Derbi to dual-token)
    Real Madrid — monitor for Chiliz token confirmation
      (creates El Clásico as highest-profile new dual-token
      La Liga fixture — escalate immediately)

---

## Section 3 — Canonical Rivalry Register

Authoritative register of confirmed rivalry fixtures.
Load this section before any derby fixture analysis.
Verify token status at complete-registry.md before applying.
All weights are initial structural estimates — uncalibrated.

| Fixture | Tokens | Tier | Weight | Token Status | Monitor |
|---|---|---|---|---|---|
| Derby della Madonnina | $INTER/$ACM | 1 | ×1.80 | DUAL-TOKEN ✓ | CDI asymmetry 2026-27: $INTER CONSOLIDATION · $ACM TRANSITION |
| Kıtalararası Derbi | $GAL | 1 | ×1.50 (ST) | SINGLE-TOKEN | Fenerbahçe no token · reclassify if confirmed |
| Derby d'Italia | $INTER/$JUV | 2 | ×1.65 | DUAL-TOKEN ✓ | $JUV EL 2026-27 not UCL · CDI asymmetry |
| North London Derby | $AFC/$SPURS | 2 | ×1.65 | DUAL-TOKEN ✓ | $SPURS no Europe 2026-27 · CDI asymmetry |
| El Clásico variant | $BAR/$ATM | 2 | ×1.65 | DUAL-TOKEN ✓ | Real Madrid no token · El Clásico itself is single-token |
| Derby della Capitale | $ASR | 3 | ×1.70 (canonical exception) | SINGLE-TOKEN | Lazio monitoring ACTIVE · reclassify if confirmed |
| PSG vs Monaco | $PSG/$ASM | 3 | ×1.50 | DUAL-TOKEN ✓ | Competitive gap large — apply CDI context |
| EL dual-token watch | $ACM/$JUV | 4 | ×1.20 | DUAL-TOKEN ✓ | Only if drawn in EL 2026-27 · verify draw before applying |

REGISTER INTEGRITY RULES:
· Only fixtures with at least one confirmed active Chiliz
  fan token appear in this register.
· Never apply a rivalry modifier to an unverified token.
· If a fixture is not in this register: classify as
  UNCLASSIFIED · do not invent a weight · flag to
  Strategy & Brainstorm for review.
· New entries require Strategy & Brainstorm approval before
  addition — never add in Build Chat without scope.

---

## Section 4 — Rivalry Modifier Interaction Rules

Rivalry weight is an occasion weight component. It feeds
into Layer 4 (Contextual) of the compound signal framework,
Tier 5 (Occasion Weight) in the dominance hierarchy.

### What Rivalry Weight Does NOT Do

  · Does NOT override CAPITULATION (Tier 1 — always dominant)
  · Does NOT override CDI gate (TRANSITION cap applies in derby)
  · Does NOT replace H2H signal (they are separate layers)
  · Does NOT predict match outcome

### Interaction Patterns

AMPLIFICATION — most common derby pattern:
  Rivalry weight + H2H home dominance + strong CDI + winning
  form = AMPLIFICATION. Stack all four. Apply rivalry weight
  (as occasion weight component) last — after Tiers 1-4 resolved.

CANCELLATION — CDI asymmetry in a derby:
  Both clubs have tokens. CDI gates differ (e.g. CONSOLIDATION
  vs TRANSITION). Rivalry weight applies to both tokens but
  CDI gate caps the TRANSITION token at directional only.
  Apply dominance hierarchy from compound-signal-framework.md.
  State CDI asymmetry explicitly in output.

CONFLICT — TRANSITION vs high rivalry weight:
  A TRANSITION club in a Tier 1 derby. High rivalry weight
  suggests elevated demand but TRANSITION cap limits confidence.
  Load core/contradiction-resolution-framework.md.
  Never average the conflict. Surface it explicitly.

CAPITULATION INTERACTION:
  CAPITULATION ×0.70 applies to the compound result after all
  layers including rivalry weight are stacked.
  A Tier 1 derby under CAPITULATION still produces a discounted
  compound result. The rivalry modifier does not restore the
  suppressed signal. It amplifies the post-suppressor result only.

  Example:
    Compound result (pre-suppressor): POSITIVE · HIGH CONFIDENCE
    CAPITULATION ×0.70: discounts compound result
    Rivalry weight (as final multiplier): amplifies discounted result
    Final output: POSITIVE but materially discounted vs non-CAPITULATION.

---

## Section 5 — Agent Rules

10 rules. Apply in order. Never skip.

RULE 1 — LOAD FIRST:
  Load this file before any confirmed derby fixture — not
  after other layers are stacked. Rivalry classification
  is context for all other signal layers.

RULE 2 — VERIFY TOKEN STATUS:
  Verify current token status at complete-registry.md
  before applying any modifier. Black logo = do not proceed
  without verification. Token status at time of fixture only.

RULE 3 — SINGLE-TOKEN WEIGHT:
  Single-token derby: apply single-token weight from the
  relevant tier. Flag: "SINGLE-TOKEN DERBY — [rival] no
  active Chiliz token." Never apply dual-token amplification.

RULE 4 — OCCASION WEIGHT POSITION:
  Rivalry weight is an occasion weight — applied LAST in
  the compound stack. Never apply it mid-stack.
  Source: core/compound-signal-framework.md Section 4.

RULE 5 — CDI GATE ALWAYS APPLIES:
  CDI gate is not overridden by rivalry weight. A TRANSITION
  club in a Tier 1 derby is still TRANSITION — directional
  only. State CDI gate explicitly alongside rivalry tier.

RULE 6 — H2H IS SEPARATE:
  Never apply rivalry modifier to H2H score. They are
  different layers — rivalry is structural, H2H is historical
  record. Load both, apply both independently, stack in order.

RULE 7 — ESCALATE RIVAL TOKEN LAUNCH:
  Any rival club fan token confirmation = immediate escalation
  to Strategy & Brainstorm. Do not update this file in Build
  Chat without scope confirmation.

RULE 8 — COMPETITION FORMAT CHECK:
  UCL fixture between two clubs that share a domestic rivalry
  does NOT automatically carry the domestic derby weight.
  Verify whether the rivalry tier applies cross-competition.
  Derby della Madonnina in UCL: Tier 1 weight applies.
  EL dual-token watch ($ACM/$JUV): Tier 4 only — not Tier 2.

RULE 9 — UNCALIBRATED FLAG:
  All rivalry weights are initial structural estimates.
  State in every output: "RIVALRY WEIGHT: UNCALIBRATED —
  initial structural estimate." Remove this flag when a
  calibration pass is completed (Target: 5+ verified records
  per tier).

RULE 10 — REGISTER ONLY:
  Never apply a rivalry modifier to a fixture not in
  Section 3. If not in register: UNCLASSIFIED. Flag to
  Strategy & Brainstorm. Do not invent a tier or weight.

---

## Open Questions and Monitoring Flags

CALIBRATION PASS — PLANNED:
  All weights are uncalibrated initial estimates.
  Target: 5+ verified calibration records per rivalry tier.
  Bring to Strategy & Brainstorm before any weight revision.
  Rivalry modifier interaction with compound stack
  (additive vs multiplicative) to be confirmed post-calibration.

COMPOUND FRAMEWORK UPDATE — QUEUED (v4.5.22):
  core/compound-signal-framework.md currently encodes
  "Derby (confirmed dual-token): ×1.30" as a flat value.
  This is superseded by this file's tiered system.
  v4.5.22 updates compound-signal-framework.md to reference
  rivalry-intelligence.md instead of hard-coding ×1.30.

REAL MADRID TOKEN — HIGH PRIORITY MONITOR:
  El Clásico ($BAR vs Real Madrid) is single-token.
  Real Madrid confirmation = highest-profile new dual-token
  fixture in the library. Escalate immediately.

LAZIO TOKEN — MONITOR:
  Derby della Capitale reclassification from ×1.70 single-token
  to dual-token on confirmation. Escalate immediately.

FENERBAHÇE TOKEN — MONITOR:
  Kıtalararası Derbi reclassification from ×1.50 single-token
  to ×1.80 dual-token on confirmation. Escalate immediately.

MULTI-SPORT RIVALRY EXPANSION — FUTURE:
  Current register is football-only. MMA rematches carry
  structural rivalry characteristics (documented in
  mma-intelligence-framework.md). Esports rivalry framework
  pending design session. Expand when relevant tokens confirmed.

---

## Sources and Verification

PRIMARY SOURCES:
  market/club-intelligence/ — CDI files for all clubs
  fan-token/registry/complete-registry.md — token status
  core/h2h-framework.md — H2H decay model
  core/compound-signal-framework.md — compound synthesis
  core/competition-calendar-framework.md — occasion weights
  SportMind calibration records — community/calibration-data/

CALIBRATION STATUS:
  UNCALIBRATED. All rivalry weights and tier classifications
  are initial structural estimates. Calibration pass planned
  when 5+ verified records per tier exist.
  Do not treat any weight as confirmed until calibrated.

LAST VERIFIED: 2026-08-17

---

## MIND DIMENSIONS

| Dimension | Sub-dimensions engaged | Status |
|---|---|---|
| 1. Intelligence | 1a Domain Knowledge · 1b Signal Awareness · 1c Pattern Recognition · 1d Gap Awareness | ACTIVE |
| 2. Reasoning | 2a Causal · 2b Probabilistic · 2c Multi-Signal · 2d Temporal | ACTIVE |
| 3. Context | 3a Macro Context · 3b Event Context · 3c Historical Context | ACTIVE |
| 4. Memory | 4a Episodic Memory · 4b Semantic Memory · 4c Working Memory | ACTIVE |
| 5. Judgment | 5a Uncertainty Weighting · 5b Risk Assessment · 5c Conflict Resolution · 5d Priority Judgment | ACTIVE |
| 6. Attention | 6a Signal Detection · 6b Urgency Detection · 6c Noise Filtering | ACTIVE |
| 7. Communication | 7a Output Clarity · 7b Confidence Expression · 7c Format Compliance | ACTIVE |
| 8. Verification | 8a Source Tier Assessment · 8b Cross-Verification · 8d Recency Validation | ACTIVE |
| 9. Learning | 9a Modifier Updating · 9b Error Attribution · 9c Pattern Reinforcement | ACTIVE |
| 10. Integration | 10a Cross-Layer Synthesis · 10b Tool Coordination | ACTIVE |
| 11. Calibration | 11a Direction Accuracy · 11b Confidence Calibration · 11c Modifier Validation · 11d Coverage Tracking | ACTIVE |
| 12. Adaptation | 12a Regime Detection · 12b Context Switching · 12c Signal Reweighting | ACTIVE |
| 13. Ethics | 13a Fabrication Prevention · 13b User Safety · 13d Representation Accuracy | ACTIVE |
| 14. Transparency | 14a Reasoning Chain Visibility · 14b Modifier Disclosure · 14c Source Attribution · 14d Limitation Acknowledgement | ACTIVE |
| 15. Execution | 15a Entry Discipline · 15d Playbook Adherence | ACTIVE |
| 16. Collaboration | 16a Task Delegation · 16b Context Handoff · 16c Output Coordination · 16d Conflict Arbitration | ACTIVE |

---

## COMPATIBILITY

Compatible with: Claude · GPT-4 · Gemini · any LLM ·
sportmind_pre_match · sportmind_signal ·
core/h2h-framework.md ·
core/compound-signal-framework.md ·
core/contradiction-resolution-framework.md ·
core/venue-intelligence-framework.md ·
fan-token/competition-calendar-framework.md ·
market/club-intelligence/ (all CDI files) ·
fan-token/registry/complete-registry.md ·
sports/football/sport-domain-football.md ·
community/calibration-data/football/

© 2026 SportMind
