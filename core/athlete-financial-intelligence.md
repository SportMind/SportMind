# Athlete Financial Intelligence

**The financial layer that makes APS calculations accurate.**
An athlete's commercial value and portability cannot be correctly assessed without
understanding their financial structure. This skill extends the commercial brief
stack with wage, contract, image rights, and bonus intelligence.

---

## Why financial intelligence belongs in SportMind

The APS (Athlete Portability Score) in `fan-token/transfer-signal/` uses social
and on-chain engagement data as proxies for commercial portability. These proxies
are good but incomplete. The financial reality directly constrains portability:

```
FINANCIAL CONSTRAINTS ON APS:

High wage gap (player earning 3× target club's wage ceiling):
  APS may read 0.78 (high engagement portability)
  But financial reality: target club cannot match wages = transfer impossible
  True APS after financial adjustment: 0.48 (MODERATE)

Image rights structure:
  Player retains 100% image rights (common in elite football):
  Reduces club's commercial leverage but improves athlete's individual brand
  APS adjustment: +0.05 (player has more portable brand independent of club)
  
  Club controls image rights:
  Limits athlete's individual commercial brand
  APS adjustment: -0.03 (brand more tied to current club)

Bonus structure (performance-linked):
  Agent requests Champions League appearance bonuses:
  Only relevant if target club competes in Europe
  APS adjustment: -0.10 to -0.15 if target club doesn't match competition tier
  
  This is the wage-matching problem expressed differently:
  "I'll earn less and fewer bonuses at this club."
  → Reduces real portability despite headline wage agreement

FINANCIAL APS FORMULA EXTENSION:
  APS_adjusted = APS_base × Wage_Feasibility × Image_Rights_Factor × Contract_Stage

  Where:
    Wage_Feasibility = target_wage_ceiling / player_current_wage (capped at 1.00)
    Image_Rights_Factor = 1.05 (player-controlled) or 0.97 (club-controlled)
    Contract_Stage = expiry year multiplier (see below)
```

---

## Contract stage multipliers

When a contract expires matters enormously for APS and transfer feasibility.

```
CONTRACT STAGE MODEL:

4+ years remaining:
  Transfer requires large fee (max financial commitment from target)
  APS_adjusted × 0.85 — financial barrier is highest
  Unless player explicitly requests transfer or club accepts low fee

2-3 years remaining:
  Standard transfer window. Fee is substantial but not prohibitive.
  APS_adjusted × 1.00 — no multiplier (baseline)

1 year remaining:
  Leverage window opens. Clubs must sell or lose on free.
  APS_adjusted × 1.15 — financial barrier reduced; both clubs motivated
  Agent strategy: use leverage for pre-contract talks

< 6 months remaining (pre-contract eligible):
  Player can sign pre-contract with new club from January (football)
  APS_adjusted × 1.25 — maximum financial portability
  Fee = zero. Only loyalty bonus and image rights to negotiate.

Contract expired (free agent):
  APS_adjusted × 1.30 — maximum portability
  Financial barrier = zero. Agent controls timeline entirely.
  
AGENT RULE: Always check contract expiry date before APS calculation.
  Contract expiry is the single most reliable financial portability signal.
```

---

## Wage intelligence framework

```
WAGE TIER STRUCTURE (football benchmark, 2025-2026):

Elite Tier (€300k+/week):
  Clubs: Manchester City, PSG, Real Madrid, Barcelona, Bayern Munich
  Maximum APS target: another Elite Tier club only
  Wage_Feasibility for mid-tier target: 0.35-0.55 (severe constraint)
  
Top Tier (€150-300k/week):
  Clubs: Top-6 Premier League, top-3 Serie A/La Liga/Bundesliga
  Maximum APS target: Elite or Top Tier clubs
  Wage_Feasibility for mid-tier target: 0.60-0.75 (significant constraint)
  
Mid Tier (€60-150k/week):
  Clubs: Europa League-level clubs
  Portable to: Top Tier with wage uplift ambition; lateral Mid Tier moves
  Wage_Feasibility: 0.80-1.00 for most targets (manageable)
  
Lower Tier (< €60k/week):
  Most leagues and most players
  Highly portable financially — APS_adjusted ≈ APS_base
  
MONITORING SIGNALS FOR WAGE INTELLIGENCE:
  Published contracts (Italy Serie A publishes wages publicly)
  Contract disputes in media (indirectly reveals wage tier)
  Transfer fee relative to reported wage cap of buying club
  Agent statements: "We need a club that can match his level" = financial constraint
```

