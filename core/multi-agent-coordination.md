# Multi-Agent Coordination — SportMind

How to build agents that span multiple sports, maintain context across sessions,
and chain SportMind skills efficiently. This file bridges the gap between a
prototype that works for one sport and a production agent that handles real use cases.

**Two ways to use SportMind in production:**

```
MODE 1 — LIBRARY (load skill files into context):
  Load markdown files directly into the agent's system prompt.
  Works with any LLM. No dependencies. Good for prototypes and simple use cases.
  See: agent-prompts/agent-prompts.md for ready-to-deploy prompts.

MODE 2 — PLATFORM CONTRACTS (call skill interfaces):
  Call SportMind via formal skill contracts: signal.full, modifier.athlete, etc.
  Standardised inputs and guaranteed outputs. Better for production systems.
  See: platform/api-contracts.md for the complete contract specifications.
  
For multi-agent systems, Mode 2 (contracts) is recommended — agents can call
exactly the intelligence they need without managing file loading themselves.
```

---

## The core challenge

SportMind contains ~185 files totalling ~750KB. No LLM context window can load
everything simultaneously. Production agents must make intelligent decisions about:
- Which files to load for a given query
- How to maintain state across a multi-turn conversation
- How to route multi-sport queries to the right skill combination
- How to handle conflicting signals from different layers

This file gives developers the patterns to solve these problems.

---

## 1. Context window management

### File size reference (approximate token counts)

```
LARGE FILES (>5,000 tokens — load selectively):
  sportmind-overview.md:          ~18,700 tokens — reference only; never load in full
  CHANGELOG.md:                   ~18,000 tokens — never load in agent context
  agent-prompts/agent-prompts.md: ~3,700 tokens — load relevant prompt only

MEDIUM FILES (1,000–5,000 tokens — load when relevant):
  Sport domain skills:            ~1,500–4,000 tokens each
  Athlete skills:                 ~2,000–4,500 tokens each
  Fan token skills:               ~1,500–3,500 tokens each
  Market files:                   ~800–2,500 tokens each
  Macro files:                    ~1,500–3,000 tokens each

SMALL FILES (<1,000 tokens — always safe to load):
  core-athlete-modifier-system.md: ~1,240 tokens
  core-signal-weights-by-sport.md: ~2,800 tokens (but load football row only if single sport)
  confidence-output-schema.md:     ~3,100 tokens (load schema definition section only)
  Individual market files:         ~800–1,200 tokens typical
```

### Minimum viable loading sets

```
USE CASE 1 — Single sport prediction market (no tokens):
  MINIMUM: Layer 1 sport skill + athlete skill + output schema definition
  TOKENS: ~4,000–8,000 (fits in any modern context window)
  SKIP: All Layer 3, Layer 5 (if no active macro events), market file

USE CASE 2 — Fan token signal (Tier 1 sport):
  MINIMUM: Layer 1 + athlete + fan-token-pulse + sport token intelligence + output schema
  TOKENS: ~7,000–12,000
  LOAD ORDER: macro check → market tier → Layer 1 → Layer 2 → Layer 3

USE CASE 3 — Full five-layer analysis:
  MINIMUM: 1 macro file + 1 market file + Layer 1 + Layer 2 + 1-2 Layer 3 + output schema
  TOKENS: ~12,000–20,000
  PRACTICAL LIMIT: Drop market file and macro if no active events; adds ~4,000 tokens

USE CASE 4 — DeFi-aware token agent:
  MINIMUM: DeFi skill + fan-token-pulse + Layer 1 + output schema (with defi_context)
  TOKENS: ~8,000–13,000
  PRE-LOAD: Run liquidity check data retrieval BEFORE loading any skills

USE CASE 5 — Commercial intelligence (brands, agents, clubs):
  MINIMUM: fan-token-why + fan-token-pulse + brand-score + athlete-social-activity + output schema
  TOKENS: ~9,000–15,000
  SKIP: Sport domain skill (not needed for commercial analysis)
```

### Selective loading patterns

