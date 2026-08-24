# Fan Token Holder Tax Framework

**Domain:** fan-token/holder-tax-framework.md
**Version:** v4.6.31
**Library Rule:** Six-Month Test PASSES · Proper Noun Test PASSES
**Scope:** Cross-jurisdictional fan token holder tax framework. Fills
Priority 3 coverage gap — holder jurisdiction tax regime as a structural
demand modifier. All token lists verified against SportMind fan token
registry.

---

## Critical Distinction — Holder vs Issuer Jurisdiction

```
AGENT RULE 1 — HOLDER JURISDICTION GOVERNS:
  The tax regime that matters for demand behaviour is the jurisdiction
  where the TOKEN HOLDER is resident — NOT where the fan token was
  issued or where the club is based.

  A Japanese holder of $INTER faces Japanese tax law.
  An Italian holder of $INTER faces Italian tax law.
  The token is the same. The demand behaviour is different.

  Never apply the club's home country tax framework to holders.
  Never assume all holders of a token face the same tax treatment.

AGENT RULE 2 — PRIMARY HOLDER MARKET DETERMINES MODIFIER:
  For each fan token, identify the primary holder market jurisdiction(s).
  Apply the relevant tax regime modifier to that demand layer.
  Secondary holder markets apply secondary modifiers.
  Global aggregate: weighted average of primary market modifiers.
```

---

## Four Tax Regime Types

| Type | Description | Holding period relief | Friction level |
|---|---|---|---|
| A | Zero CGT after minimum holding period | YES — 0% after threshold | VERY LOW (long-term) |
| B | Progressive income tax on all crypto gains | NO | VERY HIGH |
| C | Flat CGT rate on all disposals | NO | MODERATE-HIGH |
| D | Progressive CGT with rate tiers | Partial (annual allowance) | MODERATE |

---

## Eight Primary Holder Market Profiles

### Germany — Type A

```
TAX REGIME: Type A — Zero CGT after 12-month holding period
  Short-term (under 12 months): taxed as miscellaneous income
  Long-term (12 months+): 0% — zero capital gains tax
  This is the most favourable crypto tax regime globally among
  major fan token holder markets.

DEMAND MODIFIER: STRONG LONG HOLD BIAS
  German holders have a structural incentive to hold fan tokens
  for at least 12 months before disposal. This creates:
  · Reduced short-term trading pressure from German holders
  · Increased long-term holder conviction signal
  · Lower velocity in German holder market
  · Exit pressure suppressed until 12-month threshold crossed

DOMESTIC TOKEN STATUS:
  No domestic German club currently has an active Chiliz fan
  token in the SportMind registry.
  Germany is a significant HOLDER MARKET for foreign club tokens.
  Tokens with large German fan bases include:
    $BAR (FC Barcelona) · $JUV (Juventus) · $ATM (Atletico Madrid)
  Do not create a "German tokens" category — apply German tax
  modifier to the German holder population of foreign club tokens.

AGENT RULE 3 — GERMAN LONG HOLD BIAS:
  Apply LONG HOLD BIAS modifier to German holders of any active
  fan token. Reduced short-term selling pressure from German
  holders vs equivalent populations in Type B or C jurisdictions.
  At 12-month threshold: potential exit pressure from those who
  accumulated specifically to qualify for 0% rate.
```

---

### Japan — Type B

