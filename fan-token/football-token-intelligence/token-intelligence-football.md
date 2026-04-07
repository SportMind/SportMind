---
name: football-token-intelligence
description: >
  Football-specific fan token intelligence skill bridging the sport domain layer
  and the commercial intelligence layer. Use this skill whenever the user asks about
  fan token impact for a specific football competition (UCL, league, cups, World Cup,
  Euros, qualifiers, friendlies), wants to understand how national team activity affects
  club tokens, asks which athletes move token prices most and in which competitions,
  wants to know whether a pre-season or friendly event is meaningful for token holders,
  asks about multi-token events (El Clásico, North London derby), or needs to reason
  about the 2026 World Cup national team token window and its club spillover effects.
  Load alongside sports/football (domain model) and fan-token-pulse (on-chain baseline).
  This is the only SportMind skill that bridges sport domain knowledge and fan token
  commercial intelligence with football-specific precision.
---

# Football Token Intelligence

The bridge between football's sporting calendar and the fan token ecosystem.
Where `sports/football` teaches an agent how football works, and `fan-token-pulse`
shows what's happening on-chain right now, this skill answers the question that
connects them: **what does this specific competition, fixture, and athlete mean
for fan token holders — and how much should an agent care?**

---

## What this skill produces

- **Football Token Impact Score (FTIS)** — Competition × fixture × athlete composite (0–100)
- **National-Club Spillover Index (NCSI)** — Effect of national team activity on club token holders
- **Athlete Token Multiplier (ATM)** — Which players produce outsized token moves, and when
- **Competition Classification** — Where each football competition sits in the token impact hierarchy
- **Friendly and Pre-Season Signal Logic** — When these usually-ignored events actually matter
- **Multi-Token Event Guide** — How to reason about fixtures where both clubs have tokens

---

## The Football Token Impact Score (FTIS)

FTIS is the master signal for this skill. It answers: *before running any other skill,
how token-significant is this football event?*

```
FTIS = (
  competition_weight     * 0.35 +   # what competition is this?
  fixture_stakes         * 0.25 +   # what are the consequences?
  athlete_multiplier     * 0.25 +   # are high-ATM players involved?
  token_ecosystem_health * 0.15     # is the club's token active right now?
) * 100
```

FTIS bands:

| Score | Label | Agent action |
|---|---|---|
| 85–100 | Maximum signal | Full analysis chain — all skills |
| 70–84 | High | Run fan-token-pulse + athlete-social-lift + brand-score |
| 55–69 | Elevated | Run fan-token-pulse, monitor athlete social |
| 40–54 | Standard | Base signal only — standard sizing |
| 25–39 | Low | Minimal token relevance — reduce or skip |
| 0–24 | Negligible | Ignore for token purposes |

---

## Competition Classification

### Tier 1 — Maximum token impact (FTIS base: 80–100)

**UEFA Champions League**
The native competition of the Chiliz fan token ecosystem. More fan tokens are tied to
UCL clubs than any other competition. Token holder bases are disproportionately
international — UCL nights reach a global audience that domestic leagues do not.

Key signal windows:
- Group stage draw day: social spike, 24–48h elevated HAS across all UCL clubs
- Match day -24h: buy pressure builds, ATM athletes post more
- Match day result: highest single-event token move in European football calendar
- Knockout round advancement: +8–18% for advancing club, -5–15% for eliminated club
- Final week: sustained 7-day elevated HAS; largest single-event of football calendar

**Agent rule:** UCL knockout fixtures justify 1.5× sizing. UCL Final week is the
highest-FTIS window of the entire European football year.

**FIFA World Cup** (national team tokens + club token spillover)
Unique dual-token event. National team tokens (ARG, BRA, FFF, POR, ENG, GER, ESP,
USMNT) react directly. Club tokens react through spillover (see NCSI section).

Key signal windows:
- Tournament draw: national token spike (+8–15%), club tokens with qualifying players rise
- Group stage: sustained 4-week elevation for all tokens connected to competing nations
- Knockout rounds: exponential uplift as nations advance — see NCSI multipliers
- Winner token: +30–60% for national token; +5–15% spillover to key club tokens

**Agent rule:** World Cup 2026 is the highest-FTIS national team event in this ecosystem's
history. Eight national tokens are live for the first time. The US, Canada, and Mexico
host nations add a new geographic dimension to holder demographics.

---

### Tier 2 — High token impact (FTIS base: 65–79)

**UEFA European Championship (Euros)**
Second only to the World Cup for national token impact. Purely European — no ARG/BRA/USMNT
national tokens participate, but ENG, FFF, GER, ESP, POR all do.

