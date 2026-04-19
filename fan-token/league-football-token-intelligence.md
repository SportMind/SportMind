---
name: league-football-token-intelligence
description: >
  League-specific fan token signal intelligence for the seven token-active
  football leagues. Covers domestic result sensitivity, European competition
  multipliers, transfer window signal patterns, post-WC2026 squad fatigue
  protocols, and the unique signal architecture of each league's token
  ecosystem. Distinct from football-token-intelligence/ (which covers
  the token mechanics and FTIS framework) and football-leagues-advanced.md
  (which covers competition stakes and prize windows). This file covers
  the league-level token dimension that neither of those files addresses:
  how each league's structure, calendar, and competitive dynamics translate
  into token-specific signal patterns.
---

# League Football Token Intelligence

**Seven leagues. 63 active Chiliz tokens. Distinct signal architectures.**

The FTIS framework and NCSI model in `fan-token/football-token-intelligence/`
apply universally. This file covers what the universal framework cannot: why
a $GAL match in the Turkish Süper Lig behaves differently from a $BAR match
in La Liga, even when the competition tier weight is identical. Each league
has a token ecosystem fingerprint. Understanding those fingerprints is the
difference between a generic football signal and a precise one.

---

## Why league token ecosystems differ

```
THE SAME FTIS SCORE MEANS DIFFERENT THINGS IN DIFFERENT LEAGUES:

FTIS 65 in the Premier League:
  Likely a mid-table match with a top-4 or relegation sub-narrative
  Token holders: globally distributed, English-neutral, mixed archetypes
  Signal decay: 48h — international holder base moves on quickly

FTIS 65 in the Turkish Süper Lig:
  Likely a Galatasaray or Trabzonspor match with title implications
  Token holders: 70–80% Turkish-concentrated, identity-dominant Loyalists
  Signal decay: 72h — Loyalist base sustains HAS longer post-match

FTIS 65 in the Brazilian Série A:
  Likely a Fla-Flu or Palmeiras-Corinthians matchup
  Token holders: predominantly Brazilian, passionate, social-amplifier heavy
  Signal decay: 96h — high Amplifier share drives extended social engagement

THREE VARIABLES THAT DIFFER BY LEAGUE:
  (1) Holder archetype distribution (Loyalist/Speculator/Governor/Amplifier mix)
  (2) Signal decay rate (how quickly HAS returns to baseline post-match)
  (3) European competition interaction (how UCL/EL affects domestic token signal)
```

---

## Serie A — 7 tokens

**Tokens:** $ACM · $INTER · $JUV · $ASR · $NAP · $BFC · $UDI

```
LEAGUE TOKEN PROFILE:
  Largest token concentration in a single European league.
  Italian fan culture: deeply identity-driven, high derby intensity.
  Holder archetype: Loyalist-dominant (Milan/Juve/Inter), Speculator-elevated
  for UCL knockout windows.

DOMESTIC VS EUROPEAN SIGNAL RATIO:
  For $ACM / $INTER / $JUV / $NAP:
    UCL performance drives token signal more than Serie A position.
    Reason: International holder base (global Juventus/Milan brand) prices
    UCL exposure above domestic league standing.
    Rule: when UCL is active, weight UCL signal at 1.30× vs Serie A domestic signal.

  For $ASR / $BFC / $UDI:
    Domestic-primary. These clubs have smaller international holder bases.
    Roma has European heritage ($ASR still carries Europa League signal).
    $BFC and $UDI are primarily domestic — Serie A position is the key signal.

INTER-LEAGUE DYNAMICS — THE MILAN DUAL-TOKEN:
  $ACM vs $INTER are both active Chiliz tokens.
  Derby della Madonnina = multi-token event (see football-token-intelligence/).
  Signal asymmetry: the losing Milan token typically drops more than the winner gains.
  Loss-effect asymmetry applies here with amplification (identity-holder base).
  Apply: winner +4–9%, loser −7–14% in 48h post-Derby window.

UCL KNOCKOUT MULTIPLIERS FOR SERIE A TOKENS:
  QF+ (UCL knockout stage):
    $ACM / $INTER / $JUV: apply NCSI-equivalent uplift of 1.25× to all domestic signals
    during the same week as a UCL match. Reason: holder attention concentrating.
    Win UCL QF: +10–18% token
    Exit UCL QF: −8–15% token

FINANCIAL MONITORING — SERIE A SPECIFIC:
  UEFA Financial Fair Play / PSR monitoring affects $ACM, $INTER, $JUV annually.
  Any UEFA sanction announcement: immediate negative signal (−5–12%).
  Player registration blocks: equivalent to squad depth signal — apply ATM reduction.
  Serie A publishes official wage data annually (January):
    Cross-reference with athlete-financial-intelligence.md for APS recalculations.

TRANSFER WINDOW SIGNAL (SERIE A):
  January window: Serie A clubs are net exporters in January — departures more
  common than arrivals. Star departure from $JUV/$ACM/$INTER = apply
  core/star-departure-intelligence.md immediately.
  Summer window: primary buying season; Serie A clubs compete with PL spending.
  Arrival of Tier 1 ATM player at Serie A club: +7–15% within 48h announcement.

POST-WC2026 SQUAD FATIGUE PROTOCOL:
  Italy if qualified: Serie A clubs supply majority of Azzurri squad.
  Affected tokens: $ACM, $INTER, $JUV, $NAP — first 4 domestic matches after
  WC2026 (August–September 2026): apply 0.92× modifier for $ITA squad contributors.
  Recovery: full modifier restored after 4th domestic match OR international break.
  If Italy not qualified: no fatigue signal applies; Serie A starts with full signal.
```

