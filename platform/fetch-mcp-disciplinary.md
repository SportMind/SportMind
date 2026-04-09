# Fetch MCP — Disciplinary Monitoring Integration

**How to use Fetch MCP to verify disciplinary status against the authoritative
sources that `sportmind_verifiable_source` maps out.**

`sportmind_verifiable_source` tells an agent where to look for disciplinary
information. Fetch MCP lets the agent actually go and look. Together they
close the loop between SportMind's static intelligence framework and live
regulatory data — without introducing a paid API dependency or ongoing
maintenance burden.

---

## The integration model

```
sportmind_disciplinary
  → Returns DSM framework + regulatory source URL + flags to check
  → Does NOT fetch live data (zero maintenance philosophy)

sportmind_verifiable_source
  → Returns the exact authoritative URL for the sport's disciplinary body
  → Tier 1 sources only

Fetch MCP
  → Fetches the content at that URL
  → Agent applies SportMind DSM framework to what it finds

RESULT: live disciplinary status + SportMind reasoning framework
        without any API keys, subscriptions, or maintenance
```

---

## Configuration

```python
# claude_desktop_config.json

{
  "mcpServers": {
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    },
    "sportmind": {
      "command": "python",
      "args": ["/path/to/SportMind/scripts/sportmind_mcp.py"]
    }
  }
}
```

---

## Authoritative sources by sport — fetch targets

These are the Tier 1 sources from `core/verifiable-sources-by-sport.md`.
All are publicly accessible, no authentication required.

### Rugby Union — World Rugby judicial decisions
```
URL: https://www.world.rugby/the-game/judicial-decisions
Content: All citing commissioner decisions published as PDFs
Update frequency: Within 48h of hearing
What to look for: Player name, ban length, offence description, entry point
Fetch approach: Page lists recent decisions — search for player name
```

### Football — FA disciplinary
```
URL: https://www.thefa.com/football-rules-governance/disciplinary
Content: Charge notifications, personal hearings, appeal outcomes
Update frequency: Business days
What to look for: Player name, charge type (E1(b) = off-field), hearing date
Fetch approach: News section lists recent charges
```

### Football — UEFA disciplinary
```
URL: https://www.uefa.com/insideuefa/disciplinary
Content: UEFA CEDB decisions, appeal body outcomes
Update frequency: Within 24-48h of decision
What to look for: Match, player, sanction type, matches banned
```

### Formula 1 — FIA steward decisions
```
URL: https://www.fia.com/documents/decisions
Content: All steward decisions published as PDFs
Update frequency: During and immediately after race weekends
What to look for: Driver name, penalty type, super licence points awarded
Super licence points tracker: https://www.racefans.net/f1-penalties/super-licence-penalty-points
```

### MMA/UFC — USADA sanctions
```
URL: https://www.usada.org/testing/results/sanctions/
Content: All athlete sanctions published
Update frequency: On announcement
What to look for: Athlete name, substance, sanction length
UFC suspensions: https://www.ufc.com/news (search "suspended")
```

### Cricket — ICC Code of Conduct
```
URL: https://www.icc-cricket.com/about/cricket/rules-and-regulations/code-of-conduct
Content: Match referee decisions and ICC tribunal outcomes
What to look for: Player name, level of offence, demerit points
ESPNcricinfo faster: https://www.espncricinfo.com (search "[player] code of conduct")
```

### Rugby League — NRL match review
```
URL: https://www.nrl.com/the-game/integrity-and-welfare/match-review-committee/
Content: Weekly match review committee decisions
Update frequency: Within 48h of matches
What to look for: Player name, charge grade, ban weeks
```

### NHL — Department of Player Safety
```
URL: https://www.nhl.com/news/department-player-safety
Content: All suspensions and supplemental discipline
Update frequency: Within 24h of incident
What to look for: Player name, incident type, games suspended
```

---

## Sequential workflow — fetch + SportMind

```
STEP 1: Call sportmind_disciplinary
  Input: { player: "Player Name", sport: "rugby", include_framework: true }
  Output: DSM framework + regulatory source URL

STEP 2: Call sportmind_verifiable_source
  Input: { query_type: "disciplinary_ban", sport: "rugby" }
  Output: { source: "world.rugby/the-game/judicial-decisions", tier: 1 }

STEP 3: Fetch the regulatory source
  Tool: fetch
  URL: https://www.world.rugby/the-game/judicial-decisions
  Look for: Player name in recent decisions list

STEP 4: Apply SportMind DSM framework to fetched content
  IF player found, ban confirmed:
    → Classify offence tier from decision description
    → Apply appropriate DSM level (MODERATE/SEVERE/CATASTROPHIC)
    → Set flags (BAN_CONFIRMED, CONDUCT_RESIDUAL)
    → Calculate return date
  IF player NOT found in recent decisions:
    → No active citing confirmed
    → DSM remains at default (MINIMAL)
    → Note: absence of citing ≠ confirmed clean (may be pending)

STEP 5: Store result in memory (if Memory MCP active)
  Update player_disciplinary record with current status
  Set expected_resolution date if hearing scheduled
```

