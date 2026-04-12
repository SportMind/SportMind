# SportMind

**The open sports intelligence library for AI agents and developers.**

SportMind teaches AI agents how to reason about sports — not just react to data.
Load a skill, and your agent immediately understands the sport, the athlete,
the commercial landscape, and the external forces acting on both.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Sports](https://img.shields.io/badge/sports-42-blue)]()
[![Calibration](https://img.shields.io/badge/calibration-126%20records%20%7C%2096%25%20accuracy-green)]()
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
- That a crypto bear market can make a Champions League winning club's token fall in fiat terms
- That a liquidity pool with $80k TVL will absorb your signal's value in slippage before you execute

This contextual reasoning is currently rebuilt from scratch by every developer
in the space. **SportMind is the shared layer.**

---

## Five-minute quickstart

**Option A — Paste into any LLM (zero setup)**

```
1. Open Claude, GPT-4, or Gemini
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

## Five layers — one system

| Layer | Directory | What it teaches |
|---|---|---|
| **1 — Sport domain** | `sports/` (42 sports) | How each sport works; event playbooks; risk variables |
| **2 — Athlete intelligence** | `athlete/` (29 sports) | Who is playing; form; composite modifier (0.55-1.25×) |
| **3 — Fan token commercial** | `fan-token/` (40 skills) | On-chain signals; lifecycle; DeFi; governance |
| **4 — Market intelligence** | `market/` (42 docs) | Commercial tier; fanbase; competition calendar |
| **5 — Macro intelligence** | `macro/` (8 docs) | Crypto cycles; geopolitical; recession |

**Load order:** macro → market → sport domain → athlete → fan token → output schema

Use a named bundle: `ftier1-football` · `ftier1-cricket` · `prematch-mma` · `governance-brief`
→ `platform/skill-bundles.md` for all 14 bundles with token estimates.

---

## What the library contains

```
42 sport domains · 29 athlete intelligence skills · 40 fan token skills
42 market documents · 45 core frameworks · 11 agentic workflow patterns
11 application blueprints · 7 starter pack examples · 66 compressed summaries
22 agent prompts · 11 agentic workflow patterns · 126 calibration records (96% accuracy)
6 recalibration reports · 26 named metrics (HAS, NCSI, ATM, FLS, KIS, CDI...)
```

**Empirically validated:** 126 real match outcomes across 21 sports. 96% correct direction.
All 5 wrong predictions are European football draws — documented with root-cause analysis.
See `core/modifier-recalibration-v6.md`.

---

## Agent output format

```json
{
  "sportmind_score":   {"sms": 79, "sms_tier": "GOOD"},
  "signal":            {"adjusted_score": 72.4, "direction": "HOME",
                        "recommended_action": "ENTER"},
  "modifiers_applied": {"athlete_modifier": 1.10, "macro_modifier": 1.00,
                        "composite_modifier": 1.08},
  "flags":             {"lineup_unconfirmed": false,
                        "macro_override_active": false}
}
```

Full schema: `core/confidence-output-schema.md`

---

## MCP server

SportMind is available as an MCP tool server — connect any AI agent to the
full library without loading files manually.

```bash
# Clone and install
git clone https://github.com/SportMind/SportMind
pip install mcp aiohttp

# Run locally — stdio (Claude Desktop / Claude Code)
python scripts/sportmind_mcp.py

# Run remotely — HTTP/SSE (hosted agents)
python scripts/sportmind_mcp.py --http --port 3001
```

Ten tools: `sportmind_signal` · `sportmind_macro` · `sportmind_stack` ·
`sportmind_verify` · `sportmind_agent_status` · `sportmind_pre_match` ·
`sportmind_disciplinary` · `sportmind_fan_token_lookup` ·
`sportmind_sentiment_snapshot` · `sportmind_verifiable_source`

**→ Full deployment guide: [MCP-SERVER.md](MCP-SERVER.md)**

---

## Integration

**Data connections:** `platform/data-connector-templates.md` — copy-paste code for
lineup data, fan token TVL, and macro state (the three most important live data sources).

**Execution layer:** `platform/chiliz-agent-kit-integration.md` — SportMind intelligence
→ Chiliz Agent Kit → on-chain execution.

**MCP deployment:** `platform/sportmind-mcp-deployment.md` — live endpoint in 30 minutes.

**Compatible with:** Claude · GPT-4 · Gemini · LangChain · CrewAI · AutoGen ·
OpenAI Assistants · any LLM (skills are structured markdown, not API wrappers).

---

## The calibration record

126 records. 96% accuracy. Zero wrong-direction records outside European football draws.

All records are in `community/calibration-data/` — publicly verifiable. Includes all
5 wrong predictions with full root-cause analysis. Not cherry-picked.

Eight modifiers with zero wrong-direction records across their entire evidence base:
qualifying_delta (F1) · india_pakistan ×2.00 · morning_skate (NHL) · dew_factor (cricket) ·
taper_modifier (swimming) · raider_primacy (kabaddi) · goalkeeper_save_rate (handball) ·
superspeedway_specialist (NASCAR)

---

## Contributing

**The fastest contribution: one calibration record.** No coding required.
See **[FIRST-RECORD-CHALLENGE.md](FIRST-RECORD-CHALLENGE.md)**.

What the community needs most:
- Football calibration records (athlete_modifier: 25/50 threshold)
- Cricket dew_factor records (evening T20 matches)
- Records from any underrepresented sport (rowing, netball, kabaddi)

Full process: `community/calibration-data/CONTRIBUTING.md`
Recognition: `community/CONTRIBUTORS.md`

---

## License

MIT — free to use, modify, and redistribute for any purpose.

---

*WHO-USES-THIS.md → FIRST-RECORD-CHALLENGE.md → examples/starter-pack/*

*SportMind is an independent open-source project. Not affiliated with Chiliz,
Socios, or any sports data provider, though designed to complement them.*