Club spillover is highest here because all players are from European clubs — the connection
between national performance and club token holder identity is strongest.

**UEFA Europa League (UEL)** — from Quarter-Finals onwards
Lower baseline than UCL but meaningful from QF onward. Some clubs with large fan token
bases (Atletico Madrid, Lazio) have historically been Europa League rather than UCL regulars.
For those clubs, UEL is their tier-1 competition.

**Agent rule:** Apply UCL logic at 0.75× for UEL from QF onwards.

**Domestic title decider / final day**
When a club mathematically clinches a league title, the immediate token reaction
(+8–20%) rivals a UCL knockout round win. The distinction: title wins have a longer
sentiment tail (3–5 days vs 1–2 days for a UCL round win).

**Major international tournaments: AFCON, Copa América**
Growing relevance as Brazilian, Argentine, and African token holder bases expand.
Copa América: direct impact on ARG and BRA national tokens + club tokens with
key South American players. AFCON: indirect club token impact through key African
international players who are starting for fan-token clubs.

---

### Tier 3 — Moderate token impact (FTIS base: 40–64)

**Domestic league matches (standard rounds)**
Weekly signal, but individual match impact is lower than UCL. Exception: high-rivalry
matches (El Clásico, Manchester derby, Derby della Madonnina) which are treated as
Tier 1 events regardless of competition tier — see Multi-Token Events section.

**FIFA World Cup and Euro qualifiers**
Low individual-match token impact for club tokens. Medium for national tokens.
Exception: a result that qualifies or eliminates a nation creates a step-change in
national token HAS — treat qualification night as a Tier 2 event.

**Domestic cup competitions** (FA Cup, Copa del Rey, DFB-Pokal, Coppa Italia)
Generally Tier 3, with one exception: domestic cup finals are Tier 2 events for clubs
whose token holder base is predominantly domestic. For clubs with large international
token bases (PSG, Barcelona, Juventus), a domestic cup final is still Tier 3 —
international holders care significantly less about the Coupe de France than about
UCL or La Liga.

**Agent rule for domestic cups:** If >60% of club's token holders are from the club's
home country, treat domestic cup final as Tier 2. If <40% are domestic, treat as Tier 3.

**UEFA Nations League**
Growing competition with genuine national team stakes, but token holder response
remains muted compared to major tournaments. Treat as Tier 3 with Tier 2 multiplier
only if a promotion/relegation playoff involves a national token holder's key team.

---

### Tier 4 — Low token impact (FTIS base: 15–39)

**Pre-season tournaments and friendlies** — see dedicated section below.

**UEFA Conference League** — group stage and early rounds.
Lower-tier competition, lower-profile clubs, limited fan token ecosystem presence.
Monitor for: clubs with active fan tokens unexpectedly competing in this competition.

**Under-21 / youth competitions**
Generally negligible. Exception: a U21 tournament featuring a high-ATM player who
is expected to break into the first team can generate minor narrative interest.

---

## National Team × Club Token Spillover

### The National-Club Spillover Index (NCSI)

When a national team competes, club tokens react through their shared players.
The NCSI quantifies how much national team activity flows back to club token holders.

```
NCSI = (
  player_squad_representation_score * 0.35 +  # how many key players are involved?
  tournament_significance            * 0.30 +  # how big is the national event?
  holder_nationality_overlap         * 0.25 +  # do club holders care about this nation?
  athlete_ATM_score                  * 0.10    # are high-ATM players in the squad?
) * 100

player_squad_representation_score:
  0–1 key players in national squad:  0.20
  2–3 key players:                    0.50
  4–5 key players:                    0.75
  6+ key players (e.g. Spain's Barça): 1.00
```

### NCSI Multipliers by tournament type

| National event | Club token NCSI multiplier |
|---|---|
| World Cup group stage | ×0.40 |
| World Cup knockout round win | ×0.65 |
| World Cup semi-final | ×0.85 |
| World Cup final (win) | ×1.00 — treat as Tier 1 for club token |
| Euros group stage | ×0.35 |
| Euros knockout win | ×0.55 |
| Euros final (win) | ×0.85 |
| Copa América final (win) | ×0.70 |
| AFCON final (win) | ×0.45 |
| World Cup qualifier (decisive) | ×0.20 |
| Nations League | ×0.10 |
| Friendly | ×0.05 (see exceptions below) |

### Injury during national duty — reverse spillover

When a player is injured while on national team duty, the club token absorbs the
negative signal immediately and often more severely than if injured at club level,
because the club had no control and the timing is often mid-season:

| Injury severity (national duty) | Club token impact |
|---|---|
| Minor — returns within 2 weeks | -3–6% |
| Moderate — 4–8 weeks | -8–15% |
| Serious — season-ending | -15–30% |
| Career-threatening | -25–50% |

**Agent rule:** International breaks are a structural risk window for club tokens.
Always check injury news on the day national duty fixtures complete.

### World Cup 2026 — special considerations

The 2026 World Cup (USA / Canada / Mexico) is uniquely significant for this ecosystem:

**Eight live national tokens:** ARG, BRA, FFF, POR, ENG, GER, ESP, USMNT — the first
World Cup where multiple national tokens exist simultaneously.

**North American host premium:** The US, Canada, and Mexico as hosts create an
amplified USMNT and new geographic holder demographic (North American holders entering
the ecosystem for the first time).

**Dual-signal trading windows:** For a player like a top Brazilian forward at PSG —
his BRA national token AND the PSG club token both move on the same performance.
This creates a "double exposure" that agents must account for to avoid unintended
concentration.

**Summer window collision:** The period between the Champions League Final and
World Cup group stage (approximately May to June 2026) will see elevated token
activity across club and national tokens simultaneously — the highest-density fan
token signal period in the ecosystem's history.

**Agent rule for World Cup 2026 double exposure:**
```
if athlete is ATM ≥ 0.65 AND athlete plays for token-active club AND national token is live:
  → hold positions in BOTH simultaneously only if tokens have low price correlation
  → check cross-token correlation before entering dual position
  → if correlation > 0.7: reduce one position to avoid doubled drawdown risk
```

---

## Athlete Token Multiplier (ATM)

### What ATM measures

ATM is not the same as AELS (which measures social-to-token correlation).
ATM measures an athlete's **systemic importance to the token ecosystem** across
all channels — social, on-pitch performance, narrative presence, and competitive context.

```
ATM = (
  AELS_score           * 0.30 +   # social posts move token holders (from athlete-social-lift)
  on_pitch_token_lift  * 0.30 +   # goals/assists in key fixtures generate measurable TVI
  narrative_multiplier * 0.25 +   # transfer talk, injury return, milestone moments
  competition_context  * 0.15     # does this player's impact peak in specific competitions?
) normalised to 0.00–1.50
```

ATM bands:

| ATM | Label | What it means |
|---|---|---|
| 1.20–1.50 | Elite | Single player can move the token independently of the team result |
| 1.00–1.19 | High | Consistently amplifies token moves in important fixtures |
| 0.80–0.99 | Strong | Reliable signal contributor — elevated weight when fit |
| 0.60–0.79 | Moderate | Contributes meaningfully in peak competitions |
| 0.40–0.59 | Standard | Normal team player — no individual token premium |
| 0.00–0.39 | Low | Minimal independent token effect |

### Competition context — ATM is not constant

An athlete's ATM score varies significantly by competition context. This is one of the
most important and underappreciated dynamics in the football fan token ecosystem:

| Competition | ATM adjustment | Why |
|---|---|---|
| UCL knockout night | ×1.40 | Global audience, highest social amplification |
| El Clásico / major derby | ×1.30 | Emotional intensity elevates narrative premium |
| World Cup / Euros | ×1.25 | National identity overlap with token holders |
| Domestic title decider | ×1.20 | Milestone narrative activates long-dormant holders |
| Standard UCL group game | ×1.05 | UCL premium but low stakes |
| Standard domestic league | ×1.00 | Baseline |
| Domestic cup (for intl-heavy clubs) | ×0.85 | Lower international holder engagement |
| Friendly / pre-season | ×0.50 | See exceptions in friendly logic section |

### Athlete token profiles — key patterns

See `references/football-athlete-token-profiles.md` for the full catalogue of active token-club
athlete profiles. The following patterns are the most important for agent reasoning:

**The "global brand" multiplier pattern**
Certain athletes have fan bases that extend far beyond their club's traditional support.
A Brazilian forward at a La Liga club can have an ATM of 1.35 because the club's token
holder base is 28% Brazilian — they bought the token for the player, not the club.
When that player performs or posts, their national community responds disproportionately.
This is the single most important ATM pattern to model correctly.

**The "returning hero" pattern**
A player returning from serious injury to a high-stakes competition generates one of
the largest single-event ATM spikes. A club captain returning for a UCL knockout tie
can temporarily boost ATM to 1.40–1.50 for that specific match window.