```
TAX REGIME: Type B — Progressive income tax on all gains
  Crypto gains classified as "miscellaneous income"
  Tax rate: 5–45% (national) + 10% (local) = up to 55% combined
  No holding period relief — short and long-term gains taxed equally
  Annual loss carry-forward: NOT permitted for miscellaneous income
  Note: Japan FIEA enacted July 15 2026 — crypto reclassified as
    financial products from fiscal 2027. Tax treatment may evolve.
    Monitor FSA for updated guidance under FIEA.

DEMAND MODIFIER: VERY HIGH FRICTION · REDUCED SHORT-TERM TRADING
  At 55% effective rate, active trading is heavily penalised.
  Japanese holder demand is likely biased toward:
  · Strategic long-term holding without disposal
  · Fan token holding as fan engagement, not financial activity
  · Reduced trading volume from Japanese retail holders
  The FIEA reclassification may reduce rates (analogous to equity
  tax rates) — monitor for framework update by fiscal 2027.

TOKENS WITH SIGNIFICANT JAPANESE HOLDER BASES:
  $INTER · $ACM · $JUV · $PSG
  Japanese football fandom is historically strongest for Italian
  and European club football — these are the primary tokens
  where Japanese holder tax friction applies as a modifier.

HP-2 SIGNAL — SBI × TOKYO VERDY:
  If confirmed and launched: first Japanese-issued fan token.
  Primary domestic holder market = Japan (Type B).
  VERY HIGH friction applies from launch as a standing modifier.
  Update this file if HP-2 confirms.

AGENT RULE 4 — JAPAN HIGH FRICTION:
  Apply REDUCED SHORT-TERM TRADING modifier to Japanese holder
  population of $INTER, $ACM, $JUV, $PSG. 55% effective rate
  makes disposal costly — Japanese holders skew toward fan
  engagement holding, not speculative trading.
```

---

### United Kingdom — Type D

```
TAX REGIME: Type D — Progressive CGT with annual allowance
  CGT rates: 10% (basic rate taxpayer) / 18% (higher rate)
  Annual CGT allowance: £3,000 (2024/25 onwards — reduced from £6,000)
  Crypto classified as a capital asset — CGT on disposal
  MARC awareness: UK Market Abuse Regulation for Cryptoassets
    active from Q4 2027. Fan token activity by UK residents on
    UK-regulated platforms will be subject to market abuse rules.
    See: macro/regulatory/uk-cryptoasset-regime.md

DEMAND MODIFIER: MODERATE FRICTION + MARC AWARENESS
  10-18% CGT is materially lower than Japan (55%) or France (30%)
  for higher-rate taxpayers. UK holders face moderate friction.
  Annual allowance of £3,000 allows small gains tax-free.
  MARC (from Q4 2027): insider trading rules apply — UK-based
  holders with non-public information face criminal liability.

REGISTRY-CONFIRMED UK CLUB TOKENS:
  $AFC (Arsenal) — largest English fan token · only confirmed
    FTP PATH_2 token — primary UK domestic fan token market
  $SPURS (Tottenham Hotspur)
  $CITY (Manchester City)
  $CPFC (Crystal Palace)
  $AVL (Aston Villa) — TRANSITION gate ACTIVE · CDI horizon SHORT
  $EFC (Everton)
  $LUFC (Leeds United)

AGENT RULE 5 — UK MODERATE FRICTION + MARC:
  Apply MODERATE FRICTION modifier to UK holder population.
  $AFC is the dominant UK domestic fan token — apply MARC
  awareness to $AFC UK holder analysis from Q4 2027.
  Annual allowance (£3,000) creates a small tax-free exit window —
  monitor for year-end selling pressure from UK holders.
```

---

### France — Type C

```
TAX REGIME: Type C — Flat CGT rate (PFU — Prélèvement Forfaitaire Unique)
  Flat tax rate: 30% on all crypto gains (12.8% income tax + 17.2% social charges)
  No holding period relief — 30% applies regardless of holding duration
  No annual allowance equivalent

DEMAND MODIFIER: MODERATE-HIGH FRICTION · NO HOLDING PERIOD INCENTIVE
  Unlike Germany (Type A), there is no incentive for French holders
  to hold beyond any specific duration — 30% applies regardless.
  This creates a more uniform trading pattern with no spike at
  any holding period threshold.
  30% flat rate is lower than Japan but higher than UK (lower band).

REGISTRY-CONFIRMED FRENCH CLUB TOKENS:
  $PSG (Paris Saint-Germain) — primary domestic French market
  Note: $PSG is the largest European club fan token by market cap
    and has the largest concentration of French domestic holders
    of any fan token in the registry.

AGENT RULE 6 — FRANCE FLAT FRICTION:
  Apply MODERATE-HIGH FRICTION modifier to French holder population.
  $PSG French holder demand: 30% flat on all disposals — no
  temporal structure to holding incentives. French holders of $PSG
  do not have a German-style 12-month threshold to optimise around.
```

---

### Spain — Type D

