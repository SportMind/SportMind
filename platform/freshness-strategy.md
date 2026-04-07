# SportMind Freshness Strategy

**The complete guide for agents and developers on keeping SportMind intelligence
current — what to check, when, how, and what to do when something is stale.**

Two distinct freshness concerns exist for any SportMind deployment:

1. **Library version freshness** — has SportMind itself been updated? New versions
   recalibrate modifiers, update market intelligence, add new skills.
2. **Application data freshness** — has the data your agent feeds into SportMind's
   framework expired? Lineups, form scores, macro state, live prices.

Both matter. An agent running the correct library version with stale lineup data
will produce a misleading signal. An agent with current match data but an outdated
market intelligence file will reason from an incorrect competitive context.

---

## Part 1 — Library version freshness

### Version check protocol

```python
# freshness/version_checker.py
"""
Check whether your loaded SportMind library is current.
Run at agent initialisation and at the start of each daily cycle.
"""
import hashlib
import json
import requests
from pathlib import Path

SPORTMIND_API = "http://localhost:8080"           # Local Skills API
SPORTMIND_REMOTE = "https://sportmind.dev/api/v3" # Hosted endpoint (when live)
LOCAL_ROOT = Path(__file__).parent.parent          # Your SportMind installation

def get_loaded_version() -> str:
    """Read the version of your currently loaded SportMind library."""
    llms_path = LOCAL_ROOT / "llms.txt"
    if not llms_path.exists():
        return "UNKNOWN"
    for line in llms_path.read_text().splitlines():
        if line.startswith("Version:"):
            return line.split(":", 1)[1].strip()
    return "UNKNOWN"

def get_latest_version(source: str = "local") -> str:
    """
    Check the latest available SportMind version.
    
    source = "local"  → read from your local installation
    source = "api"    → query the SportMind Skills API
    source = "remote" → query the hosted SportMind endpoint
    """
    if source == "local":
        return get_loaded_version()

    elif source == "api":
        try:
            r = requests.get(f"{SPORTMIND_API}/version", timeout=5)
            return r.json().get("version", "UNKNOWN")
        except Exception:
            return "UNKNOWN"

    elif source == "remote":
        try:
            r = requests.get(f"{SPORTMIND_REMOTE}/index.json", timeout=10)
            return r.json().get("version", "UNKNOWN")
        except Exception:
            return "UNKNOWN"

    return "UNKNOWN"


def check_skill_file_changes(skill_ids: list[str]) -> dict:
    """
    Check if specific skill files have changed since last loaded.
    Uses skill-hashes.json to detect content changes without downloading full files.
    
    Returns: {skill_id: "CURRENT" | "CHANGED" | "UNKNOWN"}
    """
    hashes_path = LOCAL_ROOT / "platform" / "skill-hashes.json"
    if not hashes_path.exists():
        return {s: "UNKNOWN" for s in skill_ids}
    
    registry = json.loads(hashes_path.read_text()).get("files", {})
    results  = {}
    
    for skill_id in skill_ids:
        # Find the file in the registry
        matched_path = next(
            (p for p in registry if skill_id.lower() in p.lower()), None
        )
        if not matched_path:
            results[skill_id] = "UNKNOWN"
            continue
        
        # Compute current hash
        full_path = LOCAL_ROOT / matched_path
        if not full_path.exists():
            results[skill_id] = "UNKNOWN"
            continue
        
        current_hash   = hashlib.sha256(full_path.read_bytes()).hexdigest()
        registered_hash = registry[matched_path].get("sha256", "")
        
        results[skill_id] = "CURRENT" if current_hash == registered_hash else "CHANGED"
    
    return results


class VersionUpdateStrategy:
    """
    Three update strategies for when a new library version is detected.
    Choose based on your deployment's risk tolerance.
    """
    
    @staticmethod
    def auto_reload(agent, new_version: str):
        """
        Strategy 1 — Automatic reload.
        Appropriate for: Tier 0-1 content, low-risk deployments.
        NOT appropriate for: agents mid-analysis or with pending escalations.
        """
        print(f"New version {new_version} available — auto-reloading skill stack")
        # Reload skill stacks between cycles
        # agent.reload_skill_stacks()  # Implement in your agent
        
    @staticmethod
    def flagged_reload(agent, new_version: str):
        """
        Strategy 2 — Flagged reload.
        Complete current cycle, reload at next safe pause point.
        Appropriate for: most production deployments.
        """
        print(f"New version {new_version} available — scheduling reload after current cycle")
        agent._pending_version_reload = new_version  # Set flag; reload at cycle end
        
    @staticmethod  
    def notify_operator(new_version: str, current_version: str, changes: list):
        """
        Strategy 3 — Operator notification.
        Do not auto-update; alert operator to review before deploying.
        Appropriate for: high-stakes production, regulated environments.
        """
        message = (
            f"SportMind update available: {current_version} → {new_version}\n"
            f"Changed skills: {changes}\n"
            f"Review CHANGELOG.md before updating your deployment."
        )
        print(f"VERSION UPDATE NOTIFICATION: {message}")
        # Send to your alert channel


def which_skills_affect_me(new_version_changelog: str, my_sports: list[str]) -> list:
    """
    Read the CHANGELOG to determine if a library update affects your deployment.
    
    A v3.17 update changing market/world-cup-2026.md matters to a football agent.
    The same update changing market/market-cricket.md does not.
    
    Returns list of changed skill IDs relevant to my_sports.
    """
    relevant_changes = []
    sport_patterns   = [sport.lower() for sport in my_sports]
    
    for line in new_version_changelog.splitlines():
        if any(sport in line.lower() for sport in sport_patterns):
            relevant_changes.append(line.strip())
    
    return relevant_changes
```

