# App 1 — Decentralised Sports Prediction Finance

**A SportMind-powered prediction market that publishes structured intelligence signals
before market open, routes execution through Azuro, and settles on-chain.**

---

## The problem this solves

Existing on-chain prediction markets treat all events as equal-probability until
market prices converge. A SportMind-powered market changes this: it publishes a
structured confidence signal *before* market open — not just a probability but
a full SportMind output with adjusted_score, SMS, active flags, and modifier
breakdown. This gives participants information that generic prediction platforms
don't provide.

The critical innovation is signal separation. The UFC 281 / FTX case study in
SportMind's calibration data demonstrates this precisely: the correct fight
prediction was simultaneously a losing token trade during the extreme crypto bear.
A SportMind-powered platform separates these signals by design. Prediction market
participants see one output; fan token holders see another. The macro modifier is
applied explicitly, not silently absorbed into a price.

---

## Target users

**Primary:** Prediction market participants who want structured pre-match intelligence
rather than raw statistics or crowd-sourced odds.

**Secondary:** Sports organisations and fan token platforms looking to add a prediction
layer to their existing token ecosystem.

**Tertiary:** DeFi developers building sports-adjacent liquidity products who need
reliable pre-match signal generation.

---

## Core value proposition

> *"SportMind tells you what it knows, how confident it is, and why — before the market
> opens. No other prediction platform exposes its reasoning."*

The SMS (SportMind Score) is the differentiator. When an application publishes a signal
with SMS 87 vs SMS 52, participants can immediately assess not just the direction of
the signal but the quality of the intelligence behind it. This is not available in any
existing prediction market.

---

## SportMind skill stack

```
LOADING ORDER (follows SportMind recommended order):

1. macro/macro-overview.md
   → Is there an active macro event overriding all signals?
   → Apply macro_modifier before any sport-specific analysis

2. platform/live-signals.md (Category 1 — macro state)
   → Fetch platform/macro-state.json for current BTC cycle phase

3. market/market-{sport}.md
   → What is the fan token readiness tier for this sport?
   → Commercial context for signal weighting

4. sports/{sport}/sport-domain-{sport}.md
   → Event playbook for this match type
   → Competition tier weight (UCL Final vs regular season)

5. athlete/{sport}/athlete-intel-{sport}.md
   → Player availability and form
   → Composite modifier (0.55–1.25×)

6. fan-token/{sport}-token-intelligence/
   → Sport-specific signal bridge (FTIS, NCSI, ATM etc.)
   → Only for Tier 1 sports with active tokens

7. fan-token/defi-liquidity-intelligence/
   → TVL check — is there sufficient liquidity to execute?
   → Slippage estimate for intended position size
   → LP activity signal (leading indicator)

8. core/confidence-output-schema.md
   → Produce standardised output including sportmind_score

Skills API shortcut:
  GET /stack?use_case=fan_token_tier1&sport=football
  Returns all skills in correct loading order, ready for injection.
```

---

## Signal output architecture

```json
{
  "sportmind_prediction": {
    "event_id": "ucl-semi-final-2026-psg-vs-arsenal",
    "generated_at": "2026-04-30T10:00:00Z",
    "market_open_at": "2026-04-30T18:00:00Z",
    "signal": {
      "direction": "HOME",
      "adjusted_score": 71.4,
      "confidence_tier": "MEDIUM",
      "recommended_action": "ENTER"
    },
    "sportmind_score": {
      "sms": 84.2,
      "sms_tier": "HIGH_QUALITY",
      "layers_loaded": [1, 2, 3, 4, 5]
    },
    "modifiers": {
      "athlete_modifier": 0.94,
      "macro_modifier": 1.00,
      "composite_modifier": 0.94,
      "flags": {
        "lineup_unconfirmed": true,
        "macro_override_active": false,
        "liquidity_warning": false
      }
    },
    "defi_context": {
      "pool_tvl_usd": 2400000,
      "estimated_slippage_1k": 0.21,
      "lp_activity_signal": "NEUTRAL"
    },
    "reasoning_summary": "PSG home in UCL SF. Mbappe successor confirmed fit (×0.94 due to back concern). UCL SF weight ×0.88. Macro neutral. DeFi: sufficient liquidity for standard positions. WAIT for lineup confirmation before full entry.",
    "agent_recommendation": "ENTER at 40% standard size pending lineup confirmation. Full entry if lineup_unconfirmed clears by T-2h."
  }
}
```

---

## Platform integrations

### Azuro (prediction market execution)