```
TAX REGIME: Type D — Progressive CGT (Impuesto sobre la Renta)
  CGT rates:
    Up to €6,000 gains: 19%
    €6,000 to €50,000 gains: 21%
    €50,000 to €200,000 gains: 23%
    Over €200,000 gains: 28%
  Hacienda enforcement: active and increasing for crypto assets
  No holding period relief — all gains taxed at above rates

DEMAND MODIFIER: MODERATE FRICTION · PROGRESSIVE STRUCTURE
  Progressive rates mean high-value disposals face 28% effective
  rate — similar to UK higher rate but without the UK annual allowance.
  Hacienda's active crypto enforcement creates compliance-driven
  behaviour modification among Spanish holders.

REGISTRY-CONFIRMED SPANISH CLUB TOKENS:
  $BAR (FC Barcelona) — largest Spanish domestic fan token ·
    also significant German and international holder markets
  $ATM (Atletico Madrid)
  $SEVILLA (Sevilla FC)
  $RSO (Real Sociedad)
  $LEV (Levante UD) — CONFIRMED SPANISH CLUB · not German
  $VCF (Valencia CF)

AGENT RULE 7 — SPAIN PROGRESSIVE FRICTION:
  Apply MODERATE FRICTION modifier to Spanish holder population.
  $BAR is the primary token: large Spanish domestic holder market
  with additional significant German (Type A) holder population.
  Apply split modifier when reasoning about $BAR aggregate demand:
  Spanish holders (Type D) + German holders (Type A) = composite.
```

---

### United States — Type D

```
TAX REGIME: Type D — Progressive CGT with short/long-term binary split
  Short-term (under 12 months): taxed as ordinary income — up to 37%
    federal rate at top bracket. HIGH FRICTION for active traders.
  Long-term (12 months+): 0%, 15%, or 20% depending on income bracket.
    CONDITIONAL LONG HOLD BIAS — 12-month threshold creates structurally
    similar holding behaviour to Germany (Type A) but with a rate floor
    rather than zero CGT.
  FBAR/FATCA: reporting obligations for offshore crypto holdings add
    compliance overhead and friction for US holders.
  SEC uncertainty: fan tokens face unresolved securities classification
    risk in US jurisdiction — applies as a demand suppressor independent
    of CGT rate. Escalate immediately on any SEC fan token mention.
  No domestic US sports team fan tokens currently in registry.
  US is a HOLDER MARKET for foreign club tokens.
  HP-7: US College tokens confirmed launched August 2026 (5 initial
    tokens · SEC and Big Ten conferences) — mechanic TBC. Do NOT
    encode as PTG-equivalent until mechanic confirmed. Monitor only.

DEMAND MODIFIER: CONDITIONAL LONG HOLD BIAS + SEC UNCERTAINTY SUPPRESSOR
  US holders face a structural 12-month holding incentive (long-term
  rates 0-20% vs short-term up to 37%). This creates similar temporal
  holding pressure to German Type A holders — but with a meaningful
  rate floor rather than zero CGT.
  The SEC uncertainty suppressor operates independently of CGT —
  applies to all US holder demand analysis regardless of holding period.
  Combined effect: patient long-term US holders are incentivised to hold
  12+ months, but SEC overhang suppresses aggregate US holder demand
  vs equivalent populations in resolved jurisdictions.

TOKENS WITH US HOLDER BASES (primary):
  $PSG · $BAR · $JUV · $INTER · $ACM · $CITY
  (highest-profile European clubs with confirmed US fan bases)
  $UFC · $PFL — MMA-ORG tier · primary US-domestic tokens in registry
  $ROUSH (NASCAR) — US domestic holder market
  HP-7 college tokens — incoming · do not model demand until mechanic
  confirmed · do not update fan-token-play.md yet

AGENT RULE 11 — US CONDITIONAL LONG HOLD BIAS + SEC SUPPRESSOR:
  Apply CONDITIONAL LONG HOLD BIAS to US holders after 12 months.
  Apply SEC UNCERTAINTY SUPPRESSOR to all US holder demand analysis —
  independent of CGT rate.
  Escalate IMMEDIATELY on any SEC mention of fan tokens or Socios.com.
  Do not apply any demand modifier for HP-7 college tokens until
  mechanic is confirmed via Tier 1 source.
  FBAR/FATCA compliance overhead: treat as friction modifier for
  US holders with offshore exchange exposure.
```

