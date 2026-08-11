---
name: fto-framework
description: >
  Fan Token Offering (FTO) mechanics framework. Documents FTO launch formats,
  wave structures, supply mechanics, loyalty bonuses, and jurisdiction exclusions.
  First documented two-wave FTO: $BELG (Royal Belgian Football Association, June 2026).
  Covers standard FTO, two-wave FTO format, supply scarcity signals, Locker Room
  loyalty bonus mechanics, and agent reasoning guidance for FTO period signals.
  All 16 Mind dimensions mapped.
---

# Fan Token Offering (FTO) Framework

**Enduring mechanics framework for Fan Token launch events.**

---

## What an FTO is

```
FTO — FAN TOKEN OFFERING:
  The initial public sale event through which a fan token enters
  secondary market circulation. Conducted via the Socios Locker Room
  platform (for Chiliz/Socios tokens).

  FTO IS NOT:
    Not a securities offering (see macro/regulatory/us-token-taxonomy.md —
    fan tokens classified as Digital Collectibles, not securities, under
    US federal law absent fractionalization).
    Not an Initial Coin Offering (ICO) in the traditional sense.
    Not a stake in the club.

  FTO IS:
    The mechanism by which a club's total fan token supply becomes
    available to the public for the first time.
    The price discovery event for the token's initial secondary market value.
    A demand signal moment — FTO participation volume indicates holder base size.
```

---

## Standard FTO format

```
STANDARD SINGLE-WAVE FTO:
  Access: Unlimited purchases per user
  Duration: Typically 24 hours
  Price: Fixed at issue price for duration
  Supply cap: Total token supply available

  AGENT SIGNALS DURING STANDARD FTO:
    HIGH participation volume: large holder base → positive CDI signal
    LOW participation volume: weak demand → apply DEMAND_UNCERTAINTY discount
    Supply fully subscribed: SUPPLY_PRESSURE_ACTIVE — secondary market pressure
```

---

## Two-wave FTO format

```
FIRST DOCUMENTED EXAMPLE: $BELG (Royal Belgian Football Association)
FTO DATE: 2026-06-03
Source: chiliz.com official — verified ✓

WAVE 1 — COMMUNITY ACCESS WINDOW:
  Cap:      Limited per user (e.g. 100 tokens per person maximum)
  Duration: Typically 6 hours
  Purpose:  Community distribution — prevents whale dominance at launch
  Access:   All eligible users on equal footing within the cap

WAVE 2 — OPEN MARKET ACCESS:
  Cap:      Unlimited purchases
  Duration: Remaining time (~18 hours)
  Purpose:  Open market access for any remaining supply
  Access:   First-come, first-served up to remaining supply

WHY TWO-WAVE FORMAT MATTERS FOR AGENT REASONING:

  COMMUNITY DISTRIBUTION SIGNAL:
    Wave 1 cap signals a partnership PRIORITISING COMMUNITY DISTRIBUTION
    over maximising initial sale revenue from large buyers.
    Historical pattern for comparable token structures: higher post-FTO
    holder retention and lower early sell pressure vs unlimited FTO.
    Apply: COMMUNITY_DISTRIBUTION_POSITIVE to post-FTO supply signal assessment.

  SELL PRESSURE REDUCTION:
    When no single buyer can dominate Wave 1, early concentrated selling
    from whales is structurally reduced.
    First 30-day sell pressure: LOWER than standard unlimited FTO (directional).
    Apply: EARLY_SELL_PRESSURE_REDUCED modifier to first-30-day secondary market signals.

  DEMAND ASSESSMENT DURING WAVE 1:
    If Wave 1 cap is reached early: STRONG_DEMAND_SIGNAL confirmed.
    If Wave 1 cap is NOT reached: monitor Wave 2 participation before concluding.
    Wave 1 undersubscription + Wave 2 strong = normal distribution — not weak demand.

  AGENT RULE:
    Do not assess FTO demand from Wave 1 alone in two-wave format.
    Assess total FTO participation across both waves combined.
```

---

## Supply scarcity — 2M vs 20M framework

