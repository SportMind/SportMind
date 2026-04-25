# SportMind v3.30 — Community Release

**The open sports intelligence library for AI agents is now publicly available.**

This is the first public release of SportMind — a library built over 31 version cycles
to teach AI agents how to reason about sports. Not just predict match outcomes, but
understand the full commercial, financial, and competitive intelligence that the sports
industry now runs on.

---

## What is in this release

### The intelligence framework

42 sport domains, fully documented with event playbooks, risk variables, signal weights,
and agent reasoning prompts. 29 athlete intelligence skills, all at GOOD or DEEP depth —
from football at 513 lines to kabaddi's raider primacy model to NASCAR's track-type
specialisation framework. 37 fan token commercial skills covering the full lifecycle
from Phase 1 through Phase 5e Sports DAO governance. 9 macro intelligence documents
including the crypto cycle model that every agent must consult first.

### The calibration foundation

126 empirically validated outcome records across 21 sports. 96% direction accuracy.
All 5 wrong predictions are European football draws — fully documented with root-cause
analysis in the recalibration reports. Eight individual modifiers have zero wrong-direction
records across their complete evidence base.

The calibration reports (v3 through v6 in `core/`) show exactly what was tested,
what was confirmed, and what was updated. This is not a black box — every accuracy
claim in the library is verifiable against the records in `community/calibration-data/`.

### The developer tooling

- **Skills API** — local server, named bundles (14), stack endpoints
- **MCP server** — 5 tools, deployment guide for Vercel/Render/Docker in 30 minutes
- **Data connector templates** — copy-paste Python for football-data.org lineup data,
  KAYEN fan token market data, and CoinGecko macro state
- **Starter pack** — 7 working Python examples from ⭐ to ⭐⭐⭐⭐⭐
- **Agentic workflow patterns** — 8 patterns from portfolio monitoring to governance agents
- **Application blueprints** — 11 complete application designs
- **Agent prompts** — 16 prompts organised by stakeholder type
- **Compressed summaries** — 54 token-efficient skill representations for constrained contexts

### Chiliz 2030 intelligence (v3.30)

The library is current with the Chiliz 2030 roadmap published February 2026:

- **Gamified tokenomics intelligence** — Win→tokens burn, Loss→tokens mint.
  Performance-linked supply mechanics rolling out Q2 2026. A WIN prediction
  is now simultaneously a SUPPLY REDUCTION prediction. Complete signal model
  including burn/mint rate modifiers, season supply tracking, and prediction
  market interaction flags.
- **SportFi regulatory intelligence** — Joint SEC/CFTC guidance (2026) classifying
  fan tokens as utility digital commodities under CFTC, enabling US market re-entry.
  Full four-jurisdiction framework: EU MiCA, US CFTC, UK FCA, Brazil. Regulatory
  discount model for signal generation by jurisdiction.
- **Omni-chain liquidity intelligence** — Fan tokens expanding to multiple blockchains
  via LayerZero from Q1 2026. Aggregate TVL across chains before applying liquidity
  tier. PEPPER governance token context for KAYEN protocol monitoring.
- **Three-stage Fan Token™ evolution** — Stage 1 utility → Stage 2 dynamic tokenomics
  → Stage 3 RWA with equity exposure. Stage stacking principle. Updated RSF formula
  with stage bonuses.

### The community infrastructure

Everything needed for external contributors to participate immediately:

- `FIRST-RECORD-CHALLENGE.md` — the fastest path to contributing (30 minutes, no coding)
- `GOOD_FIRST_ISSUES.md` — 4 contribution levels, each with a specific definition of done
- `community/calibration-data/CONTRIBUTING.md` — calibration record format and submission
- `community/CONTRIBUTORS.md` — recognition tiers including Founding Calibrator status
- GitHub issue templates for calibration records, skill proposals, and improvements
- PR template with quality checklist

---

## Why calibration records matter

The library's modifier pipeline improves as community records accumulate. Right now,
the athlete_modifier has 25 of the 50 records needed for a full recalibration. The
dew_factor has 5 of 50. The derby_active has 2 of 50.

Every practitioner who uses SportMind before a real match and submits the outcome
moves a modifier closer to its evidence threshold. When modifiers reach their thresholds,
the expert estimates that built the library get replaced by data-confirmed values.

The first 10 external contributors who submit calibration records receive permanent
Founding Calibrator recognition in the library's history. That recognition does not
expire or get overwritten by later contributors.

---

## What this release does not include

**Live data.** SportMind is an intelligence framework, not a data provider. Connecting
to live data sources (lineups, scores, fan token prices) is the application developer's
responsibility. `platform/data-connector-templates.md` provides copy-paste code for
the three most important sources.

**Full modifier recalibration.** The modifiers are empirically validated and confirmed
correct in direction, but the magnitudes have wide confidence intervals until thresholds
are reached. A ×1.12 athlete_modifier is "meaningfully positive" — not precisely ×1.12.
This is honest and documented.

**Hosted infrastructure.** There is no hosted SportMind API or MCP endpoint maintained
by the project. Self-hosting instructions are in `platform/sportmind-mcp-deployment.md`.
A community-hosted endpoint is in `GOOD_FIRST_ISSUES.md` as a Level 4 contribution opportunity.

---

## Getting started

**Fastest path (5 minutes, no setup):**
Open any LLM, paste `core/sportmind-purpose-and-context.md` + a sport domain file,
and ask for a pre-match signal. You have SportMind working immediately.

**Developer path:**
```bash
git clone https://github.com/SportMind/SportMind
pip install aiohttp --break-system-packages
python scripts/sportmind_api.py
python examples/starter-pack/01-simple-signal.py
```

**Find your path:** `WHO-USES-THIS.md` — 60 seconds to your starting point.

---

## Acknowledgements

SportMind was built over 31 version cycles as a structured open-source project.
The calibration foundation — 126 records across 21 sports — was built by the
founding team as seed data for the community to build on. Every modifier in the
library was designed with a recalibration threshold in mind, because the founding
team knew that expert estimates are starting points, not destinations.

The library's accuracy at release is 96%. The library's accuracy after the community
reaches all modifier thresholds will be higher, more precisely measured, and more
trustworthy — because it will be built on evidence from hundreds of practitioners,
not just one team.

That is what the calibration pipeline exists for. Now it is the community's turn.

---

## Version history

Full history in `CHANGELOG.md`. The library has 60 CHANGELOG entries across
31 version cycles from v3.0 through v3.30.

---

*MIT License · SportMind · sportmind.dev*
*Repository: https://github.com/SportMind/SportMind*
