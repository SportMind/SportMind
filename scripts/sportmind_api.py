#!/usr/bin/env python3
"""
SportMind Skills API — Content Delivery and Registry.

The hosted API for SportMind. Serves skill intelligence content on demand —
agents and developers call it to receive skill file contents ready for injection
into agent context, without cloning or managing the repository.

This is the completion of the platform layer:
  platform/skill-registry.md     → what skills exist (catalogue)
  platform/api-contracts.md      → how to call skills (contracts)
  scripts/sportmind_api.py       → serves content on demand (this file)

OBJECTIVES:
  1. Agents fetch fresh SportMind intelligence at query time
  2. Developers access skills via API — no repository management required
  3. Minimum viable skill stacks delivered as a single API call
  4. GitHub Pages deployment for hosted, versioned, public access

USAGE — HTTP server:
  python scripts/sportmind_api.py --serve --port 8080

  GET /                                    API info and available endpoints
  GET /health                              Health check + library version
  GET /skills                              Full registry (metadata)
  GET /skills?sport=football               Filter by sport
  GET /skills?type=domain                  Filter by type
  GET /skills/{skill_id}                   Single skill metadata
  GET /skills/{skill_id}/content           Single skill CONTENT (full markdown)
  GET /skills/mvs/{use_case}               MVS metadata for use case
  GET /skills/mvs/{use_case}/content       Full MVS CONTENT — ready for agent injection
  GET /stack?sport=football&use_case=fan_token_tier1  Combined metadata + content
  GET /macro-state                         Current macro state (from platform/macro-state.json)

USAGE — CLI:
  python scripts/sportmind_api.py --content domain.football
  python scripts/sportmind_api.py --stack fan_token_tier1 --sport football
  python scripts/sportmind_api.py --export-github-pages ./docs/api
  python scripts/sportmind_api.py --stats

See platform/skill-registry-api.md for hosted endpoint documentation.
See platform/api-contracts.md for skill contract specifications.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

# ── Constants ─────────────────────────────────────────────────────────────────
REGISTRY_FILE   = Path("platform/skill-registry.md")
MACRO_STATE_FILE = Path("platform/macro-state.json")
BASE_DIR        = Path(".")
API_VERSION = "3.71.0"
LIBRARY_VERSION = "3.71.0"


# ── Skill ID → file path mapping ─────────────────────────────────────────────

def build_file_map() -> dict:
    """
    Map every skill ID to its file path within the SportMind repository.
    Returns dict of {skill_id: relative_file_path}.
    """
    m = {}

    # Layer 1 — domain skills
    sports_dir = BASE_DIR / "sports"
    if sports_dir.exists():
        for sport_dir in sorted(sports_dir.iterdir()):
            if sport_dir.is_dir():
                files = list(sport_dir.glob("sport-domain-*.md"))
                if files:
                    m[f"domain.{sport_dir.name}"] = str(files[0].relative_to(BASE_DIR))

    # Layer 2 — athlete skills
    athlete_dir = BASE_DIR / "athlete"
    if athlete_dir.exists():
        id_overrides = {
            "nfl": "athlete.nfl", "nba": "athlete.nba", "nhl": "athlete.nhl",
            "meta": "athlete.meta", "rugby": "athlete.rugby",
            "rugby-league": "athlete.rugby-league", "baseball": "athlete.baseball",
            "horse-racing": "athlete.horse-racing", "winter-sports": "athlete.winter-sports",
        }
        for a_dir in sorted(athlete_dir.iterdir()):
            if a_dir.is_dir():
                skill_id = id_overrides.get(a_dir.name, f"athlete.{a_dir.name}")
                files = list(a_dir.glob("athlete-intel-*.md"))
                if files:
                    m[skill_id] = str(files[0].relative_to(BASE_DIR))

    # Layer 3 — fan token skills
    ft_map = {
        "fan-token-pulse":                "fantoken.pulse",
        "performance-on-pitch":           "fantoken.performance-on-pitch",
        "performance-off-pitch":          "fantoken.performance-off-pitch",
        "athlete-social-lift":            "fantoken.athlete-social-lift",
        "athlete-social-activity":        "fantoken.athlete-social-activity",
        "transfer-signal":                "fantoken.transfer-signal",
        "transfer-intelligence":          "fantoken.transfer-intelligence",
        "brand-score":                    "fantoken.brand-score",
        "sponsorship-match":              "fantoken.sponsorship-match",
        "sports-brand-sponsorship":       "fantoken.sports-brand-sponsorship",
        "football-token-intelligence":    "fantoken.football-bridge",
        "formula1-token-intelligence":    "fantoken.formula1-bridge",
        "mma-token-intelligence":         "fantoken.mma-bridge",
        "esports-token-intelligence":     "fantoken.esports-bridge",
        "basketball-token-intelligence":  "fantoken.basketball-bridge",
        "cricket-token-intelligence":     "fantoken.cricket-bridge",
        "nfl-token-intelligence":         "fantoken.nfl-bridge",
        "afl-token-intelligence":         "fantoken.afl-bridge",
        "rugby-token-intelligence":       "fantoken.rugby-bridge",
        "fan-token-lifecycle":            "fantoken.lifecycle",
        "fan-token-partnership-intelligence": "fantoken.partnership-intel",
        "blockchain-validator-intelligence":  "fantoken.validator-intel",
        "defi-liquidity-intelligence":    "fantoken.defi-liquidity",
    }
    ft_dir = BASE_DIR / "fan-token"
    if ft_dir.exists():
        for dir_name, skill_id in ft_map.items():
            d = ft_dir / dir_name
            if d.is_dir():
                files = list(d.glob("*.md"))
                if files:
                    m[skill_id] = str(files[0].relative_to(BASE_DIR))

    # Special root L3 files
    if (ft_dir / "fan-token-why.md").exists():
        m["fantoken.why"] = "fan-token/fan-token-why.md"

    # Layer 4 — market skills
    market_dir = BASE_DIR / "market"
    if market_dir.exists():
        for f in sorted(market_dir.glob("market-*.md")):
            sport = f.stem.replace("market-", "")
            m[f"market.{sport}"] = str(f.relative_to(BASE_DIR))
        if (market_dir / "market-overview.md").exists():
            m["market.overview"] = "market/market-overview.md"
        if (market_dir / "market-key-findings.md").exists():
            m["market.key-findings"] = "market/market-key-findings.md"
        if (market_dir / "world-cup-2026.md").exists():
            m["market.world-cup-2026"] = "market/world-cup-2026.md"

    # Layer 5 — macro skills
    macro_map = {
        "macro.overview":      "macro/macro-overview.md",
        "macro.pandemic":      "macro/macro-pandemic-public-health.md",
        "macro.geopolitical":  "macro/macro-geopolitical.md",
        "macro.crypto-cycles": "macro/macro-crypto-market-cycles.md",
        "macro.broadcast":     "macro/macro-broadcast-disruption.md",
        "macro.economic":      "macro/macro-economic-cycles.md",
        "macro.climate":       "macro/macro-climate-weather.md",
        "macro.governance":    "macro/macro-governance-scandal.md",
    }
    for sid, path in macro_map.items():
        if (BASE_DIR / path).exists():
            m[sid] = path

    # Core skills
    core_map = {
        "core.confidence-schema":  "core/confidence-output-schema.md",
        "core.athlete-modifier":   "core/core-athlete-modifier-system.md",
        "core.signal-weights":     "core/core-signal-weights-by-sport.md",
        "core.result-matrices":    "core/core-result-impact-matrices.md",
        "core.officiating":        "core/core-officiating-intelligence.md",
        "core.weather":            "core/core-weather-match-day.md",
        "core.congestion":         "core/core-fixture-congestion.md",
        "core.draft-intel":        "core/core-draft-intelligence.md",
        "core.narrative":          "core/core-narrative-momentum.md",
        "core.data-sources":       "core/data-sources.md",
        "core.context-window":     "core/context-window-management.md",
        "core.multi-agent":        "core/multi-agent-coordination.md",
        "core.sportmind-score":    "core/sportmind-score.md",
        "core.calibration":        "core/calibration-framework.md",
        "core.live-signals":       "platform/live-signals.md",
        "core.injury-master":      "core/injury-intelligence/core-injury-intelligence.md",
    }
    for sid, path in core_map.items():
        if (BASE_DIR / path).exists():
            m[sid] = path

    # Platform files
    platform_map = {
        "platform.overview":       "platform/platform-overview.md",
        "platform.api-contracts":  "platform/api-contracts.md",
        "platform.skill-registry": "platform/skill-registry.md",
        "platform.integration":    "platform/integration-partners.md",
        "platform.monitoring":     "platform/monitoring-alerts.md",
    }
    for sid, path in platform_map.items():
        if (BASE_DIR / path).exists():
            m[sid] = path

    return m


# ── Registry (metadata) ───────────────────────────────────────────────────────

def build_registry(file_map: dict) -> dict:
    """Build skill metadata registry from skill-registry.md."""
    registry = {
        "api_version": API_VERSION,
        "library_version": LIBRARY_VERSION,
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_skills": 0,
        "skills": {}
    }

    try:
        content = REGISTRY_FILE.read_text()
    except FileNotFoundError:
        return registry

    # L1 domain
    for m in re.finditer(r'\| `(domain\.\S+)` \| (.+?) \| (.+?) \| `(.+?)` \|', content):
        sid, sport, diff, contract = m.groups()
        registry["skills"][sid] = {
            "skill_id": sid, "type": "domain", "sport": sport.strip(),
            "layer": 1, "status": "stable",
            "key_differentiator": diff.strip(), "contract": contract.strip(),
            "content_available": sid in file_map,
            "file_path": file_map.get(sid, ""),
        }

    # L2 athlete
    for m in re.finditer(r'\| `(athlete\.\S+)` \| (.+?) \| (.+?) \| `(.+?)` \|', content):
        sid, sport, modifier_var, contract = m.groups()
        registry["skills"][sid] = {
            "skill_id": sid, "type": "athlete", "sport": sport.strip(),
            "layer": 2, "status": "stable",
            "primary_modifier_variable": modifier_var.strip(),
            "contract": contract.strip(),
            "content_available": sid in file_map,
            "file_path": file_map.get(sid, ""),
        }

    # L3 fantoken
    for m in re.finditer(r'\| `(fantoken\.\S+)` \| (.+?) \| (.+?) \| `(.+?)` \|', content):
        sid, metrics, output, contract = m.groups()
        registry["skills"][sid] = {
            "skill_id": sid, "type": "fantoken",
            "layer": 3, "status": "stable",
            "key_metrics": metrics.strip(), "key_output": output.strip(),
            "contract": contract.strip(),
            "content_available": sid in file_map,
            "file_path": file_map.get(sid, ""),
        }

    # L5 macro
    for m in re.finditer(r'\| `(macro\.\S+)` \| (.+?) \| (.+?) \|', content):
        sid, category, signal = m.groups()
        registry["skills"][sid] = {
            "skill_id": sid, "type": "macro",
            "layer": 5, "status": "stable",
            "category": category.strip(), "key_signal": signal.strip(),
            "content_available": sid in file_map,
            "file_path": file_map.get(sid, ""),
        }

    # Stub L1 skills
    stubs = [
        "domain.badminton", "domain.volleyball", "domain.table-tennis",
        "domain.sailing", "domain.triathlon", "domain.field-hockey",
        "domain.squash", "domain.curling", "domain.gymnastics",
        "domain.weightlifting", "domain.judo", "domain.taekwondo",
        "domain.fencing", "domain.swimming-open-water"
    ]
    for sid in stubs:
        registry["skills"][sid] = {
            "skill_id": sid, "type": "domain", "layer": 1, "status": "stub",
            "sport": sid.replace("domain.", ""), "contract": "signal.domain",
            "content_available": True,
            "file_path": file_map.get(sid, ""),
            "note": "Stub — community contribution welcome (GOOD_FIRST_ISSUES.md)"
        }

    # Add any file_map entries not yet in registry (market, core, platform)
    for sid, path in file_map.items():
        if sid not in registry["skills"]:
            skill_type = sid.split(".")[0]
            registry["skills"][sid] = {
                "skill_id": sid, "type": skill_type,
                "status": "stable", "content_available": True,
                "file_path": path,
            }

    registry["total_skills"] = len(registry["skills"])
    return registry


# ── Content delivery ──────────────────────────────────────────────────────────

def get_skill_content(skill_id: str, file_map: dict, include_hash: bool = True) -> dict:
    """Load and return the full content of a skill file, with optional integrity hash."""
    if skill_id not in file_map:
        return {"error": f"Skill '{skill_id}' not found or has no content file"}

    file_path = BASE_DIR / file_map[skill_id]
    if not file_path.exists():
        return {"error": f"File not found: {file_map[skill_id]}"}

    content = file_path.read_text(encoding="utf-8")
    result = {
        "skill_id": skill_id,
        "file_path": file_map[skill_id],
        "content": content,
        "content_length": len(content),
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "api_version": API_VERSION,
    }

    # Include SHA-256 hash for integrity verification
    if include_hash:
        import hashlib
        result["sha256"] = hashlib.sha256(content.encode("utf-8")).hexdigest()
        result["integrity_note"] = (
            "Verify this hash against platform/skill-hashes.json "            "to confirm content integrity. See SECURITY.md."
        )

    return result


def get_stack_content(use_case: str, sport: str, file_map: dict) -> dict:
    """
    Return the full content stack for a use case.
    This is the primary agent integration endpoint — one call returns
    everything an agent needs to reason about a sport.
    """
    MVS = {
        "domain_query": {
            "description": "Quick sport domain question — minimum context",
            "skills": ["domain.{sport}", "core.confidence-schema"],
            "estimated_tokens": "4,000–8,000",
        },
        "pre_match": {
            "description": "Pre-match prediction — no active fan tokens",
            "skills": [
                "macro.overview", "market.{sport}",
                "domain.{sport}", "athlete.{sport}",
                "core.athlete-modifier", "core.confidence-schema",
            ],
            "estimated_tokens": "10,000–18,000",
        },
        "fan_token_tier1": {
            "description": "Full fan token signal — Tier 1 sport with active tokens",
            "skills": [
                "fantoken.why", "macro.overview",
                "market.{sport}", "domain.{sport}",
                "athlete.{sport}", "fantoken.pulse",
                "fantoken.{sport}-bridge",
                "core.athlete-modifier", "core.confidence-schema",
            ],
            "estimated_tokens": "25,000–45,000",
        },
        "commercial_brief": {
            "description": "Commercial intelligence — clubs, agents, brands",
            "skills": [
                "fantoken.why", "fantoken.pulse",
                "fantoken.performance-on-pitch",
                "fantoken.athlete-social-activity",
                "fantoken.brand-score", "fantoken.sponsorship-match",
                "fantoken.lifecycle", "fantoken.partnership-intel",
                "core.confidence-schema",
            ],
            "estimated_tokens": "30,000–50,000",
        },
        "defi_check": {
            "description": "Pre-execution liquidity check — DeFi context only",
            "skills": [
                "fantoken.defi-liquidity", "fantoken.lifecycle",
                "core.confidence-schema",
            ],
            "estimated_tokens": "6,000–10,000",
        },
    }

    if use_case not in MVS:
        return {
            "error": f"Unknown use case: '{use_case}'",
            "available": list(MVS.keys()),
        }

    stack_def = MVS[use_case]
    skill_ids = [s.replace("{sport}", sport or "") for s in stack_def["skills"]]

    # Build content stack
    stack = []
    missing = []
    total_chars = 0

    for skill_id in skill_ids:
        if "{sport}" in skill_id:
            missing.append(skill_id)
            continue
        result = get_skill_content(skill_id, file_map)
        if "error" in result:
            missing.append(skill_id)
        else:
            stack.append({
                "skill_id":  skill_id,
                "file_path": result["file_path"],
                "content":   result["content"],
            })
            total_chars += len(result["content"])

    return {
        "use_case": use_case,
        "sport": sport,
        "description": stack_def["description"],
        "estimated_tokens": stack_def["estimated_tokens"],
        "skills_requested": len(skill_ids),
        "skills_loaded": len(stack),
        "skills_missing": missing,
        "total_content_chars": total_chars,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "api_version": API_VERSION,
        "stack": stack,
        "usage_note": (
            "Inject each item in stack[].content into your agent system prompt "
            "in order. The stack is already in the recommended SportMind loading order."
        ),
    }


def get_macro_state() -> dict:
    """Return current macro state from platform/macro-state.json."""
    try:
        return json.loads(MACRO_STATE_FILE.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "error": "macro-state.json not found or invalid",
            "note": "Run scripts/check_macro_signals.py to populate",
        }


# ── GitHub Pages static export ────────────────────────────────────────────────

def export_github_pages(output_dir: str, file_map: dict, registry: dict) -> None:
    """
    Generate all static JSON files for GitHub Pages deployment.
    Creates a complete versioned API snapshot.
    """
    out = Path(output_dir)
    versioned = out / f"v{API_VERSION}"
    latest = out / "latest"

    for d in [versioned, latest]:
        d.mkdir(parents=True, exist_ok=True)

    def write(path: Path, data: dict) -> None:
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
        print(f"  Written: {path}")

    # Full registry
    write(versioned / "registry.json", registry)
    write(latest / "registry.json", registry)

    # Stable-only registry
    stable = {
        **registry,
        "skills": {k: v for k, v in registry["skills"].items()
                   if v.get("status") != "stub"},
    }
    stable["total_skills"] = len(stable["skills"])
    write(versioned / "registry-stable.json", stable)

    # Individual skill metadata
    skills_dir = versioned / "skills"
    skills_dir.mkdir(exist_ok=True)
    for skill_id, skill_data in registry["skills"].items():
        safe_id = skill_id.replace(".", "_")
        write(skills_dir / f"{safe_id}.json", skill_data)

    # Skill content files
    content_dir = versioned / "content"
    content_dir.mkdir(exist_ok=True)
    for skill_id, file_path in file_map.items():
        fp = BASE_DIR / file_path
        if fp.exists():
            safe_id = skill_id.replace(".", "_")
            content_data = {
                "skill_id": skill_id,
                "file_path": file_path,
                "content": fp.read_text(encoding="utf-8"),
                "api_version": API_VERSION,
                "library_version": LIBRARY_VERSION,
            }
            write(content_dir / f"{safe_id}.json", content_data)

    # MVS metadata
    mvs_data = {
        "domain_query":    {"description": "Quick sport domain question", "estimated_tokens": "4,000-8,000"},
        "pre_match":       {"description": "Pre-match prediction, no active tokens", "estimated_tokens": "10,000-18,000"},
        "fan_token_tier1": {"description": "Full fan token signal, Tier 1 sport", "estimated_tokens": "25,000-45,000"},
        "commercial_brief":{"description": "Commercial intelligence brief", "estimated_tokens": "30,000-50,000"},
        "defi_check":      {"description": "Pre-execution DeFi check", "estimated_tokens": "6,000-10,000"},
    }
    write(versioned / "mvs.json", {
        "api_version": API_VERSION,
        "use_cases": mvs_data,
    })

    # Macro state
    write(versioned / "macro-state.json", get_macro_state())
    write(latest / "macro-state.json", get_macro_state())

    # Index / API info
    api_info = {
        "name": "SportMind Skills API",
        "version": API_VERSION,
        "library_version": LIBRARY_VERSION,
        "description": "Open sports intelligence for AI agents and developers",
        "license": "MIT",
        "source": "https://github.com/SportMind/SportMind",
        "endpoints": {
            f"/api/v{API_VERSION}/registry.json":              "Full skill registry",
            f"/api/v{API_VERSION}/registry-stable.json":       "Stable skills only",
            f"/api/v{API_VERSION}/skills/{{skill_id}}.json":   "Individual skill metadata",
            f"/api/v{API_VERSION}/content/{{skill_id}}.json":  "Skill content (full markdown)",
            f"/api/v{API_VERSION}/mvs.json":                   "Minimum viable skill sets",
            f"/api/v{API_VERSION}/macro-state.json":           "Current macro state",
        },
    }
    write(versioned / "index.json", api_info)
    write(out / "index.json", api_info)

    print(f"\nGitHub Pages export complete: {out}")
    print(f"  Versioned: {versioned}")
    print(f"  Latest alias: {latest}")
    print(f"  Skills: {len(registry['skills'])}")
    print(f"  Content files: {len(file_map)}")


# ── HTTP Server ───────────────────────────────────────────────────────────────

class SportMindAPIHandler(BaseHTTPRequestHandler):
    """HTTP handler for the SportMind Skills API."""

    file_map = {}
    registry = {}

    def do_GET(self):
        parsed = urlparse(self.path)
        params = {k: v[0] for k, v in parse_qs(parsed.query).items()}
        path = parsed.path.rstrip("/")

        # ── Root ─────────────────────────────────────────────────────────────
        if path in ("", "/"):
            self._json({
                "name": "SportMind Skills API",
                "version": API_VERSION,
                "library_version": LIBRARY_VERSION,
                "description": "Open sports intelligence for AI agents and developers",
                "license": "MIT",
                "endpoints": {
                    "GET /health":                           "Health check",
                    "GET /skills":                           "Full registry (metadata)",
                    "GET /skills?sport=football":            "Filter by sport",
                    "GET /skills?type=domain":               "Filter by type",
                    "GET /skills/{id}":                      "Single skill metadata",
                    "GET /skills/{id}/content":              "Single skill CONTENT",
                    "GET /skills/mvs/{use_case}":            "MVS metadata",
                    "GET /skills/mvs/{use_case}/content":    "Full MVS content stack",
                    "GET /stack?sport=football&use_case=fan_token_tier1": "Content stack shortcut",
                    "GET /macro-state":                      "Current macro state",
                },
                "example_use_cases": [
                    "domain_query", "pre_match",
                    "fan_token_tier1", "commercial_brief", "defi_check"
                ],
            })

        # ── Health ───────────────────────────────────────────────────────────
        elif path == "/health":
            self._json({
                "status": "ok",
                "api_version": API_VERSION,
                "library_version": LIBRARY_VERSION,
                "total_skills": len(self.registry.get("skills", {})),
                "content_files": len(self.file_map),
                "timestamp": datetime.now(timezone.utc).isoformat(),
            })

        # ── Macro state ──────────────────────────────────────────────────────
        elif path == "/macro-state":
            self._json(get_macro_state())

        # ── Stack shortcut ───────────────────────────────────────────────────
        elif path == "/stack":
            use_case = params.get("use_case", "pre_match")
            sport = params.get("sport", "")
            self._json(get_stack_content(use_case, sport, self.file_map))

        # ── MVS endpoints ────────────────────────────────────────────────────
        elif path.startswith("/skills/mvs/"):
            parts = path.split("/")
            use_case = parts[3] if len(parts) > 3 else ""
            serve_content = len(parts) > 4 and parts[4] == "content"
            sport = params.get("sport", "")

            if serve_content:
                self._json(get_stack_content(use_case, sport, self.file_map))
            else:
                mvs_meta = {
                    "domain_query":    {"description": "Quick domain question", "estimated_tokens": "4,000–8,000"},
                    "pre_match":       {"description": "Pre-match prediction", "estimated_tokens": "10,000–18,000"},
                    "fan_token_tier1": {"description": "Full fan token analysis", "estimated_tokens": "25,000–45,000"},
                    "commercial_brief":{"description": "Commercial intelligence brief", "estimated_tokens": "30,000–50,000"},
                    "defi_check":      {"description": "Pre-execution DeFi check", "estimated_tokens": "6,000–10,000"},
                }
                if use_case in mvs_meta:
                    self._json({
                        "use_case": use_case, "sport": sport,
                        **mvs_meta[use_case],
                        "content_endpoint": f"/skills/mvs/{use_case}/content?sport={sport}",
                    })
                else:
                    self._json({"error": f"Unknown use case: {use_case}",
                                "available": list(mvs_meta.keys())}, 404)

        # ── Skills listing ───────────────────────────────────────────────────
        elif path == "/skills":
            skills = list(self.registry.get("skills", {}).values())
            if "sport" in params:
                sp = params["sport"].lower()
                skills = [s for s in skills
                          if sp in s.get("sport", "").lower()
                          or sp in s.get("skill_id", "").lower()]
            if "type" in params:
                skills = [s for s in skills if s.get("type") == params["type"]]
            if "layer" in params:
                skills = [s for s in skills if str(s.get("layer", "")) == params["layer"]]
            if "status" in params:
                skills = [s for s in skills if s.get("status") == params["status"]]
            self._json({"count": len(skills), "skills": skills})

        # ── Skill content ────────────────────────────────────────────────────
        elif path.startswith("/skills/") and path.endswith("/content"):
            skill_id = path.replace("/skills/", "").replace("/content", "")
            self._json(get_skill_content(skill_id, self.file_map))

        # ── Single skill metadata ────────────────────────────────────────────
        elif path.startswith("/skills/"):
            skill_id = path.replace("/skills/", "")
            skill = self.registry.get("skills", {}).get(skill_id)
            if skill:
                # Add content endpoint hint
                enriched = dict(skill)
                enriched["content_endpoint"] = f"/skills/{skill_id}/content"
                self._json(enriched)
            else:
                self._json({"error": f"Skill not found: {skill_id}",
                            "hint": "Try GET /skills to browse available skills"}, 404)

        else:
            self._json({"error": "Not found", "hint": "Try GET / for available endpoints"}, 404)

    def _json(self, data: dict, status: int = 200):
        body = json.dumps(data, indent=2, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", len(body))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("X-SportMind-Version", LIBRARY_VERSION)
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print(f"[{self.log_date_time_string()}] {fmt % args}")


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="SportMind Skills API — Content Delivery and Registry",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Start HTTP server
  python scripts/sportmind_api.py --serve --port 8080

  # Fetch single skill content
  python scripts/sportmind_api.py --content domain.football

  # Fetch full stack for fan token analysis
  python scripts/sportmind_api.py --stack fan_token_tier1 --sport football

  # Export for GitHub Pages
  python scripts/sportmind_api.py --export-github-pages ./docs/api

  # Show registry stats
  python scripts/sportmind_api.py --stats

  # List all skill IDs with content
  python scripts/sportmind_api.py --list-ids
        """,
    )
    parser.add_argument("--serve", action="store_true",
                        help="Start HTTP server")
    parser.add_argument("--port", type=int, default=8080,
                        help="HTTP server port (default: 8080)")
    parser.add_argument("--content", metavar="SKILL_ID",
                        help="Fetch content of a specific skill")
    parser.add_argument("--stack", metavar="USE_CASE",
                        help="Fetch full content stack for a use case")
    parser.add_argument("--sport", metavar="SPORT",
                        help="Sport for --stack (e.g. football, mma, cricket)")
    parser.add_argument("--export-github-pages", metavar="OUTPUT_DIR",
                        help="Export all static JSON for GitHub Pages")
    parser.add_argument("--stats", action="store_true",
                        help="Show library and API statistics")
    parser.add_argument("--list-ids", action="store_true",
                        help="List all skill IDs with available content")
    args = parser.parse_args()

    file_map = build_file_map()
    registry = build_registry(file_map)

    if args.serve:
        SportMindAPIHandler.file_map = file_map
        SportMindAPIHandler.registry = registry
        server = HTTPServer(("0.0.0.0", args.port), SportMindAPIHandler)
        print(f"\nSportMind Skills API v{API_VERSION} (library {LIBRARY_VERSION})")
        print(f"{'=' * 50}")
        print(f"Serving {len(registry['skills'])} skills on http://localhost:{args.port}")
        print(f"Content files: {len(file_map)}")
        print(f"\nKey endpoints:")
        print(f"  http://localhost:{args.port}/")
        print(f"  http://localhost:{args.port}/health")
        print(f"  http://localhost:{args.port}/skills?sport=football")
        print(f"  http://localhost:{args.port}/skills/domain.football/content")
        print(f"  http://localhost:{args.port}/stack?use_case=fan_token_tier1&sport=football")
        print(f"  http://localhost:{args.port}/macro-state")
        print(f"\nCtrl+C to stop.\n")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

    elif args.content:
        result = get_skill_content(args.content, file_map)
        if "error" in result:
            print(f"ERROR: {result['error']}", file=sys.stderr)
            sys.exit(1)
        print(result["content"])

    elif args.stack:
        result = get_stack_content(args.stack, args.sport or "", file_map)
        if "error" in result:
            print(f"ERROR: {result['error']}", file=sys.stderr)
            sys.exit(1)
        # Print as concatenated content for direct agent injection
        print(f"# SportMind Stack: {result['use_case']} / {result['sport']}")
        print(f"# Skills: {result['skills_loaded']} loaded")
        print(f"# Estimated tokens: {result['estimated_tokens']}")
        print()
        for item in result["stack"]:
            print(f"\n\n{'=' * 60}")
            print(f"# SPORTMIND SKILL: {item['skill_id']}")
            print(f"{'=' * 60}\n")
            print(item["content"])

    elif args.export_github_pages:
        export_github_pages(args.export_github_pages, file_map, registry)

    elif args.stats:
        print(f"\nSportMind Skills API — Statistics")
        print(f"{'=' * 40}")
        print(f"API version:      {API_VERSION}")
        print(f"Library version:  {LIBRARY_VERSION}")
        print(f"Registry skills:  {len(registry['skills'])}")
        print(f"Content files:    {len(file_map)}")
        print()
        by_type = {}
        for s in registry["skills"].values():
            t = s.get("type", "unknown")
            by_type[t] = by_type.get(t, 0) + 1
        print("By type:")
        for t, c in sorted(by_type.items()):
            print(f"  {t}: {c}")
        print()
        print("Content available by type:")
        by_type_content = {}
        for sid in file_map:
            t = sid.split(".")[0]
            by_type_content[t] = by_type_content.get(t, 0) + 1
        for t, c in sorted(by_type_content.items()):
            print(f"  {t}: {c}")

    elif args.list_ids:
        print(f"# SportMind Skills with content ({len(file_map)} total)")
        for sid in sorted(file_map.keys()):
            print(f"  {sid:45} → {file_map[sid]}")

    else:
        parser.print_help()
        return 1

    return 0


def get_version_info():
    version = 'unknown'
    try:
        import pathlib
        for line in (pathlib.Path(__file__).parent.parent / 'llms.txt').read_text().splitlines():
            if line.startswith('Version:'): version = line.split(':',1)[1].strip(); break
    except: pass
    return {'version': version, 'library_version': LIBRARY_VERSION, 'sports': 42}

if __name__ == "__main__":
    sys.exit(main())
