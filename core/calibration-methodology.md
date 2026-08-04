# Calibration Methodology

**Domain:** core/calibration-methodology.md
**Version:** v4.1.84
**Library Rule:** Six-Month Test PASSES · Proper Noun Test PASSES
**Layer:** Core reasoning
**Last updated:** 2026-08-01
**Scope:** Documents the empirical foundation that justifies modifier
values in the SportMind library. Without calibration, modifiers are
structural estimates. With calibration, they are evidence-based.
Serves two audiences: agents reasoning about signal confidence, and
contributors creating new records. Calibration is a verification
system — not a prediction system. Records confirm or challenge what
the library already believes. They do not produce new signals
independently.

---

## Why Calibration Methodology Matters

SportMind's modifier values — decay weights, venue tiers, occasion
weights, CDI gate thresholds — are structural estimates until
calibration records provide evidence for or against them. Without
a methodology, those estimates drift in three ways:

- Modifier values are updated from a single record (too early)
- Verified and seed records are combined (inflated evidential weight)
- Accuracy claims are stated without record-base context (misleading)

A 96% direction accuracy claim means something specific: 121 of
126 seed records called the correct direction. It does not mean
96% across verified records. It does not mean 96% of all records.
It does not apply to modifiers that have zero calibration records.

This framework provides the methodology for creating valid records,
tracking modifier calibration status, updating modifiers at the
right threshold, and reporting accuracy honestly. It is used by
agents when assessing signal confidence and by contributors when
submitting new calibration records.

The two audiences must not be conflated. An agent reasoning about
compound signal confidence uses this file differently from a
contributor submitting a Libertadores record. Never produce output
that merges both uses in a single block.

---

## Two Record Tiers

All calibration records belong to one of two tiers. The distinction
determines evidential weight. Never combine the totals.

```
TIER 1 — PRE-MATCH VERIFIED RECORDS
  Definition: submitted before kickoff · result confirmed via primary
    source · direction assessed · passes all six validity gates ·
    independently verified.
  Current count: 13 pre-match verified records (as of 2026-08-01)
  Breakdown: 3 AFC April 2026 pre-match records · 9 WC2026
    series · 1 UCL Final 2026
  Weight: highest evidential weight. Modifier updates require
    pre-match verified records — seed records alone are insufficient.

TIER 2 — SEED RECORDS
  Definition: submitted by sportmind-core from historical known
    outcomes. Valid for framework validation and directional
    confidence but NOT genuine pre-match predictions.
  Current count: 117 seed records (as of 2026-08-01)
  Note: seed records were chosen from known outcomes — they
    confirm the framework works correctly but cannot validate
    modifier accuracy. Only pre-match verified records from
    external contributors can validate modifier accuracy.

CALIBRATION TOTAL — CORRECT FIGURES:
  Total records: 130 (13 pre-match verified + 117 seed)
  NEVER state: 126 (stale) · 139 (wrong) · 137 (wrong)
  NEVER combine pre-match verified + seed into one number
    without distinguishing the two tiers.
  Always state: "130 records · 13 pre-match verified · 117 seed"
  The distinction matters — seed records confirm framework
    correctness; pre-match verified records confirm modifier
    accuracy. These are different evidential claims.
  This is a library integrity rule with no exceptions.
```

---

## Validity Gates — What Makes a Record Valid

Six gates must all pass for a record to be valid. One failed gate
invalidates the record regardless of accuracy.