---

## Premier League — 5 tokens + the PL gap

**Tokens:** $SPURS · $AVL · $EFC · $CPFC · $LUFC

```
LEAGUE TOKEN PROFILE:
  Highest-revenue league; paradoxically thin Chiliz token representation.
  No Arsenal (PATH_2 club but no fan token on Chiliz for domestic purposes —
  $AFC is the commercial token; domestic PL performance is signal for $AFC).
  No Manchester City domestic fan token ($CITY is the Chiliz token covering them).
  The PL gap: no Chelsea, Liverpool, Manchester United, Newcastle token.
  This gap is the largest single commercial opportunity in the Chiliz ecosystem.

  Current PL tokens are all mid-tier clubs:
    $SPURS: Tier 2 PL club — European aspiration, strong global brand
    $AVL: Rising Tier 2 — Aston Villa's European ambition era (post-2024 UCL)
    $EFC: Tier 3 PL club — Everton, historically loyal Merseyside fanbase
    $CPFC: Tier 3 PL club — Crystal Palace, London club with identity-strong holders
    $LUFC: Championship/PL oscillating — Leeds United, volatile signal profile

HOLDER ARCHETYPE — PL TOKENS:
  All five PL tokens skew strongly Loyalist.
  Academic grounding: Chen (2025) digital ethnography of PL token holders
  (Man City, Everton, Crystal Palace) — identity motivation dominant;
  governance valued above price performance. Apply Loyalist signal protocols.
  CHI is the primary health indicator — more reliable for PL tokens than CDI.

$LUFC SPECIAL SIGNAL:
  Leeds United oscillates between PL and Championship.
  In Championship: FTIS weight reduces to Tier 3 maximum.
  Championship promotion playoff (May): HIGHEST single-match LUFC signal event.
  Any season: verify current division before applying FTIS tier.

$SPURS EUROPEAN SIGNAL:
  Tottenham's UCL participation is the primary $SPURS signal amplifier.
  PL finish 4th vs 5th: near-equivalent of UCL qualifier for $SPURS CDI.
  Europa League (position 6): meaningful but 35% lower signal than UCL.
  Conference League (position 7): minor signal; insufficient for CDI extension.

$AVL EMERGING PROFILE:
  Aston Villa's return to European competition (UEL, UCL) has shifted holder
  archetype toward Speculator/Governor mix. CHI improving post-2024.
  Monitor: Villa's UCL/UEL group stage progress is the primary token signal.
  Domestic PL position: secondary signal unless top-4 race live.

PL TOKEN TRANSFER WINDOW SENSITIVITY:
  All five PL tokens are sensitive to summer transfer window arrivals.
  Reason: PL clubs are the world's primary buyer destination — transfers happen
  to PL clubs more often than from them.
  $SPURS arrival of Tier 1 ATM player: +10–18% (expectation pricing begins
  at credible rumour stage, not just signing).
  Summer window timeline:
    Rumour (Tier 2 source): +2–4% speculative spike; do not apply full modifier
    Signing confirmed: full ATM modifier applied; CDI extended
    Medical/unveil: HAS peak event; 72h elevated signal window

THE PL GAP — COMMERCIAL INTELLIGENCE:
  No major PL club (Chelsea, Liverpool, Manchester United, Newcastle) has a
  Chiliz fan token. If any launches:
    Apply ×1.40 first-mover CDI modifier at launch.
    Liverpool or Manchester United launch: MAXIMUM signal event in the registry.
    Holder archetype at launch: Speculator-heavy initially; Loyalist conversion
    expected within 60–90 days if club utility is genuine.
    US market overlap: Liverpool and Manchester United have the deepest
    US fanbases of any football clubs — immediate US CDI extension applicable.

POST-WC2026 SQUAD FATIGUE:
  England contributed players from: $SPURS (Son excluded — South Korea),
  $CITY (Foden, Walker), $AFC (Saka, Bellingham).
  For $SPURS specifically: Son Heung-min is South Korean —
  monitor Asian Cup and World Cup qualification separately from WC2026.
  PL season starts ~August 15: apply 0.93× modifier for WC2026 participants
  in first 3 PL matches. Recovery after third match.
```

