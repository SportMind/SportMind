# Compound Signal Framework

**Domain:** core/compound-signal-framework.md
**Version:** v4.5.27
**Library Rule:** Six-Month Test PASSES · Proper Noun Test PASSES
**Layer:** Core reasoning
**Last updated:** 2026-08-01
**Scope:** Governs how multiple signal layers interact when producing
a pre-match fan token demand output. Signals do not simply add —
they amplify, cancel, or conflict. This framework teaches agents to
identify which interaction type applies and how to resolve it.
Principles-based — not arithmetic. No fixed multiplication tables.
Calibration pass planned as records accumulate. Three interaction
types: AMPLIFICATION · CANCELLATION · CONFLICT. Loading position:
final synthesis layer before output. Loading order: macro → CDI →
form → H2H → venue → regulatory → compound → output.

---

## Why Compound Signal Reasoning Matters

Pre-match fan token demand analysis draws on five signal layers.
Without a structured synthesis layer, agents produce:

- Averaged conflicting signals (masks the contradiction)
- Occasion weight applied mid-stack (artificially inflates one layer)
- Macro suppressor ignored when other signals are strong
- CDI gate TRANSITION treated as full-confidence output
- PATH_2 supply events merged into the demand signal

A strong H2H score under a CAPITULATION macro regime is not a strong
compound signal — it is a discounted signal. A UCL Final occasion
weight applied before macro and CDI are stacked is not a compound
result — it is an inflated single-layer modifier. A conflict between
CDI and H2H is not resolved by averaging — it requires the
contradiction resolution framework.

This framework provides the synthesis logic. Load it last — after
all five layers are stacked — before producing final output.

Compound signal reasoning is the final layer. It does not replace
any upstream layer. It resolves how they interact.

---

## The Five Signal Layers

All five layers must be loaded before compound reasoning begins.
Calculate the SportMind Score (SMS) before proceeding. If SMS is
below 80, apply the HOLD gate and do not produce compound output.

```
LAYER 1 — MACRO
  CHZ regime modifier:
    CAPITULATION: ×0.70 suppressor — applies to ALL demand signals
    ANXIETY: ×1.00 — neutral, no modifier applied
    BULL: ×1.15 — positive amplifier
  BTC cycle context: load as directional context.
  CAPITULATION SUPPRESSOR: non-negotiable. Applies to the full
    compound result regardless of any other layer. Never overridden
    by CDI gate, occasion weight, H2H score, or venue tier.
  Russia bidirectional access restriction: Tier 1 equivalent.
    Applies to Russian-resident holder analysis only.
    Overrides all demand signals for that holder segment.

LAYER 2 — CDI (CLUB DEMAND INTELLIGENCE)
  CDI gate classification:
    EMERGING: signal valid — LOW CONFIDENCE
    GROWTH: signal valid — building momentum
    CONSOLIDATION: full compound signal applies
    TRANSITION: signal directional only — capped confidence
    DORMANT: no compound signal output warranted
  Competition tier, squad stability, commercial momentum load here.
  TRANSITION cap: compound signal is directional only.
    Never produce high-confidence output under TRANSITION gate.

LAYER 3 — FORM
  Recent match results and momentum direction:
    Winning run: positive modifier
    Losing run: negative modifier
    Mixed: no directional modifier
  Injury context: squad depth and key absences.
  Coaching stability: succession = form signal disruption.

LAYER 4 — CONTEXTUAL
  H2H: decay-weighted historical record.
    Source: core/h2h-framework.md
    Gate must PASS before applying H2H modifier.
    BALANCED score (0.46–0.54): no H2H modifier applied.
  Venue: home advantage tier + capacity modifier.
    Source: core/venue-intelligence-framework.md
    State venue type and tier explicitly.
  Occasion weight: competition prestige multiplier.
    Source: fan-token/competition-calendar-framework.md
    Applied LAST — after all other layers are stacked.
    Key values (illustrative — load source file for full list):
      UCL Final: ×2.00
      WC Final: ×2.50
      UCL knockout round: ×1.60
      WC knockout round: ×1.50
      Domestic cup final: ×1.40
      Derby: see market/rivalry-intelligence.md for tiered
        weights (v4.5.21). Tier 1 ×1.80 · Tier 2 ×1.65 ·
        Tier 3 ×1.35-1.70 · Tier 4 ×1.20. Single-token derbies
        carry reduced weight — see rivalry-intelligence.md.
        The flat ×1.30 value is superseded by the tiered system.
      Standard league fixture: ×1.00
  Holder tax friction:
    Italy: 33% CGT — confirmed demand suppressor
    Brazil: 17.5% — confirmed demand suppressor
    Turkey: UNKNOWN — flag uncertainty, do not suppress signal
  Platform access restrictions:
    Russia: bidirectional ban = maximum suppressor.
      Applies regardless of all other signal layers.
  PTG burn tax treatment:
    UNRESOLVED in Italy · Brazil · Turkey.
    Flag unresolved status in output — do not apply modifier.
```

