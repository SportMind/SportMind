# National Team Fan Tokens — Reasoning Framework

**Enduring reasoning framework for national team fan tokens in major
tournament years. Applies to every World Cup, Euros, Copa America,
AFCON, Asian Cup, and future international tournaments.**

> SportMind Library Rule check: no specific tournament dates, named players,
> current prices, or expiring operational data. This file teaches agents
> how to reason about national team token demand — not what is true right now.

---

## National team tokens versus club tokens

```
FUNDAMENTAL DISTINCTION:

  Club tokens:
    Season runs 9–10 months
    CDI events distributed across the season
    Demand builds and decays gradually
    FTP PATH_2 supply mechanics confirmed for some clubs
    On-chain holder base is more stable

  National team tokens:
    Tournament window: 4–8 weeks
    All CDI events compressed into tournament period
    Demand can move 300–1,000% in weeks then collapse entirely
    No FTP PATH_2 confirmed for any national team token currently
    Holder base is more speculative and event-driven

  AGENT RULE:
    Never apply club token CDI frameworks directly to national tokens.
    National tokens are demand-only signals — no supply mechanics apply.
    Load this file specifically for any national team token analysis.
    Treat national tokens as HIGH_VOLATILITY, DEMAND_ONLY assets.
```

---

## Demand cycle reasoning

### Phase 1 — Tournament announcement and qualification

```
DEMAND CYCLE PHASE 1 — PRE-QUALIFICATION / ANNOUNCEMENT:

  TRIGGER EVENTS (in order of impact):
    Tournament draw announcement: host nation confirmed, dates set
      → Demand awakening for host nation tokens
      → Speculative demand for traditionally strong nations
    
    Qualification campaign begins:
      → National tokens for nations in competitive qualification begin stirring
      → Tokens for nations with uncertain qualification face qualification_risk_discount
    
    Qualification confirmed:
      → Significant demand spike: "our team is going to the World Cup"
      → Spike is proportional to the nation's fan token trading base
      
    Qualification failed:
      → Demand collapse: apply exit_curve × 0.30 (severe) for failed qualification
      → This is the worst outcome for a national token — no tournament path

  QUALIFICATION RISK MODIFIER:
    Nation in contested qualification zone: apply qualification_risk = −0.15 to CDI
    Nation already qualified (automatic): no modifier — path confirmed
    Host nation: no qualifier required — demand starts earlier, from draw announcement

  AGENT RULE:
    Before applying any tournament demand modifier, confirm:
      1. Has the nation qualified? → YES: proceed | NO: apply collapse framework
      2. Is there a fan token? → YES: load this framework | NO: no signal
```

### Phase 2 — Squad announcement

```
DEMAND CYCLE PHASE 2 — SQUAD ANNOUNCEMENT:

  The squad announcement is the single most important pre-tournament signal
  for a national team token.

  HIGH-IMPACT INCLUSION SIGNALS:
    Star player confirmed in squad → demand spike +10–20%
      (player expected, but confirmation removes uncertainty)
    Surprise inclusion (young talent, recalled veteran) → narrative spike +5–10%
    Player returning from injury confirmed fit → demand spike +15–25%
      (uncertainty resolved = maximum signal)

  HIGH-IMPACT EXCLUSION SIGNALS:
    Star player missing (injury / form / selection) → demand drop −15–30%
    Key player excluded for disciplinary reasons → sentiment spike then drop
    Large-scale absences (3+ key players) → demand cliff −20–40%

  SIGNAL DURATION:
    Squad announcement signal: 48–72h peak, then normalises as tournament approaches
    Exception: exclusion of a generational player (once-in-decade talent) → extends
    to 5–7 days of sustained negative sentiment before normalising

  AGENT RULE:
    Monitor squad announcement timing (typically 4–6 weeks pre-tournament).
    Pre-position signal readiness for announcement date.
    Apply inclusion/exclusion modifiers immediately on confirmed Tier 1 source.
```

### Phase 3 — Group draw