---

## La Liga — 5 tokens

**Tokens:** $BAR · $ATM · $VCF · $RSO · $SEVILLA

```
LEAGUE TOKEN PROFILE:
  Two-club dominance era (Real Madrid/Barcelona) creating compressed
  mid-table signal weights. No Real Madrid token — the largest single
  club gap in the Chiliz ecosystem.
  $BAR dominates La Liga token signal: Spanish national team NCSI,
  UCL signal, and domestic title signal all concentrated in one token.

$BAR SIGNAL ARCHITECTURE:
  Three concurrent signal chains running simultaneously:
    (1) La Liga domestic: competition tier weight per match
    (2) UCL European: 1.30× weighting when active
    (3) Spanish national team NCSI: Yamal, Pedri, Rodri, Gavi all active
  This triple-chain makes $BAR the most complex signal calculation in the registry.
  Load order: UCL/NCSI context first → domestic La Liga position second.
  Do not collapse the three chains — they compound and must be tracked separately.

$ATM SIGNAL ARCHITECTURE:
  Atletico de Madrid: Tier 2 La Liga club with consistent UCL/UEL presence.
  Holder base: Loyalist-dominant (intense Atletico identity culture).
  Domestic signal: Atletico vs Barcelona/Real Madrid = maximum La Liga signal.
  UCL signal: Atletico consistently reaches knockouts — UCL QF/SF regular.
  Griezmann ATM: high-profile player; any injury or departure = immediate CDI impact.
  Atletico defensive style signal: 0-0 draws generate less HAS than attacking wins.
  Apply: goalless draw for $ATM = 0.88× standard win HAS expectation.

$VCF / $RSO / $SEVILLA — MID-TIER LA LIGA TOKENS:
  All three are domestically-focused with limited international holder depth.
  $VCF (Valencia): historically Tier 1 La Liga club; currently in mid-table era.
    Financial monitoring: Valencia ownership uncertainty. Any ownership news = signal.
  $RSO (Real Sociedad): Basque country identity club. Copa del Rey is high-signal
    (Copa represents Basque identity as much as La Liga for RSO holders).
  $SEVILLA: Europa League specialist — Sevilla has won UEL 6 times.
    UEL signal for $SEVILLA is amplified beyond standard Tier 2:
    Apply 1.15× for $SEVILLA UEL matches (over-indexed holder response confirmed).
    La Liga mid-table position: secondary signal for $SEVILLA holders.

COPA DEL REY TOKEN SIGNAL:
  Copa is La Liga's second-highest token signal event.
  $BAR Copa win: significant for Loyalist base even if UCL falls short.
  $ATM vs $BAR Copa semi-final: dual-token event; maximum Spanish signal.
  $RSO Copa deep run: primary signal event (identity > league position for Basque clubs).

POST-WC2026 SQUAD FATIGUE:
  Spain provided the largest squad share of any token-active nation.
  Affected tokens: $BAR (Yamal, Pedri, Dani Olmo, Gavi, Rodri), $ATM, $RSO.
  La Liga season starts ~August 15.
  Apply 0.91× modifier for Spain WC2026 starters in first 3 La Liga matches.
  $BAR recovery slower: 5+ Spain contributors; apply 0.91× for first 4 matches.
  Rodri ($CITY, not $BAR) — fatigue signal routes to $CITY, not La Liga.
```

