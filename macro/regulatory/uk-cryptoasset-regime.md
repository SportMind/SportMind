---
name: uk-cryptoasset-regime
description: >
  Enduring framework for the UK's cryptoasset regulatory regime under
  the Financial Services and Markets Act (Cryptoassets) 2026. Covers
  authorisation requirements, admissions and disclosures regime, and
  structural implications for fan token issuers and trading platforms
  serving UK consumers. Load alongside macro/regulatory/eu-mica.md
  and macro/macro-regulatory-sportfi.md.
---

# UK Cryptoasset Regulatory Regime

**Enduring framework. Enacted 2026 under FSMA (Cryptoassets) Regulations.**

> Library Rule: No application window dates, no firm-specific compliance
> status, no enforcement action details. This file teaches agents how to
> reason about the UK regulatory framework — not current compliance status
> of any specific entity.

---

## Framework overview

The UK enacted a comprehensive cryptoasset regulatory regime in 2026
under the Financial Services and Markets Act (Cryptoassets) Regulations
2026. This represents the UK's equivalent to the EU's MiCA framework —
a principles-based authorisation regime covering a defined set of
cryptoasset activities. The regime is administered by the Financial
Conduct Authority (FCA). Firms carrying on regulated cryptoasset
activities in or from the UK must be authorised by the FCA.

---

## Regulated activities

```
REGULATED CRYPTOASSET ACTIVITIES (structural categories):

  · Cryptoasset exchange — buying, selling, exchanging cryptoassets
  · Cryptoasset custody — safeguarding cryptoassets on behalf of clients
  · Operating a cryptoasset trading platform
  · Issuing cryptoassets (public offers)
  · Arranging cryptoasset transactions

FAN TOKEN RELEVANCE:
  Fan tokens offered or traded to UK consumers by platforms fall within
  scope of regulated cryptoasset exchange and trading platform activities.
  Token issuers making public offers to UK consumers fall within the
  admissions and disclosures (A&D) regime.
  Existing AML-only registrations do NOT automatically convert to
  full authorisation — new applications required.
```

---

## Admissions and disclosures regime

```
A&D REGIME — KEY STRUCTURAL MECHANICS:

  Covers: public offers of qualifying cryptoassets and admission of
  cryptoassets to trading on UK qualifying cryptoasset trading platforms.

  DISCLOSURE REQUIREMENTS:
    Issuers making public offers to UK consumers must produce and publish
    a cryptoasset white paper meeting FCA standards.
    White paper must cover: token mechanics, issuer details, rights
    attached to the token, risks, and redemption/exit mechanisms.

  FAN TOKEN IMPLICATION:
    Fan tokens offered to UK consumers via Socios/Chiliz or any UK
    platform are subject to disclosure requirements. This creates a
    structural documentation burden that did not previously exist.
    Agents should treat UK fan token offerings as carrying A&D
    compliance requirements — not purely consumer protection only.

  AGENT RULE:
    When reasoning about fan token demand signals involving UK consumers,
    always check whether the issuer/platform is operating under the UK
    A&D regime. Non-compliant public offers = restricted UK demand signal.
```

---

## Authorisation framework

```
AUTHORISATION MECHANICS:

  WHO NEEDS AUTHORISATION:
    Any firm carrying on regulated cryptoasset activities in or from the UK.
    This includes: exchanges, custodians, trading platforms, issuers of
    qualifying cryptoassets to UK consumers.

  EXISTING REGISTRATIONS:
    Prior AML/CTF-only registrations do not confer authorisation.
    Prior FSMA authorisations and Payment Services Regulations
    authorisations do not convert automatically.
    Separate FCA application required in all cases.

  TRANSITIONAL PROVISIONS:
    A savings window exists for firms already operating — application
    during this window allows continued operation pending FCA decision.
    Window timing and deadlines: PERISHABLE — do not encode here.
    Check FCA register and SMI briefing for current status.

  UNAUTHORISED ACTIVITY:
    Firms operating without authorisation after the transitional period
    commit a criminal offence. Hard enforcement boundary, not a guideline.

  AGENT RULE:
    Never assume a fan token platform or issuer is UK-authorised.
    Verify via FCA register before treating UK demand signal as fully active.
    If platform is not authorised: UK demand signal is materially impaired.
    This is a binary gate — authorised or not, no middle ground.
```

