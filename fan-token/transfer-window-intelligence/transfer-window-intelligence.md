---
name: transfer-window-intelligence
description: >
  Transfer window calendar intelligence — the structural signal patterns that repeat
  annually around football transfer windows, independent of any specific transfer.
  Use when an agent needs to adjust fan token signals during an active transfer window,
  reason about deadline day volatility, understand the six-week summer window elevation
  pattern, or apply transfer window modifiers to commercial signals. Distinct from
  fan-token/transfer-intelligence/ (which covers individual transfer events) — this
  skill covers the window itself as a recurring market condition. Load alongside
  fan-token/football-token-intelligence/ and fan-token/fan-token-pulse/.
---

# Transfer Window Intelligence — SportMind

**The transfer window is a recurring market condition, not just a series of events.**

Every January and every summer, the football transfer market opens and creates a
structural change in the fan token signal environment that applies to all clubs
simultaneously — not just those involved in specific transfers. An agent that treats
transfer windows as neutral periods and waits for individual transfer news is missing
the structural signal that the window itself generates.

---

## Why transfer windows are a distinct signal layer

```
STANDARD COMMERCIAL SIGNAL:
  Fan token price moves on: match results, athlete performances,
  KOL content, governance events, macro conditions

TRANSFER WINDOW ADDS:
  → Speculation premium: anticipation of potential signings
  → Departure risk discount: fear of losing key commercial asset
  → Deadline day volatility: highest single-day HAS variance of the year
  → Post-window certainty relief: squad confirmed, signal stabilises
  → Cross-token contagion: one big transfer affects multiple club tokens

None of these require a transfer to actually happen.
The window itself changes the commercial signal environment.
```

---

## Transfer window calendar

### Summer window (primary window)

```
DATES (football — varies slightly by league):
  Premier League: July 1 – September 1
  La Liga:        July 1 – September 1
  Bundesliga:     July 1 – September 1
  Serie A:        July 1 – September 1
  Ligue 1:        July 1 – September 1
  Saudi Pro League: July 1 – September 25 (extended)

SIGNAL PHASES WITHIN SUMMER WINDOW:

PHASE A — Pre-window anticipation (June 1–30):
  Duration: ~30 days
  Signal: Speculation premium begins building
  HAS modifier: +0% to +5% (subdued — no official activity yet)
  Agent action: Monitor rumour velocity; do not apply full modifier yet

PHASE B — Window open, early period (July 1–31):
  Duration: ~31 days
  Signal: First signings confirmed; early departures announced
  HAS modifier: +3% to +8% for buying clubs
  Departure risk discount: -2% to -6% for clubs losing key ATM players
  Agent action: Apply window modifier; track ATM player departure risk

PHASE C — Peak speculation period (August 1–25):
  Duration: ~25 days
  Signal: Maximum speculation; biggest rumours emerge; media saturation
  HAS modifier: +5% to +12% for clubs linked to major signings
  Rumour premium: treat verified journalist reports as +3–5% directional
  TRAP: Rumour premium reverses sharply if deal falls through
  Agent action: Use source tier framework; Tier 1 journalist minimum for modifier

PHASE D — Deadline day (August 31 / September 1):
  Duration: ~48 hours
  Signal: MAXIMUM VOLATILITY — highest single-day HAS variance of year
  HAS modifier: unpredictable; swings of -15% to +20% within hours
  
  DEADLINE DAY RULES:
    DO NOT generate new ENTER signals in final 6h before deadline
    Any confirmed last-minute signing: +8–18% (excitement premium)
    Any confirmed last-minute departure: -8–15% (loss discount)
    Failed deal (announced then collapsed): -3–8% (disappointment penalty)
    
  AGENT BEHAVIOUR ON DEADLINE DAY:
    Set recommended_action to WAIT for all affected tokens 6h before deadline
    Resume normal analysis 24h after deadline closes

PHASE E — Post-window (September 2 onwards):
  Duration: ~4 months (until January window)
  Signal: Certainty premium — squad is known, stability signal
  HAS modifier: +2% to +5% for clubs who strengthened
  HAS modifier: -1% to -3% for clubs who failed to address known weaknesses
  Agent action: Return to standard pre-match signal model
```

---

### January window (secondary window)

```
DATES: January 1 – February 1 (all major leagues)

JANUARY WINDOW IS STRUCTURALLY DIFFERENT FROM SUMMER:
  Smaller market: fewer clubs buying; fewer players available
  Higher prices: sellers hold leverage (only one buyer window left in season)
  Distress signings: clubs in trouble buy; creates negative signal context
  Mid-season disruption: new signing needs time to integrate

JANUARY-SPECIFIC SIGNAL ADJUSTMENTS:
  Apply 60% of summer window modifiers (smaller market, less activity)
  Deadline day volatility: approximately 70% of summer deadline day
  Distress buying signal: club buying in January often signals squad crisis
    → If a Tier 1 token club buys multiple players in January: investigate
    → Why do they need January signings? Form signal concern.

JANUARY WINDOW MODIFIER TABLE:
  Major signing confirmed (Tier 1 ATM player):     +6–12%
  Key player departure confirmed:                  -6–12%
  Distress buying pattern (3+ signings):           -2–4% (concern flag)
  Window closes with squad unchanged:              +1–2% (stability signal)
```

---

## Cross-token contagion

