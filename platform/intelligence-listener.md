# Intelligence Listener — SportMind Platform

**The SportMind Intelligence Listener monitors external sources across all
intelligence domains and routes detected events through the three-tier
classification system. It is the runtime implementation of the intake
framework defined in `core/external-intelligence-intake.md`.**

Zero-dependency principle preserved: the listener is an optional tool in
`scripts/`. The SportMind library itself remains static markdown. The
listener monitors the world and proposes updates — humans and agents decide
what to apply.

---

## Overview

```
EXTERNAL WORLD                    LISTENER                    SPORTMIND LIBRARY
──────────────────                ─────────────               ─────────────────
Chiliz Blog        ──►           Fetch + classify ──► TIER 1 ──► Act immediately
Socios newsroom    ──►           against SportMind ──► TIER 2 ──► Human review
BBC Sport RSS      ──►           taxonomy         ──► TIER 3 ──► Log only
CoinGecko API      ──►
HLTV (esports)     ──►            Custom sources
SEC.gov            ──►            (operator-defined)
Your own feeds     ──►
```

The listener does not modify the library directly. It detects, classifies,
and routes. What happens next depends on your dispatch mode.

---

## Quick start

```bash
# Install dependencies (library itself needs none of these)
pip install requests feedparser python-dotenv

# Set up environment
cp .env.example .env
# Edit .env with your API keys (all optional — see below)

# Run a full cycle (dry run — detects but does not dispatch)
python scripts/sportmind_listener.py --dry-run

# Run live — print detected events to stdout
python scripts/sportmind_listener.py

# Monitor one domain only
python scripts/sportmind_listener.py --domain fan_token
python scripts/sportmind_listener.py --domain macro
python scripts/sportmind_listener.py --domain sport_domain
python scripts/sportmind_listener.py --domain esports

# Send events to a webhook (Slack, Discord, or custom)
python scripts/sportmind_listener.py --dispatch webhook --webhook-url https://...

# Write events to files (JSON + Markdown)
python scripts/sportmind_listener.py --dispatch file --output-dir ./detected/

# Create GitHub Issues for Tier 1 and Tier 2 events
python scripts/sportmind_listener.py --dispatch github_issue
```

---

## Intelligence domains covered

| Domain | Sources | What it detects |
|---|---|---|
| `fan_token` | Chiliz Blog, Socios newsroom, fantokens.com | New tokens, PATH_2 events, delistings, governance proposals |
| `macro` | CoinGecko (BTC/CHZ), SEC.gov, EU ESMA | Crypto regime changes, CHZ price events, regulatory guidance |
| `sport_domain` | FIFA, BBC Sport (football, F1, cricket, MMA) | Transfers, injuries, manager changes, WC2026 squad news, rule changes |
| `esports` | HLTV, Liquipedia | Patch releases, roster changes, tournament results |
| `custom` | Operator-defined | Anything you configure |

---

## The three-tier routing system

Every detected event is classified into one of three tiers, matching the
framework in `core/external-intelligence-intake.md`:

```
TIER 1 — Act immediately
  Confirmed factual events that change the state of the world SportMind models.
  Examples: new fan token confirmed on-chain, regulatory guidance published,
  WC2026 match result, game patch release.
  Action: update library files in this session.

TIER 2 — Review required
  Credible signals that require interpretation before library changes.
  Examples: transfer rumour from credible source, injury report,
  governance proposal, CHZ price movement.
  Action: flag for human or agent review.

TIER 3 — Context only
  Background information. Useful to read, no immediate library change needed.
  Examples: academic papers, general sports news, long-term trend pieces.
  Action: log and archive.
```

---

## Event taxonomy

All 29 event types the listener can detect:

| Event type | Tier | Target file |
|---|---|---|
| `new_fan_token` | 1 | fan-token/fan-token-registry/ |
| `fan_token_delisted` | 1 | fan-token/fan-token-registry/ |
| `path2_activation` | 1 | fan-token/gamified-tokenomics-intelligence/ |
| `path1_result` | 1 | fan-token/gamified-tokenomics-intelligence/ |
| `btc_regime_change` | 1 | macro/macro-crypto-market-cycles.md |
| `chz_severe_decline` | 1 | macro/macro-crypto-market-cycles.md |
| `regulatory_guidance` | 1 | macro/macro-regulatory-sportfi.md |
| `us_market_entry` | 1 | macro/macro-regulatory-sportfi.md |
| `competition_format_change` | 1 | sports/ |
| `new_sport_calibration` | 1 | community/calibration-data/ |
| `wc2026_squad_news` | 1 | fan-token/world-cup-2026-intelligence/ |
| `wc2026_match_result` | 1 | fan-token/world-cup-2026-intelligence/ |
| `game_patch_released` | 1 | sports/esports/sport-statistics-esports.md |
| `f1_regulation_update` | 1 | sports/formula1/ |
| `governance_proposal` | 2 | fan-token/fan-token-governance-intelligence.md |
| `cdi_spike` | 2 | fan-token/fan-token-lifecycle/ |
| `token_partnership` | 2 | fan-token/fan-token-registry/ |
| `geopolitical_event` | 2 | macro/macro-geopolitical.md |
| `economic_signal` | 2 | macro/macro-economic-cycles.md |
| `chz_burn_event` | 2 | macro/macro-crypto-market-cycles.md |
| `transfer_confirmed` | 2 | core/pre-match-squad-intelligence.md |
| `injury_confirmed` | 2 | core/breaking-news-intelligence.md |
| `manager_sacked` | 2 | core/breaking-news-intelligence.md |
| `esports_roster_change` | 2 | sports/esports/sport-statistics-esports.md |
| `f1_qualifying_result` | 2 | sports/formula1/sport-statistics-formula1.md |
| `token_holder_threshold` | 3 | fan-token/fan-token-lifecycle/ |
| `academic_paper` | 3 | community/academic-references.md |
| `custom_event` | 2 | custom |

---

## Dispatch modes

| Mode | Use case | Output |
|---|---|---|
| `print` | Development, ad-hoc runs | Stdout — Markdown formatted |
| `file` | Audit trail, batch review | JSON + Markdown files in `--output-dir` |
| `webhook` | Slack, Discord, custom alerting | HTTP POST with Slack-compatible payload |
| `github_issue` | Team workflow, PR-driven updates | GitHub Issues with tier labels |

### Webhook payload format

```json
{
  "text": "SportMind Intelligence Listener — 3 events\n🔴 TIER 1 — Act immediately (1):\n...",
  "events": [
    {
      "event_type": "new_fan_token",
      "tier": "TIER_1",
      "tier_desc": "Confirmed factual event — update library files",
      "target_file": "fan-token/fan-token-registry/",
      "source": "Chiliz Official Blog",
      "title": "New Fan Token Partner: Club X joins Socios",
      "description": "...",
      "url": "https://blog.chiliz.com/...",
      "confidence": 0.88,
      "detected_at": "2026-06-14T09:15:00+00:00",
      "action_required": true
    }
  ]
}
```

---

## Environment variables

All optional — the listener degrades gracefully when keys are absent:

```bash
# .env
COINGECKO_API_KEY=your_key_here        # Free tier at coingecko.com/api
CHILIZCAN_API_KEY=your_key_here        # chiliscan.com API (on-chain events)
NEWS_API_KEY=your_key_here             # newsapi.org (broader news coverage)
GITHUB_TOKEN=ghp_...                   # Required for --dispatch github_issue
GITHUB_REPO=SportMind/SportMind        # Your repo slug
ALERT_WEBHOOK_URL=https://hooks...     # Default webhook URL
SPORTMIND_LIBRARY_PATH=/path/to/lib    # Defaults to current directory
```

---

## Custom sources

Add your own sources via a JSON config file. Any source type supported by
the built-in registry can be used, plus `local_json` for file-based inputs.

```bash
python scripts/sportmind_listener.py --custom-sources my_sources.json
```

**Custom source format (`my_sources.json`):**

```json
{
  "my_arsenal_feed": {
    "name": "My Arsenal News",
    "url": "https://example.com/arsenal.rss",
    "type": "rss",
    "feed_url": "https://example.com/arsenal.rss",
    "domain": "sport_domain",
    "tier_default": "TIER_2",
    "keywords": ["Arsenal", "AFC", "Arteta", "injury", "transfer"],
    "event_map": {
      "injury|doubt|ruled out": "injury_confirmed",
      "transfer|signed|joins":  "transfer_confirmed",
      "sacked|appointed":       "manager_sacked"
    },
    "frequency": "1h"
  },

  "my_afc_path2_monitor": {
    "name": "Custom $AFC PATH_2 Monitor",
    "url": "https://my-server.com/afc-goals",
    "type": "json_api",
    "domain": "fan_token",
    "tier_default": "TIER_1",
    "thresholds": {
      "goal_scored": {
        "description": "$AFC goal — PATH_2 supply reduction",
        "field": "goals_today",
        "operator": "gt",
        "value": 0,
        "event_type": "path2_activation"
      }
    },
    "frequency": "live"
  },

  "my_local_events": {
    "name": "My Local Event Queue",
    "url": "local",
    "type": "local_json",
    "file_path": "./my_pending_events.json",
    "domain": "custom",
    "tier_default": "TIER_2",
    "keywords": [],
    "event_map": {},
    "frequency": "on_demand"
  }
}
```

