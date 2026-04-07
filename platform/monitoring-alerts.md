# Monitoring Alerts — SportMind Platform

**The alert specification for automated macro event monitoring and real-time
skill update detection.** Defines what triggers an alert, what format alerts
take, and how agents and developers receive and act on them.

---

## Two alert types

```
TYPE 1 — MACRO SIGNAL ALERT:
  What: A live signal crosses a SportMind threshold
  Examples: BTC falls below 200-day MA; CHZ drops >15% in 24h;
            geopolitical event detected in monitored regions
  Who receives: Agents subscribed to macro alerts; developers via webhook
  Agent action: Recalculate modifier; potentially change open positions
  Speed: Within 2 hours of threshold crossing

TYPE 2 — SKILL REVIEW ALERT:
  What: A detected change suggests a SportMind skill file may be outdated
  Examples: Competition format change detected; new token listed;
            partnership announcement; regulatory change
  Who receives: SportMind maintainers; community contributors
  Maintainer action: Review flagged skill file; update if needed; close alert
  Speed: Within 48 hours of detection; skill review within 7 days
```

---

## Macro signal alert specifications

### Alert 1: Crypto market cycle change

```
TRIGGER CONDITIONS:
  BTC BEAR:     BTC price crosses BELOW 200-day MA (not just dips — confirmed close)
  BTC BULL:     BTC price crosses ABOVE 200-day MA after being below
  CHZ SEVERE:   CHZ drops >25% in 7 days while BTC is flat or rising
  CHZ RECOVERY: CHZ recovers >15% from recent low while BTC is stable

CONFIRMATION RULE:
  Single-day close below MA: WARNING state (no full alert yet)
  3 consecutive closes below MA: CONFIRMED BEAR alert fires
  This prevents false alerts from intraday volatility

ALERT PAYLOAD:
{
  "alert_type": "MACRO_CRYPTO_CYCLE",
  "severity": "HIGH",
  "fired_at": "ISO-8601",
  "condition": "BTC_BEAR_CONFIRMED",
  "data": {
    "btc_price": 38500,
    "btc_200d_ma": 46200,
    "btc_vs_ma_pct": -16.7,
    "chz_price": 0.071,
    "chz_7d_change_pct": -18.2,
    "consecutive_closes_below_ma": 3
  },
  "sportmind_impact": {
    "modifier_change": "macro_modifier: 1.00 → 0.75",
    "affected_skill": "macro/macro-crypto-market-cycles.md",
    "agent_action": "Apply ×0.75 multiplier to ALL fan token signal scores",
    "prediction_market_impact": "No change — crypto modifier does not apply"
  },
  "recommended_agent_response": "Recalculate all open position signals with new macro modifier"
}

RESOLUTION:
  Alert clears when: BTC returns above 200-day MA for 3 consecutive closes
  Resolution fires separate MACRO_CRYPTO_RECOVERY alert
```

### Alert 2: Geopolitical event

```
TRIGGER CONDITIONS:
  Monitored keywords in Reuters/AP/BBC headline feeds:
  - "war", "invasion", "military operation" + country in SportMind geo-watch list
  - "sanctions" + country affecting Tier 1 sport market
  - "terrorism" + major sporting venue or tournament
  
GEO-WATCH LIST (countries with Tier 1-2 token relevance):
  Europe: UK, France, Germany, Spain, Italy, Turkey, Netherlands
  Americas: USA, Brazil, Mexico, Argentina
  Asia-Pacific: UAE, Saudi Arabia, India, Japan, South Korea, Australia
  Sport-specific: Pakistan (PSL), Russia (hockey exclusions)

ALERT PAYLOAD:
{
  "alert_type": "MACRO_GEOPOLITICAL",
  "severity": "MEDIUM | HIGH | CRITICAL",
  "condition": "CONFLICT_DETECTED | SANCTIONS | VENUE_THREAT",
  "affected_region": "string",
  "affected_sports": ["football", "cricket"],
  "affected_tokens": ["$PSG", "$CITY"],
  "sportmind_impact": {
    "modifier_change": "geopolitical_modifier: applied to affected entities",
    "affected_skill": "macro/macro-geopolitical.md",
    "agent_action": "Load macro-geopolitical.md; apply entity-specific modifier"
  },
  "source_url": "https://reuters.com/...",
  "human_review_required": true
}

NOTE: Geopolitical alerts always require human confirmation before modifier is applied.
      The alert flags; a human approves the SportMind response.
```

