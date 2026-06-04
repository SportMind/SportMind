---
name: social-sentiment-intelligence
description: >
  Core reasoning framework for community sentiment signals as modifier inputs.
  Covers sentiment classification (structural/event/noise/manipulated), platform
  weighting, cross-platform correlation, and fan token specific sentiment patterns.
  Agent-facing interface. Load alongside fan-token/fan-sentiment-intelligence/
  for the full emotional arc model.
---

# Social Sentiment Intelligence — Core Reasoning Framework

**How to classify and apply sentiment signals when they arrive.**
Not live sentiment data — the framework for interpreting sentiment
when an agent sources it from external feeds.

> Library Rule: the classification and weighting system is enduring.
> The framework applies regardless of which specific event triggers sentiment.

Related: `fan-token/fan-sentiment-intelligence/` — emotional arc model

---

## Sentiment classification — four types

```
TYPE 1 — STRUCTURAL SENTIMENT (apply this):
  Definition: sustained directional movement over 72+ hours across
    multiple platforms; driven by an enduring narrative (not a single event)
  Characteristics:
    Volume remains elevated over multiple days
    Consistent sentiment polarity (not reversing)
    Multiple platform sources showing same direction
  Modifier: ×1.05 (positive structural) or ×0.95 (negative structural)
  Duration: apply for as long as sustained signal persists; remove when signal reverses
  Examples: ongoing injury recovery narrative, post-UCL-final sentiment period,
    sustained governance engagement following new voting round

TYPE 2 — EVENT SENTIMENT (apply within window only):
  Definition: spike triggered by a specific discrete event; high intensity,
    short duration; decays to pre-event baseline
  Characteristics:
    Volume spike within 24h of event; begins decaying within 48h
    Clear trigger event identifiable
    Typically higher peak amplitude than structural sentiment
  Modifier: ×1.03 (positive event) or ×0.97 (negative event)
  Duration: apply only within 24-48h event window; remove on decay
  Examples: match result, transfer confirmation, governance vote result,
    player milestone announcement
    
TYPE 3 — NOISE (filter out, do not apply):
  Definition: single platform spike, short duration, low volume, no
    cross-platform confirmation
  Characteristics:
    Appears on one platform only
    Reverses within hours
    Volume does not sustain
  Modifier: NONE — filter entirely
  Examples: individual viral post, brief trending hashtag without depth,
    reaction to a single media article with no follow-through
    
TYPE 4 — MANIPULATED SENTIMENT (invert or ignore):
  Definition: coordinated activity pattern inconsistent with organic signal
  Bot activity indicators — if THREE or more present, classify as manipulated:
    Volume spike without corresponding price movement
    Accounts with similar creation dates posting simultaneously
    Repeated identical or near-identical phrasing across accounts
    Spike occurs outside normal active hours for the relevant market
    No corresponding organic engagement (likes, replies, shares are minimal)
  Response: IGNORE this signal entirely; do not apply modifier
  Advanced: if manipulation confirmed → brief invert signal may apply
    (manipulated pump = potential dump candidate; apply ×0.96 brief modifier)
    
  AGENT RULE:
    Default to filtering sentiment until classification is confirmed.
    Never apply Type 3 or Type 4 signals to match outcome or demand models.
    When uncertain about type: apply Type 3 (no modifier) as the safe default.
```

---

## Platform weighting

```
PLATFORM SIGNAL WEIGHT TABLE:

  Platform                          Weight   Notes
  ──────────────────────────────────────────────────────────────────────
  Official club channels            ×1.5     Highest authority; no noise
  Verified journalist accounts      ×1.3     Reporting vs opinion — check distinction
  Fan token platform (Socios app)   ×1.2     Direct ecosystem signal; holder-specific
  Community Telegram / Discord      ×1.0     Medium weight; high engagement density
  Twitter / X (verified accounts)  ×1.0     Medium weight; high noise ratio
  Twitter / X (general)            ×0.8     Apply noise filter aggressively
  Reddit                           ×0.8     Lower for real-time; higher for sustained
  Instagram / TikTok               ×0.6     Engagement platform; weak signal source

  APPLICATION:
    When aggregating multi-platform sentiment, apply weights before combining.
    Single high-weight source (official club) > multiple low-weight sources.
    
  REDDIT EXCEPTION:
    Reddit is less reliable for real-time signals (lower ×0.8 weight)
    but more reliable for sustained sentiment patterns (upgrade to ×1.0)
    when the SAME sentiment has persisted across multiple days of threads.
    Upgrade condition: 72+ hours of consistent directional posting on a subreddit.

CROSS-PLATFORM CORRELATION RULE:
  When the same sentiment appears simultaneously across THREE or more platforms:
    Treat as TYPE 1 (structural) regardless of duration
    Apply: ×1.05 or ×0.95 structural modifier immediately
    Do not wait for 72h confirmation — cross-platform confirmation accelerates classification
```

---

## Fan token sentiment specifics

