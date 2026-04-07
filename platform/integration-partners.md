# SportMind Platform — Integration Partners

Registry of how external systems connect to SportMind intelligence.
Each entry documents: what the partner provides, what SportMind provides,
how they map to each other, and the integration pattern.

**Governing principle:** SportMind is the intelligence and reasoning layer.
Partners provide data, infrastructure, or distribution. The division of
responsibility is always: your data + SportMind reasoning = better decisions.

---

## Integration architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    EXTERNAL DATA PROVIDERS                           │
│  FanTokenIntel · CoinGecko · Chiliz Chain · ESPNcricinfo · etc.     │
│                    (provide raw signals and data)                    │
└──────────────────────────────┬──────────────────────────────────────┘
                               │  base_score, on-chain data, 
                               │  player data, market prices
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    SPORTMIND INTELLIGENCE LAYER                      │
│  Five-layer reasoning: sport domain → athlete → fan token →          │
│  market → macro. Modifier pipeline. Confidence output schema.        │
│  (interprets, contextualises, and adjusts the raw signals)           │
└──────────────────────────────┬──────────────────────────────────────┘
                               │  adjusted_score, confidence_tier,
                               │  modifiers_applied, flags, reasoning
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    AGENT / DEVELOPER PRODUCTS                        │
│  Fan token platforms · Prediction markets · GameFi ·                 │
│  Commercial intelligence tools · Sports analytics                    │
│  (build products on top of the combined signal)                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Partner 1 — Fan Token Intel (primary signal partner)

**URL:** fantokenintel.com
**Role:** Primary sports signal data provider for Tier 1 fan token markets
**Relationship type:** Data-in / Intelligence-out

### What FanTokenIntel provides to SportMind

```
DATA INPUTS:
  base_score:       Raw composite signal score (0–100) for a token/event
  whale_flows:      Institutional buy/sell ratio and bracket classification
  sell_ratio_brackets: Historical win-rate by sell ratio range
  signals_active:   Current active signals with confidence level
  prematch_alpha:   Pre-match intelligence packets
  match_results:    Post-match result data for calibration
  sports_calendar:  Upcoming events with token relevance
  historical_patterns: Backtest data for strategy validation
```

### What SportMind provides to FanTokenIntel

```
INTELLIGENCE OUTPUTS:
  Athlete modifier:     Adjusts FTI's base_score for player availability/form
  Sport domain context: Interprets why signals are strong/weak for this sport
  Competition weighting: Tells agents which events warrant higher signal weight
  Macro overlay:        Applies CHZ bear/bull market multiplier to FTI scores
  Lifecycle phase:      Tells agents whether to apply full Layer 3 or reduced weight
  DeFi context:         Adds liquidity check before FTI signal triggers action
```

### Integration mapping

| FanTokenIntel tool | SportMind skill | What SportMind adds |
|---|---|---|
| `signals_active(token)` | `signal.full` | Domain context + athlete modifier + macro check |
| `whale_flows(token)` | `sports/{sport}/sport-domain` | When whale signals are most reliable for this sport |
| `prematch_alpha` | `athlete/{sport}/athlete-intel` | Player availability overlay |
| `match_results` | `core/core-result-impact-matrices.md` | Expected range validation |
| `autopilot_start` | `modifier.athlete` | Athlete-aware autopilot gate |
| `signals_active.score` | `modifier.macro` | Macro multiplier applied to score |

### Integration code pattern

```python
# FTI provides the base signal
fti_signal = fti.signals_active(token="BAR", min_confidence=0.6)
base_score = fti_signal.score  # e.g. 72

# SportMind interprets and adjusts
sm_response = sportmind.call({
    "skill": "signal.full",
    "sport": "football",
    "context": {
        "event_id": fti.next_event(token="BAR").id,
        "token_symbol": "BAR"
    },
    "inputs": {
        "base_score": base_score,
        "trade_size_usd": intended_position
    }
})

# Combined decision
final_score  = sm_response["signal"]["adjusted_score"]
action       = sm_response["sizing"]["recommended_action"]
modifier     = sm_response["modifiers_applied"]["composite_modifier"]

# FTI whale validation gate (always run after SportMind adjustment)
if action == "ENTER":
    whale = fti.analytics(metric="sell_ratio_brackets", token="BAR")
    if whale.bracket not in VALID_BRACKETS:
        action = "WAIT"  # whale validation overrides
```

### Autopilot template (athlete-aware)

