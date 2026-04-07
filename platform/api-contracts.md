# SportMind Platform — API Contracts

**Purpose:** Formal interface specifications for every SportMind skill call.
These contracts define what each skill accepts as input, what it guarantees to
return, what errors look like, and how versioning works.

**Governing principle:** SportMind's sole purpose remains unchanged — open sports
intelligence for AI agents and developers. These contracts make that intelligence
reliable, composable, and buildable-upon without changing what it is.

---

## Contract principles

```
1. OPEN INTELLIGENCE FIRST
   Every skill contract serves the same purpose as the underlying skill file:
   teaching agents to reason correctly about sports. The API layer adds
   reliability and composability — it does not restrict or monetise access.

2. STABLE GUARANTEES
   Once a field is in a versioned contract, it stays. Deprecated fields are
   kept and marked; never silently removed. Agents built on v1 contracts
   always receive v1 responses unless they explicitly upgrade.

3. FAIL INFORMATIVELY
   Every error response explains what the agent should do next.
   Errors never leave an agent in an ambiguous state.

4. GRACEFUL DEGRADATION
   If a modifier cannot be calculated (missing data), the contract specifies
   the neutral default (1.00) and sets the relevant uncertainty flag.
   Agents always receive a complete response — never a partial one.
```

---

## Versioning

```
CURRENT VERSION: 1.0
SCHEMA OBJECT FIELD: "schema_version": "1.0"

VERSION LIFECYCLE:
  1.0 (current) — initial platform formalisation
  1.x (minor)   — additive changes: new optional fields, new flag types
                  Always backward compatible; existing agents unaffected
  2.0 (major)   — breaking changes: field renamed, type changed, field removed
                  6-month deprecation notice; migration guide published

HOW AGENTS DECLARE VERSION:
  Include in request: "sportmind_schema_version": "1.0"
  If absent: platform serves current version

HOW TO DETECT SCHEMA CHANGES:
  Monitor: schema_version field in every response
  If received version > declared version: new optional fields available
  If received version = 2.x and declared = 1.x: migration required
```

---

## Core skill call format

All SportMind skill calls follow this request/response envelope:

```json
REQUEST:
{
  "sportmind_request": {
    "schema_version": "1.0",
    "skill": "skill-identifier",
    "sport": "football | basketball | mma | ...",
    "context": {
      "event_id": "string or null",
      "token_symbol": "string or null",
      "team_id": "string or null",
      "player_id": "string or null"
    },
    "inputs": {
      "base_score": 0.0,
      "additional_inputs": {}
    },
    "options": {
      "include_reasoning": true,
      "include_defi_context": false,
      "load_layers": [1, 2, 3, 4, 5]
    }
  }
}

RESPONSE:
  Standard SportMind confidence output schema (core/confidence-output-schema.md)
  with schema_version matching the requested version.
```

---

## Skill contract library

### CONTRACT: `sportmind.modifier.athlete`

**Purpose:** Compute the composite athlete modifier for a given player/team and event.
Returns the adjusted signal score and full modifier breakdown.

```
ACCEPTS:
  skill:          "modifier.athlete"
  sport:          any supported sport identifier
  context:
    event_id:     upcoming event identifier (optional; uses next scheduled if null)
    team_id:      team identifier (required for team sports)
    player_id:    specific player (optional; modifier covers full squad if null)
  inputs:
    base_score:   raw signal score from upstream platform (0–100)

GUARANTEES TO RETURN:
  modifiers_applied:
    athlete_modifier:     float (1.00 if data unavailable)
    composite_modifier:   float (product of all applied modifiers)
  signal:
    base_score:           echoes input
    adjusted_score:       base_score × composite_modifier
    confidence_tier:      HIGH | MEDIUM | LOW | ABSTAIN
  flags:
    injury_warning:       bool
    lineup_unconfirmed:   bool
    congestion_warning:   bool

NEUTRAL DEFAULT:
  If athlete data unavailable: athlete_modifier = 1.00
  Reason documented in: reasoning.primary_signal_driver
  
ERRORS:
  UNKNOWN_SPORT:     Sport not in SportMind library; returns neutral modifier
  UNKNOWN_PLAYER:    Player ID not recognised; returns squad-level modifier only
  NO_UPCOMING_EVENT: No scheduled event found; abstain recommended

VERSION STABILITY (v1.0):
  modifiers_applied, signal, and flags objects: guaranteed stable
  reasoning and sizing objects: may gain optional fields in minor versions
```

---

### CONTRACT: `sportmind.modifier.macro`

**Purpose:** Check for active macro events and return the appropriate multiplier.
The first check any agent should run — macro overrides everything else.