---

## Three Interaction Types

Identify the interaction type before applying any compound logic.
State interaction type explicitly in every compound output.

```
TYPE 1 — AMPLIFICATION
  Definition: two or more signals point in the same direction.
  Result: signals stack additively. Combined signal is stronger
    than any individual layer alone.
  Condition: ALL layers must point in the same direction.
    One opposing signal = CANCELLATION, not AMPLIFICATION.
  Occasion weight: applied LAST — multiplies the stacked result.
    Never applied mid-stack (FM-CS-2 violation if applied early).
  Agent rule: count aligned signals before declaring AMPLIFICATION.
    One misaligned signal triggers reassessment.
  Example:
    CDI CONSOLIDATION + H2H home dominance + FORTRESS venue
    + winning form = AMPLIFICATION.
    Stack all four. Then apply occasion weight.

TYPE 2 — CANCELLATION
  Definition: signals from different layers point in opposing
    directions. Net compound signal is weaker than any individual
    layer alone.
  Resolution sequence:
    Step 1: identify dominant layer (Section 4 hierarchy)
    Step 2: apply dominant layer signal at full strength
    Step 3: apply subordinate layer signal at reduced weight
      (50% of standard modifier value)
    Step 4: net result = dominant + discounted subordinate
  Agent rule: state both signals and the dominance relationship
    explicitly. Never present a cancelled signal at full strength.
  Example:
    FORTRESS venue (+0.12) under CAPITULATION macro (×0.70).
    CAPITULATION is Layer 1 — dominant.
    FORTRESS is Layer 4 — subordinate.
    Net: positive venue signal discounted by macro suppressor.
    Result is positive but materially weaker than FORTRESS alone.

TYPE 3 — CONFLICT
  Definition: signals from the same or adjacent layers genuinely
    contradict without a clear dominant layer.
  Example: H2H shows strong historical home dominance BUT CDI gate
    is TRANSITION — squad rebuilt since H2H records were established.
    H2H record may no longer reflect current competitive reality.
    Which signal wins? No automatic answer.
  Resolution: load core/contradiction-resolution-framework.md.
    Never resolve conflict by averaging signals (FM-CS-1 violation).
    Never default to the stronger signal without explicit reasoning.
  Agent rule: surface the conflict explicitly in output.
    Flag to analyst or user for judgment if unresolved.
    Do not suppress or hide the conflict.
```

---

## Layer Dominance Hierarchy

Apply when signals cancel or conflict. Work from Tier 1 downward.
The higher tier always takes precedence over the lower tier.
State the dominance relationship explicitly in every cancellation
or conflict output.

