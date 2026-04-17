# What SportMind Is

**SportMind is the open intelligence library for the sports industry.**

It teaches AI agents how to reason about sports — not just match prediction,
but the full commercial, financial, competitive, and fan engagement intelligence
that clubs, athletes, broadcasters, brands, developers, and fans need to make
better decisions in a sports world that is increasingly tokenised, data-driven,
and AI-operated.

SportMind is open source. It is free to use, free to extend, and free to build on.

---

## The problem it solves

The sports industry generates enormous signal — match results, player performance,
fan engagement, transfer activity, broadcast deals, on-chain fan token markets,
social sentiment, injury news, manager appointments. The problem is not a lack of
data. The problem is that AI agents do not know how to reason about sports without
being taught the domain.

A general-purpose LLM asked to analyse a football match will produce generic output.
It does not know that a match where the losing team drops into a relegation zone worth
£170M is structurally different from a mid-table fixture. It does not know that a
cricket match in Mumbai on a humid evening will be affected by dew in the second
innings. It does not know that a fan token in Phase 2 of its lifecycle behaves
differently from one in Phase 4. It does not know that a MotoGP wet race is the
one context where hardware tier resets and the specialist wins.

SportMind teaches agents these things. Each skill file transfers domain knowledge
that would otherwise take years of domain experience to acquire — and that knowledge
becomes part of every agent that loads it.

---

## What the library contains (v3.74)

**575 files.** 83 version cycles since v3.0.

**Five intelligence layers:**
- **Layer 1 — Sport domain (42 sports):** How each sport works; competition structures;
  event playbooks; risk variables; the sport-specific primary signal variable that agents
  must check first (lineup confirmation for football, format for cricket, weigh-in for MMA,
  qualifying for F1, morning skate for NHL)
  
- **Layer 2 — Athlete intelligence (29 sports, all at GOOD or DEEP depth):**
  Individual performance models; form; availability; sport-specific modifier (0.55-1.25×);
  venue and conditions intelligence; championship vs circuit reliability
  
- **Layer 3 — Fan token commercial (40 skills):**
  Fan token lifecycle (Phase 1-5e); HAS, FTIS, NCSI, ATM, APS, AELS, CDI, FLS, KIS, RSF
  and 16 other named metrics; DeFi liquidity intelligence; RWA/SportFi framework; governance
  intelligence; KOL influence model; on-chain event intelligence; fan sentiment CDI model
  
- **Layer 4 — Market intelligence (42 documents):**
  Football leagues, cricket cycles, basketball markets, motorsport calendars; club operations;
  broadcaster intelligence; EuroLeague basketball; World Cup 2026 deep module
  
- **Layer 5 — Macro intelligence (8 documents):**
  Crypto market cycles; geopolitical risk; pandemic and public health; economic recession;
  regulatory frameworks (MiCA, VDA, CFTC)

**Core framework (35 files):** Reasoning patterns; autonomous agent framework; goal framework;
breaking news protocols; modifier recalibration reports; calibration framework; confidence output
schema; temporal awareness; context window management; security model; purpose and context

**Platform layer (21 files):** MCP server (45 tools across 8 servers); MCP deployment guide; Skills API;
skill bundles (14 named); data connector templates; Chiliz Agent Kit integration; freshness
strategy; real-time integration patterns

**Community infrastructure:** 126 empirically validated calibration records across 21 sports;
6 recalibration reports (v3-v6); CONTRIBUTING.md; CONTRIBUTORS.md; FIRST-RECORD-CHALLENGE.md;
community leaderboard

**Developer tooling:** 7 starter pack examples (⭐ to ⭐⭐⭐⭐⭐); 11 application blueprints;
12 agentic workflow patterns; 22 agent prompts organised by stakeholder type; 66 compressed
skill summaries; 5 CI/CD GitHub Actions workflows

**International reach:** 24 i18n skill files across 7 languages (AR, DE, ES, FR, HI, JA, PT)

---

## The calibration foundation

126 outcome records. 96% correct direction predictions across 21 sports.
All 5 wrong predictions are European football draws (zero new wrong records in last 46) — fully documented with root-cause
analysis and protocol responses in `core/modifier-recalibration-v5.md`.

Eight modifiers with zero wrong-direction records across their complete evidence base:
qualifying_delta (F1), india_pakistan ×2.00 (cricket), morning_skate (NHL), dew_factor (cricket),
taper_modifier (swimming), raider_primacy (kabaddi), goalkeeper_save_rate (handball),
superspeedway_specialist (NASCAR).

