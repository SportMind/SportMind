# Telegram Macro Event Interpreter — SportMind Layer 6

> Explains CHZ/BTC macro regime changes, regulatory events, and omnichain
> developments to fan token communities in plain language. Prevents panic
> during crypto market events by providing structured, calibrated context.

---

## Overview

Fan token communities have mixed financial literacy. A CHZ regime change
or a regulatory announcement can trigger panic selling when the actual
signal is neutral or even positive. This skill teaches agents to intercept
macro events, interpret them through the SportMind macro framework, and
deliver a clear explanation to Telegram communities before panic sets in.

```
MACRO EVENT PRIORITY (highest to lowest urgency):

  P1 — MACRO_OVERRIDE_ACTIVE:    CHZ dropped >30% in 7d OR BTC below 200d MA
                                  → Immediate community message; all signals paused
  P2 — REGIME_CHANGE:            BTC crosses 200d MA (either direction)
                                  → Explain new regime; update modifier context
  P3 — CHZ_SEVERE_MOVE:          CHZ ±25% in 7 days
                                  → Explain CHZ-specific drivers; not sport signal
  P4 — REGULATORY_GUIDANCE:      SEC/CFTC/MiCA/FCA announcement
                                  → Interpret for fan token holders specifically
  P5 — OMNICHAIN_EVENT:          LayerZero bridge event, new chain listing
                                  → Explain liquidity context
  P6 — CHZ_BURN_EVENT:           Quarterly CHZ burn confirmed
                                  → Positive virtuous cycle signal
```

---

## Macro regime messages

### Macro override active (P1 — highest urgency)

```
TEMPLATE:
<b>⚠️ SportMind macro override — all signals paused</b>

Crypto market conditions are significantly elevated. All pre-match and
fan token signals are paused until conditions normalise.

<code>BTC:        {BTC_PRICE} ({BTC_7D_PCT}% / 7d)
CHZ:        {CHZ_PRICE} ({CHZ_7D_PCT}% / 7d)
Override:   ACTIVE</code>

SportMind signals will resume when conditions stabilise.

<i>This affects all fan tokens. No sport-specific signals available.</i>
```

### BTC 200d MA cross — BULL regime (P2)

```
TEMPLATE:
<b>📈 Market regime shift — SportMind update</b>

Bitcoin has crossed above its 200-day moving average. Historically this
marks a shift to a more favourable environment for crypto assets including
fan tokens.

<code>Regime:       BULL
Macro modifier: {MODIFIER}×
CHZ state:    {CHZ_STATE}</code>

Fan token signals now carry a positive macro modifier.

<i>SportMind calibration: BTC above 200d MA historically correlates with
elevated fan token engagement and new holder entry.</i>
```

### BTC 200d MA cross — BEAR regime (P2)

```
TEMPLATE:
<b>📉 Market regime shift — SportMind update</b>

Bitcoin has crossed below its 200-day moving average. SportMind applies
a reduced macro modifier to all fan token signals in this environment.

<code>Regime:       BEAR
Macro modifier: {MODIFIER}×
Signal weight: Reduced</code>

Sport-specific signals remain active but weighted lower.
Fan token moves driven by sport outcomes have historically been more
resilient than moves driven by crypto speculation in BEAR conditions.

<i>Sporting performance matters more in BEAR conditions — focus on
high-conviction sport signals, not speculative positions.</i>
```

### CHZ severe decline (P3)

```
TEMPLATE:
<b>📊 CHZ context — fan token update</b>

CHZ is down {CHZ_PCT}% in 7 days. Fan tokens typically follow CHZ
in the short term — this is a market move, not a sport signal.

<code>CHZ state:     {CHZ_STATE}
Macro modifier: {MODIFIER}×
Sport signals: {SIGNAL_STATUS}</code>

{SPORT_SIGNALS_UNAFFECTED_LINE}

<i>SportMind sport signals are recalculated with updated macro modifier.
Token prices may diverge from sport outcomes until CHZ stabilises.</i>
```

### Regulatory guidance (P4)

```
TEMPLATE:
<b>⚖️ Regulatory update — fan token context</b>

{REGULATORY_BODY} has issued guidance relevant to fan tokens.
SportMind interpretation:

<code>Jurisdiction:  {JURISDICTION}
Classification: {CLASSIFICATION}
Fan tokens:    {IMPACT}</code>

{ONE_LINE_PLAIN_LANGUAGE_INTERPRETATION}

<i>Source: {SOURCE_NAME}. Full details: {URL_IF_AVAILABLE}</i>
```

