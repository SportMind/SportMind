---
name: sportmind-mcp-suite
description: >
  Documentation for the SportMind MCP server suite — seven servers covering
  the full intelligence stack. The general-purpose server (sportmind_mcp.py)
  handles broad sports intelligence. Six domain-specific servers provide
  targeted interfaces for fan tokens, pre-match signals, broadcast/commercial
  intelligence, governance/competition, scouting/transfer, and agent lifecycle
  management. Each server runs independently on its own port and can be
  connected from any MCP-compatible client (Claude Desktop, Claude Code,
  custom agents). All servers follow the same pattern: stdio transport for
  local agents, HTTP/SSE transport for remote agents.
---

# SportMind MCP Server Suite

**Seven servers. One intelligence stack. Pick what you need.**

| Server | Script | Port | Tools | Primary audience |
|---|---|---|---|---|
| General | `sportmind_mcp.py` | 3001 | 10 | All developers |
| Fan Token | `sportmind_ft_mcp.py` | 3002 | 8 | Chiliz devs, clubs, portfolio agents |
| Pre-Match Signal | `sportmind_pm_mcp.py` | 3003 | 3 | Any developer — zero-friction entry |
| Broadcast & Commercial | `sportmind_bc_mcp.py` | 3004 | 5 | Broadcasters, rights holders |
| Governance & Competition | `sportmind_gc_mcp.py` | 3005 | 6 | Fan token governors, competition analysts |
| Scouting & Transfer | `sportmind_sc_mcp.py` | 3006 | 5 | Clubs, agents, analytics teams |
| Agent Lifecycle | `sportmind_al_mcp.py` | 3007 | 5 | Multi-agent orchestrators |

---

## Installation

```bash
pip install mcp aiohttp
```

All servers require Python 3.9+ and the `mcp` library. `aiohttp` is only needed for HTTP/SSE mode.

---

## Server 1 — General Purpose (`sportmind_mcp.py` — port 3001)

The original SportMind MCP server. Ten tools covering the full signal chain.
Use this when you want everything and do not need domain-specific interfaces.

```bash
python scripts/sportmind_mcp.py              # stdio (Claude Desktop)
python scripts/sportmind_mcp.py --http       # HTTP/SSE
```

**Tools:** `sportmind_signal` · `sportmind_macro` · `sportmind_stack` ·
`sportmind_verify` · `sportmind_agent_status` · `sportmind_pre_match` ·
`sportmind_disciplinary` · `sportmind_fan_token_lookup` ·
`sportmind_sentiment_snapshot` · `sportmind_verifiable_source`

---

## Server 2 — Fan Token (`sportmind_ft_mcp.py` — port 3002)

Dedicated Chiliz Chain / Socios ecosystem intelligence. All tools are
fan-token-specific. Start here if you are building for a club, a portfolio
monitor, or a Socios developer.

```bash
python scripts/sportmind_ft_mcp.py              # stdio
python scripts/sportmind_ft_mcp.py --http        # HTTP/SSE port 3002
```

**Tools:**

`ft_token_state` — FTP path status, lifecycle phase, supply mechanics.
Parameters: `token` (ticker or club name), `include_supply`.

`ft_burn_forecast` — Upcoming WIN burn events and maximum supply reduction
schedule for a competition. Critical for PATH_2 clubs.
Parameters: `token`, `competition`, `matches_remaining`.

`ft_community_health` — CHI framework, four holder archetypes, churn risk
signals. Returns the engagement framework, not live data.
Parameters: `token`.

`ft_fraud_scan` — MRS (Manipulation Risk Score) computation. Flags wash
trading and coordinated wallet creation. Pass TVI ratio and new wallet count.
Parameters: `token`, `tvi_ratio`, `new_wallets_48h`.

`ft_holder_brief` — Archetype-specific engagement recommendation for a
specific event type (win/loss/governance). Includes timing windows and
do-not-include lists.
Parameters: `token`, `archetype`, `event_type`.

`ft_tournament_exit` — CALENDAR_COLLAPSE impact if a team is eliminated.
Quantifies PATH_2 burns lost and LTUI trajectory reset.
Parameters: `token`, `competition`, `exit_round`.

`ft_macro_context` — Current Chiliz Chain macro: MiCA/ESMA status, CHZ
virtuous cycle, buyback programme, US market re-entry, regulatory context.
No parameters required.

`ft_registry` — Fan token registry with optional sport/tier filter.
Parameters: `sport` (optional), `tier` (optional).

**Claude Desktop config:**
```json
{
  "mcpServers": {
    "sportmind-fan-token": {
      "command": "python",
      "args": ["/path/to/sportmind/scripts/sportmind_ft_mcp.py"]
    }
  }
}
```

