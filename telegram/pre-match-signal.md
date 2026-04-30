# Telegram Pre-Match Signal — SportMind Layer 6

> Formats SportMind pre-match intelligence as Telegram-ready messages.
> Covers message structure, timing windows, inline keyboard layout,
> and the front-running signal pattern for fan token holders.

---

## Overview

Pre-match signals are the highest-frequency use case for a SportMind Telegram
bot. This skill translates the JSON output from Layers 1–3 into formatted
Telegram messages with correct timing, appropriate confidence language, and
actionable context for fan token holders.

```
PRE-MATCH SIGNAL TIMELINE (standard):

  T-48h:  Squad availability check — deliver availability briefing
  T-24h:  Primary signal generated — deliver to channel
  T-6h:   Macro gate confirmation — re-deliver if modifier changed
  T-2h:   Final lineup check — update or confirm signal
  T-0:    Kickoff — no new signals; community mode
  T+1h:   Post-match update — result + token impact

  Front-running window: T-6h to T-2h is the highest-signal delivery window.
  Community signal volume peaks in this window. Delivery here has maximum reach.
```

---

## Pre-match message format

### Standard pre-match signal

```
FORMAT:
<b>⚽ {MATCH} — SportMind Signal</b>
{COMPETITION} · {VENUE}

<code>Direction:  {DIRECTION}
Score:      {SCORE}/100
Action:     {RECOMMENDED_ACTION}
Modifier:   {COMPOSITE_MODIFIER}×</code>

{FLAG_LINE}

<i>T-{HOURS}h · {TOKEN} holders: {APPLICABLE_NOTE}</i>
```

Example output:
```
<b>⚽ PSG vs Arsenal — SportMind Signal</b>
UEFA Champions League · Parc des Princes

<code>Direction:  HOME
Score:      72.4/100
Action:     ENTER
Modifier:   1.10×</code>

🟡 Lineup unconfirmed — Saka doubtful

<i>T-6h · $AFC holders: WIN = PATH_2 supply event</i>
```

### Condensed (for high-frequency channels)

```
FORMAT:
<b>{TOKEN}</b> · {COMPETITION} · T-{H}h
<code>{DIRECTION} {SCORE}/100 · {ACTION}</code>
{PATH2_NOTE_IF_APPLICABLE}
```

### Squad availability briefing (T-48h)

```
FORMAT:
<b>🩺 {CLUB} squad update — {MATCH}</b>

{PLAYER_1}: {STATUS}
{PLAYER_2}: {STATUS}
{PLAYER_3}: {STATUS}

SportMind ATM impact:
<code>{ATM_SUMMARY}</code>

<i>Next update: T-24h signal</i>
```

---

## Flag formatting

```
FLAG DISPLAY RULES:
  lineup_unconfirmed:    🟡 Lineup unconfirmed — check T-2h update
  macro_override_active: 🔴 Macro override active — signal paused
  injury_flag:           🩺 {PLAYER} availability uncertain
  high_importance:       ⭐ High-importance match — elevated modifier
  path2_active:          🔥 WIN = PATH_2 supply burn
  wc2026_active:         🌍 WC2026 NCSI active — {NCSI_MULTIPLIER}×

  RULE: Show maximum 3 flags per message.
        If macro_override_active — show only this flag; suppress all others.
        Signal is paused; no further detail needed.
```

---

## Front-running signal pattern

```
FRONT-RUNNING INTELLIGENCE:
  Fan token price moves anticipate match outcomes.
  The most reliable pre-match signal for Telegram delivery is the T-6h to T-2h
  window — when lineup confirmation typically arrives and community volume surges.

  FRONT-RUNNING SEQUENCE:
    T-6h:  SportMind score calculated with partial lineup data
    T-2h:  Lineup confirmed → full ATM modifier applied
           Signal delta (T-6h vs T-2h) is the front-running indicator
           If delta >5 points: material new information; re-deliver
           If delta ≤5 points: confirmation; no re-delivery needed

  FOR PATH_2 TOKENS ($AFC and confirmed PATH_2 clubs):
    The front-running signal is more pronounced:
    Pre-WIN accumulation is a known pattern (holders accumulate before wins)
    Do not amplify this signal in public — it creates circular dynamics
    Deliver the neutral signal; do not speculate on pre-match accumulation

  AGENT RULE:
    The pre-match signal is intelligence, not a trading recommendation.
    Language: "SportMind signals {DIRECTION}" — not "buy before the match"
    Never produce language that implies guaranteed profit
```

