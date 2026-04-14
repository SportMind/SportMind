# The First Record Challenge

**Submit one calibration record from a real match you analysed.
Get permanently recognised as a Founding Calibrator.**

This is the most direct way to improve SportMind — and the easiest
contribution anyone can make regardless of technical background.

---

## What is a calibration record?

When you use SportMind to analyse a match *before it happens*, then record
whether the prediction was correct, you have created a calibration record.

That's it. You do not need to write code. You do not need to open a pull
request yourself (email works too). You just need to:

1. Run a SportMind analysis before a match
2. Watch the match
3. Fill in the template below
4. Submit it

---

## Why this matters

SportMind has 126 validated calibration records. All 126 were submitted by
the founding team from carefully selected historical events. That means the
library's modifiers have been validated by one team, not by a community.

Every external record changes that. When you submit a record from a match
you actually analysed — not one chosen because we knew the outcome — the
library gets evidence that reflects how real practitioners use it. That is
categorically more valuable than the same number of seed records.

The first 10 external contributors get permanent Founding Calibrator
recognition in CONTRIBUTORS.md, in the CHANGELOG entry for the version
their record appears in, and in the next recalibration report that uses
their records to update modifier values.

That recognition does not expire. When SportMind is deployed in production
systems, those names are in the library's permanent history.

---

## Step-by-step: your first record in 30 minutes

### Step 1 — Pick an upcoming match (5 minutes)

Find a match happening in the next 24-48 hours in any sport SportMind covers:
football, cricket, basketball, MMA, Formula 1, tennis, hockey, rugby —
any of the 19 sports with calibration records already, or any of the 42
sport domains in the library.

The match should be:
- Real (any league or competition is fine)
- Happening in the future when you run your analysis
- One where you can find the official result afterwards

### Step 2 — Run a SportMind analysis (15 minutes)

Load the relevant sport skill into any LLM (Claude, GPT-4, Gemini — any works).
The minimum you need:

```
Paste into your LLM:
  1. Contents of core/sportmind-purpose-and-context.md
  2. Contents of sports/{sport}/sport-domain-{sport}.md
  
Then ask:
  "Using the SportMind framework, generate a pre-match signal for
   [Team A] vs [Team B] in [competition] on [date].
   Key context: [any relevant info you know — lineup, form, conditions]"
```

Record the output. Specifically note:
- The direction prediction (HOME / AWAY / DRAW)
- The SMS score (0-100)
- The key modifier applied
- The recommended action (ENTER / WAIT / ABSTAIN)
- The time you ran the analysis

**Critical rule: you must record your analysis BEFORE the match starts.**

### Step 3 — Watch the match and record the result

After the match, note:
- The actual result (home win / away win / draw)
- The final score
- Whether the direction was correct

### Step 4 — Fill in the template

Copy this template and fill it in. Do not worry about getting every field
perfect — the important fields are marked with *.

```json
{
  "outcome_record": {
    "record_id": "YOUR_SPORT-EVENT_NAME-DATE-001",
    "sport": "football",
    "event_id": "brief-event-identifier",
    "event_name": "Full match name — Team A vs Team B",
    "kickoff_utc": "2026-XX-XXTXX:XX:XXZ",
    "recorded_at": "2026-XX-XXTXX:XX:XXZ",
    "submitted_by": "@your_github_handle",
    "source": "community-record",

    "prediction": {
      "direction": "HOME",
      "adjusted_score": 67.4,
      "confidence_tier": "MEDIUM",
      "sportmind_score": 74,
      "pre_match_note": "What SportMind said and why"
    },

    "outcome": {
      "result": "HOME_WIN",
      "direction_correct": true,
      "final_score": "Team A 2 – Team B 1",
      "result_source_url": "https://link-to-official-result"
    },

    "calibration_flags": {
      "key_modifier_validated": "athlete_modifier",
      "modifier_direction_correct": true,
      "signal_was_actionable": true,
      "notes": "What you learned — honest assessment, even if wrong direction"
    }
  }
}
```