**Custom automation example:**
Any external system can write to `my_pending_events.json` — a webhook
receiver, a scraper, a Zapier action — and the listener will pick up
those events on its next run and route them through the tier system.

---

## GitHub Actions integration

Schedule the listener to run automatically:

```yaml
# .github/workflows/intelligence-listener.yml
name: SportMind Intelligence Listener

on:
  schedule:
    - cron: '0 */4 * * *'    # Every 4 hours
    - cron: '0 8 * * *'      # Daily at 08:00 UTC
  workflow_dispatch:           # Manual trigger

jobs:
  listen:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install requests feedparser python-dotenv

      - name: Run intelligence listener
        env:
          COINGECKO_API_KEY:  ${{ secrets.COINGECKO_API_KEY }}
          ALERT_WEBHOOK_URL:  ${{ secrets.ALERT_WEBHOOK_URL }}
          GITHUB_TOKEN:       ${{ secrets.GITHUB_TOKEN }}
          GITHUB_REPO:        ${{ github.repository }}
        run: |
          python scripts/sportmind_listener.py \
            --domain all \
            --dispatch github_issue \
            --min-confidence 0.70

      # WC2026 window: run more frequently June 11 – July 19 2026
      - name: WC2026 intensive monitoring
        if: ${{ env.WC2026_ACTIVE == 'true' }}
        env:
          ALERT_WEBHOOK_URL: ${{ secrets.ALERT_WEBHOOK_URL }}
        run: |
          python scripts/sportmind_listener.py \
            --domain sport_domain \
            --tier 1 \
            --dispatch webhook
```

---

## Recommended schedules

| Domain | Recommended frequency | Rationale |
|---|---|---|
| `macro` (CHZ/BTC price) | Every 4 hours | Price moves are continuous |
| `fan_token` (Chiliz blog) | Daily | Announcements are infrequent |
| `sport_domain` (football) | Every 1 hour during season | Injuries and transfers are time-sensitive |
| `sport_domain` (F1) | Every 4 hours during race weekends | Qualifying and race results |
| `esports` | Every 4 hours | Patch drops are unpredictable |
| `sport_domain` (WC2026) | Every 1 hour June 11–July 19 | High-velocity tournament window |

---

## Confidence scoring

The listener calculates confidence per event based on keyword density:

```
Base confidence:  0.60 (pattern match only)
Per keyword hit:  +0.08 (up to 0.95 maximum)
Price thresholds: 0.95 (numeric — high confidence)

Default minimum:  0.60 (use --min-confidence to adjust)
Recommended:      0.70 for GitHub Issues
                  0.80 for Tier 1 auto-dispatch
```

---

## Extending the listener

**Adding a new source type:**
Implement a `fetch_{type}` function following the pattern of `fetch_rss`
and `fetch_json_api`. Register the type in `BUILT_IN_SOURCES` entries.

**Adding a new event type:**
Add an entry to the `EVENT_TYPES` dictionary with tier and target file.
Add keyword patterns to relevant source `event_map` dictionaries.

**Adding a new domain:**
Add the domain string to source configs and extend `domains_to_check`
in `main()`.

---

## Compatibility

**Requires (optional — graceful degradation without):**
  `requests` — HTTP fetching
  `feedparser` — RSS parsing
  `python-dotenv` — .env file loading

**Extends:**
  `core/external-intelligence-intake.md` — three-tier classification framework
  `core/breaking-news-intelligence.md` — Category 1/2/3 event taxonomy
  `platform/monitoring-alerts.md` — existing macro and skill monitoring

**Related scripts:**
  `scripts/check_macro_signals.py` — macro-only price monitoring (existing)
  `scripts/check_token_partnerships.py` — token registry monitoring (existing)
  `scripts/check_skill_freshness.py` — skill freshness checks (existing)

The listener supersedes the three narrow scripts above when running in
`--domain all` mode. The narrow scripts remain useful for targeted,
lightweight monitoring in resource-constrained environments.

---

*SportMind v3.93.5 · MIT License · sportmind.dev*
