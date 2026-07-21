# Contributing Gaps to SportMind

SportMind improves from real usage.
If you are building on SportMind and encounter something the library cannot reason about well — a missing framework, dimension, layer, or modifier — this is how to tell us about it.

## What qualifies as a gap

A gap is a situation where SportMind's existing intelligence, reasoning, or context frameworks cannot adequately support your analysis.

**Valid gaps:**
- A reasoning pattern that no existing file covers
- A sport or domain context where modifiers do not apply correctly
- A combination of signals that produces no guidance on how to resolve the conflict
- A Mind dimension that is clearly relevant but has no framework
- A modifier that behaves incorrectly in a specific but repeatable context

**Not valid gaps:**
- Current news or match results (these are expiring data — not library additions)
- Specific player, manager, or club current status
- Requests for SportMind to become a data provider
- Anything that fails the Library Rule: *"Will this intelligence still be true and useful in six months?"*

## The Library Rule

Before submitting a gap apply this test:

Remove all proper nouns from your proposed gap — club names, player names, manager names, specific dates, prices.

Does the gap still have value without the proper nouns?

**YES** → submit it.
**NO** → it is not a library gap.

Also apply the six-month test: Will this intelligence still be true and useful in six months? If no — it is not a library gap.

## How to submit

Open a GitHub Issue using this format:

---

**Gap type:**
FRAMEWORK_GAP / DIMENSION_GAP / MODIFIER_GAP / LAYER_GAP (fan-token · athlete · macro · market · sports) / SUB_DIMENSION_GAP

**Sport or domain:**
[Which sport, competition, or domain triggered this gap?]

**Situation:**
[What were you trying to reason about? Describe the scenario without proper nouns where possible. Minimum 50 words.]

**What SportMind could not do:**
[What reasoning was missing, incorrect, or produced no useful output? Minimum 30 words.]

**Why this matters:**
[What is the real consequence of this gap? Who else building on SportMind would encounter the same situation?]

**Affected files (if known):**
[Which SportMind files are relevant or insufficient for this situation?]

**Affected Mind dimension (if known):**
[Which of the 14 dimensions does this gap fall within or between?
Intelligence / Reasoning / Context / Memory / Judgment / Attention / Learning / Integration / Communication / Calibration / Adaptation / Verification / Ethics / Transparency]

**Suggested resolution:**
[Optional but valued. What would a framework look like? What modifier values or reasoning chain would address this?]

**Evidence:**
[Optional but strongly valued. Link to a calibration record or describe a specific analysis where this gap produced a wrong or incomplete output.]

**Your context:**
[What are you building? Which sport or domain? Approximately how many analyses have you run where this gap appeared?]

---

## What happens next

Submitted gaps are reviewed against the Library Rule and the SportMind scope. Not every gap will be accepted — but every well-formed submission is read and considered.

Gaps accepted into the library will credit the submitter in the release notes and changelog.

The first 10 external gap contributors whose submissions result in a library addition will be permanently credited in SportMind's contribution history.

## What SportMind will never add from gap reports

- Expiring data of any kind
- Named current status of any player, manager, or club
- Specific prices, scores, or results
- Any framework that fails the six-month Library Rule
- Any gap that only passes with proper nouns intact

## Questions

If you are unsure whether your gap qualifies — open an issue anyway with the label `gap-question`. The worst outcome is a redirect to an existing file that already covers your scenario.

---

*SportMind is MIT licensed and open source. Gap reports are voluntary contributions to a shared intelligence commons.*

*sportmind.dev · github.com/SportMind/SportMind*