---

## Server 3 — Pre-Match Signal (`sportmind_pm_mcp.py` — port 3003)

Zero-friction. Three tools. One call returns a complete pre-match package.
The lowest barrier-to-entry entry point to SportMind. Start here if you
are new to the library or building a simple signal agent.

```bash
python scripts/sportmind_pm_mcp.py              # stdio
python scripts/sportmind_pm_mcp.py --http        # HTTP/SSE port 3003
```

**Tools:**

`pm_signal` — Full pre-match signal: direction, SMS, composite modifier,
recommended action (ENTER/WAIT/ABSTAIN), and macro gate check. Load this
with any sport, home team, away team, and competition.
Parameters: `sport`, `home_team`, `away_team`, `competition`, `kickoff`, `notes`.

`pm_squad_brief` — Squad availability summary: lineup confirmation window,
manager language decoder signals, and ARI input checklist.
Parameters: `sport`, `team`, `match_date`, `competition`.

`pm_readiness` — Simplified ARI (Athlete Readiness Index) gate for a
named player. Returns readiness score, label, and FTIS impact.
Parameters: `player`, `sport`, `days_rest`, `season_matches`,
`recent_injury`, `confirmed_starter`.

---

## Server 4 — Broadcast & Commercial (`sportmind_bc_mcp.py` — port 3004)

Commercial intelligence for broadcasters, rights holders, sponsors, and
content teams. Answers the commercial question (what is this match worth
commercially?) not the performance question.

```bash
python scripts/sportmind_bc_mcp.py --http --port 3004
```

**Tools:**

`bc_broadcast_value` — BVS (Broadcast Value Signal) for a match or event.
Four components: audience reach, engagement depth, rights scarcity,
commercial premium.
Parameters: `sport`, `competition`, `event_label`, `home_club`, `away_club`.

`bc_rights_tier` — Rights tier, annual valuation, key broadcaster breakdown.
Coverage: Premier League, NFL, UCL, IPL, NBA and more.
Parameters: `competition`, `territory`.

`bc_audience_reach` — Audience reach tier, territory window analysis, India
Rule flag. Includes EU/Americas overlap premium detection.
Parameters: `sport`, `competition`, `kickoff_time_utc`, `primary_market`.

`bc_context_quality` — Full CQS (Context Quality Score) across all six
dimensions: slot, venue capacity/occupancy, audience reach, schedule
density, season position, territory window.
Parameters: `sport`, `competition`, `kickoff_local_time`, `venue_capacity`,
`occupancy_pct`, `season_position`, `is_neutral_venue`.

`bc_dts_effect` — Drive to Survive / content catalyst effect. Documents
how documentary/streaming content amplifies commercial signals per sport.
Parameters: `sport`, `content_type`, `franchise`.

---

## Server 5 — Governance & Competition (`sportmind_gc_mcp.py` — port 3005)

Competition calendar, standings intelligence, and fan token governance.
The season-arc server — where are teams, what is the governance state,
what does the table trajectory mean for commercial signals?

```bash
python scripts/sportmind_gc_mcp.py --http --port 3005
```

**Tools:**

`gc_governance_state` — GSI score, participation rate, Governor archetype
risk, vote quality assessment.
Parameters: `token`, `participation_rate`, `last_votes`, `votes_participated`.

`gc_vote_alert` — Governance vote timing and notification sequence generator.
T-72h/T-24h/T-4h/T+2h sequence with quality filter check.
Parameters: `token`, `vote_topic`, `vote_close_utc`, `current_participation_pct`.

`gc_standings` — League table position, threshold proximity (title/top4/
relegation), and CQS season_position score from table context.
Parameters: `club`, `league`, `current_position`, `points`, and more.

`gc_competition_state` — Competition phase, knockout context, two-legged tie
aggregate rules (away goals removed from UEFA 2021), CALENDAR_COLLAPSE risk.
Parameters: `competition`, `sport`, `current_round`, `home_club`, `away_club`,
`home_aggregate`, `away_aggregate`, `is_second_leg`.

`gc_fixtures` — Upcoming fixture context, schedule density rules, and free
data connector guidance per sport.
Parameters: `club`, `sport`, `competitions`.

`gc_calendar` — Season arc position and commercial calendar. Football and
NBA detailed; returns load instruction for other sports.
Parameters: `sport`, `competition`, `current_month`.

---

## Server 6 — Scouting & Transfer (`sportmind_sc_mcp.py` — port 3006)

Player scouting, transfer valuation, and recruitment intelligence.
Exposes Pattern 10 (CVS scouting formula) as callable tools.