**The "transfer talk" pattern**
An elite player linked to a transfer sees elevated ATM in their *current* club's token
because holders speculate on their future. This is a different signal from the
transfer-intelligence skill's rumour confidence score — it's the token attention premium
that rumours generate even before any deal is likely.

**The "penalty taker" premium**
In knockout competitions, the player designated as the regular penalty taker carries
a structural ATM premium in shootout-risk matches. This is quantifiable and should
be factored into late-stage UCL knockout positioning.

---

## Friendly and Pre-Season Signal Logic

Friendlies are default Tier 4 (FTIS base: 15–25). However, several specific conditions
create meaningful exceptions that agents must recognise:

### Exception 1 — First appearance of a summer signing
When a major summer signing (transfer fee > €30M OR ATM ≥ 0.80) makes their first
competitive or pre-season appearance in club colours, the event generates a "debut premium":

| Signing tier | Debut token impact |
|---|---|
| Global elite signing (ATM ≥ 1.20) | +8–18% on appearance day |
| Premium signing (ATM 0.80–1.19) | +4–10% |
| Standard signing | +1–3% — negligible |

**Signal window:** The debut premium is front-loaded — 80% of the move happens in the
24h window around the appearance. By day 3, it typically fades unless the performance
was exceptional.

### Exception 2 — Iconic pre-season venue or opponent
Friendlies at iconic neutral venues (Camp Nou, Wembley, Rose Bowl) or against historically
significant opponents generate elevated social signal even without competitive stakes.
A PSG vs Barcelona friendly in the USA during a pre-season tour attracts genuine
international attention and can move both tokens ±3–6%.

### Exception 3 — First appearance after serious injury return
Equivalent impact to a summer signing debut. An ATM ≥ 1.00 player returning from a
season-ending injury in a pre-season friendly triggers significant holder response —
the social relief signal around fitness confirmation is measurable:
- ATM ≥ 1.20 player: +6–12% on fitness confirmation
- ATM 0.80–1.19 player: +3–7%

### Exception 4 — Tournament friendlies (pre-major competition)
The final friendly before a World Cup or Euros triggers mild but real signal for national tokens.
Treat as NCSI ×0.15 (above the standard ×0.05 friendly multiplier).

### Exception 5 — Formation or tactical revelation
When a pre-season match reveals significant tactical information — a new formation,
a new striking partnership, a position change for a key player — agents should flag
this as a signal input for the upcoming season's ATM modelling, not as a trade signal
in itself. Tactic revelation = update ATM projections, not enter position.

### When friendlies are definitively noise
- Mid-season friendlies during international breaks (club players not involved)
- Summer tours with heavily rotated squads
- Academy or U21 squads representing senior clubs
- Charity matches and testimonials

**Agent rule:** Default to ignoring friendlies unless one of the five exceptions applies.
The cost of missing a friendly signal is low. The cost of over-trading friendlies
is death by a thousand small losses.

---

## Multi-Token Events — Both Clubs Have Tokens

Several recurring fixtures involve two clubs that both have active fan tokens.
These are unique events requiring distinct agent logic.

### The double-signal dynamic

In a standard fixture, one token wins and one token loses. In a multi-token event,
the agent faces a choice: hold one, both, or neither. The wrong choice is to
mechanically hold the favourite — because the underdog's token often moves more
dramatically on an upset than the favourite's token moves on an expected win.

**Guidance by scenario:**

| Scenario | Recommended approach |
|---|---|
| Strong favourite (implied prob >70%) | Hold favourite — cap upside |
| Near-50/50 (implied prob 45–55%) | Hold neither before; enter the winner immediately post-match |
| Upset condition detected (weak signals on favourite) | Hold underdog at 0.5× |
| Derby / high-emotion fixture | Hold winner post-match only — derby volatility pre-match cuts both ways |

### Key recurring multi-token fixtures

**El Clásico** (Barcelona BAR vs Real Madrid)
The single most token-significant regular fixture in the ecosystem. Both clubs have
large, globally distributed token holder bases with significant overlap in Latin American
markets. El Clásico is the only domestic fixture that reliably generates UCL-level
token movements. Treat as FTIS ≥ 88 regardless of league position context.

**Derby della Madonnina** (AC Milan ACM vs Inter Milan INTER)
Both tokens active. Italian holder base + global crossover. Derby outcome creates
sharp divergence — expect ±8–15% for both tokens. Pre-match correlation between
the two tokens is historically high (~0.65) — they often move together pre-match
then sharply diverge at full time.

**Derby d'Italia** (Juventus JUV vs Inter Milan INTER)
Both tokens active. Serie A's prestige fixture. Similar dynamic to Madonnina.