---

## Example: Rugby citing check workflow

```
Scenario: Key PSG player cited for dangerous play before UCL quarter-final.
Token: PSG (football fan token — but rugby example for citing process demonstration)

Agent workflow with Fetch + SportMind:

1. sportmind_disciplinary called:
   Returns: DSM_MODERATE framework, World Rugby source URL

2. sportmind_verifiable_source called:
   Returns: world.rugby/the-game/judicial-decisions — Tier 1

3. fetch called on World Rugby judicial decisions page:
   Agent searches for player name in PDF list
   
   IF found:
     Document shows: "8-week ban, dangerous play, first offence, mitigated by early plea"
     Agent: applies DSM_MODERATE (8 weeks < 12 weeks — moderate range)
     Agent: flags BAN_CONFIRMED, calculates return date
     Agent: "Commercial modifier 0.88 for 8-week duration + 2 weeks CONDUCT_RESIDUAL"
     
   IF not found:
     Agent: "No World Rugby decision found. Check if:
             (a) citing has not yet been heard — CITING_PENDING
             (b) citing was not upheld — not cited, clean
             (c) domestic competition (check Premiership Rugby disciplinary)"

4. Memory update:
   player_disciplinary record updated with BAN_CONFIRMED
   expected_resolution = [kickoff date + 8 weeks]
   
5. Signal synthesis:
   PSG token: WAIT (BAN_CONFIRMED, key player unavailable 8 weeks)
   Return to ENTER assessment: [return date + 2 weeks]
```

---

## Handling fetch errors and access issues

```
COMMON ISSUES AND HANDLING:

Site temporarily unavailable:
  → Do not fail the analysis
  → Apply DSM_MODERATE as precautionary default
  → Flag: SOURCE_TEMPORARILY_UNAVAILABLE
  → Note: "Could not verify disciplinary status — applying conservative DSM_MODERATE"

Content not parseable (JavaScript-heavy page):
  → Try alternative source (backup from sportmind_verifiable_source)
  → For World Rugby: try searching Google for "[player name] World Rugby ban"
    (official PDFs are indexed and may appear in search results)
  → If still unable: flag MANUAL_VERIFICATION_REQUIRED

Player name not found in recent decisions:
  → Does NOT mean player is clean
  → Means: no confirmed ban in recent published decisions
  → Flag: NOT_FOUND_IN_DECISIONS — check pre-charge or club statement
  → Recommend: check club official statement for any squad suspension

Rate limiting:
  → Space fetch calls: one authoritative source per disciplinary check
  → Do not loop over multiple pages — check only the current/recent list
  → If rate limited: use cached result from Memory MCP if available
```

---

## What Fetch MCP is NOT for in SportMind

```
DO NOT USE FETCH FOR:
  Live match scores — use official league API or sportmind_verifiable_source
  Live player stats — use FBref, Basketball Reference directly
  Social media sentiment — this is a data layer concern, not intelligence layer
  Odds or betting prices — outside SportMind's intelligence scope
  General news scraping — too broad; use Tier 1 disciplinary sources only
  Fan token prices — use chiliscan.com or Kayen API directly

FETCH IS SPECIFICALLY FOR:
  Authoritative disciplinary body decisions (the sources in this document)
  Official match result verification (when a definitive source is needed)
  Verifying a specific fact that sportmind_verifiable_source has pointed to

RULE: Fetch follows sportmind_verifiable_source. It does not explore freely.
```

---

## Combined three-server setup

```python
# Complete SportMind + Sequential Thinking + Memory + Fetch configuration
# claude_desktop_config.json

{
  "mcpServers": {
    "sportmind": {
      "command": "python",
      "args": ["/path/to/SportMind/scripts/sportmind_mcp.py"],
      "description": "SportMind sports intelligence — ten tools"
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
      "description": "Structured step-by-step reasoning"
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "description": "Persistent cross-session memory"
    },
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"],
      "description": "Fetch authoritative disciplinary sources"
    }
  }
}
```

### What each server contributes

```
sportmind          — intelligence framework, signal generation, fan token registry
sequential-thinking — explicit step-by-step reasoning chain (no errors, auditable)
memory             — cross-session persistence (patterns, history, upcoming events)
fetch              — live disciplinary verification from Tier 1 sources

Together: a SportMind agent that reasons correctly, remembers what it learned,
verifies its disciplinary signals against live authoritative sources, and
improves with every session.
```

---

*SportMind v3.35 · MIT License · sportmind.dev*
*See also: platform/sequential-thinking-integration.md · platform/memory-integration.md*
*core/verifiable-sources-by-sport.md · core/athlete-disciplinary-intelligence.md*