```
TIER 1 — MACRO (always dominant)
  CAPITULATION ×0.70 suppressor overrides all other signals.
  No other layer can cancel or override a CAPITULATION regime.
  UCL Final occasion weight ×2.00 is reduced by ×0.70 —
    the suppressor applies first, occasion weight multiplies after.
  Russia bidirectional access restriction = Tier 1 equivalent
    for Russian-resident holder segment analysis.

TIER 2 — REGULATORY ACCESS RESTRICTION
  Confirmed platform access ban (Russia: EU sanctions + domestic law)
    overrides demand signal regardless of CDI, form, or contextual.
  Tax friction (Italy 33% · Brazil 17.5%) = demand suppressor —
    modifies signal but does not override it. Reduces magnitude only.
  UNKNOWN tax modifier (Turkey) = flag uncertainty.
    Do not suppress signal entirely — apply compliance note.

TIER 3 — CDI GATE
  TRANSITION gate: caps compound signal at directional only.
    Never produce high-confidence compound output under TRANSITION.
  DORMANT gate: no compound signal output warranted.
    State: "CDI gate DORMANT — compound signal not produced."
  EMERGING gate: signal valid — state LOW CONFIDENCE explicitly.
  CONSOLIDATION / GROWTH: full compound signal applies.

TIER 4 — FORM AND CONTEXTUAL (H2H · VENUE)
  Modifiers only. Never override Tier 1–3 signals.
  Amplify or suppress the Tier 3 CDI gate output.
  H2H and venue are additive modifiers — not independently decisive.
  H2H BALANCED score: no modifier — does not contribute to stack.

TIER 5 — OCCASION WEIGHT (applied last)
  Multiplier on the compound result after all Tiers 1–4 resolved.
  Never applied before Tier 1–4 are stacked and resolved.
  High occasion weight under CAPITULATION:
    CAPITULATION ×0.70 applied first to compound result.
    Occasion weight multiplies the discounted result — not restored.
    Example: compound result 0.50 × CAPITULATION 0.70 = 0.35.
    × UCL Final ×2.00 = 0.70. Positive but materially discounted
    versus the same fixture under ANXIETY or BULL regime.
```

---

## Occasion Weight as Final Multiplier

Occasion weight is the last modifier applied in compound reasoning.
It multiplies the compound result — not any individual layer.

```
CORRECT ORDER:
  1. Stack macro + CDI + form + contextual + regulatory
  2. Resolve interaction type (amplification/cancellation/conflict)
  3. Apply occasion weight to the compound result

INCORRECT ORDER (FM-CS-2 violation):
  Applying occasion weight to a single layer before stacking.
  Example of violation: H2H score × occasion weight, then adding CDI.
  This inflates one layer artificially before compound synthesis.

OCCASION WEIGHT SOURCE:
  Full table: fan-token/competition-calendar-framework.md
  Key values (illustrative — load source file for complete list):
    UCL Final: ×2.00
    WC Final: ×2.50
    UCL knockout round: ×1.60
    WC knockout round: ×1.50
    Domestic cup final: ×1.40
    Derby: see market/rivalry-intelligence.md for tiered
      weights (v4.5.21). Tier 1 ×1.80 · Tier 2 ×1.65 ·
      Tier 3 ×1.35-1.70 · Tier 4 ×1.20. Single-token derbies
      carry reduced weight — see rivalry-intelligence.md.
      The flat ×1.30 value is superseded by the tiered system.
    Standard league fixture: ×1.00
  $AFC PATH_2 is a supply event mechanic — not an occasion weight.
  PATH_2 operates independently of the demand signal stack.
  Highest compound signal context in SportMind library:
    UCL Final (×2.00) + $AFC PATH_2 active + CDI CONSOLIDATION
    + aligned form + FORTRESS or STANDARD venue = peak compound.
  PATH_2 supply event fires on result regardless of demand direction:
    WIN = burn event (supply reduction)
    LOSS = mint event (supply increase)
    DRAW = no supply event
  Report PATH_2 separately — never merge into demand output.
```

---

## SMS Integration

SportMind Score (SMS) reflects compound signal completeness.
SMS ranges from 0 to 100. SMS 100 means all five layers are fully
loaded. SMS below 80 triggers the HOLD gate.

