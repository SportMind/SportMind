# Contributing to SportMind

Thank you for wanting to contribute. SportMind's value comes entirely from the quality and breadth of its skills — every sport expert who contributes makes every AI agent that uses SportMind smarter.

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

**Completeness** — A skill is not complete without all five sections: domain model, risk variables, event playbooks (minimum 4), key commands, and agent reasoning prompts.

**Neutrality** — Skills should be analytically neutral. Do not write skills that favour a particular team, fighter, or outcome.

**Agent-readiness** — Read your skill aloud as if you are an AI agent receiving it as a system prompt. Does it give clear, actionable guidance? If it is vague or requires outside knowledge to interpret, revise it.

**Format consistency** — Follow the template exactly. Reviewers will reject PRs with structural inconsistencies — this is not pedantry, it is what allows agents to parse skills reliably.

---

## How to contribute a new sport skill

### Step 1 — Check what exists

Look at the skills table in the main README. If the skill already exists (even as 🔜 Planned), open an issue first to coordinate — someone may already be working on it.

### Step 2 — Copy the template

```bash
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
- [ ] Key commands table references real skills from the ecosystem
- [ ] Agent reasoning prompts section has 5–8 numbered rules
- [ ] Data sources section is complete
- [ ] Compatibility section is complete
- [ ] No placeholder text remaining from the template

### Step 4 — Open a PR

Title format: `[Sport] Add football domain skill` or `[Athlete] Improve mma striking profile`

In the PR description, briefly explain:
- What you added or changed
- What sources or data informed the result impact matrices
- Any areas where you were estimating vs citing data

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

## Review process

All PRs are reviewed by at least one maintainer with knowledge of the relevant sport. Reviews focus on:

1. **Structural compliance** — does it follow the template?
2. **Factual accuracy** — are the result matrices and risk tiers credible?
3. **Agent utility** — would an AI agent following this skill reason correctly?
4. **Writing quality** — is it clear, concise, and unambiguous?

Target review time is 7 days. If your PR has not been reviewed in 14 days, comment to request a review.

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

---

## Becoming a co-maintainer

SportMind is designed to be maintained by its community, not by a single person.
Co-maintainers have merge rights for their area of the repository and are added to
`.github/CODEOWNERS` so GitHub automatically routes relevant PRs to them.

**There is no application process.** Co-maintainership happens through demonstrated
contribution. The path is:

```
1. Contribute quality work consistently
   — 3+ merged PRs in a domain, OR
   — 10+ validated calibration records, OR
   — 5+ validated translations in a single language

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
- Review everything — only PRs touching their CODEOWNERS area
- Be available immediately — 7-day review windows are the standard

**Domain areas that will need co-maintainers first:**
- Calibration records (highest volume once community is active)
- Football domain (most contributions expected)
- Cricket domain (second highest volume)
- i18n languages (native speaker reviewers for each language)

If you are interested in becoming a co-maintainer, the fastest path is submitting
calibration records — they demonstrate judgment, honesty, and familiarity with the
library's quality standards in a concrete, verifiable way.

---

Thank you for helping build the sports intelligence layer for AI.

---

## Contributing beyond skills (v3.0+)

### Calibration data

Submit outcome records to improve SportMind's modifier accuracy.

```
Location: community/calibration-data/{sport}/{year}/{month}/
Format: See community/calibration-data/README.md
Label: calibration-data
Reward: +1 leaderboard point per validated record
```

### Translations (i18n)

Translate skills into supported languages. Native speakers only — quality over quantity.

```
Location: i18n/{lang}/sports/{sport}/ or i18n/{lang}/athlete/{sport}/
Standards: See i18n/README.md — field names and code stay in English
Label: translation, lang-{code}
Reward: +8 leaderboard points per skill per language
```

### Platform and tooling

Improve the platform layer, monitoring scripts, or skill registry.

```
Files: platform/*.md, scripts/*.py, .github/workflows/*.yml
Label: platform, tooling
Requirements: All changes must be backward compatible
Review: maintainers review for API stability
```

### Skill registry metadata

When submitting new skills, include the metadata block at the top of your skill file:

```yaml
---
skill_id: domain.{sport}
type: domain | athlete | fantoken | core | market | macro
sport: {sport-name}
tier: 1-4
status: stable | beta | stub
layers: [1]
contract: signal.domain | modifier.athlete | etc.
version: 1.0.0
contributor: "@your-github-handle"
---
```

See `platform/skill-registry.md` for the complete metadata standard.
---

## Community modifier extension review

When external contributors are regularly active, SportMind will introduce a
structured peer-review process for new modifier extensions — planned for v4.0.

This will cover:
- Minimum calibration record requirements for any new modifier proposal
- Community review before new signal modifiers enter the library
- GitHub Discussions voting on modifier additions
- Versioned modifier extension framework

Until then: new modifier proposals should be raised as GitHub Issues with label
`modifier-proposal`. Maintainers will review within 14 days.

For security concerns about skill file integrity, see `SECURITY.md`.
