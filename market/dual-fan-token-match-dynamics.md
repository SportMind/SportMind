# Dual Fan Token Match Dynamics

Domain: market/dual-fan-token-match-dynamics.md
Version: v4.5.28
Library Rule: Six-Month Test PASSES · Proper Noun Test PASSES
Scope: Framework governing compound signal analysis when two active
Chiliz fan tokens meet in the same fixture. A dual-token fixture is
not two separate analyses — it is one fixture producing two token
outputs that must be related to each other. The relationship between
the two outputs is itself intelligence. Companion to
core/compound-signal-framework.md · market/rivalry-intelligence.md ·
market/trophy-premium-framework.md · market/fan-base-intelligence.md.

---

CRITICAL DISTINCTION — Dual Token vs Single Token Analysis

An agent that produces two independent single-token analyses for a
dual-token fixture and presents them side by side has missed the
point. The dual-token relationship — ALIGNED, ASYMMETRIC, or
CONFLICTED — is mandatory intelligence that must be surfaced
explicitly in every dual-token output.

WHAT THIS FILE ADDRESSES:
  · How to sequence dual-token compound analysis correctly
  · How to resolve CDI asymmetry between two tokens in the same
    fixture
  · How to handle supply event asymmetry (PATH_2 on one side only)
  · How to apply the HOLD gate when one token passes and one does not
  · How to report dual-token output in a structured format that
    surfaces the relationship between the two outputs

WHAT THIS FILE DOES NOT REPLACE:
  · core/compound-signal-framework.md — single-token compound logic
    still applies to each token independently before comparison
  · market/rivalry-intelligence.md — rivalry tier and occasion weight
    source; this file consumes it, does not redefine it
  · core/contradiction-resolution-framework.md — load for CONFLICTED
    relationship type; this file identifies the conflict, that file
    resolves it

---

SECTION 1 — Dual Token Analysis Sequencing

Six steps. Complete in order. Never skip or reorder.

STEP 1 — IDENTIFY DUAL TOKEN STATUS:
  Verify BOTH clubs have confirmed active Chiliz fan tokens via
  fan-token/registry/complete-registry.md before proceeding.
  Black logo = potentially inactive — verify before proceeding.
  If only one club has an active token: single-token analysis only.
  Load market/rivalry-intelligence.md to confirm dual vs single-token
  weight for the rivalry tier.