```
GATE 1 — PRE-KICKOFF SUBMISSION (TFM6 — MANDATORY)
  Record must be created and committed before the match begins.
  Post-kickoff records are invalid regardless of accuracy.
  TFM6 is the most critical validity gate — it ensures the record
  represents a genuine pre-match signal, not hindsight.
  Agent rule: timestamp of commit must precede kickoff time.
  Any doubt about timing = record is invalid.
  A post-kickoff record that is 100% correct is still invalid.
  It does not count toward any calibration total.

GATE 2 — ACTIVE FAN TOKEN REQUIREMENT
  At least one active Chiliz fan token must be present on either
  side of the fixture for a fan token calibration record.
  No active fan token on either side:
    Valid for sports intelligence layer only.
    Counts toward community/calibration-data/[sport]/ totals.
    Does NOT count toward 13 verified / 126 seed fan token totals.

GATE 3 — CONFIRMED RESULT FROM PRIMARY SOURCE
  Match result confirmed via official competition authority or
  primary source: UEFA.com · FIFA.com · official club results.
  Aggregator confirmation is cross-check only — not primary source.
  Result must include: final score · extra time / penalties
  (if applicable) · confirmed as competitive fixture.

GATE 4 — DIRECTION ASSESSED
  Direction must be one of: HOME · AWAY · DRAW.
  Assessed against the pre-match signal direction.
  CORRECT: signal direction matches result direction.
  INCORRECT: signal direction does not match result direction.
  DRAW: signal called DRAW · match ended as draw = CORRECT.
  WRONG DRAW: signal called HOME or AWAY · match ended draw = INCORRECT.
  All outcomes including incorrect ones are valid records.
  Incorrect records are as important as correct ones — they
  identify where modifiers need updating.

GATE 5 — CLUB INTELLIGENCE GATE COMPLIANCE
  Named player signings or individual athlete performance data
  must not be the primary basis for the signal.
  Valid inputs: coaching succession · squad archetype shift ·
    competition tier change · structural CDI signals.
  Per Club Intelligence Gate: named players are excluded from
  library files — calibration records must comply.

GATE 6 — COMPETITIVE FIXTURE
  Friendly matches, preseason fixtures, and exhibition games are
  not valid calibration records.
  Competitive only: league · cup · continental · international
  tournament · playoff.
```

---

## Direction Accuracy as Primary Metric

SportMind measures direction accuracy — not margin, score, or any
other outcome measure. Direction is the only actionable output at
the fan token demand signal level.

```
DIRECTION = HOME · AWAY · DRAW (three possible outcomes)

CORRECT: signal calls HOME · home side wins (any scoreline).
  1–0 and 5–0 are both CORRECT.
INCORRECT: signal calls HOME · away side wins or match draws.
DRAW CORRECT: signal calls DRAW · match ends as draw.
WRONG DRAW: signal calls HOME or AWAY · match ends as draw.
  Counts as INCORRECT.

WHY DIRECTION ONLY:
  Score prediction requires match simulation beyond SportMind scope.
  Direction is the actionable output — it determines fan token
  demand signal direction, not match simulation.
  Direction accuracy is also the most honest measure:
    Random guessing on a three-outcome system = 33% accuracy.
    SportMind seed record accuracy: 96% (121/126).
    WC2026 series accuracy: 100% (9/9).

ACCURACY REPORTING RULES:
  Verified records: state accuracy separately from seed records.
  Seed records: 96%+ direction accuracy (117 seed records).
  Pre-match verified: 13/13 correct within verified series
    (WC2026 9/9 · UCL Final 1/1 · AFC April 2026 3/3)
  WC2026 series: "9/9 · 100% — WC2026 verified series."
  Combined accuracy: do not calculate or state.
    Each tier reports its own accuracy independently.
  Never state "96% accuracy" without stating the record base.
  Website stat bar: does not show 96% accuracy as headline.
    Shows: "9/9 WC2026 · 100%" for the verified series.

ZERO INTERNALLY INCONSISTENT RECORDS:
  The 5 incorrect seed records are not internally inconsistent —
  they are cases where the signal logic was sound but the match
  result went against the signal. Internally inconsistent would
  mean the signal logic contradicted itself. No such records exist.
```

---

## Modifier Update Process

Calibration records inform modifier updates — they do not
automatically trigger them. All modifier updates go through
Strategy & Brainstorm before Build Chat executes.

