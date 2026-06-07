# SportMind — Open Sports Intelligence for AI Agents

> **A reasoning library. Not a data feed.**
> Every file teaches an agent how to think — not what is true right now.

⚠️ **Beta** — active development · MIT licensed · [sportmind.dev](https://sportmind.dev)

---

## What SportMind Is

SportMind is an open reasoning library for AI agents and developers. It teaches AI agents how to think about sports — the commercial, financial, and competitive intelligence the industry runs on.

It is not a data feed. It does not provide live scores, current prices, or real-time injury updates. It provides the **reasoning frameworks** that allow any AI agent to interpret that data intelligently when it arrives.

A human sports analyst does not need to look up what a weight miss means in MMA, or how dew affects spin bowling in an evening T20, or what a UCL Final means for a fan token holder. They already know — it is internalised knowledge. SportMind gives AI agents that same internalised knowledge.

---

## The One Principle

**Will this intelligence still be true and useful in six months?**

If yes — it belongs in the library.
If no — it does not.

This single test governs every file in SportMind. It is why the library does not decay — it accumulates enduring reasoning that gets more valuable over time, not less.

---

## The Library — Seven Intelligence Domains

SportMind is designed to grow and scale over time — building toward a complete Mind for Sports. The domains below are not fixed. New intelligence, new sports, new fan token mechanics, and new regulatory frameworks are added continuously. The goal has no finish line.

### Sport Domain — `sports/`
42 sports. Event playbooks, signal weights, risk variables, and agent reasoning prompts. Cricket dew factor. F1 qualifying delta. MMA weight miss signals. Rugby, combat sports, esports, motorsport. Referee and officiating intelligence. Venue and stadium intelligence. Weather and environmental modifiers. Tournament structures across World Cup, Euros, Copa America, AFCON, and Asian Cup. Psychological intelligence. Coaching and management frameworks. Historical pattern reasoning.

### Athlete Intelligence — `athlete/`
Position modifier weights by club identity. Squad depth reasoning. Injury type and return timeline frameworks. Coaching and management signals. Psychological patterns. Historical performance frameworks. Fan token demand impact by position and absence type.

### Fan Token Commercial — `fan-token/`
FTP PATH_2 mechanics in full — 1/400 pre-liquidation ratio, Model 1 and Model 2 documented, 75% stop-loss, credit burn system. Lifecycle phases 1–5e. Governance intelligence. Social sentiment frameworks. Portfolio correlation reasoning. National team tokens. Emerging sports pipeline. Ecosystem health intelligence with five-dimension maturity scoring.

### Market Intelligence — `market/`
Commercial tier, fanbase depth, competition calendar, transfer window dynamics. Broadcast and media intelligence. Seasonal and cyclical demand patterns. How marquee signings affect demand over 2–4 weeks. How departures produce asymmetric decay curves. How World Cup years affect national token demand cycles.

### Macro Intelligence — `macro/`
Regulatory frameworks across UK, US, EU, APAC, and MENA. CLARITY Act activity vs passive yield. MiCA. UAE VARA. Saudi M/121. Qatar QFC 2024. Bahrain CBB Vol 6. Japan FIEA. South Korea CGT and 5-minute reconciliation. Vietnam pilot. Crypto and digital asset intelligence. Institutional intelligence — sovereign wealth funds, private equity, venture capital. Exchange and listing intelligence. Government policy and national sports strategy frameworks.

### Blockchain and On-Chain Intelligence — `core/`
Wallet concentration as confidence weight modifier. On-chain transaction velocity signals. Bridge activity as pre-liquidation pool indicator. Smart contract upgrade and emergency pause modifiers (×0.75 HOLD trigger). Supply event on-chain verification. Holder behaviour pattern reasoning. Pre-liquidation monitoring T-12h to T-2h.

### Agent Reasoning Architecture — `core/`
Complete end-to-end reasoning chains for all common scenarios. Signal confidence framework with HOLD trigger conditions. Agent onboarding with mandatory file loading order. Fan token context bridge. Cross-layer conflict resolution hierarchy. Output format specification including confidence level and signal class.

---

## What Makes SportMind Different

### FTP PATH_2 Mechanics
The official Chiliz Fan Token Play mechanic — documented in full. A WIN is not just a result. It is a permanent supply reduction event. A LOSS is a mint event. A DRAW produces no supply change.

```
Arsenal WIN  → tokens burned permanently from circulation
Arsenal LOSS → tokens minted to treasury
DRAW         → no supply change
Pre-liquidation pool = circulating supply ÷ 400
```

### Calibration Records
129 verified records across 21 sports. Submitted before real events. Outcomes confirmed. Including the wrong ones. 96% direction accuracy — defensible because every record is in the repository.

### The Library Rule
Every file passes one test. Will this intelligence still be true and useful in six months? Named player injuries, current standings, and live prices fail this test. Reasoning frameworks about how to think about those things pass it.

---

## Signal Output

```json
{
  "direction":           "HOME",
  "adjusted_score":      72.4,
  "sms":                 79,
  "recommended_action":  "ENTER",
  "composite_modifier":  1.10,
  "confidence_level":    "HIGH",
  "signal_class":        "EXECUTION",
  "modifiers_applied": {
    "athlete_modifier":     1.10,
    "macro_modifier":       1.00,
    "venue_modifier":       1.05,
    "officiating_modifier": 1.02
  },
  "flags": {
    "lineup_unconfirmed":    false,
    "ftp_path2_active":      true,
    "supply_event_type":     "REDUCTION",
    "macro_override_active": false
  }
}
```

---

## Use Cases

**Pre-match intelligence agent** — Loads SportMind layers, fetches live team news and referee appointment, follows agent reasoning chains, produces a structured pre-match signal with confidence level.

**Fan token supply event detector** — Monitors the pre-match liquidation window. Calculates expected burn or mint pool from circulating supply divided by 400. Alerts the holder before the supply event fires.

**Regulatory impact interpreter** — Receives a regulatory news signal. SportMind's macro layer tells the agent which tokens are affected and what the modifier implication is.

**Telegram intelligence bot** — Developer forks the Telegram kit, loads a SportMind system prompt, deploys via Managed Bots. Bot delivers pre-match signals, monitors sentiment, and interprets macro events.

**Weekly intelligence briefing** — An agent monitors public sources, classifies signals, and delivers structured weekly briefings. SMI is the reference implementation — running live since May 2026.

**Fan token wallet agent** — Connects to Chiliz Chain, reads balances, tracks FTP PATH_2 supply events, executes wallet actions within guardrails. Macro gate and signal confidence threshold both enforced.

**Calibration contributor** — Runs SportMind before a real match, submits a pre-match signal, records the outcome. First 10 external contributors become **Founding Calibrators** — permanently credited in the library's history.

---

## The Possibilities Are Endless

The use cases above are examples — not limits.

SportMind is a reasoning primitive. The intelligence layers are a foundation. What gets built on top of them is limited only by the developer's imagination.

Any domain that intersects with sports, fan tokens, commercial intelligence, or competitive analysis is fair game. Any agent, any LLM, any application. The library is MIT licensed and zero dependency — it works with everything and restricts nothing.

The intelligence layers are not fixed either. SportMind is designed to grow and scale over time — building toward a complete Mind for Sports. New layers, new sports, new fan token mechanics, new regulatory frameworks, new modifiers. Every addition makes every agent that uses the library smarter. The goal is a complete, living intelligence layer for sports and everything connected to fan tokens — and that goal has no finish line.

---

## Who SportMind Is For

**AI agent developers** — building sports analysis tools, fan token trading assistants, match intelligence bots, or calibration systems.

**Fan token holders and traders** — who want AI-powered reasoning about supply mechanics, demand signals, macro context, and match outcome probability.

**Sports analytics developers** — building prediction models or intelligence pipelines who need structured domain knowledge rather than generic sports data.

**Researchers and analysts** — who want a verifiable, calibrated foundation. Every calibration record is in the repository, submitted before the event, with the outcome recorded.

**Builders with new ideas** — SportMind is an open playground. If you see a use case not listed here — that is exactly the point. The intelligence layers grow over time. Build anything on top of them.

---

## SMI — The Reference Implementation

SMI is SportMind's own intelligent reporter — running in production since May 2026. It monitors public sources continuously, classifies every signal against SportMind's three-tier framework, applies the Library Rule, and delivers structured weekly briefings with analyst-level context and reasoning. It fires immediate Tier 1 alerts when primary signals are detected.

SMI does not act autonomously. It researches, classifies, and presents. The human decides what enters the library.

The [intelligence agent repository](https://github.com/SportMind/intelligence-agent) is the forkable version.

---

## The SportMind Suite

| Repository | What it does | Link |
|------------|-------------|------|
| **SportMind/SportMind** | The core intelligence library | [sportmind.dev](https://sportmind.dev) |
| **telegram-ai-bot-starter-kit** | Deploy SportMind-powered Telegram bots | [sportmind.dev/suite/telegram](https://sportmind.dev/suite/telegram) |
| **fan-token-agentic-wallet-starter-kit** | Build fan token wallet agents on Chiliz Chain | [sportmind.dev/suite/wallet](https://sportmind.dev/suite/wallet) |
| **intelligence-agent** | Forkable intelligence briefing agent | [sportmind.dev/suite/intelligence-agent](https://sportmind.dev/suite/intelligence-agent) |

---

## Key Numbers

```
671   files in the library
452   markdown intelligence files  
129   calibration records
96%   direction accuracy
21    sports calibrated
42    sports with domain coverage
7     intelligence domains
4     suite repositories
0     external dependencies
0     autonomous commits
```

---

## Quick Start

```bash
git clone https://github.com/SportMind/SportMind

# Mandatory loading order:
# 1. core/smi-digest.md
# 2. macro/macro-regulatory-sportfi.md
# 3. fan-token/ftp-path2.md
# 4. sports/[sport].md
# 5. athlete/[club].md
# 6. core/agent-reasoning-chains.md
# 7. core/signal-confidence-framework.md
```

Compatible with any LLM. Zero external dependencies. MIT licensed.

---

## Contribute

Submit a calibration record. Expand a sport file. Add a reasoning framework that passes the Library Rule. See [CONTRIBUTING.md](CONTRIBUTING.md). First 10 external contributors become Founding Calibrators.

---

[sportmind.dev](https://sportmind.dev) · [github.com/SportMind/SportMind](https://github.com/SportMind/SportMind) · MIT License

> ⚠️ Beta — SportMind v4.0.0. Active development. Not financial advice.