```json
{
  "template_id": "sportmind_athlete_aware_matchday",
  "description": "FTI autopilot with SportMind athlete modifier and DeFi gate",
  "params": {
    "sport": "football",
    "sportmind_contracts": ["modifier.athlete", "modifier.macro", "modifier.defi"],
    "entry_timing": "-2h",
    "exit_timing": "fulltime",
    "min_sportmind_adjusted_score": 68,
    "require_lineup_confirmed": true,
    "require_liquidity_warning_false": true,
    "max_congestion_modifier": 0.95,
    "whale_bracket_required": ["0.68-0.70", "0.75-0.80"],
    "position_size_pct_at_2h": 60,
    "position_size_pct_at_lineup": 40
  }
}
```

---

## Partner 2 — Chiliz / Socios (blockchain infrastructure)

**URL:** chiliz.com · socios.com
**Role:** Fan token blockchain platform and primary on-chain data source
**Relationship type:** Infrastructure provider

### What Chiliz/Socios provides to SportMind

```
ON-CHAIN DATA:
  Token holder counts and distribution (by country, wallet size)
  Voting event history and participation rates
  Partnership announcements and utility event calendar
  Validator registry (for blockchain-validator-intelligence.md)
  CHZ price and market data
  Fan token contract addresses (for DEX pool lookup)
  
SOCIOS PLATFORM DATA:
  Active token list with partnership status
  Utility event frequency data (UEF component of PHS)
  Club social promotion activity
```

### SportMind Layer 3 skills powered by Chiliz data

```
fan-token/fan-token-pulse/              HAS, TVI from on-chain holder data
fan-token/fan-token-lifecycle/          Phase determination from on-chain activity
fan-token/fan-token-partnership-intel/  PHS from utility event and holder data
fan-token/blockchain-validator-intel/   VSI from Chiliz Chain validator registry
fan-token/defi-liquidity-intel/         DEX pool data via Chiliz DEX subgraph
```

### Integration data sources

```
Chiliz Chain explorer:  explorer.chiliz.com
Chiliz Chain RPC:       rpc.ankr.com/chiliz
Validator registry:     explorer.chiliz.com/validators
DEX pool data:          chiliz.net/dex (Chiliz DEX) + GeckoTerminal
Socios utility events:  socios.com (partner content)
```

### Notes for developers

```
IMPORTANT: SportMind uses Chiliz data to REASON about tokens.
It does not replicate or redistribute Chiliz's proprietary data.
Developers accessing on-chain data directly must comply with
Chiliz Chain's terms of service.

SportMind's Layer 3 intelligence is built on top of publicly
available on-chain data (blockchain is public by design) and
publicly announced partnership information.
```

---

## Partner 3 — Azuro (prediction market infrastructure)

**URL:** azuro.org
**Role:** Sports prediction market protocol
**Relationship type:** DeFi intelligence consumer

### What Azuro provides to SportMind

```
PREDICTION MARKET DATA:
  Pool TVL per market (match outcome, total goals, etc.)
  Implied odds from pool state
  Liquidity provision activity (LP additions/removals)
  Sports data feed (Chainlink oracle integration)
```

### What SportMind provides to Azuro integrations

```
INTELLIGENCE FOR AZURO BUILDERS:
  Sport domain context:  Which sporting factors affect prediction pool pricing
  Athlete modifier:      Adjust position size in Azuro pools based on player news
  Narrative momentum:    High-narrative events generate larger Azuro pool activity
  Macro modifier:        Crypto market conditions affect LP willingness in Azuro
  Lifecycle context:     Non-contractual tokens → Azuro is primary utility venue
```

### Integration pattern for Azuro builders

```python
# Azuro provides pool data
pool = azuro.get_market(event_id="UCL_FINAL_2026")
pool_tvl = pool.liquidity_usd           # e.g. $2.1M
implied_odds = pool.get_odds("HOME")    # e.g. 1.85

# SportMind adds sport intelligence
sm = sportmind.call({
    "skill": "signal.domain",
    "sport": "football",
    "context": {"event_id": "UCL_FINAL_2026"},
    "inputs": {"base_score": odds_to_score(implied_odds)}
})

# Use SportMind's modifier to adjust LP position sizing
if sm["flags"]["liquidity_warning"]:
    # Pool is thin — LP position generates high fees but high risk
    lp_position_size = standard_size * 0.40
else:
    lp_position_size = standard_size * sm["modifiers_applied"]["composite_modifier"]
```

---

## Partner 4 — Sports data providers (Opta / Stats Perform / Sportradar)

