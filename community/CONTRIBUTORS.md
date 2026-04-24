# Community Contributor Recognition

**How SportMind recognises, tracks, and celebrates community contributors
who submit calibration records, translations, skill improvements, and
application examples.**

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

```markdown
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
STEP 1 — Pick an upcoming match (any sport SportMind covers)
  Best: a match where you can run a full signal analysis 2-4 hours before

STEP 2 — Run SportMind analysis before the match
  Load the appropriate skill stack for your sport
  Generate a signal with SMS, direction, key modifiers
  Record your analysis output (screenshot or copy-paste is fine)

STEP 3 — Watch the match result

STEP 4 — Fill in the outcome record template
  Template: community/calibration-data/CONTRIBUTING.md
  The key fields:
    recorded_at: the time you ran your analysis (BEFORE the match)
    submitted_by: your GitHub handle or identifier
    direction_correct: was your direction prediction right?
    key_modifier_validated: which modifier were you testing?
    notes: what did you learn? (honest; wrong-direction records valued equally)

STEP 5 — Submit via GitHub PR
  Target path: community/calibration-data/{sport}/{year}/{month}/
  File name: {sport}-{event-description}-{date}-outcome.json
  Or open a GitHub Issue with the "calibration-submission" label (we handle the PR for you)

STEP 6 — Get credited
  Your handle appears in the record and in CONTRIBUTORS.md
  
Most important rule: the analysis must be run BEFORE the match.
Records submitted after knowing the outcome are not calibration records.
```

---

## Recognition for the first external contributors

The first 10 external contributors to submit calibration records will receive:

1. Permanent credit in CONTRIBUTORS.md with a "Founding Calibrator" notation
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
HIGHEST PRIORITY (most tokens, most commercial relevance):
  Football: EPL, La Liga, UCL, international qualifiers
    Modifiers most needing records: derby_active (need 47 more)
    
  Cricket: IPL, T20WC qualifiers, PSL
    Modifiers: dew_factor (need 47 more), india_pakistan (need 48 more)
    
  Basketball: NBA regular season, EuroLeague group stage
    Modifiers: playoff_modifier (need 47 more)
    
  Formula 1: qualifying + race (street circuits especially)
    Modifiers: qualifying_delta (need 46 more street circuit records)

GROWING PRIORITY (new sports in library):
  MotoGP, Athletics, Swimming, Winter sports
    Any records from these sports are firsts and highly valued
    
COMMUNITY RECORD FORMAT NOTE:
  Records for common modifiers (athlete_modifier, competition_tier_weight)
  are valuable even if those modifiers perform well — confirming accuracy
  is as important as finding errors.
```

---

*MIT License · SportMind · sportmind.dev*
*Contribute: github.com/sportmind/sportmind/blob/main/community/calibration-data/CONTRIBUTING.md*