```
DEMAND CYCLE PHASE 3 — GROUP DRAW:

  The group draw determines the tournament path. Signal impact varies by
  how favourable or unfavourable the draw is perceived to be.

  FAVOURABLE DRAW SIGNALS:
    Nation avoids top-ranked opponents in group → demand +8–15%
    Nation drawn into perceived "easy" group → extended demand elevation
    Token nation drawn with a host nation (extra crowd support) → +5%

  UNFAVOURABLE DRAW SIGNALS:
    Nation drawn into "group of death" → demand flat or −5–10%
    Nation faces defending champion or multiple strong opponents → −5%

  DRAW SIGNAL DURATION:
    Group draw signal: 24–48h peak, then absorbs into baseline expectation
    The draw recalibrates the baseline — it is not a sustained signal

  AGENT RULE:
    Apply group draw modifier within 24h of draw confirmation.
    Do not sustain draw modifier beyond 48h — it becomes baseline assumption.
    Reassess at group stage conclusion.
```

### Phase 4 — Tournament progression

```
DEMAND CYCLE PHASE 4 — TOURNAMENT IN PROGRESS:

  Each match result creates a demand event. The magnitude scales with
  the stage of the tournament.

  MATCH RESULT DEMAND IMPACT TABLE:

  Stage             WIN signal    LOSS signal   DRAW signal
  ──────────────────────────────────────────────────────────
  Group stage       +5–10%        −5–10%        +3–5% (if progresses)
  Round of 32/16    +10–20%       EXIT (−40%)   n/a (knockout = no draw)
  Quarter-final     +20–35%       EXIT (−50%)   n/a
  Semi-final        +35–60%       −15–25% (3rd) n/a
  Final WIN         +60–100%+     n/a           n/a
  Final LOSS        n/a           −20–35%       n/a

  COMPOUND EFFECT — UNDERDOG PREMIUM:
    A lower-ranked nation defeating a highly ranked opponent generates
    amplified demand beyond the standard WIN signal.
    Giant killing: multiply WIN signal by 1.5–2.0×
    This is proportional to the perceived gap between nations.

  AGENT RULE:
    Track tournament round for every national token match.
    Apply stage-appropriate signal magnitudes.
    Exit events require immediate demand decay framework (see Phase 5).
```

### Phase 5 — Exit impact and demand decay curves

```
DEMAND CYCLE PHASE 5 — EXIT AND DECAY:

  How a nation exits determines the shape of the demand decay curve.
  Early exits decay faster. Late exits decay more slowly.

  EXIT DECAY CURVES BY ROUND:

  Group stage exit (3 matches played):
    Immediate drop: −30–40% within 24h
    Secondary decay: −10% per week for 3–4 weeks
    Baseline return: 4–6 weeks post-tournament

  Round of 32/16 exit:
    Immediate drop: −35–45% within 24h
    Secondary decay: −8% per week for 3–4 weeks
    Baseline return: 5–7 weeks post-tournament

  Quarter-final exit:
    Immediate drop: −20–30% within 24h
    Secondary decay: −5% per week for 4–5 weeks
    Baseline return: 8–10 weeks post-tournament
    Note: QF exit is "proud exit" — decay is slower than early exit

  Semi-final exit:
    Immediate drop: −15–20% within 24h
    Secondary decay: slower — narrative keeps demand elevated longer
    Baseline return: 10–14 weeks post-tournament
    Note: SF exit includes a third-place play-off (additional match signal)

  Runner-up (Final LOSS):
    Immediate drop: −10–20% after final loss
    Secondary decay: very slow — "we almost won" narrative
    Baseline return: 12–16 weeks post-tournament

  Tournament winner:
    No immediate drop — demand elevated post-win
    Decay begins 2–3 weeks post-tournament
    Baseline return: 16–24 weeks (sustained winner premium)
    Note: next tournament anticipation begins before full decay

  AGENT RULE:
    Identify the round of exit immediately on elimination.
    Apply the appropriate decay curve from the elimination moment.
    Do not apply flat decay — curves differ significantly by round.
```

---

## World Cup year modifier

