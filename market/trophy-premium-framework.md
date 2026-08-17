# Trophy Premium Framework

**Domain:** market/trophy-premium-framework.md
**Version:** v4.5.23
**Library Rule:** Six-Month Test PASSES · Proper Noun Test PASSES
**Scope:** Enduring post-event demand modifier reflecting the
structural impact of trophy success on fan token holder behaviour.
Trophy premium operates after an event — not during it. Distinct
from occasion weight (pre-match multiplier), CDI gate (structural
trajectory), and PTG/FTP supply events (on-chain mechanics).
Companion to market/rivalry-intelligence.md ·
core/compound-signal-framework.md · market/club-intelligence/.

---

## Critical Distinctions

Three things trophy premium is NOT — understand these before
applying.

NOT OCCASION WEIGHT:
  Occasion weight fires pre-match as a compound stack multiplier.
  Trophy premium fires post-event as an enduring CDI baseline
  modifier. They address different time horizons.
  Occasion weight: "How much does this fixture matter right now?"
  Trophy premium: "How does winning this trophy affect demand
  for the next 6-24 months?"

NOT A CDI GATE CHANGE:
  Trophy premium modifies the effective demand signal within
  an existing CDI gate classification. It does NOT upgrade
  a TRANSITION club to CONSOLIDATION, or a CONSOLIDATION
  club to GROWTH. Gate reclassification requires a formal
  CDI reassessment via Strategy & Brainstorm.
  A TRANSITION club with an active trophy premium is still
  TRANSITION — directional only. The premium increases the
  magnitude of the directional signal, not its confidence tier.

NOT A SUPPLY EVENT:
  PTG burns are on-chain supply events — separate mechanics.
  Trophy premium is a demand modifier. They are additive, not
  the same thing. For national tokens with PTG: trophy premium
  + completed PTG burns = compound positive signal. Never
  conflate the two. Source: fan-token/burn-to-glory-framework.md

WINS ONLY:
  Trophy premium applies to trophy wins only — not finalist
  positions. Runner-up finishes are captured by occasion weight
  (the pre-match compound signal). No enduring post-event
  premium applies to a loss. A finalist position that ends in
  defeat resets to zero post-event — no carryover modifier.

---

## Section 1 — Trophy Tier Classification

Four tiers. Apply the highest applicable tier. State tier
and modifier explicitly in every output. All values are
initial structural estimates — uncalibrated.

### TIER 1 — PINNACLE TROPHY
  Trophies: UCL · FIFA World Cup (national tokens) ·
    Copa Libertadores
  Modifier: +0.15 to CDI baseline demand signal
  Decay window: 24 months from win date
  Rationale: generational achievement for most clubs.
    Elevates global token appeal across two full seasons.
    Highest prestige in SportMind library.

### TIER 2 — MAJOR CONTINENTAL TROPHY
  Trophies: Europa League · UEFA Super Cup ·
    WC runner-up is NOT eligible (wins only) ·
    Copa Sudamericana
  Modifier: +0.08 to CDI baseline demand signal
  Decay window: 18 months from win date
  Reference case: $AVL Europa League 2025-26 (May 2026) —
    documented in market/club-intelligence/avl.md as CDI
    upgrade trigger alongside UCL qualification.
    Trophy premium: ACTIVE as of v4.5.23.

### TIER 3 — DOMESTIC TITLE
  Trophies: League championship in the club's primary
    domestic competition (PL · La Liga · Serie A ·
    Bundesliga · Ligue 1 · Süper Lig · Brasileirão ·
    equivalent for non-European tokens)
  Modifier: +0.05 to CDI baseline demand signal
  Decay window: 12 months from win date
  Rationale: domestic title matters most in the club's
    primary holder market — triggers heightened engagement
    for one full season.

### TIER 4 — DOMESTIC CUP / SECONDARY TROPHY
  Trophies: FA Cup · Coppa Italia · Copa del Rey ·
    Coupe de France · domestic cup equivalents ·
    Community Shield / domestic super cup
  Modifier: +0.03 to CDI baseline demand signal
  Decay window: 6 months from win date
  Rationale: the event itself carries primary weight
    (occasion weight). Enduring premium is modest.

### HERITAGE PREMIUM (pre-token era wins)
  Applies when: major trophy won before the club's fan
    token was active on Chiliz Chain.
  Modifier: one tier lower than the actual trophy tier.
    UCL win pre-token → applies as Tier 2 modifier (+0.08)
    EL win pre-token → applies as Tier 3 modifier (+0.05)
  Decay window: same as the downgraded tier.
  Rationale: trophy history creates holder affinity even
    before the token exists — but the direct demand impact
    of the win itself was not captured by token holders.
  Agent rule: verify token launch date before applying
    heritage premium. If trophy was won after token launch,
    apply standard tier — not heritage rate.

---

## Section 2 — Trophy Premium Decay Model

Trophy premium decays over time. Three stages.
Apply the stage that matches time elapsed since win date.
Verify win date from Tier 1 source before applying.

