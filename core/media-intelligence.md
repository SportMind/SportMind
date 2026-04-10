---
name: media-intelligence
description: >
  Media and journalism intelligence framework for SportMind. Covers which outlets
  break news first by sport, journalist authority tiers, how to weight unconfirmed
  reports, news velocity as a fan token sentiment signal, and how media coverage
  duration affects commercial signal windows. Use when an agent needs to evaluate
  the reliability of a news source before using it as a signal input, determine
  whether a journalist report should modify a current signal, or understand how
  media coverage volume affects HAS trajectory. Sits between verifiable-sources
  (confirmed facts) and social-intelligence-connector (social media volume).
  The middle intelligence layer: reputable journalism as a structured signal.
---

# Media Intelligence — SportMind

**Structured journalism as a signal input layer.**

`core/verifiable-sources-by-sport.md` covers confirmed facts — where to verify
something that has been officially announced. `platform/social-intelligence-connector.md`
covers social media volume. This skill covers the layer between them: reputable
sports journalism as a structured signal input that carries intelligence value
*before* official confirmation.

A manager press conference 48 hours before a match is not a verified fact.
It is a Tier 2 media signal that modifies the pre-match analysis. Knowing how
to weight it correctly is the difference between an agent that reacts to noise
and one that incorporates structured media intelligence.

---

## The media signal framework

```
THREE TYPES OF MEDIA SIGNAL:

TYPE 1 — BREAKING NEWS (Category 1-4 from core/breaking-news-intelligence.md):
  Hard facts reported by reliable media before official confirmation
  Example: "Sky Sports: [Player] will not feature tonight — confirmed injury"
  Treatment: Apply Tier 2 confidence weighting; verify at Tier 1 ASAP
  Signal impact: IMMEDIATE — modify current signal

TYPE 2 — DIRECTIONAL INTELLIGENCE:
  Informed reporting that signals what is likely to happen
  Example: "The Athletic: Manager plans to rotate heavily for domestic cup"
  Treatment: Apply as directional modifier only; await confirmation
  Signal impact: MODERATE — flag for monitoring, reduce position sizing

TYPE 3 — NARRATIVE SIGNAL:
  Media coverage volume and tone that affects fan sentiment independent of facts
  Example: 12 articles about a player's "return to form" in one week
  Treatment: Feeds CDI extension model via core/core-narrative-momentum.md
  Signal impact: INDIRECT — extends or reduces commercial duration
```

---

## Journalist authority tiers — football

```
TIER 1 — CONFIRMED NEWS (apply as near-fact):
  Fabrizio Romano (@FabrizioRomano)
    Authority: Transfer market globally
    "Here we go" phrase = deal confirmed; do not wait for club announcement
    Track record: 98%+ accuracy on transfers marked as confirmed
    
  Official club sources
    Club website, verified club X account, official press conference
    These ARE Tier 1 — treat as ground truth

  Sky Sports News (UK)
    Transfer deadline day: fastest confirmed transfer reporting in UK
    Injury updates: official club confirmations relayed immediately
    
  BBC Sport
    UK football: reliable, fast, factual
    Investigative journalism: The Guardian (longer-form, verified)

TIER 2 — RELIABLE DIRECTIONAL (apply with 0.7x confidence weighting):
  The Athletic
    Deep club access; beat reporters with confirmed source networks
    Transfer speculation from Athletic = high credibility
    
  L'Équipe (France)
    Primary source for French football (PSG, French national team)
    First to know: PSG squad issues, French international news
    
  Marca / AS (Spain)
    Primary sources for Real Madrid and Barcelona respectively
    Rival club reporting: treat with caution (competitive bias possible)
    
  Gazzetta dello Sport / Corriere dello Sport (Italy)
    Primary sources for Italian football (ACM, INTER, JUV tokens)
    Italian media often speculative; verify transfers with Romano
    
  ESPN FC
    Global reach; reliable for American markets and major European news
    
  Sport Bild (Germany)
    Primary source for Bundesliga; strong on German national team
    
TIER 3 — USE WITH CAUTION (apply with 0.3x confidence; flag for monitoring):
  Mirror Sport, Daily Mail Sport, The Sun Sport
    UK tabloid football coverage; often speculative on transfers
    Match news and confirmed injuries: more reliable
    Transfer rumours: treat as monitoring flag only, not signal input
    
  Social media fan accounts (even large ones)
    Never use as signal input; monitor for social volume only
    
  Transfer aggregators (transfermarkt.com rumour section)
    Source aggregation: reliability depends on original source cited
    If original source is Tier 1/2: use original source, not aggregator
```