---

## Image rights intelligence

```
IMAGE RIGHTS — THE HIDDEN APS VARIABLE:

Standard arrangement (most clubs retain majority):
  Club uses player's image for commercial purposes
  Player receives fixed fee or small percentage
  APS impact: neutral (standard expectation priced into transfers)

Player-controlled image rights (elite/agent-driven):
  Player (or player's company) retains image rights
  Club licenses from player for specific activations
  
  Commercial implications:
  + Player can run independent sponsorships (own Instagram, YouTube, etc.)
  + Player's brand is more portable (doesn't depend on club's commercial relationships)
  - Club has less leverage to mandate commercial commitments
  - More complex to negotiate token/digital asset terms
  
  APS impact: +0.05 (brand more independent of current club)
  
  Examples of player-controlled image rights structures:
  Common among elite players with strong individual brands
  Often negotiated by agents during contract renewals at ages 24-27
  
  AGENT RULE: If a player's individual social following is > 50% of their
  club's following, they likely have significant image rights leverage.
  This is a positive APS signal.

Token-native image rights:
  Emerging: some player contracts now include clauses for digital/token activations
  A player with explicit token/digital asset clauses in their contract:
  → Highest APS for fan token purposes
  → Contractual commitment to token engagement
  Apply APS bonus: +0.08 to +0.12

MONITORING:
  Contract disputes sometimes reveal image rights structure
  Player launching independent brand products = strong image rights signal
  Player-branded apps, NFT collections = full image rights confirmed
```

---

## Bonus and incentive structure intelligence

```
PERFORMANCE BONUS SIGNALS:

UCL appearance bonuses:
  Common in elite contracts: €5-20k per UCL appearance
  Implication for APS: reduces portability to non-European clubs
  Target club must offer equivalent or player accepts earnings reduction
  
  AGENT RULE: Elite players with UCL appearance bonuses → APS_adjusted
  reduced by 0.10-0.15 for target clubs not in UCL

Goals/assists bonuses:
  High goal bonus (attacking players): positional-role dependent
  High assist bonus (creative players): assists are harder to guarantee
  
  Signal: Very high goal bonus = player is motivated primarily by on-pitch performance
  Positive for PI trajectory but neutral for commercial portability

Loyalty bonuses:
  Paid to player if they remain at club past a certain date
  Incentive to delay any transfer
  APS temporary suppression: if loyalty bonus date < 3 months away,
  club is likely to delay transfer until after payment
  
  MONITORING: Loyalty bonus payment windows often precede transfer windows
  by 2-3 months. Watch for agents delaying talks until bonus is secured.

Relegation release clauses:
  Common in Premier League / promoted club contracts
  Player can leave at reduced fee if club is relegated
  APS spike: +0.20 to +0.30 if relegation looks likely
  
  This is the most reliable short-term APS signal available.
  A quality player at a relegating club with a release clause =
  maximum transfer market efficiency.
```

---

## Financial intelligence in governance and scouting

