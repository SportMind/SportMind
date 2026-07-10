---
name: agent-failure-modes-fan-token
description: >
  Documents recurring failure patterns in AI agent reasoning about fan tokens.
  Eight structural failure modes where agents produce plausible-sounding but
  incorrect or misleading output. Used to calibrate confidence, flag weak
  inference, and prevent systematic errors in fan token signal production.
  Companion file to core/agent-failure-modes.md (general sports intelligence
  failure modes). Library Rule: PASSES — enduring reasoning architecture,
  not tied to any match, price, or season.
---

# Agent Failure Modes — Fan Token Intelligence

---

## Purpose

Documents recurring failure patterns in AI agent reasoning about fan tokens.
Used to calibrate confidence, flag weak inference, and prevent systematic errors.

These are not theoretical failures — they are structural patterns that emerge
whenever an agent applies general reasoning heuristics to fan token signals
without accounting for the specific mechanics of the Chiliz/Socios ecosystem.

Each failure mode includes: the pattern, why it occurs, and the prevention rule.

---

## Failure Mode 1 — Price-Signal Conflation

```
PATTERN:
  Agent treats token price movement as a direct signal of club performance
  or fan sentiment, ignoring macro crypto regime, liquidity conditions,
  and speculative flows unrelated to the underlying club.

WHY IT OCCURS:
  Price is the most visible fan token signal. Agents trained on financial
  instruments default to treating price as the primary information source.
  Fan token price is heavily influenced by CHZ macro regime, thin liquidity,
  and speculative flows — not just club or fan signal.

PREVENTION RULE:
  Before interpreting price movement as a CDI signal:
    1. Check CHZ macro regime (CAPITULATION/RECOVERY/EXPANSION)
    2. Check trading volume — low volume makes price directionally unreliable
    3. Separate ecosystem-wide movement from token-specific movement
    4. Only then assess club/fan signal component

  Price movement = CHZ macro + liquidity noise + ecosystem signal + club signal
  Never treat it as club signal alone.
  Reference: fan-token/agent-failure-modes-fan-token.md FM1
```

---

## Failure Mode 2 — Supply Event Misclassification

```
PATTERN:
  Agent misidentifies the type of supply event (burn vs lockup vs release
  vs mint) or assumes a supply event occurred without confirming the
  on-chain trigger condition was met (e.g. match result threshold,
  governance vote, tournament round).

WHY IT OCCURS:
  Multiple supply mechanics exist in the ecosystem simultaneously.
  CHZ buy-back burn, Fan Token Play treasury burn, FTP PATH_2 settlement,
  and Burn to Glory are four distinct mechanics with different triggers,
  sources, assets, and scopes. Conflating them produces incorrect supply signals.

PREVENTION RULE:
  Before applying any supply event signal:
    1. Identify WHICH mechanic is active (four-way burn distinction)
    2. Confirm the on-chain trigger condition was met
    3. Verify via chiliscan.com — never assume from match result alone
    4. Apply the correct signal for that specific mechanic

  Four-way burn distinction — never conflate:
    CHZ buy-back burn → CHZ asset, revenue-linked
    Fan Token Play treasury → club tokens, match result trigger
    FTP PATH_2 → $AFC only, 90-min settlement
    Burn to Glory → national tokens, tournament WIN only
  Reference: fan-token/burn-to-glory-framework.md, fan-token/fan-token-play.md
  Reference: fan-token/agent-failure-modes-fan-token.md FM2
```

---

## Failure Mode 3 — Temporal Decay Blindness

```
PATTERN:
  Agent applies intelligence from a previous cycle (transfer window, season,
  tournament) to the current context without flagging that the signal may
  be stale. Particularly acute for squad composition, managerial tenure,
  and club competition tier.

WHY IT OCCURS:
  Library files encode intelligence at a point in time. Squad composition,
  coaching succession, and competition tier change each cycle. An agent
  that loads a club intelligence file without checking its recency will
  apply outdated context to current signals.

PREVENTION RULE:
  Before applying any club intelligence file:
    1. Check the file version date and last-updated marker
    2. Flag any signal involving: squad composition, manager, competition tier
    3. Apply temporal decay modifier if signal is from previous cycle
    4. Note in output: "Squad intelligence as of [version] — verify for current cycle"

  Highest decay risk signals:
    Squad composition — changes each transfer window
    Managerial tenure — can change mid-season
    Competition tier — changes each season
    Tournament bracket position — changes each round
  Reference: fan-token/agent-failure-modes-fan-token.md FM3
```