```
UPDATE THRESHOLDS (minimum record counts before update):

SINGLE RECORD (1–2 records on a modifier):
  Status: DIRECTIONAL SIGNAL ONLY.
  No modifier update warranted.
  Note the directional signal in SMI briefing.
  Flag to Strategy & Brainstorm if a pattern develops.

UPDATE CANDIDATE (3–4 records on a modifier):
  Status: EMERGING PATTERN.
  Minimum threshold for discussing a modifier update.
  Bring to Strategy & Brainstorm for assessment.
  Do not update modifier without Strategy Chat approval.
  Both VERIFIED and SEED records count toward threshold —
  VERIFIED records carry greater evidential weight.

STRONG UPDATE SIGNAL (5–9 records on a modifier):
  Status: CALIBRATION UPDATE WARRANTED.
  Bring to Strategy & Brainstorm with full record evidence.
  State: which modifier · direction of all records ·
    proportion correct · proposed adjustment.
  Strategy Chat produces Build Chat task. Build Chat executes.

CONFIRMED UPDATE (10+ records on a modifier):
  Status: HIGH CONFIDENCE UPDATE.
  Modifier should be updated unless contradicted by other evidence.
  Strategy & Brainstorm reviews and approves before execution.
  After update: reset calibration tracking for that modifier.
  Note prior calibration history in the updated file.

MODIFIER CATEGORIES FOR TRACKING:
  H2H framework: decay weights · amplification values ·
    familiarity discount thresholds · Pattern B trigger values
  Venue framework: FORTRESS · STANDARD · WEAKENED tier values ·
    crowd composition modifier · prestige amplifier
  Compound signal framework: occasion weight table values ·
    SMS layer weightings · cancellation discount (50%)
  Sport-specific modifiers: qualifying_delta · dew_factor ·
    sport-specific decay curves
  CDI gate thresholds: gate classification boundary conditions
  Macro regime modifiers: CAPITULATION · ANXIETY · BULL values
```

---

## Calibration Series

A calibration series is a structured set of records covering a
specific competition or tournament window. Series results are
permanently archived and closed on completion.

```
SERIES RULES:
  All records in a series must be created before kickoff (Gate 1).
  Series records must share a common competition context.
  Series verdict recorded after final match result is confirmed.
  Completed series are permanently archived — never reopened.

CONFIRMED SERIES:

AFC APRIL 2026 PRE-MATCH SERIES:
  Records: 3 (all pre-match verified)
  Fixtures: WIN vs Sporting CP · LOSS vs Bournemouth ·
    DRAW vs Sporting CP
  Status: CLOSED · VERIFIED
  Note: First confirmed pre-match records in the library.
    These predate the WC2026 series.

WC2026 SERIES:
  Records: 9 (all pre-match verified)
  Result: 9/9 CORRECT · 100% direction accuracy
  Window: WC2026 group stage through final
  Status: CLOSED · PERMANENTLY ARCHIVED
  Location: calibration/2026/
  Key result: $SPAIN WORLD CHAMPION · 8 PTG burns documented
  Do not reopen or reinterpret — historical record only.

UCL FINAL 2026:
  Records: 1 (verified — $PSG vs $AFC)
  Location: calibration/2026/ucl-final-psg-vs-arsenal-2026-05-30.md
  Status: ARCHIVED

LIBERTADORES LAST 16 SERIES (UPCOMING):
  Window: August 11–20 2026
  Tokens: $MENGO · $VERDAO · $FLU · $SCCP
  Status: PENDING — records must be created before each kickoff
  Location: community/calibration-data/football/
  Note: NOT in calibration/2026/ — that folder is for WC2026
    series and UCL Final 2026 only. All other records go to
    community/calibration-data/football/

SERIES NAMING CONVENTION:
  [competition]-[round]-[home]-vs-[away]-[YYYY-MM-DD].md
  Example: wc2026-r16-spain-vs-portugal-2026-07-06.md
  Use competition shorthand · round abbreviation · lowercase.
```

---

## Founding Calibrators

```
PROGRAMME:
  Recognises the first 10 external contributors to the SportMind
  calibration series. Founders are permanently credited in the
  library's history via GitHub commit record.

CONFIRMED FOUNDING CALIBRATORS (as of 2026-08-01):
  Founding Calibrator #1: @AltcoinDaddy
  Founding Calibrator #2: @charan0318
  Slots remaining: 8 of 10

CONTRIBUTION REQUIREMENTS:
  Records must pass all six validity gates.
  Records must be submitted before kickoff (TFM6 — Gate 1).
  At least one active fan token required for fan token
    calibration credit.
  Records committed to community/calibration-data/ via GitHub
    Desktop — never included in a Build Chat zip.

ATTRIBUTION:
  Founding Calibrator records are attributed by GitHub commit
  history — not by personal name in library markdown files.
  No personal names appear in library markdown files.
  GitHub commit history is the permanent attribution record.
```