### Reading the CHANGELOG as a version signal

The CHANGELOG is a machine-readable version signal. Each entry documents exactly
what changed and which sports/use_cases are affected.

```python
# freshness/changelog_monitor.py

import re
import requests
from pathlib import Path

def parse_latest_changelog_entry(changelog_path: str = "CHANGELOG.md") -> dict:
    """
    Parse the most recent CHANGELOG entry to understand what changed.
    Returns structured data about the latest release.
    """
    content = Path(changelog_path).read_text()
    
    # Find the most recent version entry
    pattern = r"## \[([0-9.]+)\] — ([0-9-]+) — (.+?)(?=\n## \[|$)"
    matches = re.findall(pattern, content, re.DOTALL)
    
    if not matches:
        return {}
    
    version, date, body = matches[0]
    
    # Extract changed files from the entry
    file_pattern = r"`([a-zA-Z0-9/._-]+\.md)`"
    changed_files = re.findall(file_pattern, body)
    
    # Categorise by layer
    layers_changed = set()
    for f in changed_files:
        if f.startswith("sports/"):          layers_changed.add("L1_domain")
        elif f.startswith("athlete/"):       layers_changed.add("L2_athlete")
        elif f.startswith("fan-token/"):     layers_changed.add("L3_fantoken")
        elif f.startswith("market/"):        layers_changed.add("L4_market")
        elif f.startswith("macro/"):         layers_changed.add("L5_macro")
        elif f.startswith("core/"):          layers_changed.add("core")
        elif f.startswith("platform/"):      layers_changed.add("platform")
    
    return {
        "version":        version,
        "date":           date,
        "summary":        matches[0][2].strip().split("\n")[0],
        "changed_files":  changed_files,
        "layers_changed": sorted(layers_changed),
        "affects_agents": "core" in layers_changed or "platform" in layers_changed
    }


def subscribe_to_updates(webhook_url: str):
    """
    Register your webhook to receive SportMind update notifications.
    When a new version is published, your endpoint receives a POST with the
    CHANGELOG entry for that version.
    
    Payload: {"version": "3.17.0", "changed_files": [...], "changelog_entry": "..."}
    
    Note: SportMind's GitHub Actions CI (validate.yml) runs on every commit.
    Connect your webhook to the GitHub repository's release events for push notifications.
    """
    # In GitHub: Settings → Webhooks → Add webhook
    # Events: Releases
    # Payload URL: your webhook endpoint
    print(f"Register {webhook_url} as a GitHub release webhook on the SportMind repo")
```

---

## Part 2 — Application data freshness

### The six-tier refresh schedule

This is the operational implementation of `core/temporal-awareness.md`.

