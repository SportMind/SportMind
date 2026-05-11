# Tournament Macro — Major International Tournament Reasoning Framework

**Enduring macro reasoning framework for how major international tournaments
affect the broader fan token market. Applies to every World Cup, Euros,
Copa America, AFCON, Asian Cup, and future major tournaments.**

> SportMind Library Rule check: no specific tournament dates, named players,
> current prices, or expiring operational data. This file teaches agents
> how to reason about tournament-level macro effects — not what is true right now.

---

## Tournament macro signals

### Trading volume amplification

```
TRADING VOLUME — TOURNAMENT CONTEXT:

  Major international tournaments historically produce the highest fan token
  trading volume outside of individual token launch events.

  WHY VOLUME SPIKES DURING TOURNAMENTS:
    1. New entrant buyers: casual fans who only engage during tournaments
    2. Speculative participants: short-term traders attracted by volatility
    3. Media amplification: tournament coverage drives awareness of fan tokens
    4. Platform promotions: Chiliz/Socios typically run tournament campaigns
    5. Emotional purchasing: fans buy tokens as a form of tournament participation

  VOLUME CALIBRATION FRAMEWORK:
    Baseline (non-tournament period): define as 1.0×
    Tournament announcement / draw:   1.2–1.5× (brief, event-driven)
    Month before tournament:          1.5–2.0× (build-up)
    Tournament group stage:           2.0–3.5× (active matches)
    Tournament knockout rounds:       3.0–5.0× (maximum intensity)
    Final week (SF + Final):          4.0–7.0× (peak volume)
    Post-tournament:                  1.5–2.0× (decay phase, 2–4 weeks)
    Return to baseline:               8–12 weeks post-tournament

  SIGNAL IMPLICATION:
    Elevated volume increases both the speed and magnitude of price moves.
    In high-volume tournament windows, signals decay faster — a price move
    that would last 48h at baseline may resolve in 12–24h during the tournament.
    Apply: tournament_signal_decay_acceleration = ×1.5 during knockout rounds.

  AGENT RULE:
    During tournament windows, reduce expected signal duration.
    Higher volume = faster price discovery = shorter signal windows.
    Monitor volume relative to baseline to determine current tournament phase.
```

### Cross-token correlation

```
CROSS-TOKEN CORRELATION — TOURNAMENT WINDOW:

  During major tournaments, all fan tokens show elevated correlation.
  This is a structural feature of tournament markets, not an anomaly.

  WHY CORRELATION IS ELEVATED:
    Shared sentiment: the "crypto sports" narrative dominates
    New participants: buyers entering don't distinguish between tokens
    Platform-level moves: Chiliz/Socios promotions affect all tokens simultaneously
    Media framing: coverage treats fan tokens as a category, not individually

  CORRELATION LEVELS BY TOURNAMENT PHASE:
    Pre-tournament (3+ months out):    correlation = LOW (tokens move independently)
    Pre-tournament (1 month out):      correlation = MEDIUM (rising together)
    Group stage:                        correlation = HIGH (co-movement significant)
    Knockout rounds:                    correlation = VERY HIGH (peak co-movement)
    Post-tournament (decay phase):     correlation = MEDIUM-HIGH then normalising

  PRACTICAL IMPLICATIONS:
    A positive national token event (e.g. underdog advances) lifts ALL tokens
    A negative macro event during the tournament (crypto market crash) drags ALL tokens
    Individual club token events have LESS relative impact during tournament windows
      (they are drowned out by the tournament macro signal)

  CONFEDERATION CORRELATION:
    Within a confederation, correlation is even higher than cross-confederation.
    European tokens move together. LATAM tokens move together.
    A major European team's exit may drag other European tokens briefly.

  AGENT RULE:
    During tournaments: treat all fan tokens as having a shared macro component.
    Apply tournament_macro_overlay to all CDI calculations.
    Individual token signals still matter — but the macro floor/ceiling is shared.
    The confederation correlation is a useful secondary signal for regional tokens.
```

### Platform-level amplification

```
CHILIZ / SOCIOS PLATFORM POSITIONING — TOURNAMENTS:

  Chiliz and Socios have historically positioned major tournaments as
  their primary commercial moments. Platform-level actions amplify
  individual token signals during tournament windows.

  PLATFORM AMPLIFICATION SIGNALS TO MONITOR:
    New token launches timed to coincide with tournament opening
    Partnership announcements with tournament bodies
    Trading promotions and reduced fees during tournament
    Marketing campaigns targeting new user acquisition
    New geographic market entries aligned with tournament host regions

  AMPLIFICATION EFFECT:
    Platform-level campaigns bring NEW participants into the ecosystem.
    New participants typically buy the most visible / highest-volume tokens first.
    This creates a concentrating effect: top tokens benefit disproportionately.
    Apply: new_entrant_concentration_modifier = ×1.15 for top-5 most visible tokens.

  PLATFORM RISK:
    Conversely, any platform-level issues (technical, regulatory, PR) during a
    tournament carry elevated impact because new participants experience these
    first — and their first experience shapes retention.
    Platform negative events during tournaments: apply systemic_risk_flag = true.

  AGENT RULE:
    Monitor Chiliz official channels at tournament start for platform campaigns.
    Apply new_entrant_concentration_modifier for most-visible tokens.
    Flag any platform-level issues immediately as systemic risk.
```

