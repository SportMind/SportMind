# SportMind Application Layer — Actionable Acts

**What your application can do with SportMind intelligence.**

SportMind reasons. Your application acts.

This document catalogues the concrete actions the application layer can
take once SportMind's intelligence layer has produced its output — organised
by domain, grounded in the intelligence SportMind actually provides today,
and with the freedom to build custom actions stated explicitly throughout.

The eleven agent types in `examples/agent-types/README.md` define *how* to
build the intelligence layer. This document defines *what to do with it*.

---

## How to read this document

Each action entry has four parts:

```
ACTION NAME
  What it does:    The concrete act the application performs
  Intelligence:    The SportMind signals that power it
  Integration:     External system required (if any)
  Experience:      What the end user sees or receives
```

Every action listed is buildable today with the current library.
None require capabilities SportMind doesn't have.

---

## The application layer in one diagram

```
SportMind intelligence output
  ↓
  adjusted_score, SMS, direction, modifiers, flags, CDI, LTUI,
  ABS, DQI, TVS, MRS, BVS, CQS, NCSI, GSI, PATH_2 status ...
  ↓
APPLICATION LAYER
  ↓
  Notify  ·  Execute  ·  Publish  ·  Generate  ·  Alert
  Verify  ·  Rank     ·  Route    ·  Store     ·  Display
```

The application layer is everything after the intelligence output.
SportMind never crosses the line into execution. Everything below that
line is yours to build.

---

## Domain 1 — Fan token actions

The richest domain. Fan Token Play, supply mechanics, holder archetypes,
lifecycle phases, governance, and on-chain verification all create
distinct actionable moments.

---

### 1.1 — Trade execution routing

```
What it does:    Routes buy/sell/hold decisions to an execution layer
                 based on SportMind's ENTER/WAIT/ABSTAIN signal.
Intelligence:    adjusted_score, SMS, recommended_action, macro_modifier,
                 MRS (fraud check), LTUI (lifecycle position)
Integration:     Chiliz Agent Kit (TypeScript SDK), FanX DEX, any CEX API
Experience:      Agent executes or proposes a position. Human approves
                 at Autonomy Level 0-2; agent acts at Level 3-4.

EXAMPLE FLOW:
  SportMind output: { direction: "ENTER", sms: 82, mrs_score: 12 }
  Application acts: route to Chiliz Agent Kit → execute buy
  Guard: if mrs_score >= 75 → ABSTAIN regardless of direction signal
  Guard: if macro_override_active → suspend all positions

KEY FILE: platform/chiliz-agent-kit-integration.md
```

---

### 1.2 — Supply event notification

```
What it does:    Notifies holders when a PATH_2 burn or mint event
                 is confirmed on-chain. Different messages for WIN
                 (supply reduced — scarcity signal) vs LOSS (neutral).
Intelligence:    PATH_2 verification status (BURN_CONFIRMED / NEUTRAL),
                 burn_pct, season_net_change_pct, LTUI trajectory
Integration:     Push notification service, email, Telegram bot,
                 Socios notification API
Experience:      "Arsenal won. 0.24% of $AFC supply permanently burned.
                 Season total: 2.1% reduction. Scarcity is building."

TIMING RULE: Never notify before T+15 post-match (AMM rebalancing).
             Recommended: T+30min for initial; T+6h for definitive.

KEY FILES: fan-token/gamified-tokenomics-intelligence/
           platform/web-agent-connectors.md (wa_supply_verify)
```

---

### 1.3 — Holder-archetype engagement

```
What it does:    Sends targeted content to the right holder archetypes
                 at the right time. Governors get governance alerts.
                 Loyalists get match build-up. Speculators get supply
                 signals. Amplifiers get shareable moments.
Intelligence:    CHI (community health), holder archetype distribution,
                 CDI (commercial durability), active vote quality, GSI
Integration:     CRM platform, Socios engagement API, push service,
                 email marketing tool
Experience:      Governor receives a vote brief 72h before close.
                 Loyalist receives squad news T-2h. Amplifier receives
                 "Share this" post after a BURN_CONFIRMED event.

DO NOT: send governance alerts to Speculators — they don't vote and
        it drives churn. Wrong archetype targeting damages CHI.

KEY FILES: fan-token/fan-holder-profile-intelligence.md
           platform/fan-engagement-connector.md
```

---

### 1.4 — Governance vote campaign

