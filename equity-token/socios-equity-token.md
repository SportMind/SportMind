# Socios Equity Token — Intelligence HOLD File

**Version:** v4.6.81
**Directory:** equity-token/
**Status:** HOLD — Conditions 2 and 3 unresolved
**Last Verified:** 2026-09-28
**File Type:** HOLD — do not load into signal bundles or calibration records

---

## HOLD STATUS — READ FIRST

This file is a structured HOLD record. It documents confirmed
facts about the Socios Equity Token announcement and the
conditions required before this asset enters active library
analysis.

**This asset is NOT yet live. It is NOT loadable into signal
bundles, calibration records, or pre-match briefings.**

HOLD CONDITIONS:

| Condition | Status | Detail |
|---|---|---|
| 1 — Regulated infrastructure | RESOLVED ✓ | Securitize confirmed · US + EU regulated tokenisation platform · EU DLT Pilot Regime size gates apply (see Condition 1) |
| 2 — Named club | OPEN | No named club confirmed as of 2026-09-28 |
| 3 — Tokenomics published | OPEN | Tokenomics not published as of 2026-09-28 |

All three conditions must resolve before activation. Current
state: 1/3 resolved. File remains on HOLD.

---

## DIRECTORY CONVENTION

This file lives in equity-token/ — NOT fan-token/.

This distinction is structural and permanent:

| Category | Directory | Product type | Classification |
|---|---|---|---|
| Fan Tokens | fan-token/ | Utility/governance tokens | Not a security |
| Equity Tokens | equity-token/ | Regulated securities (probable) | Distinct category |

Never conflate Fan Tokens and Equity Tokens in signal bundles,
file paths, or agent output. These are distinct product
categories with distinct regulatory treatment, distinct
signal mechanics, and distinct library handling.

The equity-token/ directory is extensible — other issuers
may be added as the category develops beyond Socios/Chiliz.

---

## CONFIRMED FACTS

· Announced: 27 August 2026 · Chiliz Group press release
· Infrastructure partner: Securitize · announced 2 September 2026
· Product description: new digital asset category designed to
  provide fans and investors with access to minority equity
  stakes in professional sports teams
· Mechanism: Chiliz Group acquires minority stakes in
  participating clubs · Socios Equity Token represents a
  structured economic interest in those teams
· Chiliz MiCA whitepaper registered under ESMA — noted
· Securitize × VARA MoU signed 3 September 2026 — contextual
  signal only · noted but NOT elevated to jurisdiction claim
  (see Jurisdiction section below)
· Disclaimer on Chiliz/Socios announcement: "subject to
  applicable laws and regulatory approvals · product design ·
  token utilities · holders' rights · availability and launch
  timelines remain subject to change"

---

## CONDITION 1 — INFRASTRUCTURE (RESOLVED ✓)

**Securitize** is a US SEC-registered transfer agent and
EU-regulated tokenisation platform. Its selection as
infrastructure partner confirms:

· Regulated tokenisation pathway in place
· Compliance architecture capable of supporting securities-
  grade issuance across US and EU jurisdictions
· NOT a signal that distribution is confirmed in any
  specific jurisdiction — infrastructure ≠ distribution approval

Condition 1 is resolved. This does not activate the file.
Conditions 2 and 3 must also resolve.

### DLT Pilot Regime Mechanics

The 2 September 2026 Securitize/Socios.com release states the
first Socios Equity Token offering is expected to be the first
project launched through Securitize's European Trading &
Settlement System under the EU DLT Pilot Regime — Regulation
(EU) 2022/858. That regime carries hard numerical size gates
in Article 3. These are structural constraints on any offering
routed through it:

| Gate | Threshold | Applies to |
|---|---|---|
| Individual issuer (shares) | Market cap below EUR 500M | Admitted at the moment of admission to a DLT market infrastructure (Art. 3) |
| Individual issuance (bonds) | Issue size below EUR 1B | Bonds, securitised debt, money-market instruments (Art. 3) — issuers with market cap not above EUR 200M at issuance are not subject to this threshold |
| Aggregate — admission stop | EUR 6B | A new instrument cannot be admitted or recorded if it would take the infrastructure's aggregate market value to EUR 6B |
| Aggregate — transition trigger | EUR 9B | Operator must activate its transition strategy once aggregate market value of all instruments on the infrastructure reaches EUR 9B |

