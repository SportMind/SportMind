# Contributing to SportMind

Thank you for wanting to contribute. SportMind's value comes entirely from the quality and breadth of its skills — every sport expert who contributes makes every AI agent that uses SportMind smarter.

Looking to report a framework gap rather than submit a calibration record? See [CONTRIBUTING-GAPS.md](CONTRIBUTING-GAPS.md).

---

## The SportMind Library Rule

One question determines whether something belongs in SportMind:

**Will this intelligence still be true and useful in six months?**

If yes — it belongs in the library.
If no — it does not.

SportMind is a reasoning library, not a data feed. It teaches AI agents
how to think about sports, fan tokens, and the commercial intelligence the
industry runs on. It does not store live data, current standings, or
temporary states.

### Enduring intelligence — belongs here

**Sport domain reasoning patterns** How to reason about a UCL Final as a fan token supply event.
How qualifying delta predicts race outcomes on specific circuit types.
How dew factor changes T20 outcomes in evening matches.
These are permanently true.

**Structural mechanics** The 1/400 FTP pre-liquidation ratio.
The 75% stop-loss minimum supply.
The Model 1 and Model 2 distinction.
These are true until officially changed.

**Regulatory frameworks** Not the current status of a bill — but how a regulatory framework
affects market access and what it means for agent reasoning.
The framework for reasoning about MiCA, SI 2026/102, SEC/CFTC guidance.
These are enduring reasoning tools.

**Calibration records** Completed real-world events with verified outcomes. Pre-match signal,
post-match result, supply event confirmed. Permanently on the record.
These never expire.

**Intelligence gap fills** New layers that teach agents how to reason about domains SportMind
does not yet cover. Referee intelligence. Venue intelligence.
Tournament structure. Transfer window frameworks. Weather modifiers.
These are permanently useful.

### Expiring intelligence — does not belong here

**Current injury and availability status** Who is injured today is not SportMind intelligence. How to reason about
injury type, return timeline, and recurrence risk is.

**Live prices and market data** What Bitcoin is trading at right now is not SportMind intelligence.
How Bitcoin dominance affects fan token altcoin season probability is.

**Current league standings** Who is top of the Premier League today is not SportMind intelligence.
How title race position affects fan token demand in the final weeks of
a season is.

**Scheduled dates and process status** When a regulatory markup is scheduled is not SportMind intelligence.
What a markup outcome means for market access and how to reason about it is.

**Transfer rumours and unconfirmed moves** Today's transfer gossip is not SportMind intelligence. How a marquee
signing affects fan token demand curves and for how long is.

**Short-term conditions** Tonight's weather forecast is not SportMind intelligence. How humidity
above 75% in an evening T20 changes dew accumulation and spin bowling
effectiveness is.

### The test for every contribution

Before submitting anything to SportMind ask yourself three questions:

1. **Is this a reasoning framework or a data point?** Frameworks belong here. Data points do not.

2. **Will this be true in six months?** If yes — submit it. If no — do not.

3. **Does this teach an agent how to think, or does it tell an agent
what is true right now?** Teaching belongs here. Current states do not.

If you are uncertain — ask in the GitHub Discussions before submitting.
The maintainers will help you determine whether your contribution is
enduring intelligence or expiring data.

### What happens to expiring intelligence

Expiring intelligence is not worthless — it is just not library material.
The SportMind automation agent uses expiring intelligence in its live
reasoning layer. If you have signal data that is current and relevant
but not enduring, submit it as a calibration record after the event is
complete. A completed match result with a pre-match signal and a verified
outcome is a calibration record — enduring, verifiable, permanently useful.

---

## What we're looking for

### High priority

─ Fill any of the 14 community stub sports (see GOOD_FIRST_ISSUES.md for the full list)

- New athlete skills for sports already covered by a domain skill
- Improvements to existing skills — better playbooks, corrected data, updated competition structures
- Translations of existing skills into other languages

### Always welcome

