# First Record Guide

No coding required. No experience needed.
A prediction before a match. A result after. That's it.

SportMind is an open-source sports intelligence library for AI agents —
MIT licensed, community-calibrated. Every record you submit is a permanent
part of the calibration base, publicly verifiable on GitHub.

[sportmind.dev](https://sportmind.dev) · [sportmind.dev/first-record/](https://sportmind.dev/first-record/)

---

## What makes a valid record

SportMind has two record types. Know which one you are submitting.

### Fan token record (primary)
At least one team in the match has an active, verified fan token on Chiliz Chain.
This is the primary calibration target — SportMind is built for fan token intelligence.

**How to verify fan token status:**
- Check [fantokens.com](https://fantokens.com) or [socios.com](https://socios.com)
- Confirm on-chain via [chiliscan.com](https://chiliscan.com)
- Cross-check across at least two sources

**Black logo signal:**
If a token logo has turned black or greyscale on fantokens.com, socios.com, or
chiliscan.com, treat this as a potential indicator of a terminated or dormant
partnership. Do not assume active status. Verify before submitting.

### Sport intelligence layer record
Neither team has a fan token. Records from football, MMA, cricket, basketball,
and other sports. These validate SportMind's sport intelligence layer —
not fan token mechanics. Submit in the correct sport subdirectory under
`community/calibration-data/`.

---

## Step 1 — Get the pre-match prediction

Two paths. Choose one. Both produce a valid record.

### Option A — Any LLM (zero setup)

Works with Claude, GPT-4, Gemini, Groq, Mistral, or any capable LLM.

1. Go to [sportmind.dev/first-record/](https://sportmind.dev/first-record/)
2. Copy the SportMind quickstart prompt (clearly marked on the page)
3. Paste into a new chat with any LLM
4. Run: `SportMind pre-match analysis — [Team A] vs [Team B], [Competition], [Date]`
5. Record the DIRECTION and CONFIDENCE from the output

The quickstart prompt loads `core/sportmind-purpose-and-context.md` — the
canonical SportMind context file. No API key, no installation required.

### Option B — MCP server (Claude Desktop)

Requires Claude Desktop with SportMind MCP server configured.
See [MCP-SERVER.md](MCP-SERVER.md) for setup instructions.

1. Open Claude Desktop with SportMind MCP connected
2. Run: `sportmind_pre_match` for [Team A] vs [Team B], [Competition], [Date]
3. Record the full pre-match output — DIRECTION, CONFIDENCE, all modifiers

Option B gives the full structured output with modifier stack, fan token
status, and verifiable source chain. Preferred for fan token records.

---

## Step 2 — Submit before kickoff

1. Go to [github.com/SportMind/SportMind](https://github.com/SportMind/SportMind)
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
5. Submit the issue **before kickoff** — timestamp is everything

---

## Step 3 — Submit the result

After the match:

1. Comment on your issue with the final result
2. State whether direction was CORRECT or INCORRECT
3. If INCORRECT — include a root cause note: what signal or modifier
   was weighted incorrectly? This is as valuable as a correct record.

Use the template in `community/calibration-data/TEMPLATE.md` to format
your submission correctly.

---

## Record template

Use this format when submitting your calibration record as a GitHub Issue or PR:

```
Event:           [Team A] vs [Team B]
Competition:     [League / Tournament / Event]
Date:            [YYYY-MM-DD]
Fan Token Status: [Active ($TICKER) · Chiliz Chain verified] or [None — sport intelligence record]
Record Type:     [Fan token record] or [Sport intelligence layer record]
LLM / Path:      [Claude (Option A)] or [MCP server via Claude Desktop (Option B)]

PRE-MATCH:
Direction:       [HOME / AWAY / DRAW]
Confidence:      [LOW / MEDIUM / HIGH]
Key signals:     [Brief summary — 1-3 lines]

RESULT:
Outcome:         [Team A score] — [Team B score] ([90 min / AET / Pens])
Direction:       [CORRECT / INCORRECT]
Root cause note: [If incorrect — what was missed? If correct — leave blank or note key signal]
```

---

## Suggested matches

### Dual fan token football (highest value)

Both teams have active, verified Chiliz Chain fan tokens. These are the
primary calibration target for SportMind fan token intelligence.

Active fan token clubs to look for in fixtures:
`$AFC` · `$SPURS` · `$CITY` · `$PSG` · `$BAR` · `$ATM` · `$JUV` · `$NAP` · `$GAL` · `$TRA` · `$INTER` · and others

Check fixture calendars for matchups where both teams appear on [fantokens.com](https://fantokens.com).

### MMA — fan token confirmed

Both $UFC and $PFL are confirmed active Chiliz Chain fan token partners.
Any UFC or PFL event produces a valid fan token record.
MMA records go in `community/calibration-data/mma/`.

### Single fan token match

One team has an active fan token, the other does not.
Still a valid fan token record — validates one-sided fan token intelligence.
Mark as one-sided record in the Fan Token Status field.

### Sport intelligence layer

Any match from football, cricket, basketball, tennis, Formula 1, rugby,
or other sports in the library. No fan token required.
Submit in the correct sport subdirectory under `community/calibration-data/`.

---

## Founding Calibrators

The first 10 contributors to submit verified calibration records
earn permanent recognition as Founding Calibrators.

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

8 slots remaining. Your record could be next.

---

## Resources

- [sportmind.dev/first-record/](https://sportmind.dev/first-record/) — quickstart prompt + live leaderboard
- [fantokens.com](https://fantokens.com) — fan token status and prices
- [socios.com](https://socios.com) — fan token platform and token list
- [chiliscan.com](https://chiliscan.com) — on-chain verification
- [QUICKSTART.md](QUICKSTART.md) — Option A full setup guide
- [MCP-SERVER.md](MCP-SERVER.md) — Option B MCP server setup
- [community/calibration-data/TEMPLATE.md](community/calibration-data/TEMPLATE.md) — record template

---

*SportMind · MIT License · [github.com/SportMind/SportMind](https://github.com/SportMind/SportMind)*
