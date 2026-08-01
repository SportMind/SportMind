# H2H Framework

**Domain:** core/h2h-framework.md
**Version:** v4.1.81
**Library Rule:** Six-Month Test PASSES · Proper Noun Test PASSES
**Scope:** Head-to-head historical record framework for SportMind
agent pre-match signal generation. H2H records are historical
context — not predictive certainty. Three structured outputs:
relevance gate (PASS/FAIL/NOT APPLICABLE), decay-weighted H2H
confidence score (0.0–1.0), and dual-token demand modifier.
Additive to CDI, macro, and regulatory signals — never replace.
Loading order: macro → CDI → form → H2H → regulatory → output.

---

## Why H2H Intelligence Matters

Head-to-head history is one of the most frequently cited inputs
in pre-match analysis — and one of the most frequently misapplied.
Raw H2H records ignore:

- How long ago the meetings occurred
- Whether the squads or managers are the same
- Whether the competition tier was equivalent
- Whether the sample is large enough to be meaningful
- Whether both teams have active fan tokens

An agent that applies a 10-year-old H2H record without decay, or
draws conclusions from three meetings, or applies a lower-tier
record to a higher-tier fixture, is producing a misleading signal.
This framework eliminates those failure modes through a structured
gate, decay model, and explicit output format.

H2H intelligence is additive. It does not replace macro regime
checks, CDI gate classification, or regulatory overlays. Load it
after those layers, not instead of them.

---

## The Relevance Gate — Five Conditions

All five conditions must pass before H2H intelligence is applied.
State gate result explicitly in every signal output.

### Condition 1 — Competitive Fixture Only

Friendly matches, preseason games, exhibition fixtures, and neutral
warmups are excluded from H2H records and analysis.

```
PASS: Competitive league, cup, or continental fixture
FAIL: Friendly, preseason, exhibition, neutral warmup
NOT APPLICABLE: No prior competitive meetings exist
```

### Condition 2 — Same Competition Tier or Higher

H2H records from a lower competition tier applied to a higher-tier
fixture require a weight reduction. The reverse does not apply.

```
SAME TIER: No adjustment
HIGHER TIER RECORD APPLIED TO CURRENT: No adjustment
LOWER TIER RECORD APPLIED TO HIGHER TIER FIXTURE: ×0.70 weight
U21 / YOUTH RECORDS: Never applied to senior fixtures — GATE FAILS
```

### Condition 3 — Minimum Three Competitive Meetings

Fewer than three competitive meetings produces an insufficient sample
for H2H signal generation.

```
3+ meetings: GATE PASSES (proceed to decay model)
Fewer than 3: GATE FAILS
Output: "H2H: INSUFFICIENT SAMPLE" — never "H2H: 50/50"
```

The difference matters. "Insufficient sample" is an honest statement
about data availability. "50/50" implies balanced evidence where none
exists. Never use "50/50" as a substitute for "insufficient sample."

### Condition 4 — Dual-Token Status Check

H2H records are valid for single-token analysis. Dual-token demand
modifiers in Section 4 require at least one meeting while both tokens
were active on Chiliz Chain.

```
Both tokens active in at least one prior meeting: DUAL-TOKEN eligible
Only one token active in all prior meetings: SINGLE-TOKEN H2H only
```

Single-token H2H still applies to signal output if other conditions
pass — but the dual-token amplification section is not applied.

### Condition 5 — Squad and Manager Continuity Check

Significant changes to squad composition or management since the
H2H records were established require a discount to reflect reduced
comparability.

```
Full rebuild (60%+ lineup change AND new manager): ×0.50 discount
Partial rebuild OR manager change only: ×0.30 discount
No significant change: No discount
```

Apply this discount to the decay-weighted score before scoring.

### Gate Output Format

```
H2H GATE: PASS (5 conditions met)
OR
H2H GATE: FAIL — [condition number and reason]
OR
H2H GATE: NOT APPLICABLE — [reason]
```

---

## The Decay Model

H2H records decay over time. A meeting from six seasons ago carries
less weight than a meeting from last season. This section defines
the decay curve, accelerators, score bands, and sample confidence
tiers.

### Decay Weights by Season

Decay unit is seasons elapsed since each meeting.

| Seasons ago | Decay weight |
|---|---|
| Current season | 1.00 |
| 1 season ago | 0.85 |
| 2 seasons ago | 0.70 |
| 3 seasons ago | 0.55 |
| 4 seasons ago | 0.40 |
| 5 seasons ago | 0.25 |
| 6+ seasons ago | 0.10 (floor) |

