CHANGELOG.md — PREPEND PATCH — v4.1.22
======================================
INSTRUCTION: Insert the block below immediately after the `# Changelog`
header line and before the existing `## [4.1.5]` entry.
Do not modify any existing content below that point.
======================================

## [4.1.22] — 2026-07-22

### Changed
- CHANGELOG.md: Added 16 missing entries covering v4.1.6 through v4.1.21
  (full WC2026 build period and GitHub documentation audit Pass 1).
  Closes Pass 1 of the GitHub documentation audit. All root-level files
  now audited and current.

---

## [4.1.21] — 2026-07-22

### Changed
- SECURITY.md: Skill hash count (273) generalised to "all skill files"
  in two occurrences to avoid future staleness. Duplicate Changelog
  section removed (first incomplete instance with single 3.5.0 entry).
  Calibration provenance note added — clarifies JSON block is internal
  validation schema; community submissions use markdown via GitHub Issues
  and community/calibration-data/TEMPLATE.md. Trust tier table corrected:
  "Expert/Senior on leaderboard" → "established contribution history".
  Changelog entry added for v4.1.21.

---

## [4.1.20] — 2026-07-22

### Changed
- OVERVIEW.md: Opening description updated to canonical SportMind framing.
  Key Numbers corrected: 762 files, 542 markdown, 137 calibration records.
  96% accuracy claim removed — replaced with verifiable WC2026 record
  (9/9, 100%, perfect). 21 sports calibrated removed (unverifiable).
  Calibration section updated: 137 records, WC2026 9/9 100% perfect.
  Footer version corrected: v3.97.41 → v4.1.19. SMI description updated
  to reflect Claude-native implementation. Direction format note added
  after signal output block. Founding Calibrators: #1 @AltcoinDaddy,
  #2 @charan0318, 8 slots remaining noted in use cases and contribute
  sections.

---

## [4.1.19] — 2026-07-22

### Changed
- QUICKSTART.md: Example output version updated: 3.40.0 → 4.1.18.
  Direction format note added after example output — clarifies
  LONG/SHORT/DRAW for fan token vs HOME/AWAY/DRAW for sport intelligence,
  with link to FIRST-RECORD-GUIDE.md. Agent prompt count removed from
  "Where to go next" table ("19 agent prompts" → "all agent prompts").

---

## [4.1.18] — 2026-07-22

### Changed
- MCP-SERVER.md: Health check version updated: 3.30.0 → 4.1.17.
  Malformed version strings removed from two section headers
  (v3.97.66.0.0.0.0.0.0.0.0.0 — build artefact). "The ten tools" →
  "Core tools" with note clarifying five/five split between core and
  additional tools. sportmind_pre_match added to tool sequencing as
  recommended primary tool for all pre-match analysis. Fan token registry
  count corrected: 84 → 85 verified tokens. Model string updated:
  claude-sonnet-4-20250514 → claude-sonnet-4-6. sportmind_agent_status
  pointer added to examples/agentic-workflows/.

---

## [4.1.17] — 2026-07-22

### Changed
- FIRST-RECORD-CHALLENGE.md: Calibration count updated to 137. Founding
  Calibrators noted inline: #1 @AltcoinDaddy, #2 @charan0318, 8 remaining.
  Step 2 rewritten with Option A (any LLM) and Option B (MCP server) paths.
  Direction terminology updated: LONG/SHORT/DRAW for fan token records,
  HOME/AWAY/DRAW for sport intelligence. SMS → SportMind Score. JSON template
  replaced with reference to community/calibration-data/TEMPLATE.md. File
  path corrected: {year}/{month}/ removed, .json → .md. Basketball removed
  (no confirmed active Chiliz fan token). Modifier table counts replaced
  with "why valuable" column. WHO-WE-ARE.md reference removed. Fan token
  verification guidance added (black logo signal). High-value record types
  table added.
- community/CONTRIBUTORS.md: Founding Calibrators named table added at top:
  #1 @AltcoinDaddy, #2 @charan0318, slots 3-10 open. Basketball removed
  from priorities. Modifier counts removed. JSON/path references corrected
  to TEMPLATE.md and .md format. Sport priorities rewritten with fan token
  framing: $UFC and $PFL noted as confirmed active Chiliz partners. Footer
  link corrected to FIRST-RECORD-CHALLENGE.md.

---

## [4.1.16] — 2026-07-21

