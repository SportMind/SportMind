---
name: staleness-register
description: Central staleness tracking register for all
  Tier A SportMind library files. Read by SMI Chat on
  every briefing. Updated by Build Chat on every patch.
version: v1.0.0
last-updated: 2026-09-21
sources: [chat]
---

# SportMind Staleness Register

## Purpose

Central tracking register for SportMind Tier A library
files. Tier A files contain time-sensitive regulatory
content with a 30-day verification cycle. This register
enables automatic staleness detection across all reading
surfaces — SMI Chat, Build Chat, and external agents.

## Status values

| Status | Meaning | Action |
|---|---|---|
| CURRENT | Verified within 30-day cycle | None |
| DUE | Within 7 days of threshold | Monitor |
| OVERDUE | Past 30-day threshold | Flag in SMI · escalate to Strategy Chat |
| NEEDS UPDATE | Known content issue | Patch required · escalate immediately |

## Verification cycles

Tier A — 30-day cycle: macro/regulatory/ · intelligence/country-scan/
Tier B — 90-day cycle: market/CDI files (to be added — follow-on task)

---

## AGENT RULES

RULE 1 — SMI CHAT:
On every briefing, scan this register for any file with
status OVERDUE or NEEDS UPDATE. Surface all flagged files
in the Priority 0 regulatory block. Include: file path ·
days overdue · last verified date · any notes.
If no files are OVERDUE or NEEDS UPDATE: state
"Staleness register: all Tier A files CURRENT or DUE."

RULE 2 — BUILD CHAT:
After every file patch or verification, update the
relevant row in this register immediately before
committing. Update: Last Verified date · Next Due date ·
Status · Notes. Update last-updated in frontmatter.
This is a mandatory step — never skip register update.

RULE 3 — EXTERNAL AGENTS:
If loading a file whose status in this register is
OVERDUE or NEEDS UPDATE, surface a caveat in output:
"Note: [file] is [N] days past its verification cycle.
Regulatory content may not reflect current framework.
Verify against primary sources before applying to live
analysis."

---

## TIER A — macro/regulatory/ (30-day cycle)

Last audit: 2026-09-09 · Source: Strategy Chat 28
Status refresh (date-based, no content verification): 2026-09-21

| File | Last Verified | Next Due | Status | Notes |
|---|---|---|---|---|
| argentina.md | 2026-09-25 | 2026-10-25 | CURRENT | Verified 2026-09-25 · V1 (AFIP→ARCA, Decree 953/2024) · V2 (cepo partial easing, individuals free Apr 2025, corporate restricted) · V4 (CNV PSAV RG 1058/2025) · V5 (Bienes Personales FY2025 thresholds) CONFIRMED · V3 (CGT) UNKNOWN stands · V7 ($ARG token) not reconfirmed · V8 (Independiente) UNRESOLVED · Italy diaspora rate corrected 26%→33% |
| belgium.md | 2026-08-22 | 2026-09-21 | DUE | due today · content re-verification queued |
| brazil.md | 2026-09-07 | 2026-10-07 | CURRENT | Patched BC9 · MP 1.303/2025 lapsed · CGT corrected · BCB deadline corrected Oct 29 → Oct 30 per secondary sources · primary-source confirmation pending |
| eu-mica.md | 2026-09-14 | 2026-10-14 | CURRENT | MiCA full application Dec 2024 · CASP wave ongoing · fan token utility token classification substance-over-form · BC11 Task 10 |
| eu.md | 2026-09-14 | 2026-10-14 | CURRENT | MiCA fully in force Dec 2024 · Socios/Chiliz MFSA authorised · MiCA passporting operative · BC11 Task 10 |
| france.md | 2026-08-21 | 2026-09-20 | OVERDUE | 31 days overdue |
| germany.md | 2026-08-21 | 2026-09-20 | OVERDUE | 31 days overdue |
| global-regulatory-landscape.md | 2026-09-14 | 2026-10-14 | CURRENT | Regime clusters updated · BC11 tasks integrated · MiCA full application · Russia statutory suppressor · UK FCA gateway · Equity Token category added · BC11 Task 12 · BCB deadline corrected Oct 29 → Oct 30 per secondary sources · primary-source confirmation pending |
| hong-kong.md | 2026-09-14 | 2026-10-14 | CURRENT | VATP live Jun 2023 · retail access permitted · probable non-security VA · Socios/Chiliz licence UNCONFIRMED · BC11 Task 7 |
| italy.md | 2026-07-31 | 2026-08-30 | OVERDUE | 52 days overdue |
| ksa.md | 2026-07-10 | 2026-08-09 | OVERDUE | 73 days overdue |
| netherlands.md | 2026-08-25 | 2026-09-24 | DUE | due in 3 days · content re-verification queued |
| pakistan.md | 2026-08-24 | 2026-09-23 | DUE | due in 2 days · HP-13 weekly monitoring |
| russia.md | 2026-09-03 | 2026-10-03 | CURRENT | Patched BC9 · 282-FZ statutory suppressor |
| singapore.md | 2026-09-14 | 2026-10-14 | CURRENT | PSA + DTSP live · probable DPT · Socios/Chiliz licence UNCONFIRMED · BC11 Task 6 |
| south-africa-sars.md | 2026-09-14 | 2026-10-14 | CURRENT | HP-9 ACTIVE · CARF live 2 Mar 2026 · ITR12 4522 enforcement active · VDP window active · $SAFA affected · BC11 Task 11 |
| turkey.md | 2026-07-31 | 2026-08-30 | OVERDUE | 52 days overdue |
| uae.md | 2026-07-10 | 2026-08-09 | OVERDUE | 73 days overdue |
| uk-cryptoasset-regime.md | 2026-09-14 | 2026-10-14 | CURRENT | HP-10 ELEVATED · NCA freeze extended ~Jan 2027 · FCA gateway 30 Sep 2026 · go-live 25 Oct 2027 · Socios/Chiliz FCA auth UNCONFIRMED · BC11 Task 8 |
| south-korea.md | 2026-09-14 | 2026-10-14 | CURRENT | VAUPA live · DABA pending · fan token classification OPEN · BC11 Task 5 |
| us-token-taxonomy.md | 2026-07-10 | 2026-08-09 | OVERDUE | 73 days overdue · CLARITY status patched · primary-source confirmation of SEC/CFTC 17 Mar 2026 release pending |