```
WORLD CUP YEAR DEMAND PREMIUM:

  National tokens in a World Cup year experience a structural demand
  premium that begins before the tournament and persists through it.

  PRE-TOURNAMENT PREMIUM BUILD:
    6 months before tournament: first signs of demand awakening
    3 months before: moderate premium (+20–40% vs off-year baseline)
    1 month before: elevated premium (+50–80% vs off-year baseline)
    Tournament start: maximum pre-match premium

  HISTORICAL DEMAND PATTERNS:
    National tokens historically show 300–1,000% price movement during
    World Cup cycles for nations that reach the knockout rounds.
    This range is wide because it depends on:
      - Nation's initial token liquidity and holder base
      - Depth of tournament run
      - Global fan base size
      - Macro crypto market conditions during the tournament

  QUALIFIER FAILURE — DEMAND COLLAPSE:
    If a nation fails to qualify, the World Cup year premium collapses.
    Apply qualification_failure_modifier:
      Immediate: −40–60% within 72h of elimination
      Post-collapse: token returns to baseline demand
      Recovery: demand does not fully recover until next qualification cycle

  CROSS-TOKEN CORRELATION:
    National tokens from the same confederation tend to move together.
    Positive tournament sentiment for one CONCACAF nation lifts others.
    Negative sentiment for a group of European exits drags all European tokens.
    Cross-correlation is stronger during tournaments than at baseline.
    Apply: confederation_correlation_factor = 0.3–0.5 during tournament window.

  AGENT RULE:
    In World Cup years, apply WC_year_premium before any other signal.
    Confirm qualification status before applying premium.
    Track confederation sentiment as a secondary signal.
```

### Host nation token reasoning

```
HOST NATION TOKEN REASONING:

  Host nations receive a structural demand amplification beyond standard
  tournament progression signals.

  HOST NATION AMPLIFIERS:
    Home crowd advantage: genuine performance benefit → higher win probability
    Media exposure: tournament saturated with host nation coverage
    Civic pride: domestic holder base expands during tournament
    Commercial partnerships: tournament sponsors associate with host nation

  DEMAND TRAJECTORY (HOST NATION):
    Pre-tournament: earlier and larger premium than comparable non-host nations
    During tournament: each win amplified by home crowd narrative
    Exit: if host nation exits, crash is often larger than for non-host
      (narrative reversal: "embarrassment at home" amplifies the drop)

  HOST NATION WITHOUT A TOKEN:
    If the host nation(s) do not have an active fan token at tournament time:
      → Structural demand opportunity for tokens of nations playing in the host country
      → Monitor for any announced token launches by host nations
      → A host nation token launch during the tournament = maximum CDI event

  AGENT RULE:
    Identify host nation(s) before the tournament.
    Apply host_nation_amplifier = ×1.20 to all host nation token signals.
    Monitor for host nation token launch announcements.
```

---

## No PATH_2 for national tokens — demand only

```
SUPPLY MECHANICS — NATIONAL TEAM TOKENS:

  As of the library's current knowledge state, NO national team fan token
  has confirmed FTP PATH_2 mechanics.

  WHAT THIS MEANS (updated WC2026):
    National token signals are DEMAND_ONLY by default.
    FTP PATH_2 (Model 2 prediction market) remains unconfirmed for all
    national team tokens as of current library state.

    HOWEVER — Burn to Glory treasury burn mechanic IS active for
    confirmed participating tokens (WC2026: $ARG, $POR, $BELG, $SAFA, $SFA).
    This is a treasury-source burn, not PATH_2.

    KEY DISTINCTION:
      Burn to Glory: treasury holdings burned on WIN — user wallets unaffected
      FTP PATH_2: market pre-liquidation settlement — club tokens only
      These are separate mechanics. Load fan-token/burn-to-glory-framework.md
      for full Burn to Glory signal architecture.

    AGENT RULE:
      Check whether a national token has confirmed Burn to Glory participation
      before treating it as purely demand-only.
      If confirmed: apply burn signal + demand signal (additive).
      If unconfirmed: demand-only framework applies as before.

  AGENT RULE:
    Never apply PATH_2 supply mechanics to national team tokens.
    Load fan-token/ftp-path2.md only for confirmed club tokens.
    
  IF THIS CHANGES:
    If a national team token launches with confirmed PATH_2 mechanics:
    Apply the standard fan-token/ftp-path2.md framework.
    Update this file with the confirmed mechanic and source.
```

---

## Compatibility

**Tournament structure:** `sports/football/sport-domain-football-world-cup.md`
**Tournament macro:** `macro/tournament-macro.md`
**FTP mechanics:** `fan-token/ftp-path2.md` (club tokens only)
**WC 2026 specific:** `fan-token/world-cup-2026-intelligence/`

**Burn to Glory:** `fan-token/burn-to-glory-framework.md`

---

*SportMind v4.0.2 · MIT License · sportmind.dev*
*Enduring framework — applies to every major international tournament*


## MIND DIMENSIONS