---

## Inline keyboard layout

```
RECOMMENDED INLINE KEYBOARD (for pre-match messages):

Row 1: [📊 Full analysis] [🔄 Refresh]
Row 2: [🔥 PATH_2 explainer] [📋 Squad news]    (only if PATH_2 token)
Row 2: [📋 Squad news] [📈 Token chart]          (for non-PATH_2 tokens)
Row 3: [ℹ️ About SportMind]

CALLBACK DATA FORMAT:
  full_analysis:{TOKEN}:{MATCH_ID}
  refresh_signal:{TOKEN}:{MATCH_ID}
  path2_explainer:{TOKEN}
  squad_news:{TOKEN}:{MATCH_ID}
  about_sportmind

BUTTON LABELS: max 20 characters per button
```

---

## Sport-specific delivery notes

```
FOOTBALL:
  UCL/UEL/UECL matches: include competition tier in header
  El Clásico / Der Klassiker / Derby della Madonnina: add ⭐ flag
  PATH_2 tokens: always include PATH_2 line even at HOLD signal
  WC2026 (June 11 – July 19, 2026): include NCSI multiplier

FORMULA 1:
  Race weekend: deliver qualifying signal (Friday) + race signal (Sunday)
  Qualifying signal includes circuit type modifier
  Constructor token holders: note constructor standings context

MMA:
  Weight cut signal: deliver at weigh-in result (T-20h)
  Title fight: elevated modifier; note in header
  Retirement risk tokens: CRI score as context

CRICKET:
  Evening match (>20:00 local) + humidity >70%: note dew protocol active
  IPL tokens: include format weight
  India/Pakistan: dual output — $IND and $PAK signals separately
```

---

## Timing automation

```
RECOMMENDED SCHEDULE (cron-style, for bot runtime):

  # Squad availability briefing
  0 10 * * *  python bot.py --signal squad_check --window T-48h

  # Primary pre-match signal
  0 8 * * *   python bot.py --signal pre_match --window T-24h

  # Macro gate check + signal refresh
  0 */4 * * * python bot.py --signal macro_check

  # Final lineup confirmation
  */30 * * * * python bot.py --signal lineup_check --window T-2h

  # WC2026 intensive (June 11 – July 19, 2026)
  # Set WC2026_ACTIVE=true in environment
  0 * * * *   python bot.py --signal wc2026 --all-tokens
```

---

## Autonomous Execution

**Trigger conditions:**
- T-24h before any match involving a monitored token
- Lineup confirmation received (changes ATM modifier by >5 points)
- Macro modifier changes by >0.05 since last signal delivery
- PATH_2 burn confirmed post-match

**Level 2 actions (no human required):**
- Generate pre-match signal from Layers 1–3
- Format as Telegram message using appropriate template
- Stage for delivery (do not yet send)

**Level 3 actions (operator confirmation):**
- Send to configured channel
- Pin message in channel if T-2h or closer

**Hard boundaries:**
- macro_override_active = no delivery at any autonomy level
- Never pin a message automatically without operator confirmation
- Never include specific price targets or "guaranteed" language
- WC2026 national token signals: human review if NCSI >×3.0

---

## Compatibility

**Bot API:** Telegram Bot API 9.6
**OpenClaw:** Maps to `/signal` command output format
**@LobsterClawBot:** Primary delivery skill for pre-match intelligence
**Inline keyboards:** Bot API 9.6 InlineKeyboardMarkup compatible

---

## Related skills

- `telegram/sentiment-monitor.md` — community context pre-delivery
- `telegram/price-movement-explainer.md` — post-match follow-up
- `fan-token/gamified-tokenomics-intelligence/` — PATH_2 mechanics
- `fan-token/world-cup-2026-intelligence/world-cup-2026-pre-tournament.md`

---

*SportMind v3.96.0 · MIT License · sportmind.dev · Layer 6*