### Changed
- CONTRIBUTING-GAPS.md: Six-Month Test added to Library Rule section for
  consistency with CONTRIBUTING.md. LAYER_GAP type annotated with five
  SportMind layers (fan-token · athlete · macro · market · sports).

---

## [4.1.15] — 2026-07-21

### Changed
- CONTRIBUTING.md: MIND DIMENSIONS added as required section in skill quality
  standards (Completeness criterion), self-review checklist, and review
  process criterion 1. New section added: "How to contribute a calibration
  record" — two record types, high-value targets (dual fan token football,
  MMA $UFC/$PFL), GitHub Issue process, links to TEMPLATE.md and
  FIRST-RECORD-GUIDE.md. Removed non-existent infrastructure: GitHub Action
  JSON validation, leaderboard points, {year}/{month}/ calibration path,
  community/calibration-data/README.md link, automated merge thresholds,
  community modifier voting, skill registry metadata block, Translations and
  Platform/tooling subsections. Tier A calibration list corrected: basketball,
  MotoGP, cricket removed (no confirmed active Chiliz fan tokens). Co-maintainer
  section simplified. Recognition updated with Founding Calibrators reference.
  Section heading case normalised.

---

## [4.1.14] — 2026-07-21

### Changed
- WHO-USES-THIS.md: Calibration counts updated: 126 → 137 (Researcher section)
  and 100 → 137 with Founding Calibrator note (Contributor section). MMA added
  to "what we need most" section: $UFC and $PFL are confirmed active Chiliz fan
  token partners — any UFC/PFL main event qualifies as a fan token calibration
  record. MCP server user path added to decision tree and quick reference card.

---

## [4.1.13] — 2026-07-21

### Added
- FIRST-RECORD-GUIDE.md: Full rewrite. Two-path Step 1: Option A (any LLM,
  zero setup via quickstart prompt) and Option B (MCP server via Claude Desktop).
  Fan token validity rules explicit: active/inactive distinction, black logo
  signal, multi-source verification. Record types distinguished: fan token
  record vs sport intelligence layer record. Suggested matches updated: dual
  fan token football, MMA ($UFC/$PFL both confirmed active Chiliz partners),
  single fan token, sport intelligence layer. Historical WC2026 fixtures removed.
  Founding Calibrators expanded to 10 slots (#1 @AltcoinDaddy, #2 @charan0318,
  8 open). Inline record template with full field set.
- community/calibration-data/TEMPLATE.md: New contributor-facing calibration
  record template. Full field set: Event, Competition, Venue, Date, Fan Token
  Status with verification source, Record Type, LLM/Path used, Pre-Match Signal
  with modifiers and key signals, Result, Root Cause Note. Not a library skill
  file — no MIND DIMENSIONS section.

---

## [4.1.12] — 2026-07-20

### Added
- fan-token/burn-to-glory-framework.md: Treasury size variation agent rule added.
  Identical burn % produces materially different absolute amounts across tokens
  due to varying initial treasury sizes. Agent rule: use burn % as the comparable
  metric — never compare absolute amounts across different tokens. Newer tokens
  (recent FTO) typically carry larger treasuries, producing larger absolute burns
  at the same %. Correct method: % of remaining supply as the structural supply
  signal.
- macro/macro-regulatory-sportfi.md: GENIUS Act (enacted 2025) US payment
  stablecoin framework added. Scope: payment stablecoins only. Fan tokens NOT
  in scope — classified as digital collectibles/tools under SEC/CFTC March 2026
  guidance. Effective 2027. Macro context: INSTITUTIONAL_LEGITIMACY signal
  LOW-MEDIUM weight. Agent rule: do not conflate stablecoin regulation with fan
  token regulation. CLARITY Act remains primary pending US legislation for fan tokens.

---

## [4.1.11] — 2026-07-17

### Added
- fan-token/use-cases.md: Champion Call pre-match demand amplifier mechanic added.
  Balance snapshot model, proportional entry, holding requirement, live conviction
  display, winner-linked outcome. Classified as structured buying pressure, not
  organic demand. FM1/FM4/FM8 agent rules. Post-match holding pressure liquidity
  modifier added.
- macro/regulatory/uk-cryptoasset-regime.md: Five-policy-statement architecture
  confirmed (June 30 2026). MARC: market abuse regime for cryptoassets — insider
  trading now explicitly covered under UK law for the first time. Criminal liability
  from Q4 2027. Six regulated activity categories documented. International firms:
  branch model available for MiCA-authorised entities. Consumer Duty applies.

---

## [4.1.10] — 2026-07-16