```
DEFINITION: When one club's transfer activity affects the tokens of OTHER clubs.

TYPE 1 — SELLING CLUB SIGNAL:
  Club A sells key ATM player to Club B
  Club A token: -6–15% (losing commercial asset)
  Club B token: +4–12% (gaining commercial asset)
  This is the most common cross-token transfer pattern.

TYPE 2 — COMPETITOR STRENGTHENING:
  Club A's rival signs a star player
  Club A may face competitive pressure
  Club A token: -1–3% (indirect competitive signal)
  This is subtle and often missed by standard models.

TYPE 3 — MARKET VALUATION SIGNAL:
  A major transfer sets a new market value benchmark
  All players of similar profile see APS recalibration
  Indirect effect on all clubs potentially selling similar players

TYPE 4 — LEAGUE-WIDE TRANSFER NARRATIVE:
  If 3+ major signings happen in the same week:
  Entire league's token market elevates on excitement/engagement signal
  Apply +1–3% to ALL active tokens in that league for 48h

CROSS-TOKEN MONITORING:
  Run sportmind_fan_token_lookup for sport="football" to get all football tokens
  After any major transfer confirmation: check cross-token exposure for all held tokens
  See platform/memory-integration.md for storing cross-token relationships
```

---

## Transfer window and fan token lifecycle interaction

```
LIFECYCLE PHASE INTERACTION:

PHASE 3 TOKEN (Active utility) + Strong summer window:
  Club buys ATM players → FTIS elevates → sustained HAS
  Most positive combination for fan token commercial signal

PHASE 3 TOKEN + Weak summer window (key player sold, no replacement):
  ATM degradation signal → immediate HAS decline
  May indicate Phase 4 drift beginning
  Monitor holder count trend for 30 days post-window

PHASE 4 TOKEN (Utility plateau) + Summer window activity:
  Major signing can temporarily reverse plateau signal
  But if Phase 4 drift is structural, signing impact decays faster than Phase 3
  CDI for Phase 4 token post-signing: 50% of Phase 3 equivalent

PHASE 5/6 TOKEN + Any transfer activity:
  Club is no longer an active token partner — transfer has minimal impact
  Standard transfer window modifiers do not apply

RULE: Always check lifecycle phase (sportmind_fan_token_lookup) before
applying transfer window modifier. Phase 4/5/6 tokens respond differently.
```

---

## World Cup 2026 transfer window overlap

```
UNIQUE 2026 CALENDAR SITUATION:
  World Cup: June 11 – July 19, 2026
  Summer transfer window: July 1 – September 1, 2026

OVERLAP PERIOD: July 1–19 (World Cup knockout phase + window open)

THIS CREATES A DUAL SIGNAL:
  Player performing well in World Cup knockout rounds
  = simultaneously a World Cup NCSI signal AND a transfer value signal
  
  A player scoring in a World Cup semi-final on July 18
  is also a player whose transfer market value is rising in real-time
  with the window already open.

AGENT PROTOCOL FOR OVERLAP PERIOD:
  Apply BOTH World Cup NCSI signal AND transfer window modifier
  Composite: World Cup NCSI (x3.5) + transfer speculation premium
  
  Example:
    Player A scores hat-trick in WC semi-final → NCSI +15–20% club token
    Same player immediately linked to transfer by Tier 1 journalist
    Apply: NCSI signal FIRST, then transfer speculation as additive signal
    Do not double-count: maximum combined uplift cap 1.25x either signal alone
  
  Post-tournament (July 20 onwards):
    World Cup NCSI persists for 45 days for winner squad members
    Transfer window continues until September 1
    Monitor: does the transfer happen or not? Confirmation vs failed bid
    affects final commercial signal significantly
```

---

## Verifiable sources for transfer window intelligence

```
TIER 1 (ground truth — confirmed transfers only):
  Club official announcements (website, official X account)
  League registration confirmations (PL, La Liga, Serie A official sites)

TIER 2 (reliable directional signal):
  Fabrizio Romano (@FabrizioRomano) — "here we go" = confirmed
  The Athletic (verified investigative journalism)
  Sky Sports Transfer Centre (deadline day — fastest confirmed reporting)
  Trusted beat reporters for specific clubs (verify via track record)

TIER 3 (usable with caution — apply 50% modifier weight):
  Unnamed "sources close to the club" reports
  Italian and Spanish media (often speculative; verify with Romano)
  Club-linked social media accounts (not official)

TIER 4 (do not use):
  Anonymous social media accounts
  Transfer market aggregators without named sources
  Fan forums and speculative threads

RULE: Apply transfer window signal modifiers ONLY at Tier 1 or Tier 2 confirmation.
      Tier 3 sources = flag for monitoring; do not modify signal.
```

---

## Integration with SportMind skills

```
FEEDS INTO:
  fan-token/football-token-intelligence/    → FTIS adjustment during window
  fan-token/fan-token-lifecycle/            → Phase 3/4 drift detection
  fan-token/transfer-intelligence/          → Individual transfer analysis
  fan-token/transfer-signal/               → APS and TVS calculations

USES:
  core/breaking-news-intelligence.md        → Deadline day news protocol
  core/media-intelligence.md                → Journalist source tiers
  platform/memory-integration.md            → Store window state per token
  platform/fetch-mcp-disciplinary.md        → Verify transfer via official source

MODIFIER APPLICATION ORDER:
  macro_modifier FIRST (gates everything)
  × DSM modifier (if applicable)
  × transfer_window_modifier (this skill)
  × lineup/availability modifier
  = composite_modifier applied to base signal
```

---

*SportMind v3.40 · MIT License · sportmind.dev*
*See also: fan-token/transfer-intelligence/ · fan-token/football-token-intelligence/*
*core/breaking-news-intelligence.md · core/media-intelligence.md*
*fan-token/world-cup-2026-intelligence/ (2026 window overlap)*