---

## TIER A — intelligence/country-scan/ (30-day cycle)

Last audit: 2026-09-09 · Source: Strategy Chat 28
Status refresh (date-based, no content verification): 2026-09-21

| File | Last Verified | Next Due | Status | Notes |
|---|---|---|---|---|
| _registers.md | 2026-08-25 | 2026-09-24 | DUE | due in 3 days |
| argentina.md | 2026-08-18 | 2026-09-17 | OVERDUE | 34 days overdue · Country-scan cycle lapsed — re-verification not yet scheduled |
| brazil.md | 2026-09-10 | 2026-10-10 | CURRENT | CGT corrected · MP 1.303/2025 lapsed confirmed · one-liner added · BC10 Task C |
| eu-bloc.md | 2026-08-19 | 2026-09-18 | OVERDUE | 33 days overdue · Country-scan cycle lapsed — re-verification not yet scheduled |
| france.md | 2026-08-18 | 2026-09-17 | OVERDUE | 34 days overdue · Country-scan cycle lapsed — re-verification not yet scheduled |
| germany.md | 2026-08-18 | 2026-09-17 | OVERDUE | 34 days overdue · Country-scan cycle lapsed — re-verification not yet scheduled |
| hong-kong.md | 2026-09-14 | 2026-10-14 | CURRENT | BC11 Task 7 |
| italy.md | 2026-08-18 | 2026-09-17 | OVERDUE | 34 days overdue · Country-scan cycle lapsed — re-verification not yet scheduled |
| japan.md | 2026-08-18 | 2026-09-17 | OVERDUE | 34 days overdue · Country-scan cycle lapsed — re-verification not yet scheduled |
| netherlands.md | 2026-08-26 | 2026-09-25 | DUE | due in 4 days · content re-verification queued |
| portugal.md | 2026-08-18 | 2026-09-17 | OVERDUE | 34 days overdue · Country-scan cycle lapsed — re-verification not yet scheduled |
| russia.md | 2026-09-10 | 2026-10-10 | CURRENT | 282-FZ statutory suppressor added · STRUCTURALLY EXCLUDED IN STATUTE · one-liner added · BC10 Task C |
| singapore.md | 2026-09-14 | 2026-10-14 | CURRENT | BC11 Task 6 |
| south-africa.md | 2026-08-18 | 2026-09-17 | OVERDUE | 34 days overdue · Country-scan cycle lapsed — re-verification not yet scheduled |
| south-korea.md | 2026-09-14 | 2026-10-14 | CURRENT | BC11 Task 5 |
| spain.md | 2026-08-18 | 2026-09-17 | OVERDUE | 34 days overdue · Country-scan cycle lapsed — re-verification not yet scheduled |
| turkey.md | 2026-08-18 | 2026-09-17 | OVERDUE | 34 days overdue · Country-scan cycle lapsed — re-verification not yet scheduled |
| uk.md | 2026-08-18 | 2026-09-17 | OVERDUE | 34 days overdue · HP-10 active · monitor · Country-scan cycle lapsed — re-verification not yet scheduled |
| usa.md | 2026-08-19 | 2026-09-18 | OVERDUE | 33 days overdue · Country-scan cycle lapsed — re-verification not yet scheduled |