- Corrections to result impact matrices (if data shows different numbers)
- New playbooks for edge cases not yet covered
- Agent reasoning prompt improvements
- Documentation improvements

### Out of scope

- Data pipeline code (SportMind is reasoning documents, not code)
- Platform-specific API wrappers (those belong in integration packages)
- Skills for fictional sports or non-competitive entertainment

---

## Skill quality standards

Every skill in SportMind — whether sport domain or athlete — must meet these standards before merging:

**Accuracy** — All result impact matrices, risk tiers, and timing windows must be grounded in real historical patterns. If you are estimating, say so clearly.

**Completeness** — A skill is not complete without all six sections: domain model, risk variables, event playbooks (minimum 4), key commands, agent reasoning prompts, and a `## MIND DIMENSIONS` section mapping the file to all 14 SportMind dimensions.

**Neutrality** — Skills should be analytically neutral. Do not write skills that favour a particular team, fighter, or outcome.

**Agent-readiness** — Read your skill aloud as if you are an AI agent receiving it as a system prompt. Does it give clear, actionable guidance? If it is vague or requires outside knowledge to interpret, revise it.

**Format consistency** — Follow the template exactly. Reviewers will reject PRs with structural inconsistencies — this is not pedantry, it is what allows agents to parse skills reliably.

---

## How to contribute a new sport skill

### Step 1 — Check what exists

Look at the skills table in the main README. If the skill already exists (even as 🔜 Planned), open an issue first to coordinate — someone may already be working on it.

### Step 2 — Copy the template

```
cp templates/template-new-sport-skill.md sports/your-sport/sport-domain-your-sport.md
```

Fill in every section. Do not skip sections or mark them "TODO" in a PR.

### Step 3 — Self-review checklist

Before opening a PR, check every item:

- [ ] Domain model covers the full season calendar with token behaviour notes
- [ ] Competition reference covers at least 2 tiers (primary and secondary)
- [ ] Result impact matrix has at least 5 distinct result scenarios with % ranges
- [ ] Risk variables section covers at least 3 sport-specific risks with token impact
- [ ] Minimum 4 playbooks, each with trigger / entry / exit / filter / sizing / note
- [ ] Key commands table references real skills from the suite
- [ ] Agent reasoning prompts section has 5–8 numbered rules
- [ ] `## MIND DIMENSIONS` section present, all 14 dimensions mapped
- [ ] Data sources section is complete
- [ ] Compatibility section is complete
- [ ] No placeholder text remaining from the template

### Step 4 — Open a PR

Title format: `[Sport] Add sport name` or `[Athlete] Improve sport name`

In the PR description, briefly explain:

- What you added or changed
- What sources informed the result impact matrices
- Any areas where you estimated rather than cited data

No fixed review window. Skills merge when they meet the quality standards above.
If your PR has been open more than 30 days, comment to request review.

---

## How to contribute an athlete skill

Athlete skills follow the same process but use `templates/template-new-athlete-skill.md`.

Additional requirements for athlete skills:

- Every command must have complete parameter and return value documentation
- Return value examples must be valid JSON
- Modifier values must be consistent with the modifier system defined in `core/core-athlete-modifier-system.md`
- Sport-specific form metrics must be added to `core/core-athlete-record-schema.json`

---

## How to improve an existing skill

1. Open an issue describing what is inaccurate or missing
2. Get a maintainer to confirm the improvement is needed
3. Submit a PR with the specific changes and a brief rationale

For small corrections (typos, outdated competition names, minor % adjustments), you can skip the issue and go straight to a PR.

---

## How to contribute a calibration record

Calibration records are the most direct way to contribute to SportMind.
A record is a pre-match signal submitted before an event, with the result verified after.

### Two record types

**Fan token record** — at least one team has an active, verified Chiliz Chain fan token.
This is the primary calibration target. Fan token records validate SportMind's
core fan token intelligence layer.

**Sport intelligence layer record** — neither team has a fan token. Records from football,
MMA, cricket, basketball, and other sports. These validate SportMind's sport
intelligence layer across different domains.

