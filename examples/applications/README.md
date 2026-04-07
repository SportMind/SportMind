# SportMind Application Blueprints

**Six fully specified applications that developers can build using SportMind intelligence.**

Each blueprint defines: the application's purpose, the exact SportMind skill stack it uses,
the agent prompt template, platform integrations required, target users, and the core value
proposition that SportMind enables.

These are blueprints — not implementations. They show developers exactly what to build and
exactly which SportMind intelligence to use. The library provides the reasoning layer;
these blueprints show what that layer makes possible.

---

## The six applications

| # | Application | Primary use case | SportMind layers | Key integration |
|---|---|---|---|---|
| 1 | [Decentralised Sports Prediction Finance](#app-1) | Pre-match signal → on-chain market | L1–L5 + DeFi | Azuro |
| 2 | [Fan Token Portfolio Intelligence](#app-2) | Portfolio context for holders | L1 + L3 + L5 | Chiliz/Socios |
| 3 | [Athlete Commercial Intelligence Platform](#app-3) | Athlete valuation for agents/brands | L2 + L3 | FanTokenIntel |
| 4 | [Sports Brand Token Strategy Tool](#app-4) | Pre-launch due diligence for clubs | L3 + L4 + L5 | Chiliz |
| 5 | [World Cup 2026 Intelligence Dashboard](#app-5) | Live WC2026 signal and portfolio | L1 + L3 + L4 | FanTokenIntel |
| 6 | [Sports GameFi Intelligence Layer](#app-6) | On-chain fantasy sport with SMS | L1 + L2 + L3 | Azuro / chain |
| 7 | [SportFi Kit + SportMind Full Stack](#app-7) | Complete integration reference | All layers | SportFi Kit + Chiliz |

---

## Why these applications, why now

SportMind was built to solve a specific problem: every developer in the sports-adjacent
digital asset space rebuilds the same domain knowledge from scratch. Cricket's dew factor.
The MMA weigh-in signal. The CVC investment as a fan token catalyst. The macro override
when crypto bear markets disconnect token prices from sporting performance.

These six applications represent the categories where that problem is most acute — where
the absence of structured sports intelligence produces the worst outcomes for builders
and the worst experience for users.

**The intelligence already exists. These blueprints show how to use it.**

---

## Architecture principle across all six

Every application built on SportMind follows the same architectural separation:

```
SportMind           Intelligence layer — reasoning, context, signal interpretation
Data providers      Raw data layer — FanTokenIntel, Chiliz, live sources
Agent framework     Execution layer — Claude, GPT-4o, LangChain, CrewAI
On-chain protocol   Settlement layer — Azuro, Chiliz Chain, other chains
```

SportMind never touches execution. It reasons. The application decides what to do
with that reasoning, how to execute it, and how to settle on-chain. This separation
is fundamental — it means SportMind can be integrated into any application architecture
without changing what the library is.

---

## Application blueprints

*Each blueprint is in its own file in this directory.*

| File | Application |
|---|---|
| `app-01-defi-prediction-market.md` | Decentralised Sports Prediction Finance |
| `app-02-portfolio-intelligence.md` | Fan Token Portfolio Intelligence |
| `app-03-athlete-commercial.md` | Athlete Commercial Intelligence Platform |
| `app-04-brand-token-strategy.md` | Sports Brand Token Strategy Tool |
| `app-05-world-cup-dashboard.md` | World Cup 2026 Intelligence Dashboard |
| `app-06-gamefi-layer.md` | Sports GameFi Intelligence Layer |
| `app-07-sportfi-kit-integration.md` | SportFi Kit + SportMind Full-Stack Blueprint |

---

## Getting started

All six applications use the Skills API to load intelligence:

```python
import requests

BASE = "http://localhost:8080"  # or your hosted endpoint

# Load the intelligence stack for your application
stack = requests.get(
    f"{BASE}/stack?use_case=fan_token_tier1&sport=football"
).json()

# Check current macro state before any analysis
macro = requests.get(f"{BASE}/macro-state").json()
macro_modifier = macro["macro_state"]["crypto_cycle"]["macro_modifier"]
```

Start the Skills API: `python scripts/sportmind_api.py --serve --port 8080`

See `platform/skill-registry-api.md` for hosted endpoint documentation.

---

*MIT License · SportMind · sportmind.dev*
*These blueprints are provided as guidance for developers. They do not constitute
financial advice. Applications built on these blueprints should comply with all
applicable laws and regulations in their target markets.*
