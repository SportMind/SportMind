---
name: external-intelligence-intake
description: >
  Classification framework for incoming external articles, news, research
  papers, and media as intelligence inputs to SportMind. Three-tier system:
  Tier 1 (act immediately — update library files), Tier 2 (queue for trend
  review — inform next version), Tier 3 (monitor — no immediate action).
  Trusted source registry by tier and domain. Verification thresholds before
  any library update. Decision rules for which library files each article type
  updates. Designed for the workflow: external article arrives → classify →
  identify impacted files → confirm with human → update library. The MCP
  intake tool (sportmind_ingest_article) implements this framework as a
  developer-accessible tool. Zero automatic library changes — the framework
  produces recommendations only; human confirmation required before any update.
---

# External Intelligence Intake — SportMind

**Not every article is equal. Not every update is urgent.
The framework for deciding what incoming intelligence means for the library.**

SportMind is an empirically grounded library. Its strength is that every claim
is verifiable and every modifier is calibrated. External articles are valuable
inputs — but they need to be classified before they change anything. The CoinDesk
SEC/CFTC article of April 2026 is a good example: the regulatory fact (guidance
issued March 17) is Tier 1 intelligence that directly updates the macro layer.
The commercial optimism in the same article is Tier 3 opinion that requires
calibration evidence before affecting any signal.

---

## The three-tier classification system

```
TIER 1 — ACT IMMEDIATELY (update library files within this session)
  Definition: Confirmed factual events that change the state of the world
  SportMind models. Not opinion, not forecast, not rumour.

  What qualifies:
    → Official regulatory guidance documents (SEC, CFTC, MiCA enforcement, etc.)
    → Confirmed new fan token launch (official Socios/Chiliz announcement)
    → Confirmed PATH mechanism change (new club confirmed on PATH_2, etc.)
    → Confirmed major partnership (new naming rights, major sponsorship)
    → Confirmed rule change in a sport (new points system, format change)
    → Confirmed market structure change (new exchange listing, delisting)
    → Confirmed significant calibration data (independently verified match result)
    → Peer-reviewed academic papers with empirical findings directly relevant
      to SportMind's frameworks (e.g., Ante et al. 2025 on fan token governance)

  Library files updated:
    Regulatory change     → macro/macro-regulatory-sportfi.md
    New token launch      → scripts/sportmind_mcp.py (registry) + relevant token skill
    PATH mechanism change → fan-token/gamified-tokenomics-intelligence/
    Major partnership     → relevant sport token intelligence + fan-token-lifecycle
    Sport rule change     → relevant sports domain skill + athlete skill
    Market structure      → fan-token/defi-liquidity-intelligence/ + macro
    Academic paper        → relevant core/ skill (e.g., fan-holder-profile cites Ante et al.)

  Verification required:
    Primary source confirmed (official announcement, regulatory document URL)
    Not retracted or disputed within 48h
    Source tier ≥ 2 (see trusted source registry below)

TIER 2 — QUEUE FOR TREND REVIEW (inform next version, not urgent update)
  Definition: Market analysis, confirmed trend signals, pattern documentation,
  and significant journalistic reporting that informs the library's trend and
  macro intelligence but does not represent a single confirmed factual event.

  What qualifies:
    → Major media analysis pieces (CoinDesk features, The Athletic deep dives)
    → Multiple independent confirmations of an emerging trend
    → Regulatory developments that are confirmed but whose impact is still evolving
    → New data or research that suggests a modifier value needs recalibration
    → Documented market behaviour patterns across multiple events
    → Suite development updates (Chiliz roadmap updates, new platform features)
    → World Cup 2026 intelligence (token launches, Chiliz programme updates)

  Library files updated (at next version release):
    Trend confirmation    → core/sports-trend-intelligence.md (new trend entry)
    Macro evolution       → macro/macro-overview.md + relevant specific macro file
    Modifier recalibration→ core/modifier-recalibration-vN.md (new recalibration record)
    Suite update      → fan-token/fan-token-lifecycle/ + gamified-tokenomics

  Verification required:
    Multiple independent sources (minimum 2 Tier 1/2 sources)
    Pattern confirmed across multiple events (not single data point)
    No active dispute or contradiction from primary actors

TIER 3 — MONITOR, NO IMMEDIATE ACTION
  Definition: Opinion pieces, retail-facing guides, prediction content,
  unconfirmed rumours, and single-source claims. Valuable context but
  requires corroboration before influencing any library signal.

  What qualifies:
    → Opinion articles (CoinDesk "Opinion" section, blog posts)
    → Retail investor guides and price prediction content
    → Single-source transfer rumours without Tier 1 confirmation
    → Social media posts, even from verified accounts
    → Press release content without independent verification
    → Analyst predictions about future regulatory or market developments

  Action: Note in monitoring queue. Do not update library.
  If a Tier 3 article subsequently gains Tier 1/2 corroboration: reclassify.
```