---

## Journalist authority tiers — other sports

```
RUGBY UNION:
  Tier 1: BBC Sport rugby · RugbyPass (rugbypass.com) · World Rugby official
  Tier 2: The Rugby Paper · ESPN Scrum · Guardian Sport (rugby section)
  Note: Club citing decisions — always verify at world.rugby/judicial-decisions

CRICKET:
  Tier 1: ESPNcricinfo (espncricinfo.com) · Cricbuzz · ICC official
  Tier 2: The Guardian Cricket · Sky Sports Cricket · Wisden
  Note: Selection and availability — verify at ESPNcricinfo squad pages

FORMULA 1:
  Tier 1: Formula1.com official · FIA fia.com/documents
  Tier 2: Autosport · Motorsport.com · RaceFans.net
  Note: Steward decisions and super licence points — only FIA PDFs are Tier 1

MMA:
  Tier 1: UFC.com official · USADA.org
  Tier 2: MMA Fighting (mmafighting.com) · Sherdog · ESPN MMA
  Note: Weigh-in results — UFC.com event page, not secondary reports

NBA:
  Tier 1: NBA.com official · ESPN NBA injury report
  Tier 2: The Athletic NBA · Bleacher Report (verified reporters only)
  Note: Trade news — Tier 2 minimum; always confirm with official team statement

NFL:
  Tier 1: NFL.com official · ESPN NFL injury report
  Tier 2: PFF (pff.com) · The Athletic NFL
  Note: Wednesday/Thursday/Friday injury designations — NFL.com only for Tier 1
```

---

## News velocity as sentiment signal

```
DEFINITION: The rate at which news articles about a club or token accumulate
over a defined time window — independent of the content of those articles.

WHY VELOCITY MATTERS:
  High news velocity = high media attention = social amplification = HAS movement
  The content of articles matters, but the volume also matters independently
  
  A club generating 15+ articles in 24h is in a high-engagement media cycle
  regardless of whether those articles are positive or negative

VELOCITY THRESHOLDS:
  > 20 articles in 24h: VIRAL — media cycle peaked; fan token HAS spike likely
  10–20 articles in 24h: HIGH — elevated engagement; monitor for HAS movement
  5–10 articles in 24h: MODERATE — active news cycle; normal elevated state
  < 5 articles in 24h: LOW — quiet period; standard CDI applies

VELOCITY × SENTIMENT COMBINATIONS:
  HIGH velocity + POSITIVE sentiment: strongest commercial signal (full HAS spike)
  HIGH velocity + NEGATIVE sentiment: sentiment cascade risk (see DSM framework)
  HIGH velocity + NEUTRAL sentiment: engagement without direction (small positive)
  LOW velocity + NEGATIVE sentiment: slow bleed (harder to detect, worse long-term)

VELOCITY SOURCE:
  Use platform/social-intelligence-connector.md to measure volume
  get_ecosystem_sentiment() returns ecosystem_tweet_count as velocity proxy
  get_token_mindshare() returns mention_count as token-specific velocity

VELOCITY DECAY:
  Peak velocity periods typically decay within 48–72h
  Exception: ongoing stories (transfer saga, disciplinary proceedings) sustain velocity
  CDI extension from high velocity: +20–40% of standard CDI duration
```

---

## Press conference intelligence

