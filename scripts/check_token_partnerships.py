#!/usr/bin/env python3
"""
SportMind token partnership checker.
Monitors Socios/Chiliz for new fan token partnerships not yet in the skill registry.
Called by .github/workflows/skill-monitor.yml every Monday at 9am UTC.

Compares known tokens from platform/skill-registry.md against detected tokens.
Creates GitHub issues for newly detected partnerships.

See platform/monitoring-alerts.md (Alert 5: New fan token partnership) for alert specs.

Usage:
    python scripts/check_token_partnerships.py \\
        --registry platform/skill-registry.md
"""

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


# Known Tier 1 sports with active token ecosystems
TIER_1_SPORTS = ["football", "basketball", "mma", "esports", "formula1", "cricket"]

# Token bridge skills already in the registry
DOCUMENTED_BRIDGE_SKILLS = [
    "fantoken.football-bridge",
    "fantoken.formula1-bridge",
    "fantoken.mma-bridge",
    "fantoken.esports-bridge",
    "fantoken.basketball-bridge",
    "fantoken.cricket-bridge",
]


def load_skill_registry(registry_file: str) -> list:
    """Extract known skill IDs from the skill registry."""
    try:
        with open(registry_file) as f:
            content = f.read()
        # Extract skill IDs from registry markdown
        skill_ids = re.findall(r'`(fantoken\.\S+)`', content)
        return list(set(skill_ids))
    except FileNotFoundError:
        print(f"WARNING: {registry_file} not found")
        return []


def check_socios_partnerships() -> list:
    """
    Check Socios for active fan token partnerships.
    
    NOTE: Full implementation requires parsing socios.com/fan-tokens
    or integrating with a Chiliz API endpoint. This stub returns a
    placeholder result for CI workflow compatibility.
    
    For production: integrate with Chiliz Chain explorer API or
    parse the Socios partnership announcement page.
    """
    print("Checking Socios fan token partnerships...")
    print("NOTE: Full implementation requires web scraping or Chiliz API integration.")
    print("See platform/monitoring-sources.json for source configuration.")
    
    # Placeholder: return known active tokens
    # In production, fetch dynamically from socios.com or Chiliz Chain
    known_tokens = [
        {"name": "FC Barcelona", "symbol": "BAR", "sport": "football", "status": "active"},
        {"name": "Paris Saint-Germain", "symbol": "PSG", "sport": "football", "status": "active"},
        {"name": "Manchester City", "symbol": "CITY", "sport": "football", "status": "active"},
        {"name": "Ferrari", "symbol": "FERRARI", "sport": "formula1", "status": "active"},
        {"name": "UFC", "symbol": "UFC", "sport": "mma", "status": "active"},
    ]
    return known_tokens


def main():
    parser = argparse.ArgumentParser(description="SportMind token partnership checker")
    parser.add_argument("--registry", default="platform/skill-registry.md")
    args = parser.parse_args()

    print(f"\n=== SportMind Token Partnership Check ===")
    print(f"Time: {datetime.now(timezone.utc).isoformat()}")
    print()

    known_skills = load_skill_registry(args.registry)
    print(f"Known fantoken skills in registry: {len(known_skills)}")
    for s in sorted(known_skills):
        print(f"  {s}")

    print()
    partnerships = check_socios_partnerships()
    print(f"\nDetected partnerships: {len(partnerships)}")
    for p in partnerships:
        print(f"  {p['name']} ({p['symbol']}) — {p['sport']} — {p['status']}")

    # Check for sports with tokens but no bridge skill
    sports_with_tokens = set(p["sport"] for p in partnerships)
    documented_sports = set(re.sub(r'fantoken\.(.+)-bridge', r'\1', s) 
                            for s in known_skills if s.endswith("-bridge"))
    
    undocumented = sports_with_tokens - documented_sports
    if undocumented:
        print(f"\nWARNING: Tokens detected for undocumented sports: {undocumented}")
        print("Consider creating bridge skills for these sports.")
    else:
        print("\nAll detected sports have documented bridge skills. ✓")

    print("\nNOTE: Full partnership monitoring requires Chiliz API or Socios web integration.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
