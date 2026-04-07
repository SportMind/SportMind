# Temporal Awareness — SportMind Information Freshness Model

**Defines what information expires when, how agents should handle stale data,
and how to build production SportMind deployments that stay accurate over time.**

---

## Why temporal awareness matters

SportMind contains information at many different freshness levels. Domain knowledge
about how cricket's dew factor works never expires. A specific player's injury status
changes within hours. The macro_modifier can shift in a day. Getting these freshness
levels confused produces bad analysis — an agent reasoning from a month-old lineup
confirmation as if it were current, or refreshing static domain knowledge every hour
at unnecessary cost.

This document defines SportMind's **information freshness taxonomy** — what expires
when, how agents should detect and handle staleness, and what `platform/live-signals.md`
already covers versus what agents must manage themselves.

---

## The freshness taxonomy

SportMind information falls into six freshness tiers:

### Tier 0 — Permanent (never expires)

*Load once. Never refresh.*

```
WHAT:
  Domain knowledge — how cricket's dew factor works, what a UCL Tier 1 event means,
  why State of Origin disrupts NRL signals, how GSAx is calculated
  Historical calibration records — outcome records in community/calibration-data/
  Library architecture — loading order, skill structure, confidence schema
  Named metrics definitions — HAS, SMS, FTIS, NCSI etc.
  Sport rules and competition format — best-of-7 playoff structure, DLS rules

WHERE IN LIBRARY:
  sports/*/sport-domain-*.md (the reasoning models — not the current data)
  core/calibration-framework.md
  core/confidence-output-schema.md
  core/sportmind-score.md
  fan-token/fan-token-why.md

AGENT RULE:
  Load these once per session (or less — they can be pre-loaded in system prompt).
  Never mark these as stale. Never refresh these mid-session.
```

### Tier 1 — Slow (months)

*Update quarterly or when explicitly changed.*

```
WHAT:
  Commercial tier assessments — is cricket Tier 1 or Tier 2 for fan tokens?
  Market structure — how many clubs have tokens, which sports have active ecosystems
  Athlete career trajectory — DTS (Development Trajectory Score)
  Partnership health scores — PHS at a structural level
  Regulatory framework summaries — India VDA status, UK FCA stance on fan tokens

WHERE IN LIBRARY:
  market/market-*.md (tier assessments and commercial structure)
  fan-token/fan-token-lifecycle/ (LTUI baseline projections)
  fan-token/fan-token-partnership-intelligence/ (structural PHS)

AGENT RULE:
  Flag if last update > 90 days ago.
  Update when SportMind releases a new version that includes market reassessments.
  Do not refresh intra-session — these do not change within a conversation.

STALE SIGNAL:
  "Market tier last assessed: v3.2.0 (90+ days ago)"
  → Flag as potentially stale for commercial brief applications
  → For signal analysis, still valid — tier changes are announced, not silent
```

### Tier 2 — Moderate (weeks)

*Update at season transitions and major news events.*

```
WHAT:
  Team form scores — current season performance rating
  League standings and playoff positioning
  Manager/coach continuity — squad philosophy signals
  Athlete career stage — where in their career arc (peak, decline, emerging)
  Fan token partnership development signals — new Socios signings, new utility

WHERE IN LIBRARY:
  sports/*/sport-domain-*.md (the form-related sections, not the rules)
  athlete/*/athlete-intel-*.md (the modifier tables, not the specific modifiers)
  fan-token/fan-token-lifecycle/ (current phase assessments)

AGENT RULE:
  Update at start of each season and after major news events (manager sackings,
  major signings, relegation/promotion).
  Within a season: form scores degrade ~15% reliability per week without update.
  After 4 weeks without update: apply ×0.85 uncertainty modifier to form-based signals.

STALE FORMULA:
  form_modifier_reliability = 1.00 - (days_since_update / 28) × 0.15
  At 28+ days: form_modifier_reliability = 0.85 (maximum degradation)
```

### Tier 3 — Daily (hours to days)

*Refresh before each significant analysis session.*