---

### Belgium — Type A

```
TAX REGIME: Type A — Zero CGT under normal management standard
  Framework: SPF Finances income classification
  Normal management (bon père de famille): 0% — zero CGT
    No hard holding period threshold — behaviour standard governs
    Long-term infrequent holding reinforces 0% classification
  Speculative income: 33% + communal surcharge (~50% effective)
  Professional income: Progressive income tax up to 50%
  Unlike Germany (§23 EStG 12-month threshold), Belgium has no
    single trigger date — incentive is continuous and
    behaviour-driven throughout the holding period
  Enacted: confirmed via SPF Finances guidance · longstanding
    Belgian tax doctrine · no enacted legislation as of library date

DEMAND MODIFIER: BELGIUM BEHAVIOUR BIAS
  Long-term Belgian holders face 0% CGT — positive demand signal.
  Active traders face classification risk — 33-50% friction layer.
  No 12-month exit pressure spike — no threshold clustering effect.
  Net effect: positive demand signal for long-term holders ·
  friction signal for active traders.

DOMESTIC TOKEN STATUS:
  $BELG (Belgian national team) — ACTIVE · Chiliz Chain ·
    primary domestic Belgian market · EURO 2028 co-host PTG active
  No Jupiler Pro League club tokens in registry.
  Belgium is a holder market for foreign club tokens and $BELG.
  Do not create a Belgian club tokens category.

AGENT RULE 12 — BELGIUM BEHAVIOUR BIAS:
  Apply BEHAVIOUR BIAS modifier to Belgian holders of any active
  fan token. Long-term infrequent holders: 0% CGT — positive
  demand signal. Active traders: classification risk — 33% or
  50% effective rate. $BELG is the primary domestic Belgian token.
  No Jupiler Pro League tokens in registry — Belgium is a holder
  market only. No time-threshold model — behaviour standard governs.
```

### Pakistan — Type CONDITIONAL (HP-13 binary outcome pending)

```
TAX REGIME: Type CONDITIONAL — PVARA ACCESS GATE (binary) + 15% CGT + ADOPTION AMPLIFIER
  Framework: Virtual Assets Act 2026 · PVARA · FBR
  HP-13 ACTIVE — September 5 2026 NOC deadline · binary outcome pending
  Socios.com / Chiliz NOC status: NOT CONFIRMED

THREE-SIGNAL STRUCTURE (assess separately, never net):
  SIGNAL 1 — PVARA ACCESS GATE (binary · dominant):
    REGISTERED: Access PASS · adoption amplifier activates
    NOT REGISTERED: PLATFORM ACCESS SUPPRESSOR — dominant signal
    Current state: UNRESOLVED · apply UNRESOLVED modifier

  SIGNAL 2 — CGT MODIFIER (friction):
    15% flat on profits exceeding PKR 500,000 · 6+ months
    Budget 2026-27 proposes 20-30% — UNRESOLVED upward pressure
    PTG burn tax treatment: UNKNOWN
    Current modifier: MODERATE FRICTION · Type C-adjacent

  SIGNAL 3 — ADOPTION SCALE AMPLIFIER (conditional):
    40M+ crypto users · #3 globally (Chainalysis 2025)
    $300B+ annual transaction volume
    ACTIVATES only if PVARA ACCESS GATE = REGISTERED
    Current state: CONDITIONAL — do not apply until gate confirmed

DOMESTIC TOKEN STATUS:
  NONE — no Pakistani club or national team tokens on Chiliz Chain.
  Pakistan is a holder market only. Do not model a Pakistani national
  team token without verified Chiliz partnership confirmation.

AGENT RULE 13 — PAKISTAN CONDITIONAL:
  Apply UNRESOLVED modifier until September 5 2026 HP-13 resolution.
  Gate resolves to PLATFORM ACCESS SUPPRESSOR (dominant) or
  CONDITIONAL DEMAND AMPLIFIER (40M+ users). Never net the three
  signals. CGT at 15% MODERATE FRICTION until FBR Budget 2026-27
  confirmation. See macro/regulatory/pakistan.md for full framework.
```