```
What it does:    Runs a structured notification sequence around an
                 active governance vote — quality check, archetype
                 targeting, T-72h / T-24h / T-4h / result sequence.
Intelligence:    GSI score, vote quality classification, participation
                 rate, governor archetype share, CDI extension signal
Integration:     Socios governance API, notification service
Experience:      Substantive votes drive engagement. Trivial votes
                 are silently skipped — protecting governor trust.
                 Post-close result is shared as a community moment.

KEY FILE: fan-token/sports-governance-intelligence/
          scripts/sportmind_gc_mcp.py (gc_governance_state, gc_vote_alert)
```

---

### 1.5 — Lifecycle phase dashboard

```
What it does:    Displays the fan token's current lifecycle phase
                 (1–5e) with commercial context — what it means,
                 what typically happens next, what to watch.
Intelligence:    LTUI trajectory, lifecycle phase, CDI, HAS trend,
                 ATM score for key squad members
Integration:     Web dashboard, mobile app, Socios embed
Experience:      "$PSG is in Phase 3 — established utility with DeFi
                 integration approaching. CDI is elevated heading into
                 the UCL knockout phase. Watch for Phase 4 signals in
                 Q3 if DeFi launch confirmed."

KEY FILE: fan-token/fan-token-lifecycle/
```

---

### 1.6 — Portfolio context report

```
What it does:    Explains why each token in a portfolio moved — not
                 just the price change but the sporting, commercial,
                 and on-chain reason behind it.
Intelligence:    FTIS, NCSI, ATM, macro_modifier, DSM, LTUI, CDI,
                 seasonal supply position, PATH_2 event log
Integration:     FanTokenIntel (data layer), portfolio UI
Experience:      "Your $BAR token is down 4.2% today. Spain qualified
                 for the World Cup quarter-final last night but Pedri
                 picked up a knock — the ATM concern outweighed the
                 NCSI uplift. We're monitoring."

KEY FILES: fan-token/football-token-intelligence/
           examples/fan-token-intel/integration-fan-token-intel.md
```

---

### 1.7 — Fraud alert

```
What it does:    Raises an alert when MRS (Manipulation Risk Score)
                 exceeds the threshold — stops execution and notifies
                 the operator before any position is taken or held.
Intelligence:    MRS 0–100, six attack types, TVI ratio, wallet age,
                 wash trading signals, coordinated buy/sell patterns
Integration:     Alert system, position management system
Experience:      Operator receives: "COMPROMISED signal on $XYZ.
                 MRS 78/100. Suspected wash trading. All positions
                 suspended pending human review."

THRESHOLD: MRS ≥ 75 = COMPROMISED (auto-ABSTAIN)
           MRS 50–74 = SUSPECT (WAIT, flag for review)

KEY FILE: platform/fraud-signal-intelligence.md
```

---

### 1.8 — World Cup tournament tracker

```
What it does:    Manages parallel supply and signal tracking across
                 8+ tokens for 39 days. Cascade CALENDAR_COLLAPSE on
                 elimination. Apply NCSI round amplifiers. Verify
                 $AFC burns per match. Reset post-July 19.
Intelligence:    NCSI amplifiers (×3.5→4.0), CDI windows by stage,
                 PATH_2 burn events, post-tournament decay phases
Integration:     Dashboard, portfolio tool, notification service
Experience:      Real-time tournament tracker showing which tokens
                 are still active, which have CALENDAR_COLLAPSED,
                 and what the cumulative supply reduction is for $AFC.

KEY FILES: fan-token/world-cup-2026-intelligence/
           fan-token/gamified-tokenomics-intelligence/
```

---

## Domain 2 — Commercial and brand actions

SportMind's commercial intelligence — ABS, APS, BVS, AFS, TVS — is
designed to be delivered as structured output to commercial stakeholders.
The application layer here is often a document, a brief, or a dashboard
rather than an execution action.

---

### 2.1 — Athlete commercial brief

```
What it does:    Generates a structured commercial brief for a player —
                 brand value, social reach, portability score, fan token
                 impact, and sponsorship compatibility.
Intelligence:    ABS (Athlete Brand Score), AELS (social lift),
                 APS (portability), SHS (social health), PS (professionalism),
                 AFS (audience fit), fan token ATM contribution
Integration:     PDF generation, CRM output, sports agency platform
Experience:      Sports agent receives: "Viktor Gyökeres — Brand Score 71.
                 Social following 4.2M. APS 0.68 (brand travels with him).
                 Sponsor audience fit: sportswear brands 94%, automotive 71%."

KEY FILES: fan-token/fan-token-athlete-brand-score/
           fan-token/fan-token-sponsorship-match.md
           scripts/sportmind_sc_mcp.py (sc_cvs_brief)
```

