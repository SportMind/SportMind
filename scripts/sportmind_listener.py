#!/usr/bin/env python3
"""
SportMind Intelligence Listener — Universal Update Monitor

Monitors external sources across all SportMind intelligence domains and
routes detected events through the three-tier classification system defined
in core/external-intelligence-intake.md.

Coverage:
  Fan token ecosystem   — new tokens, PATH_2 events, CDI changes, governance
  Sport domain          — rule changes, competition formats, calibration signals
  Athlete intelligence  — transfers, injuries (breaking news Category 1/2)
  Macro intelligence    — crypto cycles, regulatory changes, geopolitical events
  Esports               — patch drops, roster changes
  Custom sources        — operator-defined feeds, webhooks, local files

Zero-dependency for the library itself. This script requires:
  requests, python-dotenv (pip install requests python-dotenv)
  Optional: feedparser (pip install feedparser) for RSS sources

Usage:
  # Run full listener cycle (all domains)
  python scripts/sportmind_listener.py

  # Run specific domain only
  python scripts/sportmind_listener.py --domain fan_token
  python scripts/sportmind_listener.py --domain macro
  python scripts/sportmind_listener.py --domain sport_domain

  # Dry run — detect events but do not write any files
  python scripts/sportmind_listener.py --dry-run

  # Load custom sources from your own config file
  python scripts/sportmind_listener.py --custom-sources my_sources.json

  # Set dispatch mode for routing detected events
  python scripts/sportmind_listener.py --dispatch webhook --webhook-url https://...
  python scripts/sportmind_listener.py --dispatch github_issue
  python scripts/sportmind_listener.py --dispatch file --output-dir ./detected/
  python scripts/sportmind_listener.py --dispatch print  (default — stdout only)

Environment variables (set in .env or environment):
  COINGECKO_API_KEY       CoinGecko API key (free tier works)
  CHILIZCAN_API_KEY       ChiliZ chain explorer (optional)
  NEWS_API_KEY            NewsAPI.org key (optional — broader news coverage)
  GITHUB_TOKEN            GitHub token (required for --dispatch github_issue)
  GITHUB_REPO             Repository slug e.g. SportMind/SportMind
  ALERT_WEBHOOK_URL       Default webhook URL for dispatch
  SPORTMIND_LIBRARY_PATH  Path to SportMind library root (default: current dir)

See platform/intelligence-listener.md for full documentation.
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# ── OPTIONAL IMPORTS ──────────────────────────────────────────────────────────
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

try:
    from dotenv import load_dotenv
    load_dotenv()
    HAS_DOTENV = True
except ImportError:
    HAS_DOTENV = False

try:
    import feedparser
    HAS_FEEDPARSER = True
except ImportError:
    HAS_FEEDPARSER = False


# ── VERSION ───────────────────────────────────────────────────────────────────
VERSION = "3.93.5"
LISTENER_VERSION = "1.0.0"


# ── THREE-TIER CLASSIFICATION ─────────────────────────────────────────────────
# Maps to core/external-intelligence-intake.md
TIER_1 = "TIER_1"   # Act immediately — confirmed factual events
TIER_2 = "TIER_2"   # Queue for review — credible but requires interpretation
TIER_3 = "TIER_3"   # Context only — background, no immediate action

TIER_DESCRIPTIONS = {
    TIER_1: "Confirmed factual event — update library files",
    TIER_2: "Credible signal — queue for human review",
    TIER_3: "Background context — log only",
}

# ── EVENT TAXONOMY ────────────────────────────────────────────────────────────
# All event types SportMind can detect and route
EVENT_TYPES = {
    # Fan token ecosystem
    "new_fan_token":           (TIER_1, "fan-token/fan-token-registry/"),
    "fan_token_delisted":      (TIER_1, "fan-token/fan-token-registry/"),
    "path2_activation":        (TIER_1, "fan-token/gamified-tokenomics-intelligence/"),
    "path1_result":            (TIER_1, "fan-token/gamified-tokenomics-intelligence/"),
    "governance_proposal":     (TIER_2, "fan-token/fan-token-governance-intelligence.md"),
    "cdi_spike":               (TIER_2, "fan-token/fan-token-lifecycle/"),
    "token_partnership":       (TIER_2, "fan-token/fan-token-registry/"),
    "token_holder_threshold":  (TIER_3, "fan-token/fan-token-lifecycle/"),

    # Macro intelligence
    "btc_regime_change":       (TIER_1, "macro/macro-crypto-market-cycles.md"),
    "chz_severe_decline":      (TIER_1, "macro/macro-crypto-market-cycles.md"),
    "regulatory_guidance":     (TIER_1, "macro/macro-regulatory-sportfi.md"),
    "us_market_entry":         (TIER_1, "macro/macro-regulatory-sportfi.md"),
    "geopolitical_event":      (TIER_2, "macro/macro-geopolitical.md"),
    "economic_signal":         (TIER_2, "macro/macro-economic-cycles.md"),
    "chz_burn_event":          (TIER_2, "macro/macro-crypto-market-cycles.md"),

    # Sport domain
    "competition_format_change": (TIER_1, "sports/"),
    "new_sport_calibration":     (TIER_1, "community/calibration-data/"),
    "wc2026_squad_news":         (TIER_1, "fan-token/world-cup-2026-intelligence/"),
    "wc2026_match_result":       (TIER_1, "fan-token/world-cup-2026-intelligence/"),
    "transfer_confirmed":        (TIER_2, "core/pre-match-squad-intelligence.md"),
    "injury_confirmed":          (TIER_2, "core/breaking-news-intelligence.md"),
    "manager_sacked":            (TIER_2, "core/breaking-news-intelligence.md"),

    # Esports
    "game_patch_released":       (TIER_1, "sports/esports/sport-statistics-esports.md"),
    "esports_roster_change":     (TIER_2, "sports/esports/sport-statistics-esports.md"),

    # Formula 1
    "f1_regulation_update":      (TIER_1, "sports/formula1/"),
    "f1_qualifying_result":      (TIER_2, "sports/formula1/sport-statistics-formula1.md"),

    # Academic / research
    "academic_paper":            (TIER_3, "community/academic-references.md"),

    # Custom / operator-defined
    "custom_event":              (TIER_2, "custom"),
}


# ── SOURCE REGISTRY ───────────────────────────────────────────────────────────
# All built-in sources SportMind monitors
# Operators can add custom sources via --custom-sources

BUILT_IN_SOURCES = {

    # ── FAN TOKEN ECOSYSTEM ───────────────────────────────────────────────────
    "chiliz_blog": {
        "name":        "Chiliz Official Blog",
        "url":         "https://blog.chiliz.com",
        "type":        "rss",
        "feed_url":    "https://blog.chiliz.com/feed/",
        "domain":      "fan_token",
        "tier_default": TIER_1,
        "keywords":    ["fan token", "new club", "new partner", "PATH", "launch",
                        "listing", "delisting", "milestone"],
        "event_map":   {
            "new.*partner|new.*club|launch": "new_fan_token",
            "PATH_2|fan token play":         "path2_activation",
            "delist|expired|retired":        "fan_token_delisted",
        },
        "frequency":   "daily",
    },

    "socios_newsroom": {
        "name":        "Socios.com Newsroom",
        "url":         "https://www.socios.com/press/",
        "type":        "html_scrape",
        "domain":      "fan_token",
        "tier_default": TIER_1,
        "keywords":    ["announce", "partner", "launch", "fan token",
                        "exclusive", "governance"],
        "event_map":   {
            "new.*partner|launch|announce": "token_partnership",
            "governance|vote":              "governance_proposal",
        },
        "frequency":   "daily",
    },

    "fantokens_registry": {
        "name":        "Fan Tokens Registry (fantokens.com)",
        "url":         "https://fantokens.com",
        "type":        "html_scrape",
        "domain":      "fan_token",
        "tier_default": TIER_1,
        "keywords":    ["new", "expired", "active", "inactive"],
        "event_map":   {
            "new token|launched":   "new_fan_token",
            "expired|inactive":     "fan_token_delisted",
        },
        "frequency":   "daily",
    },

    # ── MACRO INTELLIGENCE ────────────────────────────────────────────────────
    "coingecko_btc": {
        "name":        "CoinGecko — BTC price",
        "url":         "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true&include_market_cap=true",
        "type":        "json_api",
        "domain":      "macro",
        "tier_default": TIER_1,
        "auth_env":    "COINGECKO_API_KEY",
        "thresholds": {
            "btc_200d_ma_cross": {
                "description": "BTC crosses 200-day MA — macro regime signal",
                "event_type":  "btc_regime_change",
                "requires_200d_ma": True,
            },
        },
        "frequency":   "4h",
    },

    "coingecko_chz": {
        "name":        "CoinGecko — CHZ price",
        "url":         "https://api.coingecko.com/api/v3/simple/price?ids=chiliz&vs_currencies=usd&include_24hr_change=true&include_7d_change=true",
        "type":        "json_api",
        "domain":      "macro",
        "tier_default": TIER_1,
        "auth_env":    "COINGECKO_API_KEY",
        "thresholds": {
            "chz_7d_decline_25pct": {
                "description": "CHZ drops >25% in 7 days",
                "field":       "chiliz.usd_7d_change",
                "operator":    "lt",
                "value":       -0.25,
                "event_type":  "chz_severe_decline",
            },
            "chz_7d_gain_30pct": {
                "description": "CHZ gains >30% in 7 days — positive macro signal",
                "field":       "chiliz.usd_7d_change",
                "operator":    "gt",
                "value":        0.30,
                "event_type":  "chz_burn_event",
            },
        },
        "frequency":   "4h",
    },

    "sec_gov_releases": {
        "name":        "SEC.gov — Press releases",
        "url":         "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&type=8-K&dateb=&owner=include&count=10&search_text=",
        "type":        "rss",
        "feed_url":    "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=&dateb=&owner=include&count=5&search_text=&output=atom",
        "domain":      "macro",
        "tier_default": TIER_2,
        "keywords":    ["crypto", "digital asset", "token", "blockchain",
                        "fan token", "Chiliz", "Socios"],
        "event_map":   {
            "fan token|chiliz|socios":      "regulatory_guidance",
            "digital asset|crypto":         "regulatory_guidance",
        },
        "frequency":   "daily",
    },

    "mica_euractiv": {
        "name":        "EU MiCA regulatory updates",
        "url":         "https://www.esma.europa.eu/press-news/esma-news",
        "type":        "html_scrape",
        "domain":      "macro",
        "tier_default": TIER_2,
        "keywords":    ["MiCA", "crypto-asset", "digital asset", "token",
                        "fan token", "Chiliz"],
        "event_map":   {
            "MiCA|MICA|crypto-asset": "regulatory_guidance",
        },
        "frequency":   "weekly",
    },

    # ── SPORT DOMAIN ──────────────────────────────────────────────────────────
    "fifa_news": {
        "name":        "FIFA Official News",
        "url":         "https://www.fifa.com/en/articles",
        "type":        "rss",
        "feed_url":    "https://www.fifa.com/en/articles.rss",
        "domain":      "sport_domain",
        "tier_default": TIER_2,
        "keywords":    ["World Cup 2026", "squad", "injury", "suspension",
                        "format change", "rule", "regulation"],
        "event_map":   {
            "World Cup 2026|WC2026":        "wc2026_squad_news",
            "injury|fitness|doubt":         "injury_confirmed",
            "rule change|format":           "competition_format_change",
        },
        "frequency":   "daily",
    },

    "bbc_sport_football": {
        "name":        "BBC Sport — Football",
        "url":         "https://feeds.bbci.co.uk/sport/football/rss.xml",
        "type":        "rss",
        "feed_url":    "https://feeds.bbci.co.uk/sport/football/rss.xml",
        "domain":      "sport_domain",
        "tier_default": TIER_2,
        "keywords":    ["Arsenal", "Manchester City", "PSG", "Barcelona",
                        "transfer", "injury", "sacked", "signed",
                        "World Cup", "Champions League"],
        "event_map":   {
            "transfer|signed|joins":        "transfer_confirmed",
            "injury|doubt|ruled out":       "injury_confirmed",
            "sacked|dismissed|appointed":   "manager_sacked",
            "World Cup":                    "wc2026_squad_news",
        },
        "frequency":   "1h",
        "high_priority": True,
    },

    "bbc_sport_formula1": {
        "name":        "BBC Sport — Formula 1",
        "url":         "https://feeds.bbci.co.uk/sport/formula1/rss.xml",
        "type":        "rss",
        "feed_url":    "https://feeds.bbci.co.uk/sport/formula1/rss.xml",
        "domain":      "sport_domain",
        "tier_default": TIER_2,
        "keywords":    ["qualifying", "regulation", "technical directive",
                        "penalty", "FIA", "Sauber", "Audi"],
        "event_map":   {
            "regulation|technical directive|rule": "f1_regulation_update",
            "qualifying":                          "f1_qualifying_result",
        },
        "frequency":   "4h",
    },

    "bbc_sport_mma": {
        "name":        "MMA Fighting — News",
        "url":         "https://www.mmafighting.com/rss/current",
        "type":        "rss",
        "feed_url":    "https://www.mmafighting.com/rss/current",
        "domain":      "sport_domain",
        "tier_default": TIER_2,
        "keywords":    ["missed weight", "weigh-in", "UFC", "title",
                        "injury", "withdrawal", "camp change"],
        "event_map":   {
            "missed weight|failed.*weight":  "injury_confirmed",
            "injury|withdrawal|pull":        "injury_confirmed",
        },
        "frequency":   "4h",
    },

    "bbc_sport_cricket": {
        "name":        "ESPN Cricinfo — News",
        "url":         "https://www.espncricinfo.com/rss/content/story/feeds/0.xml",
        "type":        "rss",
        "feed_url":    "https://www.espncricinfo.com/rss/content/story/feeds/0.xml",
        "domain":      "sport_domain",
        "tier_default": TIER_2,
        "keywords":    ["injury", "squad", "World Cup", "IPL",
                        "India", "Pakistan", "dew", "pitch report"],
        "event_map":   {
            "injury|ruled out|doubt":        "injury_confirmed",
            "World Cup|squad":               "wc2026_squad_news",
        },
        "frequency":   "4h",
    },

    # ── ESPORTS ───────────────────────────────────────────────────────────────
    "hltv_cs2": {
        "name":        "HLTV — CS2 News",
        "url":         "https://www.hltv.org/rss/news",
        "type":        "rss",
        "feed_url":    "https://www.hltv.org/rss/news",
        "domain":      "esports",
        "tier_default": TIER_2,
        "keywords":    ["patch", "update", "roster", "transfer",
                        "Vitality", "NIP", "leaves", "joins"],
        "event_map":   {
            "patch|update|release":          "game_patch_released",
            "roster|transfer|leaves|joins":  "esports_roster_change",
        },
        "frequency":   "4h",
    },

    "liquipedia_esports": {
        "name":        "Liquipedia — Esports results",
        "url":         "https://liquipedia.net/counterstrike/api.php",
        "type":        "html_scrape",
        "domain":      "esports",
        "tier_default": TIER_2,
        "keywords":    ["patch", "roster", "tournament", "Vitality", "NIP"],
        "event_map":   {
            "roster|transfer":               "esports_roster_change",
        },
        "frequency":   "daily",
    },
}


# ── DETECTED EVENT ────────────────────────────────────────────────────────────
class DetectedEvent:
    """A single intelligence event detected from a source."""

    def __init__(self, event_type: str, source_name: str, title: str,
                 description: str, url: str = "", confidence: float = 0.8,
                 raw_data: dict = None):
        tier, target_file = EVENT_TYPES.get(event_type, (TIER_2, "unknown"))
        self.event_type   = event_type
        self.tier         = tier
        self.target_file  = target_file
        self.source_name  = source_name
        self.title        = title
        self.description  = description
        self.url          = url
        self.confidence   = confidence
        self.raw_data     = raw_data or {}
        self.detected_at  = datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> dict:
        return {
            "event_type":   self.event_type,
            "tier":         self.tier,
            "tier_desc":    TIER_DESCRIPTIONS[self.tier],
            "target_file":  self.target_file,
            "source":       self.source_name,
            "title":        self.title,
            "description":  self.description,
            "url":          self.url,
            "confidence":   self.confidence,
            "detected_at":  self.detected_at,
            "action_required": self.tier in (TIER_1, TIER_2),
        }

    def to_markdown(self) -> str:
        tier_label = {TIER_1: "🔴 TIER 1", TIER_2: "🟡 TIER 2", TIER_3: "🔵 TIER 3"}[self.tier]
        return f"""## {tier_label} — {self.event_type.replace('_', ' ').title()}