### South Africa — Reference Only

```
DETAILED COVERAGE: macro/regulatory/south-africa-sars.md (v4.1.42)
  See that file for full SARS framework, CARF, VDP, ITR12 4522.

PRIMARY TOKEN: $SAFA (South African Football Association)
  WC2026: 1 PTG burn confirmed · eliminated Round of 32

KEY MODIFIERS (summary):
  · SARS CGT max effective rate: 18% for individuals
  · CARF active from 2 March 2026 — offshore reporting live
  · VDP closing window — compliance-driven selling pressure modifier
  · ITR12 source code 4522: enforcement infrastructure live now
  · TFM4 T-30 active August 1 2026

AGENT RULE 8: see macro/regulatory/south-africa-sars.md
  for full $SAFA holder tax intelligence.
```

---

## Additional Jurisdictions

### Brazil — Reference Only

```
DETAILED COVERAGE: macro/regulatory/brazil.md (v4.1.78)
  See that file for full Receita Federal framework, CGT rates,
  MP 1.303/2025 ratification status, and PTG burn treatment.

PRIMARY TOKENS: 9 Brazilian club tokens
  $MENGO (Flamengo) · $VERDAO (Palmeiras) · $FLU (Fluminense)
  $SCCP (Corinthians) · $SPFC (São Paulo) · $BAHIA (EC Bahia)
  $GALO (Atletico Mineiro) · $SACI (SC Internacional) · $VASCO (Vasco da Gama)

KEY MODIFIERS (summary):
  · 17.5% effective CGT rate (MP 1.303/2025 — subject to ratification)
  · INVERTED CALENDAR: season March-December · peak demand NOW (August)
  · PTG burn treatment: UNRESOLVED
  · Ratification risk: lapse or amendment = immediate library update required

AGENT RULE 9 (BRAZIL): see macro/regulatory/brazil.md for full framework.
  Daily scan: congress.leg.br · escalate if MP lapses or is amended.
```

---

### Turkey — Reference Only

```
DETAILED COVERAGE: macro/regulatory/turkey.md (v4.1.79)
  See that file for full SPK licensing framework, TCMB payment ban,
  CGT status, and MASAK AML obligations.

PRIMARY TOKENS: 6 Chiliz Chain Turkish club tokens
  $GAL (Galatasaray) · $TRA (Trabzonspor) · $ALA (Alanyaspor)
  $IBFK (Istanbul Basaksehir) · $GOZ (Göztepe) · $SAM (Samsunspor)

KEY MODIFIERS (summary):
  · CGT: UNKNOWN — no enacted framework as of library date · monitor
  · TCMB payment ban: active — Turkish holders investment/speculation only
  · SPK licensing: CASP licence required — verify before holder analysis
  · Turkish-German diaspora: LONG HOLD BIAS via German Type A holders ($GAL primary)

NOTE: $BJK (Besiktas) — on Ethereum, NOT Chiliz Chain.
  Do not include $BJK in Chiliz Chain Turkish token analysis.

AGENT RULE 9 (TURKEY): see macro/regulatory/turkey.md for full framework.
  Monitor: Turkish CGT — escalate immediately on any enacted legislation.
```

---

## Cross-Jurisdiction Demand Modifier Summary