---

### 2.2 — Transfer valuation report

```
What it does:    Generates a structured valuation report comparing
                 market value against DQI-adjusted value — surfaces
                 the gap and flags UNDERVALUED targets.
Intelligence:    DQI, TVS (Transfer Viability Score), DLVS (loan value),
                 RAF (Residual Athletic Fit), APS, fan token ATM impact
Integration:     Scouting platform, club analytics dashboard, agent tool
Experience:      Club director sees: "Gyökeres market €90M / DQI-adjusted
                 €108M — UNDERVALUED by €18M. Viability score 81/100.
                 World Cup NCSI exposure adds post-tournament value uplift."

KEY FILES: core/transfer-negotiation-intelligence.md
           core/athlete-decision-intelligence.md
           scripts/sportmind_sc_mcp.py
```

---

### 2.3 — Sponsorship matching

```
What it does:    Scores brand-athlete alignment for sponsorship decisions —
                 AFS tells you whether a brand's target demographic overlaps
                 with an athlete's actual audience.
Intelligence:    AFS (Audience Fit Score), ABS, SHS, PS, fan token
                 holder archetype demographics, CDI
Integration:     Sports marketing platform, brand agency tool
Experience:      Brand manager sees: "Lamine Yamal — Sportswear AFS 96,
                 Automotive AFS 42, Financial services AFS 71. Primary
                 audience: 18-24 male, 68% Southern Europe, 22% LATAM."

KEY FILE: fan-token/fan-token-sponsorship-match.md
          fan-token/fan-token-sports-brand-sponsorship.md
```

---

### 2.4 — Broadcast value signal

```
What it does:    Provides BVS scores to broadcast rights teams,
                 schedulers, and media partners for commercial
                 decisions — which matches are highest value,
                 which slots maximise reach.
Intelligence:    BVS, CQS (Context Quality Score), rights tier,
                 audience reach tier, DTS effect (documentary uplift)
Integration:     Rights management platform, scheduling tool,
                 broadcaster analytics dashboard
Experience:      Scheduler sees: "Arsenal vs PSG UCL QF — BVS 91.
                 US primetime slot adds 1.35× CQS. Recommend 20:00 ET."

KEY FILES: market/broadcaster-media-intelligence.md
           core/contextual-signal-environment.md
           scripts/sportmind_bc_mcp.py
```

---

### 2.5 — Club fan token strategy report

```
What it does:    Produces a pre-launch or annual strategic review for
                 a club considering or managing a fan token — LTUI
                 projection, partnership health score, DeFi readiness,
                 holder archetype target mix.
Intelligence:    LTUI lifecycle model, PHS (Partnership Health Score),
                 CHI targets, CDI drivers, competitive landscape
Integration:     Consultancy output, club commercial department tool
Experience:      Club commercial director receives a structured report:
                 "Based on your fanbase depth score and existing digital
                 asset adoption, a Phase 2 launch targeting Governor
                 and Loyalist archetypes is projected to reach LTUI
                 Tier B within 18 months."

KEY FILES: fan-token/fan-token-partnership-intelligence/
           fan-token/fan-token-lifecycle/
           examples/applications/app-04-sports-brand-token-strategy.md
```

---

### 2.6 — Narrative commercial window alert

```
What it does:    Alerts commercial teams when a high-narrative window
                 is opening — a record chase, a revenge fixture, a
                 must-win elimination — creating a moment for brand
                 activations, content campaigns, or partnership
                 visibility uplift.
Intelligence:    Narrative score 0-100, category (revenge/record/
                 comeback/rivalry), CDI extension signal, AELS uplift,
                 social volume multiplier vs baseline
Integration:     Marketing platform, social scheduling tool, campaign
                 management system
Experience:      Marketing team receives: "High narrative window opening
                 72h: Arsenal vs Man City (revenge — FA Cup Final 2025).
                 Narrative score 78/100. AELS elevated. Activate
                 pre-planned campaign assets now."

KEY FILE: core/core-narrative-momentum.md
          fan-token/kol-influence-intelligence/
```

---

## Domain 3 — Prediction market and DeFi actions

---

### 3.1 — Pre-match signal publication

