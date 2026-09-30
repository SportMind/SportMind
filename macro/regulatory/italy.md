---
name: macro-regulatory-italy
file: macro/regulatory/italy.md
tier: A — 30-day verification cycle
last-verified: 2026-09-28
next-check-due: 2026-10-28
status: CURRENT
agent-rule: >
  File re-verified within required cycle. No material change found on any
  of the four open flags (CONSOB fan token classification, PTG burn tax
  treatment, staking/airdrop treatment, 33% CGT rate stability). Apply
  content with normal confidence. Verify key dates and rates against
  primary sources for live analysis.
---

# Italy — Crypto Regulatory Framework for Fan Token Holder Analysis

**Domain:** macro/regulatory/italy.md
**Version:** v4.6.85
**Library Rule:** Six-Month Test PASSES · Proper Noun Test PASSES
**Scope:** Italian domestic holder tax and regulatory framework. Law
199/2025 effective January 1 2026 (33% CGT rate). DAC8 automatic
exchange reporting active from 2026. MiCA fully operational.
Resolves UNKNOWN modifier for Italian domestic holders of $ITA ·
$ACM · $INTER · $JUV · $NAP.
**Jurisdiction:** Italy (Italian Republic)
**Regulatory authority:** Agenzia delle Entrate (Revenue Agency) ·
CONSOB (Commissione Nazionale per le Società e la Borsa) · Bank of Italy
**Framework status:** ACTIVE — Law 199/2025 effective January 1 2026
**Last verified:** 2026-09-28

---

## Legislative History

```
ITALIAN CRYPTO TAX FRAMEWORK — EVOLUTION:

Law 197/2022 (2023 Budget Law) — effective January 1 2023:
  First dedicated crypto framework in Italian law.
  CGT rate: 26% substitute tax (imposta sostitutiva).
  Annual threshold: €2,000 (gains below threshold tax-exempt).
  Source: TUIR Article 67(1)(c-sexies).

Law 213/2023 (2024 Budget Law) — effective January 1 2024:
  Framework refinements. 26% rate maintained.
  Regulatory alignment with EU crypto developments.

Law 207/2024 (2025 Budget Law) — effective January 1 2025:
  €2,000 annual exemption threshold ABOLISHED.
  All gains taxable from the first euro.
  26% rate maintained. (An initial proposal floated a 42% rate
  during the 2025 Budget Law's own drafting process, October 2024 —
  this was walked back before enactment; re-confirmed as historical
  context this pass, not a live proposal.)

Law 199/2025 (2026 Budget Law) — effective January 1 2026:
  CGT rate RAISED: 26% → 33%.
  No threshold (threshold already abolished in 2025).
  DAC8 reporting framework activated simultaneously.
  A parliamentary amendment (Lega, Centemero — via the Milleproroghi
  decree) attempted to delay the 33% rate's start to January 1 2027;
  this did not succeed — the 33% rate took effect on schedule January
  1 2026 as Law 199/2025 states, re-confirmed this pass via multiple
  independent Tier 2 tax-advisory sources.

D.Lgs. 194/2025 — effective January 1 2026:
  DAC8 transposition (EU Directive 2023/2226).
  Automatic exchange reporting for all Italian-resident
  crypto holders on MiCA-authorised platforms.

Agenzia delle Entrate measure — June 22 2026:
  DAC8 practical implementation machinery activated (Provvedimento
  del Direttore dell'Agenzia delle Entrate n. 186865).
  First reporting year: 2026.
  First exchange report deadline: June 30 2027.
  First international data exchange: September 30 2027.
  NEW THIS PASS: Agenzia delle Entrate published operational FAQ
  clarifications on July 29 2026, confirming that the scope of
  transactions CASPs/CAOs must report to the tax authority does NOT
  fully coincide with the scope of transactions that are actually
  taxable under TUIR Article 67(1)(c-sexies) — i.e. some reported
  transactions will not themselves generate a tax liability. This is
  a reporting-scope clarification, not a change to what triggers CGT,
  and does not itself resolve the PTG burn question below (a burn-
  for-reward event's reportability and its taxability are separate
  questions; this FAQ addresses the former, not the latter).

DIRECTION OF TRAVEL:
  Rate increased at every legislative revision since 2023, with one
  unsuccessful attempt each to increase it further (42% proposal,
  2025 Budget Law drafting) and to delay the increase (Lega
  amendment, Milleproroghi, targeting the 2026 increase) — both
  reconfirmed as historical/failed this pass, not live proposals.
  Threshold abolished in 2025. No hold period relief has been
  introduced or signalled at any legislative cycle. No 2027 Budget
  Law preview or amendment proposal touching the crypto CGT rate was
  found as of this verification pass (2026-09-28) — the next Budget
  Law cycle (for 2027) had not yet surfaced any crypto-specific
  proposal in Tier 2 coverage at time of check.
  Do not assume rate stability — treat 33% as current floor.
```