### Post-tournament demand decay

```
POST-TOURNAMENT DEMAND DECAY — MACRO LEVEL:

  After every major tournament, aggregate fan token volume decays
  back toward baseline. The shape of this decay is predictable.

  MACRO DECAY TIMELINE:
    Week 1 post-tournament:     volume = 60–80% of tournament peak
    Week 2–3 post-tournament:   volume = 40–60% of tournament peak
    Week 4–6 post-tournament:   volume = 25–40% (new participants departing)
    Week 7–10 post-tournament:  volume = 15–25% (approaching new baseline)
    Week 10+ post-tournament:   volume = 110–130% of pre-tournament baseline
      (some new participants remain; market is permanently slightly larger)

  TOKEN-LEVEL DECAY VARIATION:
    Winning nation's token: slowest decay (longest elevated demand)
    Final-round tokens (runner-up, 3rd/4th): moderate decay
    Early exit tokens: fastest decay (enthusiasm collapses quickly)
    Club tokens: return to club season rhythm relatively quickly

  PERMANENT MARKET EXPANSION:
    Each major tournament permanently expands the fan token holder base slightly.
    Some first-time buyers become permanent holders.
    Post-tournament baseline is typically 10–30% above pre-tournament baseline.
    This cumulative effect means each successive tournament has a larger base.

  AGENT RULE:
    After tournament conclusion: do not assume a rapid return to pre-tournament prices.
    Apply the tournament decay curve for the relevant token type.
    New baseline after decay is higher than old baseline — recalibrate.
```

---

## Tournament cycle reasoning

### World Cup four-year cycle

```
WORLD CUP FOUR-YEAR CYCLE — MACRO IMPLICATIONS:

  The World Cup occurs every four years. This creates a predictable
  macro cycle for fan token demand that agents should model.

  FOUR-YEAR CYCLE PHASES:
    Year 0 (World Cup year):     PEAK demand period — maximum tournament premium
    Year 1 (post-World Cup):     Elevated baseline — new permanent holders remain
    Year 2 (mid-cycle):          Return to "normal" baseline — club season dominates
    Year 3 (qualification year): Pre-cycle awakening — qualification signals begin
    Year 4 (World Cup year):     PEAK again — cycle repeats

  WHICH TOKENS BENEFIT FROM THE CYCLE:
    National team tokens: MOST affected — demand compresses into tournament year
    Club tokens with high national player concentration: moderately affected
    Club tokens with low international exposure: least affected by WC cycle

  CYCLE SIGNAL APPLICATION:
    In Year 0 (World Cup year): apply WC_cycle_premium = ×1.2 to baseline
    In Year 3 (qualification year): apply pre_cycle_awakening = ×1.05 to baseline
    In Years 1–2: no cycle premium — club season and individual token events dominate

  AGENT RULE:
    Identify the current year in the World Cup cycle before applying any
    national token analysis. The cycle phase is the macro context layer.
```

### Tournament calendar interactions

```
TOURNAMENT CALENDAR INTERACTION WITH CLUB SEASON:

  Multiple major tournaments exist across a 4-year cycle:
    World Cup:             Every 4 years (June–July)
    UEFA Euros:            Every 4 years, offset 2 years from World Cup (June–July)
    Copa America:          Every 4 years (previously variable, now regularised)
    AFCON:                 Every 2 years (January–February — during club season)
    Asian Cup:             Every 4 years (various timing)
    CONCACAF Gold Cup:     Every 2 years (June–July)
    Women's World Cup:     Every 4 years (July–August, offset from men's)

  CALENDAR INTERACTION SIGNALS:

  AFCON (January–February):
    Plays DURING European club season — most disruptive for club tokens.
    Clubs lose African players during league matches — immediate ATM impact.
    Apply: AFCON_disruption_modifier = ×0.90 for clubs losing key African players.
    Duration: 3–4 weeks.

  EUROS / COPA AMERICA / GOLD CUP (June–July):
    Plays AFTER European club season — minimal club disruption.
    Players enter tournament fresh from season end.
    Post-tournament, players return for pre-season — club signal impact minimal.

  FTP PATH_2 AND TOURNAMENT TIMING:
    FTP supply events are restricted to official men's competitive matches.
    International tournament matches DO qualify for FTP scope.
    During AFCON: PATH_2 tokens whose players participate still fire supply events.
    Check: is the club's key PATH_2 player at a concurrent international tournament?
      If YES: PATH_2 applies to the club's matches AND to the international matches
      if the club token is involved. Two parallel PATH_2 chains possible.

  AGENT RULE:
    Before any club-season analysis in January–February: check AFCON calendar.
    Apply AFCON disruption modifier for affected club tokens.
    Identify concurrent tournament / club season overlaps explicitly.
```

