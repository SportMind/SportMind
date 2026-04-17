---
name: web-agent-connectors
description: >
  Framework for web agent integration with SportMind's three highest-value
  live data use cases. Documents exactly what to fetch, what to extract,
  how to translate the extraction into SportMind input format, source tier
  classification, and failure modes. Three connectors: (1) Lineup
  confirmation — official club social accounts at T-2h, ARI availability
  component input; (2) PATH_2 supply verification — Chiliscan post-match
  burn confirmation and season supply tracking; (3) Regulatory and macro
  monitoring — ESMA, SEC/CFTC, Chiliz communications for library-level
  updates. Designed for web-capable agents (Fetch MCP, Claude in Chrome,
  browser-use, Playwright). Zero-dependency principle maintained: SportMind
  defines what to extract and how to interpret it; the agent that does the
  browsing is the application layer. Extends platform/fetch-mcp-disciplinary.md
  (the existing Fetch MCP integration pattern) to cover all three connectors.
---

# Web Agent Connectors — SportMind

**SportMind provides the intelligence framework. A web agent provides the
live sensory input. This skill is the bridge between them.**

Three connectors. Each is narrow and explicit — not "browse the web for
sports news" but "fetch this specific URL, extract these specific fields,
translate them into SportMind inputs using this formula." The narrowness
is intentional. Web agents are brittle; tight scoping reduces failure modes.

This document extends `platform/fetch-mcp-disciplinary.md`, which established
the pattern of Fetch MCP + SportMind tools for disciplinary monitoring.
The same architecture applies to all three connectors here.

---

## Architecture — how web agents connect to SportMind

```
FLOW:
  SportMind tool call
    → Returns framework + target URL + extraction spec
    → Does NOT fetch live data (zero maintenance philosophy preserved)

  Web agent (Fetch MCP / Claude in Chrome / Playwright)
    → Fetches the URL returned by SportMind tool
    → Extracts the specified fields
    → Returns structured data

  SportMind reasoning
    → Applies the framework to the extracted data
    → Produces calibrated signal output

WHAT SPORTMIND PROVIDES:
  → Which URL to fetch (from verifiable-sources-by-sport.md)
  → What fields to extract (this document)
  → How to interpret the extracted data (framework files)
  → What to do when the source is unavailable (fallback rules)

WHAT THE WEB AGENT PROVIDES:
  → The actual HTTP fetch
  → HTML/text parsing
  → Raw extracted content

WHAT THE DEVELOPER PROVIDES:
  → The web agent infrastructure (Fetch MCP, browser, Playwright)
  → The integration plumbing between web agent and SportMind tools

SOURCE TIER RULE (non-negotiable):
  Web agents MUST only fetch Tier 1 and Tier 2 sources.
  See core/verifiable-sources-by-sport.md for tier definitions.
  Tier 3 and below: do not feed into SportMind signal chain.
  Unknown sources: classify first using core/external-intelligence-intake.md.
```

---

## Connector 1 — Lineup Confirmation

