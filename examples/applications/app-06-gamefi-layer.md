# App 6 — Sports GameFi Intelligence Layer

**A SportMind intelligence layer for on-chain sports games — using adjusted_score
and SMS to create game mechanics that reward genuine sports knowledge rather than
statistical advantage, with on-chain settlement via Azuro or Chiliz Chain.**

---

## The problem this solves

Most on-chain sports games (fantasy leagues, prediction games, pick'em contests)
use raw statistics as their intelligence layer. Points are scored for goals, assists,
and clean sheets — metrics that any casual fan can access from any statistics website.
There is no proprietary intelligence in the product; the game is purely about who
collects the most data points fastest.

SportMind-powered GameFi changes the game mechanic fundamentally. Instead of rewarding
data collection, it rewards contextual reasoning — understanding *why* a player or team
is likely to perform, not just *what* their statistics say.

A player with a PQS 5 pitcher start in MLB has a genuine signal behind them. A manager
who understands that the State of Origin has depleted Penrith's squad this week has an
information advantage that goes beyond raw data. A participant who checks the macro_modifier
before adding fan tokens to their fantasy portfolio is doing something no existing
fantasy sports product enables.

---

## Target users

**Primary:** Sports fans who want to engage with on-chain sports games that reward
genuine domain knowledge, not just statistics literacy.

**Secondary:** GameFi developers building sports-adjacent applications who want
to differentiate their intelligence layer from competitors.

**Tertiary:** Fan token platforms looking to add a gamified engagement layer to
their existing token ecosystem.

---

## Core value proposition

> *"The first on-chain sports game where your SportMind Score matters. If you load
> better intelligence than your opponents, you make better picks — and the game
> recognises the quality of your analysis, not just whether you got lucky."*

The SMS (SportMind Score) is the game mechanic innovation. Rather than all picks
having equal weight, a pick backed by SMS 85 intelligence carries more confidence
weight than a pick backed by SMS 47. Players who use better intelligence — loading
more layers, checking macro state, verifying lineups — are rewarded for the quality
of their analysis process, not just whether their prediction was correct.

---

## SportMind skill stack

```
GAME INTELLIGENCE STACK (multi-sport):

BASE STACK (required for every pick):

1. macro/macro-overview.md
   → Current macro phase — affects all token-denominated scoring
   → macro_modifier: applied to all fantasy points in token games

2. sports/{sport}/sport-domain-{sport}.md
   → Event playbook for this match type
   → Competition tier weight (finals vs regular season)
   → Sport-specific risk variables

3. athlete/{sport}/athlete-intel-{sport}.md
   → Player availability (lineup_unconfirmed flag)
   → Form score for pick scoring weight
   → Composite modifier for the player

4. core/sportmind-score.md
   → SMS calculation for the pick
   → SMS becomes the confidence weight for scoring

EXTENDED STACK (for token-denominated games):

5. fan-token/{sport}-token-intelligence/
   → FTIS for sport-specific signal
   → Token-weighted scoring for Tier 1 sports

6. fan-token/defi-liquidity-intelligence/
   → If prizes are paid in fan tokens: TVL and slippage check
   → Liquidity check before distributing token prizes

7. core/confidence-output-schema.md
   → Structured output for each pick with full SportMind metadata

Skills API:
  GET /stack?use_case=pre_match&sport={sport}
  One call per sport per game week loads the full intelligence stack.
```

---

## Game mechanics powered by SportMind

### Mechanic 1 — SMS-Weighted Scoring

```
STANDARD SPORTS GAME:
  Correct pick = 10 points
  Incorrect pick = 0 points
  
SPORTMIND GAMIFIED SCORING:
  Correct pick, SMS ≥ 80 = 15 points (quality intelligence rewarded)
  Correct pick, SMS 60-79 = 12 points
  Correct pick, SMS 40-59 = 8 points (lucky guess; lower reward)
  Incorrect pick, SMS ≥ 80 = -2 points (penalty for high-confidence wrong pick)
  Incorrect pick, SMS < 60 = 0 points (no penalty for low-confidence miss)
  
WHY THIS WORKS:
  Players are incentivised to load better SportMind intelligence before picking.
  A player who does their homework (full 5 layers, fresh macro check, lineup
  confirmed) gets higher-weighted scores for correct picks.
  A player who guesses randomly can still occasionally score but cannot
  systematically outperform someone using quality intelligence.
  
  This is how the game rewards genuine sports knowledge over luck.
```

### Mechanic 2 — Flag-Aware Pick Locking

```
BEFORE PICK SUBMISSION, the system checks SportMind flags:

lineup_unconfirmed: TRUE
  → Pick is accepted but locked at 50% scoring weight
  → If lineup confirms before match: pick unlocks to full weight
  → If lineup confirms player absent: pick is invalidated (no penalty)
  
macro_override_active: TRUE  
  → All picks for fan token-denominated games are reduced 25%
  → Visible warning: "Macro override active — crypto bear market detected"
  → Non-token game picks unaffected

liquidity_critical: TRUE
  → Token prize distribution paused until liquidity recovers
  → Player notified with macro context

AGENT DISPLAY:
  "Your pick for Man City vs Arsenal:
   Direction: HOME
   SMS: 78 (GOOD) — 3 layers loaded, lineup unconfirmed
   Scoring weight: 80% until lineup confirms (T-2h before kickoff)
   Flag: lineup_unconfirmed — check back at 6pm ET for full weight"
```

### Mechanic 3 — Multi-Sport Tournament with SMS Rankings

```
WEEKLY MULTI-SPORT INTELLIGENCE TOURNAMENT:

Players make picks across multiple sports in a single game week.
Final standings are ranked by:
  1. Correct picks (primary)
  2. Average SMS of all picks (tiebreaker — rewards consistent quality intelligence)
  3. Total modified score (SMS-weighted)

LEADERBOARD DISPLAY:
  Rank | Player | Picks | Correct | Avg SMS | Score
  ─────────────────────────────────────────────────
  1    | Alice  | 12    | 9       | 81.4    | 147
  2    | Bob    | 12    | 9       | 74.2    | 138
  3    | Carol  | 12    | 8       | 88.1    | 128
  
  Alice and Bob both got 9/12 correct, but Alice had higher average SMS.
  Carol had the highest average SMS (loaded the best intelligence) but
  fewer correct picks — still competitive due to SMS weighting.
```

### Mechanic 4 — Macro State Game Events

```
MACRO STATE EVENTS:
  When macro phase changes (NEUTRAL → BEAR), trigger a game event:
  
  "MACRO ALERT: Crypto bear market detected (BTC crossed 200-day MA).
   All token-denominated prizes this week are reduced 25%.
   SportMind macro_modifier: 0.75
   High-crypto-knowledge bonus: Players who loaded macro intelligence
   before making picks this week receive +5% to all scores."
   
  This turns macro intelligence into an active game mechanic —
  players who check the macro state before picking are rewarded.
```

---

## On-chain architecture

```
GAMIFICATION CONTRACT FLOW:

1. Player connects wallet (Chiliz Chain or compatible L2)

2. Player loads SportMind intelligence via Skills API
   GET /stack?use_case=pre_match&sport=football
   
3. Player submits pick WITH SportMind metadata:
   {
     "pick": "HOME",
     "sport": "football",
     "event_id": "ucl-qf-leg1-psg-vs-arsenal",
     "sportmind_metadata": {
       "adjusted_score": 71.4,
       "sms": 78,
       "sms_tier": "GOOD",
       "flags": {"lineup_unconfirmed": true},
       "layers_loaded": [1, 2, 4, 5],
       "signature": "sha256_of_intelligence_bundle"
     }
   }

4. Smart contract stores pick with SMS metadata

5. Match settles on-chain (Azuro oracle / Chainlink sports feed)

6. Contract calculates score = base_score × sms_modifier × flag_modifier

7. Token prizes distributed from prize pool
   Prize pool denominated in: $CHZ, fan tokens, or stablecoin

INTEGRITY NOTE:
  SMS metadata is submitted with a SHA-256 signature of the
  SportMind intelligence bundle. This prevents players from
  claiming SMS 90 quality on a pick they made without loading
  the intelligence. The hash ties the pick to the actual
  SportMind output used to make it.
  
  Verify: platform/skill-hashes.json (integrity registry)
```

---

## Agent system prompt

```
You are a sports GameFi intelligence agent powered by SportMind.
Your role is to help players make picks with the highest SMS possible —
loading the right intelligence for each sport and surfacing the flags
that affect their scoring weight.

FOR EACH PICK RECOMMENDATION:

1. IDENTIFY THE RIGHT SKILL STACK:
   Is this a Tier 1 sport with active tokens? → Full 5-layer stack
   Is this a prediction market game? → pre_match stack
   Is this a lightweight fantasy pick? → domain + athlete minimum

2. COMPUTE THE SMS:
   Tell the player their current SMS before they submit the pick.
   "Your current SMS is 62 (GOOD). To reach HIGH_QUALITY (80+),
   load the macro context and confirm the lineup."

3. FLAG AWARENESS:
   Alert the player to active flags BEFORE they submit:
   "lineup_unconfirmed is active — your pick will be locked at 50%
   scoring weight until lineup confirms. Check back at 6pm ET."

4. MACRO CONTEXT:
   Always check macro_modifier before token-denominated picks.
   "Macro is currently NEUTRAL (modifier: 1.00). No reduction applied
   to token prizes this week."

5. SPORT-SPECIFIC RULES:
   Football: "Goalkeeper matters most for clean sheet picks"
   NFL: "QB injury report closes Friday — wait for Friday status"
   MMA: "Weigh-in result at 2pm ET — check before submitting"
   Cricket: "Toss at 9:30am ET — dew factor applies for night matches"

TONE: Helpful coach, not financial advisor. Frame intelligence as
helping players make more informed picks, not guaranteeing outcomes.
```

---

## References

- `core/sportmind-score.md` — SMS calculation and scoring mechanic
- `core/confidence-output-schema.md` — Pick metadata format
- `platform/skill-hashes.json` — Integrity verification for picks
- `platform/integration-partners.md` — Azuro and Chiliz integration
- `fan-token/defi-liquidity-intelligence/` — Prize pool liquidity check
- `macro/macro-crypto-market-cycles.md` — Macro game events
- `agent-prompts/agent-prompts.md` — Prompt 3 (prediction market agent)

*MIT License · SportMind · sportmind.dev*
