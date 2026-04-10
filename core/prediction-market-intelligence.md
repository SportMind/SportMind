---
name: prediction-market-intelligence
description: >
  Framework for reading prediction market odds as a confirming or contradicting signal
  for SportMind pre-match analysis. Covers Azuro, Polymarket, and sport-specific
  prediction protocols. Use when an agent needs to compare SportMind's structural
  signal against market consensus, detect divergence between structural intelligence
  and market pricing, or understand how prediction market pool depth affects fan token
  on-chain mechanics. Distinct from fan-token/defi-liquidity-intelligence/ (which covers
  DeFi pool mechanics) — this skill covers prediction market odds as an intelligence
  input, not as an execution layer.
---

# Prediction Market Intelligence — SportMind

**What the market believes, and whether it aligns with what SportMind concludes.**

SportMind generates signals from structured intelligence — sport domain knowledge,
athlete modifiers, macro conditions, disciplinary status. Prediction markets aggregate
the beliefs of many participants and express them as outcome probabilities. These are
different signal sources and they are not always in agreement.

When they agree, conviction is higher. When they diverge, the divergence is itself
a signal — either SportMind has information the market has not priced, or the market
has information SportMind has not incorporated.

This framework teaches agents how to read that comparison correctly.

---

## The fundamental distinction

```
SPORTMIND SIGNAL:
  Source: structured intelligence (domain knowledge, modifiers, calibration)
  Strength: domain expertise, disciplinary intelligence, macro awareness
  Weakness: does not incorporate live betting flow or market participant knowledge

PREDICTION MARKET ODDS:
  Source: aggregated participant beliefs (money-weighted consensus)
  Strength: incorporates all publicly known information; sharp participants
  Weakness: can be manipulated; thin pools less reliable; does not know
            SportMind-specific signals (dew factor, morning skate, etc.)

DIVERGENCE IS THE SIGNAL:
  SportMind says HOME (adjusted_score 68, SMS 82)
  Market says 45% HOME probability (implied odds)
  
  This divergence means one of:
    A) SportMind has structural insight the market underweights
    B) Market has live information SportMind does not have
    C) Normal variance — not every divergence is actionable

HOW TO INTERPRET:
  Small divergence (<10% probability difference): alignment — standard confidence
  Moderate divergence (10-20%): investigate — why does the market disagree?
  Large divergence (>20%): high-conviction signal OR live information missing
```

---

## Prediction market sources

### Azuro — primary SportMind-integrated protocol

```
URL:       azuro.org
Chain:     Polygon, Gnosis Chain (cross-chain)
Coverage:  Football, basketball, MMA, tennis, esports, cricket
API docs:  gem.azuro.org/docs

WHY AZURO FOR SPORTMIND:
  Azuro is the listed integration partner in platform/integration-partners.md
  Decentralised — censorship-resistant, permissionless access to odds
  Pool liquidity transparent on-chain (unlike opaque bookmaker models)
  API available for programmatic odds retrieval

KEY ENDPOINTS:
  GET /api/v1/conditions → available markets for upcoming events
  GET /api/v1/conditions/{id} → outcome probabilities for a specific market
  GET /api/v1/games → all available games with liquidity data

AZURO LIQUIDITY SIGNAL:
  Pool TVL for a specific event = market confidence proxy
  High pool TVL (>$50k): sharp market signal — divergence is meaningful
  Low pool TVL (<$5k): thin market — divergence less reliable
  
  RULE: Never use Azuro odds from a pool with TVL <$5k as a confirming signal.
        Thin pools can be moved by a single participant.
```

### Polymarket — broader market coverage

```
URL:       polymarket.com
Chain:     Polygon
Coverage:  Broader event types including sports, geopolitics, crypto
API:       docs.polymarket.com

FOR SPORTMIND:
  Polymarket covers some high-profile sporting events not on Azuro
  Useful for World Cup 2026 (tournament outcomes, group advancement)
  Less deep on routine league football than Azuro
  
  SIGNAL QUALITY: Polymarket sports markets tend to have fewer participants
  than financial/political markets — lower confidence for niche sports events
```

