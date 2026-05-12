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

## The Library — Six Intelligence Layers

Load in order. Each layer builds on the last.

| Layer | Name | Domain | Directory |
|-------|------|---------|-----------|
| 1 | Sport Domain | 42 sports. Event playbooks, signal weights, risk variables, agent reasoning prompts. | `sports/` |
| 2 | Athlete Intelligence | Position modifier weights, squad depth reasoning, return from injury frameworks, fan token demand impact. | `athlete/` |
| 3 | Fan Token Commercial | FTP PATH_2 mechanics, lifecycle phases, gamified tokenomics, governance, social sentiment, portfolio correlation. | `fan-token/` |
| 4 | Market Intelligence | Commercial tier, fanbase depth, competition calendar, transfer window dynamics, demand curves. | `market/` |
| 5 | Macro Intelligence | Regulatory frameworks (UK, US, EU, APAC, MENA), crypto cycles, geopolitical context. | `macro/` |
| 6 | Deployment Intelligence | Telegram Managed Bots integration, prompts, configs, use case examples. | `core/` |

---

## What Makes SportMind Different

### FTP PATH_2 Mechanics
The official Chiliz Fan Token Play mechanic — documented in full. A WIN is not just a result. It is a permanent supply reduction event. A LOSS is a mint event. A DRAW produces no supply change.

The **1/400 pre-liquidation ratio** means the supply event magnitude is calculable before the match begins. No standard model captures this. SportMind does.

```
Arsenal WIN  → tokens burned permanently from circulation
Arsenal LOSS → tokens minted to treasury
DRAW         → no supply change

Pre-match liquidation pool = circulating supply ÷ 400
```

### Calibration Records
129 verified records across 21 sports. Submitted before real events. Outcomes confirmed. **Including the wrong ones.** This is what makes the 96% direction accuracy claim defensible rather than asserted.

### The Library Rule
Every file passes one test. Will this intelligence still be true and useful in six months? Named player injuries, current league standings, and live prices fail this test. Reasoning frameworks about how to think about those things pass it.

---

## Signal Output

When an agent loads SportMind and applies it to a real scenario:

```json
{
  "direction":           "HOME",
  "adjusted_score":      72.4,
  "sms":                 79,
  "recommended_action":  "ENTER",
  "composite_modifier":  1.10,

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

Direction · Adjusted score · Confidence · Recommended action · Composite modifier · Modifiers applied · Active flags.

---

## Use Cases

**Pre-match intelligence agent**
Loads SportMind layers, fetches live team news and referee appointment, applies reasoning frameworks, produces a structured pre-match signal before any fan token club match.

**Fan token supply event detector**
Monitors the pre-match liquidation window. Calculates the expected burn or mint pool from current circulating supply divided by 400. Alerts the holder before the supply event fires.

**Regulatory impact interpreter**
Receives a regulatory news signal. SportMind's macro layer tells the agent which tokens are affected, what the modifier implication is, and whether the signal is enduring or expiring.

**Telegram intelligence bot**
Developer forks the Telegram kit, loads a SportMind system prompt, deploys via Managed Bots. Bot delivers pre-match signals, monitors sentiment, interprets macro events.

**Weekly intelligence briefing**
An agent monitors public sources, applies SportMind's three-tier classification framework, delivers structured weekly briefings with analyst-level context and reasoning. SMI is the reference implementation — running live since May 2026.

**Fan token wallet agent**
Connects to Chiliz Chain, reads balances, tracks FTP PATH_2 supply events, executes wallet actions within guardrails. Macro gate active — no execution during risk-off periods.

**Calibration contributor**
Runs SportMind before a real match, submits a pre-match signal, records the outcome. The first 10 external contributors become **Founding Calibrators** — permanently credited in the library's history.

---

## The Possibilities Are Endless

The use cases above are examples — not limits.

SportMind is a reasoning primitive. The intelligence layers are a foundation. What gets built on top of them is limited only by the developer's imagination.

Any domain that intersects with sports, fan tokens, commercial intelligence, or competitive analysis is fair game. Any agent, any LLM, any application. The library is MIT licensed and zero dependency — it works with everything and restricts nothing.

SportMind is not a product with a defined feature set. It is an open intelligence layer that developers, researchers, and builders can take in any direction. The calibration records, reasoning frameworks, and modifiers are building blocks — not a ceiling.

The intelligence layers are not fixed either. SportMind is designed to grow and scale over time — building toward a complete Mind for Sports. New layers, new sports, new fan token mechanics, new regulatory frameworks, new modifiers. Every addition makes every agent that uses the library smarter. The goal is a complete, living intelligence layer for sports and everything connected to fan tokens — and that goal has no finish line.

---

## Who SportMind Is For

**AI agent developers** — building sports analysis tools, fan token trading assistants, match intelligence bots, or calibration systems. SportMind is the knowledge layer.

**Fan token holders and traders** — who want AI-powered reasoning about supply mechanics, demand signals, macro context, and match outcome probability.

**Sports analytics developers** — building prediction models or intelligence pipelines who need structured domain knowledge rather than generic sports data.

**Researchers and analysts** — who want a verifiable, calibrated foundation. Every calibration record is in the repository, submitted before the event, with the outcome recorded.

**Builders with new ideas** — SportMind is an open playground. If you see a use case not listed here — that is exactly the point. The intelligence layers are a foundation that grows over time. Build anything on top of it.

---

## SMI — The Reference Implementation

SMI is SportMind's own intelligent reporter — built on the intelligence agent repository and running in production since May 2026.

SMI monitors public sources continuously, classifies every signal against SportMind's three-tier framework, applies the Library Rule, and delivers structured weekly briefings every Monday morning with analyst-level context and reasoning. It fires immediate Tier 1 alerts when primary signals are detected.

SMI does not act autonomously. It researches, classifies, and presents. The human decides what enters the library.

The [intelligence agent repository](https://github.com/SportMind/intelligence-agent) is the forkable version — any developer can deploy their own instance.

---

## The SportMind Suite

Four repositories. All MIT licensed. All zero external dependencies.

| Repository | What it does | Link |
|------------|-------------|------|
| **SportMind/SportMind** | The core intelligence library | [sportmind.dev](https://sportmind.dev) |
| **telegram-ai-bot-starter-kit** | Deploy SportMind-powered Telegram bots in minutes | [sportmind.dev/suite/telegram](https://sportmind.dev/suite/telegram) |
| **fan-token-agentic-wallet-starter-kit** | Build AI agents that manage fan token positions on Chiliz Chain | [sportmind.dev/suite/wallet](https://sportmind.dev/suite/wallet) |
| **intelligence-agent** | The forkable intelligence briefing agent | [sportmind.dev/suite/intelligence-agent](https://sportmind.dev/suite/intelligence-agent) |

---

## Key Numbers

```
651   files in the library
432   markdown intelligence files
129   calibration records
96%   direction accuracy
21    sports calibrated
42    sports with domain coverage
6     intelligence layers
4     suite repositories
0     external dependencies
0     autonomous commits
```

---

## Quick Start

Load the relevant SportMind skill files as context for your agent. The agent applies the reasoning frameworks to live data it fetches independently.

```
# Clone the library
git clone https://github.com/SportMind/SportMind

# Load macro context first — always
# Then fan-token, sports, athlete in order

# Example system prompt addition:
# "Load core/smi-digest.md for current library state,
#  then macro/macro-regulatory-sportfi.md,
#  then fan-token/ftp-path2.md for supply mechanics."
```

Compatible with any LLM. Zero external dependencies. MIT licensed.

---

## Contribute

**Submit a calibration record** — Run SportMind before a real match. Submit the outcome. No coding required. Wrong predictions are as valuable as correct ones. First 10 external contributors become Founding Calibrators.

**Expand a stub sport** — 32 sports are stubs waiting for domain knowledge.

**Add a reasoning framework** — Any enduring intelligence that passes the Library Rule. See [CONTRIBUTING.md](CONTRIBUTING.md) before submitting.

---

## License

MIT. Free to use. Free to build on.

[sportmind.dev](https://sportmind.dev) · [github.com/SportMind/SportMind](https://github.com/SportMind/SportMind) · [MIT License](LICENSE)

> ⚠️ Beta — SportMind is in active development. Reasoning frameworks, modifiers, and calibration records are updated regularly.
