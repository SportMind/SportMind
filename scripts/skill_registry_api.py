#!/usr/bin/env python3
"""
SportMind Skill Registry API.
Serves platform/skill-registry.md as a queryable JSON endpoint.

This script reads the static skill registry and provides:
  - Full registry as JSON
  - Query by sport, type, tier, or status
  - Minimum viable skill sets for common use cases
  - Skill metadata for any skill ID

Usage:
    # Start as a simple HTTP server
    python scripts/skill_registry_api.py --serve --port 8080

    # Query from command line
    python scripts/skill_registry_api.py --query sport=football
    python scripts/skill_registry_api.py --query type=domain
    python scripts/skill_registry_api.py --query id=domain.football
    python scripts/skill_registry_api.py --mvs fan_token_tier1 sport=football

    # Export full registry as JSON
    python scripts/skill_registry_api.py --export > registry.json

See platform/skill-registry.md for the full skill catalogue.
See platform/api-contracts.md for skill contract specifications.
"""

import argparse
import json
import re
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

REGISTRY_FILE = Path("platform/skill-registry.md")
BASE_DIR = Path(".")

# ── Registry data ─────────────────────────────────────────────────────────────

def build_registry() -> dict:
    """
    Parse platform/skill-registry.md into a structured registry dictionary.
    Returns skill entries indexed by skill_id.
    """
    try:
        content = REGISTRY_FILE.read_text()
    except FileNotFoundError:
        print(f"ERROR: {REGISTRY_FILE} not found. Run from SportMind root directory.")
        sys.exit(1)

    registry = {
        "schema_version": "1.0",
        "source": str(REGISTRY_FILE),
        "skills": {}
    }

    # Parse stable L1 skills from table
    l1_pattern = re.compile(
        r'\| `(domain\.\S+)` \| (.+?) \| (.+?) \| `(.+?)` \|'
    )
    for match in l1_pattern.finditer(content):
        skill_id, sport, differentiator, contract = match.groups()
        registry["skills"][skill_id] = {
            "skill_id": skill_id,
            "type": "domain",
            "sport": sport.strip(),
            "layer": 1,
            "status": "stable",
            "key_differentiator": differentiator.strip(),
            "contract": contract.strip(),
            "file": f"sports/{sport.strip().lower().replace(' / ', '/').split('/')[0].replace(' ', '-')}/",
        }

    # Parse L2 athlete skills
    l2_pattern = re.compile(
        r'\| `(athlete\.\S+)` \| (.+?) \| (.+?) \| `(.+?)` \|'
    )
    for match in l2_pattern.finditer(content):
        skill_id, sport, modifier_var, contract = match.groups()
        registry["skills"][skill_id] = {
            "skill_id": skill_id,
            "type": "athlete",
            "sport": sport.strip(),
            "layer": 2,
            "status": "stable",
            "primary_modifier_variable": modifier_var.strip(),
            "contract": contract.strip(),
        }

    # Parse L3 fan token skills
    l3_pattern = re.compile(
        r'\| `(fantoken\.\S+)` \| (.+?) \| (.+?) \| `(.+?)` \|'
    )
    for match in l3_pattern.finditer(content):
        skill_id, purpose_or_metrics, key_output, contract = match.groups()
        registry["skills"][skill_id] = {
            "skill_id": skill_id,
            "type": "fantoken",
            "layer": 3,
            "status": "stable",
            "key_metrics": purpose_or_metrics.strip(),
            "key_output": key_output.strip(),
            "contract": contract.strip(),
        }

    # Parse macro skills
    macro_pattern = re.compile(
        r'\| `(macro\.\S+)` \| (.+?) \| (.+?) \|'
    )
    for match in macro_pattern.finditer(content):
        skill_id, category, key_signal = match.groups()
        registry["skills"][skill_id] = {
            "skill_id": skill_id,
            "type": "macro",
            "layer": 5,
            "status": "stable",
            "category": category.strip(),
            "key_signal": key_signal.strip(),
        }

    # Add stub L1 skills
    stubs = [
        "domain.badminton", "domain.volleyball", "domain.table-tennis",
        "domain.sailing", "domain.triathlon", "domain.field-hockey",
        "domain.squash", "domain.curling", "domain.gymnastics",
        "domain.weightlifting", "domain.judo", "domain.taekwondo",
        "domain.fencing", "domain.swimming-open-water"
    ]
    for stub_id in stubs:
        sport = stub_id.replace("domain.", "")
        registry["skills"][stub_id] = {
            "skill_id": stub_id,
            "type": "domain",
            "layer": 1,
            "status": "stub",
            "sport": sport,
            "contract": "signal.domain",
            "contributor_info": "See GOOD_FIRST_ISSUES.md to claim this stub"
        }

    return registry