```
WHAT:
  Macro state — crypto cycle phase, BTC vs 200-day MA, active macro events
  Competition standings — current league table, playoff bracket
  Injury lists — squad injury status from official club sources
  Transfer window activity — confirmed signings and departures
  Recent on-chain data — HAS (Holder Activity Score) trends

WHERE IN LIBRARY:
  platform/macro-state.json — updated by scripts/update_macro_state.py
  platform/live-signals.md (Category 1: macro state)
  fan-token/fan-token-pulse/ (HAS and TVI current values)

AGENT RULE:
  Refresh macro_state.json every 4-8 hours in production deployments.
  For the MCP server: call sportmind_macro before each analysis session.
  If macro_state.json last_updated > 8 hours ago: add freshness_warning flag.
  
  FRESHNESS WARNING FORMAT:
  "freshness_warning": "Macro state is 12h old — refresh recommended before token decisions"

STALE DETECTION:
  import json
  from datetime import datetime, timezone, timedelta
  
  state = json.load(open("platform/macro-state.json"))
  last_updated = datetime.fromisoformat(state["macro_state"]["last_updated"])
  age_hours = (datetime.now(timezone.utc) - last_updated).total_seconds() / 3600
  
  if age_hours > 8:
      signal["freshness_warning"] = f"Macro state is {age_hours:.0f}h old"
  if age_hours > 24:
      signal["flags"]["macro_state_stale"] = True  # Stronger flag
```

### Tier 4 — Match-day (hours)

*Refresh on match day; critical in the T-2h window.*

```
WHAT:
  Lineup confirmation — starting XI / starting lineup
  Goalkeeper start confirmation (NHL, ice hockey)
  Pitcher start confirmation (MLB)
  Weigh-in result (MMA) — binary pass/fail event
  Weather conditions — rain probability at match venue
  Late injury news — official pre-match fitness tests

WHERE IN LIBRARY:
  platform/live-signals.md (Category 2: match-day inputs)
  The lineup_unconfirmed flag in the confidence output schema

TIMING MODEL:
  T-48h:  Squad announcement (if club publishes — not always)
  T-24h:  Injury list update (official club channels)
  T-4h:   Manager press conference — lineup hints
  T-2h:   CRITICAL WINDOW — lineup confirmation / team sheet
  T-0:    Kickoff

  AGENT RULE: The T-2h window is the single most important
  information update point for match-day signal accuracy.
  
  Before T-2h: set lineup_unconfirmed = True
               apply ×0.85 to position-size recommendation
  After T-2h:  if lineup confirmed → clear flag, full position size
               if key player absent → reload analysis entirely

  SPORT-SPECIFIC TIMING:
    Football:   Team sheet released ~60-75 minutes before kickoff
    NHL:        Morning skate (T-6h) is the goaltender confirmation signal
    MLB:        Lineup posted ~3 hours before first pitch
    MMA:        Weigh-in day before fight; final staredown day of fight
    Cricket:    Toss at match start — dew factor known only post-toss
    F1:         Qualifying (T-24h) locks grid; race-day weather is primary unknown
```

### Tier 5 — Live (minutes)

*Cannot be pre-loaded — must be fetched in real time.*

```
WHAT:
  DeFi pool state — TVL, current token price, slippage estimate
  Live match events — goals, cards, injuries in-play
  Live odds movements — prediction market pricing

WHERE IN LIBRARY:
  platform/live-signals.md (Category 3: real-time inputs)
  fan-token/defi-liquidity-intelligence/ (TVL thresholds — the model is permanent,
  but the actual TVL value must be fetched live)

AGENT RULE:
  SportMind does NOT provide live data — it provides the framework for reasoning
  about live data when it arrives.
  
  The TVL thresholds in defi-liquidity-intelligence are PERMANENT (Tier 0).
  The actual TVL value for a specific pool is LIVE (Tier 5).
  
  An agent must:
  1. Load the threshold model from SportMind (Tier 0 — permanent)
  2. Fetch the current TVL from the Chiliz/KAYEN API (Tier 5 — live)
  3. Apply the model to the live value
  
  SportMind provides step 1. The application provides step 2. The agent does step 3.
  
LIVE DATA SOURCES (see platform/live-signals.md for full list):
  TVL:         https://api.kayen.finance/v1/market/{token_address}
  Token price: https://api.kayen.finance/v1/tokens?chain=chiliz
  Match data:  Club official channels, official league apps
```

---

## Freshness summary table

| Tier | Type | Expires | Where in library | Refresh trigger |
|---|---|---|---|---|
| 0 | Permanent | Never | Domain skills, core schemas, calibration records | Never |
| 1 | Slow | 90 days | Market tier assessments, regulatory summaries | Version update |
| 2 | Moderate | 1-4 weeks | Form scores, standings, career stage | Season transitions, major news |
| 3 | Daily | 4-8 hours | Macro state, injury lists, HAS trends | Scheduled — scripts/update_macro_state.py |
| 4 | Match-day | T-2h | Lineups, weather, weigh-ins | Match day — manual or API |
| 5 | Live | Minutes | DeFi TVL, token price, in-play events | Real-time API fetch |