---

## TIER A — equity-token/ (30-day cycle)

Last audit: 2026-09-14 · Source: BC11 Task 4
Status refresh (date-based, no content verification): 2026-09-21

| File | Last Verified | Next Due | Status | Notes |
|---|---|---|---|---|
| socios-equity-token.md | 2026-09-14 | 2026-10-14 | CURRENT | HOLD FILE · Conditions 2+3 open · no named club · no tokenomics |

---

## COVERAGE GAPS

Jurisdictions present in macro/regulatory/ but missing
from intelligence/country-scan/:

| Jurisdiction | regulatory/ | country-scan/ | Priority |
|---|---|---|---|
| Pakistan | ✅ pakistan.md | ❌ missing | HIGH · HP-13 active |
| KSA | ✅ ksa.md | ❌ missing | MEDIUM |
| UAE | ✅ uae.md | ❌ missing | MEDIUM |

Action: scope country-scan files for Pakistan, KSA, UAE
as Build Chat tasks. Pakistan is highest priority given
HP-13 active status.

---

## OVERDUE SUMMARY (as of 2026-09-21 — date-based)

Status recalculated from Next Due dates for all rows. No content verification performed or claimed.

**OVERDUE (19 rows):**

| File | Days overdue | Priority | Reason |
|---|---|---|---|
| macro/regulatory/ksa.md | 73 | 🔴 HIGH | PROHIBITIVE jurisdiction · BC12 task |
| macro/regulatory/uae.md | 73 | 🔴 HIGH | VARA/ADGM framework · BC12 task |
| macro/regulatory/us-token-taxonomy.md | 73 | 🔴 HIGH | CLARITY Act not enacted · SEC/CFTC Mar 2026 operative · primary-source confirmation pending |
| macro/regulatory/italy.md | 52 | 🟠 MEDIUM | Active UCL fan token jurisdiction · BC12 task |
| macro/regulatory/turkey.md | 52 | 🟠 MEDIUM | Active UCL fan token jurisdiction · BC12 task |
| macro/regulatory/france.md | 31 | 🟠 MEDIUM | Country-scan cycle lapsed — re-verification not yet scheduled |
| macro/regulatory/germany.md | 31 | 🟠 MEDIUM | Country-scan cycle lapsed — re-verification not yet scheduled |
| intelligence/country-scan/argentina.md | 34 | MEDIUM | Country-scan cycle lapsed — re-verification not yet scheduled |
| intelligence/country-scan/eu-bloc.md | 33 | MEDIUM | Country-scan cycle lapsed — re-verification not yet scheduled |
| intelligence/country-scan/france.md | 34 | MEDIUM | Country-scan cycle lapsed — re-verification not yet scheduled |
| intelligence/country-scan/germany.md | 34 | MEDIUM | Country-scan cycle lapsed — re-verification not yet scheduled |
| intelligence/country-scan/italy.md | 34 | MEDIUM | Country-scan cycle lapsed — re-verification not yet scheduled |
| intelligence/country-scan/japan.md | 34 | MEDIUM | Country-scan cycle lapsed — re-verification not yet scheduled |
| intelligence/country-scan/portugal.md | 34 | MEDIUM | Country-scan cycle lapsed — re-verification not yet scheduled |
| intelligence/country-scan/south-africa.md | 34 | MEDIUM | Country-scan cycle lapsed — re-verification not yet scheduled |
| intelligence/country-scan/spain.md | 34 | MEDIUM | Country-scan cycle lapsed — re-verification not yet scheduled |
| intelligence/country-scan/turkey.md | 34 | MEDIUM | Country-scan cycle lapsed — re-verification not yet scheduled |
| intelligence/country-scan/uk.md | 34 | MEDIUM | Country-scan cycle lapsed — re-verification not yet scheduled · HP-10 active |
| intelligence/country-scan/usa.md | 33 | MEDIUM | Country-scan cycle lapsed — re-verification not yet scheduled |