---

## Current Tax Framework (effective January 1 2026)

```
CGT RATE: 33% flat substitute tax (imposta sostitutiva)
  Applied to all realised crypto capital gains by Italian residents.
  This is the primary fan token holder demand modifier for Italy.
  RE-CONFIRMED 2026-09-28: still in force, no amendment found.

THRESHOLD: NONE
  All gains taxable from the first euro.
  (€2,000 threshold abolished January 1 2025 — one full year before
  the rate increase.)

COST BASIS METHOD: LIFO (Last In, First Out)
  Mandated by Agenzia delle Entrate.
  The most recently acquired fan tokens are treated as disposed of
  first upon any realisation event.
  This is distinct from FIFO — agents must not assume FIFO applies
  to Italian holders.

TAXABLE EVENTS:
  · Sale of fan token for fiat currency
  · Swap of fan token for another crypto asset
  · Use of fan token to purchase goods or services
  · Gifting of fan tokens

NON-TAXABLE:
  · Transfer between wallets controlled by the same Italian holder
  · Purchase of fan tokens with fiat currency
  · Swaps between crypto-assets with equal characteristics and
    function remain fiscally neutral (re-confirmed this pass,
    per Agenzia delle Entrate Circolare n. 30/E of 2023, still the
    operative guidance as of 2026-09-28) — distinct from the general
    "swap = taxable event" rule above, which applies to swaps between
    crypto-assets of differing character; this neutral-swap carve-out
    is narrow and should not be assumed to apply to a fan-token-for-
    fan-token swap without confirming the assets are of genuinely
    equal characteristics and function

LOSS OFFSETTING:
  Capital losses may offset against gains in the same tax year.
  Unused losses may be carried forward up to 4 years.
  This creates a potential year-end demand pattern — Italian holders
  with embedded losses may realise them before December 31 to offset
  gains elsewhere.

ANNUAL DECLARATION:
  Modello 730 or Redditi PF · deadline October 15 each year.
  Crypto holdings must be declared even if no disposal occurred
  in the tax year. NEW THIS PASS: Agenzia delle Entrate has
  simplified the declaration process for the 2026 filing year,
  introducing new Quadro T and Quadro W sections and permitting
  Modello 730 filers to declare crypto tax obligations without
  needing to also file the supplementary Redditi PF forms — a
  procedural simplification, not a substantive rate or scope change.

WEALTH TAX (IVAFE):
  0.2% annual levy on crypto held outside Italy.
  Applies to: Chiliz Chain wallets · Socios.com holdings.
  Italian residents holding fan tokens on Chiliz Chain owe 0.2%
  annually on the December 31 value.
  This is a background structural cost — not a primary signal driver —
  but relevant for high-value Italian holder analysis.
  RE-CONFIRMED this pass: crypto-assets are now also explicitly
  included in ISEE (Indicatore della Situazione Economica
  Equivalente) household wealth calculations for 2026 — a related but
  distinct disclosure point from IVAFE itself; noted for completeness,
  does not change the IVAFE rate or scope.

EMT CARVE-OUT (DOES NOT APPLY TO FAN TOKENS):
  MiCAR-compliant euro-denominated stablecoins (e.g. EURC) are
  taxed at 26%, not 33%. Fan tokens do not qualify for this
  carve-out — they are utility tokens, not e-money tokens.

SPORTMIND MODIFIER — ITALIAN DOMESTIC HOLDERS:
  ITALY: 33% CGT · no threshold · LIFO · no hold period relief
```

---

## Fan Token Classification under MiCA