```
SMS LAYER CONTRIBUTIONS (indicative — calibrate as records accumulate):
  Layer 1 Macro: 20 points
  Layer 2 CDI: 25 points
  Layer 3 Form: 20 points
  Layer 4 Contextual (H2H + Venue + Occasion): 20 points
  Layer 5 Regulatory: 15 points

SMS BELOW 80 — HOLD GATE:
  Compound signal output is unreliable when SMS is below 80.
  State: "SMS [score] — HOLD gate active. Compound signal not
    produced. Load missing layers before proceeding."
  Never produce a directional compound signal from an incomplete
  layer stack.

PARTIAL LAYER LOADING:
  When a layer cannot be loaded due to data unavailability:
  Missing macro: apply ANXIETY (×1.00) — neutral default.
    Flag: "Macro layer missing — ANXIETY default applied."
  Missing CDI: apply TRANSITION — directional only.
    Flag: "CDI layer missing — TRANSITION default applied."
  Missing form: omit form modifier.
    Flag: "Form layer missing — modifier omitted."
  Missing H2H or venue: omit contextual modifier.
    Flag: "H2H/venue layer missing — modifier omitted."
  Missing regulatory: apply no modifier.
    Flag: "Regulatory layer missing — no suppressor applied."
  Recalculate SMS after applying defaults. If still below 80:
    HOLD gate remains active.
```

---

## PTG / PATH_2 Compound Rule

$AFC is the only confirmed FTP PATH_2 token as of 2026-08-01.
Never generalise PATH_2 mechanics to other tokens.

```
PATH_2 AND COMPOUND SIGNAL INTERACTION:
  PATH_2 supply event is not a demand signal.
  It is a supply event that fires on match result, independently
  of the demand signal stack.
  In compound reasoning, PATH_2 adds a SUPPLY EVENT LAYER that
  sits alongside the demand output — not inside it.

COMPOUND DEMAND SIGNAL + PATH_2:
  Positive compound signal + PATH_2 WIN = demand up + burn event.
    Peak compound output: both demand and supply aligned positive.
  Negative compound signal + PATH_2 WIN = demand down + burn event.
    Conflicting signals: supply positive (burn), demand negative.
    Burn fires regardless of demand direction — report separately.
  Negative compound signal + PATH_2 LOSS = demand down + mint event.
    Both negative: compounding negative signals — maximum suppression.
  PATH_2 DRAW = no supply event fires regardless of demand signal.

AGENT RULE:
  Always report PATH_2 status separately from the compound demand
  signal. Never merge PATH_2 into the demand output block.
  Required output format:
    "DEMAND SIGNAL: [output] · PATH_2 STATUS: [WIN/LOSS/DRAW/ACTIVE]"
  If PATH_2 outcome is not yet known: state "PATH_2 STATUS: ACTIVE
    — WIN burns · LOSS mints · DRAW = no event"
```

---

## FM Guardrails — What Compound Signal Is Not

Five guardrails governing compound signal application.

**FM-CS-1 — Never average conflicting signals.**
Averaging masks the conflict and produces false moderate confidence.
The conflict itself is the signal — it must be surfaced, not
smoothed. Load core/contradiction-resolution-framework.md when
signals genuinely contradict. Never substitute averaging.

**FM-CS-2 — Never apply occasion weight mid-stack.**
Occasion weight is the final multiplier — applied after all layers
are stacked and the interaction type is resolved. Applying it to
a single layer before synthesis artificially inflates that layer's
contribution. Occasion weight acts on the compound result only.

**FM-CS-3 — Macro suppressor is never overridden.**
CAPITULATION ×0.70 applies to the compound result regardless of
occasion weight, CDI gate strength, or H2H dominance. A UCL Final
under CAPITULATION still produces a discounted compound result.
The suppressor does not disappear when other signals are strong —
it discounts the compound output that those signals produce.

