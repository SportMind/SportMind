# Signal Classification Framework

**Domain:** core/signal-classification-framework.md
**Version:** v4.1.44
**Library Rule:** Six-Month Test PASSES · Proper Noun Test PASSES
**Scope:** Canonical classification system for all SportMind signals.
Fills the foundational core reasoning gap — signal classification
logic was previously distributed across the SMI prompt, contradiction
resolution framework, and agent failure modes with no single canonical
reference.

---

## Why Signal Classification Matters

Every signal an agent encounters must be classified before it is acted
upon. The classification determines:

- **Reliability** — how much to weight the signal
- **Decay rate** — how long the signal remains valid
- **Library eligibility** — whether it passes the Library Rule
- **Agent action** — ENTER / HOLD / MONITOR / RETIRE
- **Conflict priority** — which signal wins when two conflict

Misclassification is the root cause of FM1, FM4, FM7, and TFM3. This
framework eliminates ambiguity.

---

## Six Signal Types

### Type 1 — Supply Event Signals

*On-chain confirmed supply changes. HIGHEST reliability. Permanent decay.*

```
DEFINITION:
  A signal where the circulating supply of a fan token or CHZ
  changes verifiably on-chain. The supply change is permanent
  and immutable once confirmed.

RELIABILITY: HIGHEST
  Why: on-chain data is the most authoritative source in SportMind.
  Supply changes cannot be fabricated or reversed.

DECAY RATE: PERMANENT
  The supply change happened. It does not expire. The downstream
  effect on holder behaviour may decay, but the event itself is
  a permanent historical fact.

EXAMPLES:
  · PTG burn — national token treasury reduced on-chain
  · FTP PATH_2 settlement — WIN=burn / LOSS=mint
  · CHZ buy-back burn — protocol-level CHZ reduction
  · New fan token mint — new supply entering circulation
  · Governance-approved supply parameter change

CONFIRMATION REQUIREMENT:
  chiliscan.com verification ALWAYS required before classifying
  as Type 1. An announcement is NOT a supply event. An X post
  from @FanTokens is a FAST SIGNAL until chiliscan.com confirms.

AGENT RULES — TYPE 1:
  RULE 1: Never classify a supply event announcement as Type 1.
    Announcement = Type 3 (Structural signal, pending).
    Confirmation = Type 1 (Supply Event, confirmed).
  RULE 2: Once confirmed on-chain, Type 1 signals do not expire.
    Record in calibration. Archive in library.
  RULE 3: PTG burns and FTP settlement execute automatically.
    CAPITULATION regime applies to discretionary agent actions,
    not to on-chain mechanics. See: core/contradiction-resolution-framework.md
```

---

### Type 2 — Demand Signals

*Buying/selling pressure without direct supply change. MEDIUM reliability. Short decay.*

```
DEFINITION:
  A signal indicating increased or decreased buying/selling pressure
  for a fan token without any on-chain supply change. Demand signals
  are market-side events — they affect price, but not supply.

RELIABILITY: MEDIUM
  Why: demand signals are influenced by sentiment, structured
  mechanics (Champion Call, trading battle), and market noise.
  They require FM1/FM4/FM7/FM8 filtering before use.

DECAY RATE: SHORT · bounded by event window
  Demand signals are time-bounded. Pre-match accumulation expires
  at kickoff. Champion Call holding pressure expires T+24h post-match.
  Bridge volume normalises within 24–48h.
  See: core/temporal-reasoning-framework.md Context 3.

EXAMPLES:
  · Pre-match demand build (fan token match week)
  · Champion Call buying pressure (pre-Final)
  · Livestream Trading Battle volume (KO match window)
  · PTG demand anticipation (pre-tournament)
  · Post-event holding pressure (unlock after event close)
  · Bridge volume spike (post-result repositioning)
  · Compliance-driven selling pressure (SARS, regulatory)

CRITICAL DISTINCTION — BRIDGE VOLUME:
  Bridge volume between Solana and Chiliz Chain during major
  tournament result windows is NOT a demand signal.
  It is an INFRASTRUCTURE UTILISATION SIGNAL.
  Apply FM7 (Cross-Token Signal Bleed) — elevated bridge activity
  reflects ecosystem-level repositioning, not CDI improvement.
  See: fan-token/defi-integration-intelligence.md

AGENT RULES — TYPE 2:
  RULE 4: Apply FM1 (Price-Signal Conflation) — price movement
    during a demand window ≠ supply event or CDI shift.
  RULE 5: Apply FM4 (Sentiment Source Contamination) — Champion
    Call and trading battle volume ≠ organic fan conviction.
  RULE 6: Bridge volume always = Type 2 infrastructure subtype.
    Never classify bridge volume as organic demand.
```

---