---

## Trusted source registry

```
TIER A SOURCES — Tier 1 articles almost always from these:
  Regulatory documents:
    SEC.gov official releases
    CFTC.gov official guidance
    EUR-Lex (EU MiCA official text)
    FCA.org.uk (UK Financial Conduct Authority)
    
  Chiliz/Socios ecosystem:
    Blog.chiliz.com (official Chiliz announcements)
    Socios.com official press releases
    KAYEN.finance official documentation
    Chiliz Chain GitHub (protocol-level changes)
    
  Sports governing bodies:
    FIFA.com, UEFA.com, NBA.com, NFL.com, ICC-cricket.com
    (Official rule changes, competition structures)

TIER B SOURCES — Tier 1 or 2 depending on content type:
  CoinDesk (coindesk.com) — news reports = Tier 1/2; opinion = Tier 3
  The Block (theblock.co) — news = Tier 1/2; analysis = Tier 2
  Decrypt (decrypt.co) — confirmed news = Tier 2; analysis = Tier 3
  CoinTelegraph (cointelegraph.com) — verified news = Tier 2
  BeInCrypto (beincrypto.com) — research pieces = Tier 2
  The Athletic (theathletic.com) — sports news = Tier 1/2 per journalist
  ESPN (espn.com/AP Sport) — confirmed transfers/results = Tier 1
  BBC Sport — confirmed = Tier 1
  Sky Sports — confirmed breaking = Tier 1; rumour = Tier 3
  Fabrizio Romano (@FabrizioRomano) — "here we go" = Tier 1 for transfers
  
TIER C SOURCES — Tier 2 or 3 only:
  Retail crypto guides (CryptoManiaks, CoinBureau general guides)
  Social media posts (even verified)
  Anonymous or pseudonymous analysis
  Company blog posts (self-reported metrics; verify independently)
  AI-assisted journalism (declared) — flag for additional verification

ACADEMIC SOURCES — Tier 1 for empirical findings, Tier 2 for frameworks:
  Peer-reviewed journals (Digital Business, Journal of Finance, etc.)
  SSRN pre-prints — Tier 2 until peer-reviewed
  Conference papers (ECIS, ICIS) — Tier 2
```

---

## Decision rules — what each article type updates