```
WHY THIS IS THE HIGHEST-PRIORITY CONNECTOR:
  Every SportMind pre-match signal degrades under the LINEUP_UNCONFIRMED flag.
  At T-2h, official lineups are posted on club accounts. Removing the need for
  a human to manually check and input these is the highest-friction reduction
  available in the entire pre-match chain.

WHAT TO FETCH:

  Football — club official X/Twitter account:
    URL pattern:  https://twitter.com/{club_handle}/with_replies
    Better:       https://nitter.privacydev.net/{club_handle} (no auth required)
    Alternative:  Premier League official: https://www.premierleague.com/news
    Post timing:  75 min before kickoff (official Premier League rule)
    Example:      https://twitter.com/Arsenal (look for "Starting XI" tweet)

  Football — league official lineup:
    Premier League: https://www.premierleague.com/match/{match_id}/lineups
    UEFA:           https://www.uefa.com/uefachampionsleague/match/{match_id}/lineups
    La Liga:        https://www.laliga.com/en-ES/laliga-ea-sports/{match_slug}

  Basketball — NBA official injury report:
    URL: https://www.nba.com/game/{game_id}/injury-report
    Note: NBA releases official injury report at T-90m and T-30m

  Cricket — playing XI announcement:
    URL: https://www.espncricinfo.com/series/{series_id}/match/{match_id}
    Timing: at toss, or pre-toss official announcement

  MMA — UFC fight card:
    URL: https://www.ufc.com/events
    Note: Weigh-in results confirm who competed (T-24h)

  Ice Hockey — morning skate confirmation:
    URL: Club official X account or beat reporter accounts
    Timing: T-5h to T-3h (morning skate report)
    Key signal: "skating" vs "did not skate" for injured players

WHAT TO EXTRACT:

  Starting XI (football):
    - 11 player names in starting lineup
    - Formation (4-3-3, 4-2-3-1, 3-5-2 etc.)
    - Notable absences from expected XI
    - Confirmed substitutes (if listed)

  Availability status (all sports):
    - Status: CONFIRMED_STARTER | CONFIRMED_ABSENT | PROBABLE | DOUBTFUL | DNP
    - For each player in the pre-match squad brief

TRANSLATION TO SPORTMIND INPUTS:

  Confirmed starter → availability_confidence = 1.00
  Club official post (Tier 1) confirms → availability_confidence = 0.98
  League official lineup page → availability_confidence = 1.00

  If expected key player NOT in lineup:
    → availability_confidence for that player = 0.00
    → Trigger: re-run ARI for team, remove player from composite
    → Raise: LINEUP_CHANGE_FLAG

  Formation change from expected:
    → Load core/tactical-matchup-intelligence.md to re-assess TMAS
    → If formation significantly different: TMAS_RECOMPUTE_REQUIRED flag

AGENT EXTRACTION INSTRUCTIONS:

  1. Call sportmind_pre_match first to get expected squad brief
  2. Fetch official lineup source at T-2h
  3. Compare fetched lineup against expected:
     - Match each name in fetched XI against expected XI
     - Fuzzy match acceptable (Saka = Bukayo Saka = B. Saka)
  4. For each discrepancy:
     - Expected starter confirmed absent → ABSENCE_CONFIRMED flag
     - Unexpected starter in XI → UNEXPECTED_INCLUSION flag
  5. Update ARI availability_confidence for each player
  6. If key player (ARI > 0.90 expected) absent → re-run full signal

FAILURE MODES AND FALLBACKS:

  Source unavailable (404, rate limit, auth wall):
    → Do NOT substitute a Tier 2 or 3 source as confirmation
    → Set availability_confidence = 0.85 (unconfirmed, not unknown)
    → Raise LINEUP_UNCONFIRMED flag
    → Try alternative source (league official) before accepting unconfirmed

  Lineup posted but parse fails:
    → Return raw text to agent for manual classification
    → Do not silently drop the data — flag for human review

  Lineup posted in language other than English:
    → Player names are language-independent — extract names regardless
    → Formation information may require translation

SPORT-SPECIFIC TIMING:

  Football (European):     T-75m official (earlier posts may be leaks)
  Football (Americas):     T-90m to T-60m
  Basketball (NBA):        T-90m official injury report
  Cricket:                 At toss (T-0 for batting order) or T-30m
  MMA:                     Weigh-in T-24h (confirms fight still on)
  Ice Hockey:              T-3h (morning skate reports)
  Rugby Union:             T-60m (official team sheet)
  Rugby League:            T-60m (NRL team list)
  Formula 1:               Grid confirmed post-qualifying (T-18h)
  Tennis:                  Match order confirmed day before
```

---

## Connector 2 — PATH_2 Supply Verification

