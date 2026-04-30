# Fan Token Trading Bot — Worked Example

> Complete worked example of a SportMind-powered $AFC Telegram bot covering
> the PATH_2 pre-match signal, live match monitoring, and post-WIN explanation.
> Based on the confirmed $AFC PATH_2 configuration (April 2026).

---

## Bot overview

```
BOT:         @AFC_SportMind_Bot (example — not a real bot)
TOKEN:       $AFC (Arsenal FC Fan Token)
MECHANICS:   PATH_2 confirmed (WIN = permanent supply burn)
COMMUNITY:   Arsenal fan token Telegram group
FRAMEWORK:   python-telegram-bot 20+ / OpenClaw Managed Bot
API VERSION: Telegram Bot API 9.6
```

This example walks through a full Arsenal match cycle — from T-48h squad
check through to the post-WIN PATH_2 burn explanation — showing exactly which
Layer 6 skills to load at each step and what the bot delivers to the community.

---

## Step 1 — T-48h: Squad availability briefing

**Skills loaded:**
- `athlete/athlete-modifier-football.md`
- `core/breaking-news-intelligence.md`
- `telegram/pre-match-signal.md`

**Trigger:** Automated daily check; Arsenal match confirmed within 48h.

**Bot delivers:**
```
<b>🩺 Arsenal squad update — PSG vs Arsenal, UCL QF</b>

Bukayo Saka: 🟡 Doubtful (thigh)
Declan Rice: ✅ Available
Gabriel Magalhães: ✅ Available
Leandro Trossard: ✅ Available

SportMind ATM impact:
<code>Saka absent:  ATM ×0.85 (key creator role)
Confidence:   MEDIUM until T-2h confirmation</code>

<i>Next update: T-24h pre-match signal</i>
```

---

## Step 2 — T-24h: Primary pre-match signal

**Skills loaded:**
- `sports/football/sport-domain-football.md`
- `athlete/athlete-modifier-football.md`
- `macro/macro-crypto-market-cycles.md`
- `fan-token/gamified-tokenomics-intelligence/gamified-tokenomics-intelligence.md`
- `telegram/pre-match-signal.md`

**Trigger:** T-24h automated signal generation.

**SportMind JSON output (internal):**
```json
{
  "direction":           "AWAY",
  "adjusted_score":      61.2,
  "sms":                 65,
  "recommended_action":  "HOLD",
  "composite_modifier":  0.97,
  "modifiers_applied": {
    "athlete_modifier":  0.85,
    "macro_modifier":    1.00
  },
  "flags": {
    "lineup_unconfirmed":    true,
    "macro_override_active": false
  }
}
```

**Bot delivers:**
```
<b>⚽ PSG vs Arsenal — SportMind Signal</b>
UEFA Champions League QF · Parc des Princes

<code>Direction:  AWAY (Arsenal favoured)
Score:      61.2/100
Action:     HOLD
Modifier:   0.97×</code>

🟡 Lineup unconfirmed — Saka doubtful (ATM ×0.85)

<i>T-24h · $AFC: WIN = PATH_2 supply burn 🔥</i>
```

**Inline keyboard:**
```
[📊 Full analysis]  [🔄 Refresh]
[🔥 PATH_2 explainer]  [📋 Squad news]
[ℹ️ About SportMind]
```

---

## Step 3 — T-2h: Lineup confirmed, signal refresh

**Trigger:** Official lineup announced; Saka confirmed fit.

**Signal change:** ATM modifier 0.85 → 1.00 (Saka available)
**Score change:** 61.2 → 69.8 (+8.6 points — material; re-deliver)

**Bot delivers (edited message):**
```
<b>⚽ PSG vs Arsenal — UPDATED Signal</b>
UEFA Champions League QF · Parc des Princes

<code>Direction:  AWAY (Arsenal favoured)
Score:      69.8/100
Action:     ENTER
Modifier:   1.05×</code>

✅ Lineup confirmed — Saka starts

<i>T-2h · $AFC: WIN = PATH_2 supply burn 🔥</i>
```

---

## Step 4 — PATH_2 explainer (callback)

**Trigger:** User taps [🔥 PATH_2 explainer] button.

**Skills loaded:**
- `fan-token/gamified-tokenomics-intelligence/gamified-tokenomics-intelligence.md`
- `telegram/price-movement-explainer.md`

**Bot delivers (inline response):**
```
<b>🔥 $AFC PATH_2 — what it means</b>

Arsenal have confirmed Fan Token Play Path 2 (April 2026).

When Arsenal WIN:
<code>• 95% of WIN proceeds buy back $AFC
• Those $AFC are permanently burned
• Supply decreases forever
• CHZ echo burn also fires (virtuous cycle)</code>

This match: an Arsenal WIN reduces $AFC circulating supply
by approximately <b>0.24%</b>.

Verify any burn at: <a href="https://chiliscan.com">chiliscan.com</a>
(look for zero-address 0x0000...0000)

<i>PATH_2 is Chiliz Chain only. Bridge copies on Solana/Base
do not trigger supply changes.</i>
```