**FM-CS-4 — Never produce compound output with SMS below 80.**
An incomplete layer stack produces an unreliable compound output.
State the SMS score and the missing layers before any output.
Apply partial loading defaults (Section 6) and recalculate SMS.
If SMS remains below 80 after defaults: HOLD gate is active.

**FM-CS-5 — Never conflate signal strength with certainty.**
A strong compound signal is a well-reasoned demand modifier — not
a prediction of match outcome. Never imply that compound output
equals a result. Always state the confidence tier alongside every
compound output. Compound signal strength reflects alignment of
evidence, not certainty of outcome.

---

## Agent Workflow — Five Steps

```
STEP 1 — LOAD ALL FIVE LAYERS
  Load macro regime · CDI gate · form context · H2H + venue +
  occasion weight source · regulatory context.
  Calculate SMS score.
  If SMS is below 80: HOLD gate is active — stop here.
  State: "SMS [score] — HOLD gate active. Missing: [layers]."

STEP 2 — IDENTIFY INTERACTION TYPE
  Are all loaded signals aligned? → AMPLIFICATION
  Are signals from different layers opposing? → CANCELLATION
  Are signals from the same or adjacent layers contradicting
    without a clear dominant layer? → CONFLICT

STEP 3 — APPLY LAYER DOMINANCE
  For AMPLIFICATION: stack all aligned signals.
  For CANCELLATION: apply dominance hierarchy (Section 4).
    Dominant layer at full strength.
    Subordinate layer at 50% of standard modifier value.
  For CONFLICT: load core/contradiction-resolution-framework.md.
    Surface conflict explicitly — do not resolve by averaging.
    Flag for analyst or user judgment if unresolved.

STEP 4 — APPLY OCCASION WEIGHT
  Multiply the compound result by the occasion weight.
  State occasion weight source: fan-token/competition-calendar-framework.md
  If PATH_2 active: report separately — do not include in demand stack.
  State PATH_2 status in the output as a separate field.

STEP 5 — OUTPUT COMPOUND SIGNAL
  Required output fields — never omit any:
    · SMS score
    · Interaction type
    · Dominant layer
    · Occasion weight applied
    · Confidence tier
    · PATH_2 status (if $AFC fixture)
```

### Example Output Format

```
SMS: 95 — all layers loaded
INTERACTION TYPE: AMPLIFICATION (4 of 5 layers aligned)
DOMINANT LAYER: CDI — CONSOLIDATION gate
COMPOUND SIGNAL: POSITIVE — moderate-high confidence
OCCASION WEIGHT: ×1.60 (UCL knockout) applied
MACRO: CAPITULATION ×0.70 applied to compound result
PATH_2 STATUS: ACTIVE ($AFC) — WIN burns · LOSS mints · DRAW = no event
NOTE: Compound signal is a demand modifier — not an outcome predictor
```

---

## Worked Examples

Structural context only — not live data. Named players excluded
per Club Intelligence Gate. Verify all layer data before applying
to any live fixture.