```
REGULATORY GUIDANCE (Tier 1):
  1. Identify jurisdiction (US, EU, UK, Asia-Pacific)
  2. Identify classification change (securities/utility/collectible/other)
  3. Update: macro/macro-regulatory-sportfi.md
     → Change jurisdiction status (BARRIER/UNCERTAIN/OPEN/RESTRICTED)
     → Update regulatory_clarity modifier value
     → Add to jurisdiction timeline
  4. Check: does this affect any active token in the MCP registry?
     If yes: flag relevant token intelligence file for review

NEW TOKEN LAUNCH (Tier 1):
  1. Verify: official Socios/Chiliz announcement (not rumour)
  2. Confirm: token address on Chiliz Chain (chiliscan.com)
  3. Update: scripts/sportmind_mcp.py fan token registry
  4. Create or update: sport-specific token intelligence file
  5. Update: fan-token/fan-token-lifecycle/ if launch creates new lifecycle data

ACADEMIC PAPER (Tier 1 empirical / Tier 2 framework):
  1. Read abstract and findings section
  2. Identify: which SportMind frameworks does this validate, challenge, or extend?
  3. If it validates: add citation to relevant skill file
  4. If it challenges: flag for recalibration consideration
  5. If it extends: evaluate whether new intelligence file is warranted
  Example: Ante et al. 2025 → fan-holder-profile-intelligence.md
           added four holder archetypes based on paper's expert interview findings

MARKET ANALYSIS PIECE (Tier 2):
  1. Extract: any confirmed data points (verified market metrics, confirmed events)
  2. Separate: confirmed data from author's interpretation/opinion
  3. Confirmed data only → queue for core/sports-trend-intelligence.md update
  4. Do not carry author's commercial optimism or pessimism into library
  5. Check: does the confirmed data suggest modifier recalibration?

WORLD CUP 2026 INTELLIGENCE (Tier 1 or 2 depending on source):
  High priority category — tournament June/July 2026.
  Any confirmed national team token launch → Tier 1 (update MCP registry)
  Any confirmed commercial partner → Tier 1 (update world-cup-2026-intelligence)
  Market analysis/prediction → Tier 2 (inform trend update)
```

---

## The intake workflow

```
STEP 1 — ARTICLE ARRIVES
  You share a URL or paste article text.
  (Or the sportmind_ingest_article MCP tool fetches it — see below.)

STEP 2 — CLASSIFY
  Apply three-tier classification.
  Identify the primary intelligence type (regulatory/market/academic/etc.)
  Check source tier from registry.

STEP 3 — EXTRACT FACTS
  Separate confirmed facts from opinion/interpretation.
  For each confirmed fact: which library file does it affect?
  State the specific claim: "SEC/CFTC issued guidance March 17, 2026
  classifying fan tokens as digital collectibles and digital tools."

STEP 4 — IMPACT ASSESSMENT
  For Tier 1: identify specific lines/sections in library files to update.
  State the before and after: "US status in macro-regulatory-sportfi.md
  currently shows UNCERTAIN → should show OPEN post March 17 guidance."
  Note: file already updated in this case (library was ahead of the article).

STEP 5 — HUMAN CONFIRMATION
  Present the assessment. Pele confirms or adjusts.
  Zero automatic changes. The framework recommends; the human decides.

STEP 6 — IMPLEMENT OR QUEUE
  Tier 1 confirmed: implement in current session, changelog entry.
  Tier 2 confirmed: add to version backlog, implement at next release.
  Tier 3: log in monitoring queue, no library change.
```

---

## The sportmind_ingest_article MCP tool (specification)

```
Tool name: sportmind_ingest_article
Purpose: Fetch an article URL, classify it, identify impacted files,
         return structured intake brief.

INPUT:
  url: string — the article URL
  context: string (optional) — brief description of why this is relevant

OUTPUT:
  {
    "tier": 1 | 2 | 3,
    "tier_label": "ACT_IMMEDIATELY" | "QUEUE_FOR_REVIEW" | "MONITOR",
    "source_tier": "A" | "B" | "C",
    "intelligence_type": "regulatory" | "market" | "academic" | "ecosystem" | "opinion",
    "confirmed_facts": [
      "Fact 1: SEC/CFTC joint guidance issued March 17, 2026..."
    ],
    "opinion_content": "Summary of interpretive/opinion content (not acted on)",
    "impacted_files": [
      {
        "file": "macro/macro-regulatory-sportfi.md",
        "current_state": "...",
        "recommended_update": "..."
      }
    ],
    "action_required": "Update macro-regulatory-sportfi.md US section" | "Queue for trend review" | "No action",
    "already_reflected": true | false,
    "confidence": 0.90,
    "source_url": "...",
    "fetched_at": "ISO-8601"
  }

Implementation: Uses platform/fetch-mcp-disciplinary.md pattern for URL fetch.
Applies this classification framework as the reasoning prompt.
All output is advisory — no automatic file writes.
```

