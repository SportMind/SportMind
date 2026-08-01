# Venue Intelligence Framework

**Domain:** core/venue-intelligence-framework.md
**Version:** v4.1.82
**Library Rule:** Six-Month Test PASSES · Proper Noun Test PASSES
**Layer:** Core reasoning
**Last updated:** 2026-08-01
**Scope:** Structured framework for applying venue context as a demand
signal modifier. Venue is a structural modifier — not a data feed.
Three structured outputs per fixture: venue type classification
(HOME/AWAY/NEUTRAL/SHARED/TEMPORARY), home advantage modifier
(FORTRESS/STANDARD/WEAKENED/ZERO), and neutral venue flag (YES/NO).
Additive to H2H, CDI, form, and macro signals — never replaces.
Loading order: macro → CDI → form → H2H → venue → regulatory →
output. Venue loads after H2H — historical context before physical
context. Prevents double-counting of venue-based H2H patterns.

---

## Why Venue Intelligence Matters

Venue context is applied in almost every pre-match analysis. It is
also routinely misapplied. Without structure, venue application
produces:

- FORTRESS classification without confirmation (inflated modifier)
- Home advantage applied to neutral venues (incorrect framework)
- Full home advantage applied to shared stadiums (×0.5 missing)
- Sold-out assumed when attendance is unknown (capacity error)
- Temporary displacement ignored when a club has moved grounds

A displaced club playing a "home" fixture in an unfamiliar stadium
is not receiving full home advantage. A UCL Final at a neutral
venue gives neither side home advantage regardless of crowd size.
A shared stadium fixture reduces the territorial edge for the
designated home club.

This framework eliminates those failure modes through a structured
five-type classification, three-tier home advantage model, and
explicit output format.

Venue intelligence is additive. It does not replace CDI gate
classification, macro regime checks, H2H signals, or regulatory
overlays. Load it after H2H, before regulatory output.

---

## Venue Type Classification — Five Types

Classify venue type before applying any modifier. State venue type
explicitly in every signal output. Source classification from the
official competition fixture list — never infer from match location
alone.

### Type 1 — HOME

Club's primary registered ground. Full home advantage tier modifier
applies (FORTRESS / STANDARD / WEAKENED as determined in Section 3).

```
PASS CONDITIONS:
  · Club listed as home side in official fixture
  · Fixture at club's primary registered ground
  · No confirmed displacement in effect
MODIFIER: Apply home advantage tier (Section 3)
```

### Type 2 — AWAY

Opponent's primary registered ground. The away side receives no
home advantage modifier. Standard away context applies.

```
PASS CONDITIONS:
  · Club listed as away side in official fixture
MODIFIER: None — standard away context
```

### Type 3 — NEUTRAL

UCL Finals, World Cup matches, playoff legs at a third venue, and
cup finals at a designated neutral ground. Home advantage is ZERO
for both sides. Crowd composition becomes the primary venue signal.

```
PASS CONDITIONS:
  · Competition authority designates fixture as neutral
  · Neither club's primary ground is the venue
  · Confirmed via official competition authority source
HOME ADVANTAGE: ZERO for both sides
MODIFIER: Crowd composition modifier (Section 4)
CONFIRMATION REQUIRED: Official source only — never assume neutral
```

### Type 4 — SHARED

Two clubs share the same stadium as their primary registered
ground. Home advantage modifier is reduced to ×0.5 for the
designated home club. Neither club holds full territorial advantage.

```
PASS CONDITIONS:
  · Both clubs list the same stadium as primary ground
  · One club is officially designated home for the fixture
HOME ADVANTAGE: ×0.5 applied to standard tier modifier
FAMILIARITY DISCOUNT: Same ground, same surface, same dressing
  rooms — psychological territorial edge reduced
CONFIRMED SHARED STADIUMS (as of 2026-08-01):
  San Siro (Milan, Italy): $INTER (Inter Milan) and $ACM (AC Milan)
Agent rule: verify which club is officially designated home before
  applying shared rules. Do not apply shared rules to cup finals
  at shared stadiums — if designated neutral, apply Type 3 rules.
```

### Type 5 — TEMPORARY

Club is confirmed playing home fixtures at a venue other than
their primary registered ground. Home advantage is WEAKENED
regardless of historical fortress status.

```
CAUSES (examples — not exhaustive):
  · Stadium renovation or construction
  · UEFA or domestic competition venue ban
  · Financial enforcement affecting stadium access
  · Force majeure (natural disaster, safety closure)
HOME ADVANTAGE: WEAKENED tier (+0.02) — mandatory
CONFIRMATION REQUIRED: Official club statement or competition
  authority announcement. Never infer from match location alone.
DURATION: Apply for confirmed displacement period only.
  When club returns to primary ground: revert to standard
  tier classification.
```

---

