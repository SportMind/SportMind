---
name: intelligence-briefing-agent
description: >
  Protocol document for SportMind Intelligence (SMI) briefing agents.
  Defines the full signal lifecycle from receipt to library update,
  including tier classification, verification gates, actioning rules,
  false signal handling, and the FALSE SIGNAL PROTOCOL for self-corrections.
  Works in conjunction with core/external-intelligence-intake.md.
---

# Intelligence Briefing Agent — Protocol Document

**Defines how SMI briefing agents interact with the SportMind library.
From signal receipt through to library update or rejection — including
what to do when a signal turns out to be wrong.**

---

## Signal lifecycle overview

```
SIGNAL RECEIVED
      ↓
TIER CLASSIFICATION (see core/external-intelligence-intake.md)
      ↓
VERIFICATION GATE
      ↓
  TIER 1 (act immediately)  →  Update library file → CHANGELOG → Release
  TIER 2 (monitor)          →  Queue for review → Future version if confirmed
  TIER 3 (context)          →  Log only → No library change
      ↓
POST-ACTION MONITORING
      ↓
SELF-CORRECTION (if signal is later found to be false)
      ↓
FALSE SIGNAL PROTOCOL (see below)
```

---

## Verification gate — minimum thresholds

```
BEFORE ANY LIBRARY UPDATE:

  Tier 1 requires:
    Primary source confirmation (official body, club, regulatory authority)
    Source URL traceable to originating organisation
    Signal consistent with existing library intelligence (or clearly supersedes it)
    No contradictory Tier 1 source available

  Tier 2 requires:
    Credible specialist press or secondary source
    No primary source contradiction available
    Signal labelled UNVERIFIED — MONITOR in any library note

  Tier 3 requires:
    No threshold — log and discard if insufficient to reach Tier 2

  HARD RULE:
    A Tier 1 library update may only be applied on a Tier 1 source.
    Specialist press + no primary source = Tier 2 maximum.
    No exceptions. This gate is the primary defence against false positives.
```

---

## Actioning rules

```
SIGNAL ACTIONED (library file updated):
  Document in CHANGELOG with source, verification status, and date.
  Tag as versioned release if ### Added content.
  Update core/smi-digest.md after every tagged release.

SIGNAL HELD (Tier 2 — not yet actioned):
  Add monitoring note to relevant library file if warranted.
  Label clearly: UNVERIFIED — MONITOR.
  Do not update confirmed status fields.
  Do not displace confirmed Tier 1 intelligence with unverified signal.

SIGNAL REJECTED (Tier 3 or failed verification):
  Log in CHANGELOG as ### Fixed if previously partially actioned.
  No library file update required.
  No further action unless signal is re-submitted with Tier 1 confirmation.
```

---

## FALSE SIGNAL PROTOCOL

**When SMI self-corrects a Tier 1 alert — two scenarios.**

### Scenario 1 — Signal not yet actioned

```
SITUATION:
  SMI issued a Tier 1 alert.
  The signal was classified as Tier 2 (UNVERIFIED — MONITOR) by the
  verification gate and no library update was made.
  SMI subsequently self-corrects — primary source audit found no confirmation.

ACTION:
  Do not make any library changes.
  
  Paste a documentation note only into the relevant library file or CHANGELOG:

  "False positive detected and self-corrected by SMI on [date].
   Signal: [description].
   No library changes made."

EXAMPLE (v3.97.11):
  Alert: CLARITY Act markup scheduled May 14, 2026
  Classification: Tier 2 (UNVERIFIED — no primary source confirmation)
  Self-correction: 2026-05-09 03:40 UTC — banking.senate.gov audited,
                   no committee record found
  Library change: None — documentation note added to macro-regulatory-sportfi.md
  Outcome: Protocol functioned correctly; false positive caught before actioning

WHY THIS IS VALUABLE:
  False positives that were caught are calibration events.
  Documenting them shows the verification protocol is working.
  Future agents can use the documented pattern to weight similar signals.
  Silent discard of false positives removes calibration value from the library.
```

### Scenario 2 — Signal already actioned