### Sport-specific prediction markets

```
BETFAIR EXCHANGE (betfair.com):
  Not a prediction market in the crypto sense but functions identically:
  peer-to-peer odds, transparent liquidity, market-driven prices
  Highest global liquidity for football — Betfair is the sharpest market signal
  available for European football. Treat Betfair prices as highest-quality
  market consensus for football analysis.

PINNACLE (pinnacle.com):
  Known as the "sharp bookmaker" — limits winners less than competitors
  Pinnacle closing odds are the best single reference for market consensus
  in football, basketball, and tennis
  Available via odds comparison APIs (OddsPortal, BetBurger)
```

---

## Divergence analysis framework

```
STEP 1: Convert SportMind signal to implied probability
  SportMind adjusted_score 72.4 (HOME) with SMS 82 (HIGH_QUALITY)
  Rough conversion: adjusted_score / 100 = SportMind implied probability
  Example: 72.4 → ~72% HOME probability (SportMind)

STEP 2: Retrieve market implied probability
  From Azuro, Betfair, or Pinnacle: convert decimal odds to probability
  Decimal odds = 1 / probability
  Example: Betfair HOME odds 1.85 → 1/1.85 = 54% probability

STEP 3: Calculate divergence
  SportMind: 72% HOME | Market: 54% HOME
  Divergence: 18 percentage points → MODERATE (investigate)

STEP 4: Apply divergence decision tree

  DIVERGENCE < 10% (alignment):
    Market agrees with SportMind direction
    → Full conviction ENTER (if macro and DSM clear)
    → Divergence provides no additional information

  DIVERGENCE 10-20% (investigate):
    SportMind and market disagree moderately
    POSSIBLE CAUSES — check each:
      a) Did lineup just confirm (SportMind has it, market hasn't priced yet)?
      b) Is there a disciplinary flag market doesn't know about?
      c) Is the dew factor / weather signal active?
      d) Is there a breaking news event post-market open?
    If cause identified and SportMind signal is based on valid information:
      → Proceed with ENTER at slightly reduced sizing (0.85×)
    If no cause identified:
      → Flag divergence_unresolved; do not increase sizing

  DIVERGENCE > 20% (high conviction or missing information):
    EITHER SportMind has strong structural insight
    OR the market has live information SportMind lacks
    
    CHECK FOR LIVE INFORMATION SportMind might be missing:
      → Recent injury announced post-market open
      → Weather change (check Open-Meteo)
      → Breaking news (check core/breaking-news-intelligence.md protocol)
      → Transfer news affecting team morale
    
    If live information explains divergence:
      → Update SportMind analysis with new information
      → Recalculate signal with updated inputs
    
    If no live information found:
      → HIGH CONVICTION opportunity — SportMind structural insight unpriced
      → Proceed with ENTER at standard or increased sizing

  MARKET CONTRADICTS DIRECTION ENTIRELY (>30% divergence, opposite direction):
    Market says HOME 35% (i.e. expects AWAY), SportMind says HOME 72%
    
    This is the highest-stakes divergence scenario.
    
    MANDATORY CHECKS before proceeding:
    □ Is lineup confirmed? (unconfirmed lineup = do not proceed against market)
    □ Is there a disciplinary event SportMind has but market lacks?
    □ Is there active breaking news? (check breaking-news protocol)
    □ Is the sport's primary signal active? (dew factor, morning skate, etc.)
    
    If all checks clear and SportMind signal is based on confirmed information:
      → ENTER at 50% sizing (major divergence = higher uncertainty)
      → Record as potential calibration event regardless of outcome
    
    If any check fails:
      → WAIT — resolve information gap first
```

---

## Gamified tokenomics + prediction market interaction