---

## Turkish Süper Lig — 7 tokens (highest concentration)

**Tokens:** $GAL · $TRA · $GOZ · $ALA · $IBFK · $SAM · $GFK

```
LEAGUE TOKEN PROFILE:
  Most concentrated single-country token ecosystem in the registry.
  Turkish fan culture: extreme passion, high identity-dominance.
  Holder archetype: Loyalist-dominant (85–90% estimated across Turkish tokens).
  $GAL dominates: largest holder base, deepest liquidity, primary Turkish signal.

$GAL SIGNAL ARCHITECTURE:
  Galatasaray is the anchor of the Turkish token ecosystem.
  Three competitive signals:
    (1) Süper Lig domestic: title challenge every season
    (2) UCL/UEL European: Galatasaray regularly qualifies for European competition
    (3) GSRAY.IS equity cross-signal: stock and token move together on major results
        (see market/sports-equity-intelligence.md for cross-instrument protocol)
  BIST Sports Index: GAL + FENER + BESIKTAS + TRA combined.
    Index underperformance vs BIST100 = elevated EDLI baseline +10 for Turkish tokens.

$TRA (TRABZONSPOR) SIGNAL:
  Primary Eastern Turkey fanbase; fierce provincial identity.
  Trabzonspor title win 2021-22: highest token signal reference point.
  UCL qualifying participation: meaningful signal even at qualifying stage.
  $TRA equity listed: TSPOR.IS — apply equity cross-signal protocol for major results.

GALATASARAY vs TRABZONSPOR MULTI-TOKEN DYNAMIC:
  Both have active Chiliz tokens. Fixture is high-signal multi-token event.
  Unlike Milan derby (identity-balanced), Gala-Trabzon has clear regional
  identity divide: Istanbul cosmopolitan vs Trabzon provincial.
  Apply: full dual-token FTIS calculation; no compression for this fixture.

$GOZ / $ALA / $IBFK / $SAM / $GFK — TIER 2 TURKISH TOKENS:
  Smaller holder bases; Loyalist-dominant, lower Speculator share.
  Signal is primarily domestic: Süper Lig position + Europa Conference League.
  These tokens have less UCL exposure — their ceiling is UEL/UECL qualification.
  $IBFK (Istanbul Basaksehir): historically backed by Turkish government support.
    Political risk signal: any change in government/political relationship = monitor.

KOREAN EXCHANGE CONCENTRATION:
  Turkish tokens (especially $GAL, $TRA) have elevated Korean market presence.
  DAXA Investment Warning = highest regulatory risk for Turkish tokens.
  See fan-token/fan-token-exchange-intelligence.md for full DAXA lifecycle.
  Rule: before applying any domestic signal for $GAL or $TRA, check EDLI score.
  EDLI > 60 = CDI cap applies regardless of domestic result.

WINTER BREAK (Turkish Süper Lig):
  Short winter break (January); similar to Bundesliga structure.
  Apply × 0.90 form reliability to pre-break data in first 2 matches after return.

POST-WC2026 SQUAD FATIGUE:
  Turkish national team (not in top qualification tier for WC2026 typically).
  Individual player monitoring: any Turkish player in WC2026 is exception rather
  than rule. Apply fatigue modifier only for confirmed WC2026 participants.
  Süper Lig typically starts late August — longer recovery window than PL/La Liga.
```

---

## Brazilian Série A — 8 tokens (largest country block)