```
WHY THIS IS THE HIGHEST-PRIORITY FAN TOKEN CONNECTOR:
  After a WIN, SportMind's PATH_2 framework predicts a supply burn of ~0.24%.
  The only way to confirm this happened is to check the Chiliz Chain directly.
  Manual verification requires navigating Chiliscan. A web agent closes this
  loop automatically, turning a prediction into a confirmed fact.

WHAT TO FETCH:

  PRIMARY — Chiliscan token info (circulating supply):
    URL: https://chiliscan.com/api?module=token&action=tokeninfo
         &contractaddress={contract_address}
    Returns: totalSupply, circulatingSupply, holders

  BURN CONFIRMATION — Chiliscan burn address balance change:
    URL: https://chiliscan.com/api?module=account&action=tokentx
         &contractaddress={contract_address}
         &address=0x0000000000000000000000000000000000000000
         &sort=desc&offset=10
    Returns: Recent transactions to burn address (0x0000...)

  TREASURY WALLET — Pre-liquidation detection:
    URL: https://chiliscan.com/api?module=account&action=tokenbalance
         &contractaddress={contract_address}
         &address={treasury_wallet_address}
    Returns: Current treasury balance

  TOKEN REGISTRY for contract addresses:
    Tool:   ft_registry from scripts/sportmind_ft_mcp.py
    Call:   ft_registry() → returns contract_address for each ticker

  Fan token holders overview (browser):
    URL: https://chiliscan.com/token/{contract_address}
    Content: Current supply, holder count, recent transactions
    Use when: API unavailable or quota exceeded

WHAT TO EXTRACT:

  From tokeninfo response:
    - totalSupply: current total supply (compare against pre-match)
    - circulatingSupply: current circulating supply
    - holders: current unique holder count

  From burn address transactions:
    - Recent transactions TO 0x0000... from contract address
    - Transaction hash (for verification)
    - Amount burned (in token units)
    - Block timestamp (compare to match end time)

  Season supply tracking (compute from extracted data):
    - Pre-match supply (stored from previous check)
    - Post-match supply (freshly fetched)
    - Delta = pre - post (positive delta = burn confirmed)
    - Season cumulative = sum of all confirmed deltas

TRANSLATION TO SPORTMIND INPUTS:

  WIN confirmed, burn transaction found within T+4h of match end:
    → ftp_event = "WIN_BURN_CONFIRMED"
    → supply_change_pct = (pre_supply - post_supply) / pre_supply × 100
    → Expected: ~0.24% (tolerance ±0.05%)
    → If within tolerance: BURN_CONFIRMED
    → If outside tolerance: BURN_ANOMALY — flag for review

  WIN confirmed, no burn transaction within T+4h:
    → AMM rebalancing may still be in progress
    → Wait until T+15h before raising BURN_MISSING flag
    → Check treasury wallet — funds may not have settled yet

  LOSS confirmed, supply unchanged:
    → ftp_event = "LOSS_SUPPLY_NEUTRAL"
    → supply_change_pct = 0 (expected)
    → If supply changed (increase): UNEXPECTED_SUPPLY_CHANGE — flag immediately

  Pre-liquidation detection (T-48h):
    → Monitor treasury wallet for USDT increase
    → If treasury USDT balance increases T-48h to T-24h before match:
       → ftp_event = "PRE_LIQUIDATION_DETECTED"
       → classification = "PROTOCOL_EVENT" (never bearish)

SEASON SUPPLY LOG — maintaining the record:

  After each confirmed burn event:
    - Store: {date, match, result, supply_before, supply_after, burn_pct, tx_hash}
    - Cumulative total updates automatically
    - This data feeds directly into ft_supply_history tool

  Storage format:
    {
      "season": "2025-26",
      "token": "AFC",
      "burns": [
        {
          "match": "Arsenal vs PSG UCL QF",
          "date": "2026-04-15",
          "result": "WIN",
          "supply_before": 20000000,
          "supply_after": 19952000,
          "burn_pct": 0.240,
          "tx_hash": "0xabc...",
          "confirmed": true
        }
      ],
      "cumulative_burn_pct": 0.240,
      "last_updated": "2026-04-15T23:00:00Z"
    }

FAILURE MODES AND FALLBACKS:

  Chiliscan API unavailable:
    → Try browser fetch of https://chiliscan.com/token/{contract_address}
    → Parse HTML for supply figures (less reliable but available)
    → If both fail: set burn_status = "UNVERIFIED" (not CONFIRMED)
    → Never assume burn happened — only confirmed transactions count

  Supply figure mismatch (different from expected burn amount):
    → Could be: additional supply changes unrelated to PATH_2
    → Could be: timing issue (AMM not settled)
    → Could be: PATH_2 mechanics changed
    → Action: flag SUPPLY_ANOMALY, halt automated tracking, escalate

  Rate limiting (Chiliscan free API: ~5 requests/second):
    → Space requests minimum 1 second apart
    → For monitoring agents: 10-minute poll interval is sufficient
    → Chiliscan free tier: no API key required for basic endpoints

TIMING RULES:

  Do NOT fetch supply immediately after match end:
    → AMM rebalancing takes T+15m minimum
    → Treasury settlement: T+4h typical, T+24h maximum
    → Recommended first check: T+30m post-match
    → Definitive check: T+6h post-match

  Pre-liquidation window:
    → Monitor from T-72h to T-0
    → Check treasury wallet every 12h in this window
```