```
ACCEPTS:
  skill:          "modifier.macro"
  inputs:
    btc_price:    current BTC price (optional; platform fetches if null)
    btc_200d_ma:  BTC 200-day moving average (optional)
    chz_price:    current CHZ price (optional)
    sport:        sport to check macro relevance for

GUARANTEES TO RETURN:
  modifiers_applied:
    macro_modifier:       float (1.00 if no active event)
  flags:
    macro_override_active: bool
  reasoning:
    primary_signal_driver: describes active macro event if present, or "No active macro event"
  
  Additional field (platform extension, v1.0):
  "macro_context": {
    "active_events": [],           list of active macro events
    "crypto_cycle_phase":          "BULL | NEUTRAL | BEAR | EXTREME_BEAR"
    "chz_btc_correlation_90d":     float
    "recommended_next_check_utc":  ISO-8601
  }

NEUTRAL DEFAULT:
  No active macro event: macro_modifier = 1.00; macro_override_active = false

ERRORS:
  PRICE_DATA_UNAVAILABLE: Returns macro_modifier = 1.00 with data_unavailable flag
```

---

### CONTRACT: `sportmind.modifier.defi`

**Purpose:** Pre-execution liquidity check. Must run before any fan token position.
Returns liquidity assessment, slippage estimate, and LP activity signal.

```
ACCEPTS:
  skill:          "modifier.defi"
  context:
    token_symbol: fan token symbol (e.g. "BAR", "PSG")
  inputs:
    trade_size_usd: intended position size in USD
    base_score:     current signal score (to calculate effective adjusted score)

GUARANTEES TO RETURN:
  flags:
    liquidity_warning:   bool (true if TVL < $500k)
    liquidity_critical:  bool (true if TVL < $100k or slippage > 3%)
  defi_context:
    primary_venue:       "CEX" | "DEX"
    pool_tvl_usd:        float
    estimated_slippage_pct: float
    lp_activity_signal: "ACCUMULATION" | "NEUTRAL" | "DISTRIBUTION" | "UNKNOWN"
    lifecycle_phase:     integer (1–6)
  sizing:
    position_size_pct:   float (adjusted for liquidity; max 20% if liquidity_critical)
    recommended_action:  "ENTER" | "REDUCE" | "ABSTAIN"

NEUTRAL DEFAULT:
  If pool data unavailable: liquidity_warning = true (conservative)
  position_size_pct capped at 40% when data unavailable

ERRORS:
  TOKEN_NOT_FOUND:       No pool data for this token; liquidity_critical = true
  DATA_STALE:            Pool data > 10 minutes old; liquidity_warning = true
```

---

### CONTRACT: `sportmind.signal.full`

**Purpose:** Full five-layer SportMind analysis. The complete intelligence stack
for any event. Calls all relevant sub-contracts and returns a unified output.

```
ACCEPTS:
  skill:          "signal.full"
  sport:          sport identifier
  context:
    event_id:     event identifier
    token_symbol: fan token symbol (optional; omit for non-token analysis)
  inputs:
    base_score:   raw signal score from upstream platform
    trade_size_usd: intended position size (optional; required for defi check)
  options:
    include_defi_context: bool (default: true if token_symbol provided)
    load_layers:          array (default: [1,2,3,4,5])
    skip_layers:          array (default: [])

GUARANTEES TO RETURN:
  Full SportMind confidence output schema (all objects)
  layer_inputs: shows which layers were loaded and active

EXECUTION ORDER:
  1. macro modifier (layer 5)
  2. market tier check (layer 4)
  3. sport domain context (layer 1)
  4. athlete modifier (layer 2)
  5. on-chain state if token provided (layer 3)
  6. DeFi check if token and trade_size provided
  7. Modifier pipeline: congestion → officiating → weather → narrative
  8. Compose final confidence output

ERRORS:
  SPORT_NOT_FOUND:       Returns null output with error code
  INSUFFICIENT_CONTEXT:  Required fields missing; specifies which fields needed
```

---

### CONTRACT: `sportmind.intelligence.partnership`

**Purpose:** Assess the health and phase of a fan token partnership.
Returns PHS score with all component indicators and lifecycle phase.

```
ACCEPTS:
  skill:          "intelligence.partnership"
  context:
    token_symbol: fan token symbol
  inputs:
    uef:   utility event frequency (0–1.0, optional; fetched if null)
    csp:   club social promotion score (0–1.0, optional)
    hct:   holder count trend (0–1.0, optional)
    tui:   token utility innovation (0–1.0, optional)
    pds:   partnership duration signal (0–1.0, optional)
    vsi:   validator status indicator (0–1.0, optional; null for non-validators)

GUARANTEES TO RETURN:
  Additional field:
  "partnership_context": {
    "phs_score":         float (0–1.0)
    "phs_tier":          "HEALTHY | PLATEAU | DECLINING | TERMINAL"
    "validator_adjusted": bool
    "lifecycle_phase":   integer (1–6)
    "phase_label":       "PRE_LAUNCH | LAUNCH | ACTIVE | PLATEAU | NON_CONTRACTUAL_TRANSITION | NON_CONTRACTUAL"
    "indicators": {
      "uef": float, "csp": float, "hct": float,
      "tui": float, "pds": float, "vsi": float or null
    }
    "recommended_layer3_weight": float (0.0–1.0)
  }
  
PHS THRESHOLDS:
  >= 0.75: HEALTHY — full Layer 3 applicable
  0.50–0.74: PLATEAU — reduce Layer 3 weight to 0.70
  0.25–0.49: DECLINING — reduce Layer 3 weight to 0.40
  < 0.25: TERMINAL — begin non-contractual assessment
```