```
What it does:    Publishes SportMind's structured pre-match signal to
                 a prediction market before open — giving participants
                 direction, confidence tier, and modifier breakdown
                 that generic markets don't provide.
Intelligence:    direction, adjusted_score, SMS, modifiers_applied,
                 flags, reasoning sequence
Integration:     Azuro Protocol, Polymarket, any on-chain prediction
                 market; or off-chain via API
Experience:      Market participants see structured intelligence with
                 confidence tier before placing positions. The signal
                 separation (sporting outcome vs macro) is transparent.

KEY FILE: core/prediction-market-intelligence.md
          examples/applications/app-01-defi-prediction-market.md
```

---

### 3.2 — Liquidity signal alert

```
What it does:    Alerts when DeFi liquidity conditions around a fan token
                 change in ways that affect position sizing or execution —
                 TVL shift, slippage threshold breached, LP activity spike.
Intelligence:    DeFi signal category, TVL trend, slippage estimate,
                 LP activity signal, cross-DEX arbitrage flag
Integration:     FanX DEX, on-chain monitoring (chiliscan), LP dashboard
Experience:      "Liquidity warning: $AFC pool TVL down 18% in 4h.
                 Slippage on >$5k position estimated at 1.8%.
                 Consider splitting or waiting for rebalancing."

KEY FILE: fan-token/defi-liquidity-intelligence/
```

---

### 3.3 — GameFi signal layer

```
What it does:    Powers on-chain fantasy or prediction games with
                 SportMind's SMS as the intelligence layer — players
                 who load better intelligence get a genuine edge.
Intelligence:    SMS, direction, sport-specific signal weights,
                 LQI (lineup quality), TMAS (tactical matchup)
Integration:     On-chain game contract (Chiliz Chain or EVM),
                 game frontend, result oracle
Experience:      Fantasy league player loads SportMind intelligence
                 and sees their picks scored against SMS confidence.
                 Better intelligence = better in-game outcomes.

KEY FILE: examples/applications/app-06-sports-gamefi-layer.md
```

---

### 3.4 — Collateral health monitor

```
What it does:    Monitors whether fan tokens used as collateral in
                 DeFi protocols remain above safe collateralisation
                 thresholds — LTUI decline, lifecycle phase change,
                 or CALENDAR_COLLAPSE could trigger margin calls.
Intelligence:    LTUI trajectory, lifecycle phase, CDI, HAS trend,
                 CALENDAR_COLLAPSE event detection, macro modifier
Integration:     CollateralFi protocol, DeFi lending dashboard
Experience:      Lender receives: "Collateral health alert: $BAR
                 collateral position LTUI declining. CDI compressed
                 post-UCL elimination. Recommend reducing LTV ratio
                 pending new season narrative."

KEY FILE: fan-token/rwa-sportfi-intelligence/ (CollateralFi section)
```

---

## Domain 4 — Operational and club actions

---

### 4.1 — Pre-match build-up brief

```
What it does:    Generates a plain-English pre-match briefing for
                 fans, analysts, or internal club staff — squad status,
                 manager signals, opponent context, and key watch items.
Intelligence:    LQI, ARI, pre-match-squad-intelligence, TMAS,
                 OTP (opponent tendency), narrative score, weather
Integration:     Club website, fan app, internal comms system,
                 media platform
Experience:      Fan sees: "Arsenal vs PSG — UCL QF. Saka is doubtful
                 (ATM concern). Martinelli confirmed. PSG's corner
                 delivery from the left is their primary set piece
                 threat. Watch for Dembélé inside right channel runs."

KEY FILES: core/pre-match-squad-intelligence.md
           core/opponent-tendency-intelligence.md
           agent-prompts/agent-prompts.md (Prompt 22)
```

---

### 4.2 — Scouting pipeline output

```
What it does:    Produces ranked scouting reports for transfer targets —
                 CVS scores, DQI, system fit, valuation gap, fan token
                 commercial impact — in a format a sporting director
                 can act on.
Intelligence:    CVS (Composite Value Score), DQI, TMAS system fit,
                 RAF, APS, UNDERVALUED flag, fan token ATM acquisition
                 impact for the buying club
Integration:     Scouting platform, internal transfer committee tool
Experience:      Sporting director sees a ranked shortlist with one
                 paragraph per target: performance, commercial value,
                 system fit, risk, and the token impact of signing them.

KEY FILES: examples/agentic-workflows/scouting-agent.md (Pattern 10)
           scripts/sportmind_sc_mcp.py
           examples/applications/app-09-talent-scouting.md
```

