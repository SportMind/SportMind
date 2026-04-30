# Telegram Price Movement Explainer — SportMind Layer 6

> Translates fan token price moves into plain-language Telegram messages.
> Maps the move to its structural cause using SportMind's five-layer intelligence
> stack. Prevents community confusion during volatile periods.

---

## Overview

Fan token price moves confuse communities when they happen without context.
A 12% drop on a match day is different from a 12% drop during a crypto crash.
This skill teaches agents to identify which of SportMind's five cause categories
explains the move and deliver that explanation in one or two clear sentences.

```
FIVE CAUSE CATEGORIES (in priority order):

  1. MACRO_DRIVEN       — CHZ/BTC price move causing correlated fan token move
  2. MATCH_RESULT       — Direct sporting outcome driving supply change (PATH_2)
  3. TRANSFER_NEWS      — Athlete availability or transfer signal
  4. SENTIMENT_SHIFT    — Community sentiment spike (Telegram/X activity)
  5. LIQUIDITY_EVENT    — Exchange listing, delisting, bridge inflow/outflow

  AGENT RULE: Always check macro state first.
  A 15% fan token drop during a 20% BTC drop is Category 1, not Category 2.
  Never attribute a move to sport before ruling out macro.
```

---

## Cause identification protocol

```
STEP 1 — MACRO CHECK:
  Load macro/macro-crypto-market-cycles.md
  Is CHZ price change > ±3% in same timeframe?
    YES → Category 1 (MACRO_DRIVEN) — use macro explanation template
    NO  → proceed to Step 2

STEP 2 — MATCH RESULT CHECK:
  Was there a recent match (within T+2h)?
    YES, and PATH_2 token: check for supply change (chiliscan.com)
      Confirmed burn → Category 2 (MATCH_RESULT / supply reduction)
      No burn → check for result impact without PATH_2
    YES, standard token → Category 2 (MATCH_RESULT / sentiment)
    NO → proceed to Step 3

STEP 3 — TRANSFER/ATHLETE CHECK:
  Any confirmed transfer news or injury in T-48h to T+2h window?
    YES → Category 3 (TRANSFER_NEWS)
    NO  → proceed to Step 4

STEP 4 — SENTIMENT CHECK:
  Is Telegram/X message volume >2× baseline?
    YES → Category 4 (SENTIMENT_SHIFT) — likely a coordinated or organic spike
    NO  → proceed to Step 5

STEP 5 — LIQUIDITY CHECK:
  New exchange listing, bridge inflow, or known whale activity?
    YES → Category 5 (LIQUIDITY_EVENT)
    NO  → UNKNOWN — acknowledge uncertainty; do not fabricate cause
```

---

## Message templates

### Category 1 — Macro driven

```
TEMPLATE:
<b>📊 {TOKEN} — market context</b>

The wider crypto market is moving. BTC is {BTC_DIRECTION} {BTC_PCT}%,
CHZ is {CHZ_DIRECTION} {CHZ_PCT}%. Fan tokens typically follow.

This move is not sport-specific. SportMind macro state: <code>{MACRO_STATE}</code>

<i>Sport signal unchanged. Macro modifier: {MACRO_MODIFIER}×</i>
```

### Category 2 — Match result (standard)

```
TEMPLATE:
<b>⚽ {TOKEN} — match signal</b>

{CLUB} {RESULT} {OPPONENT} {SCORE}. {TOKEN} is responding to the result.

SportMind signal:
<code>Post-match modifier: {MODIFIER}×
Direction:          {DIRECTION}
Decay window:       {DECAY_HOURS}h</code>
```

### Category 2 — Match result (PATH_2 burn)

```
TEMPLATE:
<b>🔥 {TOKEN} — PATH_2 supply event</b>

{CLUB} WIN confirmed. PATH_2 burn triggered.

<code>Supply reduction: ~{BURN_PCT}% circulating
CHZ echo:         burn confirmed on-chain
New supply:       {NEW_SUPPLY} {TOKEN}</code>

<i>Permanent reduction. Verify: chiliscan.com</i>
```

### Category 3 — Transfer/athlete news

