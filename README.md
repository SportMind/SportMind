# SportMind

**The open sports intelligence library for AI agents and developers.**

SportMind teaches AI agents how to reason about sports — not just react to data.

> **SportMind is a reasoning library, not a data feed. Every file teaches an agent how to think — not what is true right now.**
Load a skill, and your agent immediately understands the sport, the athlete,
the commercial landscape, and the external forces acting on it.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-4.1.12-green)]()
[![Sports](https://img.shields.io/badge/sports-42-blue)]()
[![Calibration](https://img.shields.io/badge/calibration-137%20records%20%7C%2096%25%2B%20accuracy-green)]()
[![Fan Tokens™](https://img.shields.io/badge/fan%20tokens-85%20verified-orange)]()
[![Validator](https://img.shields.io/badge/validator-passing-green)]()

---

## Find your starting point in 60 seconds

→ **[WHO-USES-THIS.md](WHO-USES-THIS.md)** — Developer, agent builder, analyst, researcher,
or contributor? This maps you to exactly the files you need.

---

## What problem does this solve?

AI agents that analyse fan tokens, run prediction markets, or power sports GameFi
need more than raw data. They need context:

- That a weigh-in miss in MMA is categorically different from a team losing a regular season game
- That a cricket match on a Mumbai evening will be affected by dew in the second innings
- That a DAXA Investment Warning on a Korean exchange is a staged lifecycle event with
  a predictable intervention window — not a binary delisting signal
- That a new Binance listing aligned with a club's actual fanbase geography extends CDI
  durability; a misaligned listing does not
- That Galatasaray equity on Borsa Istanbul (GSRAY.IS) leads the GAL fan token by 24–72
  hours on commercial news — both instruments are pricing the same underlying entity
- That a liquidity pool with $80k TVL will absorb your signal's value in slippage before you execute

This contextual reasoning is currently rebuilt from scratch by every developer
in the space. **SportMind is the shared layer.**

---

## Five-minute quickstart

**Option A — Paste into any LLM (zero setup)**

```
1. Open Claude, GPT-4, Gemini, Groq, Mistral, or any LLM
2. Paste: contents of core/sportmind-purpose-and-context.md
3. Paste: contents of sports/football/sport-domain-football.md
4. Ask: "PSG vs Arsenal UCL tonight. PSG full squad. Arsenal striker injured.
         Using SportMind, generate a pre-match signal."
```

Working in under 3 minutes.

**Option B — Skills API**

```bash
python scripts/sportmind_api.py   # start local API

curl "http://localhost:8080/bundle/ftier1-football"   # named bundle
curl "http://localhost:8080/stack?sport=football&use_case=fan_token_tier1"
```

**Option C — Clone and run**

```bash
git clone https://github.com/SportMind/SportMind
pip install aiohttp --break-system-packages
python examples/starter-pack/01-simple-signal.py
```

---

## Six layers — one system

| Layer | Directory | What it teaches |
|---|---|---|
| **1 — Sport domain** | `sports/` (42 sports) | How each sport works; event playbooks; risk variables |
| **2 — Athlete intelligence** | `athlete/` (50 files) | Who is playing; form; composite modifier (0.55–1.25×) |
| **3 — Fan token commercial** | `fan-token/` (90 files) | Lifecycle; DeFi; governance; exchange intelligence; RWA |
| **4 — Market intelligence** | `market/` (51 files) | Commercial tier; fanbase; sports equity signals; competition calendar |
| **5 — Macro intelligence** | `macro/` (20 files) | Crypto cycles; regulatory (MiCA, SEC/CFTC); geopolitical |
| **6 — Deployment** | `core/` | Reasoning chains; agent frameworks; failure modes; MCP server |

**Load order:** macro → market → sport domain → athlete → fan token → output schema

Use a named bundle: `ftier1-football` · `ftier1-cricket` · `prematch-mma` · `governance-brief`
→ `platform/skill-bundles.md` for all 14 bundles with token estimates.

---

## What the library contains

```
760 files · 540 markdown skill files

Sport domain:      42 sports · event playbooks · risk variables · agent reasoning prompts
Athlete:           29 sports · form models · availability · composite modifier (0.55–1.25×)
Fan token:         85 verified tokens · Lifecycle phases 1–6 · DeFi liquidity · exchange intelligence
                   Fan Token Play PATH_2 · governance · KOL influence · FTO framework
                   Sports equity signals (GSRAY.IS, MANU, JUVE.MI, FWONK, TKO) · CHZ macro layer
Market:            51 documents · club operations · broadcaster intelligence · World Cup 2026
Macro:             20 documents · MiCA · SEC/CFTC joint guidance (March 2026) · CLARITY Act · KSA/UAE

Core frameworks:   reasoning patterns · autonomous agent framework · modifier system
                   seven-step reasoning chain · pre-match signal framework · athlete framework
Platform:          MCP server tools · data connectors · API providers · Chiliz Agent Kit
                   social intelligence · web agent connectors · fraud signals
Community:         137 calibration records (96%+ accuracy, 21 sports) · benchmarks
Developer tools:   application blueprints · agentic workflow patterns · agent prompts
                   copy-paste templates · compressed summaries · Skills API
```

---

## Agent output format

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

Full schema: `core/confidence-output-schema.md`

---

## MCP server

SportMind exposes its intelligence as MCP tools for Claude Desktop and any MCP-compatible AI agent.

**→ Standalone MCP server repository: [github.com/SportMind/mcp-server](https://github.com/SportMind/mcp-server)**

Confirmed working: 2026 UCL Final — all five layers loaded, SMS 100, pre-match signal produced 48 hours before kickoff. Direction CORRECT.

The server is also available embedded in the core library:

```bash
git clone https://github.com/SportMind/SportMind
pip install mcp aiohttp

# stdio (Claude Desktop / Claude Code)
python scripts/sportmind_mcp.py

# HTTP/SSE (hosted agents)
python scripts/sportmind_mcp.py --http --port 3001
```

Tools: `sportmind_pre_match` · `sportmind_signal` · `sportmind_macro` · `sportmind_stack` · `sportmind_fan_token_lookup` · `sportmind_sentiment_snapshot` · `sportmind_disciplinary` · `sportmind_verifiable_source` · `sportmind_verify` · `sportmind_agent_status`

**→ Standalone repo with full setup guide: [github.com/SportMind/mcp-server](https://github.com/SportMind/mcp-server)**
**→ Embedded deployment guide: [MCP-SERVER.md](MCP-SERVER.md)**

---

## Integration

**Data connections:** `platform/data-connector-templates.md` — lineup data, fan token TVL,
macro state.

**Execution layer:** `platform/chiliz-agent-kit-integration.md` — SportMind intelligence
→ Chiliz Agent Kit → on-chain execution.

**Web agents:** `platform/web-agent-connectors.md` — lineup confirmation (T-2h), PATH_2
supply verification, exchange monitoring, regulatory/macro monitoring.

**MCP deployment:** `platform/sportmind-mcp-deployment.md` — live endpoint in 30 minutes.

**Compatible with:** Claude · GPT-4 · Gemini · LangChain · CrewAI · AutoGen ·
any LLM (skills are structured markdown, not API wrappers).

---

## The calibration record

134 records. 96%+ accuracy. Zero wrong-direction records outside European football draws.

All records are in `community/calibration-data/` — publicly verifiable, pre-submitted
before real matches. Includes all wrong predictions with root-cause analysis.
Not cherry-picked.

The most recent verified series: **FIFA World Cup 2026** —
9 records across group stage, knockouts, and Final. 9/9 correct.
100% accuracy. Perfect record. Spain beat Argentina 1-0 AET in the
Final — SportMind signal: SPAIN (HOME). CORRECT.
See the full signal and outcome: [sportmind.dev/first-record/](https://sportmind.dev/first-record/)

Eight modifiers with zero wrong-direction records across their entire evidence base:
qualifying_delta (F1) · india_pakistan ×2.00 · morning_skate (NHL) · dew_factor (cricket) ·
taper_modifier (swimming) · raider_primacy (kabaddi) · goalkeeper_save_rate (handball) ·
superspeedway_specialist (NASCAR)

---

## Contributing

**The fastest contribution: one calibration record.** No coding required.
See **[FIRST-RECORD-CHALLENGE.md](FIRST-RECORD-CHALLENGE.md)**.

**Found a framework gap?**
See [CONTRIBUTING-GAPS.md](CONTRIBUTING-GAPS.md) for how to report missing intelligence frameworks.

What the community needs most:
- Football calibration records (athlete_modifier: 25/50 threshold)
- Cricket dew_factor records (evening T20 matches)
- Records from any underrepresented sport (rowing, netball, kabaddi)

Full process: `community/calibration-data/CONTRIBUTING.md`
Recognition: `community/CONTRIBUTORS.md`

---

## License

MIT — free to use, modify, and redistribute for any purpose.

## Privacy

SportMind does not collect or process personal data.

Some SportMind frameworks reason about holder behaviour and on-chain wallet
activity. Developers building applications that combine these frameworks with
identifying information may be processing personal data under GDPR, UK GDPR,
CCPA, or applicable local law.

See `core/privacy-notice.md` for a full developer privacy reference.

SportMind is MIT licensed. Developers are responsible for their own compliance
with data protection law when building on this library.

---

*WHO-USES-THIS.md → FIRST-RECORD-CHALLENGE.md → examples/starter-pack/*

*SportMind is an independent open-source project. Not affiliated with Chiliz,
Socios, or any sports data provider, though designed to complement them.*