# ── Minimum viable skill sets ────────────────────────────────────────────────

MINIMUM_VIABLE_SETS = {
    "domain_query": {
        "description": "Quick sport domain question — no token analysis",
        "skills": ["domain.{sport}", "core.confidence-schema"],
        "estimated_tokens": "4000–8000"
    },
    "pre_match": {
        "description": "Pre-match prediction — no active tokens",
        "skills": [
            "domain.{sport}", "athlete.{sport}",
            "core.athlete-modifier", "core.confidence-schema"
        ],
        "conditional": {
            "injury_concern": "core.injury-master",
            "outdoor_weather": "core.weather",
            "heavy_schedule": "core.congestion",
            "active_macro": "macro.overview"
        },
        "estimated_tokens": "10000–18000"
    },
    "fan_token_tier1": {
        "description": "Full fan token analysis — Tier 1 sport with active tokens",
        "skills": [
            "fantoken.why", "macro.overview", "market.{sport}",
            "domain.{sport}", "athlete.{sport}",
            "fantoken.pulse", "fantoken.{sport}-bridge",
            "core.athlete-modifier", "core.confidence-schema"
        ],
        "conditional": {
            "defi_check_needed": "fantoken.defi-liquidity",
            "lifecycle_assessment": "fantoken.lifecycle",
            "high_narrative": "core.narrative"
        },
        "estimated_tokens": "25000–45000"
    },
    "commercial_brief": {
        "description": "Commercial intelligence brief for clubs, agents, brands",
        "skills": [
            "fantoken.why", "fantoken.pulse",
            "fantoken.performance-on-pitch", "fantoken.athlete-social-activity",
            "fantoken.brand-score", "fantoken.sponsorship-match",
            "fantoken.lifecycle", "fantoken.partnership-intel",
            "core.confidence-schema"
        ],
        "estimated_tokens": "30000–50000"
    },
    "defi_check": {
        "description": "Pre-execution liquidity check only",
        "skills": [
            "fantoken.defi-liquidity", "fantoken.lifecycle",
            "core.confidence-schema"
        ],
        "estimated_tokens": "6000–10000"
    }
}


# ── Query functions ──────────────────────────────────────────────────────────

def query_registry(registry: dict, filters: dict) -> list:
    """Filter registry by sport, type, layer, status, or skill_id."""
    results = list(registry["skills"].values())

    if "sport" in filters:
        sport = filters["sport"].lower()
        results = [s for s in results
                   if sport in s.get("sport", "").lower()
                   or sport in s.get("skill_id", "").lower()]

    if "type" in filters:
        results = [s for s in results if s.get("type") == filters["type"]]

    if "layer" in filters:
        results = [s for s in results if str(s.get("layer", "")) == str(filters["layer"])]

    if "status" in filters:
        results = [s for s in results if s.get("status") == filters["status"]]

    if "id" in filters:
        results = [s for s in results if s.get("skill_id") == filters["id"]]

    return results


def get_mvs(use_case: str, sport: str = None) -> dict:
    """Get minimum viable skill set for a use case, optionally with sport substitution."""
    if use_case not in MINIMUM_VIABLE_SETS:
        return {"error": f"Unknown use case: {use_case}. Available: {list(MINIMUM_VIABLE_SETS.keys())}"}

    mvs = dict(MINIMUM_VIABLE_SETS[use_case])

    if sport:
        mvs["skills"] = [s.replace("{sport}", sport) for s in mvs["skills"]]
        if "conditional" in mvs:
            pass  # Conditional skills keep {sport} placeholder for developer substitution

    return mvs


# ── HTTP Server ───────────────────────────────────────────────────────────────