```python
# Pattern: Load only the rows you need from large tables

# Instead of loading all 30 rows from core-signal-weights-by-sport.md:
FOOTBALL_SIGNAL_WEIGHTS = """
For football, weight signals as follows:
  Sports catalyst: 30% | Whale/market: 25% | Social: 20% | Price trend: 15% | Macro: 10%
"""

# Instead of loading the full confidence-output-schema.md (3,100 tokens):
SCHEMA_QUICK = """
Output format: JSON with keys:
  signal.adjusted_score (0-100), signal.direction, signal.confidence_tier (HIGH/MEDIUM/LOW/ABSTAIN)
  modifiers_applied.composite_modifier
  flags.injury_warning, flags.liquidity_warning
  sizing.recommended_action (ENTER/REDUCE/WAIT/ABSTAIN), sizing.position_size_pct
"""

# Instead of loading the full modifier system:
MODIFIER_QUICK = """
adjusted_score = base_score × composite_modifier (clamped 0.40–1.40)
HIGH confidence (≥70): ENTER at 75–100%  
MEDIUM (55–69): ENTER at 40–60%
LOW (<55) or critical flag: REDUCE or ABSTAIN
"""
```

---

## 2. Session state management

### State object structure

For agents that handle multiple queries in a session, maintain a state object
rather than reloading skills on every turn:

```json
{
  "session_state": {
    "loaded_skills": {
      "layer_5_macro": "macro-overview — no active events",
      "layer_4_market": "market-football — Tier 1",
      "layer_1_domain": "sports/football",
      "layer_2_athlete": "athlete/football",
      "layer_3_token": "football-token-intelligence"
    },
    "current_context": {
      "sport": "football",
      "competition": "UEFA Champions League",
      "active_flags": {
        "injury_warning": false,
        "lineup_unconfirmed": true,
        "liquidity_warning": false
      }
    },
    "modifier_cache": {
      "athlete_modifier": 1.08,
      "computed_at": "2026-04-01T15:00:00Z",
      "valid_until": "2026-04-01T19:00:00Z",
      "invalidate_on": ["lineup_confirmation", "injury_news"]
    },
    "macro_state": {
      "crypto_cycle": "neutral",
      "chz_vs_200dma": "above",
      "modifier": 1.00,
      "last_checked": "2026-04-01T12:00:00Z"
    }
  }
}
```

### Cache invalidation rules

```
ATHLETE MODIFIER cache:
  Valid: From pre-match → until official lineup released OR injury news
  Invalidate immediately on: Official team sheet, manager press conference,
    injury announcement, transfer announcement
  Re-check at: T-2h before kickoff (lineup confirmation window)

MACRO STATE cache:
  Valid: 24 hours for stable crypto conditions
  Invalidate immediately on: Major crypto news, regulatory announcement,
    market crash (BTC move >10% in 24h), geopolitical breaking news
  Re-check: Twice daily for active macro periods; once daily for stable periods

LIQUIDITY DATA cache:
  Valid: 30 minutes (pool TVL changes continuously)
  Do not cache: Pre-execution liquidity check — always fetch fresh
  Re-check: Immediately before any position entry

SPORT DOMAIN cache:
  Valid: Indefinitely within a season (rules don't change mid-season)
  Invalidate on: Rule changes, format changes, restructuring announcements
```

---

## 3. Multi-sport routing

### Query classification

When an agent receives a query, classify it before loading any skills:

```python
def classify_query(query: str) -> dict:
    """
    Returns: {
        "sport": str,
        "layer_needs": list[int],  # [1,2,3,4,5] or subset
        "token_relevant": bool,
        "defi_relevant": bool,
        "commercial": bool,
        "prediction_market": bool
    }
    """
    
    # Sport detection (from explicit mention or context)
    # Token/DeFi indicators
    TOKEN_KEYWORDS = ["token", "CHZ", "$BAR", "fan token", "holder", "on-chain",
                      "pool", "TVL", "liquidity", "stake"]
    DEFI_KEYWORDS = ["liquidity", "pool", "DEX", "CEX", "slippage", "yield", "LP"]
    COMMERCIAL_KEYWORDS = ["sponsor", "brand", "deal", "value", "commercial"]
    PREDICTION_KEYWORDS = ["predict", "win", "odds", "signal", "should I enter"]
```

### Routing table