| Jurisdiction | Regime | Friction | Key tokens | Standing modifier |
|---|---|---|---|---|
| Germany | Type A (0% CGT after 12m) | VERY LOW (long-term) | $BAR $JUV $ATM (holder market) | LONG HOLD BIAS |
| Japan | Type B (up to 55%) | VERY HIGH | $INTER $ACM $JUV $PSG | REDUCED SHORT-TERM TRADING |
| UK | Type D (10-18% CGT) | MODERATE | $AFC $SPURS $CITY $CPFC $AVL $EFC $LUFC | MODERATE FRICTION + MARC |
| France | Type C (30% flat) | MODERATE-HIGH | $PSG | MODERATE-HIGH · NO HOLDING INCENTIVE |
| Spain | Type D (19-28% progressive) | MODERATE | $BAR $ATM $SEVILLA $RSO $LEV $VCF | PROGRESSIVE FRICTION |
| USA | Type D (up to 37% short / 0-20% long) | MODERATE-HIGH (short) / MODERATE (long) | $PSG $BAR $JUV $INTER $ACM $CITY $UFC $PFL $ROUSH | CONDITIONAL LONG HOLD BIAS + SEC SUPPRESSOR |
| Belgium | Type A (0% CGT — normal management) | LOW (long-term) | $BELG | BEHAVIOUR BIAS |
| South Africa | Type D (18% max CGT) | MODERATE | $SAFA | see south-africa-sars.md |
| Brazil | Type C — 17.5% CGT (MP 1.303 — ratification pending) | MODERATE (subject to ratification) | $MENGO $VERDAO $FLU $SCCP $SPFC $BAHIA $GALO $SACI $VASCO | see macro/regulatory/brazil.md |
| Turkey | UNKNOWN CGT · TCMB payment ban active | UNKNOWN friction · investment/speculation only | $GAL $TRA $ALA $IBFK $GOZ $SAM | see macro/regulatory/turkey.md |
| Pakistan | CONDITIONAL (HP-13 binary outcome pending) | UNRESOLVED (HP-13) | $PSG $BAR $GAL $INTER (holder market — no domestic tokens) | September 5 2026 |

---

## 13 Agent Rules

```
RULE 1 — HOLDER JURISDICTION GOVERNS:
  Apply the holder's jurisdiction tax framework, not the issuer's.
  Never apply club home country tax to holder population.

RULE 2 — PRIMARY HOLDER MARKET DETERMINES MODIFIER:
  Identify primary holder market before applying any tax modifier.
  Multi-market tokens ($BAR, $PSG, $JUV) require composite modifiers.

RULE 3 — GERMAN LONG HOLD BIAS:
  0% CGT after 12 months. Apply LONG HOLD BIAS to German holders.
  No domestic German club tokens in registry — Germany is a holder
  market for foreign club tokens.

RULE 4 — JAPAN HIGH FRICTION:
  55% effective rate. Apply REDUCED SHORT-TERM TRADING modifier.
  FIEA reclassification may reduce — monitor fiscal 2027.

RULE 5 — UK MODERATE FRICTION + MARC:
  10-18% CGT + MARC awareness from Q4 2027. $AFC is primary.
  Annual £3,000 allowance creates a small tax-free exit window.

RULE 6 — FRANCE FLAT FRICTION:
  30% flat PFU. No temporal holding incentive. $PSG primary.

RULE 7 — SPAIN PROGRESSIVE FRICTION:
  19-28% progressive. $BAR and $ATM primary tokens. Hacienda active.
  $BAR requires composite: Spanish (Type D) + German (Type A) modifier.

RULE 8 — SOUTH AFRICA:
  See macro/regulatory/south-africa-sars.md for full framework.

RULE 9 — BRAZIL AND TURKEY:
  Brazil: apply 17.5% CGT modifier (MP 1.303/2025 — subject to ratification).
  Escalate immediately if MP lapses or is amended — modifier reverts to UNKNOWN.
  Turkey: CGT UNKNOWN — apply UNKNOWN friction modifier until legislation enacted.
  TCMB payment ban active for all Turkish holders — investment/speculation only.
  Both: see respective macro/regulatory/ files for full frameworks.

RULE 10 — COMPLIANCE-DRIVEN SELLING IS TYPE 3 STRUCTURAL:
  If a jurisdiction confirms material enforcement increase (SARS,
  Hacienda, Receita Federal), classify as Type 3 Structural signal.
  Applies as a demand-suppressing modifier for that jurisdiction's
  holder population. Not Type 5 operational — enduring structural shift.

RULE 11 — USA CONDITIONAL LONG HOLD BIAS + SEC SUPPRESSOR:
  12-month threshold creates LONG HOLD BIAS for patient US holders.
  SEC uncertainty applies as demand suppressor independent of CGT.
  Escalate immediately on any SEC fan token or Socios.com mention.
  HP-7 mechanic unconfirmed — no demand modifier applicable yet.

RULE 12 — BELGIUM BEHAVIOUR BIAS:
  Apply BEHAVIOUR BIAS modifier to Belgian holders of any active
  fan token. 0% CGT contingent on normal management classification
  — no hard holding period threshold. Long-term infrequent holders:
  positive demand signal. Active traders: classification risk —
  33% (speculative) or 50% (professional) effective rate.
  $BELG is the primary domestic Belgian token. No Jupiler Pro
  League tokens in registry. Never apply a time-threshold model
  to Belgian holder analysis — behaviour standard governs.
  See macro/regulatory/belgium.md for full framework.

RULE 13 — PAKISTAN CONDITIONAL:
  Apply UNRESOLVED modifier to all Pakistani holder analysis until
  September 5 2026 HP-13 outcome confirmed. Binary gate outcome:
  REGISTERED = CONDITIONAL DEMAND AMPLIFIER (40M+ users · #3
  global adoption) activates. NOT REGISTERED = PLATFORM ACCESS
  SUPPRESSOR (dominant signal — overrides all other modifiers).
  Never net the three signals (ACCESS GATE + CGT MODIFIER +
  ADOPTION AMPLIFIER). CGT: 15% MODERATE FRICTION current ·
  Budget 2026-27 proposes 20-30% (UNRESOLVED). PTG burn tax:
  UNKNOWN. No domestic Pakistani tokens — holder market only.
  See macro/regulatory/pakistan.md for full framework.
```