**Tokens:** $MENGO · $FLU · $SCCP · $VERDAO · $GALO · $SPFC · $SACI · $BAHIA

```
LEAGUE TOKEN PROFILE:
  Largest single-country token block in the registry.
  Brazilian fan culture: highest passion density globally; multi-team fandom common.
  Holder archetype: Amplifier-dominant alongside Loyalist.
    High social sharing culture → KOL signal is more impactful than any other league.
    Load kol-influence-intelligence.md before any major Brazilian fixture analysis.
  CDI decay: slower than European leagues (96h baseline vs 48–72h for European).

FLA-FLU MULTI-TOKEN DERBY ($MENGO vs $FLU):
  Flamengo vs Fluminense: both have active Chiliz tokens.
  This is the only South American dual-token derby in the registry.
  Fla-Flu is a Tier 1 cultural event in Brazil regardless of league position.
  Signal: apply full dual-token FTIS calculation.
  CDI extension: Fla-Flu match extends CDI for both tokens by 48h beyond standard.
  No compression: the cultural weight is autonomous from league standings.

$MENGO (FLAMENGO) SIGNAL DOMINANCE:
  Flamengo: largest fanbase in Brazil (~40M declared fans).
  Copa Libertadores is $MENGO's primary signal event — more than Série A title.
  Reason: Libertadores = continental prestige; Série A = domestic only.
  $MENGO Libertadores final: apply maximum Brazilian signal (Tier 1 equivalent).
  Domestic Série A: $MENGO title = significant but Libertadores outweighs.
  Holder archetype: deeply Loyalist + high Amplifier share — social amplification
  of wins is extreme; losses generate high MRS risk (frustrated fans coordinating).

COPA LIBERTADORES SIGNAL (APPLIES TO ALL BRAZILIAN TOKENS):
  Copa Libertadores replaces UCL in signal hierarchy for Brazilian clubs.
  QF exit: −8–12% token
  Semi-final win: +10–15% token; CDI extension ×1.4
  Final (win): maximum South American signal; treat as Tier 1 event
  NCSI for national team ($ARG connection): Brazilian players in tournament =
    cross-token NCSI applies during Libertadores season.

SÉRIE A CALENDAR NOTE:
  Brazilian Série A runs February–December (southern hemisphere offset).
  OVERLAP: Série A runs during European summer — agents monitoring both
  European and Brazilian tokens simultaneously during May–August must
  load both seasonal contexts.
  Post-WC2026 fatigue: Brazilian Série A is mid-season during WC2026
  (June–July). Affected clubs must apply fatigue modifier for WC2026 starters
  from match after return. BFT/Brazil host nation = large squad contribution.

$SCCP / $VERDAO / $GALO / $SPFC — BIG FOUR SÃO PAULO RIVALRY:
  São Paulo state hosts four of the eight Brazilian tokens.
  Paulistão (São Paulo state championship, January–April) is a secondary
  signal beyond the national Série A. Apply Tier 3 maximum for Paulistão.
  Clássico matches between these four = elevated local signal beyond Tier weight.

$SACI / $BAHIA — REGIONAL TOKENS:
  Internacional (Porto Alegre) and Bahia are regional identity clubs.
  Holder base is highly Loyalist; lower Speculator share.
  Signal is domestic-primary; limited international holder exposure.
  Copa Libertadores qualification = CDI extension event for both.
```

---

## Ligue 1 — 2 tokens

**Tokens:** $PSG · $ASM