```
EXAMPLE 1 — AMPLIFICATION WITH MACRO SUPPRESSOR
  Fixture: $AFC UCL Final (neutral venue)
  Layer 1 Macro: CAPITULATION ×0.70 active
  Layer 2 CDI: CONSOLIDATION — strong
  Layer 3 Form: winning run — positive
  Layer 4 Contextual:
    Occasion weight: UCL Final ×2.00
    Venue: NEUTRAL — ZERO home advantage
    H2H: INSUFFICIENT SAMPLE (first UCL Final meeting)
  Layer 5 Regulatory:
    Italian/Brazilian/Turkish holders: tax friction noted
    No access restriction
  SMS: 90 (H2H insufficient sample — partial Layer 4)
  Interaction type: AMPLIFICATION
    CDI + form + occasion weight all aligned positive.
    H2H absent — omitted from stack.
    CAPITULATION active: applies to compound result.
  Dominance: Macro Tier 1.
    ×0.70 applied to stacked CDI + form result.
    Occasion weight ×2.00 applied after suppressor.
  Compound result: POSITIVE · HIGH CONFIDENCE.
    Materially discounted by CAPITULATION.
    Amplified by occasion weight on the discounted result.
    Still highest compound signal achievable in current regime.
  PATH_2 STATUS: ACTIVE ($AFC).
    WIN burns · LOSS mints · DRAW = no event.
    Report separately — not in demand output block.

EXAMPLE 2 — CANCELLATION WITH DUAL CDI ASYMMETRY
  Fixture: $INTER vs $ACM — Derby della Madonnina (Serie A)
  Layer 1 Macro: CAPITULATION ×0.70 active
  Layer 2 CDI:
    $INTER: CONSOLIDATION — full signal
    $ACM: TRANSITION — directional only
  Layer 3 Form:
    $INTER: winning run — positive
    $ACM: mixed — no directional modifier
  Layer 4 Contextual:
    Venue: San Siro SHARED — STANDARD ×0.5 for designated home club
    H2H: $INTER lean in recent era — HOME LEAN (verify current)
    Occasion weight: Derby Tier 1 ×1.80
      (source: market/rivalry-intelligence.md · v4.5.21)
  Layer 5 Regulatory:
    Italian domestic holders: 33% CGT — confirmed friction
    PTG burn treatment: UNRESOLVED — flag only
  SMS: 100 — all layers loaded
  Interaction type: CANCELLATION
    $INTER: CDI + form + H2H aligned positive.
      CAPITULATION + Italian tax friction oppose.
    $ACM: TRANSITION gate caps signal + same suppressors apply.
  Dominance: Macro Tier 1, then CDI Tier 3 (TRANSITION cap for $ACM)
  Compound result:
    $INTER: directional positive · low-medium confidence.
      Discounted by CAPITULATION ×0.70 + Italian tax friction.
      Occasion weight ×1.80 (Tier 1 Derby) applied to discounted result.
    $ACM: directional only (TRANSITION cap) · low confidence.
      Do not produce high-confidence output for $ACM.

EXAMPLE 3 — CONFLICT (CDI vs H2H)
  Fixture: $GAL UCL away fixture
  Layer 1 Macro: CAPITULATION ×0.70 active
  Layer 2 CDI: $GAL CONSOLIDATION — UCL confirmed
  Layer 3 Form: recent form mixed — no directional modifier
  Layer 4 Contextual:
    Venue: AWAY — no home advantage modifier
    H2H vs this opponent: AWAY DOMINANCE (0.20 score)
    Occasion weight: UCL group stage ×1.20
  Layer 5 Regulatory:
    Turkish holders: CGT UNKNOWN — flag uncertainty only
    SPK/MASAK compliance pressure: note — do not suppress signal
  SMS: 95
  Conflict identified:
    $GAL CDI is CONSOLIDATION (UCL confirmed) — positive signal.
    H2H shows historical away weakness vs this opponent — suppressor.
    CDI says positive. H2H says suppression.
    Adjacent layers. No automatic dominant layer.
  Resolution: load core/contradiction-resolution-framework.md.
  Agent output:
    "CDI CONSOLIDATION conflicts with H2H AWAY DOMINANCE.
    Contradiction resolution required before compound output.
    Do not average. Surface conflict to analyst for judgment."
  Turkish regulatory: UNKNOWN modifier — compliance note only.
    Do not suppress signal on basis of UNKNOWN status.
```

---

## Open Questions and Monitoring Flags