Decay floor: no individual meeting drops below 0.05 regardless
of age.

### Decay Accelerators

Accelerators are applied multiplicatively to the decay weight of
affected meetings. Multiple accelerators stack multiplicatively.

| Event | Multiplier |
|---|---|
| Manager succession (either side) | ×0.80 |
| Squad rebuild (40%+ lineup change) | ×0.85 |
| Promotion or relegation (either side) | ×0.75 |
| Competition format change | ×0.90 |

Example: a meeting 2 seasons ago (base: 0.70) where one side
subsequently had a manager change (×0.80) and a squad rebuild
(×0.85) gives: 0.70 × 0.80 × 0.85 = 0.476.

### Scoring Calculation

```
STEP 1: Apply decay weight to each meeting outcome
  Win: outcome value = 1.0
  Draw: outcome value = 0.5
  Loss (from home perspective): outcome value = 0.0

STEP 2: Apply accelerators to individual meetings where triggered

STEP 3: Apply Condition 5 continuity discount to weighted total

STEP 4: Normalise to 0.0–1.0 scale
  Score = sum of (decay weight × outcome) ÷ sum of decay weights

STEP 5: Assign score band and confidence tier
```

### Score Bands

| Score | Band | Modifier applied |
|---|---|---|
| 0.65–1.00 | HOME DOMINANCE | Yes |
| 0.55–0.64 | HOME LEAN | Yes |
| 0.46–0.54 | BALANCED | No modifier applied |
| 0.36–0.45 | AWAY LEAN | Yes |
| 0.00–0.35 | AWAY DOMINANCE | Yes |

BALANCED range: no H2H modifier is applied. The record does not
provide a meaningful directional signal.

### Sample Confidence Tiers

| Meetings | Confidence tier |
|---|---|
| 3–5 | LOW CONFIDENCE |
| 6–10 | MODERATE CONFIDENCE |
| 11–20 | HIGH CONFIDENCE |
| 20+ | VERY HIGH CONFIDENCE |

Always state the confidence tier alongside the H2H score. A score
of 0.70 from 4 meetings (LOW CONFIDENCE) is a fundamentally
different signal from a score of 0.70 from 18 meetings
(HIGH CONFIDENCE).

---

## Dual-Token H2H Amplification

Applies when: both clubs have active Chiliz fan tokens AND the
relevance gate passes AND the score falls outside the BALANCED range.

### Amplification Values

Dominant side (higher score): **+0.10 demand amplifier**

Subordinate side: two mutually exclusive patterns.

**Pattern A — Suppression (default):**
```
Modifier: -0.08
Applies: whenever Pattern B conditions are not met
```

**Pattern B — Contrarian Spike:**
```
Modifier: +0.06
Triggers — ALL THREE required:
  · H2H score 0.75+ (dominant) or 0.25- (subordinate away dominance)
  · Tier 1 narrative framing (rivalry, local derby, cup final)
  · Subordinate side in strong current form (independent signal)

Pattern A and Pattern B are mutually exclusive.
Never apply both to the same token in the same analysis.
```

### Familiarity Discount

When an H2H pattern is so well-established that it is already
priced into holder behaviour, apply a ×0.50 familiarity discount
to the dual-token amplification values.

Fixtures with familiarity discount as of 2026-07-31:

```
EL CLÁSICO — $BAR vs $ATM (La Liga)
  Note: Real Madrid has no active Chiliz fan token as of
  2026-07-31. El Clásico ($BAR vs Real Madrid) is a
  single-token fixture. $BAR vs $ATM is the dual-token
  La Liga pairing — apply familiarity discount.

DERBY DELLA MADONNINA — $INTER vs $ACM (Serie A / UCL)
  Both clubs confirmed active Chiliz Chain tokens.
  Familiarity discount applies.

PSG vs BAR (UCL)
  Apply when 3+ UCL meetings in previous 10 years.
  Verify meeting count before applying discount.

AFC vs CITY (Premier League / domestic cup)
  $AFC is the only confirmed FTP PATH_2 token.
  PATH_2 supply events are independent of H2H signal —
  never conflate H2H modifier with PATH_2 activation.
  Familiarity discount applies.

JUV vs INTER (Serie A / Coppa Italia)
  Note: $JUV CDI gate is TRANSITION (Europa League 2026-27).
  Apply CDI gate context before H2H modifier.
  Familiarity discount applies.
```

---

## FM Guardrails — What H2H Is Not