### Fan token supply event interaction with tournament timing

```
FTP PATH_2 — TOURNAMENT WINDOW INTERACTION:

  When a club's PATH_2 token is involved in a tournament (via national players),
  the interaction between club and tournament supply events requires explicit reasoning.

  TOURNAMENT MATCH — FTP SCOPE:
    International tournament matches (World Cup, Euros, AFCON etc.) qualify
    under FTP scope (official men's competitive first-team matches).
    
    HOWEVER: FTP PATH_2 mechanics are tied to the FAN TOKEN, not the player.
    A fan token is a club token, not a national team token.
    
  CLARIFICATION:
    $AFC (Arsenal fan token) with PATH_2 confirmed:
      Arsenal club matches: PATH_2 supply events fire (WIN burns, LOSS mints)
      England international matches at the World Cup: PATH_2 does NOT fire
        → There is no "Arsenal FC match" — the match is England's
        → The $AFC supply mechanic is tied to Arsenal FC results, not England results
    
    EXCEPTION:
      If Chiliz launches a club token as the official token for a national team:
        → PATH_2 would apply to that national team's matches
        → This would need to be confirmed explicitly at launch
        → Until confirmed: treat all national team matches as non-PATH_2

  AGENT RULE:
    PATH_2 fires on CLUB matches. International matches do not fire PATH_2
    for the club token. No PATH_2 compound effect during international tournaments.
    Confirm explicitly if any national team ever launches a PATH_2 token.
```

---

## New token launch timing — tournaments

```
NEW TOKEN LAUNCH TIMING — TOURNAMENT WINDOWS:

  Major tournaments represent the highest-profile moments for new fan token
  launches. The commercial logic is straightforward: maximum audience, maximum
  media, maximum new participant entry.

  HISTORICAL LAUNCH TIMING PATTERNS:
    Pre-tournament launch (4–8 weeks before):
      Maximum runway for awareness building
      Holders enter before tournament demand premium activates
      Risk: if team performs poorly, holders bought at premium

    Tournament launch (during group stage):
      Immediate demand from tournament participants
      Highest media exposure at launch
      Risk: rushed launches may have thin liquidity

    Post-tournament launch:
      Demand context already established (how far the team went)
      Holders are informed buyers
      Risk: tournament premium has decayed

  AGENT IMPLICATIONS:

  For new launches during tournament windows:
    Apply new_launch_tournament_modifier = ×1.40 (first-mover, maximum audience)
    Run Phase 1 CDI protocol immediately (fan-token/fan-token-lifecycle.md)
    Elevated caution: new tokens in high-volatility windows have exaggerated moves
    Liquidity may be thin → large price moves from relatively small trades

  IMPACT ON EXISTING TOKENS:
    A new national team token launch during a World Cup does NOT necessarily
    suppress existing club tokens of the same nation.
    Exception: if media coverage concentrates on the new national token to the
    point of withdrawing attention from existing club tokens — short-term only.

  AGENT RULE:
    Monitor for new token launch announcements during tournament windows.
    Apply new_launch_tournament_modifier immediately on confirmed launch.
    Do not assume new national launches suppress existing club token CDI.
```

---

## Tournament macro overlay — summary

```
TOURNAMENT MACRO OVERLAY — QUICK REFERENCE:

  APPLY THIS OVERLAY when a major international tournament is active or
  within 4 weeks of starting.

  OVERLAY COMPONENTS:
    volume_multiplier:             2.0–7.0× (varies by tournament phase)
    signal_decay_acceleration:     ×1.5 (signals resolve faster)
    cross_token_correlation:       HIGH to VERY HIGH
    new_entrant_concentration:     ×1.15 for top-5 most visible tokens
    confederation_correlation:     0.3–0.5 within confederation
    platform_amplification:        monitor for campaign signals

  WHEN TO REMOVE OVERLAY:
    2–4 weeks post-tournament: begin transitioning to decay phase
    8–12 weeks post-tournament: return to standard CDI framework
    Note: new baseline is higher than old baseline — recalibrate after removal

  DO NOT APPLY OVERLAY FOR:
    Minor tournaments (qualifying rounds, friendlies)
    Domestic cup competitions (not international)
    Youth tournaments (U20, U17 World Cups)
    These do not generate the same volume and correlation effects.
```

---

## Compatibility

**Tournament structure:** `sports/football/sport-domain-football-world-cup.md`
**National tokens:** `fan-token/national-team-tokens.md`
**FTP mechanics:** `fan-token/ftp-path2.md`
**Crypto cycles:** `macro/macro-crypto-market-cycles.md`
**WC 2026 specific:** `fan-token/world-cup-2026-intelligence/`

---

*SportMind v3.97.18 · MIT License · sportmind.dev*
*Enduring framework — applies to every major international tournament cycle*