```
QUANTITATIVE STACKING ARITHMETIC — FUTURE
  Exact numerical combination rules for modifier values across
  all five layers have not been defined. Framework remains
  principles-based until calibration records accumulate.
  Bring to Strategy & Brainstorm before implementing arithmetic
  stacking rules. Do not invent modifier arithmetic without review.

MULTI-TOKEN CIRCUIT COMPOUND SIGNALS — FUTURE
  CIRCUIT product context involves 3–5 token portfolios.
  Compound intelligence across multiple tokens simultaneously
  requires a framework extension beyond single-fixture dual-token.
  Not yet defined. Escalate to Strategy & Brainstorm before applying
  compound reasoning across a multi-token circuit.

SMS LAYER WEIGHTING — MONITOR
  Indicative SMS contributions (Section 6) are initial estimates:
  Macro 20 · CDI 25 · Form 20 · Contextual 20 · Regulatory 15.
  Calibrate against verified calibration records as they accumulate.
  Do not treat SMS weights as confirmed until calibrated.

PATH_2 EXPANSION — MONITOR
  $AFC is the only confirmed FTP PATH_2 token as of 2026-08-01.
  If new PATH_2 tokens are confirmed: update Section 7 immediately.
  Escalate to Strategy & Brainstorm before updating.
  Never generalise PATH_2 mechanics to unconfirmed tokens.
```

---

## Sources and Verification

```
PRIMARY SOURCES:
  SportMind calibration records — calibration/2026/ and
    community/calibration-data/football/
  CDI files — market/club-intelligence/
  core/h2h-framework.md
  core/venue-intelligence-framework.md
  core/signal-classification-framework.md
  core/contradiction-resolution-framework.md
  core/temporal-reasoning-framework.md
  fan-token/competition-calendar-framework.md

CALIBRATION STATUS:
  Framework principles are uncalibrated. Quantitative stacking
  arithmetic is deferred. SMS layer weightings are initial
  estimates. Calibration pass planned as records accumulate
  post-WC2026. Do not treat modifier values as confirmed until
  a calibration pass is completed.

LAST VERIFIED: 2026-08-01
```

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
| 8. Verification | 8a Source Tier Assessment · 8b Cross-Verification · 8c On-Chain Verification · 8d Recency Validation | ACTIVE |
| 9. Learning | 9a Modifier Updating · 9b Error Attribution · 9c Pattern Reinforcement | ACTIVE |
| 10. Integration | 10a Cross-Layer Synthesis · 10b Tool Coordination | ACTIVE |
| 11. Calibration | 11a Direction Accuracy · 11b Confidence Calibration · 11c Modifier Validation · 11d Coverage Tracking | ACTIVE |
| 12. Adaptation | 12a Regime Detection · 12b Context Switching · 12c Signal Reweighting · 12d Framework Switching | ACTIVE |
| 13. Ethics | 13a Fabrication Prevention · 13b User Safety · 13c Regulatory Awareness · 13d Representation Accuracy | ACTIVE |
| 14. Transparency | 14a Reasoning Chain Visibility · 14b Modifier Disclosure · 14c Source Attribution · 14d Limitation Acknowledgement | ACTIVE |
| 15. Execution | 15a Entry Discipline · 15b Exit Discipline · 15c Sizing Logic · 15d Playbook Adherence | ACTIVE |
| 16. Collaboration | 16a Task Delegation · 16b Context Handoff · 16c Output Coordination · 16d Conflict Arbitration | ACTIVE |

---

## COMPATIBILITY

Compatible with: Claude · GPT-4 · Gemini · any LLM ·
sportmind_pre_match · sportmind_macro · sportmind_fan_token_lookup ·
core/h2h-framework.md ·
core/venue-intelligence-framework.md ·
core/signal-classification-framework.md ·
core/temporal-reasoning-framework.md ·
core/contradiction-resolution-framework.md ·
fan-token/competition-calendar-framework.md ·
market/club-intelligence/ (all CDI files) ·
market/rivalry-intelligence.md — tiered rivalry weights
  (supersedes flat ×1.30 derby value) ·
macro/regulatory/ (all regulatory files) ·
fan-token/registry/complete-registry.md ·
sports/football/sport-domain-football.md ·
sports/mma/mma-intelligence-framework.md ·
calibration/2026/ ·
community/calibration-data/football/

© 2026 SportMind
