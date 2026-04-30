---
name: mma-token-intelligence
description: >
  MMA-specific fan token intelligence. Use when the user asks about fighter token
  impact from fight results, weigh-ins, career events, promotional announcements,
  or any on-chain signal tied to MMA. Fighter tokens are unique — the token IS the
  athlete, not the club. Existential risk (retirement, career-ending injury) has no
  equivalent in team sport tokens. Produces FighterTIS (Fighter Token Impact Score),
  Fighter Token Multiplier (FTM), and Career Risk Index (CRI).
  Load alongside sports/mma and fan-token-pulse.
---

# MMA Token Intelligence

MMA fan tokens are structurally unlike any other sport in the Chiliz ecosystem.
Where football and F1 have *club* or *constructor* tokens, MMA tokens are **fighter-centric
— the token IS the athlete**. This creates the highest-upside and highest-risk token
profile in the entire suite. A single fight can double a fighter token or send it
to near-zero. A retirement announcement can permanently collapse a token that no team
sport equivalent can replicate.

---

## What this skill produces

- **Fighter Token Impact Score (FighterTIS)** — Fight × opponent × career context composite (0–100)
- **Fighter Token Multiplier (FTM)** — Individual fighter's inherent token amplification (0.50–1.60)
- **Career Risk Index (CRI)** — Probability-weighted existential risk to token value (0–100)
- **Fight Week Signal Map** — Specific signal windows across the full fight week cycle
- **Weigh-in Risk Assessment** — Binary risk scoring for the fight's critical pre-event
- **Post-Fight Trajectory** — Expected token arc based on result and method of victory

---

## Fighter Token Impact Score (FighterTIS)

```
FighterTIS = (
  event_tier_weight    * 0.30 +  # PPV vs Fight Night vs prelims
  fight_stakes         * 0.30 +  # title fight vs ranking fight vs exhibition
  fighter_token_health * 0.20 +  # HAS baseline from fan-token-pulse
  ftm_score            * 0.20    # inherent fighter token amplification
) * 100
```

| FighterTIS | Label | Agent action |
|---|---|---|
| 85–100 | Maximum | Full chain — all fight week windows |
| 70–84 | High | fan-token-pulse + social monitoring + weigh-in entry |
| 55–69 | Elevated | Enter post-weigh-in; monitor fight week |
| 40–54 | Standard | Base signal; standard sizing |
| 25–39 | Low | Minimal exposure — opponent or stakes not warranting |
| 0–24 | Negligible | Skip |

---

## Fighter Token Multiplier (FTM)

FTM measures a fighter's inherent ability to drive token ecosystem activity
independent of the specific fight outcome. In MMA this is driven almost entirely
by narrative — personality, rivalries, cultural identity, social presence, and
crossover appeal.

```
FTM = (
  social_reach_score       * 0.25 +  # following and AELS
  narrative_premium        * 0.30 +  # personality, trash talk, crossover appeal
  cultural_identity_score  * 0.25 +  # national/ethnic identity overlap with holders
  championship_proximity   * 0.20    # title holder, contender, or ranked
) normalised to 0.50–1.60
```

### FTM archetypes

**Elite FTM (1.35–1.60) — The Crossover Star**
Profile: Fighter whose appeal transcends MMA. Global following, mainstream media
presence, social virality. Token moves on quotes, press conference moments, walk-ons —
not just fight results. Their fights are cultural events.
Pattern: FighterTIS is elevated for every fight regardless of opponent ranking.
Token holder base is broader than typical MMA fans — sports casual audience included.
Retirement announcement = catastrophic CRI event. Token may not recover.

**High FTM (1.15–1.34) — The Champion**
Profile: Active world champion or multiple-division champion. Title fights generate
the largest single-event moves in the MMA token ecosystem. Consistent top-5 ranking.
Pattern: FTM is highest during title defences and potential superfight announcements.
Social narrative peaks around fight camps — gym footage, sparring partner announcements,
weight cut progress all generate measurable token responses.

**Strong FTM (0.90–1.14) — The Contender**
Profile: Top-10 ranked fighter, consistently competing in high-profile matchups.
Pattern: FTM activates strongly in title eliminator bouts. A win here is the
"next step" narrative that drives holder accumulation ahead of a title shot.

**Standard FTM (0.65–0.89) — The Ranked Fighter**
Profile: Ranked but not title contention. Token exists but suite is relatively thin.
Pattern: Token responds to results but lacks the narrative premium of higher tiers.

**Low FTM (0.50–0.64) — The Journeyman**
Profile: Unranked or early-career fighter. Token barely active.
Pattern: Results have limited suite impact. Token may spike on major upset win.

---

## Career Risk Index (CRI)

**This is MMA's unique existential risk variable — no equivalent exists in team sports.**

Fighter tokens can go to near-zero permanently. CRI scores the probability of a
career-ending event occurring and the token ecosystem not recovering.

