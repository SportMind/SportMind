---
name: transfer-intelligence
description: >
  Full-spectrum transfer intelligence skill covering the entire lifecycle of a football
  transfer: rumour detection, valuation, fan sentiment, contract mechanics, fee structure
  analysis, loan spells, release clauses, and post-transfer impact on club and athlete.
  Use this skill whenever the user asks about any aspect of player transfers — rumours,
  valuations, fee breakdowns, contract length, whether a deal makes financial sense, how
  a transfer affects a club's squad or finances, what a loan spell means for development,
  or how a completed transfer has changed an athlete's trajectory. Also trigger for
  questions about transfer windows, free agents, contract expiry, buy-back clauses,
  sell-on clauses, or any "should we sign [player]" type queries. More comprehensive than
  transfer-signal (which focuses narrowly on fan token impact) — this skill covers the
  full football business and athlete development picture. Feeds brand-score and
  performance-on-pitch.
---

# Transfer Intelligence

Full-lifecycle transfer analysis — from the first rumour to post-signing impact
assessment. Covers football business, athlete development, and fan ecosystem angles.

## What this skill produces

- **Transfer Viability Score (TVS)** — Does this deal make sense for club AND athlete? (0–100)
- **Market Valuation Report** — Independent value estimate vs. reported fee
- **Contract Risk Assessment** — Length, wages, clauses, sell-on, release clauses
- **Loan Spell Analysis** — Development value of a loan; return readiness scoring
- **Fan Sentiment Delta** — How transfers shift supporter sentiment and token ecosystems
- **Post-Transfer Trajectory** — 6-month and 12-month impact forecast for athlete
- **Rumour Intelligence Brief** — Source credibility, confidence scoring, timeline

---

## Data sources

### Transfer market data
- **Transfermarkt** (unofficial API): `https://transfermarkt-api.fly.dev`
  - `/players/{id}/market-value` — valuation history
  - `/players/{id}/transfers` — full transfer history
  - `/players/{id}/profile` — age, nationality, contract expiry
  - `/clubs/{id}/players` — squad roster for destination club assessment
- **API-Football** via RapidAPI: `https://api-football-v1.p.rapidapi.com/v3`
  - `/transfers?player={id}` — confirmed transfer records
  - `/players?id={id}&season={year}` — performance context
- **CIES Football Observatory** (public reports): squad value benchmarks
- **Capology.com** (public): wage estimates by league and tier

### News & rumour feeds
- RSS: BBC Sport, Sky Sports, Marca, L'Équipe, Gazzetta, Kicker, Record
- Twitter/X monitored accounts: see `references/journalist-source-tiers.md`
- Reddit: r/soccer, r/transfers, club-specific subreddits

### Contract intelligence
- **Swiss Ramble** (public analysis): club financial deep-dives
- **Deloitte Football Money League** (annual): club revenue context
- **UEFA Financial Reports** (public): FFP compliance context

---

## Workflow

### Step 1 — Resolve athlete and transfer context
1. Accept: athlete name + optional (current club / destination club / loan detail)
2. Resolve to Transfermarkt player ID
3. Fetch: age, nationality, position, contract expiry, current market value
4. Identify whether this is: rumoured transfer / completed transfer / loan / contract extension / free agent

### Step 2 — Market Valuation
```
Estimated fair value = (
  current_transfermarkt_value * 0.40 +    # market consensus
  age_curve_adjustment * 0.20 +           # peak = 24–27, discount above 28
  performance_tier_multiplier * 0.25 +    # from performance-on-pitch if available
  scarcity_premium * 0.15                 # position shortage in target league
)
```

Age curve multipliers:
- U21: × 1.15 (upside premium)
- 21–24: × 1.10 (ascending)
- 24–27: × 1.00 (peak, no adjustment)
- 27–29: × 0.90 (slight discount)
- 30–31: × 0.75
- 32+: × 0.55 or lower

Fee vs. value classification:
- Fee < 80% of estimated value: Excellent deal for buying club
- Fee 80–110%: Fair market deal
- Fee 110–130%: Premium — justified if scarcity or tournament-year uplift
- Fee > 130%: Overpay risk — flag and explain

### Step 3 — Contract Risk Assessment
Parse available contract intelligence:
```
contract_risk_score = (
  contract_length_years * 0.25 +         # longer = higher commitment risk
  wage_vs_league_median * 0.30 +         # wage inflation risk
  release_clause_protection * 0.20 +     # no clause = vulnerability
  sell_on_pct_obligation * 0.15 +        # limits future sale value
  buy_back_clause_risk * 0.10            # ex-club can reclaim
)
```

Flags to surface:
- Contract expiry < 12 months → free agent risk, negotiate now or sell
- Release clause present → exposure to rivals triggering at inopportune moment
- Wage > 2× league median for position → squad wage structure risk
- Sell-on clause > 20% → significantly limits club's future profit