```
QUERY TYPE                    | LAYERS TO LOAD        | SKILLS TO PRIORITISE
------------------------------|----------------------|----------------------
"Should I enter $BAR?"        | 5→4→1→2→3            | Full stack Tier 1
"Who will win tomorrow's game"| 1→2                  | Domain + athlete only
"PSG token analysis"          | 5→4→1→2→3+validator  | Token-focused stack
"Best sponsorship for Mbappé" | 3 (commercial chain)  | brand-score → sponsorship
"DeFi yield on fan tokens"    | 3 (DeFi)             | defi-liquidity → lifecycle
"UCL final prediction"        | 5→4→1→2              | Full stack, no Layer 3
"NBA player token value"      | 4→1→2→3 (basketball) | basketball-token-intel
"Cricket match tonight"       | 5→4→1→2→weather      | Domain + weather check
```

### Multi-sport session example

```
Developer building a multi-sport agent:

PATTERN: Lazy loading with sport detection

def get_sport_from_query(query):
    """Detect sport from user query."""
    sport_keywords = {
        "football": ["football", "soccer", "premier league", "ucl", "la liga"],
        "mma": ["ufc", "mma", "fighter", "fight", "grappling"],
        "cricket": ["cricket", "ipl", "psl", "test", "ashes", "t20"],
        # ... etc
    }
    
def load_skills_for_sport(sport: str, use_case: str) -> list[str]:
    """Return ordered list of skill file paths to load."""
    base = [f"macro/macro-overview.md",
            f"market/market-{sport}.md",
            f"sports/{sport}/sport-domain-{sport}.md",
            f"athlete/{sport}/athlete-intel-{sport}.md"]
    
    if use_case == "token":
        base += [f"fan-token/{sport}-token-intelligence/*.md"]
    elif use_case == "defi":
        base += ["fan-token/defi-liquidity-intelligence/*.md"]
    
    return base

AGENT RULE:
  Load skills in response to the QUERY, not upfront.
  A multi-sport agent should NOT load all 185 files at session start.
  It should load the minimum viable set identified by query classification.
```

---

## 4. Handling conflicting signals

### When layers disagree

```
COMMON CONFLICT: Strong sport signal but adverse macro

  Layer 1 says: "High importance match, strong team signal"
  Layer 5 says: "Crypto extreme bear — CHZ falling"
  
  RESOLUTION RULE: Macro overrides sport signal for TOKEN positions.
  Macro does NOT override prediction market positions.
  
  Agent output should surface both:
  {
    "signal_direction": "BULLISH",
    "token_signal": "SUPPRESSED (macro override)",
    "prediction_market_signal": "ENTER at full size"
  }

COMMON CONFLICT: High confidence signal but thin liquidity

  Signal says: HIGH confidence, ENTER at 100%
  DeFi check says: TVL $90k, liquidity_critical = true
  
  RESOLUTION RULE: Liquidity OVERRIDES confidence for position sizing.
  High confidence does not earn you full position when liquidity is critical.
  
  Agent output:
  {
    "signal_confidence_tier": "HIGH",
    "recommended_action": "ENTER",
    "position_size_pct": 20.0,
    "note": "liquidity_critical overrides HIGH confidence on sizing"
  }

COMMON CONFLICT: Athlete modifier positive but injury unconfirmed

  Athlete skill says: Modifier × 1.12 (strong squad)
  Reality: Lineup not yet confirmed, key player doubtful
  
  RESOLUTION RULE: WAIT until lineup confirmed if injury_warning active.
  Do not use a modifier based on unconfirmed assumptions.
  Re-compute modifier when official team sheet released.
```

### Signal priority hierarchy

```
Priority order when signals conflict (highest to lowest priority):

1. Critical flags (liquidity_critical, macro_override_active, lineup_unconfirmed + injury)
   → These override everything; apply their rules regardless of other signals

2. Macro modifier (Layer 5)
   → Overrides sport signals for TOKEN positions (not prediction markets)
   → Never skip; always check

3. Injury/availability modifier (Layer 2)
   → Overrides form signals; a fit average player beats a doubtful star

4. Sport domain signal (Layer 1)
   → The base signal framework; competition tier, event playbooks

5. On-chain signal (Layer 3)
   → Supplementary to 1-4; do not override with on-chain data alone

6. Narrative modifier (last)
   → Max ±8%; applied last; never overrides critical flags
```

