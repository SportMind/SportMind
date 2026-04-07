# SportMind — Purpose and Context

**A single-load context document. Any agent loading this file has the complete
picture of what SportMind is, what it does, and how to use it correctly.**

Load this at agent initialisation before any sport-specific skills. It takes
approximately 600 tokens and eliminates the need to load `WHO-WE-ARE.md`,
`core/autonomous-agent-framework.md` purpose sections, and `platform/integration-partners.md`
overview sections separately.

---

## What SportMind is

SportMind is the open intelligence library for the sports industry. It teaches
AI agents how to reason about sports — the full commercial, financial, competitive,
and fan engagement intelligence that clubs, athletes, broadcasters, developers,
and fans need to make better decisions.

It is not a data provider. It provides reasoning frameworks. It does not replace
FanTokenIntel, SportFi Kit, or any other application. It is the intelligence
layer that those applications reason from.

**The library provides:**
- 42 sport domain skills (Layer 1)
- 29 athlete intelligence skills (Layer 2)
- 36+ fan token commercial skills (Layer 3)
- 42 market intelligence documents (Layer 4)
- 8 macro intelligence documents (Layer 5)
- 24 core shared frameworks
- 16 platform integration documents
- 60 empirically validated calibration records across 14 sports
- 47 named metrics from HAS through FLS

---

## What any SportMind agent must always do

```
THE NON-NEGOTIABLE RULES:

RULE 1 — MACRO FIRST:
  Load and check macro state before any fan token signal analysis.
  macro_modifier < 0.75 = MACRO_OVERRIDE_ACTIVE — all token signals reduced reliability.
  Never skip this step. Never assume macro state without checking.

RULE 2 — LOADING ORDER:
  macro → market → sport domain → athlete → fan token → confidence schema
  This order is not arbitrary. Each layer contextualises the next.
  Loading athlete modifiers before domain context produces unreliable signals.

RULE 3 — INTELLIGENCE SEPARATION:
  This agent generates intelligence. It does not execute trades, submit
  governance votes, or make financial commitments. Application layers do that.
  This boundary is a safety principle, not a constraint to work around.

RULE 4 — CONFIDENCE HONESTY:
  SMS < 60 = PARTIAL intelligence. State this. Do not present partial analysis
  as complete. An SMS of 45 with honest uncertainty is more valuable than an
  SMS of 80 built on hidden assumptions.

RULE 5 — SPORT-SPECIFIC PRIMARY SIGNAL:
  Every sport has a different primary signal variable. Know yours.
  Football:   lineup confirmation at T-2h (who is actually playing?)
  Cricket:    FORMAT FIRST — T20/ODI/Test before anything else
  MMA:        WEIGH-IN FIRST — weight miss supersedes all other analysis
  F1:         qualifying delta (Saturday result predicts Sunday)
  NHL:        morning skate goaltender confirmation (T-8h window)
  NBA:        star player DNP-rest status before any other modifier
  Rugby:      kicker form (40-50% of points; most predictive individual variable)
  Tennis:     surface win% for this specific surface before H2H
  Athletics:  PB proximity (how close to personal best = form indicator)
```

---

## The ecosystem SportMind operates within

```
SportMind is the intelligence layer. It sits between data and applications.

DATA LAYER (SportMind reads from):
  Chiliz Chain / KAYEN — fan token on-chain data
  Live sports APIs — match data, lineups, results (Sportradar, football-data.org)
  Crypto market data — BTC/CHZ prices (CoinGecko, KAYEN)
  Social data — sentiment signals, KOL activity

SPORTMIND INTELLIGENCE LAYER (this library):
  Reasoning frameworks → named metrics → calibrated modifiers → confidence output

APPLICATION LAYER (reads from SportMind):
  FanTokenIntel — sports intelligence application (primary partner)
  SportFi Kit — React/TypeScript fan engagement components + contracts
  Third-party applications — prediction markets, scouting tools, governance UIs
  LLMs — Claude, GPT-4, Gemini (reasoning engines that use SportMind as context)

EXECUTION LAYER (SportMind never touches):
  Chiliz Agent Kit — token trading, CHZ transfer, smart contract execution
  Wallet connections — Socios App, MetaMask, WalletConnect
  Smart contracts — governance, staking, token-gating
```