---

## Standing intelligence feeds to monitor

```
These sources should be checked regularly regardless of incoming articles:

WEEKLY CHECK:
  Blog.chiliz.com — suite announcements, new token launches
  KAYEN.finance — token registry updates, new listings
  Socios.com newsroom — official partner announcements
  Macro crypto: BTC 200-day MA status (macro modifier trigger)

MONTHLY CHECK:
  CoinDesk Fan Token™ coverage — market analysis pieces
  Chiliz Chain GitHub — protocol-level changes
  Relevant academic pre-print servers (SSRN: blockchain, sports finance)

BEFORE MAJOR EVENTS (tournament windows, transfer windows):
  Chiliz official roadmap updates
  National team fan token launch announcements
  New FTP PATH confirmations or changes
  Regulatory developments in key markets (US, UK, Asia-Pacific)

WORLD CUP 2026 SPECIFIC (June–July 2026):
  Daily: Chiliz official channels
  Per match: KAYEN token price on-chain
  Per result: FTP burn transaction confirmation on chiliscan.com
```

---


---

## Processed intake — Fan Token Play (April 2026)

```
INTAKE DATE: 17 April 2026
CLASSIFICATION: TIER 1 — ACT IMMEDIATELY (source: Chiliz official)

ARTICLE 1:
  Title:  "The Chiliz Group Announces Gamified Fan Tokens Including Disruptive
           New Mint and Burn Tokenomics"
  Source: chiliz.com/blog
  Date:   09 April 2026
  URL:    https://www.chiliz.com/chiliz-group-announces-gamified-fan-tokens...
  
ARTICLE 2:
  Title:  "Win and They Burn, Lose and They Mint: Fan Token Play Explained"
  Source: chiliz.com/blog
  Date:   17 April 2026
  URL:    https://www.chiliz.com/win-and-they-burn-lose-and-they-mint-fan-token-play-explained/

ACTIONS TAKEN (v3.74.0):
  1. fan-token/gamified-tokenomics-intelligence/gamified-tokenomics-intelligence.md
     → Added competitive matches scope section (friendlies/pre-season excluded)
     → Flagged PATH_1 goal-difference scaling as UNVERIFIED (not in either article)
     → Fixed annual inflation framing (integral protocol, not fallback)
     → Added tiered inflation model detail (0% <45% win rate, scales >60%)
     → Added T+48h execution windows for both WIN and LOSS
     → Added vesting cap current status (not active for any token — Apr 2026)
     → Added binary WIN confirmation (no goal-diff confirmed)
     → Updated sources and version footer

  2. compressed/README.md
     → FTP compressed skill updated with all corrections

NEW FACTS CONFIRMED:
  - PATH_1: Binary WIN/LOSS only — no goal-difference scaling in protocol
  - PATH_2: Both buyback (WIN) and minting (LOSS) execute within 48h of result
  - Vesting cap: defined in protocol but not currently active for any token
  - Competitive matches only: friendlies, pre-season, academy, women's excluded
  - Annual inflation 1-5%: three models under evaluation (variable, static, tiered)
  - First trial: $AFC vs Sporting Lisbon, UCL, 07 April 2026 (confirmed)

OUTSTANDING UNCERTAINTY:
  - PATH_1 exact burn rate per win not confirmed in either article
  - PATH_1 full rollout timeline not specified ("coming months")
  - Future tokens beyond $AFC not named
```


---

## Processed intake — Academic batch (April 2026)