```
CRITICAL INTERACTION FOR FAN TOKENS:

Standard prediction market: bet on HOME win → settled based on match result
Fan token with gamified tokenomics: WIN = supply burn = price increase

WHEN PREDICTION MARKET AND FAN TOKEN SIGNAL ALIGN:
  Prediction market says HOME likely (70%+)
  Fan token has gamified tokenomics: win = burn = price increase
  RESULT: Double signal — both market consensus AND supply mechanics support

WHEN PREDICTION MARKET AND FAN TOKEN SIGNAL DIVERGE:
  Prediction market says AWAY likely (HOME only 30%)
  Fan token signal says ENTER (based on narrative/sentiment not match outcome)
  
  RESOLUTION: Fan token signal is not purely about match outcome
  → Fan sentiment can be elevated pre-match regardless of predicted outcome
  → A team's fan token can be in commercial elevation even when the team is predicted to lose
  → Prediction market odds relate to match result, not fan token commercial signal

THE CORRECT FRAMEWORK:
  Pre-match fan token signal: driven by sporting context + commercial sentiment
  Post-match fan token signal: driven by actual result + NCSI + CDI
  
  Prediction market odds are inputs to pre-match analysis (what outcome is likely?)
  They are NOT a substitute for the fan token commercial signal framework.
  
  Use prediction markets to:
    → Calibrate match outcome probability (confirming/contradicting sportmind_pre_match)
    → NOT to generate fan token commercial signals directly

See: fan-token/gamified-tokenomics-intelligence/ for full supply mechanics framework
```

---

## Pool depth as market quality signal

```
PREDICTION MARKET POOL DEPTH TABLE:

Pool TVL > $500k:
  Market quality: INSTITUTIONAL — treat as highest-quality market signal
  Azuro/Betfair equivalent: sharp market
  Use: full weight as confirming/contradicting signal

Pool TVL $50k-$500k:
  Market quality: RETAIL — solid signal with some noise
  Use: standard weight (0.85×) as confirming signal

Pool TVL $5k-$50k:
  Market quality: THIN — directionally useful, not quantitatively reliable
  Use: directional signal only (0.5× weight); do not calculate precise divergence

Pool TVL <$5k:
  Market quality: NEGLIGIBLE — a single participant can move this market
  Use: ignore as signal; note that market exists but do not use odds

RULE: Always check pool TVL before using prediction market odds as a SportMind input.
      See: fan-token/defi-liquidity-intelligence/ for full pool depth framework.
```

---

## Integration with SportMind skills

```
WHERE PREDICTION MARKET INTELLIGENCE FITS IN THE FIVE-PHASE CHAIN:

PHASE 2 — Pre-match signal:
  After sportmind_pre_match generates direction:
  → Retrieve Azuro/Betfair odds for the same event
  → Calculate divergence
  → Apply divergence decision tree
  → Adjust sizing or flag for investigation

PHASE 5 — Signal synthesis:
  Include market_divergence in final signal output:
  {
    "sportmind_direction": "HOME",
    "market_implied_prob":  0.54,
    "sportmind_implied_prob": 0.72,
    "divergence":           0.18,
    "divergence_tier":     "MODERATE_INVESTIGATE",
    "divergence_resolved": true,
    "resolution_note":     "Lineup confirmed post-market open — SportMind had confirmed info"
  }

FEEDS INTO:
  fan-token/defi-liquidity-intelligence/   → pool depth as market quality input
  fan-token/gamified-tokenomics-intelligence/ → supply mechanics interaction
  core/confidence-output-schema.md         → divergence field in output schema

USES:
  platform/api-providers.md               → Azuro API access
  core/breaking-news-intelligence.md      → checking for live info causing divergence
  platform/fetch-mcp-disciplinary.md      → verifying disciplinary info market lacks
```

---

*SportMind v3.43 · MIT License · sportmind.dev*
*Azuro docs: gem.azuro.org/docs · Polymarket docs: docs.polymarket.com*
*See also: fan-token/defi-liquidity-intelligence/ · fan-token/gamified-tokenomics-intelligence/*
*core/core-result-impact-matrices.md · platform/api-providers.md*