```python
# freshness/refresh_schedule.py
"""
Complete refresh schedule for all six data tiers.
Embed this in your agent's monitoring cycle.
"""
import asyncio
import subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path
import json

class SportMindRefreshScheduler:
    """
    Manages all six data freshness tiers for a SportMind deployment.
    Call check_and_refresh() at the start of each agent cycle.
    """
    
    def __init__(self, sportmind_root: Path, sportmind_api: str):
        self.root = sportmind_root
        self.api  = sportmind_api
        self.last_refresh = {
            "tier0": None,  # Never refresh
            "tier1": None,  # Quarterly
            "tier2": None,  # 1-4 weeks
            "tier3": None,  # 4-8 hours
            "tier4": None,  # Match day
            "tier5": None,  # Real-time (never cached)
        }

    async def check_and_refresh(self, upcoming_match_hours: float = 999) -> dict:
        """
        Check all tiers and refresh what is stale.
        Call at the start of every agent cycle.
        
        upcoming_match_hours: hours until next match (triggers Tier 4 refresh)
        """
        now     = datetime.now(timezone.utc)
        refreshed = []
        warnings  = []

        # TIER 0 — Permanent (domain knowledge, schemas, calibration records)
        # Never refresh mid-session. Load once at initialisation.
        # Action: None — these never expire

        # TIER 1 — Slow (market tier assessments, 90-day cycle)
        # Action: Alert operator when 90+ days since last library update
        last_version_check = self._get_last_version_check()
        if last_version_check and (now - last_version_check) > timedelta(days=90):
            warnings.append("Tier 1 data may be stale — check for SportMind library updates")
            warnings.append(f"Last version check: {last_version_check.date()}")
            warnings.append("Run: python scripts/check_skill_freshness.py")

        # TIER 2 — Moderate (form scores, 1-4 week cycle)
        # Action: Apply reliability degradation formula past 4 weeks
        tier2_age_days = self._get_tier2_age_days()
        if tier2_age_days > 28:
            reliability = max(0.85, 1.00 - (tier2_age_days / 28) * 0.15)
            warnings.append(
                f"Tier 2 data is {tier2_age_days:.0f} days old — "
                f"form modifier reliability: {reliability:.2f}"
            )

        # TIER 3 — Daily (macro state, 4-8 hour cycle)
        # Action: Run update_macro_state.py if stale
        macro_age = await self._get_macro_age_hours()
        if macro_age > 8:
            await self._refresh_macro()
            refreshed.append(f"Tier 3 (macro state) — was {macro_age:.1f}h old")
        elif macro_age > 4:
            warnings.append(f"Macro state is {macro_age:.1f}h old — consider refreshing")

        # TIER 4 — Match day (lineup, weather — T-72h, T-24h, T-2h windows)
        # Action: Trigger lineup and weather fetch at each window
        if upcoming_match_hours <= 2:
            warnings.append("T-2h CRITICAL WINDOW — confirm lineup now or set lineup_unconfirmed")
        elif upcoming_match_hours <= 24:
            warnings.append(f"T-{upcoming_match_hours:.0f}h — refresh injury list and lineup hints")
        elif upcoming_match_hours <= 72:
            warnings.append(f"T-{upcoming_match_hours:.0f}h — monitor lineup news")

        # TIER 5 — Live (DeFi TVL, token price — always fetch fresh)
        # Action: Never cache Tier 5 data; always fetch per-analysis
        # No check needed — Tier 5 is always treated as needing a fresh fetch

        return {
            "refreshed":        refreshed,
            "warnings":         warnings,
            "tier3_age_hours":  macro_age,
            "tier2_age_days":   tier2_age_days,
            "match_window":     self._classify_match_window(upcoming_match_hours),
            "checked_at":       now.isoformat()
        }

    # ── Tier-specific refresh implementations ─────────────────────────────

    async def _refresh_macro(self):
        """Tier 3: Refresh macro state."""
        script = self.root / "scripts" / "update_macro_state.py"
        if script.exists():
            result = subprocess.run(
                ["python3", str(script)],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                self.last_refresh["tier3"] = datetime.now(timezone.utc)
            else:
                # Graceful degradation — keep existing state
                print(f"Macro refresh failed: {result.stderr[:200]}")
        else:
            # Fetch directly if script not available
            import aiohttp
            async with aiohttp.ClientSession() as s:
                async with s.get(f"{self.api}/macro-state") as r:
                    state = await r.json()
                    macro_path = self.root / "platform" / "macro-state.json"
                    macro_path.write_text(json.dumps(state, indent=2))
                    self.last_refresh["tier3"] = datetime.now(timezone.utc)

    async def _get_macro_age_hours(self) -> float:
        """How old is the macro state?"""
        macro_path = self.root / "platform" / "macro-state.json"
        if not macro_path.exists(): return 999.0
        try:
            state = json.loads(macro_path.read_text())
            last  = state["macro_state"]["last_updated"]
            dt    = datetime.fromisoformat(last.replace("Z","+00:00"))
            return (datetime.now(timezone.utc) - dt).total_seconds() / 3600
        except: return 999.0

    def _get_tier2_age_days(self) -> float:
        """Age of form/standings data in days. Replace with your data timestamp."""
        # In production: track when you last loaded form data
        # This stub returns 7 days as a placeholder
        return 7.0

    def _get_last_version_check(self):
        """When did we last check for a library version update?"""
        check_file = self.root / ".last_version_check"
        if not check_file.exists(): return None
        try:
            return datetime.fromisoformat(check_file.read_text().strip())
        except: return None

    def _classify_match_window(self, hours_away: float) -> str:
        if hours_away <= 2:    return "CRITICAL_T2H"
        elif hours_away <= 24: return "MATCH_DAY_T24H"
        elif hours_away <= 72: return "PRE_MATCH_T72H"
        elif hours_away <= 168: return "UPCOMING_WEEK"
        else:                   return "NOT_IMMINENT"
```