Two separate aggregate mechanisms — never conflate them. EUR 6B
blocks new admissions; EUR 9B forces the operator to begin
transitioning instruments to conventional market infrastructure.

**Structural consequence for Condition 2 (named club):**
The EUR 500M individual-issuer ceiling is a size gate on which
clubs could realistically take part in a first offering under
this regime. A club whose market capitalisation exceeds EUR 500M
would not qualify as an issuer of shares under Article 3. This
narrows the plausible field for Condition 2 but does NOT resolve
it — no club is named.

**Caveats — read before using these figures:**
· EUR 500M is the regulation's ceiling. National competent
  authorities may set LOWER thresholds for a specific
  infrastructure (ESMA publishes any such lower thresholds).
  Securitize's actual authorised limits were not verified at
  this pass — treat EUR 500M as the upper bound, not the
  confirmed binding figure.
· Market cap is measured at admission, so a club's eligibility
  is a point-in-time test, not a permanent classification.
· Juventus: secondary reporting following the 2 September 2026
  release states Juventus's market cap exceeds the EUR 500M
  individual-issuer threshold. This specific claim was NOT
  independently verified at this pass — no primary source and no
  named-club statement in the release supports it. Treat as
  unconfirmed. Do NOT infer that Juventus, or any club, is a
  participant or is excluded: the release names no club.
· The European Commission proposed amendments to Regulation
  (EU) 2022/858 on 4 December 2025 (Market Integration and
  Supervision Package). The base regulation remains in force
  and the thresholds above are the current text, but they could
  change if that proposal is adopted. Monitor.