---

## Fan token demand signal implications

```
DEMAND SIGNAL FRAMEWORK — UK REGIME:

  BINARY GATE (authorisation status):
    Platform/issuer AUTHORISED: UK demand signal applies normally
    Platform/issuer NOT AUTHORISED: UK demand signal suppressed
    Apply this gate before any UK-specific fan token demand reasoning.

  SUPPLY SIGNAL INTERACTION:
    A&D white paper disclosure requirement is an enduring structural cost.
    Higher compliance burden creates potential supply-side friction for
    new fan token launches targeting the UK market.
    Does not suppress existing token demand — applies to new issuances.

  MACRO INTERACTION:
    UK authorisation regime operates independently of EU MiCA.
    A platform can be MiCA-authorised but NOT UK-authorised.
    Do not conflate EU and UK regulatory status.
    Check both independently for dual-jurisdiction fan token signals.

  AGENT RULE:
    UK regulatory status and EU MiCA status are separate gates.
    Both must be verified independently.
    A fan token platform authorised under MiCA is not thereby
    authorised in the UK. Apply the binary gate for each jurisdiction.
```

---

## Comparison with EU MiCA

```
UK REGIME vs EU MiCA:

  SIMILARITIES:
    Both require authorisation for cryptoasset trading platforms
    Both impose white paper / disclosure requirements on issuers
    Both are principles-based with a defined set of regulated activities
    Both create a binary gate: authorised or not

  KEY DIFFERENCES:
    UK regime enacted under FSMA — domestic law, FCA-administered
    MiCA is EU-wide regulation across 27 member states
    UK and EU savings window / grandfathering mechanics differ
    Separate applications required for each jurisdiction

  AGENT RULE:
    Load both files when reasoning about fan tokens with UK + EU exposure.
    Neither regime substitutes for the other.
    See macro/regulatory/eu-mica.md for EU framework.
```

---

## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | UK cryptoasset regime: authorisation, A&D, binary gate |
| Reasoning | ACTIVE | Authorisation gate reasoning before any UK demand signal |
| Context | ACTIVE | UK regulatory context: FSMA 2026, FCA, post-Brexit framework |
| Memory | ACTIVE | UK regime distinct from MiCA — separate jurisdiction, separate gate |
| Judgment | ACTIVE | Binary gate: authorised/not authorised, no middle ground |
| Attention | ACTIVE | UK + EU status must both be verified independently |
| Communication | ACTIVE | Output always states UK authorisation gate status explicitly |
| Verification | ACTIVE | FCA register verification required before UK demand signal |
| Learning | ACTIVE | Regime new (2026) — calibration developing as enforcement begins |
| Integration | ACTIVE | Integrates with eu-mica.md, macro-regulatory-sportfi.md |
| Calibration | EMERGING | First enforcement cycle — outcomes accumulating |
| Adaptation | ACTIVE | Regime will evolve as FCA issues guidance and enforcement decisions |
| Ethics | ACTIVE | Never assume authorisation — always verify via FCA register |
| Transparency | ACTIVE | Always state: UK gate status, verification source, MiCA independence |

---

## Compatibility

**National team demand:** `fan-token/national-team-tokens.md`
**EU MiCA:** `macro/regulatory/eu-mica.md`
**US framework:** `macro/macro-regulatory-sportfi.md`
**Fan token demand signals:** `fan-token/demand-levers.md`
**Global landscape:** `macro/regulatory/global-regulatory-landscape.md`

---

*SportMind v4.1.1 · MIT License · sportmind.dev*
*Enduring framework — UK FCA cryptoasset regime under FSMA 2026.*
*All 14 Mind dimensions mapped.*