This is not a cherry-picked result. All 126 records are in `community/calibration-data/`
and publicly verifiable. The modifiers were expert-defined estimates in v3.0 and are now
empirically validated across multiple sports and competition levels.

---

## How it works

SportMind skills are structured markdown. They load into any LLM as context and give it
domain-specific reasoning capability that general training alone cannot provide.

**The loading order is non-negotiable:**
`macro → market → sport domain → athlete → fan token → output schema`

**The five rules every agent must follow:**
1. Check macro state first — always, without exception
2. Follow the loading order — each layer contextualises the next
3. Never execute — generate intelligence; applications act
4. State confidence honestly — SMS < 60 is PARTIAL; say so
5. Check the sport-specific primary signal — each sport has one variable that matters most

**The output is structured and consistent:**
Every SportMind analysis produces the same schema — direction, adjusted score, SMS,
recommended action, modifier breakdown, active flags. Any application layer that reads
SportMind output works across all 19 calibrated sports.

---

## Who is building with SportMind

**Fan token application developers** — agents that monitor Chiliz Chain tokens,
generate pre-match signals, and surface commercial opportunities for fan token holders

**Club commercial teams** — analysts using the APS, AELS, and LTUI frameworks
to evaluate transfers, partnerships, and fan token strategy

**Sports agents and athlete representatives** — building commercial briefs from
the athlete financial intelligence layer

**DeFi and prediction market builders** — integrating fan token signals with
on-chain execution via the Chiliz Agent Kit integration patterns

**Autonomous agent systems** — deploying the full agentic workflow suite for
continuous portfolio monitoring, league watching, transfer intelligence, and governance

**Researchers** — using the calibration pipeline to validate AI-assisted sports
intelligence claims against real outcomes

---

## Where SportMind fits in the ecosystem

```
DATA LAYER:
  Chiliz Chain / KAYEN (fan token on-chain data)
  Sports APIs (lineups, results, form — see platform/data-connector-templates.md)
  Crypto market data (macro state — CoinGecko / CMC)
  Social data (KOL signals, sentiment)

SPORTMIND INTELLIGENCE LAYER (this library):
  Reasoning frameworks → named metrics → calibrated modifiers → confidence output

APPLICATION LAYER:
  FanTokenIntel — primary intelligence application partner
  SportFi Kit — React/TypeScript fan engagement components + contracts
  Third-party applications — prediction markets, scouting, governance UIs

EXECUTION LAYER:
  Chiliz Agent Kit — CHZ transfer, fan token trading, governance execution
  Wallet connections — Socios App, MetaMask, WalletConnect
  Smart contracts — governance, staking, token-gating

SportMind generates intelligence. Applications read it. Execution layers act on it.
SportMind never touches the execution layer.
```

---

## Contributing

The calibration pipeline is how SportMind improves. Every outcome record submitted
by a practitioner who used SportMind before a real match moves a modifier one step
closer to its evidence threshold — the point where expert estimates become data-confirmed.

**Fastest path to contributing:**
See `FIRST-RECORD-CHALLENGE.md` — one calibration record, no coding required.

**What the community needs most:**
- Football calibration records (athlete_modifier: 25/50 threshold)
- Cricket dew_factor records (5/50 threshold)
- Any records from underrepresented sports (rowing, netball, kabaddi, handball, NASCAR)
- External records — all current records were submitted by the founding team

---

## The long-horizon vision

SportMind's aspiration is to be the sports intelligence layer that AI systems share —
the framework that developers do not rebuild from scratch, that clubs and athletes trust
for commercial decisions, that the sports industry relies on the way medicine relies
on clinical literature.

That requires three things working together: the quality of the framework (the library
itself), the breadth of the calibration (community records), and the depth of the
application ecosystem (developers building on top).

v3.67 has delivered a complete intelligence framework including Fan Token Play (Path 1/2), CHZ virtuous cycle intelligence, developer toolkit (templates, 22 agent prompts, 12 workflow patterns), benchmark framework (40 scenarios), and governance/scouting agents. World Cup 2026 module live.
breadth and application ecosystem depth. Neither of those happens without the community.

---

*MIT License · SportMind · sportmind.dev*
*Current version: 3.66.0 · Built by [Pele Roberts](https://github.com/peleroberts)*