| Stage | Period | Modifier applied |
|---|---|---|
| ACTIVE | 0–6 months post-win | Full modifier (100%) |
| FADING | 7–18 months post-win | 50% of modifier |
| RESIDUAL | 19–24 months post-win | 25% of modifier (Tier 1 only) |
| EXPIRED | Beyond decay window | No modifier applied |

TIER DECAY WINDOWS SUMMARY:
  Tier 1: ACTIVE 0-6m · FADING 7-18m · RESIDUAL 19-24m
  Tier 2: ACTIVE 0-6m · FADING 7-18m · EXPIRED 19m+
  Tier 3: ACTIVE 0-12m · EXPIRED 13m+
  Tier 4: ACTIVE 0-6m · EXPIRED 7m+

RESET RULE:
  If a club wins another trophy during the ACTIVE or FADING
  period of an existing premium: reset to full ACTIVE modifier
  from the new win date. Apply the higher tier if different.
  Never stack two premiums for the same trophy tier —
  take the higher and reset.

STACKING RULE (different tiers):
  A club that wins both a UCL (Tier 1) and a domestic title
  (Tier 3) in the same season may carry both premiums
  simultaneously. Cap: maximum combined modifier of +0.20
  regardless of how many trophies are stacked.
  State each premium separately in output.

---

## Section 3 — Canonical Trophy Premium Register

Current confirmed trophy premium status for tokens in
the library. Verify win date and current decay stage
before applying. All modifiers uncalibrated.

| Token | Trophy | Tier | Full Modifier | Win Date | Stage (Aug 2026) |
|---|---|---|---|---|---|
| $PSG | UCL 2026 | 1 | +0.15 | May 2026 | ACTIVE |
| $AVL | Europa League 2025-26 | 2 | +0.08 | May 2026 | ACTIVE |
| $INTER | Serie A 2025-26 | 3 | +0.05 | May 2026 | ACTIVE |
| $GAL | Süper Lig 2025-26 (3rd consecutive) | 3 | +0.05 | May 2026 | ACTIVE |
| $SPAIN | FIFA World Cup 2026 | 1 | +0.15 | Jul 2026 | ACTIVE |
| $AFC | UCL 2026 finalist | — | — | — | NOT ELIGIBLE (loss) |
| $ARG | WC2026 finalist | — | — | — | NOT ELIGIBLE (loss) |
| $GALO | Copa Libertadores 2025 | 1 | +0.15 | Nov 2025 | ACTIVE |

NOTE ON $GALO: Copa Libertadores 2025 win date November 2025.
As of August 2026 (~9 months): FADING stage applies.
Effective modifier: +0.08 (50% of +0.15).
Verify win date and token active status before applying.

REGISTER INTEGRITY RULES:
  · Only confirmed trophy wins appear in this register.
  · Finalist positions are never added — wins only.
  · Verify win date from Tier 1 source (UEFA.com · FIFA.com ·
    CONMEBOL.com · official club sources) before applying.
  · New entries require CHANGELOG confirmation — never add
    in Build Chat without scope.
  · Update decay stage at each Strategy Chat or SMI session.

---

## Section 4 — Interaction with Compound Signal Framework

Trophy premium feeds into Layer 2 (CDI) of the compound
signal stack. It modifies the CDI baseline demand signal
before compound synthesis begins.

POSITION IN STACK:
  Load order: macro → CDI + trophy premium → form → H2H →
  venue → regulatory → compound → output.
  Trophy premium is applied to the CDI baseline BEFORE
  the compound stack resolves — not as a final multiplier.

CAPITULATION INTERACTION:
  CAPITULATION ×0.70 applies to the compound result including
  trophy premium. Trophy premium does NOT restore a suppressed
  signal. Under CAPITULATION, the premium is discounted along
  with all other demand signals.
  Example: CDI CONSOLIDATION baseline + Tier 1 premium (+0.15)
  under CAPITULATION ×0.70 = positive but materially discounted.

CDI GATE INTERACTION:
  TRANSITION gate: trophy premium applies to the directional
    signal but does not unlock high confidence output.
    TRANSITION cap remains. State explicitly:
    "CDI TRANSITION — trophy premium ACTIVE (+0.08) —
    directional only."
  CONSOLIDATION / GROWTH: full compound signal applies.
    Trophy premium amplifies within existing gate.
  DORMANT: no compound output warranted regardless of
    trophy premium. State: "CDI DORMANT — trophy premium
    noted but compound signal not produced."

PTG INTERACTION (national tokens):
  Trophy premium and PTG burns are additive layers — never
  conflate. For $SPAIN post-WC2026:
    PTG burns: on-chain supply events (supply reduction) —
      permanent, recorded in complete-registry.md.
    Trophy premium: demand modifier — time-decaying,
      expires 24 months post-win (July 2028).
  Both apply simultaneously. Report separately in output:
    "TROPHY PREMIUM: Tier 1 ACTIVE (+0.15 · WC2026 win)"
    "PTG SUPPLY: 8 burns · ~25.18% compound treasury burn"