```
CRI = (
  age_risk_score              * 0.25 +  # 35+ = elevated; 38+ = high
  consecutive_loss_risk       * 0.30 +  # 2 in a row = moderate; 3 = high
  injury_pattern_risk         * 0.20 +  # chronic injuries = retirement signal
  retirement_signal_risk      * 0.25    # public comments, social silence, agent activity
) * 100
```

| CRI | Label | Agent action |
|---|---|---|
| 0–20 | Low | Normal position sizing |
| 21–40 | Moderate | Reduce sizing 20%; monitor closely |
| 41–60 | Elevated | Reduce sizing 40%; set hard stop on any loss |
| 61–80 | High | Avoid new positions; hold existing with tight stop |
| 81–100 | Critical | Exit existing positions; structural risk of permanent token collapse |

### CRI trigger events (immediate reassessment required)

| Event | CRI adjustment |
|---|---|
| Fighter announces retirement | CRI → 95+ immediately. EXIT. |
| Career-ending injury (orbital, ACL at 36+, spinal) | CRI → 85+. EXIT. |
| USADA/WADA doping ban | CRI → 70+. EXIT immediately. |
| Three consecutive losses | CRI +25 |
| Two consecutive KO losses | CRI +35 (brain health concern) |
| Fighter drops division (unusual weight class move at 34+) | CRI +15 |
| Extended layoff 18+ months (not injury explained) | CRI +20 |
| Manager/promotional contract dispute going public | CRI +10 |

---

## Fight Week Signal Map

MMA has the most complex pre-event signal structure of any sport:

```
FIGHT WEEK:
  Day -7:  Fight announcement / opponent confirmed
           → Initial FTM spike: +5–15% for high-FTM fighters
           → Opponent quality assessment: is this a step up or tune-up?

  Day -5:  Open workouts / media day
           → Physical condition signals: weight cut progress, sharpness
           → Body language and confidence signals (agent-detectable via social)

  Day -3:  Press conference / face-off
           → Trash talk and psychological signals
           → Elite FTM fighters generate viral moments here
           → Social engagement spike: monitor TVI correlation

  Day -2:  OFFICIAL WEIGH-INS → BINARY RISK EVENT (see below)
           → Single most important non-fight event in MMA token lifecycle

  Day -1:  Ceremonial weigh-ins / public face-off
           → Final form check — fighter appearance and energy
           → Social peak for narrative fighters

  Day 0:   FIGHT NIGHT
           → Pre-fight: walk-on music, octagon entrance — minor signal
           → Fight result: primary token event
           → Post-fight interview: "who's next" statements drive next cycle

  Day +1:  Result digestion
           → Title shot announcement (if earned): +secondary signal
           → "Rematch?" narrative: activates if controversial result
```

---

## Weigh-in Risk Assessment

The MMA weigh-in is the most significant pre-event binary risk in any sport.
No other sport has an equivalent single event that can:
- Cancel the fight entirely
- Void title eligibility while the fight still proceeds
- Signal training camp problems that affect performance

```
WEIGH-IN OUTCOMES:

Makes weight cleanly (within limit):
  → Token: Neutral to +2% (confirmation; weight cut stress removed)
  → Agent: Highest-conviction entry point of fight week
  → Note: Enter post-weigh-in for any FighterTIS > 60

Misses weight by < 1lb (fight proceeds, title voided if applicable):
  → Own token: -8–18% (title implications lost; camp question)
  → Opponent token: +4–8% (psychological advantage; title shot if defending)
  → Agent: Reassess FighterTIS downward; title shot probability gone

Misses weight by > 1lb:
  → Own token: -18–30%
  → Agent: Consider exit or significant position reduction

Fight cancelled due to weight miss:
  → Both tokens: -15–35% (uncertainty + narrative disruption)
  → Agent: EXIT — no fight = no resolution signal

Opponent misses weight:
  → Own token: +5–12% (opponent potentially weakened, psychological edge)
  → Agent: Can add position — you gain, opponent weaken simultaneously
```

**Agent rule: Never hold full position through weigh-ins for FighterTIS > 70.**
Enter post-weigh-in for maximum conviction. Pre-weigh-in entry = accepting binary risk.

---

## Event Tier Classification

### Tier 1 — UFC Numbered PPV Events (FighterTIS base: 75–100)

UFC PPV events (UFC 300, 305, etc.) represent the highest FighterTIS events in MMA.
Title fights on PPV main cards are the maximum signal events.

| Fight type | FighterTIS base |
|---|---|
| Undisputed title fight (PPV main event) | 95 |
| Interim / unified title fight (PPV) | 88 |
| Non-title superfight (PPV main event) | 85 |
| High-ranked PPV co-main (top 5 vs top 5) | 78 |
| PPV undercard (ranked fights) | 65 |

### Tier 2 — UFC Fight Night Main Events (FighterTIS base: 55–74)

UFC Fight Night events (ESPN+, ABC, etc.) — main event fighters still generate
meaningful token signal but at lower baseline than PPV.