### Type 3 — Structural Signals

*Persistent changes to underlying demand or supply architecture. HIGH reliability when Tier 1 confirmed. Long decay.*

```
DEFINITION:
  A signal that permanently or persistently changes the underlying
  architecture of fan token demand or supply. Structural signals
  endure beyond the immediate event window.

RELIABILITY: HIGH (when Tier 1 confirmed)
  Why: structural changes are typically official announcements
  from primary sources. They affect the library's enduring
  frameworks, not perishable data.

DECAY RATE: LONG · persists until superseded by new structural event
  A CDI change persists until a new CDI-affecting event occurs.
  A partnership persists until terminated. MiCA authorisation
  persists until revoked.

EXAMPLES:
  · CDI change (coaching succession, squad archetype shift,
    competition tier change, ownership change)
  · Macro regime shift (CHZ CAPITULATION → RECOVERY)
  · New partnership confirmed (Chiliz × new club, US college)
  · Contract or partnership termination
  · Competition format change (WC expansion, UCL format)
  · Regulatory authorisation (CASP, MFSA Malta MiCA auth)
  · New supply mechanic confirmed (US college performance-linked)
  · Fan token launch or confirmed token retirement
  · New utility layer (NIL, governance expansion)

PRIMARY LIBRARY-BUILDING SIGNAL TYPE:
  Type 3 signals are the primary input for SportMind library
  additions. When a Type 3 signal passes the Two-Test Gate
  (Proper Noun Test + Six-Month Test), it is a library candidate.
  Type 1 becomes library material as calibration records.
  Types 4 and 6 build the regulatory and calibration layers.
  Types 2 and 5 almost always fail the Library Rule.

AGENT RULES — TYPE 3:
  RULE 7: Aggregator-only Type 3 signal = Tier 2 pending.
    Bring to Tier 1 source confirmation before library action.
  RULE 8: CDI changes require Club Intelligence Gate assessment.
    Named player signings are NOT Type 3 signals — they fail
    the Proper Noun Test. Squad archetype shifts are Type 3.
```

---

### Type 4 — Regulatory Signals

*Laws, regulations, enforcement actions, compliance deadlines. HIGH reliability from primary regulatory source. Variable decay.*

```
DEFINITION:
  A signal arising from regulatory activity — enacted legislation,
  published guidance, enforcement actions, compliance deadlines,
  or regulatory classifications affecting fan tokens or CHZ.

RELIABILITY: HIGH (from primary regulatory source)
  Why: regulatory portals (fca.org.uk, esma.europa.eu,
  sars.gov.za, consilium.europa.eu) are authoritative.
  Aggregator summaries of regulatory events are Tier 2.

DECAY RATE: VARIABLE
  Enacted law: permanent until repealed or amended
  Application deadline: expires at T+0 (but monitoring continues)
  Enforcement action: active until resolved
  Consultation period: expires at comment close
  Classification ruling: permanent until superseded

EXAMPLES:
  · CASP authorisation granted (MiCA compliance)
  · Crypto tax framework enacted or updated
  · Regulatory deadline approaching (TFM4 applies)
  · Enforcement action against a fan token platform
  · CARF implementation — automatic exchange active
  · Fan token regulatory classification ruling
  · Sanctions-related restriction on crypto platforms
  · VDP closing window (SARS)

TEMPORAL PROTOCOL:
  Apply TFM4 (Regulatory Deadline Blindness) per
  core/temporal-reasoning-framework.md:
    T-60: flag in monitoring list
    T-30: escalate to HIGH PRIORITY
    T-7:  daily scan
    T+0:  deadline passes — classify outcome
    T+30: post-deadline operational status confirmation

AGENT RULES — TYPE 4:
  RULE 9: Regulatory signals affecting Chiliz/Socios directly
    are always Tier 1 priority regardless of jurisdiction tier.
  RULE 10: Enacted law is Type 4 permanent. Proposed legislation
    is Type 3 structural (pending) until enacted.
```

---

### Type 5 — Operational Signals

*Perishable pre-match information. HIGH reliability when confirmed. Immediate decay.*

