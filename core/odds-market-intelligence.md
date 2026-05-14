---
name: odds-market-intelligence
description: >
  Enduring reasoning framework for betting market signals as pre-match intelligence
  inputs. Covers odds signal classification, line movement patterns, sharp vs public
  money, reverse line movement, fan token connection, and integrity signal interaction.
  SportMind does not facilitate betting — odds are used as signal inputs only.
---

# Odds and Market Intelligence

**How to reason about betting market signals as pre-match intelligence inputs.**
Odds reflect collective information aggregation — not a betting recommendation.

> IMPORTANT FRAMING:
> SportMind does not facilitate betting. Odds are used as a signal input only —
> a reflection of how professional and informed market participants collectively
> assess match probability. This is a pre-match intelligence framework.

---

## Why odds matter as signals

```
THE INFORMATION AGGREGATION PRINCIPLE:

  Betting markets aggregate information from thousands of participants including
  professional analysis teams, statistical models, and insider-adjacent knowledge.
  
  SIGNAL VALUE:
    Significant line movements often precede confirmed news by hours or days.
    The odds signal is not the news — it is the market's reaction to information
    that may not yet be publicly confirmed.
    
  LIMITATION:
    Odds reflect market consensus and market manipulation risk.
    They are a supplementary signal — not a replacement for SportMind's
    layer-by-layer analysis.
    Cross-reference: if odds diverge significantly from SportMind adjusted score,
    check for missing modifiers before applying an odds-based adjustment.
    
  HOW TO USE:
    1. Identify the implied probability from the odds
    2. Compare to SportMind adjusted score (converted to probability)
    3. If divergence > 15 points: investigate — either SportMind has missing
       information or the odds market has noise/error
    4. Apply appropriate confidence adjustment based on the source
```

---

## Odds signal classification

```
OPENING LINE SIGNAL:

  SIGNIFICANT DIVERGENCE FROM SPORTMIND ADJUSTED SCORE:
    If odds imply probability >15 percentage points ABOVE SportMind score:
      Signal: market has information not captured in SportMind inputs
      Action: review all active modifiers; check for confirmed news not yet
        processed; flag as INPUTS_REVIEW_REQUIRED
      
    If odds imply probability >15 percentage points BELOW SportMind score:
      Signal: SportMind may hold an informational advantage
      Action: verify all modifiers are correctly applied; if confirmed correct,
        maintain SportMind signal — do not automatically defer to market

LINE MOVEMENT SIGNAL CLASSIFICATION:

  SHARP MOVEMENT:
    Definition: rapid, large, sustained movement (10+ percentage points in
      implied probability within 6 hours)
    Profile: professional money indicator — informed participants acting
    Modifier: sharp_movement_confidence = ×1.08 to direction aligned with movement
    Cross-reference: does the movement align with a SportMind signal already present?
      If yes: high confidence — signals are corroborating
      If no: strong trigger for inputs review
      
  PUBLIC MONEY MOVEMENT:
    Definition: gradual, small, consistent movement aligned with public betting
    Profile: recreational bettor activity — lower signal value
    Modifier: public_money_confidence = ×0.90 — discount this movement type
    Mechanism: public money moves markets but does not reflect sharp information
    
  REVERSE LINE MOVEMENT:
    Definition: odds move OPPOSITE to the public betting percentage
    Example: 70% of bets on Team A, but odds move to favour Team B
    Profile: strong professional money indicator — significant sharp action
    Modifier: reverse_line_confidence = HIGH confidence signal
    Treat as equivalent to sharp movement in confidence weight (×1.08)
    
  NO MOVEMENT (line holds despite public action):
    Books are comfortable with their position.
    Typically indicates balanced action or confident market assessment.
    No modifier — treat as neutral confirmation of existing signal.
```

---

## Fan token connection

```
FOR $AFC (FTP PATH_2):

  SHARP MOVEMENT TOWARD ARSENAL WIN:
    Recalculate supply event estimates using the updated WIN probability.
    If sharp movement increases implied WIN probability by X%:
      Adjust burn pool estimate proportionally (WIN prob × multiplier range)
    Communicate: revised net expected supply change with updated probability
    
  SHARP MOVEMENT TOWARD ARSENAL LOSS OR DRAW:
    Mint event estimate increases | DRAW = no supply change
    Adjust supply event probability distribution accordingly.
    
  NOTE: Odds movement does NOT change the pre-liquidation pool size (circulating
    supply ÷ 400). It only changes the probability weighting applied to
    burn vs mint vs neutral outcomes.

FOR DEMAND-ONLY TOKENS:

  SHARP MOVEMENT TOWARD CLUB WIN:
    Pre-match demand premium signal: ×1.05 for that token on match day
    Mechanism: market consensus aligns with positive outcome — demand amplified
    Duration: match day signal only; result then drives standard demand framework
    
  SHARP MOVEMENT TOWARD CLUB LOSS:
    Pre-match demand pressure: ×0.96 for that token on match day
    Duration: match day signal only
    
  AGENT RULE:
    Odds-based demand modifiers apply on match day only.
    Do not carry odds-derived modifiers beyond T+2h post-match.
    Post-match: result-based demand framework takes over entirely.
```

---

## Integrity and manipulation signals

```
SUSPICIOUS ODDS MOVEMENT SIGNALS:

  HIGH-RISK PATTERNS:
    · Very large movement on obscure/small exchange NOT reflected on major markets:
      Manipulation risk — do not apply as signal; flag for integrity review
      
    · Movement concentrated in one jurisdiction only with no global market reflection:
      Local manipulation risk signal — apply ×0.70 confidence weight maximum
      
    · Movement on markets with documented integrity issues:
      Elevated risk — require corroboration from Tier 1 major market before applying
      
CROSS-REFERENCE WITH SPORTS INTEGRITY INTELLIGENCE:

  If suspicious odds movement coincides with:
    A competition in sports-integrity-intelligence.md Tier 3 (elevated risk)
    AND a dead rubber match context
    AND/OR a team with documented fixing history in that competition:
    → Apply INTEGRITY_TRIPLE_FLAG = HOLD signal
    → Do not produce directional signal
    → Flag for review from sports integrity organisations (primary sources)
    
  AGENT RULE:
    Odds divergence alone is not an integrity signal.
    Integrity signals require: suspicious movement + competition context + absence of news.
    See: core/sports-integrity-intelligence.md for full integrity framework.
```

---

## Compatibility

**Integrity signals:**       `core/sports-integrity-intelligence.md`
**PATH_2 supply events:**    `fan-token/ftp-path2.md`
**Demand modifiers:**        `core/fan-token-context-bridge.md`
**Confidence framework:**    `core/signal-confidence-framework.md`

---

*SportMind v3.97.46 · MIT License · sportmind.dev*
*Sharp movement + SportMind signal alignment = high confidence corroboration.*
*Odds diverge significantly from SportMind? Check inputs before deferring to market.*