RIVALRY INTERACTION:
  A derby fixture between a trophy premium club and a non-
  premium club creates CDI asymmetry within the rivalry
  occasion weight. Apply both layers independently:
    Step 1: Apply trophy premium to CDI baseline (Layer 2)
    Step 2: Apply rivalry weight as occasion weight (Layer 4)
    Step 3: Resolve compound stack
  Never merge trophy premium into rivalry weight — they
  are different layers applied at different stack positions.
  Source: market/rivalry-intelligence.md

---

## Section 5 — Agent Rules

8 rules. Never skip.

RULE 1 — WINS ONLY:
  Trophy premium applies to wins — never finalist positions.
  Runner-up finishes carry no enduring post-event premium.
  Occasion weight captures the fixture value — trophy premium
  captures the post-win enduring demand modifier only.

RULE 2 — VERIFY WIN DATE:
  Always verify trophy win date from a Tier 1 source before
  applying any modifier. Calculate decay stage from win date.
  Never assume Active status without date verification.

RULE 3 — CDI GATE UNCHANGED:
  Trophy premium does NOT change CDI gate classification.
  A TRANSITION club with trophy premium is still TRANSITION.
  Gate change requires Strategy & Brainstorm review.
  State gate AND premium separately in every output.

RULE 4 — SEPARATE FROM PTG:
  For national tokens: PTG supply events and trophy premium
  are additive and independent. Never conflate. Report both
  separately in output. Source: burn-to-glory-framework.md.

RULE 5 — HERITAGE RATE FOR PRE-TOKEN WINS:
  Verify token launch date before applying any premium.
  Pre-token era wins apply at one tier lower — heritage rate.
  Post-token era wins apply at full tier rate.

RULE 6 — STACKING CAP:
  Maximum combined trophy premium: +0.20 regardless of
  how many trophies are stacked. State each separately.
  Never exceed +0.20 combined modifier.

RULE 7 — REGISTER ONLY:
  Only apply trophy premium to tokens in Section 3.
  If a trophy win is not yet in the register: flag it in
  SMI briefing · verify from Tier 1 source · bring to
  Strategy & Brainstorm for register addition.
  Never invent a modifier for an unregistered win.

RULE 8 — UNCALIBRATED FLAG:
  All trophy premium values are initial structural estimates.
  State in every output: "TROPHY PREMIUM: UNCALIBRATED —
  initial structural estimate."
  Remove this flag when calibration pass is completed.

---

## Open Questions and Monitoring Flags

CALIBRATION PASS — PLANNED:
  All modifier values and decay windows are initial estimates.
  Target: 5+ verified calibration records per trophy tier.
  Bring to Strategy & Brainstorm before any value revision.
  Priority: Tier 2 ($AVL EL win) and Tier 3 (domestic title)
  records should accumulate fastest — calibrate those first.

TROPHY DROUGHT MODIFIER — DEFERRED:
  Extended trophy drought creates a structural demand
  suppressor for clubs where trophy expectation is embedded
  in the fan base. Deliberately excluded from v4.5.23 —
  drought only makes sense relative to fan base expectations,
  and those are not yet documented in the library.
  Design session required: fan-base-intelligence.md must
  exist first. Queue drought modifier as follow-up after
  fan-base-intelligence.md lands.

COPA LIBERTADORES CALIBRATION — MONITOR:
  $GALO Libertadores 2025 win is in the register but $GALO
  token active status requires verification before applying.
  Verify via complete-registry.md · fantokens.com before use.

CONSECUTIVE TITLE PREMIUM — FUTURE:
  $GAL has won 3 consecutive Süper Lig titles. Does
  consecutive title success amplify the premium beyond
  a single Tier 3 win? Not encoded in v4.5.23 — bring
  to Strategy & Brainstorm with calibration evidence.

NATIONAL TOKEN EXPANSION — MONITOR:
  $SAFA and $SFA both active but no major international
  trophy wins yet. AFCON (HP-9) and EURO 2028 (HP-10) are
  the first realistic Tier 1/2 opportunities. No register
  entries until wins confirmed.

---

## Sources and Verification

PRIMARY SOURCES:
  market/club-intelligence/ — CDI files for all clubs
  fan-token/registry/complete-registry.md — token status
    and PTG burn history
  fan-token/burn-to-glory-framework.md — PTG mechanics
  market/rivalry-intelligence.md — rivalry weights
  core/compound-signal-framework.md — compound synthesis
  UEFA.com · FIFA.com · CONMEBOL.com — trophy verification
  SportMind calibration records — community/calibration-data/

CALIBRATION STATUS:
  UNCALIBRATED. All modifier values, decay windows, and
  tier classifications are initial structural estimates.
  Calibration pass planned when 5+ verified records per
  tier exist. Do not treat any value as confirmed until
  calibrated.

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
core/compound-signal-framework.md ·
core/contradiction-resolution-framework.md ·
market/rivalry-intelligence.md ·
market/club-intelligence/ (all CDI files) ·
fan-token/burn-to-glory-framework.md ·
fan-token/registry/complete-registry.md ·
fan-token/competition-calendar-framework.md ·
sports/football/sport-domain-football.md ·
community/calibration-data/football/

© 2026 SportMind
