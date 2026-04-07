# SportMind Skill Bundles

**Named pre-configured skill stacks for the most common SportMind use cases.**

Instead of assembling a skill stack from scratch, developers and agents can
reference a named bundle that loads exactly the right skills in the right order
for a specific use case. Bundles reduce setup time, ensure correct loading order,
and provide a shared vocabulary for common deployments.

---

## Bundle catalogue

| Bundle ID | Use case | Sports | Layers | Token count |
|---|---|---|---|---|
| `ftier1-football` | Fan token Tier 1 — football | Football | 5 | ~8,200 |
| `ftier1-cricket` | Fan token Tier 1 — cricket | Cricket | 5 | ~7,400 |
| `ftier1-basketball` | Fan token Tier 1 — basketball | Basketball/NBA | 5 | ~7,100 |
| `ftier1-motorsport` | Fan token Tier 1 — F1/MotoGP | F1, MotoGP | 5 | ~6,800 |
| `ftier2-football` | Fan token Tier 2 — football | Football | 4 | ~5,600 |
| `prematch-football` | Pre-match analysis — football | Football | 3 | ~4,200 |
| `prematch-cricket` | Pre-match analysis — cricket | Cricket | 3 | ~3,800 |
| `prematch-mma` | Pre-match analysis — MMA | MMA | 3 | ~3,600 |
| `governance-brief` | Governance intelligence brief | Any | 3 | ~3,400 |
| `transfer-intel` | Transfer intelligence | Football | 4 | ~5,100 |
| `commercial-brief` | Athlete commercial brief | Any | 4 | ~4,800 |
| `tournament-tracker` | Tournament NCSI tracking | Multi-sport | 4 | ~5,400 |
| `macro-only` | Macro state check | Any | 1 | ~800 |
| `minimal-signal` | Minimum viable signal | Any | 2 | ~2,100 |

---

## Bundle definitions

### `ftier1-football` — Fan Token Tier 1: Football

The complete fan token intelligence stack for football. Use for portfolio monitoring,
pre-match token signal, and governance intelligence for football club tokens.

```yaml
bundle_id: ftier1-football
version: "3.19.0"
loading_order:
  1. macro/macro-overview.md                              # Always first
  2. macro/macro-crypto-market-cycles.md                  # Crypto cycle state
  3. macro/macro-geopolitical.md                          # Geopolitical context
  4. market/market-football.md                            # Football market tier
  5. market/football-leagues-advanced.md                  # League stakes intelligence
  6. market/international-football-cycle.md               # Competition calendar + NCSI weights
  7. sports/football/sport-domain-football.md             # Domain signals + modifiers
  8. athlete/football/athlete-intel-football.md           # Athlete intelligence
  9. fan-token/fan-token-lifecycle/                       # Lifecycle model
  10. fan-token/fan-token-pulse/                          # HAS + real-time signals
  11. fan-token/defi-liquidity-intelligence/              # DeFi + TVL context
  12. fan-token/transfer-signal/                          # Transfer + APS signals
  13. fan-token/fan-sentiment-intelligence/               # Emotional arc + CDI
  14. core/confidence-output-schema.md                    # Output format

use_cases:
  - fan_token_tier1
  - portfolio_monitor
  - pre_match_football
  - governance_brief_football

estimated_tokens: 8200
freshness_requirements:
  macro: Tier 3 (refresh every 4-8h)
  athlete: Tier 4 (refresh at T-72h, T-24h, T-2h)
  defi: Tier 5 (always fetch live)
```

### `ftier1-cricket` — Fan Token Tier 1: Cricket

```yaml
bundle_id: ftier1-cricket
version: "3.19.0"
loading_order:
  1. macro/macro-overview.md
  2. macro/macro-crypto-market-cycles.md
  3. market/market-cricket.md
  4. market/international-cricket-cycle.md                # IPL, T20 WC, PSL calendar
  5. sports/cricket/sport-domain-cricket.md               # Format-first rule
  6. athlete/cricket/athlete-intel-cricket.md             # IPL + format specialist
  7. fan-token/fan-token-lifecycle/
  8. fan-token/fan-token-pulse/
  9. fan-token/defi-liquidity-intelligence/
  10. fan-token/fan-sentiment-intelligence/               # India-Pakistan arc model
  11. core/confidence-output-schema.md

format_note: Always identify T20/ODI/Test BEFORE loading athlete modifiers.
india_pakistan_note: ×2.00 ATM modifier applies regardless of competition tier.
estimated_tokens: 7400
```

### `ftier1-basketball` — Fan Token Tier 1: Basketball (NBA)

