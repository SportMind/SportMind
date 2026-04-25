# Agentic Workflow Pattern 13 — Web Agent Live Data

**Combines SportMind's intelligence framework with live web data
fetching for real-time grounding — lineup confirmation, on-chain
verification, and regulatory monitoring.**

---

## What this pattern does that others do not

Patterns 1–12 produce intelligence from SportMind's static library
plus any live data a developer manually provides. Pattern 13 is the
first pattern where the agent itself fetches live data sources and
feeds them back into the SportMind signal chain — without human
intervention between the fetch and the analysis.

This closes the highest-friction manual steps in the library:

- **Lineup confirmation** — instead of a developer manually checking
  `@Arsenal` at T-2h and updating availability inputs, Pattern 13
  does it autonomously using `wa_lineup_target` + Fetch MCP.

- **PATH_2 supply verification** — instead of manually navigating
  Chiliscan post-match, the agent fetches the supply delta and
  confirms or flags the burn event.

- **Regulatory monitoring** — instead of waiting for news to surface
  in a session, the agent monitors ESMA, Chiliz blog, and SEC/CFTC
  on schedule.

**The key principle:** SportMind tells the web agent exactly what to
fetch and how to interpret it. The agent does the fetching. No live
data dependency is built into the library itself.

---

## Required MCP servers

```json
{
  "mcpServers": {
    "sportmind":           { "command": "python", "args": [".../sportmind_mcp.py"] },
    "sportmind-ft":        { "command": "python", "args": [".../sportmind_ft_mcp.py"] },
    "sportmind-web-agent": { "command": "python", "args": [".../sportmind_wa_mcp.py"] },
    "fetch":               { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-fetch"] }
  }
}
```

**Minimum for lineup only:** `sportmind` + `sportmind-web-agent` + `fetch`

**Minimum for supply verify only:** `sportmind-ft` + `sportmind-web-agent` + `fetch`

---

## Use case A — Autonomous lineup confirmation (T-2h)

```python
# workflow/web_agent_lineup.py

import schedule, time
from datetime import datetime, timezone

MATCHES = [
    {
        "sport":       "football",
        "home_team":   "Arsenal",
        "away_team":   "PSG",
        "competition": "UCL Quarter-Final",
        "kickoff":     "2026-05-07T20:00:00Z",
        "token":       "AFC"
    }
]

def run_lineup_confirmation(match: dict):
    """
    Autonomous lineup confirmation cycle.
    Agent flow: pre_match → wa_lineup_target → fetch → compare → update signal.
    """

    # Step 1 — Get SportMind pre-match framework and expected squad
    pre_match_result = call_mcp("sportmind_pre_match", {
        "sport":       match["sport"],
        "home_team":   match["home_team"],
        "away_team":   match["away_team"],
        "competition": match["competition"],
        "kickoff":     match["kickoff"],
        "use_case":    "fan_token_tier1"
    })

    # Step 2 — Get fetch targets from web agent MCP
    lineup_spec = call_mcp("wa_lineup_target", {
        "sport":               match["sport"],
        "home_team":           match["home_team"],
        "kickoff":             match["kickoff"],
        "include_all_sources": False  # Tier 1 only
    })

    # Step 3 — Fetch the official lineup source
    primary_source = lineup_spec["fetch_targets"][0]
    fetched_content = call_fetch_mcp(primary_source["url_pattern"].format(
        club_handle=get_club_handle(match["home_team"])
    ))

    # Step 4 — Extract and compare
    extracted_xi = extract_starting_xi(fetched_content, match["sport"])
    expected_squad = pre_match_result["squad_brief"]["expected_xi"]

    absences = []
    unexpected = []
    for player in expected_squad:
        if player not in extracted_xi:
            absences.append(player)
    for player in extracted_xi:
        if player not in expected_squad:
            unexpected.append(player)

    # Step 5 — Build updated signal
    if absences:
        for absent in absences:
            # Check if ATM-tier player (fan token impact)
            if is_atm_tier_player(absent, match["token"]):
                log_event("ABSENCE_CONFIRMED", {
                    "player":        absent,
                    "impact":        "ATM-tier — re-run ARI with availability=0.00",
                    "ftis_impact":   "-5 FTIS dampener",
                    "token":         match["token"]
                })
            else:
                log_event("ABSENCE_CONFIRMED", {"player": absent})

        # Re-run pre_match with updated availability
        updated_signal = call_mcp("sportmind_pre_match", {
            **match,
            "squad_override": {p: {"availability": 0.0} for p in absences}
        })
        return {"status": "UPDATED", "signal": updated_signal, "absences": absences}

    else:
        log_event("LINEUP_CONFIRMED", {"xi": extracted_xi})
        return {"status": "CONFIRMED", "signal": pre_match_result, "unexpected": unexpected}


# Schedule: run at T-2h for each match
for match in MATCHES:
    kickoff = parse_iso(match["kickoff"])
    schedule_time = kickoff.subtract(hours=2)
    schedule.at(schedule_time).do(run_lineup_confirmation, match=match)
```