---

## MIND DIMENSIONS

| Dimension | Status | Notes |
|---|---|---|
| Intelligence (1) | ACTIVE | Holder tax regimes as structural demand intelligence |
| Reasoning (2) | ACTIVE | Causal reasoning: tax regime → holder behaviour → demand modifier |
| Context (3) | ACTIVE | Jurisdictional context as demand signal layer |
| Memory (4) | ACTIVE | Tax regime types, holding period thresholds, token market mappings |
| Judgment (5) | ACTIVE | Composite modifier weighting for multi-market tokens ($BAR, $PSG) |
| Attention (6) | ACTIVE | 12-month threshold flags (Germany), MARC activation (UK Q4 2027) |
| Communication (7) | ACTIVE | Modifier notation and regime type labelling |
| Verification (8) | ACTIVE | Registry verification of token-to-country mappings |
| Learning (9) | ACTIVE | Tax rate changes update this file — calibration feedback loop |
| Integration (10) | ACTIVE | Cross-layer: holder tax + CDI + macro regime = composite signal |
| Calibration (11) | ACTIVE | Modifier values to be calibrated via verified calibration records |
| Adaptation (12) | ACTIVE | FIEA reclassification (Japan 2027), MARC (UK Q4 2027) — file must update |
| Ethics (13) | ACTIVE | No tax advice framing — this is a demand modifier framework |
| Transparency (14) | ACTIVE | Unknown modifiers (Brazil, Turkey) explicitly stated |
| Execution (15) | ACTIVE | Composite modifier calculation for multi-market tokens |
| Collaboration (16) | ACTIVE | Cross-file coordination with belgium.md Rule 12 · pakistan.md Rule 13 · germany.md · france.md · multi-market token composite modifiers |

---

## COMPATIBILITY

- fan-token/registry/complete-registry.md — source of truth for all token-to-country mappings
- intelligence/country-scan/usa.md — US regulatory and holder market context
- macro/regulatory/belgium.md — Belgium detailed coverage · Rule 12
- macro/regulatory/pakistan.md — Pakistan detailed coverage · Rule 13 · HP-13 binary outcome
- macro/regulatory/south-africa-sars.md — South Africa detailed coverage
- macro/regulatory/eu-mica.md — EU regulatory context for European holder markets
- macro/regulatory/france.md — France detailed coverage · $PSG holder tax framework
- macro/regulatory/germany.md — Germany detailed coverage · Type A · diaspora hub · LONG HOLD BIAS
- macro/regulatory/uk-cryptoasset-regime.md — MARC context for UK holder analysis
- macro/global-regulatory-landscape.md — four-jurisdiction overview
- fan-token/fan-holder-behaviour.md — holder behaviour framework
- core/signal-classification-framework.md — compliance enforcement = Type 3 Structural

© 2026 SportMind
