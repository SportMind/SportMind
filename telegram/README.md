# Telegram Intelligence Layer — SportMind Layer 6

> **Deployment Intelligence** — Structured markdown skills for agents that
> deliver SportMind outputs directly into Telegram communities. Layer 6 bridges
> the intelligence stack (Layers 1–5) and the Telegram platform.

---

## What this layer is

Layers 1–5 teach agents how to reason about sports. Layer 6 teaches agents how
to **deliver** that reasoning inside Telegram — the platform where most sports
fan token communities actually live.

The four skills in this layer map to the four most common Telegram bot use cases
in the SportMind ecosystem:

| Skill | What it does | Primary audience |
|---|---|---|
| `sentiment-monitor.md` | Tracks community sentiment shifts in fan token Telegram groups | Bot operators, analysts |
| `price-movement-explainer.md` | Explains token price moves in plain language | Community members |
| `pre-match-signal.md` | Delivers pre-match intelligence as Telegram-formatted messages | Pre-match agents |
| `macro-event-interpreter.md` | Explains CHZ/BTC regime changes and regulatory events | Holders during macro events |

---

## Compatibility

**Telegram Bot API 9.6** — all message formats, inline keyboards, and callback
handlers described in this layer are compatible with Bot API 9.6.

**@LobsterClawBot and OpenClaw**
This layer is designed to work within the OpenClaw managed bot ecosystem.
LobsterClawBot (`@LobsterClawBot`) is the reference Telegram interface for
SportMind intelligence delivery. Developers building on OpenClaw's managed bot
infrastructure can load any Layer 6 skill as a context document to their bot's
system prompt and receive structured, Telegram-ready output immediately.

```
OPENCLAW INTEGRATION:
  Load order:   Layer 5 macro → Layer 3 fan token → Layer 6 telegram
  Bot context:  Load this README + relevant skill file as system prompt context
  Output mode:  Skills produce Telegram-formatted messages (HTML parse mode)
  Managed Bots: Compatible with OpenClaw Bot API 9.6 endpoint

LOBSTERCLAWBOT COMPATIBILITY:
  @LobsterClawBot reads from Layer 6 skills directly.
  Pre-match signal skill maps to /signal command output format.
  Sentiment monitor skill maps to /sentiment command output.
  Price explainer maps to /explain command output.
  Macro interpreter maps to /macro command output.
```

**Standalone deployment:** Every skill in this layer also works independently
of LobsterClawBot and OpenClaw — any Telegram bot framework (python-telegram-bot,
Grammy, Telegraf, aiogram) can load these skills as agent context.

---

## Load order

Layer 6 is loaded **after** the relevant lower-layer skills:

```
FULL STACK (fan token Telegram bot):
  1. macro/macro-crypto-market-cycles.md       (Layer 5)
  2. fan-token/fan-token-lifecycle/             (Layer 3)
  3. fan-token/gamified-tokenomics-intelligence/ (Layer 3)
  4. telegram/[relevant skill].md               (Layer 6)

PRE-MATCH ONLY:
  1. sports/[sport]/sport-domain-[sport].md     (Layer 1)
  2. athlete/athlete-modifier-[sport].md        (Layer 2)
  3. telegram/pre-match-signal.md               (Layer 6)

MACRO EVENT ONLY:
  1. macro/macro-crypto-market-cycles.md        (Layer 5)
  2. macro/macro-regulatory-sportfi.md          (Layer 5)
  3. telegram/macro-event-interpreter.md        (Layer 6)
```

---

## What Layer 6 does not do

- Layer 6 does not make predictions. Predictions come from Layers 1–5.
- Layer 6 does not connect to the Telegram API. It produces formatted output
  strings that a bot runtime then sends.
- Layer 6 does not store state. Message history and user preferences are the
  bot runtime's responsibility.
- Layer 6 does not override hard boundaries from Layers 1–5. EXIT signals
  always require human confirmation regardless of delivery channel.

---

## Message format conventions

All Layer 6 skills produce output in **HTML parse mode** (Telegram default).
Bold: `<b>text</b>` · Italic: `<i>text</i>` · Code: `<code>text</code>`
Pre-formatted block: `<pre>text</pre>` · Inline URL: `<a href="url">text</a>`

Output length targets:
- Standard signal message: 200–350 characters (fits without truncation on mobile)
- Extended analysis: 350–600 characters (two mobile screens)
- Full briefing: up to 1,024 characters (Telegram caption limit)

---

## File index

```
telegram/
├── README.md                         This file — layer overview, compatibility
├── sentiment-monitor.md              Fan token community sentiment tracking
├── price-movement-explainer.md       Token price change plain-language explanation
├── pre-match-signal.md               Pre-match intelligence delivery format
├── macro-event-interpreter.md        CHZ/BTC macro event community explanation
└── examples/
    └── fan-token-trading-bot.md      Complete worked example: $AFC PATH_2 bot
```

---

*SportMind v3.96.0 · MIT License · sportmind.dev · Layer 6 — Deployment Intelligence*