---

## FM Guardrails — Calibration Failure Modes

Five guardrails governing calibration record creation and use.

**FM-CAL-1 — Never create a record after kickoff.**
Post-kickoff records are invalid regardless of accuracy. TFM6 is
non-negotiable. If kickoff time is uncertain: submit before the
earliest possible kickoff time. A post-kickoff record that calls
the correct direction is still invalid — it does not count toward
any calibration total and must not be cited as evidence.

**FM-CAL-2 — Never state stale or incorrect record totals.**
Correct total: 130 records (13 pre-match verified + 117 seed).
NEVER state: 126 (stale seed-only count) · 139 (wrong) ·
137 (wrong) · any combined number without tier distinction.
Always state: "130 records · 13 pre-match verified · 117 seed"
Combining or misquoting totals misrepresents the evidential
base. This is the most frequently violated calibration rule.

**FM-CAL-3 — Never use non-fan-token records for fan token modifier updates.**
Records without an active fan token validate the sports intelligence
layer — not the fan token calibration layer. Do not cite non-fan-token
records when justifying fan token modifier updates. The evidential
basis is categorically different.

**FM-CAL-4 — Never update a modifier from a single record.**
One record is a directional signal — not calibration evidence.
Minimum 3 records before any modifier update discussion. A single
incorrect record does not invalidate a modifier. A pattern of
incorrect records across 5 or more fixtures does.

**FM-CAL-5 — Never claim accuracy figures without stating the record base.**
"96% accuracy" without context is misleading. Always state the
basis: "96% direction accuracy across 126 seed records" or
"9/9 · 100% across the WC2026 verified series." The website does
not use headline accuracy claims — it uses verifiable series
results instead.

---

## Agent Rules — Using Calibration in Reasoning

```
RULE 1 — CALIBRATION INFORMS CONFIDENCE TIER:
  When producing a compound signal, state how many calibration
  records support the modifiers being applied.
  0 records: UNCALIBRATED — initial structural estimate.
  1–2 records: LOW CALIBRATION CONFIDENCE.
  3–4 records: EMERGING CALIBRATION — use directionally.
  5–9 records: CALIBRATED — use with standard confidence.
  10+ records: HIGH CALIBRATION CONFIDENCE.

RULE 2 — DO NOT OVERRIDE CALIBRATED MODIFIERS WITHOUT EVIDENCE:
  If a modifier has 10+ calibration records, do not override it
  based on a single contradicting signal. Surface the contradiction
  — do not resolve by discarding the calibrated modifier. Load
  core/contradiction-resolution-framework.md if needed.

RULE 3 — CALIBRATION SERIES RESULTS ARE PERMANENTLY CLOSED:
  AFC April 2026 (3/3) · WC2026 9/9 · UCL Final (1/1)
  are all closed, verified pre-match series.
  Do not reopen or reinterpret series results.
  Series results are historical record — not live signals.
  They inform modifier confidence, not current fixture analysis.

RULE 4 — UPCOMING CALIBRATION WINDOWS ARE ACTIONABLE:
  When a calibration window is approaching (Libertadores August
  11–20), flag in SMI briefings.
  Records must be created before each kickoff — not after.
  Calibration windows are time-sensitive by definition (Gate 1).
  Pre-match record creation is the only valid contribution.

RULE 5 — CALIBRATION DOES NOT GUARANTEE FUTURE ACCURACY:
  96% seed record accuracy and 9/9 WC2026 are historical results.
  They do not guarantee future signal accuracy.
  Calibration builds confidence in modifiers — it does not make
  SportMind infallible. Always state confidence tier alongside
  any accuracy reference in an agent output.
```

---

## Record File Format

Reference structure for valid calibration record files. Not a
prescriptive template — apply the structure to the competition
context. All six validity gates must be met.

