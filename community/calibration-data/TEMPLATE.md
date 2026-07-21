# Calibration Record Template

Use this template when submitting a calibration record to SportMind.
Copy the block below and fill in every field before submitting as a GitHub Issue or PR.

Two record types:
- **Fan token record** — at least one team has an active, verified Chiliz Chain fan token
- **Sport intelligence layer record** — no fan token; validates SportMind's sport intelligence layer

For fan token status verification: [fantokens.com](https://fantokens.com) ·
[socios.com](https://socios.com) · [chiliscan.com](https://chiliscan.com)

See [FIRST-RECORD-GUIDE.md](../../FIRST-RECORD-GUIDE.md) for full submission instructions.

---

## Record

```
Event:            [Team A / Fighter A] vs [Team B / Fighter B]
Competition:      [League / Tournament / Promotion / Event]
Venue:            [Stadium or Arena, City, Country]
Date:             [YYYY-MM-DD]
Kickoff / Start:  [HH:MM UTC]

FAN TOKEN STATUS:
  Home team:      [Active ($TICKER) · Chiliz Chain verified] or [None]
  Away team:      [Active ($TICKER) · Chiliz Chain verified] or [None]
  Record type:    [Fan token record — dual] or [Fan token record — one-sided] or [Sport intelligence layer record]
  Verified via:   [fantokens.com / socios.com / chiliscan.com — state which]

LLM / PATH:
  Option:         [Option A — any LLM] or [Option B — MCP server, Claude Desktop]
  LLM used:       [Claude / GPT-4 / Gemini / Groq / Mistral / other]
  Library version:[vX.X.X — shown in output, or "unknown"]

PRE-MATCH SIGNAL:
  Direction:      [HOME / AWAY / DRAW]
  Confidence:     [LOW / MEDIUM / HIGH]
  Raw score:      [If shown in output — e.g. 55.0]
  Modifiers:      [Key modifiers applied — e.g. CHZ CAPITULATION ×0.70, Neutral venue]
  Key signals:    [1-3 lines — what drove the direction call]

[Paste full pre-match output below this line]


RESULT (complete after match):
  Score:          [Team A] [X] — [Y] [Team B] ([90 min] / [AET] / [Pens])
  Direction:      [CORRECT] or [INCORRECT]
  
ROOT CAUSE NOTE (required if INCORRECT — leave blank if CORRECT):
  [What signal or modifier was weighted incorrectly?
   What was missed or over-weighted?
   This note is as valuable as a correct record.]
```

---

*SportMind · MIT License · [github.com/SportMind/SportMind](https://github.com/SportMind/SportMind)*