class RegistryHandler(BaseHTTPRequestHandler):
    """Simple HTTP handler for registry API."""

    registry = None  # Set at server start

    def do_GET(self):
        parsed = urlparse(self.path)
        params = {k: v[0] for k, v in parse_qs(parsed.query).items()}

        if parsed.path == "/" or parsed.path == "/skills":
            # Full registry or filtered
            results = query_registry(self.registry, params)
            self._respond({"count": len(results), "skills": results})

        elif parsed.path == "/skills/mvs":
            use_case = params.get("use_case", "pre_match")
            sport = params.get("sport")
            self._respond(get_mvs(use_case, sport))

        elif parsed.path.startswith("/skills/"):
            skill_id = parsed.path.replace("/skills/", "")
            skill = self.registry["skills"].get(skill_id)
            if skill:
                self._respond(skill)
            else:
                self._respond({"error": f"Skill not found: {skill_id}"}, 404)

        elif parsed.path == "/health":
            self._respond({
                "status": "ok",
                "total_skills": len(self.registry["skills"]),
                "version": self.registry.get("schema_version", "1.0")
            })

        else:
            self._respond({"error": "Not found", "available_paths": [
                "/skills", "/skills?sport=football", "/skills?type=domain",
                "/skills/{skill_id}", "/skills/mvs?use_case=fan_token_tier1&sport=football",
                "/health"
            ]}, 404)

    def _respond(self, data: dict, status: int = 200):
        body = json.dumps(data, indent=2).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(body))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {format % args}")


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="SportMind Skill Registry API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/skill_registry_api.py --serve --port 8080
  python scripts/skill_registry_api.py --query sport=football
  python scripts/skill_registry_api.py --query type=domain status=stable
  python scripts/skill_registry_api.py --query id=domain.football
  python scripts/skill_registry_api.py --mvs fan_token_tier1 --sport football
  python scripts/skill_registry_api.py --export > registry.json
  python scripts/skill_registry_api.py --stats
        """
    )
    parser.add_argument("--serve", action="store_true", help="Start HTTP server")
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument("--query", nargs="*", metavar="KEY=VALUE",
                        help="Query skills by filters (sport, type, layer, status, id)")
    parser.add_argument("--mvs", metavar="USE_CASE",
                        help="Get minimum viable skill set for a use case")
    parser.add_argument("--sport", metavar="SPORT",
                        help="Sport for --mvs substitution")
    parser.add_argument("--export", action="store_true",
                        help="Export full registry as JSON")
    parser.add_argument("--stats", action="store_true",
                        help="Show registry statistics")
    args = parser.parse_args()

    registry = build_registry()

    if args.serve:
        RegistryHandler.registry = registry
        server = HTTPServer(("0.0.0.0", args.port), RegistryHandler)
        print(f"SportMind Skill Registry API")
        print(f"Serving {len(registry['skills'])} skills on http://localhost:{args.port}")
        print(f"Try: http://localhost:{args.port}/skills?sport=football")
        print(f"     http://localhost:{args.port}/skills/domain.football")
        print(f"     http://localhost:{args.port}/skills/mvs?use_case=fan_token_tier1&sport=football")
        print("Ctrl+C to stop.")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

    elif args.query is not None:
        filters = {}
        for item in (args.query or []):
            if "=" in item:
                k, v = item.split("=", 1)
                filters[k] = v
        results = query_registry(registry, filters)
        print(json.dumps({"count": len(results), "skills": results}, indent=2))

    elif args.mvs:
        result = get_mvs(args.mvs, args.sport)
        print(json.dumps(result, indent=2))

    elif args.export:
        print(json.dumps(registry, indent=2))

    elif args.stats:
        skills = registry["skills"].values()
        by_type = {}
        by_status = {}
        for s in skills:
            t = s.get("type", "unknown")
            st = s.get("status", "unknown")
            by_type[t] = by_type.get(t, 0) + 1
            by_status[st] = by_status.get(st, 0) + 1

        print(f"\nSportMind Skill Registry — Statistics")
        print(f"{'=' * 40}")
        print(f"Total skills: {len(registry['skills'])}")
        print(f"\nBy type:")
        for t, count in sorted(by_type.items()):
            print(f"  {t}: {count}")
        print(f"\nBy status:")
        for st, count in sorted(by_status.items()):
            print(f"  {st}: {count}")
        print(f"\nUse cases available:")
        for uc in MINIMUM_VIABLE_SETS:
            print(f"  {uc}: {MINIMUM_VIABLE_SETS[uc]['description']}")

    else:
        parser.print_help()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