### Step 4 — Loan Spell Analysis (if applicable)
Loans are a distinct transfer type requiring separate logic:

**Loan purpose classification:**
```
"development_loan"    → young player (U23) moving to lower league for minutes
"recovery_loan"       → injured/out-of-form player needing regular play
"financial_loan"      → club clearing wages; player not in plans
"pathway_loan"        → club relationship building ahead of permanent deal
"emergency_loan"      → January window squad crisis cover
```

**Development loan value score:**
```
DLVS = (
  minutes_likely_per_week / 90 * 0.35 +         # will they actually play?
  league_tier_delta * 0.25 +                     # appropriate challenge level?
  position_specificity_match * 0.20 +            # playing their actual position?
  coaching_quality_at_destination * 0.20         # will they be developed properly?
) * 100
```

**Return readiness forecast:**
After loan, estimate probability player returns to parent club first team:
```
return_readiness = DLVS * performance_trajectory_at_loan_club * age_factor
```
- DLVS > 70 + strong stats at loan club → High readiness (>70% return probability)
- DLVS 50–70 → Medium — depends on parent club circumstances
- DLVS < 50 → Low — likely permanent sale or further loan

### Step 5 — Rumour Intelligence (if pre-transfer)
See `transfer-signal` skill for token-focused rumour scoring.
This skill adds:
- **Timeline estimation**: based on window timing and source patterns, when might this resolve?
- **Competing clubs detection**: are multiple clubs linked? Drives up fee.
- **Club motivation analysis**: why does the selling club want to sell? (financial, tactical, squad harmony)
- **Athlete motivation signals**: public comments, agent activity, social hints

### Step 6 — Fan Sentiment Delta
Cross-reference with `fan-token-pulse` if available:
- Incoming: will this signing energise the token holder community?
- Outgoing: is there significant fan resistance (sell pressure risk)?
- Loan return: is there fan appetite for this player returning?

### Step 7 — Post-Transfer Trajectory Forecast
For completed transfers, forecast:
- **6-month outlook**: settling-in period, tactical fit, expected role
- **12-month outlook**: full integration, performance trajectory, contract value change
- **Risk factors**: injury history, style fit with manager, language/cultural adaptation

### Step 8 — Format output

```
TRANSFER INTELLIGENCE — [ATHLETE NAME]
Movement: [CLUB A] → [CLUB B]  |  Type: [Permanent / Loan / Free]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Transfer Viability Score (TVS):    78 / 100  [Strong deal for buying club]

VALUATION
  Transfermarkt value:             €42M
  SportMind estimated fair value:  €45M
  Reported fee:                    €48M
  Assessment:                      Slight premium (107%) — justifiable given
                                   position scarcity in destination league

CONTRACT
  Contract length:                 4 years
  Estimated weekly wage:           €180K (1.8× La Liga midfield median)
  Release clause:                  €95M (inserted — good protection)
  Sell-on clause:                  None
  Buy-back clause:                 €55M within 2 years (monitor risk)
  Contract risk score:             Medium — wage premium is high but clause
                                   protection mitigates squad value risk

RUMOUR INTELLIGENCE
  Confidence:                      81%  [Tier 1 + Tier 2 corroborated]
  Competing clubs:                 1 (Premier League club also linked)
  Timeline estimate:               5–10 days to resolution
  Athlete motivation:              Strong — social activity consistent with move

FAN SENTIMENT DELTA
  Destination fans (incoming):     84 / 100  [High enthusiasm]
  Source fans (outgoing):          41 / 100  [Resistance — monitor token]

POST-TRANSFER FORECAST
  6-month outlook:   Starting XI likely from week 3. Tactical fit with 4-3-3 high.
  12-month outlook:  Full integration expected. Valuation uplift +15–20% if goals met.
  Key risk:          Previous knee injury (2023) — monitor workload management

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Run performance-on-pitch for statistical validation of valuation
→ Run fan-token-pulse to track post-announcement token response
→ Run brand-score to assess commercial value change post-transfer
```

---

## Transfer window monitoring mode

During January and summer windows:
- Poll rumour feeds every 4 hours for monitored player list
- Alert thresholds: RCS > 65%, Tier 1 source mention, bidirectional token spike
- Daily digest: all monitored athletes sorted by deal likelihood

---

## Reference files

- `references/journalist-source-tiers.md` — Journalist/publication credibility tiers (shared with transfer-signal)
- `references/transfer-fee-benchmarks.md` — Fee benchmarks by position, league, age band
- `references/contract-clause-templates.md` — Common clause types and risk frameworks
- `references/loan-case-studies.md` — Historical loan spell outcomes for DLVS calibration *(planned)*

---

## Environment variables

```
RAPIDAPI_KEY=<key>              # API-Football
X_BEARER_TOKEN=<key>            # Rumour monitoring
REDDIT_CLIENT_ID=<id>
REDDIT_CLIENT_SECRET=<secret>
```