---

## Use case B — PATH_2 supply verification (post-match)

```python
# workflow/web_agent_supply.py

def run_supply_verification(token: str, match_result: str, match_end_time: str):
    """
    Autonomous PATH_2 supply verification cycle.
    Agent flow: ft_status → wa_supply_verify → fetch → compare → log.
    """

    # Step 1 — Confirm PATH_2 active and get contract address
    ft_status = call_mcp("ft_token_state", {"token": token})
    if ft_status["ftp"]["path"] != "PATH_2":
        return {"status": "NO_PATH_2", "note": "Supply verification not applicable"}

    contract = ft_status["contract_address"]

    # Step 2 — Get verification spec from web agent MCP
    verify_spec = call_mcp("wa_supply_verify", {
        "token":             token,
        "match_result":      match_result,
        "hours_since_match": hours_since(match_end_time)
    })

    # Step 3 — Fetch pre-match supply (should be stored from pre-match cycle)
    pre_match_supply = retrieve_stored("supply_before", token, match_end_time)

    # Step 4 — Fetch current supply from Chiliscan
    # TIMING RULE: minimum T+15min; recommended T+30min; definitive T+6h
    if hours_since(match_end_time) < 0.25:
        return {"status": "TOO_EARLY", "note": "AMM rebalancing not complete. Retry at T+30min."}

    tokeninfo_url = verify_spec["api_endpoints"]["token_info"]
    response = call_fetch_mcp(tokeninfo_url)
    post_match_supply = extract_supply(response)

    # Step 5 — Compute delta and classify
    if not pre_match_supply:
        return {"status": "PRE_MATCH_SUPPLY_MISSING", "note": "Cannot verify without baseline"}

    supply_delta = pre_match_supply - post_match_supply
    burn_pct = supply_delta / pre_match_supply

    EXPECTED_BURN = 0.0024
    TOLERANCE     = 0.0005

    if match_result.upper() == "WIN":
        if abs(burn_pct - EXPECTED_BURN) <= TOLERANCE:
            result = {
                "status":       "BURN_CONFIRMED",
                "burn_pct":     round(burn_pct * 100, 4),
                "supply_before": pre_match_supply,
                "supply_after":  post_match_supply,
                "within_tolerance": True
            }
        elif supply_delta == 0:
            result = {
                "status":    "BURN_PENDING",
                "note":      "No supply change yet — AMM may not have settled. Retry at T+6h."
            }
        else:
            result = {
                "status":    "BURN_ANOMALY",
                "burn_pct":  round(burn_pct * 100, 4),
                "expected":  EXPECTED_BURN * 100,
                "note":      "ESCALATE — supply change outside expected range"
            }

    elif match_result.upper() in ("LOSS", "DRAW"):
        if supply_delta == 0 or abs(burn_pct) < 0.0001:
            result = {
                "status": "SUPPLY_NEUTRAL_CONFIRMED",
                "note":   "Loss as expected — supply returned to pre-match level"
            }
        else:
            result = {
                "status":    "UNEXPECTED_SUPPLY_CHANGE",
                "change_pct": round(burn_pct * 100, 4),
                "note":      "ESCALATE — supply changed on a LOSS result"
            }

    # Step 6 — Log to season record
    log_season_supply(token, {
        "date":           match_end_time,
        "result":         match_result,
        "supply_before":  pre_match_supply,
        "supply_after":   post_match_supply,
        "burn_pct":       round(burn_pct * 100, 4),
        "status":         result["status"]
    })

    return result


# Schedule: run at T+30min and T+6h after each match result
```