**DUE within 7 days (5 rows):**

| File | Days until due | Note |
|---|---|---|
| macro/regulatory/belgium.md | 0 (due today) | content re-verification queued |
| macro/regulatory/pakistan.md | 2 | HP-13 weekly monitoring active |
| macro/regulatory/netherlands.md | 3 | content re-verification queued |
| intelligence/country-scan/_registers.md | 3 | |
| intelligence/country-scan/netherlands.md | 4 | content re-verification queued |


## REGISTER CHANGELOG

| Date | Action | Files affected | Updated by |
|---|---|---|---|
| 2026-09-09 | Register created · initial Tier A audit | All 34 files | Strategy Chat 28 · BC10 Task A |
| 2026-09-10 | Staleness notice blocks added | macro/regulatory/ — all 18 files | BC10 Task B |
| 2026-09-10 | Staleness one-liners added + content fixes | country-scan/brazil.md · country-scan/russia.md | BC10 Task C |
| 2026-09-14 | CGT content fix — MP 1.303/2025 LAPSED · progressive rate applied | market/south-america/south-america-fan-token-intelligence.md | BC11 Task 3 |
| 2026-09-14 | New Tier A section added · equity-token/ · HOLD file registered | equity-token/socios-equity-token.md | BC11 Task 4 |
| 2026-09-14 | New files added · regulatory + country-scan · South Korea gap filled | macro/regulatory/south-korea.md · intelligence/country-scan/south-korea.md | BC11 Task 5 |
| 2026-09-14 | New files added · regulatory + country-scan · Singapore | macro/regulatory/singapore.md · intelligence/country-scan/singapore.md | BC11 Task 6 |
| 2026-09-14 | New files added · regulatory + country-scan · Hong Kong | macro/regulatory/hong-kong.md · intelligence/country-scan/hong-kong.md | BC11 Task 7 |
| 2026-09-14 | Patch · HP-10 update · NCA freeze extended · FCA gateway 30 Sep 2026 · go-live 25 Oct 2027 confirmed | macro/regulatory/uk-cryptoasset-regime.md | BC11 Task 8 |
| 2026-09-21 | CLARITY Act status patched · NOT ENACTED (Senate cloture failed 15 Sep 2026) · row stays OVERDUE · primary-source confirmation pending | macro/regulatory/us-token-taxonomy.md | BC12 Task 5 |
| 2026-09-21 | BCB VASP deadline corrected Oct 29 → Oct 30 · secondary sources only · primary-source (BCB Resolutions 519–521) confirmation pending | macro/regulatory/brazil.md · macro/regulatory/global-regulatory-landscape.md | BC12 Task 6 |
| 2026-09-21 | argentina.md re-verification attempted · primary sources unreachable · Status → NEEDS UPDATE · perishable Copa América wording corrected · Italy diaspora conflict flagged | macro/regulatory/argentina.md | BC12 Task 8a |
| 2026-09-25 | argentina.md web verification · V1/V2/V4/V5 confirmed · ARCA rename · cepo partial easing · CNV PSAV · Bienes Personales thresholds · Italy diaspora 26%→33% · V3 UNKNOWN stands · V7 not reconfirmed · V8 UNRESOLVED · Status → CURRENT | macro/regulatory/argentina.md | BC12 Argentina Follow-Up |
| 2026-09-21 | Status refresh · statuses recalculated from Next Due dates for all rows · 19 rows OVERDUE · 5 rows DUE · no content verification claimed | intelligence/staleness-register.md | BC12 Task 8 |
| 2026-09-14 | Patch · eu.md + eu-mica.md · MiCA full application · Socios/Chiliz MFSA authorisation noted | macro/regulatory/eu.md · macro/regulatory/eu-mica.md | BC11 Task 10 |
| 2026-09-14 | Patch · HP-9 update · CARF confirmed first African · ITR12 4522 active · VDP window active | macro/regulatory/south-africa-sars.md | BC11 Task 11 |
| 2026-09-14 | Patch · regime clusters updated · BC11 tasks integrated · friction tiers · key themes · equity token | macro/regulatory/global-regulatory-landscape.md | BC11 Task 12 |