---

## The confidence output schema (always the final step)

```json
{
  "event_id":   "string",
  "sport":      "string",
  "generated_at": "ISO8601",

  "signal": {
    "direction":          "HOME | AWAY | DRAW | OVER | UNDER",
    "adjusted_score":     0.0,
    "confidence_tier":    "HIGH | MEDIUM | LOW | ABSTAIN",
    "recommended_action": "ENTER | REDUCE | WAIT | ABSTAIN",
    "position_size":      "100% | 65% | 50% | 0%"
  },

  "sportmind_score": {
    "sms":      0.0,
    "sms_tier": "HIGH_QUALITY | GOOD | PARTIAL | INCOMPLETE | INSUFFICIENT"
  },

  "modifiers": {
    "macro_modifier":    1.00,
    "composite":         1.00,
    "flags": {
      "lineup_unconfirmed":    false,
      "macro_override_active": false,
      "injury_warning":        false,
      "liquidity_warning":     false
    }
  },

  "freshness_warning": null
}
```

---

## The SportMind Score (SMS) — what it means

```
SMS = (Layer_Coverage × 0.35) + (Data_Freshness × 0.25)
    + (Flag_Health × 0.25) + (Modifier_Confidence × 0.15)

SMS TIERS:
  80-100: HIGH_QUALITY — act with standard position size
  60-79:  GOOD — act with moderate confidence; note any gaps
  40-59:  PARTIAL — advisory only; do not act autonomously at Level 2+
  20-39:  INCOMPLETE — provide partial intelligence; flag what is missing
  0-19:   INSUFFICIENT — do not provide signal; escalate or abstain

BLOCKING FLAGS (always reduce to WAIT regardless of SMS):
  macro_override_active = True → WAIT (crypto market conditions unfavourable)
  liquidity_critical = True → WAIT (insufficient pool depth for entry)
  lineup_unconfirmed at T-0 → WAIT or 50% size only
  governance_theatre = True → do not act on governance signal
```

---

## Autonomy levels (for agent deployments)

```
Level 0 (Supervised):    Human approves every output
Level 1 (Advisory):      Agent informs; human decides
Level 2 (Semi-autonomous): Acts at SMS ≥ threshold; escalates outside boundary
Level 3 (Autonomous/review): Acts immediately; human reviews log
Level 4 (Fully autonomous): Operates within hard technical boundaries

HARD LIMIT (ALL LEVELS):
  Financial execution → never autonomous (always Level 0-1 regardless of SMS)
  Governance votes → never autonomous (always Level 0-1)
  These are permanent limits, not configuration options.
```

---

## Key document map

```
For domain knowledge:
  sports/{sport}/sport-domain-{sport}.md — competition rules, signals, modifiers

For athlete intelligence:
  athlete/{sport}/athlete-intel-{sport}.md — individual performance signals

For fan token commercial intelligence:
  fan-token/fan-token-lifecycle/ — where is this token in its commercial life?
  fan-token/defi-liquidity-intelligence/ — can the market support a position?

For macro and market context:
  macro/macro-overview.md — always load first
  market/market-{sport}.md — competition tier context

For agent operations:
  core/autonomous-agent-framework.md — full lifecycle, safety model, decision matrix
  core/breaking-news-intelligence.md — how to handle breaking news
  core/reasoning-patterns.md — six-step reasoning chain
  platform/freshness-strategy.md — keeping intelligence current
  platform/skill-bundles.md — pre-configured named stacks

For developers:
  examples/starter-pack/README.md — entry points by complexity level
  platform/chiliz-agent-kit-integration.md — connecting to Chiliz execution
  platform/sportmind-mcp-server.md — five MCP tool definitions
```

---

*This document: ~600 tokens. Loads the full purpose/context in one call.*
*MIT License · SportMind · sportmind.dev*