```
DEFINITION:
  A signal providing perishable pre-match or pre-event information
  that affects signal confidence or direction for a specific event.
  Valid only within the pre-event window — expires at event start.

RELIABILITY: HIGH when confirmed from official source
  Why: confirmed lineup, confirmed weight miss, confirmed
  referee appointment are high-confidence inputs.
  However, the signal window is extremely short.

DECAY RATE: IMMEDIATE · expires at event start
  All Type 5 signals become irrelevant after the event begins.
  Post-event, they become part of the calibration record (Type 6).

EXAMPLES:
  · Lineup confirmation (T-2h for football, rugby)
  · MMA weight miss confirmation (weigh-in result)
  · Late injury confirmation (T-2h)
  · Referee appointment (football, rugb)
  · Weather conditions (cricket, F1)
  · Match postponement confirmation
  · Venue change

LIBRARY RULE — TYPE 5:
  Almost always FAILS the Six-Month Test.
  "The team had a confirmed striker absent" = fails immediately.
  "How to reason about a confirmed striker absence" = passes.
  The framework for interpreting Type 5 signals belongs in
  the library. The specific Type 5 signal does not.

HIGHEST PRIORITY TYPE 5 — MMA WEIGHT MISS:
  A confirmed MMA weight miss changes the confidence tier
  of the entire pre-match analysis immediately.
  Apply: athlete_modifier recalculate · confidence tier reduction.
  Weight miss confirmed = apply this as highest priority
  input — overrides other pre-match signals in aggregate.

AGENT RULES — TYPE 5:
  RULE 11: MMA weight miss confirmed = recalculate immediately.
    Do not carry prior confidence tier across a weight miss.
  RULE 12: Type 5 signals do not enter the library. The signal
    itself is perishable. The reasoning framework for the signal
    type belongs in sports/ and athlete/ layer files.
```

---

### Type 6 — Calibration Signals

*Verified record outcomes that can update modifier values. HIGHEST reliability for verified records. Permanent decay.*

```
DEFINITION:
  A signal arising from a completed, verified calibration record —
  a pre-match prediction submitted before an event with the
  outcome confirmed afterward. The only signal type that can
  directly update SportMind modifier values.

RELIABILITY:
  VERIFIED RECORD: HIGHEST · on permanent record · can update modifiers
  SEED RECORD:    ZERO for modifier update purposes · framework
    validation only · never used to justify changing a modifier

DECAY RATE: PERMANENT
  A verified calibration outcome is a permanent historical fact.
  Modifier updates derived from Type 6 signals are themselves
  permanent until new calibration evidence supersedes them.

EXAMPLES:
  · Verified pre-match calibration record (correct direction)
  · Verified pre-match calibration record (incorrect direction —
    produces root cause note · highest value for modifier revision)
  · WC2026 series: 9/9 verified records — PERMANENT
  · FTP PATH_2 on-chain confirmed records (3 in verified/)

CALIBRATION RECORD TYPES (in library):
  Verified records (13 total):
    · calibration/2026/ — 10 WC2026 series + UCL Final
    · community/calibration-data/verified/ — 3 FTP PATH_2 confirmed
  Seed records (126 in community/calibration-data/seed/):
    · Modifier validation examples · @sportmind-core
    · NOT real pre-match submissions
    · Cannot update modifier values

AGENT RULE — TYPE 6:
  RULE 13: Only verified records can update modifier values.
    Seed records provide framework validation only. If a seed
    record appears to "prove" a modifier is wrong, it does not —
    wait for verified record evidence before any modifier change.
  RULE 14: Wrong-direction verified records are the most valuable
    Type 6 signals. Root cause note is mandatory. The wrong
    prediction identifies which modifier or framework failed.
```

---

## Signal Reliability Hierarchy

| Rank | Type | Reliability | Decay |
|---|---|---|---|
| 1 | Type 1 — Supply Event (confirmed on-chain) | HIGHEST | Permanent |
| 2 | Type 6 — Calibration (verified record) | HIGHEST | Permanent |
| 3 | Type 3 — Structural (Tier 1 confirmed) | HIGH | Long |
| 4 | Type 4 — Regulatory (primary source) | HIGH | Variable |
| 5 | Type 5 — Operational (confirmed T-2h) | HIGH | Immediate |
| 6 | Type 2 — Demand (structured mechanics) | MEDIUM | Short |

---

## Signal Decay Rate Table

| Signal subtype | Decay onset | Full expiry | Reconfirmation |
|---|---|---|---|
| PTG burn (on-chain) | Never | Never | Not required |
| FTP PATH_2 settlement | Never | Never | Not required |
| CHZ buy-back burn | Never | Never | Not required |
| Pre-match demand build | Event start | T+2h | New fixture |
| Champion Call | Match end + T+24h | T+48h | New Final |
| Bridge volume spike | T+48h | T+72h | New tournament |
| CDI change | Next gate event | Gate superseded | New gate event |
| Macro regime | Regime change | Regime change | Price crosses floor |
| Partnership confirmed | Termination | Termination | N/A |
| Enacted regulation | Amended/repealed | Amended | N/A |
| Regulatory deadline | T+0 | T+30 (post-monitor) | Deferral resets |
| Lineup confirmation | Event start | Event start | N/A |
| MMA weight miss | Event start | Event start | N/A |
| Verified calibration | Never | Never | N/A |
| Seed calibration | Immediately (not actionable) | N/A | N/A |

