# App 2 — Fan Token Portfolio Intelligence

**A contextual intelligence layer for fan token holders — explaining portfolio movements,
surfacing upcoming signal events, and providing lifecycle-aware reasoning for each token.**

---

## The problem this solves

Fan token platforms show price movements. They do not explain them. A holder watching
their $PSG token move 8.2% in a day sees a number — not the UCL Quarter-Final result
that drove it, not the NCSI spillover from the French national team's qualifying run,
not the fact that the macro_modifier is currently 1.00 (neutral) meaning this is a
genuine sporting signal and not a crypto-cycle artefact.

The absence of context produces two bad outcomes: holders panic-sell on normal signal
events they don't understand, and holders miss genuine entry opportunities because they
can't distinguish signal from noise.

SportMind already contains everything needed to explain these movements. This application
surfaces that explanation automatically.

---

## Target users

**Primary:** Existing fan token holders on Socios/Chiliz who want to understand their
portfolio beyond raw price data.

**Secondary:** Fan token platforms (Socios, Binance Fan Tokens) looking to increase holder
retention through contextual intelligence.

**Tertiary:** Sports journalists and analysts covering the fan token market.

---

## Core value proposition

> *"Your $PSG token rose 8.2% today. Here's exactly why, what comes next, and what
> would need to happen for it to move further."*

The SportMind lifecycle skill is the core differentiator. A token in Phase 3 (plateau)
with a declining HAS score and a competition exit produces a different narrative than
a token in Phase 1 (launch) with the same percentage move. Generic portfolio trackers
cannot distinguish these; SportMind can.

---

## SportMind skill stack

```
MINIMUM VIABLE STACK (lightweight — runs on token refresh):

1. macro/macro-crypto-market-cycles.md
   → Current phase (BULL/NEUTRAL/BEAR)
   → Is this price move a crypto cycle artefact or genuine sporting signal?

2. fan-token/fan-token-pulse/
   → HAS (Holder Activity Score): are holders engaging or disengaging?
   → TVI (Token Velocity Index): liquidity health
   → Current on-chain state baseline

3. fan-token/{sport}-token-intelligence/
   → Sport-specific signal bridge: FTIS, NCSI, ATM, CTI etc.
   → What events drive this token specifically?

4. fan-token/fan-token-lifecycle/
   → Which lifecycle phase is this token in?
   → LTUI (Lifetime Token Utility Index)
   → Is this token post-partnership? Prediction market utility?

5. sports/{sport}/sport-domain-{sport}.md
   → What events are coming up for this club/franchise?
   → Competition calendar — when are the next signal windows?

EXTENDED STACK (for deep portfolio analysis):

6. fan-token/performance-on-pitch/
   → PI (Performance Index): is on-pitch form supporting the token price?

7. fan-token/athlete-social-activity/
   → SHS, AGI: are key athletes driving social engagement?
   → Crisis early warning for narrative risk

8. core/confidence-output-schema.md
   → Structured output for each token in portfolio

Skills API shortcut:
  GET /skills/fantoken.pulse/content         → On-chain baseline
  GET /skills/fantoken.football-bridge/content → Sport bridge
  GET /skills/fantoken.lifecycle/content     → Lifecycle context
```

---

## Portfolio output format

```json
{
  "portfolio_intelligence": {
    "generated_at": "2026-04-30T08:00:00Z",
    "macro_context": {
      "phase": "NEUTRAL",
      "macro_modifier": 1.00,
      "note": "Neutral crypto cycle — price movements reflect sporting signals"
    },
    "tokens": [
      {
        "symbol": "PSG",
        "price_24h_change_pct": 8.2,
        "sportmind_explanation": {
          "primary_driver": "PSG qualified for UCL Quarter-Final (Tier 2 event, ×1.45 signal weight)",
          "secondary_driver": "Mbappé successor scored decisive goal — ATM signal active",
          "macro_contribution_pct": 0,
          "lifecycle_phase": "ACTIVE_UTILITY",
          "lifecycle_note": "Token in Phase 2 — full partnership utility active. Price moves reflect genuine sporting events."
        },
        "upcoming_events": [
          {
            "event": "UCL Quarter-Final Draw",
            "date": "2026-05-03",
            "signal_weight": "MEDIUM",
            "historical_range": "+3% to +12% depending on opponent tier"
          },
          {
            "event": "UCL Quarter-Final First Leg",
            "date": "2026-05-08",
            "signal_weight": "HIGH",
            "note": "Tier 2 event. Load full 5-layer analysis 48h before."
          }
        ],
        "has_score": 72.4,
        "tvi": 0.84,
        "recommendation": "HOLD — event signal active. Monitor lineup confirmation T-2h before QF."
      }
    ]
  }
}
```

---

## Agent system prompt