---

### 4.3 — Standings intelligence alert

```
What it does:    Alerts when a club crosses a meaningful standings
                 threshold — title clinch possible, UCL place
                 confirmed, relegation zone entered — and surfaces
                 the commercial implications for the fan token.
Intelligence:    SIB (Standings Intelligence Brief), trajectory,
                 proximity flags, LTUI trajectory from standings phase
Integration:     Club analytics dashboard, fan app, token platform
Experience:      Token holder receives: "Arsenal have moved to within
                 4 points of the title with 5 games left. LTUI
                 trajectory upgraded to STRONGLY POSITIVE. Each
                 remaining WIN is now a championship narrative event."

KEY FILE: core/standings-intelligence.md
          scripts/sportmind_gc_mcp.py (gc_standings)
```

---

### 4.4 — Breaking news response

```
What it does:    Fires immediately when a Tier 1 breaking news event
                 occurs — injury confirmed, manager sacked, transfer
                 announced — and publishes an updated signal with
                 the news already factored in.
Intelligence:    Breaking news category (1–8), signal update delta,
                 DSM impact, ATM impact on fan token, LTUI effect
Integration:     News monitoring webhook, push service, trading system
Experience:      Operator receives signal update within minutes of
                 the breaking news hitting Tier 1 sources — not
                 hours later when everyone already knows.

KEY FILES: core/breaking-news-intelligence.md
           core/media-intelligence.md
```

---

### 4.5 — Wearable performance feed

```
What it does:    Translates wearable biometric data (GPS load,
                 heart rate, recovery scores) into ARI inputs —
                 feeds readiness intelligence into the pre-match
                 signal automatically.
Intelligence:    ARI (Athlete Readiness Index), fatigue trajectory,
                 injury risk accumulation, recovery penalty
Integration:     Catapult, STATSports, Whoop, Oura, StatsBomb 360
                 (via platform/wearable-biometric-connectors.md)
Experience:      Analyst sees: "Saka: ARI 0.82 (CONCERN flag).
                 GPS load peaked Thursday. Recovery 71%. Suggest
                 consideration for rotation or reduced role."

KEY FILE: platform/wearable-biometric-connectors.md
```

---

## Domain 5 — Developer and platform actions

Actions for developers building on top of SportMind as an infrastructure
layer — surfacing intelligence to end users, other developers, or
downstream systems.

---

### 5.1 — MCP tool integration

```
What it does:    Connects any MCP-compatible client (Claude Desktop,
                 Cursor, any MCP host) to SportMind's 45 tools across
                 8 servers — making the full intelligence library
                 available as tool calls in any agent conversation.
Intelligence:    All layers — 45 tools across 8 servers
Integration:     MCP client configuration (claude_desktop_config.json)
Experience:      Developer asks Claude "What's the pre-match signal for
                 Arsenal tonight?" — Claude calls sportmind_pre_match,
                 gets a structured output, and reasons with it.

KEY FILE: platform/sportmind-mcp-suite.md
```

---

### 5.2 — Intelligence API endpoint

```
What it does:    Exposes SportMind intelligence as a REST API for
                 downstream applications — mobile apps, web frontends,
                 third-party integrations — without requiring direct
                 library access.
Intelligence:    Any SportMind output via skills_api.py
Integration:     Any HTTP client; documented in platform/api-contracts.md
Experience:      Mobile app calls /signal?sport=football&home=Arsenal
                 and receives JSON with direction, SMS, and modifiers.

KEY FILES: scripts/sportmind_api.py
           platform/api-contracts.md
```

---

### 5.3 — FanTokenIntel intelligence stack

```
What it does:    Combines FanTokenIntel's live signal scores and on-chain
                 data with SportMind's reasoning layer — FTI provides
                 the raw numbers, SportMind provides the interpretation.
Intelligence:    FTIS overlay on FTI base scores, sport-specific context,
                 athlete modifier, macro gating
Integration:     FanTokenIntel API
Experience:      Developer gets a compound signal: FTI score + SportMind
                 context = a signal that knows both the on-chain momentum
                 AND why it's happening in sporting terms.

KEY FILE: examples/fan-token-intel/integration-fan-token-intel.md
```

---

### 5.4 — SportFi Kit full-stack application