### Alert 3: Economic recession signal

```
TRIGGER CONDITIONS:
  GDP_NEGATIVE_2:   Second consecutive quarter of negative GDP growth
                    in UK, USA, Eurozone, or Australia
  INFLATION_SPIKE:  CPI > 8% YoY in key token market countries
  
ALERT PAYLOAD:
{
  "alert_type": "MACRO_ECONOMIC",
  "severity": "MEDIUM",
  "condition": "RECESSION_CONFIRMED | INFLATION_SPIKE",
  "affected_markets": ["UK", "EU"],
  "sportmind_impact": {
    "modifier_change": "economic_modifier: 1.00 → 0.88",
    "affected_tokens": "Premium sports token valuations",
    "agent_action": "Load macro-economic-cycles.md; apply premium sport modifier"
  }
}
```

---

## Skill review alert specifications

### Alert 4: Competition format change

```
TRIGGER CONDITIONS:
  Detected via structured monitoring of official competition websites:
  - New team count detected (league expansion/contraction)
  - New tournament format (e.g. Champions League format change)
  - New competition announced (e.g. new T20 league)
  - Competition cancelled or suspended

DETECTION SOURCES:
  Football: UEFA.com, FIFA.com, Premier League, La Liga official sites
  Cricket: ICC official, BCCI, PCB
  NBA: NBA.com official news
  Others: Official league/federation sites per sport

ALERT PAYLOAD:
{
  "alert_type": "SKILL_REVIEW",
  "category": "COMPETITION_FORMAT_CHANGE",
  "severity": "MEDIUM",
  "detected_at": "ISO-8601",
  "sport": "football",
  "detected_change": "Champions League format expanded to 36 clubs from 2024",
  "source_url": "https://www.uefa.com/...",
  "skill_files_to_review": [
    "sports/football/sport-domain-football.md",
    "fan-token/football-token-intelligence/football-token-intelligence.md",
    "market/market-football.md"
  ],
  "review_priority": "HIGH",
  "review_deadline": "ISO-8601 (7 days)",
  "github_issue_template": "skill-improvement",
  "assigned_to": null
}
```

### Alert 5: New fan token partnership

```
TRIGGER CONDITIONS:
  Detected via Socios/Chiliz official announcements:
  - New club partnership announced
  - New sport category partnership
  
ALERT PAYLOAD:
{
  "alert_type": "SKILL_REVIEW",
  "category": "NEW_PARTNERSHIP",
  "sport": "string",
  "entity": "Club/league name",
  "token_symbol": "string",
  "source_url": "string",
  "skill_files_to_review": [
    "market/market-{sport}.md",
    "fan-token/fan-token-layer-overview.md"
  ],
  "review_priority": "HIGH"
}
```

### Alert 6: Regulatory change

```
TRIGGER CONDITIONS:
  Monitored jurisdiction announcements:
  - India: SEBI or Finance Ministry crypto framework updates
  - EU: MiCA implementation updates affecting sports tokens
  - UK: FCA crypto asset guidance changes
  - US: SEC or CFTC sports token classification

ALERT PAYLOAD:
{
  "alert_type": "SKILL_REVIEW",
  "category": "REGULATORY_CHANGE",
  "jurisdiction": "India",
  "summary": "SEBI clarifies VDA framework — sports tokens may qualify",
  "sportmind_impact": "IPL token pathway potentially opened",
  "skill_files_to_review": [
    "market/market-cricket.md",
    "fan-token/cricket-token-intelligence/cricket-token-intelligence.md",
    "macro/macro-economic-cycles.md"
  ],
  "review_priority": "CRITICAL"
}
```

---

## Webhook format

All alerts are delivered via webhook in the same envelope format:

```json
{
  "sportmind_alert": {
    "alert_id": "uuid",
    "alert_version": "1.0",
    "fired_at": "ISO-8601",
    "alert_type": "MACRO_SIGNAL | SKILL_REVIEW",
    "severity": "LOW | MEDIUM | HIGH | CRITICAL",
    "payload": { /* alert-specific payload from specifications above */ },
    "delivery": {
      "retry_count": 0,
      "next_retry_if_failed": "ISO-8601"
    }
  }
}
```