## Home Advantage Modifier — Three Tiers

Apply after venue type is confirmed. State tier and capacity
modifier explicitly in every signal output. Default is always
STANDARD until evidence confirms otherwise.

### FORTRESS Tier

```
DEFINITION:
  Club with documented disproportionate home record.
  Significantly above-average home win rate over 3+ seasons.
  Confirmed crowd intensity signal (Tier 1 source required).

MODIFIER: +0.12 applied to home token demand signal

CONFIDENCE: LOW until calibrated against live records.
  Do not apply FORTRESS without confirmation.
  Preliminary classification requires Tier 1 source
  verification before use.

STRUCTURAL FORTRESS CHARACTERISTICS (not live data — verify):
  · High crowd density relative to capacity
  · Enclosed stadium design amplifying noise
  · Historically strong home record in competition tier
```

### STANDARD Tier (default)

```
DEFINITION:
  Typical home advantage. No documented fortress or
  weakness characteristics. Applied when no specific
  fortress or weakened evidence is available.

MODIFIER: +0.06 applied to home token demand signal

DEFAULT: Apply STANDARD when no evidence supports FORTRESS
  or WEAKENED. Never escalate to FORTRESS without confirmation.
```

### WEAKENED Tier

```
DEFINITION:
  Below-average home record, stadium disputes, confirmed
  crowd atmosphere issues, or temporary displacement.

MODIFIER: +0.02 applied to home token demand signal

APPLY WHEN:
  · Confirmed weakened home environment (Tier 1 source)
  · Temporary displacement confirmed (Type 5 venue)
  · Stadium dispute or crowd atmosphere issue confirmed
NEVER INFER: Must be confirmed via Tier 1 source.
```

### ZERO (neutral venues only)

```
HOME ADVANTAGE: Does not apply.
APPLY: Crowd composition modifier instead (Section 4).
CONTEXT: Type 3 NEUTRAL venues only.
```

### Crowd Capacity Modifier

```
Sold out (95%+ capacity):        Full tier modifier applies
High attendance (70–94%):        Full tier modifier applies
Moderate attendance (50–69%):    ×0.70 reduction to modifier
Low attendance (below 50%):      ×0.40 reduction to modifier

VERIFICATION REQUIRED: Never assume sold out.
  Source: official club or competition authority attendance.
  If attendance unknown: apply STANDARD tier at ×0.70.
```

---

## Neutral Venue Rules

Home advantage is ZERO for both sides at neutral venues.
Confirm neutral status via official competition authority before
applying zero home advantage. Never assume neutral — always verify.

### Crowd Composition Modifier

```
At neutral venues, crowd composition is the primary venue signal
for dual-token fixtures.

GEOGRAPHICALLY CLOSER FAN BASE:
  +0.04 demand modifier to that side's token (proximity advantage)
  Apply when: Tier 1 source confirms crowd composition imbalance

NO CLEAR TRAVEL ADVANTAGE:
  No crowd modifier applied

SIGNAL STRENGTH: WEAK — apply only when imbalance is confirmed.
```

### UCL Final Specific Rule

```
Context: Highest-prestige neutral venue in European football.
Home advantage: ZERO
Prestige amplifier: +0.05 to BOTH tokens in confirmed dual-token
  UCL Final fixtures. This is additive — both tokens receive +0.05.
Single-token UCL Final: prestige amplifier applies to active
  token only.
Source: verify venue designation from UEFA.com each season.
```

### World Cup Final and Semi-Finals

```
Same neutral venue rules apply.
Prestige amplifier: +0.05 to active fan tokens.
Apply only when fan tokens confirmed active for both competing
  nations at fixture date.
```

---

## Shared Stadium Rules

```
DEFINITION:
  Two clubs with active fan tokens share the same stadium as
  their registered home ground.

CONFIRMED SHARED STADIUMS (as of 2026-08-01):
  San Siro (Milan, Italy):
    $INTER (Inter Milan) and $ACM (AC Milan)
    Derby della Madonnina context:
    See core/h2h-framework.md for dual-token amplification rules.
    Note: future stadium plans for both clubs may change this —
    verify shared status before each season.

MODIFIER RULES:
  Home advantage modifier: ×0.5 for officially designated home club
  Away side: no modifier (standard away context)

FAMILIARITY DISCOUNT:
  Same pitch surface · same dressing rooms · same tunnel ·
  same pre-match environment for both clubs.
  Psychological territorial edge reduced.
  The ×0.5 modifier encodes this discount.

AGENT RULE:
  Verify which club is officially designated home before applying.
  Do not apply shared rules to cup finals at shared stadiums —
  if designated neutral, apply neutral venue rules instead.
```

---

## Temporary Displacement Rules