```
INTAKE DATE: 18 April 2026
CLASSIFICATION: TIER 1 (Ante et al.) / TIER 2 (Zhou et al., Awad)

ARTICLE 1: ★★★★ HIGH VALUE
  Title:  "Blockchain-based fan tokens as a strategic resource for sports
           clubs: Opportunities, challenges, and a stakeholder-oriented model"
  Source: Digital Business (Elsevier), Volume 5 (2025) 100137
  Date:   July 2025 (online) / December 2025 (print)
  DOI:    10.1016/j.digbus.2025.100137
  Method: Qualitative — expert interviews, German professional football

  KEY FINDINGS USED:
  - Stakeholder decision framework: power/legitimacy/urgency across
    clubs, fans, investors, sponsors, associations
  - Six-dimension opportunity/challenge matrix (Economic/Social/
    Technological/Political/Legal/Environmental)
  - Membership devaluation risk (50+1 ownership structure clubs)
  - Two-tier supporter exclusion risk (digital barriers)
  - Expert consensus: largest challenges are market volatility, lack of
    internal resources, and stakeholder alignment

  ACTIONS TAKEN:
  → fan-token/fan-token-partnership-intelligence/: Part 6 added —
    Pre-adoption strategic decision framework with stakeholder map,
    six-dimension matrix, agent rules, and output schema extension

ARTICLE 2: ★★★ MODERATE VALUE
  Title:  "Cryptocurrency in sport: a thematic review"
  Source: Frontiers in Psychiatry 16:1745490, January 2026
  DOI:    10.3389/fpsyt.2025.1745490
  Method: Thematic review — 30 peer-reviewed studies, 2019–2025

  KEY FINDINGS USED:
  - Ante, Schellinger & Demir (2024) intraday event study: fan token
    returns decline −0.8% during matches, −0.7% post-match; LOSS EFFECT
    asymmetry confirmed — losses trigger larger negative reactions than
    wins create positive ones
  - Ante et al. (2024) voting data: ~50% of token holders participate
    in governance votes on average (empirical baseline for GSI assessment)
  - Confirms archetype distinction (fans vs speculators) across multiple
    independent studies
  - Five research themes mapped — gambling-like risks now multi-study
    validated, not single-paper finding

  ACTIONS TAKEN:
  → core/post-match-signal-framework.md: Loss-effect asymmetry section
    added — calibration rules for expected vs unexpected wins/losses,
    PATH_2 interaction note, draw disappointment discount
  → fan-token/fan-holder-profile-intelligence.md: governance participation
    baseline (50%) now citable from empirical source
  → examples/application-layer/README.md: governance health dashboard
    action updated to cite 50% participation empirical baseline

ARTICLE 3: ★★ CONTEXT VALUE ONLY
  Title:  "Leveraging Digital Fan Engagement for Sports Brand Loyalty:
           A Study of Emerging Marketing Strategies in Saudi Arabia"
  Source: University of Bisha academic journal, 2025
  Method: Quantitative survey — 300 students, University of Bisha
  
  KEY FINDINGS:
  - No statistically significant relationship between digital engagement
    and brand loyalty in Saudi Arabian university student context
  - Brand image did not mediate the relationship
  - Cultural and contextual factors moderate digital engagement → loyalty
    conversion (not universal)
  
  ASSESSMENT: Single-context study, limited generalisability, no novel
  intelligence for SportMind's current scope. Noted for future context
  if library expands to MENA fan token markets.
  
  ACTIONS TAKEN: None. Registered as context-only intake.

PREVIOUSLY PROCESSED (April 9/17 2026):
  See intake entry: "Fan Token Play (April 2026)" — Chiliz official articles
```

*SportMind v3.63 · MIT License · sportmind.dev*
*See also: macro/macro-regulatory-sportfi.md · core/media-intelligence.md*
*core/sports-trend-intelligence.md · platform/chiliz-chain-address-intelligence.md*
*fan-token/world-cup-2026-intelligence/*