---

## Freshness flag system

SportMind's confidence output schema includes freshness signalling:

```json
{
  "sportmind_score": {
    "sms": 74,
    "sms_tier": "GOOD",
    "freshness_flags": {
      "macro_state_age_hours": 6.2,
      "macro_state_fresh": true,
      "lineup_confirmed": false,
      "form_data_age_days": 8,
      "form_data_reliable": true
    }
  },
  "freshness_warning": null
}
```

**SMS impact of stale data:**

| Data type | Stale threshold | SMS impact |
|---|---|---|
| Macro state > 8h | Mild | SMS -3 |
| Macro state > 24h | Moderate | SMS -8, add `macro_state_stale` flag |
| Form data > 4 weeks | Moderate | ×0.85 reliability on athlete_modifier |
| Lineup unconfirmed | Significant | ×0.85 position-size recommendation |
| Market tier > 90 days | Minor for signal | Note in commercial brief output |

---

## Production deployment patterns

### Pattern 1 — Pre-session load with scheduled refresh

```python
import schedule, time, subprocess, json
from datetime import datetime, timezone

def refresh_macro():
    subprocess.run(["python", "scripts/update_macro_state.py"])
    print(f"Macro refreshed: {datetime.now(timezone.utc).isoformat()}")

# Refresh macro state every 6 hours
schedule.every(6).hours.do(refresh_macro)

# Load permanent skills once at startup — these never expire
PERMANENT_STACK = {}
for sport in ["football","basketball","cricket","mma"]:
    PERMANENT_STACK[sport] = load_sport_domain_skill(sport)  # Tier 0

# For each analysis session: fetch current macro, use permanent skill stack
def analyse_event(sport, event_id):
    macro = json.load(open("platform/macro-state.json"))      # Tier 3
    lineup_confirmed = fetch_lineup_confirmation(event_id)    # Tier 4
    domain = PERMANENT_STACK[sport]                           # Tier 0
    return generate_signal(domain, macro, lineup_confirmed)
```

### Pattern 2 — MCP tool with automatic freshness checking

```python
# In sportmind_signal MCP tool — add freshness check before returning
from datetime import datetime, timezone, timedelta

def add_freshness_context(signal: dict) -> dict:
    if MACRO_STATE.exists():
        state = json.loads(MACRO_STATE.read_text())
        last_updated_str = state.get("macro_state", {}).get("last_updated", "unknown")
        try:
            last_updated = datetime.fromisoformat(last_updated_str)
            age_hours = (datetime.now(timezone.utc) - last_updated).total_seconds() / 3600
            
            if age_hours > 24:
                signal["freshness_warning"] = f"Macro state is {age_hours:.0f}h old — refresh before token decisions"
                signal["sportmind_score"]["sms"] = max(signal["sportmind_score"]["sms"] - 8, 0)
            elif age_hours > 8:
                signal["freshness_warning"] = f"Macro state is {age_hours:.0f}h old — consider refreshing"
                signal["sportmind_score"]["sms"] = max(signal["sportmind_score"]["sms"] - 3, 0)
        except ValueError:
            signal["freshness_warning"] = "Macro state timestamp could not be parsed"
    
    return signal
```

---

## The boundary SportMind does not cross

SportMind provides intelligence models, not live data. The distinction is permanent:

```
SportMind PROVIDES:
  The cricket dew factor model (how dew affects batting-second teams)
  The TVL threshold model (what TVL levels mean for slippage)
  The macro modifier model (how crypto cycles affect token signals)
  The lineup_unconfirmed flag specification (what to do when lineup unknown)

SportMind does NOT provide:
  Whether it will actually rain at Wankhede Stadium tonight
  What the actual TVL of the $PSG/CHZ pool is right now
  Whether the starting XI has been confirmed for tonight's match
  The current BTC price

Applications bridge this gap by fetching live data and applying SportMind's models.
See platform/live-signals.md for the complete boundary specification.
```

---

*MIT License · SportMind · sportmind.dev*
*Related: `platform/live-signals.md` · `platform/sportmind-mcp-server.md` · `core/confidence-output-schema.md`*