```
STANDARD NATIONAL TEAM TOKEN SUPPLY: 20,000,000 tokens (typical)
$BELG SUPPLY: 20,000,000 tokens (STANDARD tier)
  NOTE: The FTO offered 2,000,000 tokens for initial distribution.
  Total max supply is 20,000,000 — same as typical national team tokens.

WHAT SUPPLY SCARCITY MEANS FOR SIGNALS:

  PRICE SENSITIVITY:
    Lower total supply = higher price sensitivity per unit of demand.
    The same demand volume moves price more dramatically vs high-supply tokens.
    Apply: SUPPLY_SCARCITY_AMPLIFIER to price movement signals for 2M supply tokens.
    Do NOT apply same price signals from 20M supply tokens to 2M supply tokens.

  HOLDER CONCENTRATION RISK:
    Lower supply = each holder represents a larger percentage of total supply.
    Even with Wave 1 cap: 100 tokens / 2,000,000 = 0.005% per holder.
    Concentration risk lower than unlimited FTO at same supply level.

  LIQUIDITY IMPLICATION:
    Lower float on secondary market = thinner order books (typically).
    Apply: THIN_LIQUIDITY_DISCOUNT to early secondary market depth signals.
    Resolve after 30+ days of secondary market trading data.

  SUPPLY SCARCITY TIERS (enduring reference):
    ULTRA_LOW:  < 5,000,000
    LOW:        5,000,000 — 12,000,000
    STANDARD:   12,000,000 — 25,000,000 (most national team tokens)
    HIGH:       > 25,000,000

  Apply appropriate modifier tier when comparing across tokens.
```

---

## Locker Room loyalty bonus

```
MECHANISM:
  Users who held qualifying stakes (e.g. Chiliz NFTs, CHZ, or qualifying tokens)
  at a designated snapshot date receive additional tokens as a loyalty bonus.

TYPICAL BONUS: 10% additional tokens above base FTO purchase
SNAPSHOT: Pre-announced date before FTO window opens

AGENT SIGNALS FROM LOYALTY BONUS:
  HOLDER_RETENTION_POSITIVE:
    Loyalty bonus rewards existing ecosystem participants.
    Structural incentive to hold qualifying assets ahead of new FTO launches.
    Each new FTO with loyalty bonus = demand signal for qualifying holding assets.

  SELL PRESSURE CONSIDERATION:
    Loyalty bonus recipients received tokens at effectively below-issue-price.
    Early sell pressure from loyalty recipients is possible — particularly if
    bonus tokens represent a meaningful % of total supply.
    For $BELG (20M total supply, 2M FTO tranche): 10% bonus = 200,000 additional
    tokens in circulation from loyalty recipients. Monitor secondary market for loyalty sell flow.

JURISDICTION EXCLUSION:
  UK users excluded from Locker Room loyalty bonus — regulatory compliance.
  This exclusion pattern may apply to other jurisdictions.

  AGENT RULE:
    Apply JURISDICTION_EXCLUSION monitoring to all future Locker Room FTOs.
    UK exclusion from loyalty bonus ≠ UK exclusion from token trading generally.
    UK users may still purchase on secondary market — exclusion is FTO-specific.
    Other jurisdictions (e.g. US) may have separate exclusion requirements.
    Always verify jurisdiction-specific access before applying holder base signals.
```

---

## FTO signal timing framework

```
PRE-FTO (PARTNERSHIP_ANNOUNCED → FTO_DATE):
  Signal type: DEMAND_ANTICIPATION
  Relevant signals: partnership announcement sentiment, prior comparable FTOs
  Apply: standard anticipation window (typically 7-14 days for national teams)

FTO WINDOW (Wave 1 + Wave 2):
  Signal type: DEMAND_CONFIRMATION or DEMAND_DISAPPOINTMENT
  Watch: Wave 1 sell-through speed (if two-wave format)
  Watch: Total participation volume vs comparable tokens
  Do not: apply secondary market price signals during FTO window
    (price is fixed at issue price during FTO)

POST-FTO DAY 1-7:
  Signal type: INITIAL_SECONDARY_MARKET
  Apply: THIN_LIQUIDITY_DISCOUNT — order book depth establishing
  Watch: First secondary market price vs issue price

POST-FTO DAY 8-30:
  Signal type: MARKET_DISCOVERY
  Apply: NOVEL_TOKEN modifier (×0.90 confidence)
  Secondary market liquidity improving — signals becoming more reliable

POST-FTO DAY 30+:
  Signal type: STANDARD_FAN_TOKEN_FRAMEWORK
  Full signal stack applicable
  Remove NOVEL_TOKEN and THIN_LIQUIDITY_DISCOUNT modifiers
```

---

## MIND DIMENSIONS

**Intelligence:** FTO mechanics framework — standard single-wave vs two-wave format. Wave 1 cap signal (community distribution priority). Supply scarcity tiers (2M ultra-low vs 20M standard). Locker Room loyalty bonus mechanics. UK/jurisdiction exclusion pattern. FTO signal timing framework (pre-FTO through Day 30+).

**Reasoning:** Two-wave FTO requires combined-wave demand assessment — not Wave 1 alone. Supply scarcity amplifies price sensitivity non-linearly vs standard supply. Loyalty bonus creates two effects: holder retention positive + potential early sell pressure from bonus recipients. THIN_LIQUIDITY_DISCOUNT applies Day 1-7 post-FTO for all tokens regardless of FTO format.