---

## Use case C — Regulatory monitoring (scheduled)

```python
# workflow/web_agent_regulatory.py

import schedule

def run_regulatory_check(tier: str = "1", domain: str = "all"):
    """
    Scheduled regulatory monitoring using SportMind classification framework.
    Agent flow: wa_macro_monitor → fetch each target → classify → recommend.
    """

    # Step 1 — Get monitoring targets
    targets = call_mcp("wa_macro_monitor", {"tier": tier, "domain": domain})

    findings = []

    for target in targets["monitoring_targets"].get("tier_1_act_within_24h", []):
        # Step 2 — Fetch the source
        content = call_fetch_mcp(target["url"])

        # Step 3 — Extract relevant content
        extracted = {
            "source":    target["name"],
            "url":       target["url"],
            "timestamp": now_iso(),
            "content":   extract_relevant(content, target["what_to_extract"])
        }

        # Step 4 — Apply SportMind classification
        # Only act if content has changed since last check
        if is_new_content(extracted, get_last_check(target["url"])):
            finding = {
                "source":           target["name"],
                "new_content":      extracted["content"],
                "library_file":     target.get("library_file_to_update"),
                "classification":   "TIER_1_ACT",
                "recommendation":   f"Review for update to {target.get('library_file_to_update', 'library')}",
                "human_required":   True   # ALWAYS — no auto-updates
            }
            findings.append(finding)
            log_event("REGULATORY_FINDING", finding)

    # Step 5 — Escalate if findings
    if findings:
        escalate_to_human({
            "type":     "REGULATORY_MONITORING",
            "findings": findings,
            "note":     "Human review required before any library update"
        })

    return {"checked": len(targets["monitoring_targets"].get("tier_1_act_within_24h", [])),
            "findings": len(findings)}


# Schedule
schedule.every().day.at("09:00").do(run_regulatory_check, tier="1", domain="chiliz")
schedule.every().day.at("09:00").do(run_regulatory_check, tier="1", domain="sec")
schedule.every().monday.at("09:00").do(run_regulatory_check, tier="1", domain="esma")
```

---

## Failure handling and fallbacks

```
SOURCE UNAVAILABLE:
  Lineup source down → set availability_confidence = 0.85
  Raise LINEUP_UNCONFIRMED flag
  Try alternative source (Tier 2) before accepting unconfirmed
  Do NOT suppress the signal — degraded confidence is better than false confidence

CHILISCAN API RATE LIMIT:
  Wait 60 seconds and retry once
  Fall back to browser URL: chiliscan.com/token/{contract}
  If both fail: set burn_status = UNVERIFIED (not CONFIRMED)

PARSE FAILURE:
  Return raw extracted text for human classification
  Do not silently discard — log extraction failure with source URL

NEVER:
  Auto-update the library from web agent output
  Apply burn modifier before T+15 post-match
  Use a Tier 3 source when Tier 1 is unavailable — lower confidence, not lower tier
```

---

## Connection to other patterns

```
BEFORE Pattern 13: Pattern 2 (Pre-Match Intelligence Chain)
  Pattern 2 produces the pre-match signal and expected squad.
  Pattern 13 uses that output as its baseline for comparison.

AFTER Pattern 13 (match result): Pattern 11 (Post-Match Analysis Agent)
  Pattern 11 receives the Pattern 13 supply verification result
  as one of its inputs alongside the sporting outcome.

ALONGSIDE Pattern 13: Pattern 8 (Fan Token™ Play Monitor)
  Pattern 8 handles the full PATH_2 match cycle (T-48h → T+48h).
  Pattern 13 provides the on-chain verification that completes
  Pattern 8's supply confirmation step.
```

---

*SportMind v3.70 · MIT License · sportmind.dev*
*See also: platform/web-agent-connectors.md · scripts/sportmind_wa_mcp.py*
*platform/fetch-mcp-disciplinary.md · platform/realtime-integration-patterns.md*
*core/verifiable-sources-by-sport.md · core/external-intelligence-intake.md*