**Source status:**
· Thresholds: PRIMARY — Regulation (EU) 2022/858, Art. 3
  (EUR-Lex, ELI http://data.europa.eu/eli/reg/2022/858/oj) and
  ESMA DLT Pilot Regime page (esma.europa.eu). Verified 2026-09-28.
· Link between the Socios initiative and the DLT Pilot Regime:
  Tier 1 — Securitize/Socios.com joint release, 2 September 2026
  (published on socios.com and PR Newswire), corroborated by
  multiple Tier 2 outlets including The Block.

---

## CONDITION 2 — NAMED CLUB (OPEN)

No club has been publicly named as a participant in the
Socios Equity Token programme as of 2026-09-28. The
2 September 2026 release states participating teams will be
announced when individual offerings are approved.

A named club is required before this file can activate.
The named club will determine:
· Which CDI file(s) are affected
· Whether any existing fan token files require cross-
  referencing or agent rule additions
· Whether dual-category signals (equity + fan token
  for same club) require new handling protocols

Escalate immediately to Strategy Chat on any named club
announcement.

---

## CONDITION 3 — TOKENOMICS (OPEN)

Tokenomics have not been published as of 2026-09-28.

Required before activation:
· Token supply structure
· Economic rights of holders (dividend, profit-share,
  voting, or other)
· Transfer restrictions (if any)
· Redemption or exit mechanism (if any)

Escalate immediately to Strategy Chat on tokenomics
publication.

---

## JURISDICTION NOTE

Securitize × VARA MoU (3 September 2026) is noted as
contextual signal only. It is NOT elevated to a
jurisdiction claim for the Socios Equity Token.

Distribution jurisdiction will be confirmed only when:
· Conditions 2 and 3 resolve, AND
· Regulatory approval is obtained in named jurisdiction(s)

Do NOT infer that UAE/VARA is a confirmed distribution
jurisdiction from the MoU alone. Do NOT infer that any
jurisdiction is confirmed at HOLD stage.

---

## CLASSIFICATION

**Socios Equity Token = regulated security (probable)**
in most jurisdictions. Regulatory treatment will vary
by jurisdiction — full analysis deferred to activation.

Fan Tokens = utility/governance tokens.

These are never treated as equivalent in the library.
Never combine in a single signal bundle or output block.

---

## MONITORING INSTRUCTIONS

Monitor the following sources on a weekly basis:
· chiliz.com/blog
· socios.com
· securitize.io

Escalate IMMEDIATELY to Strategy Chat on:
· Any named club announcement (Condition 2)
· Any tokenomics publication (Condition 3)
· Any regulatory approval in a named jurisdiction
· Any change to product description or disclaimer status
· Any launch timeline announced

---

## AGENT RULES

**Rule 1 — Signal bundle exclusion:**
Do NOT load Socios Equity Token into any signal bundle.
It is not a fan token. It has no confirmed tokenomics.
It has no confirmed club. It is HOLD status.

**Rule 2 — Calibration exclusion:**
Do NOT include in calibration records. No pre-match
signal can be generated for this asset at HOLD stage.

**Rule 3 — Category separation:**
Do NOT treat as a fan token. It is a distinct product
category. Never conflate with fan-token/ assets in any
output, signal bundle, or agent briefing.

**Rule 4 — Jurisdiction inference prohibition:**
Do NOT infer distribution jurisdiction from the
Securitize × VARA MoU alone. Jurisdiction is confirmed
only when Conditions 2 + 3 resolve and regulatory
approval is obtained.

**Rule 5 — Monitoring obligation:**
Monitor chiliz.com/blog · socios.com · securitize.io
weekly. Escalate immediately on any Condition 2 or
Condition 3 resolution signal.

**Rule 6 — Activation gate:**
File activates ONLY when all three conditions resolve
AND Strategy Chat scopes the activation build task.
Build Chat does not self-activate this file.

**Rule 7 — DLT Pilot size-gate discipline:**
When discussing which clubs could participate, cite the EUR 500M
individual-issuer ceiling (Regulation (EU) 2022/858, Art. 3) as
an upper bound only. Do NOT state that any named club is
eligible or ineligible — no club is confirmed. Do NOT present
the Juventus market-cap claim as verified. Keep the EUR 6B
(admission stop) and EUR 9B (transition trigger) aggregate
mechanisms distinct.

---

## MIND DIMENSIONS

| Dimension | Status | Notes |
|---|---|---|
| Intelligence (1) | EMERGING | 1b Signal Awareness — product category confirmed · insufficient signal depth for active analysis at HOLD stage |
| Reasoning (2) | EMERGING | Structural category reasoning in place · active signal reasoning deferred until Conditions 2 + 3 resolve |
| Context (3) | EMERGING | 3b Regulatory context — EU DLT Pilot Regime size gates loaded (EUR 500M / EUR 1B / EUR 6B / EUR 9B, Reg. (EU) 2022/858 Art. 3) · equity vs fan token distinction loaded · club and tokenomics context absent |
| Memory (4) | ACTIVE | HOLD conditions and confirmed facts stored as procedural memory · escalation triggers defined |
| Judgment (5) | NOT APPLICABLE | No confidence tier assignment possible at HOLD stage · no club · no tokenomics |
| Attention (6) | ACTIVE | 6a escalation prioritisation defined · 6b urgency triggers set · 6c noise filtering (MoU ≠ jurisdiction) active · 6d threshold clear |
| Communication (7) | ACTIVE | HOLD status notation mandatory in all outputs referencing this asset |
| Verification (8) | EMERGING | Infrastructure partner verified (Securitize) · DLT Pilot thresholds verified against primary source (EUR-Lex, ESMA) · Juventus market-cap claim UNVERIFIED · club and tokenomics unverified · verification protocol deferred to activation |
| Learning (9) | NOT APPLICABLE | No calibration records possible at HOLD stage |
| Integration (10) | EMERGING | Category boundary with fan-token/ established · cross-file integration protocol deferred to activation |
| Calibration (11) | NOT APPLICABLE | No calibration records possible at HOLD stage |
| Adaptation (12) | ACTIVE | HOLD status will adapt on condition resolution · escalation path defined |
| Ethics (13) | ACTIVE | Equity token classification is high-stakes regulatory · never treat as equivalent to fan token in output |
| Transparency (14) | ACTIVE | HOLD status disclosed in all outputs · disclaimer language reproduced · condition resolution gap stated |
| Execution (15) | NOT APPLICABLE | No ENTER / HOLD / MONITOR / RETIRE signal applicable at this stage · MONITOR applies to monitoring obligation only |
| Collaboration (16) | ACTIVE | Strategy Chat is the activation authority · escalation path to Strategy Chat defined · Build Chat does not self-activate |

---

© 2026 SportMind
