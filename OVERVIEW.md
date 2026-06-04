# SportMind — Open Sports Intelligence for AI Agents

**Version:** v3.97.99  
**License:** MIT  
**Website:** [sportmind.dev](https://sportmind.dev)  
**GitHub:** [github.com/SportMind/SportMind](https://github.com/SportMind/SportMind)

---

## What is SportMind?

SportMind is an open sports intelligence library for AI agents. It is not a data feed, a prediction service, or a betting tool. It is a **reasoning framework** — a structured collection of intelligence files that teach AI agents how to think about sports, fan tokens, athlete performance, market signals, and commercial dynamics.

SportMind gives AI agents the intelligence, reasoning, and context to understand sports — the commercial, financial, and competitive signals the industry runs on.

---

## Library at a Glance

| Metric | Value |
|--------|-------|
| Total files | 743 |
| Markdown skill files | 524 |
| Calibration records | 130 |
| Direction accuracy | 96%+ |
| Sports validated | 21 |
| Fan tokens in registry | 85 |
| Mind dimensions | 14 |
| License | MIT |

---

## Six Intelligence Layers

SportMind is organised into six layers. Load in order — macro → market → sport domain → athlete → fan token → core.

| Layer | Name | Contents | Directory |
|-------|------|----------|-----------|
| 1 | Sport domain | 42 sports, event playbooks, signal weights | `sports/` |
| 2 | Athlete intelligence | 29 sports, form, availability, composite modifiers | `athlete/` |
| 3 | Fan token commercial | FTP PATH_2, lifecycle, governance, RWA | `fan-token/` |
| 4 | Market intelligence | Commercial tier, fanbase depth, competition calendar | `market/` |
| 5 | Macro intelligence | Crypto cycles, MiCA, CLARITY Act, geopolitical | `macro/` |
| 6 | Core reasoning | 14 Mind dimensions, agent frameworks, calibration | `core/` |

---

## Fourteen Mind Dimensions

Every file in the SportMind library maps to one or more of the 14 Mind dimensions — a framework that describes how a complete reasoning system thinks.

**Foundation:** Intelligence · Reasoning · Context  
**Building toward:** Memory · Judgment · Attention · Communication · Verification  
**Not yet fully implemented:** Learning · Integration · Calibration · Adaptation · Ethics · Transparency

---

## Calibration Base

SportMind's accuracy claims are verifiable. 130 records submitted before real events and verified after outcomes. Including every incorrect record.

- **130** calibration records across 21 sports
- **96%+** direction accuracy (125 of 130 correct)
- **All records** stored in `calibration/` — open to audit
- **Record #130:** 2026 UCL Final — PSG vs Arsenal — direction CORRECT

### UCL Final 2026 — Record #130

The most significant calibration record in SportMind's history:

- **Pre-match signal:** PSG (Home) · Adjusted score 55 · Medium confidence · ENTER
- **Signal produced:** T-48h by SportMind MCP server · All five layers loaded · SMS 100
- **Result:** PSG win 4-3 on penalties (1-1 AET)
- **Direction:** CORRECT — SportMind predicted PSG, PSG won
- **FTP PATH_2:** $AFC LOSS → mint event · ~111,500 $AFC minted to treasury
- **Historical first:** First UCL Final with a live FTP supply event mechanism

---

## Fan Token Registry

85 verified fan tokens across Chiliz Chain, BNB Chain, Ethereum, and BITCI. The most comprehensive public fan token registry in existence.

**Registry includes:**
- Contract addresses (old 0-decimal, wrapped, and new 18-decimal)
- Partnership announcement dates and launch source URLs
- FTO dates and max token supply
- Partnership status and trading status
- FTP active dates and model type
- Omnichain status and first omnichain date
- Blockchain network and sport category

**FTP PATH_2 confirmed:** $AFC Arsenal only (Model 2 — April 7 2026)  
**Omnichain confirmed:** $AFC, $PSG, $BAR, $CITY, $JUV (Chiliz Chain + Solana + Base)

---

## Regulatory Intelligence

SportMind covers the four most commercially significant regulatory environments for fan tokens:

| Jurisdiction | Framework | Status | Fan Token Classification |
|---|---|---|---|
| USA | SEC/CFTC Joint Taxonomy | ACTIVE March 2026 | Digital collectibles — NOT securities |
| EU | MiCA | ENFORCEMENT June 30 2026 | Crypto-assets — whitepaper required |
| UAE | CMA/VARA Unified Framework | ACTIVE Q1 2026 | Utility tokens — VASP licence required |
| KSA | Unified Sports Law 2026 | ACTIVE June 10 2026 | TRANSITIONING — monitor for Chiliz/SPL signals |

**US milestone:** Fan tokens explicitly named as digital collectibles in the joint SEC/CFTC interpretive release — the first federal classification of fan tokens in US history.

---

## Fan Token Play (FTP)

Three distinct mechanisms — must never be conflated:

| Mechanism | Triggered by | Effect | Cadence |
|---|---|---|---|
| FTP Model 1 | Match result WIN | Fan Token burned from treasury | Per match |
| FTP Model 2 PATH_2 | Match result | WIN = buyback/burn · LOSS = mint | Per match |
| CHZ Ecosystem Burn | Fan Token volume | CHZ bought and burned | Monthly |

**LOSS = MINT EVENT in PATH_2** — supply increases on a loss. Not supply neutral.

**Verified UCL Final outcome (May 30 2026):** Arsenal LOSS → ~111,500 $AFC minted to treasury

---

## MCP Server

SportMind exposes its intelligence as MCP tools for Claude Desktop and other AI agents.

```bash
git clone https://github.com/SportMind/SportMind.git
pip install mcp aiohttp
# Add sportmind_mcp.py to claude_desktop_config.json
```

**Confirmed working:** UCL Final 2026 · Five parallel tool calls · SMS 100 · All five layers loaded

---

## First Record Challenge

The first 10 external contributors to submit a verified calibration record are permanently credited in SportMind's history. No coding required.

Reference example: **sportmind.dev/first-record** — the complete UCL Final 2026 signal and verified outcome.

---

## Contributing

- **Calibration records** — `FIRST-RECORD-CHALLENGE.md`
- **Gap reports** — `CONTRIBUTING-GAPS.md`
- **Framework contributions** — `CONTRIBUTING.md`

Library Rule: *"Will this intelligence still be true and useful in six months?"*

---

*SportMind v3.97.99 · MIT License · sportmind.dev · © 2026 SportMind*