```
GOVERNANCE VOTES (app-08):
  Before recommending a signing vote:
  1. Assess player wage tier vs club wage ceiling
  2. Check contract expiry for fee estimation
  3. Identify any image rights structure signals
  4. Run financial APS adjustment
  
  Governance brief should state:
  "APS_base: 0.76. APS_adjusted (financial): 0.64 — wage constraint identified.
   Target club wage ceiling estimated at 70% of player's current earnings."

TALENT SCOUTING (app-09):
  Add to scout report Section 4 (Transfer Assessment):
  Financial feasibility assessment alongside TVS and TSI
  Contract expiry = most important financial signal for timing
  
  Priority hierarchy for scouting timing:
  1. Contract < 6 months: approach now (pre-contract eligible)
  2. Contract 1 year: approach now (leverage window open)
  3. Contract 2-3 years: approach summer window (standard)
  4. Contract 4+ years: only if club signals willingness to sell
```

---

## Financial intelligence data sources

```
PUBLIC SOURCES (available without API):
  Capology.com: estimated wages for major European leagues
  Spotrac.com: North American sports contract database (NFL, NBA, MLB, NHL)
  Transfermarkt.com: market values and transfer fee history
  Italian Serie A: publishes official wage data annually (most transparent league)
  
  RELIABILITY:
  Official published data (Serie A): HIGH reliability
  Capology/Spotrac estimates: MEDIUM reliability (based on transfer fees and leaked data)
  Agent/media reports: LOW reliability (often inflated for negotiation)
  
INFERENCE SIGNALS (when direct data is unavailable):
  Transfer fee paid / player's age = crude wage estimate ratio
  Signing club's wage bill (from annual accounts) / squad size = average ceiling
  Agent's public statements about "ambition level" = financial constraint signal
  
AGENT RULE: When financial data is unavailable, apply Tier 2 uncertainty.
  State: "Financial structure unconfirmed — APS_adjusted estimated at base × 0.90."
  Never fabricate wage figures. State confidence level explicitly.
```

---

## Financial signal flags

```
NEW FLAGS (added by this skill):

wage_constraint:
  Activated when: target club wage ceiling < 75% of player's current wage
  Effect: APS_adjusted reduction; reduce transfer_feasibility recommendation

pre_contract_window:
  Activated when: contract expiry < 6 months
  Effect: APS_adjusted ×1.25; high-priority transfer signal

loyalty_bonus_pending:
  Activated when: loyalty bonus payment date < 3 months
  Effect: APS temporarily suppressed; transfer likely to be delayed

release_clause_active:
  Activated when: relegation/performance clause met or near met
  Effect: APS spike +0.20 to +0.30; high-priority transfer signal
  
image_rights_player_controlled:
  Activated when: evidence of player-controlled image rights
  Effect: APS_base +0.05; stronger individual commercial brand signal
```

---

## Agent reasoning integration

```
WHEN FINANCIAL INTELLIGENCE APPLIES:

Always apply for:
  APS calculations (financial layer is required for accuracy)
  Governance signing votes (fee feasibility is part of the brief)
  Talent scouting reports (Section 4: Transfer Assessment)
  Transfer window monitoring workflow (Pattern 4)

Optional for:
  Pre-match signal analysis (financial layer rarely affects game outcome)
  Portfolio intelligence (unless a transfer is driving the token movement)

INTEGRATION WITH EXISTING METRICS:
  APS: apply financial adjustment formula above
  TVS (Transfer Viability Score): financial layer improves accuracy
  LTUI: financial sustainability of signing affects LTUI projection
  
SEQUENCE:
  1. Load APS base from fan-token/transfer-signal/
  2. Load financial intelligence (this skill)
  3. Apply adjustments: Wage_Feasibility × Image_Rights_Factor × Contract_Stage
  4. Output: APS_adjusted with financial_confidence note
```

---

## Compatibility

**APS foundation:** `fan-token/transfer-signal/` — base APS calculation
**Transfer intelligence:** `fan-token/transfer-intelligence/` — TVS and DLVS
**Commercial brief:** `fan-token/brand-score/` — ABS synthesis
**Governance app:** `examples/applications/app-08-governance-intelligence.md`
**Talent scouting app:** `examples/applications/app-09-talent-scouting.md`
**Temporal awareness:** `core/temporal-awareness.md` — contract data is Tier 1 (months)

*MIT License · SportMind · sportmind.dev*