**URL:** statsperform.com · sportradar.com
**Role:** Licensed professional sports statistics providers
**Relationship type:** Data-in for athlete intelligence

### What these providers supply

```
LICENSED SPORTS DATA:
  Player availability and injury status (real-time)
  Live match statistics (xG, shots, possession, etc.)
  Historical player performance data
  Official team lineup data (T-60min releases)
  Competition fixtures, results, and standings
```

### How SportMind uses this data

```
Layer 2 athlete skills are the primary consumers:
  Availability modifier:    Real-time injury/availability status
  Form modifier:            Rolling performance statistics
  Lineup confirmation:      Official team sheet data (×1.15 modifier)
  H2H matchup modifier:     Historical head-to-head data

SportMind documents what DATA to retrieve and HOW TO INTERPRET it.
The actual data retrieval requires a licensed API subscription.
SportMind's core/data-sources.md lists the recommended providers.
```

### Notes for developers

```
SportMind is platform-agnostic on data providers.
The same SportMind reasoning framework works with:
  - Opta data  →  higher quality; licensed; recommended for production
  - FBref data →  free; community-maintained; good for prototyping
  - Manual inputs → for testing; use testing-scenarios.md inputs

The athlete modifier value is the same regardless of which provider
supplies the underlying data — SportMind's reasoning is the constant.
```

---

## Partner 5 — DeFi data providers (DeFiLlama / GeckoTerminal)

**URL:** defillama.com · geckoterminal.com
**Role:** DeFi pool and on-chain financial data
**Relationship type:** Data-in for DeFi intelligence

### What these providers supply

```
DEFI DATA:
  Pool TVL by token pair (real-time)
  LP add/remove transaction history
  Price impact estimates by trade size
  APR/APY for liquidity provision
  Protocol-level TVL trends
```

### How SportMind uses this data

```
defi-liquidity-intelligence.md consumes:
  pool_tvl_usd:              Primary liquidity check input
  lp_activity_signal:        Derived from add/remove transaction history
  estimated_slippage_pct:    Calculated from pool depth
  yield_apr_pct:             LP provision incentive signal

API integration:
  GeckoTerminal API:  geckoterminal.com/api — real-time pool data (free tier)
  DeFiLlama API:      defillama.com/api — TVL history (free, open)
  
Agents call modifier.defi which pulls from these sources automatically.
Developers can also supply pool_tvl_usd directly to skip the API call.
```

---

## Partner 6 — LLM providers (Claude / GPT / Gemini / open source)

**URL:** anthropic.com · openai.com · deepmind.google · huggingface.co
**Role:** Agent reasoning engines
**Relationship type:** Intelligence consumer

### SportMind relationship to LLM providers

```
SportMind is LLM-AGNOSTIC. Every skill file is plain structured markdown.
Every confidence output schema is standard JSON.
Every agent prompt is designed to work with any LLM that accepts system prompts.

TESTED CONFIGURATIONS (from context-window-management.md):
  Claude 3.5 Sonnet:   200k context; recommended for full 5-layer analysis
  GPT-4o:              128k context; recommended for single-sport deep analysis
  Gemini 1.5 Pro:      1M context; can load full library simultaneously
  Llama 3 (70B):       8k context; sport domain skill only
  Local models:        4k context; minimum viable single skill

SPORTMIND ADDS NO LLM-SPECIFIC DEPENDENCIES.
A developer switching from Claude to GPT to Gemini needs to change only
their API keys — not their SportMind integration.
```

---

## Partner 7 — SportFi Kit (fan engagement application toolkit)

**URL:** sportfikit.online · github.com/AltcoinDaddy/Sportfi-kit
**Role:** React/TypeScript developer toolkit for building fan engagement dApps on Chiliz Chain
**Relationship type:** Application layer that SportMind intelligence powers
**License:** MIT (same as SportMind — fully open integration)

### What SportFi Kit is

SportFi Kit is a specialised development suite for building fan engagement applications
on the Chiliz Chain. It describes itself as "the missing bridge between the Socios.com
ecosystem and the decentralised web."

```
SPORTFI KIT PROVIDES:
  React components and hooks  Fan token balance checks, token transfers,
                              governance voting UI, fan poll interfaces
  Smart contracts (Solidity)  Ready-to-deploy P2P wagering and prediction contracts
                              on Chiliz Chain — trustless, verified on-chain settlement
  Environment detection       Automatic UI adjustment for Socios.com Wallet Browser
                              and Telegram Mini Apps — reaches fans where they are
  CLI scaffolding             Spin up new sports dApps in seconds using
                              high-fidelity production-ready templates
  Token-gating primitives     Access control based on fan token holdings
```