```
What it does:    Uses SportFi Kit's React components, Chiliz hooks,
                 and smart contract layer as the application shell,
                 with SportMind providing the intelligence layer —
                 the complete production stack from UI to on-chain.
Intelligence:    Full five-layer stack via Skills API
Integration:     SportFi Kit (github.com/AltcoinDaddy/Sportfi-kit)
Experience:      Developer ships a complete fan engagement application
                 in days rather than months — UI, chain interaction,
                 and sports intelligence all connected.

KEY FILE: examples/applications/app-07-sportfi-kit-integration.md
```

---

### 5.5 — Compressed skill delivery

```
What it does:    Delivers token-efficient summaries (~70% smaller) to
                 agents operating with constrained context budgets —
                 enabling intelligence without burning tokens on full
                 skill files.
Intelligence:    78 compressed skills covering all major domains
Integration:     Any LLM via context loading; MCP via compressed=true flag
Experience:      Agent receives the key rules, modifiers, and thresholds
                 for a skill in 500–800 tokens. Enough to reason with.
                 Not a replacement for the full skill on high-stakes decisions.

KEY FILE: compressed/README.md
```

---

## The most important thing this document doesn't say

These fifty-plus actions are **examples, not a catalogue of everything possible**.

SportMind is an intelligence layer. The application layer is whatever you
build on top of it. The only boundary is the agent boundary — SportMind
reasons, your application acts. Everything beyond that is yours to define.

**Custom actions are not just permitted — they are the point.**

The pattern for any custom action is the same:

```python
# Custom application layer — the pattern for any action

# 1. Get SportMind intelligence
signal = sportmind.get_signal(sport, home, away, competition, kickoff)

# 2. Your application decides what to do with it
if signal["recommended_action"] == "ENTER" and signal["sms"] >= 70:
    your_app.do_whatever_makes_sense_for_your_use_case(signal)

# "whatever makes sense" could be:
#   - Send a push notification to your users
#   - Update a database record
#   - Publish to a social feed
#   - Trigger a webhook to a partner system
#   - Generate a PDF report
#   - Mint an NFT commemorating the match
#   - Update a game state
#   - Anything else
```

**Combining domains:** Every interesting application combines domains.

```
Fan token signal     +    Commercial brief    =    Investor intelligence platform
Pre-match signal     +    Governance alert    =    Full-service token dashboard
Scouting output      +    Transfer brief      =    End-to-end transfer platform
Narrative signal     +    Brand alert         =    Sponsorship timing tool
Broadcast value      +    Rights calendar     =    Media planning tool
Wearable data        +    Pre-match brief     =    Club performance dashboard
```

**Who builds these:**

```
Developers          Build the integration and application logic
Commercial teams    Define what the outputs need to say
Clubs               Specify their operational requirements
Brands              Define their commercial intelligence needs
Platform builders   Assemble multiple actions into products
```

SportMind provides one layer. You own the rest.

---

## What to build — a starting framework

If you're not sure where to start, ask three questions:

```
1. Who receives the output?
   Fan token holder → Domain 1 (fan token actions)
   Commercial/brand → Domain 2 (commercial actions)
   DeFi/prediction  → Domain 3 (market actions)
   Club/analyst     → Domain 4 (operational actions)
   Developer/platform → Domain 5 (platform actions)

2. What do they do with it?
   Read/understand → generate a brief or report
   Decide          → surface a ranked signal or recommendation
   Act immediately → trigger an alert or execution

3. What SportMind signal drives it?
   Match outcome   → adjusted_score, SMS, direction
   Supply/token    → LTUI, CDI, PATH_2 status, MRS
   Commercial      → ABS, APS, BVS, TVS, DQI
   Operational     → ARI, LQI, TMAS, SIB, OTP
   Governance      → GSI, CHI, archetype distribution
```

---

## Where to go next

| Next step | Resource |
|---|---|
| Build the intelligence layer | `examples/agent-types/README.md` |
| Full application blueprints | `examples/applications/README.md` |
| Integration with FanTokenIntel | `examples/fan-token-intel/integration-fan-token-intel.md` |
| Integration with SportFi Kit | `examples/applications/app-07-sportfi-kit-integration.md` |
| Integration with Chiliz Agent Kit | `platform/chiliz-agent-kit-integration.md` |
| System prompts for your agent | `agent-prompts/agent-prompts.md` |
| MCP server configuration | `platform/sportmind-mcp-suite.md` |

---

*SportMind v3.77.0 · MIT License · sportmind.dev*
*See also: examples/agent-types/README.md · examples/applications/README.md*
*platform/integration-partners.md · platform/chiliz-agent-kit-integration.md*
