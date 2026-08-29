---
name: audit-R[N]-[home-slug]-vs-[away-slug]-[competition-slug]-[YYYY-MM-DD]
status: COMPLETE
parent-record: R[N] · community/calibration-data/football/[filename].md
auditor: [Internal / @handle]
audit-date: [YYYY-MM-DD]
library-version: v[X.X.X]
---

# Reasoning Audit — R[N] · [HOME] v [AWAY]

## Record reference

Match: [HOME] v [AWAY]
Competition: [Competition] — [Round]
Date: [YYYY-MM-DD]
Direction: [HOME / AWAY / DRAW]
Outcome: [CORRECT / INCORRECT]
Parent record: R[N] · [filename].md
Audit date: [YYYY-MM-DD]
Auditor: [Internal / @handle]

---

## Overall verdict

OVERALL: [GREEN / AMBER / RED]

Layer 1 — Intelligence:  [PASS / PARTIAL / FAIL]
Layer 2 — Reasoning:     [PASS / PARTIAL / FAIL]
Layer 3 — Context:       [PASS / PARTIAL / FAIL]
Layer 4 — Judgment:      [PASS / PARTIAL / FAIL]
Layer 5 — Verification:  [PASS / PARTIAL / FAIL]
Layer 6 — Execution:     [PASS / PARTIAL / FAIL]

---

## Layer verdicts

### Layer 1 — Intelligence (Dim 1)

Verdict: [PASS / PARTIAL / FAIL]
Note: [One-line note on what passed, what was partial, or what failed.]

### Layer 2 — Reasoning (Dim 2)

Verdict: [PASS / PARTIAL / FAIL]
Note: [One-line note.]

### Layer 3 — Context (Dim 3)

Verdict: [PASS / PARTIAL / FAIL]
Note: [One-line note. PARTIAL if BRAZIL_REGULATORY_LOADED flag is
absent from a record involving Brazilian club tokens ($MENGO
$VERDAO $FLU $SCCP $SPFC $GALO $SACI $VASCO $BAHIA). The flag
confirms the Brazil CGT framework was loaded before analysis.
Its absence is a context loading gap, not a framework failure.]

### Layer 4 — Judgment (Dim 5)

Verdict: [PASS / PARTIAL / FAIL]
Note: [One-line note. If FAIL: state specifically whether HOLD gate
was missed or confidence tier was materially wrong.]

### Layer 5 — Verification (Dim 8)

Verdict: [PASS / PARTIAL / FAIL]
Note: [One-line note. If FAIL: state whether Gate 1 was missed or
token was unverified. For football records: PARTIAL if chiliscan.com
was not cited as on-chain verification source in the parent record.
chiliscan.com is the expected on-chain source for all Chiliz fan
token football records — its absence in the record template is a
known gap scoped for a separate fix.]

### Layer 6 — Execution (Dim 15)

Verdict: [PASS / PARTIAL / FAIL]
Note: [One-line note. REGISTRY-GAP: Pre-v4.1.32 records map to 14
Mind Dimensions only — Execution (Dim 15) and Collaboration (Dim 16)
were added at v4.1.32. A PARTIAL here for pre-v4.1.32 records is
expected and does not indicate a framework failure. State: "pre-v4.1.32
record — 14-dimension mapping · Layer 6 retroactive PARTIAL expected."
Retroactive pass planned after prospective standard established.]

---

## Key findings

STRONGEST LAYER: [Layer N — one-line reason]
WEAKEST LAYER:   [Layer N — one-line reason]

PATTERN NOTE:
[1 to 2 sentences on what this audit reveals about framework application.
What should be reinforced or watched in future records?]

---

## Action required

[Select one:]

NONE — GREEN record, no action needed.

OR

FRAMEWORK NOTE — flag for Strategy Chat review:
[Describe the issue and which framework section needs clarifying.]

OR

LIBRARY UPDATE REQUIRED — escalate to Strategy Chat immediately:
[Describe the failure and which file needs updating.]

---

*SportMind v[X.X.X] · Reasoning Audit Framework v1.0.0*
*Audit: R[N] · [OVERALL VERDICT] · [YYYY-MM-DD]*
*© 2026 SportMind*