**Tech stack:** TypeScript (80%), Solidity (3%), React + Tailwind CSS, npm monorepo

### The relationship to SportMind

SportFi Kit and SportMind operate at completely different levels of the stack
and do not overlap. The relationship is precise and complementary:

```
LAYER SEPARATION:

  SportMind           Intelligence layer — reasoning, context, signal generation
                      "What does this event mean? How confident are we? Why?"

  SportFi Kit         Application layer — UI components, wallet integration,
                      on-chain execution
                      "How do we build the product? How do we reach the user?"

  Together            A developer uses SportFi Kit to build the application shell,
                      then calls SportMind to provide the intelligence that powers
                      the decisions and displays within that shell.

NO CONFLICTS:
  Both are MIT licensed
  Both are open source
  Neither requires commercial agreement to use together
  SportMind adds no SportFi Kit-specific dependencies
  SportFi Kit adds no SportMind-specific dependencies
  A developer can use either independently or both together
```

### What SportFi Kit provides to SportMind applications

```
TOKEN-GATING:
  Check whether a user holds a specific fan token before granting access
  SportMind use case: Gate portfolio intelligence (App 2) to token holders only
  
  import { useFanToken } from '@sportfi-kit/core'
  const { balance, isHolder } = useFanToken({ symbol: 'PSG' })

P2P WAGERING CONTRACTS:
  Deploy trustless prediction contracts on Chiliz Chain
  SportMind use case: The settlement layer for the DeFi prediction market (App 1)
  SportFi Kit handles the contract; SportMind provides the pre-match signal

SOCIOS WALLET + TELEGRAM INTEGRATION:
  Auto-detects Socios.com Wallet Browser and Telegram Mini App environments
  SportMind use case: Portfolio intelligence (App 2) reaches users inside Socios app
  without requiring them to leave the platform they already use

CLI SCAFFOLDING:
  npx create-sportfi-app my-fan-app --template predictions
  Generates a production-ready project with SportMind integration hooks
```

### What SportMind provides to SportFi Kit applications

```
PRE-MATCH INTELLIGENCE (for wagering contracts):
  adjusted_score + SMS — structured signal before contract opens
  Modifier breakdown — why the signal is at this level
  Flag states — lineup_unconfirmed, macro_override_active, liquidity_warning
  SportFi Kit handles the contract settlement; SportMind handles what the bet
  should be and whether now is the right time to place it

PORTFOLIO CONTEXT (for token-gated experiences):
  HAS + TVI — current on-chain holder health
  Lifecycle phase — is this token in active utility or post-partnership?
  Upcoming signal calendar — what events matter next for this token
  SportFi Kit gates access by token holding; SportMind explains what that
  token is doing and why

MACRO STATE (for context-aware UI):
  macro_modifier — current crypto cycle phase
  Active events — geopolitical, economic, governance signals
  SportFi Kit can surface this in the UI: "Markets are in a bear cycle —
  your $PSG position context: [SportMind explanation]"

NCSI + FTIS (for live engagement displays):
  Real-time signal for token-relevant sporting events
  SportFi Kit displays the movement; SportMind explains the cause

COMMERCIAL INTELLIGENCE (for athlete/club-facing features):
  ABS, APS, AELS — athlete commercial brief generation
  SportFi Kit provides the UI shell; SportMind provides the metrics
```

### Integration code pattern