```
MiCA CATEGORY: "Other crypto-assets" (residual utility token category)

Fan tokens issued on Chiliz Chain are NOT:
  · Asset-referenced tokens (ARTs)
  · E-money tokens (EMTs)
  · Financial instruments under MiFID II

The 26% EMT carve-out does NOT apply to fan tokens.
The 33% CGT rate applies to all fan token capital gains by Italian
residents from January 1 2026.

ITALY MiCA STATUS:
  Italy's MiCA transitional period expired December 30 2025 for VASPs
  that did not file a CASP authorisation application; those that did
  file by that date could continue operating under review until no
  later than June 30 2026 (re-confirmed this pass via CONSOB's own
  published communications — this transitional mechanic is now fully
  closed out, both deadlines having passed).
  All CASPs offering services to Italian residents must now hold MiCA
  authorisation or have ceased operations.
  CONSOB adopted ESMA crypto-asset classification guidelines in 2026
  (including ESMA's guidelines on assessing knowledge/competence under
  MiCA, adopted per CONSOB's March 2026 newsletter) and continues
  routine enforcement activity against unauthorised crypto-asset
  websites (ongoing website-blocking actions re-confirmed this pass,
  most recently reported in CONSOB's own weekly newsletters through
  2026).
  No fan token-specific classification ruling issued by CONSOB as of
  2026-09-28 (RE-CHECKED this pass — searched CONSOB's own published
  activity and multiple Tier 2 sources specifically for fan-token or
  utility-token classification guidance; found none. This is a
  negative result, not a confirmed absence of any future ruling —
  continue to monitor).
```

---

## PTG Burn Tax Treatment — UNRESOLVED

```
STATUS: UNRESOLVED — no Agenzia delle Entrate guidance issued
as of 2026-09-28 (RE-CHECKED this pass — see Sources and Verification
below for what was actually searched).

A PTG burn event involves a fan token holder transferring tokens
to a burn address in exchange for a platform reward (match ticket,
experience, merchandise, treasury benefit via supply reduction).

Whether this constitutes a disposal under Italian law has not been
clarified by the Agenzia delle Entrate.

TWO POSSIBLE INTERPRETATIONS:

1. DISPOSAL INTERPRETATION:
   Burning tokens = sale for consideration (the reward received).
   CGT applies at 33% on any gain above cost basis.
   Under LIFO, the most recently acquired tokens are disposed of first.

2. NON-DISPOSAL INTERPRETATION:
   Burn for utility reward = consumption of a utility token, not a sale.
   No CGT event — analogous to spending a loyalty point or redeeming
   a voucher. No capital gain crystallised.

WHAT THIS PASS DID CHECK AND DID NOT RESOLVE: general Italian crypto
staking-reward guidance IS well-established (staking/lending rewards
are taxed as "redditi diversi" at the same 33% rate, on receipt, at
fair market value — this is a settled, general rule for proof-of-stake
validation rewards). This is a DIFFERENT fact pattern from a PTG burn
event — staking rewards are new tokens received for validating a
network, whereas a PTG burn is an existing token surrendered in
exchange for a non-monetary reward. The general staking rule does NOT
resolve, and should not be assumed to apply to, the PTG burn question.
No guidance specific to burn-for-reward mechanics was found.

AGENT RULE:
  Do not assume either interpretation applies.
  PTG burn tax treatment in Italy is UNRESOLVED.
  Do NOT apply the general staking-reward rule (33% on receipt) to a
  PTG burn event — these are different fact patterns and conflating
  them would be an unsupported assumption, not a resolution.
  When modelling Italian domestic holder demand for PTG competitions,
  flag this uncertainty explicitly.
  Do not apply the realisation assumption or the non-realisation
  assumption to Italian domestic holders.

MONITORING:
  Escalate immediately to Strategy & Brainstorm if Agenzia delle
  Entrate issues guidance on utility token burn events or fan token
  PTG mechanics.
```

---

## DAC8 and Reporting Obligations