```
DEFINITION:
  Club is confirmed playing home fixtures at a venue other than
  their registered primary ground.

CAUSES (examples — not exhaustive):
  Stadium renovation or construction.
  UEFA or domestic competition venue ban.
  Financial enforcement affecting stadium access.
  Force majeure (natural disaster, safety closure).

MODIFIER RULES:
  Apply WEAKENED tier (+0.02) regardless of whether the club's
  primary ground would otherwise qualify as FORTRESS.
  Displacement degrades home advantage structurally:
    · Unfamiliar surface
    · Different crowd acoustics
    · Changed travel and preparation patterns

CONFIRMATION REQUIRED:
  Official club statement or competition authority announcement.
  Never apply based on rumour or aggregator reports.
  Never infer from match location alone.

DURATION:
  Apply for confirmed displacement period only.
  When club returns to primary ground: revert to standard
  tier classification immediately.
```

---

## MMA Venue Application

```
NO HOME GROUND IN MMA:
  Fighters have no registered home venue.
  Home/away/shared/temporary rules do not apply.
  All MMA venues treated as NEUTRAL for both fighters.

ARENA SIZE AS ATMOSPHERE MODIFIER:

  SMALL ARENA (under 15,000 capacity):
    Intimate atmosphere · high crowd density relative to space ·
    crowd noise amplified.
    Apply: INTIMATE ATMOSPHERE +0.04 to promoted/favoured
    fighter's token demand signal.
    Promoted fighter: fighter with stronger local/regional
    following at the specific venue city.
    Never assumed — must be confirmed via Tier 1 source.

  STANDARD ARENA (15,000–35,000):
    Typical UFC/MMA venue. No atmosphere modifier applied.

  LARGE STADIUM (over 35,000):
    Diluted atmosphere · crowd spread across larger space ·
    crowd energy reduced relative to fight intensity.
    Apply: DILUTED ATMOSPHERE -0.02 to both tokens.

VERIFICATION REQUIRED:
  Always verify venue capacity before applying MMA atmosphere
  modifier. Default: standard arena, no atmosphere modifier.
```

---

## FM Guardrails — What Venue Intelligence Is Not

Five guardrails governing venue application.

**FM-V-1 — Venue is not an outcome predictor.**
Never imply that venue advantage equals match result. Venue is a
demand signal modifier — not a prediction. Never say "they always
win here" as a venue claim — state the tier and modifier value.

**FM-V-2 — Never apply home advantage to neutral venues.**
Confirm neutral status before zeroing home advantage. If venue
status is uncertain — apply STANDARD tier and flag uncertainty
explicitly. Do not assume neutral from fixture location alone.

**FM-V-3 — Crowd capacity must be verified — never assumed.**
Never assume sold out. Always apply capacity modifier based on
confirmed attendance or verified sellout status. If attendance
is unknown: apply STANDARD tier at ×0.70 and state the reason.

**FM-V-4 — Shared stadium modifier is mandatory.**
Never treat a shared stadium fixture as full home advantage for
the designated home club. The ×0.5 modifier is mandatory when a
confirmed shared stadium is identified. Omitting it is a framework
violation.

**FM-V-5 — Temporary displacement must be confirmed.**
Never infer displacement from match location alone. Always verify
via official club or competition source before applying WEAKENED
tier. Incorrect displacement classification inflates or deflates
the venue modifier without basis.

---

## Agent Workflow — Four Steps

```
STEP 1 — CLASSIFY VENUE TYPE
  Determine: HOME / AWAY / NEUTRAL / SHARED / TEMPORARY
  Source: official competition fixture list
  State venue type explicitly in every output.
  If venue type is uncertain: flag uncertainty and default
  to STANDARD tier until confirmed.

STEP 2 — APPLY HOME ADVANTAGE MODIFIER
  Select tier: FORTRESS / STANDARD / WEAKENED / ZERO
  Apply capacity modifier if attendance data available.
  For NEUTRAL: apply crowd composition modifier if confirmed
    imbalance exists. Apply prestige amplifier if UCL Final
    or World Cup Final/Semi-Final.
  For SHARED: apply ×0.5 to STANDARD tier modifier.
  For TEMPORARY: apply WEAKENED tier.
  State tier and capacity modifier explicitly.

STEP 3 — CHECK DUAL-TOKEN STATUS
  If both clubs have active Chiliz fan tokens:
    Apply venue modifier to home token demand signal.
    Away token: no venue modifier (standard away context).
    Exception: neutral venue crowd composition modifier
    and prestige amplifier apply to both tokens where relevant.
  If single-token fixture:
    Apply venue modifier to active token only.

STEP 4 — INTEGRATE WITH OTHER SIGNALS
  Venue modifier is additive to CDI, form, H2H, and macro.
  It does not replace or override other signal layers.
  Loading order: macro → CDI → form → H2H → venue →
  regulatory → output.
  Apply core/contradiction-resolution-framework.md if venue
  modifier conflicts with a higher-layer signal.
```

