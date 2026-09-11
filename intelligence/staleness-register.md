---
name: staleness-register
description: Central staleness tracking register for all
  Tier A SportMind library files. Read by SMI Chat on
  every briefing. Updated by Build Chat on every patch.
version: v1.0.0
last-updated: 2026-09-10
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

| File | Last Verified | Next Due | Status | Notes |
|---|---|---|---|---|
| argentina.md | 2026-08-20 | 2026-09-19 | CURRENT | |
| belgium.md | 2026-08-22 | 2026-09-21 | CURRENT | |
| brazil.md | 2026-09-07 | 2026-10-07 | CURRENT | Patched BC9 · MP 1.303/2025 lapsed · CGT corrected |
| eu-mica.md | 2026-08-17 | 2026-09-16 | DUE | 7 days to threshold |
| eu.md | 2026-07-10 | 2026-08-09 | OVERDUE | 60 days overdue |
| france.md | 2026-08-21 | 2026-09-20 | CURRENT | |
| germany.md | 2026-08-21 | 2026-09-20 | CURRENT | |
| global-regulatory-landscape.md | 2026-07-17 | 2026-08-16 | OVERDUE | 53 days overdue |
| italy.md | 2026-07-31 | 2026-08-30 | OVERDUE | 39 days overdue |
| ksa.md | 2026-07-10 | 2026-08-09 | OVERDUE | 60 days overdue |
| netherlands.md | 2026-08-25 | 2026-09-24 | CURRENT | |
| pakistan.md | 2026-08-24 | 2026-09-23 | CURRENT | HP-13 weekly monitoring |
| russia.md | 2026-09-03 | 2026-10-03 | CURRENT | Patched BC9 · 282-FZ statutory suppressor |
| south-africa-sars.md | 2026-07-27 | 2026-08-26 | OVERDUE | 43 days overdue · HP-9 active |
| turkey.md | 2026-07-31 | 2026-08-30 | OVERDUE | 39 days overdue |
| uae.md | 2026-07-10 | 2026-08-09 | OVERDUE | 60 days overdue |
| uk-cryptoasset-regime.md | 2026-07-17 | 2026-08-16 | OVERDUE | 53 days overdue · HP-10 active · September 14 event |
| us-token-taxonomy.md | 2026-07-10 | 2026-08-09 | OVERDUE | 60 days overdue · CLARITY Act · SEC/CFTC March 2026 |

---

## TIER A — intelligence/country-scan/ (30-day cycle)

Last audit: 2026-09-09 · Source: Strategy Chat 28

| File | Last Verified | Next Due | Status | Notes |
|---|---|---|---|---|
| _registers.md | 2026-08-25 | 2026-09-24 | CURRENT | |
| argentina.md | 2026-08-18 | 2026-09-17 | CURRENT | |
| brazil.md | 2026-08-18 | 2026-09-17 | NEEDS UPDATE | Stale CGT reference · MP 1.303/2025 lapsed |
| eu-bloc.md | 2026-08-19 | 2026-09-18 | CURRENT | |
| france.md | 2026-08-18 | 2026-09-17 | CURRENT | |
| germany.md | 2026-08-18 | 2026-09-17 | CURRENT | |
| italy.md | 2026-08-18 | 2026-09-17 | CURRENT | |
| japan.md | 2026-08-18 | 2026-09-17 | CURRENT | |
| netherlands.md | 2026-08-26 | 2026-09-25 | CURRENT | |
| portugal.md | 2026-08-18 | 2026-09-17 | CURRENT | |
| russia.md | 2026-08-18 | 2026-09-17 | NEEDS UPDATE | 282-FZ statutory suppressor not reflected |
| south-africa.md | 2026-08-18 | 2026-09-17 | CURRENT | |
| spain.md | 2026-08-18 | 2026-09-17 | CURRENT | |
| turkey.md | 2026-08-18 | 2026-09-17 | CURRENT | |
| uk.md | 2026-08-18 | 2026-09-17 | CURRENT | HP-10 active · monitor |
| usa.md | 2026-08-19 | 2026-09-18 | CURRENT | |

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

## OVERDUE SUMMARY (as of 2026-09-09)

9 files requiring attention:

| File | Days Overdue | Priority | Reason |
|---|---|---|---|
| eu.md | 60 | 🔴 HIGH | Core EU framework |
| ksa.md | 60 | 🔴 HIGH | GCC regulatory posture |
| uae.md | 60 | 🔴 HIGH | VARA/ADGM framework |
| us-token-taxonomy.md | 60 | 🔴 HIGH | CLARITY Act · SEC/CFTC March 2026 |
| global-regulatory-landscape.md | 53 | 🔴 HIGH | Cross-jurisdiction overview |
| uk-cryptoasset-regime.md | 53 | 🔴 HIGH | HP-10 active · Sep 14 event |
| south-africa-sars.md | 43 | 🟠 MEDIUM | HP-9 active |
| italy.md | 39 | 🟠 MEDIUM | Active UCL fan token jurisdiction |
| turkey.md | 39 | 🟠 MEDIUM | Active UCL fan token jurisdiction |

---

## REGISTER CHANGELOG

| Date | Action | Files affected | Updated by |
|---|---|---|---|
| 2026-09-09 | Register created · initial Tier A audit | All 34 files | Strategy Chat 28 · BC10 Task A |
| 2026-09-10 | Staleness notice blocks added | macro/regulatory/ — all 18 files | BC10 Task B |