```
MANAGER PRESS CONFERENCES:
  Held: T-24h to T-48h before most major fixtures
  Available: Club official YouTube, club official X, BBC Sport summary

  WHAT TO EXTRACT:
    Injury updates (availability language — see below)
    Tactical hints (formation, system changes — directional only)
    Player form mentions (positive or negative emphasis)
    Psychological state indicators (pressure, confidence statements)

AVAILABILITY LANGUAGE DECODER:
  "Fully fit, ready to go"           → CONFIRMED (apply availability_modifier 1.00)
  "In contention, we'll see"         → PROBABLE (apply 0.95)
  "Not ruled out, taking it day by day" → DOUBTFUL (apply 0.80)
  "Slight concern, we'll assess"     → DOUBT (apply 0.75)
  "Not in our plans for this one"    → OUT (apply 0.00 for this player)
  "He's had a knock"                 → DOUBT (apply 0.70 — British understatement)
  "Long-term" (without timeline)     → OUT extended (calculate CDI impact)
  No mention of key player           → Investigate via other sources

MANAGER SENTIMENT INDICATORS:
  Defensive/evasive responses about a player: mild concern signal
  Specific praise of opponent: may signal conservative tactical approach
  Explicit confidence statements: narrative signal, not reliability signal
  Signs of pressure (short answers, frustration): MgSI concern indicator
  See core/manager-intelligence.md for full MgSI framework
```

---

## Media coverage duration and CDI interaction

```
COMMERCIAL DURATION INDEX (CDI) INTERACTION:
  Media coverage extends or reduces the commercial value window of an event.
  Standard CDI values assume moderate media coverage.
  
  CDI MODIFIERS BY MEDIA COVERAGE:

  VIRAL coverage (>20 articles/day for 3+ days):
    CDI multiplier: ×1.40
    Example: UCL trophy win normally CDI 45 days → with viral coverage: 63 days
    
  HIGH coverage (10–20 articles/day sustained):
    CDI multiplier: ×1.20
    
  STANDARD coverage (5–10 articles/day):
    CDI multiplier: ×1.00 (baseline)
    
  LOW coverage (< 5 articles/day):
    CDI multiplier: ×0.75
    Example: Minor competition win with low media interest → shorter commercial window
    
  NEGATIVE VIRAL (>20 articles, predominantly negative):
    CDI reversal: commercial period shortens; sentiment damage accelerates
    Apply as: CDI × 0.50 AND increase DSM check frequency

NARRATIVE SATURATION RULE:
  After 3+ weeks of continuous coverage of the same narrative:
  Coverage no longer drives additional CDI extension
  The story has become background noise — fans have priced it in
  Reduce CDI modifier to ×1.00 after saturation point reached
  See core/core-narrative-momentum.md for narrative fatigue model
```

---

## Media intelligence in the sequential reasoning chain

```
WHERE MEDIA INTELLIGENCE FITS IN THE FIVE-PHASE CHAIN:

PHASE 2 — Pre-match signal:
  After loading SportMind pre-match signal:
  Check: any recent media coverage that modifies availability or form?
  Apply: Tier 2 journalist report on lineup/injury → adjust availability_modifier
  
PHASE 3 — Disciplinary check:
  Media reports of disciplinary proceedings = Tier 2 input
  Verify via Tier 1 source (governing body) before applying DSM flag
  Tier 2 report alone: flag for verification, do not apply full modifier

PHASE 4 — Fan token context:
  Media velocity contributes to sentiment_snapshot inputs
  High velocity + positive = supports ENTER
  High velocity + negative = supports WAIT until narrative clarifies

CROSS-REFERENCES:
  core/breaking-news-intelligence.md   → how to act on breaking news
  core/verifiable-sources-by-sport.md  → where to verify media claims
  platform/social-intelligence-connector.md → measuring media velocity
  core/core-narrative-momentum.md      → how media coverage affects CDI
  core/manager-intelligence.md         → press conference intelligence
```

---

*SportMind v3.40 · MIT License · sportmind.dev*
*See also: core/verifiable-sources-by-sport.md · core/breaking-news-intelligence.md*
*platform/social-intelligence-connector.md · core/core-narrative-momentum.md*