**Context:** FTO is the initial public sale event — not a securities offering. First documented two-wave FTO: $BELG (2026-06-03). Context: $BELG total supply is 20M (STANDARD tier). FTO offered 2M tokens initially.
  FTO tranche size (2M of 20M) creates thinner initial float than full supply suggests. World Cup 2026 window (June 11-July 19) amplifies FTO demand for all national team tokens launched in this period.

**Memory:** Standard single-wave FTO is the historical baseline for all prior Chiliz/Socios token launches. Two-wave format first documented June 2026 ($BELG). No prior calibration data for two-wave FTO post-launch performance — apply NOVEL_FORMAT modifier to post-FTO signal predictions until 30+ days data available.

**Judgment:** Do not conflate FTO format with token quality — two-wave format signals community priority in distribution design, not inherently superior token fundamentals. Supply scarcity below 5M vs standard 20M is a structural difference requiring separate reasoning — do not apply comparable price benchmarks across supply tiers without adjustment.

**Attention:** Monitor: first 7 days of $BELG secondary market for calibration data on two-wave FTO post-launch pattern. Monitor: future Chiliz/Socios FTO announcements for two-wave format adoption — if it becomes standard, update this file as the baseline.

**Learning:** $BELG is the first calibration data point for two-wave FTO format. Post-FTO signals from $BELG (first 30+ days) will establish baseline for this format. Until calibrated: apply NOVEL_FORMAT ×0.90 confidence to two-wave FTO post-launch predictions. After 30+ days data: update confidence accordingly.

**Integration:** Integrates with fan-token/registry/complete-registry.md ($BELG entry), fan-token/world-cup-2026-intelligence/ (World Cup demand context), macro/regulatory/us-token-taxonomy.md (Digital Collectible classification), macro/regulatory/uae.md (UAE compliance for FTO distribution), fan-token/fan-token-partnership-intelligence/ (partnership lifecycle context).

**Communication:** Agent output for FTO period: "FTO format: [single-wave/two-wave]. Supply: [amount] ([tier]). Loyalty bonus: [yes/no, %]. Jurisdiction exclusions: [list]. Current phase: [pre-FTO/Wave 1/Wave 2/post-FTO day X]. Apply: [relevant modifiers for phase]."

**Calibration:** COMMUNITY_DISTRIBUTION_POSITIVE: directional signal (two-wave). Magnitude: TBD pending $BELG post-FTO calibration. SUPPLY_SCARCITY_AMPLIFIER: applies to ULTRA_LOW tier tokens (< 5M supply). $BELG is STANDARD tier (20M total supply) — scarcity amplifier does NOT apply to $BELG. EARLY_SELL_PRESSURE_REDUCED: directional (two-wave format). All directional until 30+ days post-FTO data available.

**Adaptation:** When $BELG post-FTO data (30+ days) available: calibrate COMMUNITY_DISTRIBUTION_POSITIVE magnitude. When second two-wave FTO launches: cross-compare with $BELG baseline. When two-wave becomes standard Chiliz/Socios format: update standard FTO section accordingly.

**Verification:** FTO data verification: chiliz.com official announcements (primary). Socios.com platform (secondary). fantokens.com newsroom (tertiary). On-chain: Chiliz Chain contract events confirm FTO participation volume. Do not use social media participation claims as primary FTO demand signal.

**Ethics:** FTO framework documented neutrally. Loyalty bonus exclusions (UK) reflect regulatory compliance — not discriminatory practice by SportMind. Agent output should note jurisdiction exclusions factually without editorial comment.

**Transparency:** Every FTO signal must state: format (single/two-wave), supply tier, current phase, applicable modifiers, and jurisdiction exclusion status. Do not apply post-Day-30 signal stack before Day 30+ confirmed. State NOVEL_FORMAT uncertainty during first calibration window.

**Execution:** Signal generation workflow, event playbooks, and structured output templates defined

**Collaboration:** Integrates with core reasoning frameworks, sport domain layer, athlete intelligence, and macro layer

---

## Compatibility

**Token registry:**          `fan-token/registry/complete-registry.md`
**World Cup demand:**        `fan-token/world-cup-2026-intelligence/`
**US classification:**       `macro/regulatory/us-token-taxonomy.md`
**Partnership lifecycle:**   `fan-token/fan-token-partnership-intelligence/`
**Locker Room framework:**   `fan-token/world-cup-2026-intelligence/world-cup-2026-intelligence.md`

---

*SportMind v4.4.6 · MIT License · sportmind.dev*
*First two-wave FTO documented: $BELG (Royal Belgian FA, 2026-06-03)*
*Source: chiliz.com official — verified ✓*
*All 16 Mind dimensions mapped.*