---

## Error response format

All skill calls return errors in this standard format:

```json
{
  "sportmind_output": {
    "schema_version": "1.0",
    "error": {
      "code": "UNKNOWN_SPORT",
      "message": "Sport 'lacrosse' not found in SportMind library",
      "agent_action": "Use a supported sport identifier. See sportmind-overview.md for the complete list.",
      "fallback_applied": true,
      "fallback_description": "Returning neutral modifier (1.00) for all modifier fields"
    },
    "signal": {
      "base_score": 0.0,
      "adjusted_score": 0.0,
      "confidence_tier": "ABSTAIN"
    },
    "modifiers_applied": {
      "composite_modifier": 1.00
    }
  }
}
```

**Error code reference:**

| Code | Meaning | Agent action |
|---|---|---|
| `UNKNOWN_SPORT` | Sport not in library | Use supported identifier; check sportmind-overview.md |
| `UNKNOWN_PLAYER` | Player ID not recognised | Proceed with squad-level modifier only |
| `NO_UPCOMING_EVENT` | No event scheduled | Do not enter; monitor schedule |
| `TOKEN_NOT_FOUND` | No DEX pool data | Apply liquidity_critical = true; max 20% position |
| `DATA_STALE` | Source data > threshold age | Apply uncertainty flag; reduce position |
| `INSUFFICIENT_CONTEXT` | Required field missing | Response specifies which field(s) needed |
| `MACRO_DATA_UNAVAILABLE` | Cannot fetch BTC/CHZ price | Apply macro_modifier = 1.00 conservatively |
| `SCHEMA_VERSION_MISMATCH` | Declared version differs from served | Check migration guide |
| `LAYER_UNAVAILABLE` | Requested layer not loaded | Response specifies which layer; proceed with available layers |

---

## How third-party platforms use these contracts

### FanTokenIntel integration pattern

```python
# FanTokenIntel provides base_score
base = fti.signals_active(token="BAR").score  # e.g. 72

# SportMind provides the interpretation layer via contract
response = sportmind.call({
    "skill": "signal.full",
    "sport": "football",
    "context": {
        "event_id": fti.next_event(token="BAR").id,
        "token_symbol": "BAR"
    },
    "inputs": {
        "base_score": base,        # FTI score becomes SportMind base_score
        "trade_size_usd": 5000
    }
})

# Use SportMind's adjusted score for the decision
adjusted = response["signal"]["adjusted_score"]   # e.g. 63 (after modifier)
action   = response["sizing"]["recommended_action"] # e.g. "WAIT"
flags    = response["flags"]                       # injury_warning, etc.
```

### Any data platform — generic pattern

```python
# Step 1: Any platform provides a base signal score (0–100)
base_score = your_platform.get_signal(event_id)

# Step 2: SportMind enriches it
response = sportmind.call({
    "skill": "signal.full",
    "sport": your_sport,
    "context": {"event_id": your_event_id},
    "inputs": {"base_score": base_score}
})

# Step 3: Use the guaranteed response fields
adjusted = response["signal"]["adjusted_score"]
tier     = response["signal"]["confidence_tier"]
action   = response["sizing"]["recommended_action"]
modifier = response["modifiers_applied"]["composite_modifier"]

# The base_score is yours. The reasoning around it is SportMind's.
# This is the division of responsibility.
```

---

## Skill identifier reference

| Skill identifier | Purpose | Primary skill file |
|---|---|---|
| `modifier.athlete` | Athlete composite modifier | `athlete/{sport}/` |
| `modifier.macro` | Macro event check + multiplier | `macro/macro-overview.md` |
| `modifier.defi` | Liquidity pre-execution check | `fan-token/defi-liquidity-intelligence/` |
| `modifier.congestion` | Fixture congestion adjustment | `core/core-fixture-congestion.md` |
| `modifier.officiating` | Referee/judge tendency | `core/core-officiating-intelligence.md` |
| `modifier.weather` | Match-day conditions | `core/core-weather-match-day.md` |
| `modifier.narrative` | Narrative momentum | `core/core-narrative-momentum.md` |
| `signal.full` | Complete five-layer analysis | All layers |
| `signal.domain` | Sport domain context only | `sports/{sport}/` |
| `intelligence.partnership` | Fan token PHS assessment | `fan-token/fan-token-partnership-intelligence/` |
| `intelligence.lifecycle` | Token lifecycle phase | `fan-token/fan-token-lifecycle/` |
| `intelligence.validator` | Validator status (VSI) | `fan-token/blockchain-validator-intelligence/` |
| `intelligence.commercial` | Full commercial brief | Layer 3 commercial chain |

---

*These contracts define how SportMind's intelligence is accessed — not what it contains.
The intelligence itself lives in the skill files. The contracts make that intelligence
reliable and composable for agents and developers building on top of SportMind.*

*MIT License · SportMind · sportmind.dev*
