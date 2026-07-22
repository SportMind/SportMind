# Community Contributor Recognition

**How SportMind recognises, tracks, and celebrates community contributors
who submit calibration records, translations, skill improvements, and
application examples.**

---

## Founding Calibrators

The first 10 external contributors to submit verified fan token calibration
records earn permanent Founding Calibrator recognition.

| Slot | Calibrator | Record | Series |
|------|-----------|--------|--------|
| #1 | @AltcoinDaddy | Mexico vs South Africa | WC2026 Group Stage |
| #2 | @charan0318 | Mexico vs South Africa | WC2026 Group Stage |
| #3 | — | Open | — |
| #4 | — | Open | — |
| #5 | — | Open | — |
| #6 | — | Open | — |
| #7 | — | Open | — |
| #8 | — | Open | — |
| #9 | — | Open | — |
| #10 | — | Open | — |

See [FIRST-RECORD-CHALLENGE.md](../FIRST-RECORD-CHALLENGE.md) for how to claim an open slot.

---

## Why recognition matters

Open source projects succeed when contributors feel their work is valued
and visible. SportMind's calibration pipeline is only as strong as the
community that feeds it — every outcome record someone submits gets the
library one step closer to empirically validated modifiers.

This document defines the recognition system. It is deliberately simple:
good work should be visible, credited, and celebrated. No points systems,
no gamification, no paywalls. Just clear acknowledgement of real contributions.

---

## Contribution types and tiers

```
TIER 1 — CALIBRATION RECORDS (highest impact):
  What: Submitting outcome records from SportMind analyses you ran before matches
  Why highest impact: These are the only contributions that improve modifier accuracy
  Recognition:
    Name/handle credited in calibration record (submitted_by field)
    Listed in CONTRIBUTORS.md under "Calibration Contributors"
    After 5 records: "Calibration Contributor" badge in CONTRIBUTORS.md
    After 25 records: "Senior Calibration Contributor" status
    After 50 records: "Calibration Pioneer" — credited in recalibration reports

TIER 2 — SKILL TRANSLATIONS (i18n):
  What: Translating SportMind skill files into new languages or expanding existing ones
  Why important: Opens SportMind to non-English speaking sports markets
  Recognition:
    Credited in the translated file header (translation_author field)
    Listed in CONTRIBUTORS.md under "Translation Contributors"
    Language specialist: "AR/ES/FR/HI/PT/[lang] Specialist" notation

TIER 3 — SKILL IMPROVEMENTS:
  What: Correcting errors, adding missing sport context, improving modifier tables
  Why important: Keeps knowledge current and accurate
  Recognition:
    Credited in commit message and CONTRIBUTORS.md
    "Knowledge Contributor" notation

TIER 4 — EXAMPLES AND APPLICATIONS:
  What: New starter pack examples, application blueprints, integration patterns
  Why important: Lowers barrier for new developers
  Recognition:
    Credited as example author in the file
    "Developer Contributor" notation

TIER 5 — ISSUES AND FEEDBACK:
  What: Reporting errors, inconsistencies, or missing coverage via GitHub Issues
  Why important: Quality control that core team cannot do alone
  Recognition: Credited in the fix commit
```

---

## CONTRIBUTORS.md format

```
# SportMind Contributors

## Calibration Pioneers (50+ records)
[None yet — first opportunity to be recognised here]

## Senior Calibration Contributors (25-49 records)
[None yet]

## Calibration Contributors (5-24 records)
[None yet — be the first]

## Calibration Contributors (1-4 records)
*First external community records welcomed here — see CONTRIBUTING.md*

## Translation Contributors
| Contributor | Language | Skills translated |
|---|---|---|
| @sportmind-core | ES (Spanish) | Football domain (LaLiga/LATAM context) |
| @sportmind-core | PT (Portuguese) | Cricket domain (lusophone markets) |
| @sportmind-core | AR (Arabic) | Football domain (Gulf + North Africa) |
| @sportmind-core | HI (Hindi) | Cricket domain (India + diaspora) |
| @sportmind-core | FR (French) | Football domain (Ligue 1 + Francophone) |

## Knowledge Contributors
| Contributor | Sport | Contribution |
|---|---|---|
| @sportmind-core | All | Library foundation and all core skills |

## Developer Contributors
| Contributor | Type | Description |
|---|---|---|
| @sportmind-core | All | Starter pack, application blueprints, MCP server |
```