```
HEADER:
  Competition · fixture · date · library version at signal time
  Submitted by: SportMind or Founding Calibrator GitHub handle
  Status: VERIFIED or SEED

PRE-MATCH SIGNAL SECTION:
  Direction called: HOME · AWAY · DRAW
  Confidence tier: HIGH · MEDIUM · LOW
  Modifiers applied: list all active modifiers with values
  Macro regime at signal time: CAPITULATION / ANXIETY / BULL
  Fan token status: confirmed active tokens on each side
  PATH_2 status if applicable ($AFC only):
    ACTIVE — WIN burns · LOSS mints · DRAW = no event

RESULT SECTION:
  Actual result: score · extra time · penalties (if applicable)
  Direction correct: YES · NO · DRAW
  Supply event outcome if PATH_2 active:
    WIN: burn confirmed (chiliscan.com link required)
    LOSS: mint confirmed (chiliscan.com link required)
    DRAW: no supply event
  Chiliscan confirmation link: required for all supply events

CALIBRATION VERDICT:
  CORRECT · INCORRECT · DRAW
  Notes on what the record confirms or challenges in the library.
  State which modifier the record is most relevant to.

NAMING CONVENTION:
  [competition]-[round]-[home]-vs-[away]-[YYYY-MM-DD].md
  Example: wc2026-r16-spain-vs-portugal-2026-07-06.md
  Lowercase throughout. Round abbreviation: r16 · sf · f · gs.

FOLDER RULES:
  calibration/2026/ — WC2026 series + UCL Final 2026 ONLY
  community/calibration-data/football/ — all other football records
  community/calibration-data/[sport]/ — other sport records
  Never place club competition records in calibration/2026/
```

---

## Open Questions and Monitoring Flags

```
H2H FRAMEWORK CALIBRATION — PENDING:
  H2H decay weights · amplification values · familiarity discount
  thresholds · Pattern B trigger values are uncalibrated initial
  estimates. Libertadores series (August 11–20) will begin
  accumulating H2H-relevant records. Calibration pass planned
  post-series as records reach update candidate threshold.

VENUE FRAMEWORK CALIBRATION — PENDING:
  FORTRESS · STANDARD · WEAKENED tier values · crowd composition
  modifier · prestige amplifier values are uncalibrated initial
  estimates. Calibration pass planned as venue-specific fixture
  records accumulate post-WC2026.

COMPOUND SIGNAL FRAMEWORK CALIBRATION — PENDING:
  SMS layer weightings and occasion weight table values are initial
  estimates. Calibration pass planned as compound signal records
  accumulate. Quantitative stacking arithmetic deferred until
  sufficient records exist — do not implement without Strategy &
  Brainstorm review.

COMMUNITY CALIBRATION EXPANSION — MONITOR:
  8 Founding Calibrator slots remain open as of 2026-08-01.
  Community records in community/calibration-data/ are growing
  independently of the main verified series. Monitor for emerging
  patterns that reach UPDATE CANDIDATE threshold (3–4 records
  on a single modifier).
```

---

## Sources and Verification

```
PRIMARY SOURCES:
  calibration/2026/ — WC2026 series + UCL Final 2026 (verified)
  community/calibration-data/ — 126 seed records
  core/temporal-reasoning-framework.md — TFM6 reference
  core/compound-signal-framework.md — SMS and modifier usage
  core/signal-classification-framework.md
  core/contradiction-resolution-framework.md

CALIBRATION STATUS:
  This file documents the calibration methodology — it is not
  itself subject to calibration. The methodology is structural.
  The records it governs are empirical. Do not conflate.

LAST VERIFIED: 2026-08-02
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
core/temporal-reasoning-framework.md (TFM6 reference) ·
core/compound-signal-framework.md (modifier confidence) ·
core/contradiction-resolution-framework.md ·
core/signal-classification-framework.md ·
core/h2h-framework.md (uncalibrated modifiers noted) ·
core/venue-intelligence-framework.md (uncalibrated modifiers noted) ·
calibration/2026/ (WC2026 series + UCL Final 2026) ·
community/calibration-data/ (seed records) ·
market/club-intelligence/ (CDI gate calibration) ·
fan-token/registry/complete-registry.md

© 2026 SportMind