```yaml
bundle_id: ftier1-basketball
version: "3.19.0"
loading_order:
  1. macro/macro-overview.md
  2. macro/macro-crypto-market-cycles.md
  3. market/market-nba.md
  4. sports/nba/sport-domain-nba.md
  5. athlete/nba/athlete-intel-nba.md                     # Star player + playoff + trade deadline
  6. fan-token/fan-token-lifecycle/
  7. fan-token/fan-token-pulse/
  8. fan-token/defi-liquidity-intelligence/
  9. fan-token/fan-sentiment-intelligence/
  10. core/confidence-output-schema.md

load_management_note: Check star player DNP-rest status before any other modifier.
playoff_note: Apply ×0.92 reliability discount on regular-season form in playoffs.
estimated_tokens: 7100
```

### `ftier1-motorsport` — Fan Token Tier 1: Motorsport (F1 + MotoGP)

```yaml
bundle_id: ftier1-motorsport
version: "3.19.0"
loading_order:
  1. macro/macro-overview.md
  2. macro/macro-crypto-market-cycles.md
  3. market/market-formula1.md
  4. sports/formula1/sport-domain-formula1.md
  5. athlete/formula1/athlete-intel-formula1.md           # Driver-constructor pairing
  6. sports/motogp/sport-domain-motogp.md
  7. athlete/motogp/athlete-intel-motogp.md
  8. fan-token/fan-token-lifecycle/
  9. fan-token/fan-token-pulse/
  10. fan-token/defi-liquidity-intelligence/
  11. core/confidence-output-schema.md

qualifying_note: For F1 — load post-qualifying (Saturday) for highest-quality race signal.
street_circuit_note: Monaco/Singapore/Jeddah/Baku — apply qualifying_delta ×1.40.
estimated_tokens: 6800
```

### `prematch-football` — Pre-Match Analysis: Football

Lean stack for pre-match signal generation. No DeFi layer (not needed for match
prediction without fan token context).

```yaml
bundle_id: prematch-football
version: "3.19.0"
loading_order:
  1. macro/macro-overview.md                              # Macro modifier check
  2. market/market-football.md                            # Competition tier
  3. sports/football/sport-domain-football.md             # Full domain signal
  4. athlete/football/athlete-intel-football.md           # Lineup + form
  5. core/core-officiating-intelligence.md                # Referee signal
  6. core/derby-intelligence.md                           # Derby check
  7. core/breaking-news-intelligence.md                   # Breaking news protocol
  8. core/confidence-output-schema.md

omits: fan-token layers (no token context needed for pure match analysis)
estimated_tokens: 4200
freshness_critical: athlete (T-2h lineup confirmation)
```

### `prematch-mma` — Pre-Match Analysis: MMA

```yaml
bundle_id: prematch-mma
version: "3.19.0"
loading_order:
  1. macro/macro-overview.md
  2. sports/mma/sport-domain-mma.md
  3. athlete/mma/athlete-intel-mma.md
  4. core/breaking-news-intelligence.md                   # Weight miss protocol

weigh_in_rule: ALWAYS check weigh-in result before any other modifier.
               Weight miss → RELOAD with ×0.72 modifier regardless of other signals.
estimated_tokens: 3600
```

### `governance-brief` — Governance Intelligence Brief

```yaml
bundle_id: governance-brief
version: "3.19.0"
loading_order:
  1. macro/macro-overview.md
  2. fan-token/fan-token-lifecycle/                       # Phase context
  3. fan-token/sports-governance-intelligence/            # GSI model
  4. fan-token/fan-sentiment-intelligence/                # Emotional arc (post-outcome context)
  5. core/confidence-output-schema.md

governance_note: Decision_Weight must be classified before GSI calculation.
                 governance_theatre flag overrides all signals.
estimated_tokens: 3400
```

### `transfer-intel` — Transfer Intelligence

```yaml
bundle_id: transfer-intel
version: "3.19.0"
loading_order:
  1. macro/macro-overview.md
  2. macro/macro-crypto-market-cycles.md
  3. market/market-football.md
  4. fan-token/transfer-signal/                           # APS, TSI, ATM
  5. core/athlete-financial-intelligence.md               # Contract stage, wages
  6. core/manager-intelligence.md                         # Manager transfer strategy
  7. fan-token/fan-token-lifecycle/
  8. core/breaking-news-intelligence.md                   # Transfer confirmation protocol
  9. core/confidence-output-schema.md

contract_window_note: Apply financial_aps_adjusted() when contract < 12 months.
                      Pre-contract window opens at < 6 months remaining.
estimated_tokens: 5100
```

### `commercial-brief` — Athlete Commercial Brief