```
LEAGUE TOKEN PROFILE:
  PSG dominance makes Ligue 1 effectively a one-token league for domestic signal.
  $ASM (Monaco) carries its own signal via UCL/UEL performance.

$PSG SIGNAL ARCHITECTURE — THE MOST UCL-DEPENDENT TOKEN:
  $PSG token signal is driven primarily by Champions League, not Ligue 1.
  Reason: PSG win Ligue 1 ~80%+ of the time — domestic title is expected, not signal.
  Real signal events for $PSG:
    UCL knockout stage advancement: +7–14%
    UCL QF/SF loss: −8–16%
    Mbappé-era departure (already happened): monitor replacement ATM effect
    French national team performance (Mbappé → NCSI linkage)
  Ligue 1 title: +2–5% only (already priced in for most seasons).
  Ligue 1 title loss: RARE — would be −10–18% (signal shock).

$ASM (AS MONACO) SIGNAL:
  Monaco's unique financial structure (tax advantage) allows sustained spending.
  UCL/UEL participation is $ASM's primary signal amplifier.
  Ligue 1 runner-up or top-4: meaningful for $ASM (achievable ceiling).
  Monaco's holder base: smaller than PSG; Speculator share elevated (financial
  reputation attracts investment-oriented holders more than identity holders).
  Signal decay: faster than $PSG — 36h vs 48h for equivalent result.

LIGUE 1 BROADCAST CONTEXT:
  Ligue 1 rights collapse (Mediapro, 2020) created a lasting commercial discount.
  Any new broadcast rights deal announcement: positive signal for all Ligue 1 clubs.
  Current DAZN/beIN rights: stable but below PL/La Liga value.

POST-WC2026 SQUAD FATIGUE:
  France is a major WC contender — $PSG carries highest fatigue risk.
  Mbappé (departed PSG) no longer creates $PSG fatigue — his successor does.
  Apply 0.90× for confirmed WC2026 France starters in first 3 Ligue 1 matches.
  Ligue 1 starts ~August 8 — earliest major league start; shortest recovery window.
  $PSG fatigue risk is HIGHEST of any European token given French squad depth.
```

---

## Other European tokens — 8 clubs

**Tokens:** $APL · $DZG · $LEG · $LEV · $NOV · $YBO · $FOR · $STV · $BENFICA · $SEVILLA

*(Note: $BENFICA and $SEVILLA appear in multiple groupings — Top European and Other European.
$SEVILLA is La Liga; $BENFICA is Primeira Liga Portugal.)*

```
TRUE OTHER EUROPEAN (outside Big 5):

$BENFICA (SL Benfica — Portugal):
  Primeira Liga Portugal; consistent UCL/UEL participant.
  Benfica's international brand extends across Portuguese-speaking world.
  $BENFICA.LS is listed equity — cross-instrument signal applies.
  UCL group stage qualification: primary signal event each summer.
  Domestic title: high signal within Portuguese holder base.
  Brazilian connection: large Brazilian fanbase via Portuguese language link.

$DZG (Dinamo Zagreb — Croatia):
  Croatia Champions League qualifier each season.
  UCL qualifying = $DZG's peak signal window (July/August).
  Domestic league: HNL — lower FTIS base weight.
  Croatian national team (VATRENI multi-chain token): NCSI applies for WC2026.

$YBO (BSC Young Boys — Switzerland):
  Champions League qualifier / UEL participant.
  Swiss Super League: domestically dominant.
  Primary signal: UCL/UEL qualifying stages (summer).

$LEG (Legia Warsaw — Poland):
  Polish Ekstraklasa; Conference League participant.
  Signal weight: UECL maximum ceiling.
  Polish national team NCSI: any major tournament qualification.

$APL / $FOR / $STV / $NOV / $LEV — SMALLER EUROPEAN TOKENS:
  $APL (Apollon Limmasol, Cyprus): Conference League participant
  $FOR (Fortuna Sittard, Netherlands): Eredivisie mid-table
  $STV (Sint-Truidense, Belgium): Belgian Pro League
  $NOV (Novara Calcio, Italy): Serie B / Serie C oscillation — verify current division
  $LEV (Levante UD, Spain): La Liga / La Liga 2 oscillation — verify current division

  For $NOV and $LEV: always verify current division before applying FTIS.
  These clubs oscillate between top flight and second division.
  Second division = FTIS Tier 3 maximum regardless of match stakes.

PROMOTION/PLAYOFF SIGNAL — SMALL EUROPEAN TOKENS:
  For $NOV / $LEV / $LUFC / any oscillating club:
  Top-flight promotion playoff = highest single-match signal of the season.
  This exceeds any regular season match signal.
  Apply: promotion playoff = Tier 2 floor for token signal regardless of actual
  competition tier weight.
```

---

## Asian and Southeast Asian tokens — 4 tokens