---

## Connector 3 — Regulatory and Macro Monitoring

```
WHY THIS CONNECTOR HAS COMPOUNDING VALUE:
  Individual match signals decay after the match. Regulatory signals affect
  every analysis until superseded. A single confirmed regulatory change —
  like the March 2026 SEC/CFTC guidance — affects the entire US market tier
  permanently. Catching these early and updating the library prevents the
  macro layer from drifting out of sync with reality.

WHAT TO MONITOR:

  TIER 1 — Act within 24h (library update required):

  ESMA whitepaper register (MiCA compliance):
    URL:     https://www.esma.europa.eu/document/crypto-asset-white-papers
    What:    New fan token whitepapers registered or revoked
    Extract: Issuer name, token name, registration date, status
    Signal:  New registration → regulatory_compliance = CONFIRMED for that token
             Revocation → raise REGULATORY_RISK_FLAG for that token

  SEC/CFTC announcements:
    URL:     https://www.sec.gov/news/pressreleases
    URL:     https://www.cftc.gov/PressRoom/PressReleases
    What:    Any guidance mentioning fan tokens, digital collectibles, sports tokens
    Extract: Guidance classification, effective date, scope
    Signal:  New guidance → update macro/macro-regulatory-sportfi.md

  Chiliz official communications:
    URL:     https://www.chiliz.com/blog
    URL:     https://twitter.com/Chiliz
    What:    New fan token partnerships, PATH_2 rollouts, tokenomics changes,
             chain upgrades, omnichain migration updates
    Extract: New club names, effective dates, supply mechanic changes
    Signal:  New PATH_2 club → update library; new supply mechanics → urgent update

  TIER 2 — Review within 72h (queue for next library version):

  Socios.com partnership announcements:
    URL:     https://www.socios.com/fan-tokens
    What:    New team launches, token delistings, utility changes
    Extract: Team name, token ticker, sport, tier estimate
    Signal:  New token → add to registry; delisting → flag in registry

  CoinDesk / The Block — crypto regulatory coverage:
    URL:     https://www.coindesk.com/policy
    URL:     https://www.theblock.co/category/regulation
    What:    Fan token regulatory developments globally
    Extract: Jurisdiction, ruling type, affected tokens/platforms
    Signal:  Classify per core/external-intelligence-intake.md framework

  TIER 3 — Monitor (no automatic action):

  Mainstream sports media for commercial signals:
    Sources: BBC Sport, ESPN, Sky Sports
    What:    Major sponsorship deals, broadcast right changes, club financial news
    Action:  Flag for human review; do not auto-update library

EXTRACTION AND CLASSIFICATION WORKFLOW:

  1. Fetch source URL
  2. Extract: headline, date, jurisdiction, affected entities, ruling type
  3. Classify against core/external-intelligence-intake.md:
     - Tier 1 (act): confirmed regulatory fact, official source, direct impact
     - Tier 2 (queue): market signal, secondary analysis, trend data
     - Tier 3 (monitor): opinion, speculation, no direct regulatory impact
  4. For Tier 1: identify which library files need updating
     - SEC/CFTC guidance → macro/macro-regulatory-sportfi.md
     - New fan token → platform/sportmind-mcp-server.md + FAN_TOKEN_REGISTRY
     - Supply mechanic change → fan-token/gamified-tokenomics-intelligence/
     - ESMA registration → macro/macro-regulatory-sportfi.md
  5. Generate update recommendation with:
     - File path(s) to update
     - Specific section to change
     - Draft change text
     - Confirmation required: YES (human reviews before any library change)

MONITORING FREQUENCY:

  ESMA register:     Weekly (changes are rare and significant)
  SEC/CFTC:          Daily (during active regulatory periods)
  Chiliz blog:       Daily
  Chiliz Twitter:    Every 4h (same cadence as macro signal monitor)
  Socios:            Weekly
  CoinDesk/Block:    Daily

FAILURE MODES:

  Source returns 403 / login wall:
    → Use alternative source from same tier
    → Never use a lower-tier source as substitute for Tier 1

  Ambiguous ruling (unclear impact on fan tokens):
    → Classify as Tier 3 (monitor)
    → Flag for human expert review
    → Do NOT update library until classification confirmed

  Conflicting signals from multiple sources:
    → Official government/regulatory body always supersedes media reporting
    → Secondary analysis does not override primary source

  Language barrier (non-English regulatory source):
    → Do not auto-classify foreign-language regulatory text
    → Flag for human review with source URL and extracted date
```

