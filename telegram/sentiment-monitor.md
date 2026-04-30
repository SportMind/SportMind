# Telegram Sentiment Monitor — SportMind Layer 6

> Tracks community sentiment shifts in fan token Telegram groups and channels.
> Translates the CHI (Community Health Index) and HAS signals from Layer 3 into
> readable Telegram message formats with actionable interpretations.

---

## Overview

Fan token Telegram communities are the fastest-moving sentiment signal in the
SportMind stack. Conversations shift before on-chain data moves. This skill
teaches agents to monitor that shift, classify it, and deliver the interpretation
as a Telegram message.

```
SIGNAL PRIORITY ORDER:
  1. On-chain data (HAS, TVI)       — objective, 15-minute lag
  2. Telegram community activity    — subjective, near-real-time
  3. Twitter/X mindshare (AELS)     — broader, 1-4h lag

  Telegram community signal LEADS on-chain signal by 15–90 minutes
  during high-sentiment events (match day, major transfers, macro events).
  Use as a leading indicator, not confirmation.
```

---

## Sentiment classification framework

```
SENTIMENT TIERS (classify incoming message volume and tone):

  TIER S — SURGE (exceptional, act immediately):
    Indicators: message volume >5× baseline, price query flood,
                "moon" / "burn" / "PATH_2" mentions, screenshot sharing
    Duration:   typically 15–45 minutes post-trigger
    Trigger:    usually a match result, transfer announcement, or macro event
    Action:     Load full signal chain; prepare explanation message

  TIER A — POSITIVE (above baseline):
    Indicators: message volume 2–5× baseline, optimistic tone,
                holder count queries, "when pump" patterns absent
    Duration:   3–8 hours
    Trigger:    pre-match build-up, minor positive news
    Action:     Prepare pre-match signal if within T-24h; else HOLD

  TIER B — NEUTRAL (baseline):
    Indicators: normal message cadence, mix of topics,
                governance discussion, utility questions
    Duration:   default state between events
    Action:     Monitor only; no signal delivery needed

  TIER C — NEGATIVE (below baseline):
    Indicators: price complaint volume rising, FUD keywords,
                holder count declining queries, "wen utility" patterns
    Duration:   2–12 hours
    Trigger:    loss, macro dip, negative transfer news
    Action:     Prepare price explainer; load macro state first

  TIER D — PANIC (emergency, monitor closely):
    Indicators: sell signals, "dump" / "rug" keywords, mass exit queries,
                macro FUD, significant price queries
    Duration:   minutes to hours
    Trigger:    macro crash, large on-chain sell, major negative news
    Action:     Macro override check first; then explanation message;
                DO NOT produce signal until macro state confirmed
```

---

## Message templates

### Positive sentiment response

```
TEMPLATE — SURGE/POSITIVE:
Input:  Detected Tier S sentiment spike
Output:

<b>📈 Community pulse: {TOKEN}</b>

Activity surge detected. Community is tracking {EVENT}.

SportMind signal:
<code>Direction:  {DIRECTION}
Score:      {SCORE}/100
Modifier:   {MODIFIER}×</code>

<i>Signal generated T-{HOURS_TO_MATCH}h pre-match</i>
```

### Negative sentiment response

```
TEMPLATE — NEGATIVE/PANIC:
Input:  Detected Tier C/D sentiment
Output:

<b>📊 {TOKEN} context</b>

Current move: {PRICE_CHANGE_PCT}% in {TIMEFRAME}

SportMind context:
<code>Macro state:  {MACRO_STATE}
CHZ modifier: {MACRO_MODIFIER}×
Sport signal: {SPORT_SIGNAL}</code>

{EXPLANATION_LINE}

<i>No execution signal — macro confirmation pending</i>
```

---

## Keyword signal map

```
HIGH-SIGNAL KEYWORDS (positive):
  "burn" / "burned"     — PATH_2 awareness; positive for supply signal
  "WIN" / "goal"        — match awareness; pre-position or post-celebration
  "PATH_2" / "path 2"   — sophisticated holder; supply mechanics awareness
  "staking" / "DeFi"    — omnichain awareness; positive holder behaviour
  "governance" / "vote" — engaged holder; governance Tier A behaviour

HIGH-SIGNAL KEYWORDS (negative):
  "dump" / "dumping"    — immediate sentiment check; load macro state
  "rug" / "scam"        — Tier D; do not produce signal; monitor only
  "sell" / "exit"       — Tier C/D; price explainer may be appropriate
  "dead" / "abandoned"  — Tier D; load lifecycle phase; check Phase 4/5 markers
  "when utility"        — Phase 2→3 transition frustration; common in early tokens

NOISE KEYWORDS (do not elevate tier):
  "gm" / "gn" / "lfg"  — social noise; ignore for sentiment classification
  "fomo" / "yolo"       — speculative; does not modify signal
  memes / stickers       — community health indicator only; not sentiment signal
```

---

## CHI integration

```
COMMUNITY HEALTH INDEX (CHI) — TELEGRAM SIGNAL CORRELATION:

  CHI 80–100:  Healthy community; Telegram sentiment amplifies signal
               → Telegram surge = strong confirmation; use full modifier
  CHI 60–79:   Normal community; standard Telegram correlation
               → Telegram surge = moderate confirmation; standard modifier
  CHI 40–59:   Declining community; Telegram sentiment may be thin
               → Telegram surge may be noise; require on-chain confirmation
  CHI < 40:    Weak community; Telegram may not represent holder base
               → Ignore Telegram signal; rely on on-chain data only

Load: fan-token/fan-holder-profile-intelligence.md for CHI calculation
```

---

## Autonomous Execution

**Trigger conditions:**
- Message volume crosses Tier S threshold (5× baseline in 15-minute window)
- Keyword density crosses 3 high-signal keywords per 100 messages
- CHZ price move >5% concurrent with community surge

**Level 2 actions (no human required):**
- Log sentiment tier and timestamp
- Prepare explanation message (not yet sent)
- Check macro state and sport signal

**Level 3–4 actions (operator confirmation):**
- Send explanation message to channel
- Update signal dashboard if integrated

**Hard boundaries:**
- Never send a signal message during Tier D panic without macro confirmation
- Never reproduce individual user messages or personal data
- Never produce a SELL or EXIT message autonomously at any level
- Macro override active = no message delivery of any kind

**Escalation condition:**
Tier D + macro_override_active → immediate human notification required.

---

## Compatibility

**Bot API:** Telegram Bot API 9.6
**OpenClaw:** Compatible — maps to `/sentiment` command output
**@LobsterClawBot:** Direct integration — this skill is the context document
**Frameworks:** python-telegram-bot 20+, Grammy, Telegraf, aiogram 3+

---

## Related skills

- `telegram/price-movement-explainer.md` — for Tier C/D responses
- `fan-token/fan-holder-profile-intelligence.md` — CHI baseline
- `fan-token/fan-token-pulse/fan-token-pulse-on-chain-data.md` — HAS/TVI
- `core/media-intelligence.md` — broader social signal context

---

*SportMind v3.96.0 · MIT License · sportmind.dev · Layer 6*
