---
name: global-regulatory-landscape
description: >
  Enduring framework mapping the global cryptoasset regulatory landscape
  by jurisdiction. Covers authorisation requirements, classification
  approaches, and demand signal implications for fan tokens across major
  markets. Uses a four-tier jurisdiction classification system. Load
  alongside jurisdiction-specific regulatory files.
---

# Global Cryptoasset Regulatory Landscape

**Enduring framework. Jurisdiction tier map and multi-gate signal logic.**

> Library Rule: Tier classifications and structural approaches only.
> Specific application deadlines, current enforcement actions, and
> firm-specific compliance status are perishable — SMI briefings only.

---

## Four-tier jurisdiction classification

```
TIER 1 — ACTIVE COMPREHENSIVE FRAMEWORK (binary gate applies):

  European Union
    Framework: MiCA (Markets in Crypto-Assets Regulation)
    Administrator: ESMA + national competent authorities
    Fan token classification: utility tokens, in scope
    Key mechanic: authorisation required for trading platforms
    See: macro/regulatory/eu-mica.md

  United Kingdom
    Framework: FSMA (Cryptoassets) Regulations 2026
    Administrator: Financial Conduct Authority (FCA)
    Fan token classification: qualifying cryptoassets, A&D regime applies
    Key mechanic: binary authorisation gate, white paper disclosure
    See: macro/regulatory/uk-cryptoasset-regime.md

  Japan
    Framework: Payment Services Act (PSA) + Financial Instruments and
    Exchange Act (FIEA) — most mature APAC framework
    Administrator: Financial Services Agency (FSA)
    Fan token classification: cryptoasset exchange services regulated;
    FIEA amendment (2026) moves toward financial instrument classification
    Key mechanic: licensed exchange required, strict AML/CFT obligations
    Socios relevance: Japan is a significant Socios user market

  Singapore
    Framework: Payment Services Act — MAS licensing
    Administrator: Monetary Authority of Singapore (MAS)
    Fan token classification: digital payment tokens, licensing required
    Key mechanic: innovation-friendly but mandatory licensing for exchanges
    Socios relevance: regional hub, MAS-licensed platforms only

TIER 2 — PARTIAL OR DEVELOPING FRAMEWORK (monitor, gate developing):

  Hong Kong
    Framework: SFC licensing regime + Stablecoin Ordinance (2025)
    Fan token classification: virtual assets, exchange licensing required
    Key mechanic: two-track approach (institutional + retail separation)
    Status: active licensing regime, enforcement developing

  South Korea
    Framework: Virtual Asset User Protection Act (active)
    Digital Asset Basic Act: under consideration
    Fan token classification: virtual assets, exchange registration required
    Key mechanic: strict user protection rules, active enforcement

  Brazil
    Framework: Banco Central do Brasil (BCB) authorisation regime
    Fan token classification: virtual assets, VASP licensing required
    Key mechanic: AML/CFT + capital requirements for licensed VASPs
    Socios relevance: large football fan base, growing crypto adoption

  Australia
    Framework: Capital gains tax framework exists; no comprehensive
    crypto regime yet — consultation ongoing
    Status: regulatory framework expected to develop 2026-2027
    Monitor: ASIC for any fan token-specific developments

TIER 3 — RESTRICTIVE OR MINIMAL (demand signal materially impaired):

  India
    Framework: Partial oversight — exchange registration required
    but no broad regulatory regime
    Tax: 30% on crypto gains — suppresses retail demand materially
    Fan token signal: impaired by tax burden and regulatory uncertainty

  China
    Framework: Ban on most cryptoasset activity since 2021
    Exception: Hong Kong operates as regulatory sandbox (see Tier 2)
    Fan token signal: mainland China demand effectively zero

TIER 4 — NOT YET IN SCOPE (no active framework, low Socios presence):
  Most of Africa, Southeast Asia (ex-Singapore), Central Asia
  Monitor via SMI for any Socios partnership or new regulatory framework
```

---

## Multi-jurisdiction signal framework