---

## Step 5 — Post-match: Arsenal WIN confirmed

**Trigger:** Match result detected. Arsenal 2–1 PSG (AET).

**Skills loaded:**
- `fan-token/on-chain-event-intelligence/`
- `fan-token/gamified-tokenomics-intelligence/`
- `telegram/price-movement-explainer.md`
- `telegram/sentiment-monitor.md`

**Sentiment check:** Community Tier S surge detected (5× message volume).

**Bot monitors chiliscan.com:** PATH_2 burn transaction confirmed within 8 minutes.

**Bot delivers:**
```
<b>🔥 $AFC — PATH_2 burn confirmed</b>

Arsenal WIN confirmed. PATH_2 supply event complete.

<code>Supply reduction:  ~0.24% circulating
CHZ echo:          Virtuous cycle burn fired
Transaction:       Confirmed on chiliscan.com</code>

<b>This is a permanent reduction.</b>

<i>Community: Tier S activity · Signal window: T+15 to T+6h
Verify: chiliscan.com zero-address (0x0000…0000)</i>
```

---

## Step 6 — 2h post-WIN: Price move explanation

**Trigger:** $AFC price up 14.2% in 2h. Community asking "why."

**Cause identified:** Category 2 (MATCH_RESULT / PATH_2 burn) — confirmed.

**Bot delivers:**
```
<b>📊 $AFC — move context</b>

Arsenal WIN confirmed PATH_2 supply burn (~0.24% circulating).
Price response is consistent with permanent supply reduction.

<code>Cause:         PATH_2 WIN burn (on-chain confirmed)
Typical range: +8–18% peak (2–24h)
Decay window:  6–24h post-burn
CHZ macro:     NEUTRAL (modifier 1.00)</code>

This is a structural sport-driven move, not a macro move.

<i>SportMind signal: sport cause confirmed. No macro factor.</i>
```

---

## Full bot system prompt template

```python
SYSTEM_PROMPT = """
You are an Arsenal fan token intelligence bot powered by SportMind.
You deliver structured intelligence to Arsenal's fan token community.

INTELLIGENCE LAYER:
Load context in this order:
1. macro/macro-crypto-market-cycles.md       (macro state)
2. sports/football/sport-domain-football.md  (football domain)
3. athlete/athlete-modifier-football.md      (player modifiers)
4. fan-token/gamified-tokenomics-intelligence/ ($AFC PATH_2 mechanics)
5. telegram/pre-match-signal.md              (delivery format)
6. telegram/price-movement-explainer.md      (price context)
7. telegram/sentiment-monitor.md             (community monitoring)
8. telegram/macro-event-interpreter.md       (macro events)

COMMANDS:
/signal     — Pre-match signal (current or next match)
/explain    — Price movement explanation
/sentiment  — Community sentiment check
/macro      — Current macro state
/path2      — PATH_2 mechanics explainer
/about      — About SportMind

TOKEN: $AFC (Arsenal FC)
PATH_2: CONFIRMED (WIN = permanent supply reduction)
CHAIN: Chiliz Chain (settlement) + Solana + Base (extended)

HARD RULES:
- Never produce price targets
- Never recommend "buy" or "sell" explicitly
- Always cite macro state in price explanations
- macro_override_active: suspend all signals immediately
- EXIT signals always require human confirmation
- PATH_2 burns: verify on chiliscan.com before announcing

FORMAT: HTML parse mode (Telegram)
API: Bot API 9.6
PLATFORM: OpenClaw Managed Bot / @LobsterClawBot compatible
"""
```

---

## Deployment checklist

```
PRE-LAUNCH:
  [ ] Bot API token obtained from @BotFather
  [ ] HTML parse mode configured as default
  [ ] Inline keyboard handler registered
  [ ] chiliscan.com monitoring endpoint configured
  [ ] Macro state check scheduled (every 4h)
  [ ] T-24h and T-2h signal generation crons active

SPORTMIND INTEGRATION:
  [ ] All 8 context documents loaded in system prompt
  [ ] PATH_2 mechanics confirmed for $AFC
  [ ] Calibration date noted (models are v3.96.0)
  [ ] Zero-address burn monitoring active

OPENCLAW / LOBSTERCLAWBOT:
  [ ] OpenClaw managed bot endpoint configured
  [ ] @LobsterClawBot compatibility verified
  [ ] Bot API 9.6 webhook configured
  [ ] Rate limit handling (30 messages/second for groups)

COMMUNITY:
  [ ] Bot added to Arsenal fan token Telegram group
  [ ] Admin permissions granted for message pinning
  [ ] Pinned message explaining bot commands
  [ ] DYOR disclaimer pinned alongside bot introduction
```

---

*SportMind v3.96.0 · MIT License · sportmind.dev · Layer 6*