---

## How to get your first calibration record in

The fastest path from new contributor to recognised in the library:

```
STEP 1 — Pick an upcoming match with an active fan token
  Best: a dual fan token match (both teams have active Chiliz Chain tokens)
  Check fantokens.com to verify token status before submitting
  Black logo signal: greyscale logo = potentially inactive, verify first

STEP 2 — Run SportMind analysis before the match
  Option A: any LLM + quickstart prompt from sportmind.dev/first-record/
  Option B: MCP server via Claude Desktop (sportmind_pre_match)
  Record DIRECTION and SportMind Score from the output

STEP 3 — Watch the match result

STEP 4 — Fill in the outcome record template
  Template: community/calibration-data/TEMPLATE.md (markdown format)
  Key fields:
    recorded_at: the time you ran your analysis (BEFORE the match)
    submitted_by: your GitHub handle or identifier
    direction_correct: CORRECT or INCORRECT
    key_modifier_validated: which modifier were you testing?
    notes: what did you learn? (honest; wrong-direction records valued equally)

STEP 5 — Submit via GitHub Issue or PR
  Issue title: Calibration Record — [Team A] vs [Team B] — [Competition] — [Date]
  File path (PR): community/calibration-data/{sport}/{your-record-filename}.md
  Or open a GitHub Issue with "calibration-submission" label (we handle the PR)

STEP 6 — Get credited
  Your handle appears in the record and in CONTRIBUTORS.md

Most important rule: the analysis must be run BEFORE the match.
Records submitted after knowing the outcome are not calibration records.
```

---

## Recognition for the first external contributors

The first 10 external contributors to submit calibration records will receive:

1. Permanent credit in CONTRIBUTORS.md as Founding Calibrators — will not be removed
2. Special acknowledgement in the CHANGELOG entry for the version their
   first record is included in
3. Their name/handle mentioned in the recalibration report that first uses
   their records to update modifier values

This is not a commercial reward — it is recognition that the first people
to believe in and contribute to a community project deserve to be remembered
in that project's history.

---

## Sport-specific calibration priorities

```
HIGHEST PRIORITY — FAN TOKEN RECORDS:
  Football (dual fan token fixtures):
    Both teams with active Chiliz Chain fan tokens — highest value record.
    Check fantokens.com for active tokens: $AFC, $SPURS, $CITY, $PSG,
    $BAR, $ATM, $JUV, $NAP, $GAL, $TRA and others.
    Key modifiers: derby_active, competition_tier_weight, burn_to_glory

  MMA:
    $UFC and $PFL are confirmed active Chiliz Chain fan token partners.
    Any UFC Fight Night, PPV, or PFL card main event qualifies as a
    fan token calibration record.

  Football (single fan token):
    One team has an active fan token, the other does not.
    Valid fan token record — validates one-sided fan token intelligence.

SPORT INTELLIGENCE LAYER (no fan token required):
  Cricket: IPL, T20WC qualifiers, PSL
    Key modifiers: dew_factor, india_pakistan
  Formula 1: qualifying + race (street circuits especially)
    Key modifiers: qualifying_delta
  Any underrepresented sport: rowing, netball, kabaddi, handball
    Any records from these sports are firsts and highly valued

RECORD FORMAT:
  Submit as .md files using community/calibration-data/TEMPLATE.md
  Records go in community/calibration-data/{sport}/
```

---

*MIT License · SportMind · sportmind.dev*
*Contribute: [FIRST-RECORD-CHALLENGE.md](../FIRST-RECORD-CHALLENGE.md)*