```
GOVERNANCE VOTE ANNOUNCEMENT:
  Engagement spike on governance vote announcement is a POSITIVE demand signal
  regardless of what the vote is about or what the outcome will be.
  Mechanism: governance engagement demonstrates active holder community
  Modifier: ×1.02 demand spike (Type 2 event signal, 48-72h duration)
  Vote close: another smaller spike ×1.01 as result announced
  
  Exception: if governance vote reveals club/platform dysfunction
    (emergency vote, dispute with club, holder backlash) → negative signal
    Apply: ×0.95 (negative structural, sustained until resolution)

MATCH RESULT SENTIMENT ASYMMETRY:
  WIN sentiment decays faster than LOSS sentiment — a documented asymmetry.
  
  WIN sentiment:
    Peak: 24h after result
    Decay: to baseline over 48h
    Modifier: ×1.03 (Type 2 event, 48h maximum)
    
  LOSS sentiment:
    Peak: 24-48h after result (slower peak than WIN)
    Sustained: 48-96h negative period before decay
    Modifier: ×0.97 (sustained Type 2, 96h maximum)
    
  LOSS > WIN asymmetry ratio: approximately 2:1
  (Loss sentiment lasts roughly twice as long as equivalent win sentiment)
  
  HEAVY LOSS (4+ goals, embarrassing defeat):
    Modifier: ×0.93 (deeper Type 2, 5-7 day sustained period)
    Elevated recency bias risk: last result dominates next match signal

TRANSFER ANNOUNCEMENT SENTIMENT:
  Apply transfer window framework (core/transfer-window-intelligence.md)
  for modifier values and duration.
  Platform weight: official club announcement via official channels = immediate ×1.5 weight
  
TROPHY WIN / MAJOR ACHIEVEMENT SENTIMENT:
  Trophy win: Type 1 structural positive signal
  Modifier: ×1.08 sustained over 2-3 weeks (longer than standard event signal)
  Major award (player wins Ballon d'Or, Golden Boot etc.): Type 2 event ×1.05, 5-7 days

SUSTAINED POOR FORM SENTIMENT:
  3+ consecutive league losses creates sustained negative structural sentiment
  Modifier: ×0.93 (Type 1 structural negative)
  Remove when: club wins and 72h of recovered sentiment confirmed
```

---

## Sentiment and signal interaction

```
HOW TO COMBINE SENTIMENT MODIFIERS WITH OTHER SIGNALS:

  ORDER OF OPERATIONS:
    1. Generate base match outcome signal (sport domain + athlete modifiers)
    2. Apply venue and weather modifiers
    3. Apply sentiment modifier LAST — it adjusts the confidence envelope,
       not the directional signal
       
  SENTIMENT DOES NOT OVERRIDE DIRECTION:
    Sentiment is a confidence/demand modifier, not a direction reverser.
    Even strongly negative sentiment (×0.93) does not flip a STRONG signal from HOME to AWAY.
    Exception: sentiment modifier shifts adjusted score enough to cross neutrality threshold
      If base signal is marginal (adjusted score 48-52) AND sentiment applies ×0.93:
      result may cross neutral threshold — acceptable to adjust direction
      
  COMPOUND SENTIMENT CAP:
    Multiple sentiment modifiers apply: cap the combined sentiment effect at:
      Maximum positive: ×1.15 combined
      Maximum negative: ×0.85 combined
    Compound beyond these levels = noisy signal; flag for human review
    
  AGENT RULE:
    Document each sentiment modifier applied and its classification (Type 1/2).
    Never apply Type 3 or Type 4 to any signal calculation.
    Show sentiment modifier separately from base signal in output.
```

---

## Compatibility

**Emotional arc model:** `fan-token/fan-sentiment-intelligence/`
**Transfer sentiment:**  `core/transfer-window-intelligence.md`
**Governance signals:**  `fan-token/governance-intelligence.md`
**CDI framework:**       `fan-token/fan-token-lifecycle/`


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | Social sentiment signals: fan engagement, social media volume, sentiment direction |
| Reasoning | ACTIVE | Sentiment reasoning chain from social signals to CDI and demand modifier |
| Context | ACTIVE | Sentiment context: platform, account type, organic vs bot activity, amplification |
| Memory | ACTIVE | Historical social sentiment baseline patterns for normal vs elevated states |
| Judgment | ACTIVE | Judgment on sentiment signal reliability — bot activity and astroturfing are material risks |
| Attention | ACTIVE | Elevated attention for unusual sentiment spikes near competition events |
| Communication | ACTIVE | Sentiment signal output with platform, volume, direction, and confidence |
| Verification | ACTIVE | Social sentiment signals require bot/manipulation detection before use |
| Learning | EMERGING | Social sentiment calibration from historical volume-to-price correlation |
| Integration | ACTIVE | Integrates with fan token demand intelligence and CHI framework |
| Calibration | EMERGING | Social sentiment calibration is limited — high noise-to-signal ratio |
| Adaptation | ACTIVE | Sentiment intelligence adapts as platform dynamics and fan behaviour evolve |
| Ethics | ACTIVE | Social sentiment about individuals requires care — aggregate signals preferred |
| Transparency | ACTIVE | Sentiment source platform, detection method, and confidence level explicit in output |


---

*SportMind v3.97.28 · MIT License · sportmind.dev*
*Default to Type 3 (no modifier) when sentiment classification is uncertain*