```
SITUATION:
  SMI issued a Tier 1 alert.
  The signal passed the verification gate and a library file was updated.
  SMI subsequently self-corrects — the signal is found to be false.

ACTION:
  Paste this correction prompt into the core SportMind build chat immediately:

  "Intelligence correction required.
   Signal [description] was actioned on [date] but has since been
   self-corrected by SMI as a false positive.
   Please revert [affected file] to previous state and document the
   correction in the changelog."

REVERT PROCEDURE (for SportMind build agent):
  1. Identify the exact change made in the original release
  2. Revert the specific field(s) modified — do not revert unrelated changes
  3. Add a correction note to the file documenting what was reverted and why
  4. Add ### Fixed entry to CHANGELOG with:
       - Original signal description and date
       - Self-correction date and source
       - What was reverted
       - What the correct status is
  5. Version bump (commit only — ### Fixed entries do not tag)
  6. Update core/smi-digest.md to reflect reverted status

CHANGELOG FORMAT FOR REVERTS:
  ## [version] — [date]
  
  ### Fixed — [file]: reverted false positive [description]
  
  Original signal:  [description] — actioned [date]
  Self-corrected:   SMI — [date] — [source audited]
  Reverted:         [specific field or section]
  Correct status:   [what it should read]
  Calibration note: False positive documented; verification gap identified at
                    [describe why the original signal passed the gate]

ESCALATION:
  If the false positive passed the Tier 1 gate (i.e. a primary source was
  cited but later found to be incorrect or misread):
    → Add a note to core/external-intelligence-intake.md under the
      relevant source's trusted source registry entry
    → Flag the source's reliability for this signal type
    → This is a source calibration event, not just a signal calibration event
```

---

## Calibration value of false positives

```
FALSE POSITIVES ARE LIBRARY ASSETS — NOT FAILURES:

  Every documented false positive adds to SportMind's calibration base.
  
  WHAT A DOCUMENTED FALSE POSITIVE PROVES:
    1. The verification protocol is working (signal was caught)
    2. The specific signal pattern (source + type + timing) is unreliable
    3. The correct status at the time is preserved and verifiable
    4. Future agents can use the pattern to downweight similar signals
  
  WHAT SILENT DISCARD LOSES:
    1. No calibration value extracted
    2. No pattern recognition for similar future signals
    3. No evidence the protocol worked
    4. Library looks cleaner but is less honest

  AGENT RULE:
    Always document false positives. Never silently discard them.
    The note costs two minutes. The calibration value persists indefinitely.

CALIBRATION RECORDS — FALSE POSITIVES:
  2026-05-09: CLARITY Act markup alert — Scenario 1 (not actioned)
    Source: specialist industry press (no primary source)
    Self-correction: banking.senate.gov audit — no committee record
    Status: DOCUMENTED in macro/macro-regulatory-sportfi.md
    Protocol: Tier 2 classification correctly prevented library change
```

---

## Integration with intake framework

```
RELATIONSHIP TO core/external-intelligence-intake.md:

  external-intelligence-intake.md:   What tier does this signal receive?
  intelligence-briefing-agent.md:    What happens after tier classification?

  LOAD ORDER FOR FULL SIGNAL PIPELINE:
    1. core/external-intelligence-intake.md  — classify the incoming signal
    2. core/intelligence-briefing-agent.md   — action or reject per tier
    3. [relevant library file]               — apply if Tier 1 confirmed
    4. CHANGELOG                             — document the decision
    5. core/smi-digest.md                    — update state summary

  The FALSE SIGNAL PROTOCOL in this file activates after step 3.
  If a signal was actioned at step 3 and later found false:
    → Scenario 2 applies → revert step 3 → document steps 4 and 5
  If a signal was not yet actioned at step 3 and found false:
    → Scenario 1 applies → document step 4 only → no revert needed
```

---

## Compatibility

**Extends:**  `core/external-intelligence-intake.md` — three-tier classification
**Used by:** `scripts/sportmind_listener.py` — automated signal routing
**Related:** `macro/macro-regulatory-sportfi.md` — regulatory signal examples
**CHANGELOG:** All actioned and reverted signals documented here


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Intelligence briefing agent: structured morning/pre-match briefing generation |
| Reasoning | ACTIVE | Briefing reasoning: prioritising signals, structuring narrative, applying confidence |
| Context | ACTIVE | Briefing context: time window, active competitions, priority signals |
| Memory | ACTIVE | Briefing history: tracking what was signalled vs what occurred for calibration |
| Judgment | ACTIVE | Briefing judgment: what to include, exclude, and flag as uncertain |
| Attention | ACTIVE | Briefing attention allocation by signal priority and time sensitivity |
| Communication | ACTIVE | This file defines structured briefing communication format |
| Verification | ACTIVE | Briefing signals require verification before inclusion |
| Learning | ACTIVE | Briefing accuracy learning from outcome comparison |
| Integration | ACTIVE | Briefing integrates all active intelligence layers |
| Calibration | ACTIVE | Briefing confidence levels are calibration outputs |
| Adaptation | ACTIVE | Briefing format adapts to user context and signal environment |
| Ethics | ACTIVE | Briefing must not present unconfirmed signals as confirmed facts |
| Transparency | ACTIVE | Briefing signal sources and confidence levels explicit throughout |


---

*SportMind v3.97.12 · MIT License · sportmind.dev*
*FALSE SIGNAL PROTOCOL — calibration through documentation*