---

## Failure Mode 4 — Sentiment Source Contamination

```
PATTERN:
  Agent weights social/community sentiment without distinguishing between
  organic fan signal, coordinated promotional activity, and speculative
  trader noise. Each has different CDI implications.

WHY IT OCCURS:
  All three signal types appear in the same channels (Twitter/X, Telegram,
  Discord) and are superficially indistinguishable without source analysis.
  Coordinated promotional campaigns and speculative trader activity can
  produce sentiment spikes that look identical to organic fan engagement.

PREVENTION RULE:
  Before applying any sentiment signal to CDI:
    1. Identify source type: fan community / official promo / trader channel
    2. Check timing: does spike coincide with official campaign or match event?
    3. Check account profiles: new accounts, coordinated posting = promotional flag
    4. Organic fan signal has different CDI weight than promotional signal

  Sentiment source hierarchy (CDI weight, highest to lowest):
    Organic fan community (verified accounts, long tenure): HIGH CDI weight
    Post-match reaction (time-correlated with result): MEDIUM CDI weight
    Official promotional campaign: LOW CDI weight (anticipated, not spontaneous)
    Speculative trader noise: NO CDI weight — separate signal entirely
  Reference: fan-token/agent-failure-modes-fan-token.md FM4
```

---

## Failure Mode 5 — Outcome Extrapolation

```
PATTERN:
  Agent extrapolates a single match result or short run of results into a
  structural CDI conclusion, ignoring sample size, opponent quality, and
  tournament context.

WHY IT OCCURS:
  Match results are the most salient recent signal. Agents over-index on
  recency without applying sample size discipline. A single win against
  a weak opponent in a low-occasion-weight match carries limited CDI signal.

PREVENTION RULE:
  Before drawing a CDI conclusion from match results:
    1. Apply occasion weight (×1.00 to ×2.00) — not all wins are equal
    2. Assess opponent quality — win against Tier C opponent ≠ Tier A signal
    3. Minimum sample size: 5 results before structural CDI conclusion
    4. Tournament context: group stage results have lower predictive value
       for knockout-round CDI than knockout results themselves

  Single result CDI signal scope:
    One result: short-term sentiment signal only, not structural CDI
    3-5 results: pattern emerging, flag uncertainty
    5+ results: structural CDI signal applicable
  Reference: fan-token/agent-failure-modes-fan-token.md FM5
```

---

## Failure Mode 6 — Regulatory Status Assumption

```
PATTERN:
  Agent assumes a fan token's regulatory status in a jurisdiction based on
  general crypto rules rather than the specific framework applicable to
  fan tokens (which may be classified differently under MiCA, FCA, or
  other regimes).

WHY IT OCCURS:
  General crypto regulatory frameworks (AML, securities law) do not always
  apply to fan tokens in the same way. Fan tokens may be classified as
  utility tokens (MiCA), qualifying cryptoassets (UK FCA), or have specific
  carve-outs. Applying general rules produces incorrect demand signal gates.

PREVENTION RULE:
  Before applying any regulatory gate to a fan token signal:
    1. Identify the specific jurisdiction(s) material to the signal
    2. Check the fan-token-specific classification in that jurisdiction
    3. Apply the binary gate (authorised/not authorised) per jurisdiction
    4. Never conflate EU MiCA status with UK FCA status — separate gates

  Key jurisdiction-specific files:
    EU: macro/regulatory/eu-mica.md
    UK: macro/regulatory/uk-cryptoasset-regime.md
    Global: macro/regulatory/global-regulatory-landscape.md
  Reference: fan-token/agent-failure-modes-fan-token.md FM6
```

---

## Failure Mode 7 — Cross-Token Signal Bleed

```
PATTERN:
  Agent allows signal from one fan token (e.g. high engagement, price spike)
  to imply analogous conditions for tokens in the same ecosystem without
  confirming the signal is token-specific rather than ecosystem-wide.

WHY IT OCCURS:
  Fan tokens share infrastructure (Chiliz Chain, Socios platform), CHZ macro
  regime, and sometimes promotional campaigns. An ecosystem-wide event
  (CHZ listing, platform promotion) can produce correlated signals across
  tokens that are mistaken for token-specific club signals.

PREVENTION RULE:
  Before treating any fan token signal as club-specific:
    1. Check whether CHZ or Socios platform had a news event at the same time
    2. Check whether other fan tokens show the same signal pattern
    3. If correlated across 3+ tokens simultaneously → ecosystem signal, not club signal
    4. Apply ecosystem-wide signals at macro layer, not CDI layer

  Separation rule:
    Token-specific signal: affects one token, not correlated with peers
    Ecosystem signal: affects multiple tokens simultaneously
    Never apply ecosystem signal as a CDI modifier for a specific club
  Reference: fan-token/agent-failure-modes-fan-token.md FM7
```