### Example Output Format

```
VENUE TYPE: HOME (San Siro — shared stadium)
VENUE TIER: STANDARD × 0.5 (shared modifier applied)
CAPACITY: sold out — full modifier
VENUE MODIFIER: +0.03 applied to home token demand signal
NOTE: Venue is a demand signal modifier — not an outcome predictor
```

---

## Known Venue Contexts

Structural notes only — not live data. Verify current status
before applying to any fixture. Named players excluded per
Club Intelligence Gate.

```
SAN SIRO (Milan, Italy)
  Clubs: $INTER (Inter Milan) · $ACM (AC Milan)
  Type: SHARED — both clubs are registered home clubs
  Modifier rule: STANDARD × 0.5 for designated home club
  Derby della Madonnina: see core/h2h-framework.md for
    dual-token amplification rules
  Note: future stadium plans for both clubs may change this —
    verify shared status before each season begins

NEF STADYUMU (Istanbul, Turkey)
  Club: $GAL (Galatasaray)
  Type: HOME — primary registered ground
  Structural characteristics: enclosed · high crowd density ·
    historically strong home record in Süper Lig and UCL
  Preliminary classification: FORTRESS candidate
  Confirmation required: verify via current season home record
    before applying FORTRESS tier. Default STANDARD until confirmed.

WEMBLEY STADIUM (London, UK)
  Primary use for SportMind: FA Cup Final · EFL Cup Final ·
    England national team home fixtures
  Type: NEUTRAL for domestic cup finals · HOME for England fixtures
  $SFA note: Scotland vs England at Wembley = AWAY fixture for $SFA
  $AFC note: Arsenal play at Emirates Stadium — Wembley is relevant
    for $AFC only in domestic cup final context

UCL FINAL VENUES (rotating by season)
  Type: NEUTRAL — highest prestige
  Prestige amplifier: +0.05 to both tokens in confirmed
    dual-token UCL Final
  Source: verify venue designation from UEFA.com each season
    before applying

UFC APEX (Las Vegas, USA)
  Type: NEUTRAL (all MMA venues are neutral)
  Capacity: approximately 1,800 — SMALL ARENA category
  Atmosphere modifier: INTIMATE ATMOSPHERE +0.04 to promoted fighter
  Special note: UFC Apex is a closed production facility —
    crowd is invitation and media heavy, not general public.
    INTIMATE ATMOSPHERE modifier status UNRESOLVED.
    Verify before applying. See Section 11: Open Questions.
```

---

## Open Questions and Monitoring Flags

```
AWAY FAN ALLOCATION AS MODIFIER — FUTURE CAPABILITY
  Away fan section size affects atmosphere balance.
  Data sourcing not yet systematic.
  Framework is data-source agnostic — apply when data available.

REAL-TIME CAPACITY DATA — FUTURE CAPABILITY
  Confirmed attendance figures typically available post-match only.
  Pre-match sellout confirmation is the primary available signal.
  Pre-match: apply STANDARD at ×0.70 unless sellout confirmed.

FORTRESS CLASSIFICATION CALIBRATION — MONITOR
  FORTRESS tier thresholds are initial estimates.
  Calibrate against verified calibration records as venue-specific
  fixtures accumulate. Bring to Strategy & Brainstorm before
  confirming any new FORTRESS classification from preliminary status.

NEW SHARED STADIUM SITUATIONS — ESCALATE
  If any Chiliz partner club moves to a new stadium or enters a
  ground-sharing arrangement: escalate to Strategy & Brainstorm
  before updating Section 10. Do not update without review.

UFC APEX ATMOSPHERE MODIFIER — UNRESOLVED
  UFC Apex has unusual crowd composition (media and industry heavy).
  INTIMATE ATMOSPHERE modifier may not apply in the same way as
  public-attended arenas. Flag for review when MMA calibration
  records accumulate. Default: do not apply until resolved.
```

---

## Sources and Verification

```
PRIMARY SOURCES:
  Official competition fixture lists (UEFA.com · domestic FA sites)
  Official club websites — registered ground confirmation
  SportMind calibration records — calibration/2026/ and
    community/calibration-data/football/
  CDI files — market/club-intelligence/
  core/h2h-framework.md — dual-token amplification context

EXTERNAL (verify before use — not runtime dependencies):
  UEFA.com — UCL Final venue designation
  Official club announcements — displacement confirmation
  Ground capacity databases — capacity verification

CALIBRATION STATUS:
  Framework principles are uncalibrated. Tier modifier values
  (FORTRESS +0.12 · STANDARD +0.06 · WEAKENED +0.02) are initial
  structural estimates. FORTRESS classification thresholds require
  calibration as venue-specific fixture records accumulate.
  Calibration pass planned post-WC2026.

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