**Required fields (*):**
- `submitted_by` — your handle so you get credit
- `recorded_at` — when you ran the analysis (must be before kick-off)
- `direction` — what SportMind predicted
- `result` — what actually happened
- `direction_correct` — true or false
- `final_score` — official result
- `result_source_url` — link to verify the result
- `notes` — one honest sentence about what you learned

**Optional but valuable:**
- `adjusted_score` and `sportmind_score` — copy from your LLM output
- `key_modifier_validated` — which modifier were you testing?

### Step 5 — Submit

**Option A (GitHub Issue — recommended, no technical knowledge required):**
Open an issue with title: `[Calibration Record] {sport} — {match name}`
Paste your JSON in the issue body. That is the entire submission.
Automated checks run immediately. Human review within 30 days — most
records confirmed faster. You receive full credit via your GitHub handle.

**Option B (GitHub PR — if you are comfortable with git):**
1. Fork the repository
2. Save your record as:
   `community/calibration-data/{sport}/{year}/{month}/{your-record-filename}.json`
3. Open a pull request with label: `calibration-record`
4. Automated validation runs immediately. Merged within 30 days.

---

## Most wanted record types

These modifier types need the most community records:

| Modifier | Records needed | Easiest to submit |
|---|---|---|
| `athlete_modifier` (football) | 35 more to preliminary threshold | Any top league match |
| `dew_factor` (cricket evening T20) | 44 more | IPL, PSL, BBL night matches |
| `derby_active` | 48 more | Any league derby you follow |
| `competition_tier_weight` | 46 more | UCL group vs knockout stage |
| `qualifying_delta_modifier` (F1) | 47 more | Any F1 weekend |

Pick any sport you already watch. The record is more valuable when it comes
from someone who actually knows the sport, not from a database lookup.

---

## What wrong-direction records do

You might worry that submitting a wrong-direction prediction makes SportMind
look bad. The opposite is true.

Wrong-direction records are the library's most valuable contributions.
Every improvement to SportMind's protocols came from a wrong-direction record
being honestly documented. The derby draw premium, the post-tournament opener
flag, the two-legged tie Leg 1 protocol, the high-stakes symmetry flag —
all of these came from analysing wrong predictions. Zero wrong-direction
records would mean nothing was learned.

When you submit a wrong-direction record, you are telling the library:
"here is a situation where the framework got it wrong — here is the evidence."
That is how modifiers get better. Submit the honest result every time.

---

## Recognition you will receive

As a Founding Calibrator (first 10 external contributors):

- Your handle appears in `community/CONTRIBUTORS.md` under "Founding Calibrators"
  permanently — it will not be removed even if later contributors outrank you
- You are named in the CHANGELOG entry for the version your first record
  is included in
- When the recalibration report that first uses your records is published,
  your contribution is acknowledged by name
- You are listed in `WHO-WE-ARE.md` when it is updated to include the
  founding community

After the first 10, you still receive:
- Credit in every calibration record you submit
- CONTRIBUTORS.md listing by tier
- Named acknowledgement in recalibration reports using your records

---

## Questions

**"What if I'm not sure my analysis was done correctly?"**
Submit it anyway with honest notes. An imperfect record with honest documentation
of what you were uncertain about is more valuable than no record. The review
process will flag anything that cannot be used.

**"What if I don't have time to run a full SportMind analysis?"**
The minimum is: paste `core/sportmind-purpose-and-context.md` into Claude,
describe the match, and ask for a direction. That takes 5 minutes. Record the
direction prediction and the result. Even that minimal record contributes.

**"Can I submit multiple records?"**
Yes — there is no limit. Every record earns credit.

**"What sports count?"**
Any of the 42 sports in the library. The underrepresented ones (rowing, netball,
kabaddi, handball) are especially valuable since they have few or no records.

---

*The library improves with every record submitted.*
*MIT License · SportMind · sportmind.dev*