Six failure modes specific to H2H misapplication.

**FM-H2H-1 — H2H as outcome predictor**
H2H is a demand signal modifier — not a prediction of match
outcome. Never imply directional certainty from H2H alone.
Never say "they always win here" — say "H2H score 0.72,
HOME LEAN, moderate confidence."

**FM-H2H-2 — Raw record without decay**
Applying a 10-year unweighted record is FM-H2H-2. Decay is
mandatory. Never use raw win-draw-loss counts without applying
the decay model.

**FM-H2H-3 — High confidence from small samples**
3–5 meetings is LOW CONFIDENCE regardless of the score value.
Always state confidence tier. Never express strong conviction
from a sample of 4.

**FM-H2H-4 — Cross-tier application without weight reduction**
Applying a UCL H2H record to a domestic league fixture as
direct equivalent is FM-H2H-4. Tier weight reduction (×0.70)
is mandatory when applying lower-tier records to higher-tier
fixtures.

**FM-H2H-5 — Pre-rebuild records without continuity discount**
A manager succeeded two seasons ago and 65% of the lineup
changed. The pre-succession H2H record requires a ×0.50
continuity discount. Never apply pre-rebuild records as if the
same squad is playing.

**FM-H2H-6 — Pattern A and Pattern B simultaneously**
Pattern A (suppression) and Pattern B (contrarian spike) are
mutually exclusive. Applying both modifiers to the same token
in the same analysis is a framework violation. Determine which
pattern applies — then apply only that one.

---

## Multi-Sport Application

### Football

Full framework as defined above. Season unit = one league season
in the primary competition of the clubs involved.

### MMA

Year-based decay for MMA (no season structure).

| Years since meeting | Decay weight |
|---|---|
| Within 1 year | 0.80 |
| 1–2 years | 0.60 |
| 3+ years | 0.35 |

MMA-specific rules:
- Rematches are HIGH VALUE — the first meeting primes audience
  demand, and rematches carry a narrative amplifier above the
  H2H score alone
- Weight class change since last meeting: ×0.50 discount
  (different physical contest)
- No squad rebuild accelerator — individual sport
- Minimum 2 prior meetings (not 3) given the lower volume
  of individual fighter matchups
- Apply mma-intelligence-framework.md before H2H layer

### Other Sports

Use the football model as the structural default. Always state
explicitly that the framework is being applied to a non-football
sport with a caveat. Consult the sport-specific framework file
before applying (sports/ directory).

---

## Agent Application Workflow — Six Steps

```
STEP 1 — GATHER H2H DATA
  Retrieve historical competitive meeting record.
  If no data available: state "H2H: NO DATA" and proceed
  without H2H layer. Never infer or estimate historical record.
  Never fabricate meeting outcomes.

STEP 2 — RUN RELEVANCE GATE
  Check all five conditions in order.
  State gate result explicitly:
    H2H GATE: PASS (5 conditions met)
    H2H GATE: FAIL — Condition [N]: [reason]
    H2H GATE: NOT APPLICABLE — [reason]
  If gate fails: stop. Do not proceed to decay model.

STEP 3 — APPLY DECAY MODEL
  Apply decay weights to each meeting.
  Apply accelerators where triggered.
  Apply Condition 5 continuity discount if applicable.
  Calculate normalised score (0.0–1.0).
  Assign score band and confidence tier.
  Output: score + band + confidence tier + meeting count.

STEP 4 — APPLY DUAL-TOKEN MODIFIER (if applicable)
  Check: both tokens active? Score outside BALANCED range?
  Determine Pattern A or Pattern B — never both.
  Apply familiarity discount if fixture qualifies.
  State modifier values explicitly.

STEP 5 — INTEGRATE WITH OTHER SIGNALS
  H2H is additive. Apply as a modifier to the existing
  signal stack, not as an override. Macro regime check
  and CDI gate must already be applied before H2H layer.

STEP 6 — STATE GUARDRAILS IN OUTPUT
  Include in every H2H output:
    · Gate result
    · Score + band + confidence tier
    · FM note (H2H is a demand signal modifier — not
      outcome predictor)
    · Dual-token modifiers if applicable
    · Familiarity discount status
```

### Example Output Format

```
H2H GATE: PASS (5 conditions met)
H2H SCORE: 0.68 (HOME LEAN · MODERATE CONFIDENCE · 8 meetings)
H2H MODIFIER: +0.08 applied to home token demand signal
DUAL-TOKEN: subordinate token PATTERN A (suppression -0.06)
FAMILIARITY: standard (no discount applied)
NOTE: H2H is a demand signal modifier — not outcome predictor
```