```
EFFECTIVE: January 1 2026 (first reporting year)
LEGISLATION: D.Lgs. 194/2025 (transposition of EU Directive 2023/2226)
FIRST EXCHANGE REPORT DEADLINE: June 30 2027
FIRST INTERNATIONAL DATA EXCHANGE: September 30 2027
RE-CONFIRMED this pass: all three dates unchanged, re-verified against
Tier 2 tax-advisory sources discussing the Agenzia delle Entrate's own
Provvedimento n. 186865 (22 June 2026) and its July 29 2026 FAQ
clarifications (see Legislative History above for the FAQ detail).

All MiCA-authorised exchanges automatically transmit to Agenzia delle
Entrate: client identification, balances, and nine categories of
transactions per Italian-resident user.

Included in DAC8 reporting scope:
  · Fan token purchases and sales
  · Crypto-to-crypto swaps (including fan token exchanges)
  · Transfer value and counterparty data

NOTE (added this pass): the July 2026 FAQ clarifications confirm that
the set of transactions a CASP must REPORT to Agenzia delle Entrate is
broader than the set of transactions that are actually TAXABLE — some
reported activity (e.g. certain neutral swaps) will generate a data
record without generating a tax liability. This does not change what
is taxable; it clarifies that reporting volume and taxable-event
volume are two different things, which is useful context for
interpreting DAC8's behavioural-visibility effect below.

STRUCTURAL IMPLICATION:
  Italian residents transacting fan tokens through regulated exchanges
  have no opacity. The tax authority receives the data regardless of
  whether the holder self-reports.
  This increases compliance pressure and may suppress speculative
  trading behaviour among Italian domestic holders relative to the
  pre-DAC8 baseline.

NON-COMPLIANT EXCHANGES:
  Italian residents transacting on non-MiCA-authorised platforms remain
  liable for Italian tax regardless of platform compliance status.
  Binance Italy ceased new account opening July 2026 pending MiCA
  authorisation — illustrates the compliance transition in progress.

AGENT RULE:
  Apply DAC8 as a behavioural modifier: Italian domestic fan token
  holders in 2026 onward are operating under full transaction visibility.
  Model Italian domestic speculative trading as structurally more
  conservative than pre-DAC8 historical patterns.
```

---

## SportMind Agent Rules

```
RULE 1 — APPLY ITALIAN FRAMEWORK ON ALL FIVE AFFECTED TOKENS:
  When analysing $ITA · $ACM · $INTER · $JUV · $NAP, load this file.
  The UNKNOWN modifier no longer applies to Italian domestic holders.
  Use: ITALY: 33% CGT · no threshold · LIFO · no hold period relief.
  This applies to any other Chiliz fan token held by Italian residents.

RULE 2 — PTG BURN TREATMENT IS EXPLICITLY UNRESOLVED:
  Do not apply the realisation assumption or non-realisation
  assumption for Italian holders in PTG analysis. Do not conflate this
  with the settled general staking-reward rule (33% on receipt) — that
  rule addresses a different fact pattern (new tokens received for
  network validation, not existing tokens surrendered for a reward).
  Flag explicitly and do not model burn-driven demand as if the tax
  outcome is known. See PTG BURN section above.

RULE 3 — ITALY IS THE HIGHEST-FRICTION JURISDICTION IN LIBRARY:
  33% with no threshold and no hold period relief = highest disposal
  friction of any jurisdiction currently documented in SportMind.
  Germany: 0% after 12 months.
  France: 30% flat, no threshold.
  UK: 20% (higher rate), £3,000 annual exempt amount.
  South Africa: 18% max CGT.
  Italy: 33%, no threshold, no relief.
  Do not treat Italian domestic holder concentration as a positive
  demand amplifier without accounting for this friction level.

RULE 4 — DAC8 CHANGES BEHAVIOURAL BASELINE:
  Italian holders cannot assume transactional opacity from 2026.
  Apply as a structural behavioural modifier — not a tax rate
  change — but model Italian domestic speculative trading as more
  conservative than pre-2026 patterns.

RULE 5 — IVAFE APPLIES TO CHILIZ CHAIN WALLETS:
  Italian residents holding fan tokens in Chiliz Chain or Socios.com
  wallets owe 0.2% annual wealth tax on December 31 value.
  Background structural cost — not a primary signal driver — but
  relevant for analysis involving high-value Italian holder cohorts.

RULE 6 — HOLDER JURISDICTION ≠ ISSUER JURISDICTION:
  $ACM · $INTER · $JUV · $NAP are Italian-club tokens, but Italian
  domestic holders may represent only a portion of total holders.
  See fan-token/holder-tax-framework.md — apply Italian framework
  only when analysing Italian-resident holder demand specifically.
  Japanese, French, German, and UK holders of these tokens face
  their respective jurisdictions' frameworks, not Italy's.
```

