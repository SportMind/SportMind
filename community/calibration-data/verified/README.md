# Verified Calibration Records

Records in this directory were submitted before a real event took
place and verified against the actual outcome afterward.

Every record has:
- A pre-match prediction submitted before kickoff/event start
- A confirmed real-world result
- Source verification (on-chain, official league, primary source, or a
  completed pre-match signal plus post-match outcome audit — see the
  Copa Libertadores QF section below for the third verification method
  this now covers)

---

## Current verified records

**FTP PATH_2 on-chain verified (football/2026/04/):**
- pl-2026-04-11-arsenal-bournemouth-ftp.json
- ucl-2026-04-07-sporting-arsenal-ftp.json
- ucl-2026-04-15-arsenal-sporting-ftp.json

Source: fantokens.com/fan-token-play — VERIFIED on-chain

**WC2026 + UCL series (in calibration/2026/):**
See `calibration/2026/` for the 10-record verified series including
the 9/9 WC2026 perfect record.

**Copa Libertadores QF series (in community/calibration-data/football/):**
- libertadores-qf-flu-vs-platense-leg1-2026-09-08.md
- libertadores-qf-platense-vs-flu-leg2-2026-09-15.md
- libertadores-qf-verdao-vs-ldu-leg1-2026-09-09.md
- libertadores-qf-ldu-vs-verdao-leg2-2026-09-16.md
- libertadores-qf-estudiantes-vs-sccp-leg1-2026-09-09.md
- libertadores-qf-sccp-vs-estudiantes-leg2-2026-09-16.md
- libertadores-qf-idv-vs-mengo-leg1-2026-09-10.md
- libertadores-qf-mengo-vs-idv-leg2-2026-09-17.md

Verification method for this series is DIFFERENT from the FTP burns
above: these 8 are not verified on-chain. Each has a documented
pre-match signal and HOLD-gate decision made before the fixture, and a
verified post-match outcome confirming directional correctness — a
completed pre-match-signal-plus-outcome audit, not a blockchain
transaction record. Do not assume all records in this file share one
verification method; the FTP burns and this series are verified by two
genuinely different processes, both rigorous, neither a substitute for
the other. (Series result for reference: 3 of 4 fixtures correct —
75% directional accuracy.)

---

## Total verified records

21 records:
- 3 in `community/calibration-data/verified/` (this directory) — FTP
  PATH_2 on-chain
- 10 in `calibration/2026/` — WC2026 series + UCL Final
- 8 in `community/calibration-data/football/` — Copa Libertadores QF
  series (see above)

---

## Relationship to the library-wide "25 pre-match verified" figure

The library's public calibration count (146 records total · 25
pre-match verified · 119 seed, per the SC34 Strategy Chat ruling,
2026-09-28) is the governing figure for all agent-facing output —
briefings, SMI updates, the website stat bar. This file's scope has
always been narrower than that library-wide figure: it indexes records
with a completed, documented verification process filed in the three
specific locations listed above, not every verified record in the
library by every possible definition.

After this update, this file accounts for 21 of the library-wide 25.
The remaining gap of 4 records has NOT been fully reconciled during
this pass. One strong candidate was identified: R138 ($NAP vs $AFC,
UCL Matchday 1) is documented elsewhere in the library as CLOSED with
a confirmed directionally-correct pre-match call, but it does not live
in any of the three locations this file indexes and was not added here
without further confirmation of exactly where it should be filed and
whether it is the only such record. The remaining records making up
the gap were NOT independently identified this pass — this file's
author did not have direct repository browsing access during this
patch and could not enumerate every calibration folder to account for
them individually.

DO NOT treat the 21 figure in this file and the 25 figure used
elsewhere as contradictory — they are not the same measurement. This
file's 21 is a conservative, fully-indexed subset; the library-wide 25
is the broader figure Pele has ruled as authoritative. This gap is
flagged here for a future pass to close, either by identifying and
indexing the remaining records in this file, or by a Strategy Chat
ruling that this file's narrower scope is intentionally permanent and
the two figures are expected to diverge going forward. Until one of
those happens, treat the 4-record gap as open, not as an error in
either figure.

---

## Adding a verified record

See [FIRST-RECORD-CHALLENGE.md](../../../FIRST-RECORD-CHALLENGE.md)
and [TEMPLATE.md](../TEMPLATE.md).

Submit a GitHub Issue before the event starts.
Timestamp is everything — the issue must be opened before kickoff.