---

## Signal Expiry Protocol

Unconfirmed signals are subject to expiry and retirement per
core/temporal-reasoning-framework.md Context 5.

| Signal type | Expiry threshold (if unconfirmed) | Action |
|---|---|---|
| Type 1 (supply event announcement) | 48 hours | RETIRE if not confirmed on-chain |
| Type 2 (demand signal) | Per event window | RETIRE at window close |
| Type 3 (structural, Tier 2 only) | 50 days | RETIRE unless Tier 1 received |
| Type 4 (regulatory bill, pre-vote) | Until session closes | MONITOR — no expiry |
| Type 4 (HP regulatory flag) | 90 days | REVIEW — escalate or CLOSE |
| Type 5 (operational) | Event start | RETIRE automatically |
| Type 6 (calibration) | Never | PERMANENT |

---

## Cross-Type Conflict Resolution

When two signal types conflict, apply these resolution rules
before using core/contradiction-resolution-framework.md.

| Conflict pair | Resolution rule |
|---|---|
| Type 1 (supply event) vs Type 2 (demand) | Type 1 governs. Supply is structural; demand is transient. |
| Type 3 (structural) vs Type 2 (demand) | Type 3 sets direction; Type 2 modulates magnitude. |
| Type 4 (regulatory) vs Type 3 (structural) | Type 4 governs when it imposes access constraints. Otherwise Type 3 governs direction. |
| Type 5 (operational) vs Type 2 (demand) | Type 5 governs for the specific event only. Type 2 resumes after event. |
| Type 6 (calibration wrong) vs Type 3 (structural) | Flag for modifier review. Do not immediately update — accumulate evidence first. |

---

## Known Signal Misclassification Failures

| Code | Name | Misclassification | Correct classification |
|---|---|---|---|
| FM1 | Price-Signal Conflation | Type 2 demand classified as Type 1 supply event | Type 2 · demand · MEDIUM reliability |
| FM4 | Sentiment Source Contamination | Type 2 structured mechanic classified as Type 3 structural | Type 2 · structured mechanic · bounded by event |
| FM7 | Cross-Token Signal Bleed | Type 2 bridge volume classified as organic demand | Type 2 · infrastructure subtype · not demand |
| TFM3 | Supply Event Conflation | Type 2 pre-match demand classified as Type 1 supply event timing | Type 2 · pre-match · expires at event start |

---

## MIND DIMENSIONS

| Dimension | Status | Notes |
|---|---|---|
| Intelligence (1) | ACTIVE | 1b Signal Awareness — primary sub-dimension. Knowing which type a signal is. |
| Reasoning (2) | ACTIVE | Classifying signal reliability and applying decay rates |
| Context (3) | ACTIVE | Signal type determines appropriate context window |
| Memory (4) | ACTIVE | Decay rate table and expiry protocol as procedural memory |
| Judgment (5) | ACTIVE | Reliability hierarchy governs confidence tier assignment |
| Attention (6) | ACTIVE | 6a-6d all active — prioritisation, urgency, noise filtering, threshold |
| Communication (7) | ACTIVE | Signal type notation in outputs |
| Verification (8) | ACTIVE | Type 1 requires on-chain confirmation · Type 3 requires Tier 1 source |
| Learning (9) | ACTIVE | Type 6 wrong-direction records drive modifier revision |
| Integration (10) | ACTIVE | Cross-type conflict resolution integrates with contradiction framework |
| Calibration (11) | ACTIVE | Type 6 signal hierarchy — verified vs seed distinction |
| Adaptation (12) | ACTIVE | Signal decay awareness and real-time reclassification |
| Ethics (13) | ACTIVE | Type 5 operational signals almost always fail Library Rule — transparency |
| Transparency (14) | ACTIVE | Signal type disclosed in all outputs — no silent classification |
| Execution (15) | ACTIVE | Signal type determines action (ENTER / HOLD / MONITOR / RETIRE) |
| Collaboration (16) | NOT APPLICABLE | — |

---

## COMPATIBILITY

- core/contradiction-resolution-framework.md — cross-type conflict resolution feeds into Rule 2 and Rule 3
- core/temporal-reasoning-framework.md — Context 3 (supply event timing), Context 5 (signal expiry)
- core/mind-dimensions-framework.md — Dimension 1b (Signal Awareness), Dimension 6 (Attention all sub-dims)
- fan-token/agent-failure-modes-fan-token.md — FM1, FM4, FM7 misclassification cross-reference
- fan-token/defi-integration-intelligence.md — bridge volume as Type 2 infrastructure subtype
- core/signal-confidence-framework.md — reliability hierarchy feeds into confidence tier assignment

© 2026 SportMind
