# CHZ Tokenomics

**Domain:** macro/chz-tokenomics.md
**Version:** v4.1.7
**Library Rule:** Six-Month Test PASSES · Proper Noun Test PASSES
**Scope:** Enduring structural tokenomics architecture only. Specific
allocation percentages, governance vote outcomes, and perishable
supply figures excluded. Current supply is a point-in-time data
point — do not hardcode; use the structural model instead.

---

## SUPPLY MODEL — HISTORICAL CONTEXT (Pre-2024)

```
MODEL:        Fixed supply
TOTAL SUPPLY: 8.8B CHZ (original issuance)
CHAINS:       ERC-20 (Ethereum) · BEP-2 (Binance Chain)
STATUS:       SUPERSEDED — replaced May 2024 via on-chain governance

Agent rule: 8.8B is a historical figure only.
  Do NOT use as current supply. Do NOT treat CHZ as fixed-supply.
  This model no longer applies.
```

---

## SUPPLY MODEL — CURRENT (Dragon8, May 6 2024 onwards)

Dragon8 was approved via on-chain validator governance on May 6 2024
(85.13% for, 0% against). It replaced the fixed-supply model with
a dynamic issuance architecture.

```
MODEL:        Dynamic — new CHZ minted per block via inflation formula
HARD CAP:     NONE — supply is uncapped
SUPPLY STATE: As of mid-2026, total supply has grown beyond 10.4B CHZ
              from the original 8.8B base
PROJECTION:   Supply expected to reach approximately 15B CHZ over
              approximately 14 years before stabilising
INFLATION:    Dynamically decreasing — high in early years,
              stabilising at 1.88% annual floor after ~14 years

BLOCK REWARD DISTRIBUTION (three channels):
  (1) Validators and their delegators — majority allocation
  (2) Community vault · liquidity providers · restaking rewards
  (3) Ecosystem and operational distribution

NOTE: Specific allocation percentages are governance-determined
  and subject to change via future proposals. See official Chiliz
  Chain governance documentation for current figures:
  governance.chilizchain.com
```

---

## DEFLATIONARY COUNTERWEIGHTS

Two deflationary mechanisms operate concurrently with block minting:

```
MECHANISM 1 — EIP-1559 TRANSACTION FEE BURN:
  Base fee burned at protocol level on every transaction.
  Reduces circulating supply in proportion to network activity.
  Higher transaction volume = higher burn rate.

MECHANISM 2 — CHZ BUY-BACK BURN:
  10% of Fan Token revenues used to buy and permanently burn CHZ
  from the open market.
  Demand-linked: burn rate scales with Fan Token ecosystem activity.

NET DEFLATION CONDITION:
  If the combined burn rate (EIP-1559 + buy-back) surpasses the
  annual inflation rate from block minting, the model turns net
  deflationary. This is a structural possibility, not a guarantee.
  Agents must not assume net deflation as a baseline.
```

---

## CONSENSUS MECHANISM — PROOF-OF-STAKED-AUTHORITY (PoSA)

Introduced via Dragon8. Hybrid model combining two elements:

```
PoA ELEMENT:
  Limited validator set takes turns producing and committing blocks.
  Not open to arbitrary participants — set is bounded.

PoS ELEMENT:
  Validator eligibility determined by CHZ staked.
  Higher stake = higher eligibility weight.

VALIDATOR TYPES:
  Main validators:      Actively produce and commit blocks
  Candidate validators: Standby — promoted if a Main validator
                        is penalised or underperforms

DELEGATORS:
  Any CHZ holder can stake with validators.
  Delegators share in block rewards proportional to stake.
  Delegator staking contributes indirectly to governance security.

GOVERNANCE WEIGHT:
  Validators vote on proposals proportional to stake held.
  CHZ staking = governance participation weight.
```

---

## ON-CHAIN GOVERNANCE

```
MECHANISM:    Validator-weighted on-chain vote
PORTAL:       governance.chilizchain.com
PRECEDENT:    Dragon8 passed May 6 2024 · 85.13% for · 0% against
              Confirms governance is functional and consequential.
STATUS:       Active — proposals continuously shape protocol evolution

Agent rule: governance proposals are perishable — specific content
  and outcomes are briefing-only signals, not library candidates.
  The existence of active governance is the structural fact to encode.
  Individual proposal outcomes (e.g. Pepper8) are monitored in SMI,
  not recorded in library files.
```

---

## AGENT RULES

```
RULE 1 — SUPPLY MODEL:
  CHZ is not a fixed-supply asset.
  Dynamic issuance with no hard cap applies from May 2024.
  Do NOT use 8.8B as current supply — it is historical.
  Do NOT model CHZ as deflationary by default.

RULE 2 — CONCURRENT PROCESSES:
  Inflationary (block minting) and deflationary (EIP-1559 burn +
  buy-back burn) mechanisms operate simultaneously.
  Net supply direction at any point depends on relative rates.
  Model both processes — do not flatten to a single direction.

RULE 3 — GOVERNANCE:
  Protocol rules are subject to change via on-chain vote.
  Any parameter in this file (allocation %, inflation rate,
  validator structure) can be modified by governance.
  Always flag governance-sensitive parameters when reasoning
  about CHZ structural mechanics in agent outputs.

RULE 4 — DATA FRESHNESS:
  Current supply figures are point-in-time data.
  Use the structural model for reasoning; fetch live data
  for current supply when precision is required.
```

---

## MIND DIMENSIONS

| Dimension | Status | Notes |
|---|---|---|
| Intelligence (1) | ACTIVE | Supply model input for CHZ demand reasoning |
| Reasoning (2) | ACTIVE | Concurrent inflation/deflation process logic |
| Context (3) | ACTIVE | Pre/post 2024 model distinction; governance context |
| Memory (4) | NOT APPLICABLE | — |
| Judgment (5) | ACTIVE | Agent rules for supply model selection |
| Attention (6) | NOT APPLICABLE | — |
| Communication (7) | NOT APPLICABLE | — |
| Verification (8) | ACTIVE | Governance-determined parameters require source check |
| Learning (9) | NOT APPLICABLE | — |
| Integration (10) | ACTIVE | Cross-references CHZ buy-back burn, Fan Token revenues |
| Calibration (11) | EMERGING | Net deflation condition is model-dependent, not confirmed |
| Adaptation (12) | ACTIVE | Governance can change any parameter — monitor actively |
| Ethics (13) | NOT APPLICABLE | — |
| Transparency (14) | ACTIVE | Supply model uncertainty disclosed; governance-sensitive flags |

---

## COMPATIBILITY

- fan-token/burn-to-glory-framework.md — CHZ buy-back burn cross-reference
- fan-token/fan-token-play.md — Fan Token revenue → buy-back burn pipeline
- macro/regulatory/global-regulatory-landscape.md — regulatory context for CHZ
- macro/partnerships.md — ecosystem infrastructure context
- fan-token/registry/complete-registry.md — Fan Token revenue sources

© 2026 SportMind
