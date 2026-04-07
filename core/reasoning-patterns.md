# Reasoning Patterns — SportMind Agent Chain-of-Thought Framework

**The formal reasoning model for SportMind agents.**
Every skill file has an "agent reasoning prompts" section. The loading order defines
a reasoning sequence. The confidence output schema enforces structured output. But
nowhere — until now — has the library stated explicitly: here is the chain of thought
an agent should follow when reasoning about a sports intelligence question.

This document makes the implicit explicit. It is the reasoning substrate that connects
all other parts of the library.

---

## The six-step SportMind reasoning chain

Every SportMind analysis follows this chain. The steps are not optional — skipping
any step degrades SMS and the accuracy of the output.

```
STEP 1 — MACRO CHECK
  Question: Is there an active macro event that overrides or modifies all signals?
  Load: platform/macro-state.json
  Decision: If macro_modifier ≠ 1.00 → apply to ALL subsequent signal calculations
            If macro_override_active → consider whether to proceed at all
  Output: macro_modifier (carry forward through all steps)

STEP 2 — COMPETITION CLASSIFICATION
  Question: What kind of event is this and what weight does it carry?
  Load: sports/{sport}/sport-domain-{sport}.md — Event Hierarchy section
  Decision: Assign competition_tier_weight (0.10 to 1.00)
  Output: competition_tier_weight (this becomes the base for STEP 4)

STEP 3 — ATHLETE AVAILABILITY
  Question: Who is actually playing and in what condition?
  Load: athlete/{sport}/athlete-intel-{sport}.md
  Decision: Is lineup confirmed? Any injury_warning flags?
  Output: athlete_modifier (0.55–1.25) and lineup_unconfirmed flag (boolean)
  
  CRITICAL: If lineup_unconfirmed = True, halve the recommended position size.
  Do not skip this step because lineup seems obvious — confirm it.

STEP 4 — SIGNAL COMPUTATION
  Question: What does the evidence say about the likely outcome?
  Inputs: competition_tier_weight (STEP 2) × athlete_modifier (STEP 3)
          × narrative_modifier (if active) × macro_modifier (STEP 1)
  Output: adjusted_score (0–100) and confidence_tier (LOW/MEDIUM/HIGH)

STEP 5 — DEFI / LIQUIDITY CHECK (fan token applications only)
  Question: Is there sufficient liquidity to act on this signal?
  Load: fan-token/defi-liquidity-intelligence/
  Decision: If TVL < $100k → signal is valid but ABSTAIN on execution
            If slippage > 3% → reduce position size or split execution
  Output: liquidity_warning or liquidity_critical flag

STEP 6 — CONFIDENCE OUTPUT
  Question: What is the SportMind Score and what should the agent recommend?
  Compute: SMS = (layer_coverage × 0.35) + (data_freshness × 0.25)
                + (flag_health × 0.25) + (modifier_confidence × 0.15)
  Output: Full confidence schema — adjusted_score, sms, sms_tier, flags,
          recommended_action, sizing, reasoning_summary
```

---

## Handling conflicting signals

The most common failure mode in sports intelligence is applying a simple signal
when two conflicting signals are present. SportMind handles this with a hierarchy.

```
SIGNAL CONFLICT RESOLUTION HIERARCHY:

Priority 1 — Hard overrides (always win):
  macro_override_active = True → reduces all signals regardless of sporting evidence
  liquidity_critical = True → ABSTAIN regardless of signal quality
  lineup_unconfirmed at T-0 → do not enter until confirmed

Priority 2 — Soft overrides (adjust but do not cancel):
  injury_warning for key player → apply × 0.85 regardless of team form
  weather_risk (cricket dew, F1 rain) → apply sport-specific weather modifier
  manager_departure_imminent flag → apply MgSI instability modifier

Priority 3 — Competing positives/negatives (average with weights):
  Strong form (× 1.15) + negative NCSI from recent international (× 0.88):
  → Weighted average: (1.15 × 0.60) + (0.88 × 0.40) = 1.04 composite
  → Rule: never simply choose the stronger signal; weight by recency and relevance

Priority 4 — Genuine uncertainty (reduce confidence tier):
  Two equally weighted opposing signals with no clear resolution:
  → Drop confidence_tier one level (HIGH → MEDIUM, MEDIUM → LOW)
  → Note conflict in reasoning_summary
  → Do not fabricate a resolution that isn't supported

EXAMPLE — STRONG FORM vs RECENT SACKING:
  Manchester City: strong form (× 1.12)
  Manager sacked 3 days ago, caretaker appointed (× 0.93 drag from Match 3+)
  
  WRONG: "Form is strong so apply × 1.12 — manager change is noise"
  WRONG: "Manager sacked so apply × 0.93 — form is irrelevant"
  RIGHT: "Form × 1.12 weighted at 0.55 (recent, sustained) + caretaker × 0.93
         weighted at 0.45 (significant but short-term) = × 1.02 composite.
         Note: caretaker_uncertainty_drag will increase if appointment extends past
         Match 5. Monitor."
```