### Freshness flags in confidence output

When data is stale, agents must communicate this to consumers through the
standard confidence output schema.

```python
def build_confidence_output_with_freshness(
    base_signal:    dict,
    refresh_status: dict,
    scheduler:      SportMindRefreshScheduler
) -> dict:
    """
    Annotate the confidence output with freshness warnings.
    Consumers (FanTokenIntel, SportFi Kit apps, humans) can act on these.
    """
    warnings  = refresh_status.get("warnings", [])
    tier3_age = refresh_status.get("tier3_age_hours", 0)

    # Freshness-adjusted SMS
    sms = base_signal.get("sportmind_score", {}).get("sms", 0)
    
    if tier3_age > 24:
        sms = max(0, sms - 8)    # Stale macro: SMS -8
        warnings.insert(0, f"Macro state is {tier3_age:.0f}h old — reliability reduced")
    elif tier3_age > 8:
        sms = max(0, sms - 3)    # Slightly stale: SMS -3

    # Freshness warning field
    freshness_warning = warnings[0] if warnings else None

    return {
        **base_signal,
        "sportmind_score": {
            **base_signal.get("sportmind_score", {}),
            "sms": sms,
            "freshness_flags": {
                "macro_age_hours":    tier3_age,
                "macro_fresh":        tier3_age <= 8,
                "match_window":       refresh_status.get("match_window"),
                "all_warnings":       warnings
            }
        },
        "freshness_warning": freshness_warning
    }
```

---

## Part 3 — Push notification for library updates

For production deployments that should update automatically when SportMind
publishes a new version:

```python
# freshness/update_listener.py
"""
Listens for SportMind library update notifications.
Connect to GitHub webhook or poll the version endpoint.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import subprocess
import hashlib
import hmac
import os

GITHUB_WEBHOOK_SECRET = os.environ.get("GITHUB_WEBHOOK_SECRET", "")
SPORTMIND_ROOT        = os.environ.get("SPORTMIND_ROOT", ".")


class GitHubWebhookHandler(BaseHTTPRequestHandler):
    """
    Receives GitHub release webhooks from the SportMind repository.
    Triggers agent skill stack reload on new release.
    """
    
    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        payload        = self.rfile.read(content_length)
        
        # Verify GitHub signature (security)
        if GITHUB_WEBHOOK_SECRET:
            sig = self.headers.get("X-Hub-Signature-256", "")
            expected = "sha256=" + hmac.new(
                GITHUB_WEBHOOK_SECRET.encode(),
                payload, hashlib.sha256
            ).hexdigest()
            if not hmac.compare_digest(sig, expected):
                self.send_response(401)
                self.end_headers()
                return
        
        data       = json.loads(payload)
        event_type = self.headers.get("X-GitHub-Event", "")
        
        if event_type == "release" and data.get("action") == "published":
            new_version = data["release"]["tag_name"]
            changelog   = data["release"]["body"]
            
            print(f"New SportMind release: {new_version}")
            print(f"Changes: {changelog[:200]}...")
            
            # Determine update strategy based on deployment configuration
            # Strategy 1: Pull and reload automatically
            # subprocess.run(["git", "pull", "origin", "main"], cwd=SPORTMIND_ROOT)
            
            # Strategy 2: Notify operator (recommended for production)
            self._notify_operator(new_version, changelog)
            
            # Strategy 3: Apply if only Tier 0-1 content changed (safe auto-update)
            # if only_safe_content_changed(changelog):
            #     subprocess.run(["git", "pull", "origin", "main"], cwd=SPORTMIND_ROOT)
        
        self.send_response(200)
        self.end_headers()
    
    def _notify_operator(self, version: str, changelog: str):
        """Send notification via your preferred channel."""
        print(f"NOTIFY: SportMind {version} available. Review and update when ready.")
    
    def log_message(self, format, *args): pass  # Suppress default logging


def start_webhook_listener(port: int = 9000):
    """Start the webhook listener server."""
    server = HTTPServer(("", port), GitHubWebhookHandler)
    print(f"SportMind update listener on port {port}")
    server.serve_forever()
```

---

## Part 4 — Freshness in the agent base class

Integrate freshness checking into the `SportMindAgent` base class from
`core/autonomous-agent-framework.md`:

```python
# Add to SportMindAgent._run_cycle():

async def _run_cycle_with_freshness(self):
    """Extended cycle with freshness checking built in."""
    from freshness.refresh_schedule import SportMindRefreshScheduler
    
    scheduler = SportMindRefreshScheduler(
        sportmind_root = Path("."),
        sportmind_api  = self.api_url
    )
    
    # Check all tiers before analysis
    upcoming_hours = await self._get_next_event_hours()
    refresh_status = await scheduler.check_and_refresh(upcoming_hours)
    
    # Log any warnings — Safety Principle 6 (never silent failure)
    for warning in refresh_status.get("warnings", []):
        self.logger.warning(f"FRESHNESS: {warning}")
    
    # Proceed with normal cycle
    await self._run_cycle()
    
    # Check for library version updates (daily)
    if self.cycle_count % (24 * 60 // self.config.cycle_interval_sec * 60) == 0:
        await self._check_library_version()

async def _check_library_version(self):
    """Daily version check. Alert if update available."""
    from freshness.version_checker import get_loaded_version, get_latest_version
    current = get_loaded_version()
    latest  = get_latest_version(source="api")
    if latest != "UNKNOWN" and latest != current:
        self.logger.warning(f"Library update available: {current} → {latest}")
        # Apply your chosen VersionUpdateStrategy here
```

---

## Quick reference — freshness at a glance

| Tier | What | Refresh? | How | Stale action |
|---|---|---|---|---|
| 0 | Domain knowledge, schemas | Never | Load once | N/A |
| 1 | Market tiers, regulatory | 90 days | Library version update | Alert operator |
| 2 | Form scores, standings | 1-4 weeks | Season data refresh | Apply ×0.85 reliability |
| 3 | Macro state | 4-8 hours | `update_macro_state.py` | SMS -3 to -8 |
| 4 | Lineup, weather | T-72h/24h/2h | Live API fetch | Set `lineup_unconfirmed` |
| 5 | Token price, TVL | Per-analysis | Real-time API | Never cache |

---

## Compatibility

**Temporal awareness model:** `core/temporal-awareness.md` — the six tiers defined
**Real-time patterns:** `platform/realtime-integration-patterns.md` — live data integration
**Agent framework:** `core/autonomous-agent-framework.md` — Safety Principle 6 (graceful degradation)
**MCP server:** `platform/sportmind-mcp-server.md` — `sportmind_verify` for integrity checking
**CHANGELOG:** `CHANGELOG.md` — version history; each entry describes what changed
**CI workflows:** `.github/workflows/validate.yml` — triggers on every library commit

*MIT License · SportMind · sportmind.dev*
