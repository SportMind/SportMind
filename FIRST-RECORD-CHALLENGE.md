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
3. Fill in the template
4. Submit it

---

## Why this matters

SportMind has 137 validated calibration records. All were submitted by
the founding team from carefully selected historical events. That means the
library's modifiers have been validated by one team, not by a community.

Every external record changes that. When you submit a record from a match
you actually analysed — not one chosen because we knew the outcome — the
library gets evidence that reflects how real practitioners use it. That is
categorically more valuable than the same number of seed records.

The first 10 external contributors get permanent Founding Calibrator
recognition. **Two slots are already filled:**
- #1 @AltcoinDaddy — WC2026 Group Stage
- #2 @charan0318 — WC2026 Group Stage
- **8 slots remaining**

That recognition does not expire. When SportMind is deployed in production
systems, those names are in the library's permanent history.

---

## Fan token status — verify before you submit

If your match involves a fan token, verify active status before submitting.

- Check [fantokens.com](https://fantokens.com) and [socios.com](https://socios.com)
- Confirm on-chain at [chiliscan.com](https://chiliscan.com)
- Cross-check across at least two sources

**Black logo signal:** If a token logo has turned black or greyscale on
fantokens.com, socios.com, or chiliscan.com, treat this as a potential
indicator of a terminated or dormant partnership. Verify before submitting
as a fan token record.

---

## High-value record types

| Record type | Example | Why valuable |
|---|---|---|
| Dual fan token football | $AFC vs $SPURS, $PSG vs $BAR | Both fan tokens validated in one record |
| MMA fan token | UFC Fight Night main event, PFL card | $UFC and $PFL are confirmed active Chiliz partners |
| Single fan token football | $CITY vs non-token club | One-sided fan token intelligence validated |
| Sport intelligence layer | Any sport, no fan token required | Validates SportMind's sport domain layer |

---

## Step-by-step: your first record in 30 minutes

### Step 1 — Pick an upcoming match (5 minutes)

Find a match happening in the next 24-48 hours in any sport SportMind covers:
football, MMA, Formula 1, tennis, cricket, hockey, rugby —
any of the sport domains in the library.

The match should be:

- Real (any league or competition is fine)
- Happening in the future when you run your analysis
- One where you can find the official result afterwards

### Step 2 — Run a SportMind analysis (15 minutes)

Two paths. Choose one.

**Option A — Any LLM (zero setup)**

Works with Claude, GPT-4, Gemini, Groq, Mistral, or any capable LLM.

1. Go to [sportmind.dev/first-record/](https://sportmind.dev/first-record/)
2. Copy the SportMind quickstart prompt (clearly marked on the page)
3. Paste into a new chat with any LLM
4. Run: `SportMind pre-match analysis — [Team A] vs [Team B], [Competition], [Date]`
5. Record the DIRECTION and CONFIDENCE from the output

**Option B — MCP server (Claude Desktop)**

Requires Claude Desktop with SportMind MCP server configured.
See [MCP-SERVER.md](MCP-SERVER.md) for setup instructions.

1. Open Claude Desktop with SportMind MCP connected
2. Run: `sportmind_pre_match` for [Team A] vs [Team B], [Competition], [Date]
3. Record the full pre-match output — DIRECTION, CONFIDENCE, all modifiers

Record the output. Specifically note:

- The direction prediction:
  - **Fan token records:** LONG $TOKEN / SHORT $TOKEN / DRAW
  - **Sport intelligence records:** HOME / AWAY / DRAW
- The SportMind Score (0–100)
- The key modifier applied
- The time you ran the analysis

**Critical rule: you must record your analysis BEFORE the match starts.**

### Step 3 — Watch the match and record the result

After the match, note:

- The actual result (home win / away win / draw)
- The final score
- Whether the direction was correct

### Step 4 — Fill in the template

Use the template in `community/calibration-data/TEMPLATE.md`.
Submit as a `.md` file — not JSON.

Key fields:

- `submitted_by` — your handle so you get credit
- `recorded_at` — when you ran the analysis (must be before kick-off)
- `direction` — what SportMind predicted
- `result` — what actually happened
- `direction_correct` — CORRECT or INCORRECT
- `final_score` — official result
- `result_source_url` — link to verify the result
- `notes` — one honest sentence about what you learned

### Step 5 — Submit

**Option A (GitHub Issue — recommended):**
Open an issue with title: `Calibration Record — [Team A] vs [Team B] — [Competition] — [Date]`
Paste your completed template in the issue body. Human review within 30 days.

**Option B (GitHub PR):**

1. Fork the repository
2. Save your record as:
   `community/calibration-data/{sport}/{your-record-filename}.md`
3. Open a pull request with label: `calibration-record`

---

## Most wanted record types

These modifier types need the most community records:

| Modifier | Why valuable |
|---|---|
| `athlete_modifier` (football) | Any top league match with confirmed lineups |
| `dew_factor` (cricket evening T20) | IPL, PSL, BBL night matches |
| `derby_active` | Any league derby — highest CDI impact modifier |
| `competition_tier_weight` | UCL group vs knockout stage distinction |
| `qualifying_delta_modifier` (F1) | Any F1 weekend — qualifying + race |

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
all of these came from analysing wrong predictions.

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

After the first 10, you still receive:

- Credit in every calibration record you submit
- CONTRIBUTORS.md listing by tier
- Named acknowledgement in recalibration reports using your records

---

## Questions

**"What if I'm not sure my analysis was done correctly?"**
Submit it anyway with honest notes. An imperfect record with honest documentation
is more valuable than no record.

**"What if I don't have time to run a full SportMind analysis?"**
The minimum is: paste `core/sportmind-purpose-and-context.md` into any LLM,
describe the match, and ask for a direction. That takes 5 minutes. Record the
direction prediction and the result.

**"Can I submit multiple records?"**
Yes — there is no limit. Every record earns credit.

**"What sports count?"**
Any of the sport domains in the library. See [FIRST-RECORD-GUIDE.md](FIRST-RECORD-GUIDE.md)
for the full list of match types and fan token verification guidance.

---

*The library improves with every record submitted.*
*MIT License · SportMind · sportmind.dev*