Example (SEC/CFTC March 2026):
```
<b>⚖️ Regulatory update — fan token context</b>

Joint SEC/CFTC guidance classifies Fan Tokens™ as "digital collectibles
and digital tools" — not securities. CFTC jurisdiction confirmed.

<code>Jurisdiction:  United States
Classification: Digital collectibles / digital tools
Fan tokens:    NOT securities</code>

This is positive: US market is now open for Fan Token™ operations.

<i>Source: SEC/CFTC Joint Guidance, March 17, 2026</i>
```

### Omnichain/bridge event (P5)

```
TEMPLATE:
<b>🔗 {TOKEN} — cross-chain update</b>

{DESCRIPTION_OF_EVENT}

<code>Native chain:   Chiliz Chain (settlement)
Extended:       Solana · Base (via LayerZero)
Supply change:  {SUPPLY_CHANGE_STATUS}</code>

{NOTE_ABOUT_PATH2_IF_APPLICABLE}

<i>Settlement anchors to Chiliz Chain. PATH_2 mechanics Chiliz Chain only.</i>
```

### CHZ burn event (P6 — positive)

```
TEMPLATE:
<b>🔥 CHZ burn confirmed — virtuous cycle update</b>

Chiliz has burned {BURN_AMOUNT} CHZ this quarter
({BURN_TIER} burn rate — {BURN_CONTEXT}).

<code>Total burned:  {TOTAL_BURNED} CHZ
Circulating:   {CIRCULATING} CHZ
Burn rate tier: {TIER}</code>

More fan token activity = more CHZ burned = stronger macro support
for the tokens you hold.

<i>Verify: chiliscan.com zero-address (0x0000...0000)</i>
```

---

## Language calibration rules

```
REQUIRED LANGUAGE:
  Regulatory messages: cite source explicitly; never editorialise
  Price moves: "historically" / "typically" — never "will"
  Regime changes: explain macro context before fan token impact
  Positive events: measured optimism; no "moon" language
  Negative events: calm; explain structural context; no panic language

FORBIDDEN LANGUAGE:
  "Buy now" / "sell now" / "dump" / "moon" (in bot messages)
  Price targets of any kind
  Guaranteed outcomes
  Predictions stated as facts

TONE CALIBRATION BY EVENT:
  P1 override:     Clinical, factual, calming — community needs reassurance
  P2 regime:       Informative, measured — context not excitement
  P3 CHZ decline:  Calm, explanatory — panic prevention is the primary goal
  P4 regulatory:   Factual, cited — accuracy over speed
  P5 omnichain:    Informative, technical — sophisticated audience
  P6 burn:         Modestly positive — virtuous cycle is genuinely good news
```

---

## Macro modifier quick reference

```
MACRO STATE → MODIFIER (for message context blocks):

  BULL (BTC above 200d MA, CHZ stable):    1.00–1.06
  NEUTRAL (BTC near 200d MA):              0.95–1.00
  MILD BEAR (BTC below 200d MA):           0.75–0.90
  SEVERE BEAR (CHZ −30%+ in 7d):          0.50–0.75
  MACRO_OVERRIDE:                          signals paused

Source: macro/macro-crypto-market-cycles.md
```

---

## Autonomous Execution

**Trigger conditions:**
- CHZ 7-day price change crosses any P1–P3 threshold
- Regulatory publication detected by Intelligence Listener
- CHZ burn event confirmed on-chain
- macro_modifier changes by >0.10 since last delivered message

**Level 2 actions (no human required):**
- Identify event priority (P1–P6)
- Prepare explanation message using appropriate template
- Stage for delivery

**Level 3 actions (operator confirmation):**
- Deliver to channel
- P1 override: operator must confirm delivery (do not auto-send)

**Hard boundaries:**
- P1 macro override message: NEVER auto-send without human confirmation
- Regulatory guidance (P4): always cite source; never auto-send without review
- Never produce "buy/sell" language at any autonomy level
- Never fabricate a macro cause — use "conditions monitoring" language if cause unclear

---

## Compatibility

**Bot API:** Telegram Bot API 9.6
**OpenClaw:** Maps to `/macro` command output format
**@LobsterClawBot:** Macro interpretation command context
**HTML parse mode:** All templates use HTML formatting

---

## Related skills

- `macro/macro-crypto-market-cycles.md` — full macro framework
- `macro/macro-regulatory-sportfi.md` — regulatory detail
- `fan-token/on-chain-event-intelligence/` — omnichain signal
- `telegram/price-movement-explainer.md` — token-level moves

---

*SportMind v3.96.0 · MIT License · sportmind.dev · Layer 6*