```
AGENT RULE — MULTI-JURISDICTION REASONING:

  STEP 1: Identify which jurisdictions are material to the fan token signal
    Where are the primary token holders and traders located?

  STEP 2: Check Tier classification for each material jurisdiction
    Tier 1: apply binary authorisation gate before applying signal
    Tier 2: note developing framework, flag uncertainty
    Tier 3: apply demand suppressor — restricted or tax-impaired market
    Tier 4: treat as unregulated, no framework signal

  STEP 3: Apply gates independently per jurisdiction
    Never conflate EU MiCA status with UK FCA status
    Never conflate Singapore MAS status with Japan FSA status
    Each jurisdiction is a separate gate

  STEP 4: Sum adjusted signals across jurisdictions
    UK gate CLOSED + EU gate OPEN ≠ full demand signal
    Each closed gate suppresses the demand from that market only
    Gate closure always takes precedence over CHZ macro regime modifier

  MACRO INTERACTION:
    CHZ CAPITULATION regime (×0.70) applies globally.
    Example: UK gate OPEN + CAPITULATION ×0.70 = UK signal at ×0.70
    Example: UK gate CLOSED + CAPITULATION ×0.70 = UK signal suppressed
    Gate closure always takes precedence over regime modifier.
```

---

## International standard-setting bodies

```
BODIES WHOSE STANDARDS SHAPE NATIONAL FRAMEWORKS:

  FATF (Financial Action Task Force)
    Travel Rule: VASPs must share originator/beneficiary information
    for crypto transfers — applies globally to compliant VASPs
    Relevance: fan token platforms must comply or face de-banking risk
    Non-compliance = structural infrastructure risk, not demand signal

  FSB (Financial Stability Board)
    Global regulatory framework for crypto-asset activities (2023)
    Adopted as baseline by G20 jurisdictions
    Not a regulator — standard-setter only

  BIS / Basel Committee
    Capital requirements for banks holding cryptoassets (active Jan 2025)
    Group 2 assets (most cryptoassets including fan tokens): 1,250% risk weight
    Limits bank custody and balance sheet exposure to fan tokens
    Structural friction on institutional fan token custody globally

  IOSCO
    Crypto and digital asset policy recommendations
    Influences securities regulators globally on token classification

  AGENT RULE:
    FATF Travel Rule compliance is a prerequisite for compliant
    fan token platform operation globally.
    BIS capital rules create structural friction on institutional
    fan token custody — not a demand signal, a supply-side constraint.
```

---

## Tier upgrade monitoring

```
TIER UPGRADE SIGNALS — flag to Strategy & Brainstorm:

  A jurisdiction moves Tier 2 → Tier 1 when:
    A comprehensive authorisation framework is enacted (not just proposed)
    The framework explicitly covers cryptoasset trading platforms
    Enforcement begins (not just consultation)

  A jurisdiction moves Tier 3 → Tier 2 when:
    A formal regulatory framework or licensing regime is proposed
    Tax treatment is materially reformed (e.g. India reducing 30% rate)

  AGENT RULE:
    Tier upgrades are library events — bring to Strategy & Brainstorm
    for scoping before updating any library file.
    Do not update Tier classification based on SMI briefing alone —
    confirmation from official regulatory source required.
```

---

## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Global regulatory map: four-tier jurisdiction classification |
| Reasoning | ACTIVE | Multi-jurisdiction gate reasoning, four-step framework |
| Context | ACTIVE | Jurisdiction-specific regulatory context per tier |
| Memory | ACTIVE | Tier classification and gate mechanics per jurisdiction |
| Judgment | ACTIVE | Tier 1 binary gate vs Tier 2 uncertainty vs Tier 3 suppressor |
| Attention | ACTIVE | Multi-jurisdiction signals require parallel independent gate checks |
| Communication | ACTIVE | Output always states: jurisdiction, tier, gate status |
| Verification | ACTIVE | Official regulator source required before Tier upgrade |
| Learning | ACTIVE | Tier classifications update as frameworks mature |
| Integration | ACTIVE | Integrates with all jurisdiction-specific regulatory files |
| Calibration | EMERGING | Global calibration developing as regimes enter enforcement |
| Adaptation | ACTIVE | Tier 2 jurisdictions may move to Tier 1 — monitor via SMI |
| Ethics | ACTIVE | Never assume compliance — always verify via official register |
| Transparency | ACTIVE | Always state: tier, gate status, jurisdiction source |

---

## Compatibility

**UK regime:** `macro/regulatory/uk-cryptoasset-regime.md`
**EU MiCA:** `macro/regulatory/eu-mica.md`
**US framework:** `macro/macro-regulatory-sportfi.md`
**CHZ macro regime:** `macro/macro-crypto-market-cycles.md`
**Fan token registry:** `fan-token/registry/complete-registry.md`

---

*SportMind v4.1.1 · MIT License · sportmind.dev*
*Enduring framework — global cryptoasset regulatory landscape.*
*All 14 Mind dimensions mapped.*