---

## Known Fixture H2H Profiles

Structural profiles only — not live records. Verify current H2H
record before each fixture application. Named players excluded
per Club Intelligence Gate.

**El Clásico variant — $BAR vs $ATM (La Liga)**
Fixture type: domestic league · Dual-token: YES ($BAR + $ATM) ·
H2H character: contested, high-profile, long rivalry history ·
Familiarity discount: YES ×0.50 · Notes: Real Madrid has no
active Chiliz token — $BAR vs Real Madrid is single-token.

**Derby della Madonnina — $INTER vs $ACM (Serie A / UCL)**
Fixture type: domestic + continental · Dual-token: YES ·
H2H character: intense city derby, frequent meetings ·
Familiarity discount: YES ×0.50 · Notes: shared San Siro
reduces home advantage distinction. CDI gate asymmetry in
2026-27: $INTER CONSOLIDATION vs $ACM TRANSITION.

**$PSG vs $BAR (UCL)**
Fixture type: continental · Dual-token: YES ·
H2H character: high-profile, recurring UCL encounters ·
Familiarity discount: YES ×0.50 if 3+ UCL meetings in 10 years ·
Notes: verify meeting count before applying discount.

**$AFC vs $CITY (Premier League / domestic cup)**
Fixture type: domestic · Dual-token: YES ·
H2H character: top-4 rivalry, high-stakes fixtures ·
Familiarity discount: YES ×0.50 · Notes: $AFC is the only
confirmed FTP PATH_2 token. PATH_2 supply events are independent
of H2H signal — never conflate.

**$JUV vs $INTER (Serie A / Coppa Italia)**
Fixture type: domestic · Dual-token: YES ·
H2H character: historic Italian rivalry, high meeting volume ·
Familiarity discount: YES ×0.50 · Notes: $JUV CDI gate is
TRANSITION (Europa League 2026-27). Apply CDI context before
H2H modifier. Gate asymmetry: $INTER CONSOLIDATION vs $JUV
TRANSITION.

---

## Open Questions and Monitoring Flags

```
H2H AUTO-POPULATION — FUTURE
  football-data.org free tier identified as fixture authoring
  assistance source. Framework is data-source agnostic —
  any verified competitive record source is acceptable.
  Do not create runtime API dependency. Revisit post-WC2026.

MMA H2H EXPANSION — EMERGING
  Individual fighter H2H profiles not yet systematic in
  library. Rematch demand signal documented structurally.
  Expand as MMA calibration records accumulate.

CONTRARIAN SPIKE CALIBRATION — MONITOR
  Pattern B (contrarian spike: +0.06) is an initial estimate.
  Calibrate against verified calibration records as they
  accumulate. Bring to Strategy & Brainstorm when sufficient
  records exist.

REAL MADRID FAN TOKEN — MONITOR
  Real Madrid has no active Chiliz fan token as of 2026-07-31.
  If confirmed: El Clásico ($BAR vs Real Madrid) profile
  needed urgently — would be highest-profile new dual-token
  La Liga fixture. Escalate immediately to Strategy &
  Brainstorm.

NEW DUAL-TOKEN FIXTURES — PROCESS
  Any new dual-token fixture pair requiring a known H2H profile:
  bring to Strategy & Brainstorm before adding to Section 8.
```

---

## Sources and Verification

```
PRIMARY SOURCES:
  SportMind calibration records — calibration/2026/ and
    community/calibration-data/football/
  CDI files — market/club-intelligence/
  mma-intelligence-framework.md — sports/mma/
  Core framework files — core/

EXTERNAL (verify before use — not runtime dependencies):
  football-data.org — fixture and result data
  UEFA.com — official continental competition records

CALIBRATION STATUS:
  This framework is currently uncalibrated. Decay weights,
  amplification values, and Pattern B thresholds are initial
  structural estimates. A calibration pass is planned
  post-WC2026 as competitive records accumulate.

LAST VERIFIED: 2026-07-31
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
core/signal-classification-framework.md ·
core/temporal-reasoning-framework.md ·
core/contradiction-resolution-framework.md ·
market/club-intelligence/ (all CDI files) ·
sports/football/sport-domain-football.md ·
sports/mma/mma-intelligence-framework.md ·
fan-token/registry/complete-registry.md ·
calibration/2026/ ·
community/calibration-data/football/

© 2026 SportMind