### Added
- macro/regulatory/global-regulatory-landscape.md: Japan FIEA Amendment enacted
  July 15 2026. Crypto reclassified from payment instruments to financial products
  under FIEA — same category as stocks and bonds. Insider trading restrictions.
  Annual disclosure obligations. 2M JPY retail cap on high-risk tokens. Tokyo
  Stock Exchange ETF pathway open. Tax 55% → 20% flat rate effective January 2028.
  Stablecoins excluded. Framework takes effect fiscal 2027. Fan token agent rule:
  Japan is now a securities-law jurisdiction for crypto from fiscal 2027.
  South Korea National Asset Basic Act announced July 14 2026. Virtual assets to
  be classified as national assets alongside land and IP. 2027 CBDC pilot. Token
  securities rules February 2027. Monitor FSC for fan token specific guidance.

---

## [4.1.9] — 2026-07-16

### Added
- fan-token/defi-integration-intelligence.md: Omnichain bridge event behaviour
  pattern added (Tier 1 confirmed). Bidirectional cross-chain movement confirmed
  during major tournament result windows. Purpose: price discovery and liquidity
  alignment across Solana and Chiliz Chain. Trigger conditions: KO result
  confirmation and Final anticipation window. Three agent rules: infrastructure
  signal not demand signal (FM7), no spot demand conflation, bidirectional — no
  net flow assumption.

---

## [4.1.8] — 2026-07-14

### Added
- macro/fan-adoption-intelligence.md: Three-tier fan demand segmentation framework
  (Active Holders / Aware Non-Holders / Unaware). Cross-market digital engagement
  expectations. US sports league international fan base structural gap analysis.
  APAC player-centric fandom FM1 modifier. All 14 Mind Dimensions mapped.
- macro/partnerships.md: Three Chiliz Chain wallet architecture models: Socios
  custodial, standard self-custody, MPC (keyless, no seed phrase, multi-region
  confirmed). FanTokens.com two-layer intelligence architecture: SportMind
  frameworks (Layer 1) + professional market analysis tooling (Layer 2). KayenFi
  identified as Chiliz-native Fan Token DEX with name-longevity encoding.

### Changed
- platform/ai-agent-economy.md: Two-layer intelligence architecture section added.
  FM1 agent rule cross-referenced. Compatibility updated.
- fan-token/defi-integration-intelligence.md: KayenFi identified as Chiliz-native
  Fan Token DEX. Name-change note added for structural longevity.
- fan-token/registry/complete-registry.md: $PEPPER entry updated with KayenFi
  official name alongside existing Kayen DEX reference.
- fan-token/use-cases.md: Livestream trading battle confirmed as structural fan
  engagement pattern for fan token KO matches. Four consecutive WC2026 activations.
  Dual-layer mechanic: BTG on-chain (Layer 1) + trading battle off-chain (Layer 2).
  Classified as SENTIMENT AMPLIFIER. FM4 and FM1 agent rules applied during KO window.

---

## [4.1.7] — 2026-07-13

### Added
- macro/chz-tokenomics.md: Dragon8 dynamic supply model documented. Pre-2024 fixed
  supply (8.8B CHZ) marked as historical — superseded May 2024 via on-chain governance.
  Dynamic issuance: no hard cap, minted per block, 1.88% annual inflation floor after
  ~14 years. Two concurrent deflationary mechanisms: EIP-1559 transaction fee burn +
  CHZ buy-back burn (10% Fan Token revenues). PoSA consensus: Main validators /
  Candidate validators / Delegators. On-chain governance via governance.chilizchain.com.
  Four agent rules: supply model, concurrent processes, governance sensitivity, data
  freshness. Agent rule: do NOT use 8.8B as current supply — historical only.
  All 14 Mind Dimensions mapped.

---

## [4.1.6] — 2026-07-11

### Changed
- Website: Version stamps updated to v4.1.6 across homepage and first-record page.
- index.html: File count updated to 760. Calibration count updated to 134.
- scripts/sportmind_mcp.py: SPAIN, BELG, SFA, SAFA added to FAN_TOKEN_REGISTRY
  with verified contract addresses and BTG data. ARG and POR updated with burn
  counts. ITA non-qualification note added. SNFT BiTCI partnership deprecated.
  CEX perp futures flag added to 9 LBank-confirmed tokens: PSG, BAR, ATM, JUV,
  CITY, AFC, GAL, ARG, POR. VERSION string updated to 4.1.5.

---