| Fight type | FighterTIS base |
|---|---|
| Fight Night: ranked main event (top 5 involved) | 72 |
| Fight Night: standard ranked main event | 62 |
| Fight Night: contender fight | 55 |

### Tier 3 — Prelims and Other Promotions (FighterTIS base: 20–54)

UFC prelims for ranked fighters: 40–54
Bellator / PFL main events: 45–60 (for fighters with active tokens)
ONE Championship: 42–55 (growing Asian market relevance)
Exhibition / crossover events (e.g., MMA vs boxing): 50–70 (narrative premium)

---

## Post-Fight Token Trajectories

Method of victory matters enormously in MMA token intelligence:

| Result | Immediate impact | 72h trajectory |
|---|---|---|
| KO/TKO win (clean finish) | +18–45% | Sustained — "highlight reel" narrative |
| Submission win | +15–35% | Sustained — technical narrative |
| Decision win (dominant) | +8–18% | Moderate — solid but less exciting |
| Split decision win | +5–12% | Cautious — controversy possible |
| Draw | -3–8% | Negative — unsatisfying |
| KO/TKO loss | -20–40% | Extended negative — career risk assessment triggered |
| Submission loss | -15–30% | Negative — technique vulnerability exposed |
| Decision loss | -8–18% | Moderate negative — can rebuild |
| No contest / DQ | -10–20% | Uncertainty premium |
| Title won (finish) | +35–70% | Maximum sustained narrative arc |
| Title won (decision) | +20–45% | Strong but less explosive |
| Title lost (any method) | -25–50% | Major structural negative |

**Key MMA-specific insight:** HOW the fight ends matters as much as WHO wins.
A dominant finish by an underdog generates larger token moves than a squeaky
decision win by the heavy favourite. Always assess both outcome AND method.

---

## Superfight and Crossover Signals

Superfight announcements (MMA legend vs boxing champion, inter-promotion challenges)
are narrative events that generate token moves independent of training camp:

| Announcement type | Token impact |
|---|---|
| UFC vs boxing crossover announced | +15–35% for MMA fighter (media amplification) |
| Inter-promotional superfight | +10–20% |
| Legend vs rising star booking | +8–15% for rising star; +5–12% for legend |
| Celebrity crossover (YouTuber, athlete) | +5–15% — pure narrative, lower conviction |

**Agent rule for crossover events:** Enter on announcement; exit at +72h.
The actual fight (often months later) has a separate signal cycle when it arrives.
Crossover announcement premiums are front-loaded narratively.

---

## Agent Reasoning Prompts

```
You are an MMA fan token intelligence agent. Before evaluating any MMA event:

1. FIGHTER TOKENS ARE EXISTENTIAL. Unlike club tokens, a fighter token can
   collapse permanently on retirement, serious injury, or doping ban.
   Always compute CRI before entering any new position.

2. WEIGH-IN IS THE HIGHEST-CONVICTION ENTRY POINT.
   For any FighterTIS > 60, the optimal entry is post-weigh-in, not pre-fight.
   The weigh-in removes the binary risk that makes pre-fight entry speculative.

3. METHOD OF VICTORY determines the narrative arc, not just the result.
   A finish generates 2–3× the token response of a decision win.
   Factor expected finishing tendency into pre-fight position sizing.

4. CAREER RISK INDEX must be computed before any entry.
   A fighter with CRI > 60 is uninvestable regardless of fight odds.
   A retirement announcement = immediate full exit, no exceptions.

5. TWO CONSECUTIVE KO LOSSES is a hard stop signal.
   This pattern raises brain health concerns that suppress token ecosystem
   long-term, regardless of what the fighter says publicly.

6. CROSSOVER EVENTS are narrative trades, not performance trades.
   Size at 0.5× maximum. Enter on announcement; exit within 72h.
   Do not hold through the actual crossover fight months later as a
   continuation of the announcement position.

7. TITLE CHANGES are the highest single-event tokens in MMA.
   A first-time champion token has the largest percentage upside.
   A multi-defence champion losing is the largest percentage downside.
   Both are more dramatic than equivalent events in any team sport token.
```

---

## Data Sources

- Fight schedules and results: UFC official, Tapology, Sherdog
- Fighter rankings: UFC official weekly rankings
- Weigh-in results: ESPN MMA, MMA Fighting, MMAjunkie
- Transfer/contract news: MMA Fighting, The Athletic MMA
- Token data: Kayen/FanX API + Socios Connect (via fan-token-pulse)
- Social: LunarCrush + fighter social handles

---

## Compatibility

**Layer 1 companion:** `sports/mma`
**Required Layer 3:** `fan-token-pulse`
**Recommended:** `athlete-social-lift` (FTM confirmation), `athlete/mma` (camp signals)
**Recommended:** `transfer-intelligence` (promotional contract context)

---

*MIT License · SportMind · sportmind.dev*