---

## 5. Error handling for agents

### Edge cases SportMind agents should handle

```
EDGE CASE 1 — Event cancelled or postponed:
  Trigger: Weather abandonment, safety concerns, force majeure
  Agent rule: Immediately ABSTAIN; set cancellation_risk flag
  See: core-weather-match-day.md abandonment protocol
  Token implication: Post-postponement signals are delayed, not cancelled

EDGE CASE 2 — Match already started:
  Agent should not apply pre-match modifiers to in-progress events
  In-progress events need live data that SportMind doesn't provide
  Agent rule: Flag as IN_PROGRESS; do not generate pre-match output
  Redirect: To live data provider; SportMind pre-match analysis is now historical

EDGE CASE 3 — Token not listed on any exchange:
  DeFi check returns: TVL = 0
  Agent rule: Apply liquidity_critical flag; do not enter any position
  May indicate: Non-contractual Phase 6 with no remaining liquidity

EDGE CASE 4 — Sport outside SportMind's library:
  User asks about a sport with no Layer 1 skill
  Agent rule: State clearly that no SportMind skill exists for this sport
  Do NOT invent sport-specific intelligence from general knowledge
  Redirect: To GOOD_FIRST_ISSUES.md if developer; to general sports knowledge if user

EDGE CASE 5 — Conflicting injury reports from different sources:
  Agent rule: Use the lowest reliability source's modifier, not the highest
  Apply source reliability tiers from core-athlete-modifier-system.md
  "Unverified rumour" = ×0.90 modifier regardless of what it says
  Wait for official confirmation before applying anything above ×0.95

EDGE CASE 6 — No athlete skill for this sport:
  Sport has a Layer 1 domain skill but no Layer 2 athlete skill
  Agent rule: Proceed with domain signal only; note athlete layer absent
  Apply: Standard form assumption (×1.00 neutral athlete modifier)
  In confidence output: layer_2_athlete_loaded = false
```

---

## 6. Calibration and improvement over time

### Tracking modifier accuracy

Production agents should log their SportMind outputs against actual outcomes
to calibrate modifier weights over time:

```json
{
  "calibration_log_entry": {
    "event_id": "string",
    "sport": "string",
    "predicted_direction": "HOME|AWAY|DRAW",
    "actual_result": "HOME|AWAY|DRAW",
    "predicted_adjusted_score": 72.4,
    "confidence_tier": "HIGH",
    "composite_modifier": 1.115,
    "modifier_breakdown": {
      "athlete_modifier": 1.12,
      "congestion_modifier": 0.97,
      "narrative_modifier": 1.06
    },
    "was_direction_correct": true,
    "token_prediction": "POSITIVE",
    "token_actual_24h_pct": 14.2,
    "was_token_direction_correct": true,
    "notes": "Athlete modifier slightly overestimated — opposition defence not modelled"
  }
}
```

### What to calibrate first

```
HIGHEST CALIBRATION VALUE (most impactful on output accuracy):
  1. Athlete availability modifier weights (CONFIRMED vs PROBABLE vs DOUBT)
     — small changes here have large downstream effects
  2. Narrative momentum modifier values (are +6% values empirically correct?)
  3. Competition tier signal weights (is UCL vs League weight differential right?)
  
MODERATE CALIBRATION VALUE:
  4. Congestion modifier tier thresholds (are 7-day/12-day boundaries correct?)
  5. Weather modifier values (sport-specific; check empirically per sport)
  
LOW CALIBRATION VALUE (set correctly by design):
  6. Source reliability tiers (these are qualitative; hard to calibrate)
  7. Macro cycle modifiers (driven by market conditions; not sport-specific)
```

---

*See `examples/worked-scenarios/` for complete historical examples showing
SportMind output applied to real events with calibration analysis.*

*MIT License · SportMind · sportmind.dev*

---

## 7. Production deployment patterns

### The three agent patterns

Before building, identify which pattern you are implementing:

```
PATTERN 1 — SINGLE-SPORT SPECIALIST:
  Scope: One sport, one token ecosystem
  Example: Football fan token signal agent
  Complexity: LOW — start with agent-prompts/agent-prompts.md → Prompt 1 or 7

PATTERN 2 — MULTI-SPORT ROUTER:
  Scope: Multiple sports; agent routes to correct skill combination per query
  Example: Prediction market agent covering football, MMA, basketball, cricket
  Complexity: MEDIUM — start with Prompt 3 + routing logic in section 3 above

PATTERN 3 — COMMERCIAL INTELLIGENCE PLATFORM:
  Scope: Full five-layer analysis; fan token commercial intelligence; DeFi context
  Example: Club/agent/brand strategy tool
  Complexity: HIGH — start with Prompt 4 (commercial) + Prompt 8 (DeFi)
```

### The 72h pre-match intelligence chain

```
T−72h: Macro check + Market + Sport domain
  → Store: macro_state, market_tier, competition_context
  → Purpose: Establish baseline; catch macro overrides early

T−24h: Athlete intelligence + Injury check
  → Store: athlete_modifier_early, injury_flags, squad_status
  → Purpose: First lineup intelligence; injury report window opens
  → Conditional: If injury_flag → load injury-intelligence for sport
  → Conditional: If weather-sensitive → load core-weather-match-day.md

T−3h: Final lineup + Liquidity check (if token work)
  → Store: athlete_modifier_final, weather_modifier, tvl_check
  → Purpose: Lineup confirmation; final modifier calculation
  → Rule: If lineup_unconfirmed at T−2h → recommended_action = WAIT

T−0: Execute final confidence output
  → Check: If lineup_unconfirmed + injury_warning both TRUE → ABSTAIN
  → Check: If liquidity_critical → cap position regardless of signal

T+0 to T+48h: Post-event calibration
  → Store actual result + actual token movement
  → Flag any modifier components that were directionally wrong
```

### Additional edge cases

```
EDGE CASE 7 — DLS event in cricket mid-match:
  Rain interrupts; DLS target set
  Agent rule: Pre-match analysis is SUPERSEDED (not updated — fully replaced)
  Recalculate: new_scoring_rate = revised_target / remaining_overs
  Apply dew modifier if batting team is batting second
  Output a NEW post-DLS confidence object; do not average with pre-match
  See: examples/worked-scenarios/scenario-ipl-dls-2023.md

EDGE CASE 8 — Context window overflow:
  All required skills exceed context limit
  Priority loading order (most → least important):
    1. core/confidence-output-schema.md (always)
    2. core/core-athlete-modifier-system.md (always)
    3. sports/{sport}/sport-domain-{sport}.md (always)
    4. athlete/{sport}/ (almost always)
    5. core/core-signal-weights-by-sport.md (recommended)
    6. macro overview (abbreviated to active events only)
    7. market context (abbreviated to tier + key facts)
    8. injury intelligence (only when injury flag active)
    9. fan token Layer 3 (load last; only for active token work)
  
  Summarisation rule: Keep all quantitative tables and modifier values.
  Numbers matter more than prose for agent reasoning.
```

### Production deployment checklist

Before going live:

```
DATA PIPELINE:
  □ Live signal data source connected and tested
  □ Live lineup/injury data source connected
  □ Live BTC/CHZ price feed for macro_modifier
  □ LP TVL API connected if using DeFi context (GeckoTerminal)
  □ Fallback source identified for each primary

AGENT CONFIGURATION:
  □ Context window budget calculated for each deployment tier
  □ Skill loading order implemented correctly (macro→market→domain→athlete→L3→modifiers)
  □ Session state object stores macro_state, active_analyses, calibration_log
  □ All 8 edge cases handled with explicit code paths
  □ Calibration log writes after every completed analysis

TESTING:
  □ Run against all 5 worked scenarios; outputs should match scenario outputs
  □ Test: lineup never confirmed → WAIT or ABSTAIN produced
  □ Test: macro event mid-session → modifier recalculated
  □ Test: liquidity_critical flag → position capped regardless of signal score
  □ Test: event postponed → position cleared; new analysis scheduled

OUTPUT:
  □ Agent produces valid SportMind confidence schema JSON
  □ Schema validator passes (see core/confidence-output-schema.md for Python validator)
  □ All required fields present; flags object populated

CALIBRATION:
  □ Calibration data structure implemented
  □ Actual results pipeline feeds calibration log
  □ First calibration review scheduled after 25 events per sport
```