**Webhook endpoints (developer-configured):**

```
SETUP:
  Developers register webhook URL in their SportMind integration config
  Separate endpoints can be configured per alert type
  
SECURITY:
  Each webhook delivery includes: X-SportMind-Signature header
  HMAC-SHA256 of payload using developer's secret key
  Verify signature before processing alert
  
RETRY POLICY:
  Failed delivery (non-2xx response): retry at 5min, 30min, 2h, 12h, 24h
  After 5 failed attempts: alert marked as undelivered; logged in platform
```

---

## GitHub Actions monitoring workflow

```yaml
# .github/workflows/macro-monitor.yml
name: Macro signal monitoring

on:
  schedule:
    - cron: '0 */4 * * *'  # Every 4 hours
  workflow_dispatch:         # Manual trigger

jobs:
  check-macro-signals:
    runs-on: ubuntu-latest
    name: Check macro thresholds

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install requests python-dotenv

      - name: Check BTC vs 200-day MA
        env:
          COINGECKO_API_KEY: ${{ secrets.COINGECKO_API_KEY }}
          ALERT_WEBHOOK_URL: ${{ secrets.ALERT_WEBHOOK_URL }}
        run: |
          python scripts/check_macro_signals.py \
            --signal btc_200d_ma \
            --threshold-type crossover \
            --consecutive-confirms 3 \
            --webhook $ALERT_WEBHOOK_URL

      - name: Check CHZ severe decline
        run: |
          python scripts/check_macro_signals.py \
            --signal chz_7d_change \
            --threshold -0.25 \
            --webhook $ALERT_WEBHOOK_URL

      - name: Update macro state file
        run: |
          python scripts/update_macro_state.py
          git config user.email "sportmind-bot@sportmind.dev"
          git config user.name "SportMind Monitor"
          git add platform/macro-state.json
          git diff --staged --quiet || git commit -m "chore: update macro state [skip ci]"
          git push
```

```yaml
# .github/workflows/skill-review-monitor.yml  
name: Skill review monitoring

on:
  schedule:
    - cron: '0 9 * * 1'   # Every Monday at 9am UTC
  workflow_dispatch:

jobs:
  detect-skill-changes:
    runs-on: ubuntu-latest
    name: Detect changes requiring skill review

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Check competition format sources
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python scripts/check_skill_freshness.py \
            --sources platform/monitoring-sources.json \
            --create-issues-if-stale \
            --stale-threshold-days 90

      - name: Check for new Chiliz partnerships
        run: |
          python scripts/check_token_partnerships.py \
            --source https://www.socios.com/fan-tokens \
            --registry platform/skill-registry.md
```

---

## Macro state file

A lightweight JSON file updated by the monitoring workflow.
Agents read this at session start as a fast macro state check.

```json
// platform/macro-state.json (auto-updated by monitor workflow)
{
  "macro_state": {
    "updated_at": "ISO-8601",
    "crypto_cycle": {
      "phase": "BULL | NEUTRAL | BEAR | EXTREME_BEAR",
      "btc_vs_200d_ma_pct": 12.4,
      "chz_30d_change_pct": 8.2,
      "macro_modifier": 1.20,
      "last_phase_change": "ISO-8601",
      "consecutive_confirms": 5
    },
    "active_geopolitical_events": [],
    "active_economic_events": [],
    "pending_skill_reviews": [
      {
        "skill": "sports/football/sport-domain-football.md",
        "reason": "Champions League format change",
        "priority": "HIGH",
        "github_issue": 142
      }
    ]
  }
}
```

**Agents use this file as a fast session-start check:**

```python
# Fast macro state check (replaces loading full macro files for common case)
import json, requests

state = json.loads(requests.get(
    "https://raw.githubusercontent.com/SportMind/sportmind/main/platform/macro-state.json"
).text)

macro_modifier = state["macro_state"]["crypto_cycle"]["macro_modifier"]
active_geo_events = state["macro_state"]["active_geopolitical_events"]

# Only load full macro files if something is active
if active_geo_events or macro_modifier != 1.00:
    # Load full macro/macro-crypto-market-cycles.md for detail
    pass
```

---

*MIT License · SportMind · sportmind.dev*