---

## MCP configuration for web agent integration

```json
{
  "mcpServers": {
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    },
    "sportmind": {
      "command": "python",
      "args": ["/path/to/SportMind/scripts/sportmind_mcp.py"]
    },
    "sportmind-fan-token": {
      "command": "python",
      "args": ["/path/to/SportMind/scripts/sportmind_ft_mcp.py"]
    }
  }
}
```

```
RECOMMENDED CALL SEQUENCE:

Lineup confirmation (pre-match):
  1. sportmind_pre_match(sport, home, away, competition, kickoff)
  2. fetch(url=lineup_source_for_sport, at=T-2h)
  3. Extract lineup from fetched content
  4. Compare against expected squad brief from step 1
  5. Update ARI inputs for confirmed absences
  6. Re-run sportmind_pre_match with updated availability data

PATH_2 supply verification (post-match):
  1. ft_status(token) → get contract_address
  2. fetch(url=chiliscan_tokeninfo_api, contractaddress=contract_address)
  3. Extract post-match supply figure
  4. Compare against pre-match supply (stored from previous fetch)
  5. Confirm burn: delta within ±0.05% of expected 0.24%
  6. Log to season supply record

Regulatory monitoring (ongoing):
  1. fetch(url=esma_register) + fetch(url=chiliz_blog) on schedule
  2. Extract: issuer names, dates, ruling types
  3. Classify against external-intelligence-intake.md framework
  4. Generate update recommendation for human review
  5. Human confirms → library update applied
```

---

## Fragility acknowledgement

```
Web agents introduce fragility that the core library deliberately avoids.
These rules are architectural, not optional:

1. NEVER treat web agent output as ground truth without source tier check
   A tweet from an unofficial account is not a lineup confirmation.
   A blog post is not a regulatory fact.

2. NEVER auto-update the library from web agent output
   All regulatory and macro updates require human review and confirmation.
   The agent recommends. The human approves. Always.

3. NEVER apply burn modifier before T+15 post-match
   Even if Chiliscan shows a supply change, AMM rebalancing is not
   complete. The modifier applies only after the market has settled.

4. ALWAYS have a fallback for unavailable sources
   If the source is down: set confidence appropriately, raise a flag,
   continue with degraded signal. Do not halt the analysis.

5. ALWAYS log what was fetched, when, and what was extracted
   Web agent outputs that are not logged cannot be audited or debugged.
   Source URL + timestamp + extracted content → stored per analysis.
```

---

*SportMind v3.68 · MIT License · sportmind.dev*
*See also: platform/fetch-mcp-disciplinary.md · platform/realtime-integration-patterns.md*
*core/verifiable-sources-by-sport.md · core/external-intelligence-intake.md*
*core/breaking-news-intelligence.md · platform/chiliz-chain-address-intelligence.md*
*fan-token/gamified-tokenomics-intelligence/ · scripts/sportmind_ft_mcp.py*