```typescript
// SportFi Kit React component + SportMind intelligence
// Example: Pre-match prediction widget powered by SportMind

import { useFanToken, useWager } from '@sportfi-kit/core'

function PreMatchWidget({ eventId, sport }: { eventId: string, sport: string }) {
  const { isHolder } = useFanToken({ symbol: 'PSG' })

  // Fetch SportMind intelligence via Skills API
  const [signal, setSignal] = useState(null)
  useEffect(() => {
    fetch(`http://your-sportmind-api/stack?use_case=fan_token_tier1&sport=${sport}`)
      .then(r => r.json())
      .then(stack => {
        // Extract the signal from the loaded stack
        const macroState = fetch('/macro-state').then(r => r.json())
        setSignal({ stack, macroState })
      })
  }, [eventId, sport])

  // SportFi Kit: token-gate the widget
  if (!isHolder) return <TokenGate symbol="PSG" />

  // SportMind: display the intelligence
  if (!signal) return <Loading />

  const sms = signal.stack.sportmind_score?.sms ?? 0
  const adjustedScore = signal.stack.signal?.adjusted_score ?? 0
  const flags = signal.stack.modifiers?.flags ?? {}

  return (
    <PredictionCard>
      <SignalDisplay score={adjustedScore} sms={sms} />
      <FlagWarnings flags={flags} />
      <WagerButton
        // SportFi Kit: trustless wagering contract
        onWager={(amount) => placeWager({ eventId, amount, direction: 'HOME' })}
        // SportMind: only enable if SMS >= 60
        disabled={sms < 60 || flags.lineup_unconfirmed}
      />
      <SmsSummary>
        {sms >= 80 ? 'High quality intelligence loaded' :
         sms >= 60 ? 'Good intelligence — some gaps remain' :
         'Insufficient intelligence — loading more data'}
      </SmsSummary>
    </PredictionCard>
  )
}
```

### Application blueprints using this integration

All six application blueprints in `examples/applications/` benefit from SportFi Kit:

| Blueprint | SportFi Kit provides | SportMind provides |
|---|---|---|
| App 1 — DeFi Prediction Market | P2P wagering contracts + Chiliz Chain settlement | Pre-match signal, SMS gate, macro modifier |
| App 2 — Portfolio Intelligence | Token-gating, Socios wallet, Telegram integration | HAS/TVI, lifecycle phase, NCSI narrative |
| App 3 — Athlete Commercial | Fan token balance display, token-native activation UI | ABS, APS, AELS, AFS metrics |
| App 4 — Brand Token Strategy | Token launch template, governance vote UI | LTUI modelling, PHS projection |
| App 5 — World Cup Dashboard | Token-gated NCSI display, fan poll integration | NCSI live tracker, FTIS, tournament calendar |
| App 6 — GameFi Layer | On-chain scoring contracts, pick submission UI | SMS-weighted scoring, flag-aware locking |

### Application blueprint reference

For the full 7-application mapping table showing SportFi Kit + SportMind split per
application, see:
`examples/applications/app-07-sportfi-kit-integration.md`

| Blueprint | SportFi Kit | SportMind |
|---|---|---|
| App 1 — DeFi Prediction Market | P2P wagering contracts | Pre-match signal + SMS gate |
| App 2 — Portfolio Intelligence | Token-gating + Socios wallet | HAS/TVI + lifecycle context |
| App 3 — Athlete Commercial | Token-native activation UI | ABS/APS/AELS metrics |
| App 4 — Brand Token Strategy | Token launch + governance UI | LTUI/PHS projections |
| App 5 — World Cup Dashboard | Token-gated NCSI display | NCSI tracker + FTIS |
| App 6 — GameFi Layer | On-chain scoring contracts | SMS-weighted scoring |
| App 7 — Full-Stack Blueprint | All SportFi Kit primitives | All SportMind layers |

### Getting started with the combined stack

```bash
# 1. Scaffold a new sports dApp with SportFi Kit
npx create-sportfi-app my-prediction-app --template predictions

# 2. Start the SportMind Skills API
python scripts/sportmind_api.py --serve --port 8080

# 3. In your SportFi Kit app, call SportMind for intelligence
const stack = await fetch(
  'http://localhost:8080/stack?use_case=fan_token_tier1&sport=football'
).then(r => r.json())

# 4. Use SportFi Kit components with SportMind signal as props
<PredictionWidget signal={stack} sport="football" />
```

---

## Adding a new integration partner

To document a new integration in this registry:

```
REQUIRED INFORMATION:
  1. Partner name, URL, and role description
  2. What data the partner provides to SportMind (as inputs)
  3. Which SportMind skills or contracts consume that data
  4. What SportMind provides back (adjusted signals, intelligence)
  5. A code integration pattern (even pseudocode is sufficient)
  6. Any licensing or access considerations for developers

SUBMIT VIA:
  GitHub Pull Request to platform/integration-partners.md
  Label: integration-partner
  Review: SportMind maintainers verify the integration pattern is correct
  and that SportMind's role (intelligence layer) is accurately described.
  
WHAT WE DON'T ADD:
  Paid or exclusive integration arrangements
  Integrations that restrict SportMind's open access
  Partners whose business model conflicts with open intelligence
  SportMind remains MIT licensed; all integrations documented here are open.
```

---

*This registry documents integrations — it does not imply endorsement, partnership
agreements, or any commercial relationship between SportMind and listed platforms.*

*SportMind is an independent open-source project. It is designed to complement data
platforms and agent frameworks, not to compete with them.*

*MIT License · SportMind · sportmind.dev*
