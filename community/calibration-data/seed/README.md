# Seed Calibration Records

Records in this directory are synthetic modifier validation
examples created by @sportmind-core. They were not submitted
before real events — they are worked scenarios designed to
validate SportMind's modifier frameworks across sports and
edge cases.

---

## Purpose

Seed records exist to:
- Document how specific modifiers perform across scenario types
- Provide worked examples of SportMind reasoning chains
- Validate modifier interactions before live deployment
- Give new contributors a reference for record format and
  the level of detail expected in a real submission

---

## What seed records are NOT

Seed records are not proof of real prediction accuracy. They
are structural examples. The verified record count (see
`community/calibration-data/verified/`) is the measure of
real-world performance.

Do not cite seed records as evidence of SportMind accuracy.
The verified records in `calibration/2026/` and
`community/calibration-data/verified/` are the accuracy evidence.

---

## Structure

Records are organised by sport and date, mirroring the verified
directory structure. The `source` field in each record reads
`"seed-record"` or `"seed record — derived from [scenario]"`.

---

## Contributing real records

If you have run a SportMind analysis before a real event and
recorded the outcome, submit it as a verified record instead.

See [FIRST-RECORD-CHALLENGE.md](../../../FIRST-RECORD-CHALLENGE.md)
for how to submit a real pre-match record and earn recognition
as a Founding Calibrator.
