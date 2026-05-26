---
name: privacy-notice
description: >
  Developer reference document. Privacy obligations that arise when building
  on SportMind. Covers which SportMind frameworks may involve personal data,
  developer GDPR/UK GDPR/CCPA obligations, on-chain pseudonymity, and
  SportMind's own privacy position under the Ethics dimension. Not a reasoning
  framework. Not legal advice. MIT licensed — developers are responsible for
  their own compliance.
---

# SportMind — Developer Privacy Notice

**This is a reference document for developers. It is not a reasoning framework,
not a Mind dimension, and not legal advice.**

---

## Purpose

SportMind is an open intelligence, reasoning, and context library. It does not
collect, store, or process personal data itself.

This notice exists because some SportMind frameworks reason about holder
behaviour, fan identity, and on-chain wallet activity. Developers building
applications on these frameworks may be processing personal data and should
understand their obligations.

---

## What SportMind does

SportMind provides:
- Reasoning frameworks for sports intelligence and fan token signals
- A verified fan token registry (publicly available blockchain data)
- Calibration records (anonymised prediction outcomes)
- Agent prompts and workflow patterns

SportMind does not:
- Collect or store user data
- Process personal data
- Track individual holders
- Store wallet addresses
- Retain any application data

---

## Where personal data may arise when building on SportMind

The following SportMind frameworks reason about holder behaviour. When a
developer's application combines these frameworks with identifying information —
wallet addresses linked to identities, account data, or user profiles — personal
data is being processed.

```
HOLDER ARCHETYPE CLASSIFICATION
File: fan-token/fan-holder-profile-intelligence.md
  Classifying individual holders as Governors, Loyalists, Speculators, or
  Amplifiers based on their on-chain behaviour constitutes profiling under
  GDPR Article 4(4) when the holder is identifiable.

COMMUNITY HEALTH INDEX (CHI)
File: fan-token/governance-intelligence.md
  CHI scoring aggregates holder behaviour data. When applied to identifiable
  individuals rather than anonymous aggregates this may constitute personal
  data processing.

ON-CHAIN ADDRESS INTELLIGENCE
File: platform/chiliz-chain-address-intelligence.md
  Wallet addresses are pseudonymous, not anonymous. Linking on-chain activity
  to identifiable individuals creates personal data processing obligations.

GOVERNANCE VOTE TRACKING
File: fan-token/governance-intelligence.md
  Tracking individual governance votes linked to identified holders is
  processing of personal data.
```

---

## Developer obligations

Developers building applications that process personal data using SportMind
frameworks are responsible for their own compliance with applicable data
protection law. This includes but is not limited to:

```
GDPR (EU/EEA):
  Establish a lawful basis for processing before collecting data.
  Provide a privacy notice to users.
  Honour data subject rights (access, deletion, portability).
  Conduct a DPIA if processing is high risk (e.g. large-scale profiling).
  Appoint a DPO if required.

UK GDPR:
  Same obligations as EU GDPR apply under UK law post-Brexit.

CALIFORNIA (CCPA/CPRA):
  Provide notice at collection.
  Honour opt-out rights.
  Do not sell personal information without explicit consent.

OTHER JURISDICTIONS:
  Check local data protection law before processing holder data.
  Fan token holders may be located anywhere globally — multi-jurisdiction
  obligations may apply.
```

---

## On-chain data and privacy

Blockchain data is public. Wallet addresses on Chiliz Chain are visible to
anyone. However:

**Pseudonymity is not anonymity.**

A wallet address linked to a Socios account, an email address, or any other
identifier becomes personal data under most data protection frameworks.
Processing public blockchain data in combination with identifying information
requires a lawful basis under GDPR and equivalent laws.

Developers should not assume that using publicly available on-chain data
removes data protection obligations.

---

## SportMind's position on privacy

SportMind's Ethics dimension (dimension 13 of the fourteen-dimension Mind
architecture) establishes that SportMind will not:

- Produce signals designed to manipulate individual holders
- Enable surveillance of individual fan behaviour without their consent
- Facilitate use of personal data beyond its original collection purpose

Privacy is not a separate Mind dimension — it is an expression of the Ethics
dimension applied to data processing contexts.

---

## Questions

SportMind is MIT licensed and open source. There is no central support function
for privacy queries.

Developers with specific privacy questions should consult a qualified data
protection practitioner in their jurisdiction.

For general SportMind questions:
`github.com/SportMind/SportMind/issues`

---

## MIND DIMENSIONS

**Intelligence:** [NOT APPLICABLE] — this is a reference document, not a reasoning framework.

**Reasoning:** [NOT APPLICABLE] — this document does not provide signal reasoning chains.

**Context:** Applies when developers are building applications that process holder behaviour data using SportMind frameworks. The four specific frameworks identified above are the key context triggers.

**Memory:** [NOT APPLICABLE]

**Judgment:** Relevant — developers must exercise judgment about when their use of SportMind frameworks crosses into personal data processing. The distinction between aggregate anonymous signals and individual holder profiling is the key judgment boundary.

**Attention:** Developers should give elevated attention to the four frameworks identified in this document when building consumer-facing applications that handle wallet or account data.

**Learning:** [NOT APPLICABLE]

**Integration:** Privacy obligations integrate with the Ethics dimension across all SportMind development contexts. When any of the four identified frameworks are used with identifying data, compliance obligations activate.

**Communication:** This document IS the communication — a clear statement of privacy context for developers building on SportMind.

**Calibration:** [NOT APPLICABLE]

**Adaptation:** Applicable — data protection law evolves. Developers should verify current law in their jurisdiction rather than relying solely on this document.

**Verification:** Developers should verify their compliance posture with qualified practitioners. This document is a starting point for awareness, not a substitute for legal advice.

**Ethics:** This document is a direct expression of SportMind's Ethics dimension — transparency about obligations that arise from using the library.

**Transparency:** This document IS a transparency measure — SportMind making visible the privacy implications of its frameworks for developers who may not have considered them.

---

## Compatibility

**Ethics dimension:**      `core/master-reasoning-architecture.md`
**Holder profiling:**      `fan-token/fan-holder-profile-intelligence.md`
**Governance signals:**    `fan-token/governance-intelligence.md`
**On-chain intelligence:** `platform/chiliz-chain-address-intelligence.md`

---

*SportMind v3.97.88 · MIT License · sportmind.dev*
*Not legal advice. Developers are responsible for their own compliance.*