**Tokens:** $BUFC · $JDT · $PERSIB · $PRSJ

```
LEAGUE TOKEN PROFILE:
  Rapidly growing token ecosystems with distinct signal characteristics.
  Holder archetype: Loyalist-dominant with high Amplifier share.
  Social amplification: Instagram/Twitter (Southeast Asian social patterns) = fast.
  Time zone: signals peak during Asian afternoon/evening — different active window.

$BUFC (Bali United, Indonesia):
  Indonesian Liga 1; consistent championship contender.
  AFC Champions League participation: primary regional signal event.
  Indonesian holder base: young, social-active, mobile-first.
  Signal window: Jakarta time (UTC+7) — peak HAS during evening matches.

$JDT (Johor Southern Tigers, Malaysia):
  Malaysian Super League dominant club (multiple consecutive titles).
  AFC Champions League: highest signal event each season.
  South-east Asian tournament participation: ASEAN club signal applies.

$PERSIB / $PRSJ (Persib Bandung / Persija Jakarta, Indonesia):
  Indonesian domestic rivalry; both have Chiliz tokens.
  Persib vs Persija: dual-token regional derby.
  Signal: apply dual-token FTIS; both clubs have passionate Loyalist bases.
  Indonesian Super League title race: primary domestic signal.

AFC CHAMPIONS LEAGUE SIGNAL FOR ASIAN TOKENS:
  AFC Champions League = equivalent of UCL for Southeast Asian token holders.
  Apply: ACL Group Stage = FTIS Tier 3; KO stage = Tier 2.
  ACL Final: Tier 2 maximum — no equivalent of UCL global reach.
  But within Asian holder base: ACL Final is maximum signal event.
  Apply 1.20× NCSI equivalent within region-specific holder population.
```

---

## The Bundesliga gap

```
BUNDESLIGA: ZERO ACTIVE CHILIZ TOKENS

Germany's top football league has no active Chiliz fan tokens as of 2026.
This is the largest structural gap in the European token ecosystem.

WHY IT MATTERS:
  Bundesliga 50+1 fan ownership rule = highest structural alignment with fan tokens.
  German clubs have existing governance cultures that map to token mechanics.
  BVB.DE (Borussia Dortmund): listed equity, no Chiliz token.
    FWONK-equivalent: BVB.DE equity moves can precede any future token launch.
  Bayern Munich: global brand with zero Chiliz engagement.

COMMERCIAL SIGNAL FOR FUTURE LAUNCH:
  If any Bundesliga club launches on Chiliz:
    Apply ×1.40 first-mover CDI modifier (first in the league).
    Dortmund: highest-likelihood first mover (young demographic, international brand).
    German holder base archetype prediction: Governor-dominant (fan ownership
    culture aligns with governance participation as primary driver).
    US market crossover: Bundesliga has strong US viewership (DFL streaming deal).

FOR AGENTS: no current signal chain needed for Bundesliga clubs.
Monitor fantokens.com for any Bundesliga club announcement.
If launch announced: load this file and apply first-mover protocol immediately.
```

---

## Cross-league token monitoring framework