```
You are a fan token portfolio intelligence agent powered by SportMind.

Your role is to provide contextual explanations for fan token portfolio movements
and surface upcoming signal events. You are not a financial advisor — you explain
what is happening and why, using SportMind's structured intelligence.

FOR EACH TOKEN IN THE PORTFOLIO:

1. MACRO CHECK — Is the price move driven by crypto cycle or sporting signal?
   If macro_modifier ≠ 1.00: note the macro contribution to the movement
   "This move is partly a crypto cycle effect (macro_modifier: 0.75)"

2. ON-CHAIN CONTEXT — What does holder behaviour show?
   HAS declining: "Holder engagement is weakening — watch for further moves"
   HAS increasing: "Holders are accumulating around this event"
   TVI low: "Liquidity is thin — price moves amplified by low volume"

3. SPORTING TRIGGER — What happened and how does SportMind weight it?
   Identify the event, apply the competition tier weight, name the signal
   "PSG qualified for UCL QF — Tier 2 event, historical range +5 to +15%"

4. LIFECYCLE PHASE — Is this token in healthy utility phase?
   Phase 1 (Launch): price driven by novelty and speculation
   Phase 2 (Active utility): price reflects sporting performance
   Phase 3 (Plateau): engagement declining; sporting signal weakening
   Post-partnership: prediction market utility applies; different framework

5. UPCOMING EVENTS — What matters next?
   List next 3 signal events with estimated weight and historical range
   Always note lineup confirmation timing for team sports

TONE: Informative, not alarmist. Explain the signal; do not recommend specific
financial actions. Always note when SMS is below 60 (incomplete intelligence).
```

---

## Platform integrations

### Chiliz/Socios (live token data)

```python
import requests

# Live token data from Chiliz
CHILIZ_API = "https://api.kayen.finance/v1"

def get_portfolio_context(token_symbols: list) -> dict:
    portfolio_data = {}
    
    for symbol in token_symbols:
        # Get on-chain data
        token_data = requests.get(
            f"{CHILIZ_API}/market/{symbol.lower()}",
            headers={"X-API-Key": KAYEN_API_KEY}
        ).json()
        
        # Get SportMind intelligence for this sport
        sport = TOKEN_TO_SPORT_MAP.get(symbol)
        if sport:
            stack = requests.get(
                f"http://localhost:8080/stack?use_case=commercial_brief&sport={sport}"
            ).json()
            
            portfolio_data[symbol] = {
                "live_data": token_data,
                "sportmind_context": stack,
                "macro_modifier": get_macro_modifier()
            }
    
    return portfolio_data
```

### Push notification integration

```python
# Alert holders when a significant signal event is imminent

def check_upcoming_signals(portfolio: list, lookahead_hours: int = 48) -> list:
    alerts = []
    
    for token in portfolio:
        sport = TOKEN_TO_SPORT_MAP.get(token["symbol"])
        calendar_skill = requests.get(
            f"http://localhost:8080/skills/domain.{sport}/content"
        ).json()
        
        # Parse upcoming events from skill content
        upcoming = parse_signal_calendar(calendar_skill["content"], lookahead_hours)
        
        for event in upcoming:
            if event["signal_weight"] in ("HIGH", "VERY_HIGH"):
                alerts.append({
                    "token": token["symbol"],
                    "event": event["name"],
                    "date": event["date"],
                    "message": f"High-signal event in {event['hours_away']}h: {event['name']}"
                })
    
    return alerts
```

---

## Lifecycle-aware intelligence example

```
TOKEN: $CITY (Manchester City)
CURRENT PHASE: Phase 2 — Active Utility

RECENT MOVE: -12.4% (last 7 days)

SPORTMIND EXPLANATION:
  Primary driver: Treble defence campaign ended — UCL exit in Round of 16
  Signal type: Tier 2 competition exit (×0.65 negative signal weight)
  Macro contribution: 0% (neutral cycle — move reflects sporting event)
  
  LIFECYCLE CONTEXT: Token is in Active Utility phase. This type of price
  move (competition exit) is expected and structural — it is not a sign
  of token ecosystem breakdown. Historical pattern: $CITY recovers 60-70%
  of competition exit losses within 8-12 weeks as Premier League title race
  enters its signal window.

UPCOMING EVENTS THAT MATTER:
  1. Premier League title decider (Est. 6 weeks) — HIGH signal
     Historical range: +8% to +18% if City win title
  2. New season kit reveal (July) — MEDIUM signal (+2-4% engagement spike)
  3. Pre-season summer signings (July-August) — transfer signal events

RECOMMENDATION: No action needed based on this move alone. Monitor
Premier League title positioning and set alert for T-48h before
title-relevant matches.
```

---

## References

- `fan-token/fan-token-pulse/` — HAS and TVI on-chain baseline
- `fan-token/fan-token-lifecycle/` — Six-phase model and LTUI
- `fan-token/football-token-intelligence/` — FTIS, NCSI, ATM
- `macro/macro-crypto-market-cycles.md` — Crypto cycle context
- `platform/integration-partners.md` — Chiliz/Socios API integration
- `agent-prompts/agent-prompts.md` — Prompt 4 (commercial intelligence agent)

*MIT License · SportMind · sportmind.dev*