---

## Reasoning under uncertainty

SportMind agents operate with incomplete information. The correct response to
incomplete information is not to fabricate completeness — it is to quantify the
gap and adjust SMS accordingly.

```
INCOMPLETE INFORMATION PROTOCOL:

LINEUP UNKNOWN (most common):
  Do not assume the expected lineup. Set lineup_unconfirmed = True.
  Apply 50% position size recommendation.
  State explicitly in reasoning_summary: "Lineup unconfirmed — signal at 50% weight."
  
FORM DATA STALE (> 4 weeks — see core/temporal-awareness.md):
  Apply Tier 2 reliability degradation formula.
  Note in output: "Form data is X weeks old — apply × 0.85 reliability."
  
MACRO STATE UNKNOWN:
  If macro-state.json is missing or > 24h old:
  Set macro_modifier = 1.00 (neutral default) with explicit warning.
  Never assume a bull or bear market — this is a critical error.
  
SPORT OUTSIDE LIBRARY COVERAGE:
  If a sport has no dedicated skill file:
  Apply generic pre-match framework (competition tier only).
  Set SMS to maximum 45 (PARTIAL) — explicitly state coverage gap.
  Do not generate a full confidence output for uncovered sports.

THE HONESTY PRINCIPLE:
  An SMS of 45 with a clear explanation is more valuable than an SMS of 80
  that was fabricated by filling gaps with assumptions.
  Always prefer lower SMS + clear reasoning over higher SMS + hidden assumptions.
```

---

## Sport-specific reasoning variations

The six-step chain applies to all sports but the relative weight of each step
varies by sport. These are the documented sport-specific adjustments.

```
FOOTBALL:
  STEP 3 heaviest: Squad depth and fitness matters most
  Lineup_unconfirmed is the highest-frequency flag in the library
  STEP 2 critical: Competition tier gap between UCL and domestic is very wide
  
CRICKET:
  STEP 2 heaviest: Format (T20/ODI/Test) changes the entire model
  Format identification must happen before STEP 1 — it is pre-chain
  Weather (dew factor) is a STEP 3 equivalent for evening T20s
  
MMA:
  STEP 3 = STEP 1 equivalent: Weigh-in result supersedes all other signals
  If fighter misses weight: reload chain from scratch with weight_miss flag
  Style matchup is STEP 2 equivalent for MMA (not competition tier)
  
FORMULA 1:
  STEP 3 equivalent: Hardware tier (more persistent than athlete form)
  Weather is a genuine STEP 1 override: wet race = hardware tier reset
  Qualifying delta (STEP 4 input) is the single most predictive variable
  
NBA / BASKETBALL:
  STEP 3 critical: Star player availability dominates more than any other sport
  Load management is a form of lineup_unconfirmed — treat it as such
  Conference standings affect STEP 2 weight significantly in playoff positioning

NHL / ICE HOCKEY:
  Goaltender confirmation is STEP 3's most critical element
  Morning skate (T-6h) = goaltender confirmation window
  Back-to-back second game = automatic STEP 3 flag
  
MotoGP:
  Weather check is STEP 1 equivalent (wet race restructures entire hierarchy)
  Hardware tier is the most persistent single variable — update only at season start
  Sprint race (Saturday) and Grand Prix (Sunday) are separate chain executions
```

---

## Reasoning chain for commercial intelligence

When the question is commercial (APS, governance, scouting) rather than pre-match,
the chain adapts:

```
COMMERCIAL REASONING CHAIN:

STEP 1 — MACRO CHECK (same as pre-match)
  Is the crypto cycle affecting commercial asset values?
  Bear market = compressed token commercial premiums

STEP 2 — ENTITY CLASSIFICATION
  Who are we assessing? Player / club / partnership / token launch?
  Load appropriate commercial brief stack

STEP 3 — FINANCIAL LAYER (new to commercial chain)
  What is the athlete's wage structure relative to market?
  What is the fee/investment relative to benchmarks?
  Load: core/athlete-financial-intelligence.md (v3.12)

STEP 4 — COMMERCIAL METRIC COMPUTATION
  ABS, APS, AELS, DTS, TAI, PS — full commercial brief
  Cross-reference metrics: APS meaningless without financial layer context

STEP 5 — LIFECYCLE CONTEXT
  Where is this entity in the fan token lifecycle?
  Load: fan-token/fan-token-lifecycle/
  LTUI impact: what does this decision do to lifetime utility?

STEP 6 — RECOMMENDATION
  Frame as intelligence context, not financial advice
  State what SportMind shows; do not recommend specific financial decisions
  Always include confidence tier and SMS
```

---

## The SportMind reasoning anti-patterns

These are the failure modes that produce poor analysis. Documenting them
explicitly prevents agents from falling into them.

```
ANTI-PATTERN 1 — Skipping macro:
  "This match is important so I'll analyse the team directly."
  PROBLEM: A correct sporting prediction during an extreme bear market produces
  a losing token trade. Macro is always first.

ANTI-PATTERN 2 — Assuming the lineup:
  "This player always starts, so lineup is confirmed."
  PROBLEM: Expected lineup ≠ confirmed lineup. Set lineup_unconfirmed until T-2h.

ANTI-PATTERN 3 — Single-variable analysis:
  "The star player is injured, so the signal is negative."
  PROBLEM: One variable rarely determines outcome. Apply the full chain.

ANTI-PATTERN 4 — False precision:
  "Adjusted score is 73.847."
  PROBLEM: The model is not this precise. Round to one decimal maximum.
  False precision signals false confidence.

ANTI-PATTERN 5 — Ignoring staleness:
  "Here is the form data." [loaded once, never refreshed]
  PROBLEM: Form data > 4 weeks old must be flagged. See core/temporal-awareness.md.

ANTI-PATTERN 6 — Conflating prediction and token signals:
  "Our prediction is correct, therefore the token will rise."
  PROBLEM: Prediction market signal ≠ fan token signal. Macro separates them.
  See: calibration-data/mma/2022/11/ (UFC 281 case study).

ANTI-PATTERN 7 — Over-narrating:
  Generating a compelling narrative for a signal that has SMS 38.
  PROBLEM: Low SMS means insufficient intelligence. State the gap clearly.
  Do not fill intelligence gaps with narrative confidence.
```

---

## Reasoning chain validation checklist

Run this checklist before producing any final SportMind output:

```
PRE-OUTPUT VALIDATION:
  [ ] Macro state checked (even if modifier = 1.00)
  [ ] Competition tier assigned (not assumed)
  [ ] Lineup confirmed OR lineup_unconfirmed flag set
  [ ] Athlete modifier computed from current data
  [ ] DeFi context checked (for fan token applications)
  [ ] SMS computed from actual layers loaded (not estimated)
  [ ] No anti-patterns present in reasoning
  [ ] Freshness warning added if any Tier 3+ data is stale
  [ ] reasoning_summary is ≤ 3 sentences (longer = over-explaining uncertainty)
  [ ] recommended_action matches SMS tier (no ENTER at SMS < 60)
```

---

## Compatibility

**Confidence output schema:** `core/confidence-output-schema.md` — output format
**SportMind Score:** `core/sportmind-score.md` — SMS calculation
**Temporal awareness:** `core/temporal-awareness.md` — data freshness by tier
**Manager intelligence:** `core/manager-intelligence.md` — MgSI as Step 3 input
**Officiating intelligence:** `core/core-officiating-intelligence.md` — referee as Step 3 input
**All agent prompts:** `agent-prompts/agent-prompts.md` — sport-specific prompt templates

*MIT License · SportMind · sportmind.dev*