STEP 2 — LOAD SHARED LAYERS:
  These layers are the same for both tokens. Load once, apply to both.
  Do not load independently for each token — creates inconsistency.
  · Macro regime (CHZ CAPITULATION / ANXIETY / BULL)
  · Venue (home/away/neutral · capacity modifier)
  · Occasion weight (rivalry tier from market/rivalry-intelligence.md ·
    competition tier from fan-token/competition-calendar-framework.md)
  · Regulatory overlay (load fan-token/holder-tax-framework.md —
    jurisdiction applies to both tokens' holder populations equally)
  · Macro gate check: if CAPITULATION active, note x0.70 suppressor
    applies to BOTH tokens before proceeding

STEP 3 — LOAD TOKEN-SPECIFIC LAYERS:
  These layers differ per token. Load separately for each.
  FOR EACH TOKEN:
  · CDI gate classification (market/club-intelligence/[token].md)
  · Form signal (recent results · squad health · coaching stability)
  · H2H (core/h2h-framework.md — apply from each token's perspective)
  · Trophy premium (market/trophy-premium-framework.md — independent
    per token · do not transfer one club's premium to the other)
  · Fan base tier (market/fan-base-intelligence.md — independent
    per token · note any demand ceiling differential)
  · Supply event status (PATH_2 for $AFC · PTG for national tokens ·
    verify per token — do not assume symmetry)

STEP 4 — RESOLVE EACH TOKEN'S COMPOUND STACK INDEPENDENTLY:
  Apply core/compound-signal-framework.md five-layer process to each
  token separately. Produce a compound result for Token A and a
  separate compound result for Token B before comparing.
  CAPITULATION x0.70 applies to both results at this stage.

STEP 5 — IDENTIFY RELATIONSHIP TYPE:
  Compare the two compound results. Classify as:
  · ALIGNED: both signals point in the same direction
  · ASYMMETRIC: signals differ in direction, confidence, or both
  · CONFLICTED: genuine contradiction — no clear dominant signal
  This classification is mandatory. Never proceed to Step 6 without it.

STEP 6 — APPLY OCCASION WEIGHT AND PRODUCE OUTPUT:
  Apply the rivalry occasion weight (from market/rivalry-intelligence.md)
  to both compound results. Apply LAST — after all layers are stacked
  per FM-CS-2. Produce the dual-token output block using the mandatory
  format in Section 6.

---

SECTION 2 — Three Dual Token Relationship Types

TYPE 1 — ALIGNED

Definition: both tokens produce compound signals in the same direction.
Both positive, or both negative. The occasion weight amplifies both
signals in the same direction.

When it occurs: both clubs in similar CDI phases · form aligned ·
  occasion drives both toward same directional output.

Output instruction:
  DUAL-TOKEN ALIGNED — both tokens [direction] · rivalry weight
  x[tier] applied to both. Confidence may differ between tokens —
  state each token's confidence tier separately even when direction
  is shared.

Note: ALIGNED does not mean equal confidence. A CONSOLIDATION token
and a TRANSITION token can both produce positive signals — the
CONSOLIDATION output carries full confidence, the TRANSITION output
is directional only. Report both.

TYPE 2 — ASYMMETRIC

Definition: the two tokens produce signals in different directions,
or one produces full-confidence output while the other is capped at
directional only, or confidence tiers differ materially.

Most common dual-token scenario. Occurs in almost every derby where
one club is in demonstrably better shape than the other.

Three asymmetric sub-types:

CDI ASYMMETRY (most common):
  One token CONSOLIDATION · one token TRANSITION.
  CONSOLIDATION token: full compound signal · normal confidence tier.
  TRANSITION token: directional only · TRANSITION cap enforced
    regardless of occasion weight tier.
  The rivalry weight x1.80 (or applicable tier) amplifies the
  directional TRANSITION signal but does NOT unlock full confidence.
  State: CDI ASYMMETRY — $[TOKEN A] CONSOLIDATION (full signal) ·
  $[TOKEN B] TRANSITION (directional only · TRANSITION cap enforced)

FORM ASYMMETRY:
  Both tokens at similar CDI phase but form signals diverge.
  One club winning run · one club poor form or mixed.
  Occasion weight amplifies both — but in opposite directions.
  State the form asymmetry and its compound effect explicitly.
  Do not average the form signals.

CONFIDENCE ASYMMETRY:
  Same direction but materially different confidence tiers.
  One HIGH · one MEDIUM. Or one MEDIUM · one LOW.
  Do not average into a single confidence tier for the fixture.
  State each token's confidence tier in the output block.

TYPE 3 — CONFLICTED

Definition: the compound stacks produce genuinely contradicting outputs
with no clear dominance relationship. Typically: both tokens
CONSOLIDATION but H2H, form, and CDI point in contradictory directions
for one or both tokens.

When it occurs: near-equal CDI phases · opposing form · H2H ambiguous.

Resolution: load core/contradiction-resolution-framework.md.
Never resolve conflict by averaging the two outputs.
Surface the conflict explicitly in the output block.
Flag to analyst or user for judgment if unresolved.

---

SECTION 3 — CDI Asymmetry Resolution Rules

CDI asymmetry is the defining characteristic of most dual-token
derbies — clubs are rarely at the same CDI stage simultaneously.
Five rules govern how CDI asymmetry is handled.

RULE A — TRANSITION CAP IS UNCONDITIONAL:
  A TRANSITION club in a Tier 1 derby (occasion weight x1.80) still
  only receives directional output. The occasion weight multiplies
  the directional signal but does not unlock confidence.
  Never produce a high-confidence output for a TRANSITION token
  regardless of occasion weight tier or rivalry prestige.

RULE B — TROPHY PREMIUM APPLIES INDEPENDENTLY:
  Each token's trophy premium (from market/trophy-premium-framework.md)
  applies only to that token's compound stack. If Token A has an
  active Tier 1 trophy premium (+0.15) and Token B has none, the
  premium modifies Token A's CDI baseline only.
  Never transfer one club's trophy premium to the opponent.

RULE C — FAN BASE TIER IS INDEPENDENT:
  Each token carries its own fan base tier from
  market/fan-base-intelligence.md. If both tokens are Tier 1
  (e.g. $INTER and $ACM both global megaclubs), note it as
  context — neither has a demand ceiling advantage.
  If the matchup is Tier 1 vs Tier 3, note the demand ceiling
  differential as structural context in the output.

RULE D — RIVALRY WEIGHT APPLIES TO BOTH TOKENS REGARDLESS OF CDI:
  The rivalry occasion weight is an attribute of the fixture, not
  of individual token health. A Derby Tier 1 weight of x1.80 applies
  to both the CONSOLIDATION token and the TRANSITION token.
  The TRANSITION token's result is capped at directional before the
  multiplier applies — but the multiplier still applies.

RULE E — CAPITULATION IS SHARED:
  The macro regime suppressor (CAPITULATION x0.70) applies to both
  tokens equally. It is a shared layer loaded in Step 2.
  Neither token escapes the suppressor.
  Neither token can offset the suppressor using trophy premium,
  rivalry weight, or fan base tier.

---

SECTION 4 — Supply Event Asymmetry

Supply events are token-specific. Never apply one token's supply
event mechanics to the opponent.

$AFC PATH_2 IN A DUAL TOKEN FIXTURE:
  $AFC is the only confirmed FTP PATH_2 token as of 2026-08-18.
  When $AFC meets a dual-token opponent:
  The PATH_2 supply event fires on the $AFC result only.
  The opponent has no equivalent supply event unless separately
  confirmed via fan-token/registry/complete-registry.md.

  Report structure:
  SUPPLY EVENTS:
   $AFC PATH_2: ACTIVE — WIN burns · LOSS mints · DRAW = no event
   $[OPPONENT]: NO SUPPLY EVENT — not applicable

  Never mention PATH_2 in the opponent's demand signal block.
  Never apply $AFC's burn/mint mechanic to the opponent's output.
  Never imply the opponent's holders are affected by $AFC's PATH_2.

PTG BURNS (NATIONAL TOKENS):
  If a national token with confirmed PTG mechanics meets another
  active token in a cup competition:
  Apply PTG supply event to the national token only.
  The opponent token has no PTG equivalent unless separately confirmed.
  Report in the same asymmetric format as PATH_2.

NO SUPPLY EVENT ON EITHER SIDE:
  Most dual-token fixtures have no supply events on either side.
  Report: SUPPLY EVENTS: NEITHER TOKEN — no supply events applicable.
  Do not omit this field — its presence confirms the check was done.

FUTURE SUPPLY EVENTS:
  If new PATH_2 or PTG-equivalent mechanics are confirmed for
  additional tokens, update this file via Strategy & Brainstorm
  before applying asymmetric supply event logic to those tokens.
  Never apply supply event mechanics to unconfirmed tokens.

---

SECTION 5 — HOLD Gate in Dual Token Context

The HOLD gate (SMS below 80) applies per token.
A dual-token fixture can produce three HOLD gate outcomes.

OUTCOME 1 — BOTH TOKENS PASS (SMS >= 80 each):
  Full dual-token output produced. All layers loaded for both tokens.
  Proceed through all six analysis steps.

OUTCOME 2 — ONE TOKEN PASSES, ONE HOLDS:
  The passing token: produce full compound output as normal.
  The HOLD token: state SMS [score] — HOLD gate active. Compound
    signal not produced for $[TOKEN]. Missing layers: [list].
  Report as PARTIAL DUAL-TOKEN OUTPUT:
  DUAL-TOKEN STATUS: PARTIAL — $[TOKEN A] output produced ·
   $[TOKEN B] HOLD gate active (SMS [score])
  Do not attempt to infer the HOLD token's signal from the passing
  token's output. The relationship type cannot be determined when
  one token is on HOLD — state:
  RELATIONSHIP TYPE: INDETERMINATE (one token on HOLD — relationship
  cannot be assessed)

OUTCOME 3 — BOTH TOKENS HOLD:
  No dual-token output produced.
  State: DUAL-TOKEN FIXTURE: BOTH TOKENS — HOLD gate active.
   $[TOKEN A]: SMS [score] · $[TOKEN B]: SMS [score]
   Compound signal not produced for either token.
   Load missing layers before proceeding.

PARTIAL LOADING DEFAULTS:
  If a specific layer is unavailable, apply the partial loading
  defaults from core/compound-signal-framework.md Section 6.
  Recalculate SMS after applying defaults. HOLD gate rule applies
  to the recalculated SMS, not the raw score.

---

SECTION 6 — Mandatory Dual Token Output Format

Required for every dual-token fixture analysis.
All fields mandatory — never omit any field.
Single-token output format is not sufficient for dual-token fixtures.

DUAL-TOKEN FIXTURE: [Competition] · [Token A] vs [Token B]
RIVALRY TIER: [Tier 1/2/3/4] · Weight: x[value]
  Source: market/rivalry-intelligence.md
RELATIONSHIP TYPE: [ALIGNED / ASYMMETRIC / CONFLICTED / INDETERMINATE]
MACRO REGIME: [CAPITULATION x0.70 / ANXIETY x1.00 / BULL x1.15]
  Applied to both tokens confirmed
VENUE: [home/away/neutral] · [FORTRESS/STANDARD/HOSTILE/NEUTRAL]
REGULATORY: [primary jurisdiction(s) · friction level]
  Applied to both tokens confirmed

TOKEN A — $[SYMBOL]:
  CDI gate: [CONSOLIDATION / TRANSITION / GROWTH / EMERGING / DORMANT]
  Form: [winning run / mixed / poor form]
  Trophy premium: [ACTIVE · Tier [N] · +[modifier] · [decay stage]]
                  OR [NOT APPLICABLE]
  Fan base tier: [Tier 1/2/3/4 · demand ceiling context]
  H2H: [HOME LEAN / AWAY LEAN / BALANCED / INSUFFICIENT SAMPLE]
  Compound signal: [POSITIVE / DIRECTIONAL POSITIVE / NEUTRAL /
                    DIRECTIONAL NEGATIVE / NEGATIVE]
  Confidence tier: [HIGH / MEDIUM / LOW / DIRECTIONAL ONLY]
    (TRANSITION cap note if applicable)
  Occasion weight x[value] applied to [discounted] compound result
  Supply event: [PATH_2 ACTIVE — WIN burns · LOSS mints · DRAW no event]
                OR [NOT APPLICABLE]

TOKEN B — $[SYMBOL]:
  CDI gate: [classification]
  Form: [signal]
  Trophy premium: [status]
  Fan base tier: [tier · context]
  H2H: [signal]
  Compound signal: [output]
  Confidence tier: [tier]
    (TRANSITION cap note if applicable)
  Occasion weight x[value] applied to [discounted] compound result
  Supply event: [status]

DUAL-TOKEN RELATIONSHIP:
  Type: [ALIGNED / ASYMMETRIC / CONFLICTED / INDETERMINATE]
  [ALIGNED: both signals [direction] · occasion weight amplifies both ·
   confidence differential: $[A] [tier] vs $[B] [tier]]
  [ASYMMETRIC: $[A] [output/confidence] vs $[B] [output/confidence] ·
   [CDI asymmetry / form asymmetry / confidence asymmetry] noted]
  [CONFLICTED: genuine contradiction identified ·
   load core/contradiction-resolution-framework.md ·
   do not produce directional output until resolved]
  [INDETERMINATE: one or both tokens on HOLD gate ·
   relationship cannot be assessed — load missing layers]

SUPPLY EVENTS:
  $[TOKEN A]: [PATH_2 ACTIVE / PTG mechanic / NOT APPLICABLE]
  $[TOKEN B]: [PATH_2 ACTIVE / PTG mechanic / NOT APPLICABLE]
  [OR: NEITHER TOKEN — no supply events applicable]

NOTE: Compound signals are demand modifiers — not outcome predictors.
DUAL-TOKEN DYNAMICS: UNCALIBRATED — initial structural framework (v4.5.28)

---

SECTION 7 — Worked Example 1: CDI Asymmetry + Italian Tax

FIXTURE: Derby della Madonnina · Serie A · $INTER vs $ACM
RIVALRY TIER: Tier 1 · Weight: x1.80 · DUAL-TOKEN confirmed
Source: market/rivalry-intelligence.md

SHARED LAYERS (Step 2):
  Macro regime: CAPITULATION x0.70 · applies to both confirmed
  Venue: San Siro SHARED · designated home club STANDARD x0.5
  Occasion weight: Derby Tier 1 x1.80 (rivalry-intelligence.md)
  Regulatory: Italy 33% CGT flat · HIGHEST FRICTION in library ·
    applies to both tokens' Italian domestic holder base ·
    PTG burn tax treatment: UNRESOLVED for both · flag only ·
    Source: macro/regulatory/italy.md

TOKEN-SPECIFIC LAYERS (Steps 3 and 4):

  $INTER:
    CDI gate: CONSOLIDATION · full compound signal applies
    Form: winning run in Serie A · positive modifier
    Trophy premium: Serie A 2025-26 · Tier 3 · +0.05 · ACTIVE
      (within 12-month decay window as of 2026-08)
    Fan base tier: Tier 1 (50M+ global fans · Italian domestic
      primary · Japanese secondary)
    H2H: slight $INTER lean in recent era (verify current before
      applying — h2h-framework.md gate must pass)
    Compound stack: POSITIVE · MEDIUM-HIGH confidence
      (CAPITULATION x0.70 discounts result)
    Occasion weight x1.80 applied to discounted result

  $ACM:
    CDI gate: TRANSITION · directional output only · cap enforced
    Form: mixed · no directional form modifier
    Trophy premium: NOT APPLICABLE
    Fan base tier: Tier 1 (60M+ global fans · Italian domestic primary ·
      Japanese secondary — same structural tier as $INTER)
    H2H: $INTER lean applies inversely · slight away lean for $ACM
      context (verify current)
    Compound stack: DIRECTIONAL POSITIVE (home fixture context ·
      venue modifier · H2H context applied directionally) ·
      LOW confidence · TRANSITION CAP ENFORCED
      Occasion weight x1.80 amplifies directional signal but does
      NOT unlock confidence — TRANSITION cap holds
    Occasion weight x1.80 applied to directional result

RELATIONSHIP TYPE: ASYMMETRIC
  Sub-type: CDI ASYMMETRY
  $INTER CONSOLIDATION (full signal · MEDIUM-HIGH) vs
  $ACM TRANSITION (directional only · LOW · cap enforced)
  Form asymmetry compounds further: $INTER winning run vs $ACM mixed

SUPPLY EVENTS: NEITHER TOKEN — no supply events applicable

FULL OUTPUT BLOCK:
  DUAL-TOKEN FIXTURE: Serie A · $INTER vs $ACM
  RIVALRY TIER: Tier 1 · Weight: x1.80 · DUAL-TOKEN confirmed
  RELATIONSHIP TYPE: ASYMMETRIC (CDI asymmetry · form asymmetry)
  MACRO REGIME: CAPITULATION x0.70 · applied to both confirmed
  VENUE: San Siro SHARED · STANDARD home advantage (designated home)
  REGULATORY: Italy 33% CGT · HIGHEST FRICTION · both tokens ·
    PTG burn tax UNRESOLVED · flag only

  TOKEN A — $INTER:
    CDI gate: CONSOLIDATION
    Form: winning run · positive
    Trophy premium: ACTIVE · Tier 3 · +0.05 · Serie A 2025-26
    Fan base tier: Tier 1 · 50M+ · Italian + Japanese friction overlay
    H2H: slight HOME LEAN (verify current)
    Compound signal: POSITIVE · MEDIUM-HIGH confidence
    Occasion weight x1.80 applied to CAPITULATION-discounted result
    Supply event: NOT APPLICABLE

  TOKEN B — $ACM:
    CDI gate: TRANSITION · TRANSITION CAP ENFORCED
    Form: mixed · no directional modifier
    Trophy premium: NOT APPLICABLE
    Fan base tier: Tier 1 · 60M+ · Italian + Japanese friction overlay
    H2H: slight AWAY LEAN context (verify current)
    Compound signal: DIRECTIONAL POSITIVE · DIRECTIONAL ONLY
      TRANSITION cap enforced — x1.80 amplifies directional signal ·
      does NOT unlock confidence
    Occasion weight x1.80 applied to directional result
    Supply event: NOT APPLICABLE

  DUAL-TOKEN RELATIONSHIP:
    Type: ASYMMETRIC
    $INTER full signal MEDIUM-HIGH vs $ACM directional only LOW ·
    CDI asymmetry is dominant driver · form asymmetry compounds ·
    Occasion weight x1.80 amplifies both but cannot close CDI gap ·
    Italian tax friction applies equally — neither token advantaged
    on regulatory dimension

  SUPPLY EVENTS: NEITHER TOKEN — no supply events applicable

  NOTE: Compound signals are demand modifiers — not outcome predictors.
  DUAL-TOKEN DYNAMICS: UNCALIBRATED — initial structural framework (v4.5.28)

---

SECTION 8 — Worked Example 2: PATH_2 Supply Event Asymmetry

FIXTURE: UCL Round of 16 · $AFC vs [dual-token opponent]
NOTE: Named opponent omitted — archetype only (CONSOLIDATION gate ·
  active Chiliz token confirmed · no supply event).

SHARED LAYERS (Step 2):
  Macro regime: CAPITULATION x0.70 · applies to both confirmed
  Venue: away leg (neutral/opponent ground) · AWAY modifier for $AFC
  Occasion weight: UCL knockout round x1.60 ·
    Source: fan-token/competition-calendar-framework.md
  NOTE: No rivalry tier applies (not a registered rivalry fixture) —
    UCL knockout occasion weight only · no derby modifier
  Regulatory: composite overlay independent per token ·
    UK Type D for $AFC holders ·
    Opponent's domestic jurisdiction for opponent holders ·
    Each token's regulatory overlay is independent (unlike shared
    Italian overlay in Example 1 — jurisdictions differ here)

TOKEN-SPECIFIC LAYERS (Steps 3 and 4):

  $AFC:
    CDI gate: CONSOLIDATION · full compound signal applies
    Form: winning run · positive modifier
    Trophy premium: verify via market/trophy-premium-framework.md ·
      apply if within active decay window · NOT APPLICABLE assumed
      for this example unless verified
    Fan base tier: Tier 1 · 35M+ global fans · UK domestic primary
    PATH_2 status: ACTIVE · confirmed FTP PATH_2 token
      WIN = burn event · LOSS = mint event · DRAW = no event
    H2H vs this opponent: verify current — apply h2h-framework.md gate
    Compound stack: POSITIVE · HIGH confidence (away leg noted ·
      venue modifier reduces but positive form + CDI maintain output) ·
      CAPITULATION x0.70 applied
    Occasion weight x1.60 applied to discounted result
    PATH_2: report separately — not included in demand stack

  OPPONENT TOKEN:
    CDI gate: CONSOLIDATION · full compound signal applies
    Form: mixed · neutral modifier
    Trophy premium: verify via market/trophy-premium-framework.md
    Fan base tier: verify via market/fan-base-intelligence.md
    PATH_2 status: NOT APPLICABLE — no confirmed supply event
    H2H vs $AFC: verify current
    Compound stack: NEUTRAL to DIRECTIONAL POSITIVE (home advantage ·
      mixed form · CAPITULATION x0.70 applied)
    Occasion weight x1.60 applied to discounted result
    NO SUPPLY EVENT — confirmed absent

RELATIONSHIP TYPE: ASYMMETRIC
  Sub-type: FORM ASYMMETRY + SUPPLY EVENT ASYMMETRY
  No CDI asymmetry (both CONSOLIDATION)
  $AFC stronger compound position (winning form) vs opponent neutral
  Supply event: $AFC PATH_2 ACTIVE · opponent no supply event
  Regulatory: different jurisdictions — no shared friction overlay
    (unlike Example 1 — important distinction)

FULL OUTPUT BLOCK:
  DUAL-TOKEN FIXTURE: UCL Round of 16 · $AFC vs [opponent token]
  RIVALRY TIER: NOT APPLICABLE — UCL knockout · no rivalry registration
  RELATIONSHIP TYPE: ASYMMETRIC (form asymmetry · supply event asymmetry)
  MACRO REGIME: CAPITULATION x0.70 · applied to both confirmed
  VENUE: AWAY (opponent ground) · AWAY modifier applied to $AFC
  REGULATORY: INDEPENDENT per token · UK Type D ($AFC) ·
    [Opponent jurisdiction] (opponent token) · no shared overlay

  TOKEN A — $AFC:
    CDI gate: CONSOLIDATION
    Form: winning run · positive
    Trophy premium: NOT APPLICABLE (assumed — verify)
    Fan base tier: Tier 1 · 35M+ · UK primary · MARC from Q4 2027
    H2H: verify current
    Compound signal: POSITIVE · HIGH confidence (pre-CAPITULATION) ·
      MEDIUM-HIGH post-CAPITULATION x0.70 discount
    Occasion weight x1.60 applied to discounted result
    Supply event: PATH_2 ACTIVE — WIN burns · LOSS mints · DRAW no event
      (report separately — not in demand stack)

  TOKEN B — [OPPONENT]:
    CDI gate: CONSOLIDATION
    Form: mixed · neutral
    Trophy premium: verify · apply if active
    Fan base tier: verify · apply as context
    H2H: verify current
    Compound signal: NEUTRAL to DIRECTIONAL POSITIVE · MEDIUM confidence
    Occasion weight x1.60 applied to discounted result
    Supply event: NOT APPLICABLE — no confirmed supply event

  DUAL-TOKEN RELATIONSHIP:
    Type: ASYMMETRIC
    $AFC stronger compound position (form + home ground advantage
    reversed — opponent home) · no CDI asymmetry ·
    Form asymmetry: $AFC positive vs opponent neutral ·
    Supply event asymmetry: $AFC PATH_2 ACTIVE ·
    opponent not affected by $AFC PATH_2 in any way ·
    Regulatory asymmetry: different jurisdictions — no shared friction

  SUPPLY EVENTS:
    $AFC PATH_2: ACTIVE — WIN burns · LOSS mints · DRAW = no event
    OPPONENT TOKEN: NO SUPPLY EVENT — not applicable

  NOTE: Compound signals are demand modifiers — not outcome predictors.
  PATH_2 NOTE: $AFC supply event fires on result — not a demand input.
  Opponent demand signal is entirely independent of $AFC PATH_2.
  DUAL-TOKEN DYNAMICS: UNCALIBRATED — initial structural framework (v4.5.28)

---

SECTION 9 — Agent Rules

10 rules. Never skip.

RULE 1 — LOAD THIS FILE FIRST:
  Any fixture with two confirmed active Chiliz fan tokens =
  dual-token fixture. Load this file before starting any analysis.
  Do not begin compound analysis without identifying dual-token status.

RULE 2 — VERIFY BOTH TOKENS BEFORE PROCEEDING:
  Confirm active token status for both clubs via complete-registry.md.
  Black logo = do not proceed without verification.
  One inactive token = single-token analysis only.

RULE 3 — SHARE MACRO AND VENUE:
  Macro regime and venue are shared layers. Load once.
  Do not load or apply them independently for each token —
  that creates inconsistency in the shared context.

RULE 4 — TOKEN-SPECIFIC LAYERS ARE INDEPENDENT:
  CDI · form · H2H · trophy premium · fan base tier · supply events
  are independent per token. Never transfer modifiers between tokens.
  Each token's stack is built from its own intelligence files.

RULE 5 — IDENTIFY RELATIONSHIP TYPE BEFORE OUTPUTTING:
  Classification as ALIGNED / ASYMMETRIC / CONFLICTED / INDETERMINATE
  is mandatory before producing any output. The relationship type
  is the core intelligence of a dual-token analysis.

RULE 6 — TRANSITION CAP IS UNCONDITIONAL:
  TRANSITION gate enforces directional-only output regardless of
  occasion weight tier, rivalry prestige, or opponent strength.
  A TRANSITION token in a UCL Final produces directional only.
  A TRANSITION token in a Tier 1 derby produces directional only.
  No exception.

RULE 7 — OCCASION WEIGHT APPLIES TO BOTH:
  Rivalry weight and competition tier weight are fixture-level
  modifiers. Apply to both tokens' compound results.
  CDI asymmetry does not exempt the lower-confidence token from
  receiving the occasion weight — it multiplies a directional result.

RULE 8 — SUPPLY EVENTS ARE STRICTLY TOKEN-SPECIFIC:
  PATH_2 applies to $AFC only. PTG applies to confirmed national
  tokens only. Never apply supply event mechanics across tokens.
  Never imply the opponent is affected by one token's supply event.
  Always report supply event status for both tokens — even when
  neither token has a supply event active.

RULE 9 — USE MANDATORY OUTPUT FORMAT:
  Section 6 output format is required for every dual-token fixture.
  Single-token output format is insufficient. All fields mandatory.
  Relationship type field is never optional.

RULE 10 — UNCALIBRATED FLAG:
  Dual-token relationship type classifications and interaction effects
  are initial structural reasoning — uncalibrated.
  State in every output: DUAL-TOKEN DYNAMICS: UNCALIBRATED —
  initial structural framework.
  Remove flag when calibration pass completed (target: 5+ verified
  records per relationship type).

---

OPEN QUESTIONS AND MONITORING FLAGS

CALIBRATION PASS — PLANNED:
  All dual-token interaction rules, relationship type classifications,
  and compound interaction effects are initial structural reasoning.
  Calibration pass planned when 5+ verified records per relationship
  type exist. Priority: ASYMMETRIC (most common) then ALIGNED
  then CONFLICTED. Bring to Strategy & Brainstorm before any changes.

CONSECUTIVE DUAL-TOKEN FIXTURE WINDOWS — MONITOR:
  When same two dual-token clubs meet multiple times in same season
  (UCL group stage + domestic league + cup), each fixture is a
  separate calibration record. Trophy premium and CDI gate should be
  checked for changes between fixtures — a club can move CDI gate
  mid-season. Never assume CDI gate is stable across a full season.

MULTI-TOKEN CIRCUIT — FUTURE:
  CIRCUIT products involving 3-5 tokens require an extension of
  this framework beyond two-token dynamics. Not yet scoped.
  Escalate to Strategy & Brainstorm when CIRCUIT products become
  active. Do not attempt to apply this two-token framework to
  three or more simultaneous tokens without a dedicated framework.

DORMANT TOKEN IN DUAL-TOKEN FIXTURE — MONITOR:
  If one token enters a DORMANT CDI gate mid-season and meets
  another active token, the fixture is treated as effectively
  single-token for signal purposes (DORMANT = no compound output).
  Update this file via Strategy & Brainstorm if this pattern
  occurs in a calibration record.

---

SOURCES AND VERIFICATION

PRIMARY SOURCES:
  fan-token/registry/complete-registry.md — token active status
  core/compound-signal-framework.md — single-token compound logic
  market/rivalry-intelligence.md — rivalry tier and occasion weight
  market/trophy-premium-framework.md — trophy premium per token
  market/fan-base-intelligence.md — fan base tier per token
  core/h2h-framework.md — H2H decay model per token
  core/contradiction-resolution-framework.md — conflict resolution
  fan-token/holder-tax-framework.md — regulatory overlays
  macro/regulatory/ — jurisdiction-specific files
  community/calibration-data/football/ — calibration records

CALIBRATION STATUS:
  UNCALIBRATED. All dual-token interaction rules, relationship type
  classifications, and compound interaction effects are initial
  structural reasoning. Calibration pass planned when 5+ verified
  records per relationship type exist. Do not treat any interaction
  rule as confirmed until calibrated.

LAST VERIFIED: 2026-08-18

---

MIND DIMENSIONS

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
| 15. Execution | 15a Entry Discipline · 15b Exit Discipline · 15d Playbook Adherence | ACTIVE |
| 16. Collaboration | 16a Task Delegation · 16b Context Handoff · 16c Output Coordination · 16d Conflict Arbitration | ACTIVE |

---

COMPATIBILITY

Compatible with: Claude · GPT-4 · Gemini · any LLM ·
sportmind_pre_match · sportmind_signal ·
core/compound-signal-framework.md ·
core/contradiction-resolution-framework.md ·
core/h2h-framework.md ·
core/venue-intelligence-framework.md ·
market/rivalry-intelligence.md ·
market/trophy-premium-framework.md ·
market/fan-base-intelligence.md ·
fan-token/holder-tax-framework.md ·
fan-token/registry/complete-registry.md ·
fan-token/competition-calendar-framework.md ·
fan-token/burn-to-glory-framework.md ·
market/club-intelligence/ (all CDI files) ·
macro/regulatory/ (all regulatory files) ·
community/calibration-data/football/

© 2026 SportMind