```python
# SportMind provides the intelligence; Azuro executes the market

import requests

# 1. Get SportMind signal
sportmind_signal = requests.post("http://localhost:8080/stack", json={
    "use_case": "fan_token_tier1",
    "sport": "football",
    "event_id": "ucl-semi-final-2026-psg-vs-arsenal"
}).json()

sms = sportmind_signal["sportmind_score"]["sms"]
direction = sportmind_signal["signal"]["direction"]
action = sportmind_signal["signal"]["recommended_action"]

# 2. Only proceed if SMS >= 60 and action is ENTER
if sms >= 60 and action == "ENTER":
    # 3. Check DeFi liquidity before execution
    tvl = sportmind_signal["defi_context"]["pool_tvl_usd"]
    slippage = sportmind_signal["defi_context"]["estimated_slippage_1k"]
    
    if slippage < 0.03:  # Under 3% slippage threshold
        # 4. Execute via Azuro protocol
        azuro_client.place_bet(
            event_id=event_id,
            outcome=direction,
            amount=calculate_position_size(sms, slippage),
            odds=azuro_client.get_odds(event_id, direction)
        )
    else:
        log("Slippage exceeds threshold — ABSTAIN")
else:
    log(f"Signal quality insufficient: SMS={sms}, action={action}")
```

### Chiliz Chain (on-chain settlement for token markets)

```python
# For fan token-specific prediction markets settling on Chiliz Chain

from web3 import Web3

chiliz_w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/chiliz"))

# SportMind output → on-chain signal publication
def publish_signal_on_chain(sportmind_output: dict, contract_address: str):
    signal = sportmind_output["signal"]
    sms = sportmind_output["sportmind_score"]["sms"]
    
    # Pack signal data for on-chain publication
    signal_data = {
        "adjusted_score": int(signal["adjusted_score"] * 100),  # scaled integer
        "sms": int(sms * 100),
        "direction": 1 if signal["direction"] == "HOME" else 2,  # 1=home, 2=away
        "flags": encode_flags(sportmind_output["modifiers"]["flags"]),
        "timestamp": int(datetime.now().timestamp())
    }
    
    # Write to prediction market contract
    contract = chiliz_w3.eth.contract(address=contract_address, abi=PREDICTION_ABI)
    tx = contract.functions.publishSignal(**signal_data).build_transaction({...})
    # sign and send...
```

---

## Agent system prompt

```
You are a decentralised sports prediction finance agent powered by SportMind.

Your role is to generate structured pre-match signals for prediction market participants.
You provide intelligence and reasoning — you do not execute trades directly.

OPERATING PROTOCOL:

1. PRE-ANALYSIS CHECKS (run before every signal generation):
   a. Fetch macro-state.json — apply macro_modifier to all signals
   b. Verify lineup confirmation status (T-2h threshold)
   c. Check DeFi liquidity (TVL and slippage estimate)
   
2. SIGNAL GENERATION (follows SportMind loading order):
   Load: macro → market → domain → athlete → fan-token bridge → DeFi
   Compute: adjusted_score, composite_modifier, SportMind Score (SMS)
   
3. SIGNAL PUBLICATION RULES:
   SMS ≥ 80: Publish HIGH_QUALITY signal — full confidence output
   SMS 60–79: Publish GOOD signal — note specific gaps
   SMS < 60: Do NOT publish — insufficient intelligence; return INSUFFICIENT_DATA
   
4. SEPARATION OF SIGNALS:
   Prediction market signal: based on sporting outcome probability
   Fan token signal: includes macro_modifier and DeFi context
   NEVER conflate these — a winning prediction can be a losing token trade
   (see: UFC 281 / FTX case study in calibration records)

5. OUTPUT FORMAT:
   Always produce: direction, adjusted_score, sms, sms_tier, active_flags,
   reasoning_summary (max 3 sentences), agent_recommendation

CONFIDENCE TIER MAPPING TO POSITION SIZE:
  HIGH (SMS ≥ 80): 100% standard position
  GOOD (SMS 60–79): 65% standard position
  MEDIUM confidence_tier: 50% standard position
  LOW confidence_tier: Do not enter
  lineup_unconfirmed flag: Halve position size until confirmed
```

---

## Key differentiators vs existing platforms

| Feature | Generic prediction market | SportMind-powered market |
|---|---|---|
| Pre-market signal | None or basic statistics | Structured SMS with modifier breakdown |
| Macro context | Not applied | Explicit macro_modifier in every output |
| Signal quality disclosure | Hidden | SMS published with every signal |
| DeFi execution check | Not integrated | TVL/slippage check before every entry |
| Prediction vs token separation | Conflated | Explicitly separated |
| Reasoning transparency | None | Full reasoning_summary published |

---

## Regulatory note

On-chain prediction markets operate under different regulatory frameworks in different
jurisdictions. Before deploying this application:
- Review the legal status of prediction markets in your target market
- Fan tokens and sports betting are regulated differently in most jurisdictions
- Azuro protocol documentation includes compliance guidance for their integration

*SportMind provides intelligence only. The application operator is responsible for
regulatory compliance in all jurisdictions where the application operates.*

---

## References

- `fan-token/defi-liquidity-intelligence/` — DeFi and liquidity pool intelligence
- `platform/integration-partners.md` — Azuro and Chiliz integration details
- `core/confidence-output-schema.md` — Standard output format
- `core/sportmind-score.md` — SMS calculation and interpretation
- `community/calibration-data/mma/2022/11/ufc-281-2022-11-12-outcome.json` — Signal separation case study
- `agent-prompts/agent-prompts.md` — Prompt 8 (DeFi-aware agent)

*MIT License · SportMind · sportmind.dev*