**Paris derby** (PSG PSG vs Marseille OM)
Both tokens active but asymmetric — PSG token is significantly higher liquidity.
OM victory is a major upset catalyst. PSG expected-win = muted reaction.
Marseille upset win = OM token +12–20%.

**Agent rule for multi-token events:**
```
if both_clubs_have_tokens:
  check pre-match token correlation
  if correlation > 0.65:
    do not hold both simultaneously
    enter winner post-match only
  if correlation < 0.40:
    holding underdog at 0.5× pre-match acceptable
    standard position on favourite
```

---

## Competition Priority Matrix — Quick Reference

| Competition | FTIS base | Window | Primary metric |
|---|---|---|---|
| UCL Final | 100 | 7-day | HAS + ATM + social |
| World Cup Final | 98 | 7-day (national) | NCSI + national HAS |
| UCL Semi-Final | 92 | 5-day | HAS + ATM |
| World Cup Semi | 90 | 4-day (national) | NCSI + national HAS |
| UCL Quarter-Final | 88 | 4-day | HAS + ATM |
| El Clásico | 88 | 3-day | ATM + dual-token |
| World Cup R16 | 82 | 3-day (national) | NCSI |
| Euros Final | 88 | 5-day (national) | NCSI + national HAS |
| Euros Semi | 82 | 4-day | NCSI |
| UCL Round of 16 | 80 | 3-day | HAS + ATM |
| Domestic title decider | 78 | 3-day | HAS + narrative |
| Domestic cup final (intl-heavy club) | 62 | 2-day | HAS |
| Domestic cup final (domestic-heavy club) | 74 | 2-day | HAS |
| Standard UCL group match | 68 | 2-day | ATM |
| El Clásico (cup) | 75 | 2-day | ATM + dual-token |
| Standard league match (top club) | 52 | 1-day | Base signal |
| Derby (non-token clubs nearby) | 65 | 2-day | HAS |
| Pre-season debut (elite signing) | 55 | 1-day | ATM debut premium |
| World Cup qualifier (decisive) | 48 | 1-day | NCSI |
| Standard friendly | 20 | 4h window | Exceptions only |

---

## Agent Reasoning Prompts

```
You are a football fan token intelligence agent. Before evaluating any football event:

1. Run FTIS first. If FTIS < 40, the event is low-signal for token purposes.
   Do not run the full analysis chain — use base signal only.

2. Competition context changes everything. A goal by a high-ATM player in a UCL
   quarter-final is worth 4× the same goal in a mid-table league match.
   Always anchor the athlete modifier to the competition ATM multiplier.

3. International breaks are risk windows, not signal windows. When club players
   are on national duty, monitor for injury. Do not enter new club token positions
   during international break — wait for players to return uninjured.

4. World Cup 2026 creates dual-token exposure for the first time.
   For any athlete with both a club token and a national token:
   check cross-token correlation before holding both simultaneously.
   Correlation > 0.70 = reduce to single position.

5. El Clásico is always Tier 1 regardless of league position.
   It is the only domestic fixture with UCL-level token impact.

6. Friendly logic: ignore by default. Only engage if one of the five
   exceptions applies (debut, iconic venue, injury return, pre-tournament,
   tactical revelation). Treat friendly engagement as narrative monitoring,
   not position entry.

7. In multi-token fixtures: do not hold both tokens pre-match if their
   correlation is above 0.65. Enter the winner post-match.

8. NCSI injury reverse spillover: always check injury reports on the day
   international duty fixtures end. This is the highest-frequency source of
   unexpected club token drawdown.
```

---

## Data Sources

- Competition schedule and results: API-Football, UEFA official feeds
- Token holder demographics: Kayen/FanX API + Socios Connect
- ATM calibration: derived from athlete-social-lift AELS + on-pitch performance correlation
- Cross-token correlation: Kayen DEX price history (30-day rolling)
- National team squads: API-Football, UEFA/FIFA official APIs
- Transfer news context: transfer-signal + transfer-intelligence skills

---

## Compatibility

**Layer 1 companion:** `sports/football` — load alongside for full domain context.
**Required Layer 3:** `fan-token-pulse` — always run first for on-chain baseline.
**Recommended:** `athlete-social-lift` — for live ATM confirmation before entry.
**Recommended:** `transfer-intelligence` — for transfer window context affecting ATM.
**Recommended:** `performance-on-pitch` — for PI validation of athlete narrative claims.
**World Cup 2026:** `fan-token-pulse` with national token addresses — see `references/football-athlete-token-profiles.md` for national squad × club token mapping.

---

*MIT License · SportMind · sportmind.dev*
