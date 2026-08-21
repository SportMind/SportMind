# First Record Guide

No coding required. No experience needed.
A prediction before a match. A result after. That's it.

SportMind is an open-source sports intelligence library for AI
agents — MIT licensed, community-calibrated. Every record you
submit is a permanent part of the calibration base, publicly
verifiable on GitHub.

[sportmind.dev](https://sportmind.dev) ·
[sportmind.dev/first-record/](https://sportmind.dev/first-record/)

---

## What makes a valid record

SportMind has two record types. Know which one you are submitting.

### Fan token record (primary)

At least one team in the match has an active, verified fan token
on Chiliz Chain. This is the primary calibration target —
SportMind is built for fan token intelligence.

**How to verify fan token status:**
- Check [fantokens.com](https://fantokens.com) or
  [socios.com](https://socios.com)
- Confirm on-chain via [chiliscan.com](https://chiliscan.com)
- Cross-check across at least two sources before submitting

**Black or greyscale logo signal:**
If a token logo has turned black or greyscale on fantokens.com,
socios.com, or chiliscan.com, treat this as a potential indicator
of a terminated or dormant partnership. Do not assume active
status. Verify before submitting.

### Sport intelligence layer record

Neither team has a fan token. Records from football, MMA,
cricket, basketball, and other sports. These validate
SportMind's sport intelligence layer — not fan token mechanics.
Submit in the correct sport subdirectory under
`community/calibration-data/`.

---

## Before you start — the HOLD gate

SportMind applies a HOLD gate to every analysis. If the adjusted
signal score falls below the entry threshold — which happens
frequently during the current CHZ CAPITULATION regime (×0.70
modifier active) — the output will say HOLD rather than
ENTER/BUY.

**A HOLD output is still a valid calibration record.**
Submit it. Record the HOLD as your direction. After the match,
note whether the HOLD was justified. This is as valuable as
a directional record.

Never force a direction from a HOLD output. Record what
SportMind actually produced.

---

## Step 1 — Get the pre-match prediction

Two paths. Choose one. Both produce a valid record.

### Option A — Any LLM (zero setup)

Works with Claude, GPT-4, Gemini, Groq, Mistral, or any
capable LLM. No API key or installation required.

1. Go to [sportmind.dev/start/](https://sportmind.dev/start/)
2. Copy the SportMind Welcome Prompt (clearly marked on the page)
3. Paste into a new chat with any LLM
4. Run: `SportMind pre-match analysis — [Team A] vs [Team B],
   [Competition], [Date]`
5. Record the DIRECTION (or HOLD) and CONFIDENCE from the output

The Welcome Prompt loads SportMind's core context file. No
setup, no account required.

### Option B — MCP server (Claude Desktop)

Requires Claude Desktop with SportMind MCP server configured.
See [MCP-SERVER.md](MCP-SERVER.md) for full setup instructions.

1. Open Claude Desktop with SportMind MCP connected
2. Run: `sportmind_pre_match` for [Team A] vs [Team B],
   [Competition], [Date]
3. Record the full pre-match output — DIRECTION or HOLD,
   CONFIDENCE, all modifiers

Option B gives the full structured output with complete modifier
stack, fan token status, and verifiable source chain.
Preferred for fan token records.

---

## Step 2 — Submit before kickoff

**Timing is everything.** The pre-match timestamp is what makes
a record valid. Submissions after kickoff are not accepted.

1. Go to
   [github.com/SportMind/SportMind](https://github.com/SportMind/SportMind)
2. Click **Issues → New issue**
3. Title format:

```
Calibration Record — [Team A] vs [Team B] — [Competition] — [Date]
```

For MMA, include both fighters:

```
Calibration Record — [Fighter A] vs [Fighter B] — [Promotion] — [Date]
```

4. Paste your full pre-match output into the issue body
5. Submit the issue **before kickoff** — this timestamp is
   your proof of pre-match submission

---

## Step 3 — Submit the result

After the match:

1. Comment on your issue with the final result
2. State whether direction was CORRECT, INCORRECT, or HOLD
   VALIDATED
3. If INCORRECT — include a root cause note: what signal or
   modifier was weighted incorrectly? This is as valuable as
   a correct record.
4. If HOLD — note whether the match outcome suggests the HOLD
   was justified (e.g. upset result, low-confidence fixture)

Use the template in
`community/calibration-data/CALIBRATION-RECORD-TEMPLATE.md`
to format your full submission correctly.

---

## Record template (quick format)

Use this format when submitting your calibration record as a
GitHub Issue. The full template with all 18 sections is in
`community/calibration-data/CALIBRATION-RECORD-TEMPLATE.md`.

```
Event: [Team A] vs [Team B]
Competition: [League / Tournament / Event]
Date: [YYYY-MM-DD]
Fan Token Status: [Active ($TICKER) · Chiliz Chain verified]
                  or [None — sport intelligence record]
Record Type: [Fan token record] or
             [Sport intelligence layer record]
LLM / Path: [Claude (Option A)] or
            [MCP server via Claude Desktop (Option B)]

PRE-MATCH:
Direction: [HOME / AWAY / DRAW / HOLD]
Confidence: [LOW / MEDIUM / HIGH]
Key signals: [Brief summary — 1-3 lines]
CHZ regime: [Current modifier — e.g. CAPITULATION ×0.70]

RESULT:
Outcome: [Score] ([90 min / AET / Pens])
Direction: [CORRECT / INCORRECT / HOLD VALIDATED]
Root cause note: [If incorrect — what was missed?
                  If HOLD — was it justified?
                  If correct — leave blank or note key signal]
```

---

## Suggested matches

### Dual fan token football (highest value)

Both teams have active, verified Chiliz Chain fan tokens.
These are the highest-value calibration records for SportMind
fan token intelligence.

Active fan token clubs to look for in fixtures:
`$AFC` · `$SPURS` · `$CITY` · `$AVL` · `$PSG` · `$ASM` ·
`$BAR` · `$ATM` · `$JUV` · `$ACM` · `$INTER` · `$NAP` ·
`$ASR` · `$BFC` · `$GAL` · `$TRA` · and others

Check fixture calendars for matchups where both teams appear
on [fantokens.com](https://fantokens.com). Dual fan token
matches are flagged automatically by Option B (MCP server).

### MMA — fan token confirmed

Both $UFC and $PFL are confirmed active Chiliz Chain fan token
partners. Any UFC or PFL event produces a valid fan token
record. MMA records go in `community/calibration-data/mma/`.

### Single fan token match

One team has an active fan token, the other does not.
Still a valid fan token record — validates one-sided fan token
demand intelligence. Mark as single-token record in the
Fan Token Status field.

### National token match

National team tokens ($SPAIN · $ARG · $POR · $SAFA · $SFA ·
$BELG and others) are active on Chiliz Chain. International
fixtures involving these tokens are valid fan token records
and may include PTG (Burn to Glory) supply event signals.
Note PTG eligibility in the Key signals field.

### Sport intelligence layer

Any match from football, cricket, basketball, tennis,
Formula 1, rugby, or other sports in the library.
No fan token required. Submit in the correct sport subdirectory
under `community/calibration-data/`.

---

## What to record for MMA

MMA records follow the same structure but use fighter names
instead of team names. A few MMA-specific notes:

- Weigh-in results (T-1 day) are the most important signal —
  if you submit before weigh-ins, note that in Key signals
- Card type matters: Numbered PPV · Fight Night · DWCS all
  have different signal weights
- $UFC and $PFL are separate tokens — record the correct ticker
- All MMA records go in `community/calibration-data/mma/`

---

## Founding Calibrators

The first 10 community contributors to submit verified
calibration records earn permanent recognition as
Founding Calibrators.

| Slot | Calibrator | Record |
|------|-----------|--------|
| #1 | @AltcoinDaddy | Mexico vs South Africa — WC2026 Group Stage |
| #2 | @charan0318 | Mexico vs South Africa — WC2026 Group Stage |
| #3 | — | Open |
| #4 | — | Open |
| #5 | — | Open |
| #6 | — | Open |
| #7 | — | Open |
| #8 | — | Open |
| #9 | — | Open |
| #10 | — | Open |

8 slots remaining. Submit a verified record to claim the next slot.

---

## Common mistakes to avoid

**Submitting after kickoff.** The timestamp is everything —
a post-kickoff submission is not a calibration record.

**Forcing a direction from a HOLD.** If SportMind says HOLD,
record HOLD. Do not reinterpret as a directional signal.

**Unverified fan token status.** Always confirm on chiliscan.com
before claiming a fan token record. A black or greyscale logo
on aggregators is a warning sign — verify independently.

**Wrong directory.** Football records go in
`community/calibration-data/football/`. MMA records go in
`community/calibration-data/mma/`. Other sports go in their
own subdirectory. Check before submitting.

**Named players in the record.** Do not include specific player
names in calibration records — use archetype descriptions
(e.g. "key midfielder absence" not a named player). This is
a standing library rule.

---

## Resources

- [sportmind.dev/start/](https://sportmind.dev/start/) —
  Welcome Prompt + onboarding guide
- [sportmind.dev/first-record/](https://sportmind.dev/first-record/) —
  live leaderboard and record tracker
- [fantokens.com](https://fantokens.com) — fan token status
  and prices
- [socios.com](https://socios.com) — fan token platform and
  token list
- [chiliscan.com](https://chiliscan.com) — on-chain verification
- [MCP-SERVER.md](MCP-SERVER.md) — Option B MCP server setup
- [community/calibration-data/CALIBRATION-RECORD-TEMPLATE.md](community/calibration-data/CALIBRATION-RECORD-TEMPLATE.md) —
  full 18-section record template

---

*SportMind · MIT License ·
[github.com/SportMind/SportMind](https://github.com/SportMind/SportMind)*