```
TEMPLATE:
<b>📋 {TOKEN} — athlete news</b>

{ATHLETE} news is driving movement. SportMind ATM modifier applied.

<code>ATM impact:     {ATM_MODIFIER}×
Availability:   {STATUS}
Signal window:  {WINDOW}</code>

<i>Monitor for official confirmation before acting.</i>
```

### Category 4 — Sentiment shift

```
TEMPLATE:
<b>💬 {TOKEN} — community activity</b>

Elevated community activity detected. On-chain data has not yet confirmed
a directional signal.

<code>Community tier: {SENTIMENT_TIER}
HAS baseline:   {HAS}
CHI:            {CHI}/100</code>

<i>Wait for on-chain confirmation before treating as signal.</i>
```

### Category 5 — Liquidity event

```
TEMPLATE:
<b>💧 {TOKEN} — liquidity event</b>

A structural liquidity change is detected. {LIQUIDITY_EVENT_DESCRIPTION}.

<code>IPS impact:    {IPS_DELTA}
EDLI change:   {EDLI}
Lifecycle:     {LIFECYCLE_PHASE}</code>
```

### Unknown cause

```
TEMPLATE:
<b>📊 {TOKEN} — move in progress</b>

SportMind is monitoring this move. No confirmed cause identified yet.
Macro: {MACRO_STATE} · Sport signal: {SPORT_SIGNAL}

<i>Update in {NEXT_CHECK_MINUTES} minutes.</i>
```

---

## Calibration reference

```
TYPICAL MOVE MAGNITUDES (approximate, for context only):

  PATH_2 WIN (confirmed burn):         +8–18% peak, 6–24h decay
  Match WIN (no PATH_2):               +4–10% peak, 2–8h decay
  Match LOSS:                          −5–12%, 2–6h decay
  UCL Final WIN:                       +15–35%, 24–72h decay
  World Cup group stage WIN:           +10–25% (NCSI ×3.5 applied)
  Transfer confirmed (star arriving):  +6–15%
  Transfer confirmed (star departing): −8–25%
  CHZ −20% (macro):                    −12–20% fan token (correlated)
  New exchange listing:                +10–30% short-term
  Bridge inflow (Solana/Base):         +2–8% (post-omnichain baseline)

These are reference ranges from historical calibration data.
They are not guarantees. Use as context, not prediction.
```

---

## Message delivery rules

```
FREQUENCY LIMITS:
  Maximum 1 explanation message per 30-minute window per token
  Do not chain multiple explanation messages — one authoritative message
  Update message (Telegram edit) preferred over sending a new message

CONTENT RULES:
  Never include specific price targets
  Never use "will" or "guaranteed" — use "typically" or "historically"
  Always include macro state context if macro modifier ≠ 1.00
  Always identify the cause category at the start (emoji signal)

CHARACTER LIMITS:
  Standard explanation: 200–400 characters
  With code block: up to 600 characters
  Never exceed 1,024 characters (Telegram caption limit)
```

---

## Autonomous Execution

**Trigger conditions:**
- Token price change >5% in any 30-minute window
- On-chain burn event confirmed on chiliscan.com
- CHZ price change >8% (macro explanation needed)

**Level 2 actions (no human required):**
- Identify cause category using five-step protocol
- Prepare explanation message using appropriate template
- Log cause, magnitude, and template used

**Level 3 actions (operator confirmation for delivery):**
- Send explanation message to configured channel/group

**Hard boundaries:**
- Never produce price target or "buy/sell" recommendation
- Never send during macro_override_active state
- Never fabricate a cause — use "unknown" template if cause unclear
- EXIT signal: human confirmation always required

---

## Compatibility

**Bot API:** Telegram Bot API 9.6
**OpenClaw:** Maps to `/explain` command output format
**@LobsterClawBot:** Direct — price explanation command context document
**HTML parse mode:** All templates use HTML formatting

---

## Related skills

- `telegram/sentiment-monitor.md` — community sentiment context
- `telegram/macro-event-interpreter.md` — macro move explanations
- `fan-token/gamified-tokenomics-intelligence/` — PATH_2 mechanics
- `fan-token/on-chain-event-intelligence/` — on-chain verification

---

*SportMind v3.96.0 · MIT License · sportmind.dev · Layer 6*