**Source:**      {self.source_name}
**Title:**       {self.title}
**Detected:**    {self.detected_at}
**Confidence:**  {self.confidence:.0%}
**Target file:** `{self.target_file}`
**URL:**         {self.url or 'N/A'}

{self.description}

**Required action:** {TIER_DESCRIPTIONS[self.tier]}
"""


# ── SOURCE FETCHERS ───────────────────────────────────────────────────────────

def fetch_rss(source: dict, dry_run: bool = False) -> list:
    """Fetch and parse an RSS feed, returning raw items."""
    if not HAS_FEEDPARSER:
        print(f"  [SKIP] {source['name']}: feedparser not installed")
        return []
    if not HAS_REQUESTS:
        print(f"  [SKIP] {source['name']}: requests not installed")
        return []
    try:
        feed = feedparser.parse(source.get("feed_url", source["url"]))
        return [{"title": e.get("title",""), "summary": e.get("summary",""),
                 "link": e.get("link","")} for e in feed.entries[:20]]
    except Exception as e:
        print(f"  [ERROR] {source['name']}: {e}")
        return []


def fetch_json_api(source: dict, dry_run: bool = False) -> dict:
    """Fetch a JSON API endpoint."""
    if not HAS_REQUESTS:
        print(f"  [SKIP] {source['name']}: requests not installed")
        return {}
    try:
        headers = {}
        api_key = os.getenv(source.get("auth_env", ""), "")
        if api_key:
            headers["x-cg-demo-api-key"] = api_key
        response = requests.get(source["url"], headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"  [ERROR] {source['name']}: {e}")
        return {}


def classify_text(text: str, source: dict) -> list:
    """
    Classify text against source event_map to detect event types.
    Returns list of (event_type, confidence, matched_pattern) tuples.
    """
    text_lower = text.lower()
    detected = []
    for pattern, event_type in source.get("event_map", {}).items():
        if re.search(pattern.lower(), text_lower):
            # Check keywords for confidence boost
            keyword_hits = sum(
                1 for kw in source.get("keywords", [])
                if kw.lower() in text_lower
            )
            confidence = min(0.95, 0.60 + (keyword_hits * 0.08))
            detected.append((event_type, confidence, pattern))
    return detected


# ── DOMAIN CHECKERS ───────────────────────────────────────────────────────────

def check_domain(domain: str, sources: dict, dry_run: bool = False) -> list:
    """
    Run all sources for a given domain and return detected events.
    """
    events = []
    domain_sources = {k: v for k, v in sources.items()
                      if v.get("domain") == domain}

    if not domain_sources:
        return events

    print(f"\n  Checking domain: {domain} ({len(domain_sources)} sources)")

    for source_key, source in domain_sources.items():
        print(f"    [{source['type'].upper()}] {source['name']}...", end=" ", flush=True)

        items = []
        if source["type"] == "rss":
            items = fetch_rss(source, dry_run)
        elif source["type"] == "json_api":
            data = fetch_json_api(source, dry_run)
            # Threshold evaluation for price APIs
            for threshold_key, threshold in source.get("thresholds", {}).items():
                event = evaluate_threshold(data, threshold, source)
                if event:
                    events.append(event)
            print(f"checked ({len(source.get('thresholds',{}))} thresholds)")
            continue
        elif source["type"] == "html_scrape":
            # HTML scraping requires requests — stub for custom implementations
            print("skipped (html_scrape requires custom implementation)")
            continue

        # Process RSS/feed items
        new_events = 0
        for item in items:
            text = (item.get("title", "") + " " + item.get("summary", "")).strip()
            classifications = classify_text(text, source)
            for event_type, confidence, pattern in classifications:
                if confidence >= 0.60:
                    events.append(DetectedEvent(
                        event_type   = event_type,
                        source_name  = source["name"],
                        title        = item.get("title", "")[:120],
                        description  = item.get("summary", "")[:300],
                        url          = item.get("link", ""),
                        confidence   = confidence,
                    ))
                    new_events += 1

        print(f"{len(items)} items → {new_events} events detected")

    return events


def evaluate_threshold(data: dict, threshold: dict, source: dict) -> Optional['DetectedEvent']:
    """Evaluate a numeric threshold against API data."""
    try:
        field_path = threshold.get("field", "")
        operator   = threshold.get("operator", "lt")
        value      = threshold.get("value", 0)

        # Navigate nested JSON
        current = data
        for key in field_path.split("."):
            if isinstance(current, dict):
                current = current.get(key)
            else:
                return None

        if current is None:
            return None

        triggered = (
            (operator == "lt" and current < value) or
            (operator == "gt" and current > value) or
            (operator == "eq" and current == value)
        )

        if triggered:
            return DetectedEvent(
                event_type   = threshold["event_type"],
                source_name  = source["name"],
                title        = threshold["description"],
                description  = f"Value: {current:.4f} | Threshold: {operator} {value}",
                confidence   = 0.95,
            )
    except Exception:
        pass
    return None


# ── DISPATCH ──────────────────────────────────────────────────────────────────

def dispatch_events(events: list, mode: str, config: dict, dry_run: bool = False):
    """Route detected events to the configured dispatch target."""

    if not events:
        print("\n  No events to dispatch.")
        return

    tier1 = [e for e in events if e.tier == TIER_1]
    tier2 = [e for e in events if e.tier == TIER_2]
    tier3 = [e for e in events if e.tier == TIER_3]

    print(f"\n{'─'*60}")
    print(f"DISPATCH SUMMARY — {len(events)} events detected")
    print(f"  🔴 TIER 1 (act immediately):    {len(tier1)}")
    print(f"  🟡 TIER 2 (review required):    {len(tier2)}")
    print(f"  🔵 TIER 3 (context only):       {len(tier3)}")

    if dry_run:
        print("\n  [DRY RUN] No dispatch performed.")
        for e in events:
            print(f"  [{e.tier}] {e.event_type}: {e.title[:60]}")
        return

    if mode == "print":
        _dispatch_print(events)
    elif mode == "file":
        _dispatch_file(events, config.get("output_dir", "./detected/"))
    elif mode == "webhook":
        _dispatch_webhook(events, config.get("webhook_url", ""))
    elif mode == "github_issue":
        _dispatch_github_issue(tier1 + tier2, config)


def _dispatch_print(events: list):
    """Print all events to stdout."""
    print()
    for e in events:
        print(e.to_markdown())
        print("─" * 40)


def _dispatch_file(events: list, output_dir: str):
    """Write events to timestamped JSON and Markdown files."""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    json_path = out / f"events_{ts}.json"
    md_path   = out / f"events_{ts}.md"

    data = {
        "generated_at":   datetime.now(timezone.utc).isoformat(),
        "sportmind_version": VERSION,
        "listener_version":  LISTENER_VERSION,
        "total_events":   len(events),
        "events":         [e.to_dict() for e in events],
    }

    json_path.write_text(json.dumps(data, indent=2))
    md_content = f"# SportMind Intelligence Listener — {ts}\n\n"
    md_content += "\n".join(e.to_markdown() for e in events)
    md_path.write_text(md_content)

    print(f"\n  Written: {json_path}")
    print(f"  Written: {md_path}")


def _dispatch_webhook(events: list, webhook_url: str):
    """POST events to a webhook URL (Slack, Discord, custom)."""
    if not webhook_url:
        webhook_url = os.getenv("ALERT_WEBHOOK_URL", "")
    if not webhook_url:
        print("  [ERROR] No webhook URL configured.")
        return
    if not HAS_REQUESTS:
        print("  [ERROR] requests library required for webhook dispatch.")
        return

    # Build a concise webhook payload (Slack-compatible blocks format)
    tier1 = [e for e in events if e.tier == TIER_1]
    tier2 = [e for e in events if e.tier == TIER_2]

    text = f"*SportMind Intelligence Listener* — {len(events)} events\n"
    if tier1:
        text += f":red_circle: *TIER 1 — Act immediately ({len(tier1)}):*\n"
        for e in tier1:
            text += f"  • {e.event_type}: {e.title[:80]}\n"
    if tier2:
        text += f":yellow_circle: *TIER 2 — Review required ({len(tier2)}):*\n"
        for e in tier2[:5]:  # cap at 5 for readability
            text += f"  • {e.event_type}: {e.title[:80]}\n"

    payload = {"text": text, "events": [e.to_dict() for e in events]}
    try:
        r = requests.post(webhook_url, json=payload, timeout=10)
        print(f"  Webhook dispatched: {r.status_code}")
    except Exception as ex:
        print(f"  [ERROR] Webhook failed: {ex}")


def _dispatch_github_issue(events: list, config: dict):
    """Create GitHub issues for Tier 1 and Tier 2 events."""
    token = os.getenv("GITHUB_TOKEN", config.get("github_token", ""))
    repo  = os.getenv("GITHUB_REPO", config.get("github_repo", ""))
    if not token or not repo:
        print("  [ERROR] GITHUB_TOKEN and GITHUB_REPO required for GitHub dispatch.")
        return
    if not HAS_REQUESTS:
        print("  [ERROR] requests library required for GitHub dispatch.")
        return

    api = f"https://api.github.com/repos/{repo}/issues"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}

    for e in events:
        label = "tier-1-intelligence" if e.tier == TIER_1 else "tier-2-intelligence"
        issue = {
            "title": f"[{e.tier}] {e.event_type}: {e.title[:80]}",
            "body":  e.to_markdown() + f"\n\n---\n*Auto-detected by SportMind Intelligence Listener v{LISTENER_VERSION}*",
            "labels": [label, "intelligence-update"],
        }
        try:
            r = requests.post(api, json=issue, headers=headers, timeout=10)
            if r.status_code == 201:
                print(f"  Issue created: {r.json().get('html_url','')}")
            else:
                print(f"  [ERROR] Issue creation failed: {r.status_code}")
        except Exception as ex:
            print(f"  [ERROR] GitHub issue: {ex}")
        time.sleep(1)  # Rate limit courtesy


# ── CUSTOM SOURCES ────────────────────────────────────────────────────────────

def load_custom_sources(path: str) -> dict:
    """
    Load operator-defined custom sources from a JSON config file.

    Custom source format (my_sources.json):
    {
      "my_transfer_news": {
        "name": "My Transfer News Feed",
        "url": "https://example.com/transfers.rss",
        "type": "rss",
        "feed_url": "https://example.com/transfers.rss",
        "domain": "sport_domain",
        "tier_default": "TIER_2",
        "keywords": ["Arsenal", "signed", "deal"],
        "event_map": {
          "signed|joins|completes": "transfer_confirmed"
        },
        "frequency": "1h"
      },
      "my_webhook_receiver": {
        "name": "My Custom Webhook Events",
        "url": "local",
        "type": "local_json",
        "file_path": "./my_events.json",
        "domain": "custom",
        "tier_default": "TIER_2",
        "keywords": [],
        "event_map": {},
        "frequency": "on_demand"
      }
    }
    """
    p = Path(path)
    if not p.exists():
        print(f"[ERROR] Custom sources file not found: {path}")
        return {}
    try:
        data = json.loads(p.read_text())
        print(f"  Loaded {len(data)} custom source(s) from {path}")
        return data
    except json.JSONDecodeError as e:
        print(f"[ERROR] Invalid JSON in {path}: {e}")
        return {}


# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description=f"SportMind Intelligence Listener v{LISTENER_VERSION}",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/sportmind_listener.py
  python scripts/sportmind_listener.py --domain fan_token
  python scripts/sportmind_listener.py --domain macro --dispatch webhook
  python scripts/sportmind_listener.py --dry-run
  python scripts/sportmind_listener.py --custom-sources my_sources.json
  python scripts/sportmind_listener.py --dispatch file --output-dir ./detected/
  python scripts/sportmind_listener.py --dispatch github_issue
        """
    )

    parser.add_argument("--domain",
        choices=["fan_token", "macro", "sport_domain", "esports", "all"],
        default="all",
        help="Intelligence domain to monitor (default: all)")

    parser.add_argument("--dispatch",
        choices=["print", "file", "webhook", "github_issue"],
        default="print",
        help="How to route detected events (default: print)")

    parser.add_argument("--dry-run", action="store_true",
        help="Detect events but do not write files or send dispatches")

    parser.add_argument("--custom-sources",
        help="Path to custom sources JSON file")

    parser.add_argument("--output-dir", default="./detected/",
        help="Output directory for --dispatch file (default: ./detected/)")

    parser.add_argument("--webhook-url",
        help="Webhook URL for --dispatch webhook (overrides ALERT_WEBHOOK_URL)")

    parser.add_argument("--github-repo",
        help="GitHub repo slug for --dispatch github_issue e.g. SportMind/SportMind")

    parser.add_argument("--min-confidence", type=float, default=0.60,
        help="Minimum confidence threshold for event detection (default: 0.60)")

    parser.add_argument("--tier", choices=["1", "2", "3", "all"], default="all",
        help="Only dispatch events at this tier or above (default: all)")

    parser.add_argument("--version", action="store_true",
        help="Print version and exit")

    args = parser.parse_args()

    if args.version:
        print(f"SportMind Intelligence Listener v{LISTENER_VERSION}")
        print(f"SportMind library v{VERSION}")
        sys.exit(0)

    # ── STARTUP ───────────────────────────────────────────────────────────────
    print(f"SportMind Intelligence Listener v{LISTENER_VERSION}")
    print(f"Library: v{VERSION} | {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    if args.dry_run:
        print("[DRY RUN MODE — no files written, no dispatches sent]")
    print(f"Domain: {args.domain} | Dispatch: {args.dispatch}")
    print("─" * 60)

    if not HAS_REQUESTS:
        print("[WARNING] requests library not installed.")
        print("Install with: pip install requests")
    if not HAS_FEEDPARSER:
        print("[WARNING] feedparser not installed — RSS sources unavailable.")
        print("Install with: pip install feedparser")

    # ── LOAD SOURCES ──────────────────────────────────────────────────────────
    all_sources = dict(BUILT_IN_SOURCES)

    if args.custom_sources:
        custom = load_custom_sources(args.custom_sources)
        all_sources.update(custom)
        print(f"  Total sources: {len(all_sources)} ({len(BUILT_IN_SOURCES)} built-in + {len(custom)} custom)")
    else:
        print(f"  Built-in sources: {len(all_sources)}")

    # ── RUN DOMAINS ───────────────────────────────────────────────────────────
    all_events = []

    domains_to_check = (
        ["fan_token", "macro", "sport_domain", "esports"]
        if args.domain == "all"
        else [args.domain]
    )

    for domain in domains_to_check:
        domain_events = check_domain(domain, all_sources, args.dry_run)
        all_events.extend(domain_events)

    # ── FILTER BY CONFIDENCE AND TIER ─────────────────────────────────────────
    all_events = [e for e in all_events if e.confidence >= args.min_confidence]

    if args.tier != "all":
        tier_map = {"1": TIER_1, "2": TIER_2, "3": TIER_3}
        target_tiers = {TIER_1, TIER_2, TIER_3}
        if args.tier == "1":
            target_tiers = {TIER_1}
        elif args.tier == "2":
            target_tiers = {TIER_1, TIER_2}
        all_events = [e for e in all_events if e.tier in target_tiers]

    # ── DISPATCH ──────────────────────────────────────────────────────────────
    dispatch_config = {
        "output_dir":   args.output_dir,
        "webhook_url":  args.webhook_url or os.getenv("ALERT_WEBHOOK_URL", ""),
        "github_repo":  args.github_repo or os.getenv("GITHUB_REPO", ""),
    }

    dispatch_events(all_events, args.dispatch, dispatch_config, args.dry_run)

    # ── EXIT CODE ─────────────────────────────────────────────────────────────
    # Non-zero exit if Tier 1 events detected (useful for CI/CD)
    tier1_count = sum(1 for e in all_events if e.tier == TIER_1)
    if tier1_count > 0 and not args.dry_run:
        print(f"\n[EXIT 1] {tier1_count} Tier 1 event(s) require immediate action.")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
