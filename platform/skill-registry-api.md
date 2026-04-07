# Skill Registry API — Versioned Endpoint

**How to access the SportMind skill registry as a live, queryable JSON endpoint.**

The skill registry is available both as a static local script and as a hosted
versioned JSON endpoint via GitHub Pages.

---

## Endpoint overview

```
BASE URL: https://SportMind.github.io/sportmind/api/v1/

ENDPOINTS:
  GET /registry.json          Full registry — all skills, all metadata
  GET /skills/{skill_id}.json Individual skill metadata
  GET /registry-stable.json   Stable skills only (no stubs)
  GET /mvs.json               All minimum viable skill sets
```

---

## Versioning

```
API version is pinned to SportMind library version.

Current version: v3.1
Endpoint: https://SportMind.github.io/sportmind/api/v3.1/registry.json

Version field in every response:
{
  "api_version": "3.1",
  "library_version": "3.1.0",
  "generated_at": "ISO-8601",
  "skills": { ... }
}

VERSION STABILITY:
  Major versions (v3.x → v4.x): may change schema — use explicit version URL
  Minor versions (v3.1 → v3.2): additive only — same schema, more skills
  Latest alias: /api/latest/registry.json (always current; may change schema)
```

---

## Generating the registry JSON for GitHub Pages

Use the `--export` flag with `scripts/skill_registry_api.py`:

```bash
# Generate full registry JSON
python scripts/skill_registry_api.py --export > docs/api/v3.1/registry.json

# Generate stable-only registry
python scripts/skill_registry_api.py --query status=stable --export-format json \
  > docs/api/v3.1/registry-stable.json

# Generate MVS catalogue
python scripts/skill_registry_api.py --export-mvs > docs/api/v3.1/mvs.json
```

**GitHub Pages setup:**

```yaml
# .github/workflows/publish-api.yml (already included in SportMind)
# Triggers on any change to sports/, athlete/, fan-token/, core/, market/, macro/,
# platform/skill-registry.md, or scripts/sportmind_api.py

# Generates complete static API:
#   docs/api/v3.2/registry.json          Full registry
#   docs/api/v3.2/registry-stable.json   Stable skills only
#   docs/api/v3.2/skills/{id}.json       Individual skill metadata
#   docs/api/v3.2/content/{id}.json      Skill content (full markdown)
#   docs/api/v3.2/mvs.json               Minimum viable sets
#   docs/api/v3.2/macro-state.json       Current macro state
#   docs/api/latest/                     Latest version alias
```

---

## Response format

### `GET /registry.json`

```json
{
  "api_version": "3.1",
  "library_version": "3.1.0",
  "schema_version": "1.0",
  "generated_at": "2026-04-02T00:00:00Z",
  "source": "platform/skill-registry.md",
  "total_skills": 88,
  "stable_skills": 74,
  "stub_skills": 14,
  "skills": {
    "domain.football": {
      "skill_id": "domain.football",
      "type": "domain",
      "sport": "Football / Soccer",
      "layer": 1,
      "status": "stable",
      "key_differentiator": "Derby scoring, competition tier, season rhythm",
      "contract": "signal.domain",
      "file": "sports/football/"
    },
    "athlete.football": { ... },
    "fantoken.football-bridge": { ... }
  }
}
```

### `GET /skills/{skill_id}.json`

```json
{
  "skill_id": "domain.football",
  "type": "domain",
  "sport": "Football / Soccer",
  "layer": 1,
  "status": "stable",
  "key_differentiator": "Derby scoring model; competition tier system; NCSI for World Cup",
  "contract": "signal.domain",
  "file": "sports/football/sport-domain-football.md",
  "related_skills": [
    "athlete.football",
    "fantoken.football-bridge",
    "market.football"
  ]
}
```

### `GET /mvs.json`

```json
{
  "use_cases": {
    "domain_query": {
      "description": "Quick sport domain question",
      "skills": ["domain.{sport}", "core.confidence-schema"],
      "estimated_tokens": "4000–8000"
    },
    "fan_token_tier1": {
      "description": "Full fan token analysis",
      "skills": ["fantoken.why", "macro.overview", "market.{sport}", ...],
      "estimated_tokens": "25000–45000"
    }
  }
}
```

---

## Client examples

### Python

```python
import requests

BASE = "https://SportMind.github.io/sportmind/api/v3.2"

# Get single skill content and inject into agent
skill = requests.get(f"{BASE}/content/domain_football.json").json()
agent_context = skill["content"]  # inject directly into system prompt

# Get full stack for fan token analysis (one call — ready to inject)
# Use local server during development:
stack = requests.get(
    "http://localhost:8080/stack?use_case=fan_token_tier1&sport=football"
).json()
for item in stack["stack"]:
    print(f"Loading: {item['skill_id']}")
    inject_into_agent(item["content"])

# Check current macro state before analysis
macro = requests.get(f"{BASE}/macro-state.json").json()
modifier = macro["macro_state"]["crypto_cycle"]["macro_modifier"]
```

### JavaScript / Node

```javascript
const registry = await fetch(
    'https://SportMind.github.io/sportmind/api/v3.1/registry.json'
).then(r => r.json());

// Get stable domain skills only
const domainSkills = Object.values(registry.skills)
    .filter(s => s.type === 'domain' && s.status === 'stable');
```

### Local development

```bash
# Run the full Skills API (content + metadata)
python scripts/sportmind_api.py --serve --port 8080

# Fetch single skill content
python scripts/sportmind_api.py --content domain.football

# Fetch full stack for agent injection
python scripts/sportmind_api.py --stack fan_token_tier1 --sport football

# Export static files for GitHub Pages
python scripts/sportmind_api.py --export-github-pages ./docs/api

# Registry metadata only (legacy)
python scripts/skill_registry_api.py --serve --port 8081
```

---

## Rate limiting and caching

```
GitHub Pages endpoints:
  Rate limit: None (GitHub Pages CDN — effectively unlimited)
  Cache TTL: GitHub Pages caches for ~10 minutes
  Update frequency: Regenerated on every push to main (when skill-registry.md changes)
  
Local server (development):
  No rate limiting
  Run with: python scripts/skill_registry_api.py --serve --port 8080

Recommended client caching:
  Cache registry.json for 1 hour (changes rarely)
  Cache individual skill files for 24 hours
  Do not cache macro-state.json (changes every 4 hours)
```

---

## Integration with platform contracts

The skill registry API is the discovery layer for platform contracts.

```python
# Workflow: discover → query → call contract
import requests

# 1. Discover: what skills exist for football?
registry = requests.get(".../api/v3.1/registry.json").json()
football_skills = [k for k, v in registry["skills"].items()
                   if "football" in str(v.get("sport", "")).lower()]

# 2. Get contract for a skill
skill = registry["skills"]["domain.football"]
contract = skill["contract"]  # "signal.domain"

# 3. Call the contract
response = sportmind.call({
    "skill": contract,
    "sport": "football",
    "inputs": {"base_score": 72}
})
```

See `platform/api-contracts.md` for full contract specifications.

---

*MIT License · SportMind · sportmind.dev*