### High-value calibration targets

- **Dual fan token football** — both teams have active Chiliz Chain fan tokens.
  Highest value. Check [fantokens.com](https://fantokens.com) for active tokens and upcoming fixtures.
- **MMA** — $UFC and $PFL are confirmed active Chiliz Chain fan token partners.
  Any UFC Fight Night, PPV, or PFL card main event qualifies as a fan token calibration record.
- **Single fan token football** — one team has a fan token, the other does not.
  Valid fan token record — validates one-sided fan token intelligence.

### How to submit

1. **Before the event:** Open a GitHub Issue with your pre-match signal output.
   Title format: `Calibration Record — [Team A] vs [Team B] — [Competition] — [Date]`
   Timestamp is everything — the issue must be opened before kickoff.

2. **After the event:** Comment on your issue with the final result and whether
   the direction was CORRECT or INCORRECT. If incorrect, include a root cause note.

Use the template in `community/calibration-data/TEMPLATE.md` for the full field set.
See [FIRST-RECORD-GUIDE.md](FIRST-RECORD-GUIDE.md) for step-by-step instructions.

---

## Review process

All PRs are reviewed by at least one maintainer with knowledge of the relevant sport. Reviews focus on:

1. **Structural compliance** — does it follow the template, including MIND DIMENSIONS?
2. **Factual accuracy** — are the result matrices and risk tiers credible?
3. **Agent utility** — would an AI agent following this skill reason correctly?
4. **Writing quality** — is it clear, concise, and unambiguous?

**Timelines:** Skill PRs (new sports, athlete skills, improvements): reviewed within 30 days.
Calibration records: most merge within 48 hours of result submission.
If a skill PR has not been reviewed in 30 days, comment to request a review.

Reviews are async — no fixed window. If your PR has not been reviewed in 30 days, comment to request a review.

---

## Style guide

- Write in plain English. Avoid jargon that a non-expert in that sport would not understand — if you must use a term, define it inline.
- Use sentence case for headings (not Title Case).
- Code blocks for all playbooks, formulas, and agent prompts.
- Tables for all matrices and command references.
- Percentage ranges (e.g., +5–15%) not point estimates — outcomes are probabilistic.
- "token" not "coin" — we are talking about fan tokens specifically.

---

## Code of conduct

SportMind is a technical project. Discussions should be about accuracy, quality, and coverage of sports knowledge. Keep all communication respectful and focused on the work.

---

## Recognition

All contributors are listed in the repository's contributor graph. Significant contributions (new complete skills, major improvements) will be called out in release notes.

The first 10 contributors to submit verified fan token calibration records earn permanent recognition as Founding Calibrators. See [FIRST-RECORD-GUIDE.md](FIRST-RECORD-GUIDE.md) for details and current open slots.

---

## Becoming a co-maintainer

SportMind is designed to be maintained by its community, not by a single person.

**There is no application process.** Co-maintainership happens through demonstrated
contribution. The path is:

```
1. Contribute quality work consistently
   — 3+ merged PRs in a domain, OR
   — 10+ validated calibration records

2. Demonstrate good judgment
   — Reviewing other contributors' PRs constructively
   — Flagging issues before they become problems
   — Understanding the quality bar, not just meeting it

3. Get invited
   — Maintainers will reach out directly
   — Or you can express interest in a GitHub issue
```

**What co-maintainers do:**

- Review and merge PRs in their domain without involving the repository owner
- Triage issues relating to their area
- Participate in recalibration decisions when modifier records accumulate

**What co-maintainers do not need to do:**

- Review everything — only PRs touching their domain area
- Be available for async review — no fixed window, but aim to respond within 30 days

If you are interested in becoming a co-maintainer, the fastest path is submitting
calibration records and proposing new modifier extensions via GitHub Issues
with the label `modifier-proposal`. Maintainers review modifier proposals within 30 days.

---

Thank you for helping build the sports intelligence layer for AI.