---

## Affected Tokens

| Token | Club | Competition 2026-27 | CDI Gate | Italian framework applies |
|---|---|---|---|---|
| $ITA | Italy national team | WC2026 DID NOT QUALIFY | — | YES — national token, Italian domestic base significant |
| $ACM | AC Milan | Europa League | TRANSITION | YES |
| $INTER | Inter Milan | UCL (Serie A champions) | CONSOLIDATION | YES |
| $JUV | Juventus | Europa League (6th place) | TRANSITION | YES |
| $NAP | Napoli | UCL | TRANSITION | YES |

Note: The Italian framework applies to any Chiliz fan token held by
Italian residents. The five tokens above are prioritised because
Italian domestic holders represent a structurally significant portion
of their holder base.

---

## Jurisdiction Comparison

| Jurisdiction | CGT rate | Threshold | Hold period relief | Transaction visibility (2026) |
|---|---|---|---|---|
| Italy | 33% | None | None | Full — DAC8 active |
| France | 30% flat | None | None | Partial |
| UK | 20% (higher rate) | £3,000 annual exempt | None | Partial |
| Germany | 0% after 12 months | €600 annual | YES — 12 months | Partial |
| South Africa | 18% max CGT | None | None | Partial — CARF active |

Italy has the highest documented disposal friction in the SportMind
library. Germany remains the most structurally favourable.

---

## Open Questions and Monitoring Flags

```
HP-11 — RESOLVED by this file: Italy regulatory gap closed for
CGT framework. The UNKNOWN modifier is replaced by specific rules.

REMAINING OPEN QUESTIONS (not resolved by this file — all four
re-checked 2026-09-28, none resolved this pass):

PTG burn = taxable disposal?
  Status: UNRESOLVED (re-checked, no change)
  Action: Escalate if Agenzia delle Entrate guidance issued

Staking/airdrop treatment for fan token rewards
  Status: UNRESOLVED for fan-token-specific rewards (re-checked)
  Action: General crypto staking rewards ARE taxed as "redditi
  diversi" at 33% on receipt (settled rule, re-confirmed this pass) —
  but this addresses proof-of-stake validation rewards, a different
  fact pattern from fan-token engagement rewards (merchandise, VIP
  access, PTG-style rewards). The up-to-43% IRPEF framing in the
  file's prior version was not traced to a specific confirmed source
  this pass — the settled general staking rate is 33% (matching CGT),
  not a separate higher IRPEF band; monitor for any fan-token-specific
  guidance that might apply a different (e.g. IRPEF) treatment,
  but do not treat 43% as a confirmed current figure without a
  specific source, which this pass did not find.

33% rate subject to further revision?
  Status: MONITOR (re-checked, no change)
  Action: No 2027 Budget Law preview or crypto-specific amendment
  proposal found as of 2026-09-28. Direction of travel historically
  upward (rate raised at every cycle since 2023), with one failed
  attempt each to raise it further and to delay its most recent
  increase — both now historical, not live. Continue to monitor the
  2027 Budget Law cycle as it develops (typically drafted
  September-October, debated through December).

CONSOB fan token-specific classification
  Status: MONITOR (re-checked, no change)
  Action: ESMA guidelines adopted 2026, no fan token ruling yet.
  CONSOB's ordinary 2026 activity (MiCA transitional deadline
  enforcement, ESMA guideline adoption, routine unauthorised-website
  blocking) continues but includes nothing fan-token-specific as of
  2026-09-28.
```

---

## Sources and Verification