```yaml
bundle_id: commercial-brief
version: "3.19.0"
loading_order:
  1. macro/macro-overview.md
  2. fan-token/transfer-signal/                           # APS base
  3. core/athlete-financial-intelligence.md               # Financial context
  4. fan-token/fan-sentiment-intelligence/                # CDI + emotional arc
  5. fan-token/sports-governance-intelligence/            # Governance eligibility
  6. core/confidence-output-schema.md

output_focus: APS, AELS, ABS, CDI, LTUI projection
estimated_tokens: 4800
```

### `macro-only` — Macro State Check

Minimal bundle for agents that only need to check macro conditions.

```yaml
bundle_id: macro-only
version: "3.19.0"
loading_order:
  1. macro/macro-overview.md
  2. macro/macro-crypto-market-cycles.md

use_case: Agent initialisation; quick macro gate before full analysis
estimated_tokens: 800
output: macro_modifier, phase, gate_recommendation (PROCEED / WAIT / ABORT)
```

### `minimal-signal` — Minimum Viable Signal

Smallest stack that produces a valid SportMind signal with SMS.

```yaml
bundle_id: minimal-signal
version: "3.19.0"
loading_order:
  1. macro/macro-overview.md
  2. sports/{sport}/sport-domain-{sport}.md              # Swap in target sport
  3. core/confidence-output-schema.md

use_case: Rapid integration testing; bandwidth-constrained agents
estimated_tokens: ~2100
sms_ceiling: 65 (partial stack — cannot reach GOOD without more layers)
note: "This is the starter pack 01-simple-signal.py stack."
```

---

## Bundle API endpoints

```bash
# Fetch a named bundle via Skills API
GET /bundle/{bundle_id}

# Examples
GET /bundle/ftier1-football
GET /bundle/prematch-cricket
GET /bundle/macro-only

# Query parameters
GET /bundle/ftier1-football?compress=true    # Return compressed versions
GET /bundle/ftier1-football?hashes_only=true  # Return SHA-256 hashes only (for integrity check)
GET /bundle/ftier1-football?meta_only=true    # Return bundle metadata without skill content

# Response structure
{
  "bundle_id": "ftier1-football",
  "version": "3.19.0",
  "loading_order": [...],
  "skills": [
    {
      "skill_id": "macro/macro-overview.md",
      "content": "...",
      "sha256": "...",
      "size_chars": 4821,
      "freshness_tier": 0
    }
  ],
  "estimated_tokens": 8200,
  "generated_at": "2026-04-05T10:00:00Z"
}
```

```python
# Python helper for bundle loading
import requests

def load_bundle(bundle_id: str, api_url: str = "http://localhost:8080") -> dict:
    """Load a named SportMind bundle."""
    response = requests.get(f"{api_url}/bundle/{bundle_id}", timeout=15)
    response.raise_for_status()
    return response.json()

def get_bundle_context(bundle_id: str, api_url: str = "http://localhost:8080") -> str:
    """Get bundle as a single context string for LLM system prompt injection."""
    bundle = load_bundle(bundle_id, api_url)
    parts = []
    for skill in bundle.get("skills", []):
        parts.append(f"--- {skill['skill_id']} ---\n{skill['content']}")
    return "\n\n".join(parts)

# Usage
context = get_bundle_context("ftier1-football")
# → inject into Claude system prompt or LLM context
```

---

## MCP bundle tool

```
The sportmind_stack MCP tool supports bundle IDs as a shorthand:

Tool call:
  {
    "name": "sportmind_stack",
    "arguments": {
      "bundle_id": "ftier1-football"
    }
  }

Equivalent to:
  {
    "name": "sportmind_stack",
    "arguments": {
      "sport": "football",
      "use_case": "fan_token_tier1"
    }
  }

Bundle IDs are preferred for production deployments — they are version-pinned
and guarantee consistent loading order across agent restarts.
```

---

## Creating custom bundles

```yaml
# Custom bundle template
bundle_id: my-custom-bundle
version: "3.19.0"
description: "My specific use case"
loading_order:
  1. macro/macro-overview.md          # Always include
  - [sport domain skill]
  - [athlete skill if needed]
  - [fan token layer if needed]
  - core/confidence-output-schema.md  # Always include last

# Rules for custom bundles:
# 1. macro/macro-overview.md MUST be first
# 2. core/confidence-output-schema.md SHOULD be last
# 3. Loading order follows: macro → market → domain → athlete → fan-token → schema
# 4. Omit layers you do not need to reduce token count
# 5. Include core/breaking-news-intelligence.md for any live-match use case
```

---

*MIT License · SportMind · sportmind.dev*
*See `platform/skill-registry-api.md` for the full Skills API specification.*
*See `platform/freshness-strategy.md` for bundle freshness management.*