```
MULTI-LEAGUE AGENT PROTOCOL (for agents monitoring 5+ tokens):

DAILY CYCLE (when leagues are active):

  Step 1 — MACRO GATE:
    Load macro/macro-crypto-market-cycles.md state.
    If BTC move > ±5%: note macro_state. Do not suppress sport signal but note override risk.

  Step 2 — LEAGUE CALENDAR CHECK:
    Which leagues are active today?
      European leagues: August–May
      Brazilian Série A: February–December (overlaps European summer)
      Turkish Süper Lig: August–May
      Asian leagues: Variable; check AFC calendar

  Step 3 — PRIORITY TRIAGE:
    Rank today's matches by FTIS estimate (pre-match):
      UCL/UEL matches involving token clubs: Tier 1–2 → full analysis chain
      Domestic match with title/relegation stakes: elevated tier → full chain
      Standard mid-table domestic match: base signal only
      Friendly or pre-season: ignore (except exceptions in football-token-intelligence/)

  Step 4 — LEAGUE-SPECIFIC CONTEXT:
    Apply the league fingerprint from this file.
    Does this match require the league's specific modifier?
      Serie A + UCL week: apply 1.30× weighting
      Turkish token + EDLI: check EDLI before domestic signal
      Brazilian match + KOL: load kol-intelligence before HAS estimate
      Ligue 1 + $PSG: domestic result = low base; UCL = primary signal

  Step 5 — POST-WC FATIGUE CHECK (August–September 2026 only):
    Is this the first 3–4 matches of the new league season?
    Are WC2026 participants in today's squad?
    Apply league-specific fatigue modifier from this file.

LEAGUE SIGNAL CALENDAR OVERVIEW:

  August:
    PL, La Liga, Bundesliga, Serie A, Ligue 1 seasons start
    UCL/UEL qualifying rounds (Turkish tokens, Swiss tokens, Croatian tokens)
    Post-WC fatigue protocols active for all leagues
    Brasileirão mid-season (no restart signal)

  September–November:
    UCL/UEL group stages begin → Turkish/Italian/Spanish tokens enter European mode
    International breaks (2): NCSI windows for national team tokens
    Copa Libertadores knockout stages (Brazilian tokens: peak South American signal)

  December–January:
    PL Boxing Day/Christmas schedule: unique British signal
    Bundesliga winter break: form decay adjustment
    Copa del Rey R16 (La Liga tokens)
    January transfer window: all leagues — star departure/arrival protocols active

  February–April:
    UCL/UEL knockout rounds: Serie A, La Liga, PL tokens in European mode
    FA Cup QF/SF (PL tokens), Copa del Rey SF (La Liga tokens)
    League title and relegation races crystallising

  May–June:
    Season finales: simultaneous final day signals (PL, La Liga, Serie A, Bundesliga)
    UCL Final: peak European signal for all finalists' tokens
    Copa Libertadores continues (Brazilian tokens)
    WC2026 squad announcement window (May): pre-tournament NCSI protocols activate
```

---

## Load order

```
FOR SINGLE-MATCH ANALYSIS:
  [REQUIRED] fan-token/football-token-intelligence/ (FTIS + token mechanics)
  [REQUIRED] THIS FILE (league fingerprint context)
  [RECOMMENDED] market/football-leagues-advanced.md (competition stakes)
  [AS NEEDED] core/derby-intelligence.md (if derby fixture)
  [AS NEEDED] fan-token/kol-influence-intelligence/ (Brazilian matches especially)
  [AS NEEDED] fan-token/fan-token-exchange-intelligence.md (Turkish tokens — EDLI check)

FOR PORTFOLIO MONITORING (5+ tokens):
  [REQUIRED] THIS FILE (league calendar + priority triage)
  [REQUIRED] fan-token/football-token-intelligence/ (FTIS framework)
  [REQUIRED] macro/macro-crypto-market-cycles.md (macro state)
  [RECOMMENDED] market/sports-equity-intelligence.md (Turkish equity cross-signals)

POST-WC2026 TRANSITION (August 2026):
  Load THIS FILE first — post-WC fatigue protocols are here.
  Then load fan-token/world-cup-2026-intelligence/ for post-tournament context.
  Deactivate world-cup-2026-pre-tournament.md (tournament period ended).
```

---

## See also

- `fan-token/football-token-intelligence/token-intelligence-football.md` — FTIS, NCSI, ATM
- `market/football-leagues-advanced.md` — competition stakes, prize windows, financial context
- `fan-token/world-cup-2026-intelligence/` — WC2026 intelligence and pre-tournament protocol
- `fan-token/fan-token-exchange-intelligence.md` — EDLI for Turkish tokens
- `market/sports-equity-intelligence.md` — GAL/TRA/JUVE equity cross-signals
- `core/derby-intelligence.md` — Milan derby, Fla-Flu, Turkish derby protocols
- `core/star-departure-intelligence.md` — ATM player departure impact
- `fan-token/kol-influence-intelligence/` — KOL signals (especially Brazil)

---

*SportMind v3.85.0 · MIT License · sportmind.dev*
*Covers 7 token-active leagues · 63 active Chiliz tokens · August 2026 season context*