```
PRIMARY SOURCES:
  Law 199/2025 (2026 Budget Law) — 33% CGT rate from January 1 2026
  D.Lgs. 194/2025 — DAC8 transposition (EU Directive 2023/2226)
  Agenzia delle Entrate measure, June 22 2026 (Provvedimento n.
    186865) — DAC8 implementation; July 29 2026 FAQ — operational
    clarifications on reporting vs. taxable scope (NEW this pass)
  TUIR Article 67(1)(c-sexies) — crypto classification basis
  CONSOB weekly newsletters (2026, various) — MiCA transitional
    deadline enforcement, ESMA guideline adoption, routine
    unauthorised-crypto-website blocking actions (checked this pass,
    consulted directly at consob.it)

SECONDARY SOURCES (cross-check only):
  Multiple crypto tax guidance and tax-advisory sources consulted
  2026-09-28 (this pass): agendadigitale.eu, fiscomania.com,
  fiscoetasse.com, milanofinanza.it, centrofiscale.com,
  aziendabanca.it, italiaoggi.it, informazionefiscale.it — consistent
  across all sources: 33% rate · no threshold · LIFO · DAC8 active ·
  EMT carve-out at 26% does not apply to fan tokens · general staking
  rewards taxed as redditi diversi at 33% on receipt (a settled but
  DIFFERENT question from the PTG burn question, see above).

CONSOB CHECK: Searched consob.it directly and multiple Tier 2 sources
  for fan-token or utility-token-specific classification guidance.
  NONE FOUND as of 2026-09-28 — negative result, re-confirming
  Strategy Chat's preliminary search rather than finding what it
  missed. Ordinary CONSOB MiCA/enforcement activity continues but
  contains nothing fan-token-specific.

PTG BURN GUIDANCE: No primary or secondary source found as of
  2026-09-28 (re-checked this pass, same negative result as the prior
  verification on 2026-07-30). UNRESOLVED status is confirmed by
  absence of guidance, not by inference from the general staking rule
  (see PTG BURN section above for why these are distinct questions).

2027 BUDGET LAW CHECK: Searched for any 2027 Budget Law preview or
  crypto-specific amendment proposal. NONE FOUND as of 2026-09-28 —
  this is expected, since Italian Budget Law drafts typically surface
  in Tier 2 coverage from October onward; monitor again at the next
  30-day cycle and more closely as the 2027 Budget Law process begins.

LAST VERIFIED: 2026-09-28
```

---

## MIND DIMENSIONS

| Dimension | Status | Notes |
|---|---|---|
| Intelligence (1) | ACTIVE | Italian holder tax as domain knowledge; 33% rate as signal framework |
| Reasoning (2) | ACTIVE | Causal: 33% rate → high disposal friction → suppressed Italian trading |
| Context (3) | ACTIVE | 2026 convergence of Law 199/2025 + DAC8 + MiCA as structural context |
| Memory (4) | ACTIVE | Legislative history 2023–2026 traceable, including two failed rate-change attempts (42% proposal, delay-to-2027 proposal) now recorded as historical |
| Judgment (5) | ACTIVE | Italy = highest-friction jurisdiction correctly positioned vs Germany |
| Attention (6) | ACTIVE | PTG burn gap flagged; monitoring triggers defined; staking rule now distinguished from PTG burn question to prevent false-resolution |
| Communication (7) | ACTIVE | Agent rules numbered; modifier stated in single-line format |
| Verification (8) | ACTIVE | Sources cited; last verified stamped; UNRESOLVED confirmed by absence on all four open flags this pass |
| Learning (9) | ACTIVE | Rate rising at every revision — direction encoded as forward signal; failed rate-change attempts on both directions now recorded as evidence of how contested the rate is |
| Integration (10) | ACTIVE | Compatibility list connects CDI files, national profile, EU-MiCA |
| Calibration (11) | ACTIVE | UNKNOWN removal tied to specific legislative evidence, not assumption |
| Adaptation (12) | ACTIVE | Open questions define monitoring triggers for future updates |
| Ethics (13) | ACTIVE | Framework presented factually; no guidance on avoidance |
| Transparency (14) | ACTIVE | UNRESOLVED sections clearly labelled; no false certainty; staking-vs-PTG-burn distinction added to prevent an agent inferring false resolution |
| Execution (15) | EMERGING | Agent rules structured for direct application in pre-match analysis |
| Collaboration (16) | EMERGING | File designed to load alongside CDI and national profile files |

---

## COMPATIBILITY

Compatible with:
macro/regulatory/eu-mica.md — MiCA classification (Italy is EU member)
fan-token/holder-tax-framework.md — cross-jurisdiction comparison
fan-token/national-profiles/ita.md — $ITA token profile
market/club-intelligence/acm.md — $ACM CDI
market/club-intelligence/inter.md — $INTER CDI
market/club-intelligence/juv.md — $JUV CDI
market/club-intelligence/nap.md — $NAP CDI
intelligence/country-scan/italy.md — country-intelligence companion file (out of scope for this patch)

© 2026 SportMind