| Dimension | Status | Notes |
|-----------|--------|-------|
| Intelligence | ACTIVE | National team token intelligence: tournament demand catalysts, FTO lifecycle, fraud amplification |
| Reasoning | ACTIVE | National team reasoning chain from tournament signals to demand modifier and supply event |
| Context | ACTIVE | National team context: World Cup window, Locker Room launch phases, qualification cycles |
| Memory | ACTIVE | Historical national team token demand patterns across tournament windows |
| Judgment | ACTIVE | Judgment on national team signal materiality — World Cup window dominates all others |
| Attention | ACTIVE | Maximum attention during World Cup fraud amplification window — ALL FOUR sources required |
| Communication | ACTIVE | National team output with tournament phase, demand modifier, and fraud risk level |
| Verification | ACTIVE | Four-source verification mandatory for all national team tokens during World Cup window |
| Learning | ACTIVE | National team token calibration growing with $SAFA/$SFA as first Locker Room examples |
| Integration | ACTIVE | Integrates with world-cup-2026-intelligence, fto-framework, and complete-registry |
| Calibration | EMERGING | National team token calibration is developing — $SAFA/$SFA are first calibration points |
| Adaptation | ACTIVE | National team framework adapts as Locker Room launch mechanics and token ecosystem evolve |
| Ethics | ACTIVE | World Cup fraud amplification requires the highest fraud detection vigilance |
| Transparency | ACTIVE | Tournament phase, FTO stage, and fraud risk level always explicit in national team outputs |


---

## Confirmed official national team Fan Tokens™

```
SPORTMIND VERIFIED REGISTRY — NATIONAL TEAM TOKENS:

  $ARG — Argentina National Team
    Partnership: Asociación del Fútbol Argentino (AFA) × Socios/Chiliz
    Integration: OFFICIAL_INTEGRATED — AFA partnership fully embedded in
      club operations, squad activation, and fan engagement programmes
    Verification: socios.com · chiliscan.com · AFA official channels
    Classification: confirmed official Fan Token™ · national team category
    Source: fan-token/official-verification-framework.md

  $POR — Portugal National Team
    Partnership: Federação Portuguesa de Futebol (FPF) × Socios/Chiliz
    Verification: socios.com · chiliscan.com · FPF official channels
    Classification: confirmed official Fan Token™ · national team category

  $SNFT — Spain National Team
    Partnership: Real Federación Española de Fútbol (RFEF) × Socios/Chiliz
    Verification: socios.com · chiliscan.com · RFEF official channels
    Classification: confirmed official Fan Token™ · national team category

  $BFT — Brazil National Team
    Partnership: Confederação Brasileira de Futebol (CBF) × Socios/Chiliz
    Verification: socios.com · chiliscan.com · CBF official channels
    Classification: confirmed official Fan Token™ · national team category

  $SAFA — South Africa National Team
    Partnership: South African Football Association (SAFA) x Socios/Chiliz
    Verification: socios.com · chiliscan.com · SAFA official channels
    Classification: confirmed official Fan Token — national team category
    Burn to Glory: CONFIRMED participant — WC2026
    Regional file: fan-token/regional-intelligence/south-africa-safa.md

  $SFA — Scotland National Team
    Partnership: Scottish Football Association (SFA) x Socios/Chiliz
    Verification: socios.com · chiliscan.com · SFA official channels
    Classification: confirmed official Fan Token — national team category
    Burn to Glory: CONFIRMED participant — WC2026
    Regional file: fan-token/regional-intelligence/scotland-sfa.md

  $BELG — Belgium National Team
    Partnership: Royal Belgian Football Association (RBFA) x Socios/Chiliz
    Verification: socios.com · chiliscan.com · RBFA official channels
    Classification: confirmed official Fan Token — national team category
    Chain: Chiliz Chain + Solana (Jupiter DEX) + Paribu CEX
    FTO: June 2026 (completed) · Supply: 2,000,000 tokens
    Burn to Glory: CONFIRMED participant — WC2026

  ALL OTHER NATIONAL TEAM TOKEN CLAIMS: UNVERIFIED
    Any token claiming national team affiliation not listed above must be
    verified through the four-source methodology before any signal is applied.
    World Cup 2026 fraud risk: heightened — verify all national team tokens
    before tournament. See fan-token/fraud-risk-intelligence.md.
```