```bash
python scripts/sportmind_sc_mcp.py --http --port 3006
```

**Tools:**

`sc_cvs_brief` — Composite Value Score (CVS) — the Pattern 10 scouting
formula. Combines DQI, commercial value (age-curve), system fit, and risk
(contract years) into one acquisition score with bid range recommendation.
Parameters: `player`, `position`, `age`, `sport`, `dqi_score`,
`system_fit_score`, `market_value_m`, `contract_years_remaining`.

`sc_dqi` — Decision Quality Index from performance metrics: xA/90,
pressured pass completion, shot quality, defensive anticipation.
Detects DECISION_QUALITY_UNDERVALUED (the Moneyball signal).
Parameters: `player`, `sport`, `position`, `xa_per_90`,
`pressured_pass_completion`, `shot_quality_score`, `defensive_anticipation`.

`sc_system_fit` — System fit score based on buying club PPDA and player
metrics. Returns CVS multiplier (×0.88–1.08) from fit assessment.
Parameters: `player`, `position`, `buying_club_ppda`, `buying_club_system`,
`player_progressive_passes_per_90`, `player_pressured_completion`.

`sc_valuation` — Market value vs DQI-adjusted fair value. Age-curve
adjustment included. Detects undervaluation and overvaluation.
Parameters: `player`, `sport`, `age`, `position`, `market_value_m`,
`dqi_score`, `contract_years`.

`sc_transfer_brief` — Transfer timeline, window timing (summer/winter),
RAF formula context, negotiation phase guide, and fan token departure
impact note.
Parameters: `player`, `buying_club`, `selling_club`, `transfer_window`,
`urgency`, `market_value_m`, `contract_years`.

---

## Server 7 — Agent Lifecycle (`sportmind_al_mcp.py` — port 3007)

For orchestrator agents managing SportMind agent fleets. Enables an
orchestrator to register, monitor, receive escalations from, and manage
SportMind agents via MCP calls. Implements the A2A coordination pattern.

```bash
python scripts/sportmind_al_mcp.py --http --port 3007
```

**Tools:**

`al_agent_start` — Register and initialise a new SportMind agent. Assigns
type, terminal goal, sport, token, and autonomy level (0–4). Returns skill
loading instructions.
Parameters: `agent_id`, `agent_type`, `terminal_goal`, `sport`, `token`,
`autonomy_level`.

`al_agent_status` — Get operational state: cycles, signals produced,
pending escalations, last active time, memory summary (optional).
Parameters: `agent_id`, `include_memory_summary`.

`al_escalation_inbox` — Retrieve pending escalations requiring human review.
Optionally resolve individual escalations by ID.
Parameters: `agent_id`, `resolve_id`.

`al_memory_write` — Write signal, result, or context to agent session
memory. Supports optional TTL.
Parameters: `agent_id`, `key`, `value`, `ttl_hours`.

`al_memory_read` — Read from agent memory by key, or list all stored keys.
Parameters: `agent_id`, `key`, `list_keys`.

**Note on memory persistence:** Session memory only. For cross-session
persistence, implement `platform/memory-integration.md` with your preferred
storage backend.

---

## Running multiple servers simultaneously

```bash
# Start all seven servers in background
python scripts/sportmind_mcp.py     --http --port 3001 &
python scripts/sportmind_ft_mcp.py  --http --port 3002 &
python scripts/sportmind_pm_mcp.py  --http --port 3003 &
python scripts/sportmind_bc_mcp.py  --http --port 3004 &
python scripts/sportmind_gc_mcp.py  --http --port 3005 &
python scripts/sportmind_sc_mcp.py  --http --port 3006 &
python scripts/sportmind_al_mcp.py  --http --port 3007 &

# Health checks
curl http://localhost:3001/health
curl http://localhost:3002/health
```

---

## Typical deployment patterns

**Fan token portfolio agent (Chiliz developer):**
Connect: Fan Token MCP (port 3002) + Governance & Competition MCP (port 3005)

**Pre-match signal agent (new developer):**
Connect: Pre-Match Signal MCP (port 3003) only — zero configuration

**Broadcaster / rights team:**
Connect: Broadcast & Commercial MCP (port 3004) + General MCP (port 3001)

**Club analytics team (full stack):**
Connect: All seven servers — orchestrate via Agent Lifecycle MCP (port 3007)

**Transfer window agent:**
Connect: Scouting & Transfer MCP (port 3006) + General MCP (port 3001)

---

*SportMind v3.67 · MIT License · sportmind.dev*
*See also: MCP-SERVER.md · platform/sportmind-mcp-server.md*
*core/agent-cognitive-architecture.md · core/multi-agent-coordination.md*