---

## Failure Mode 8 — Liquidity Illusion

```
PATTERN:
  Agent interprets low trading volume as bearish sentiment rather than
  recognising thin liquidity as a structural characteristic of most fan
  tokens, making price movements noisy and directionally unreliable at
  low volume.

WHY IT OCCURS:
  In liquid markets, low volume often signals weak conviction or bearish
  conditions. Fan tokens operate in structurally thin liquidity — low volume
  is the default state for most tokens outside high-demand fixture windows.
  Applying liquid-market heuristics to fan token volume produces false signals.

PREVENTION RULE:
  Before interpreting fan token volume as a sentiment signal:
    1. Establish baseline volume for that token (non-fixture-window average)
    2. Compare current volume against baseline, not against liquid market norms
    3. Low volume at baseline = structurally normal, not bearish signal
    4. Volume spike above baseline during fixture window = genuine demand signal
    5. Volume spike outside fixture window = flag for investigation (promo? news?)

  Volume signal reliability threshold:
    Below baseline: no signal — structural thinness, not sentiment
    At baseline: neutral — normal state
    2-5× baseline (fixture window): genuine demand signal
    2-5× baseline (non-fixture): investigate source before applying signal
  Reference: fan-token/agent-failure-modes-fan-token.md FM8
```

---

## Calibration Note

When SportMind detects a signal that touches any of the above failure modes,
output should include an explicit confidence flag and the relevant failure
mode reference before drawing a CDI conclusion.

```
OUTPUT FORMAT when failure mode detected:

  ⚠️ FAILURE MODE FLAG: [FM number] — [failure mode name]
  CONFIDENCE: REDUCED — [reason]
  CDI CONCLUSION: [conclusion with explicit uncertainty noted]

Example:
  ⚠️ FAILURE MODE FLAG: FM1 — Price-Signal Conflation
  CONFIDENCE: REDUCED — CHZ macro regime CAPITULATION active;
    price movement may reflect macro suppression not club signal
  CDI CONCLUSION: Demand signal present but suppressed by ×0.70
    macro modifier — do not interpret raw price as club sentiment
```

---

## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Eight structural failure patterns in fan token signal reasoning |
| Reasoning | ACTIVE | Prevention rules for each failure mode — structured reasoning correction |
| Context | ACTIVE | Fan token-specific context: CHZ regime, thin liquidity, ecosystem dynamics |
| Memory | ACTIVE | Failure patterns recognised from prior signal production — pattern library |
| Judgment | ACTIVE | When to apply failure mode flag vs proceed with standard confidence |
| Attention | ACTIVE | Eight specific attention triggers — one per failure mode |
| Communication | ACTIVE | Explicit failure mode flag format defined for output |
| Verification | ACTIVE | FM2 and FM6 both require on-chain and regulatory verification before signal |
| Learning | ACTIVE | Failure mode library grows as new patterns are identified from operations |
| Integration | ACTIVE | Integrates with core/agent-failure-modes.md, fan-token-play.md, regulatory files |
| Calibration | ACTIVE | Output confidence calibrated against failure mode presence |
| Adaptation | ACTIVE | Failure modes evolve as ecosystem mechanics and regulatory frameworks develop |
| Ethics | ACTIVE | Honest about limitations — never produce overconfident signal when FM detected |
| Transparency | ACTIVE | Failure mode flag always explicit in output — no hidden confidence reduction |

---

## Compatibility

**General failure modes:** `core/agent-failure-modes.md`
**Four-way burn distinction:** `fan-token/fan-token-play.md`
**Burn to Glory:** `fan-token/burn-to-glory-framework.md`
**Regulatory gates:** `macro/regulatory/global-regulatory-landscape.md`
**CHZ macro regime:** `macro/macro-crypto-market-cycles.md`
**Holder behaviour:** `fan-token/fan-holder-behaviour.md`

---

*SportMind v4.1.4 · MIT License · sportmind.dev*
*Eight structural failure modes for fan token signal reasoning.*
*All 14 Mind dimensions mapped.*
