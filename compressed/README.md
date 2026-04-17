# Compressed SportMind Skills

**Token-efficient summaries of SportMind's most-used skills.**
Each compressed skill is approximately 500–800 tokens — roughly 70% smaller than
the full skill. Use when context budget is constrained and full skill detail
is not required.

These are summaries, not replacements. When analysis quality matters more than
token cost, load the full skill. When you need a fast reference or are running
many simultaneous analyses, use these compressed versions.

---

## When to use compressed vs full skills

| Situation | Use |
|---|---|
| First analysis of a topic, high-stakes decision | Full skill |
| SMS >= 80 required | Full skill |
| Routine monitoring, portfolio overview | Compressed |
| MCP tool calls with token budget | Compressed (use `compressed=true`) |
| Multi-sport quick comparison | Compressed |
| Agent already has strong context, just needs a check | Compressed |

Load compressed via MCP: `sportmind_stack(sport="football", compressed=true)`
Load compressed via API: `GET /stack?sport=football&compressed=true`

---

## [COMPRESSED] Football domain

```
FORMAT: 90min match. TIERS: UCL Final=1.0, UCL KO=0.75, domestic title=0.55, standard=0.30.
INJURY: GK/ST absence ×0.85. KEY RULE: Derby = reduce form differential 40%.
TIMELINE: T-2h lineup critical. Pre-match press = first hint. Team sheet = T-75min.
FLAGS: lineup_unconfirmed until T-2h. injury_warning if key player absent.
NCSI: national team performance → club token spillover. See international-football-cycle.md.
Full skill: sports/football/sport-domain-football.md
```

## [COMPRESSED] Cricket domain

```
FORMAT FIRST: T20 (3h, high token impact) | ODI (7h, World Cup=Tier 1) | Test (5 days, low volatility).
INDIA RULE: India match ×1.40. India-Pakistan ×2.00. No exceptions.
DEW FACTOR: Evening T20, South Asian venue → batting second +10-12%. Check toss result.
DLS: Rain interruption supersedes pre-match analysis — reload required.
IPL: Largest untapped market. Regulatory clarity (SEBI) = library's biggest commercial event.
Full skill: sports/cricket/sport-domain-cricket.md
```

## [COMPRESSED] Basketball (NBA) domain

```
TIERS: NBA Finals G7=1.00, Finals=0.85, Conference Final=0.70, standard=0.25.
STAR RULE: Top-5 MVP candidate absent → ×0.75 modifier.
LOAD MANAGEMENT: Track rest days. B2B second game = elevated load management risk.
TRADE DEADLINE: Feb 6 = NBA's transfer window. Buyer team positive, seller disrupted.
NBATIS: (Game_Importance×0.35)+(Star_Player_Tier×0.30)+(Playoff_Position×0.25)+(Market_Sentiment×0.10)
Full skill: sports/basketball/sport-domain-basketball.md
```

## [COMPRESSED] MMA domain

```
WEIGH-IN IS THE KEY EVENT: Pass = confirm signal. Fail = ×0.72-0.75 negative modifier.
TIMELINE: Weigh-in day before fight. Final staredown day of. Fight night.
STYLE: Striker vs Grappler matchup = primary variable after weigh-in.
TITLE: Championship fights ×1.35 base weight. Interim titles ×1.15.
CAMP: Injury rumours from camp = activate injury_warning. Monitor officially.
Full skill: sports/mma/sport-domain-mma.md
```

## [COMPRESSED] Formula 1 domain

```
QUALIFYING DELTA: Most predictive F1 variable. Track vs next driver in qualifying.
HARDWARE TIER: Tier 1 (current champion constructor) ×1.15. Tier 4 ×0.88. Updates at season start.
WET: Rain probability >40% → activate weather_risk. Wet specialist advantage overrides hardware.
SEASON: Points leader with 5+ rounds remaining = season modifier active.
DRIVER TOKEN: Constructor token ≠ driver token. Align token correctly before analysis.
Full skill: sports/formula1/sport-domain-formula1.md
```

## [COMPRESSED] Football token intelligence (FTIS + NCSI)

```
FTIS: (competition_weight×0.35)+(fixture_stakes×0.25)+(athlete_multiplier×0.25)+(token_health×0.15)×100
FTIS BANDS: 85-100=full analysis. 70-84=high. 55-69=elevated. <40=skip.
NCSI WEIGHTS (from international-football-cycle.md):
  World Cup/Euros=1.00 | Nations League Finals=0.75 | Qualification decisive=0.70
  Standard friendly=0.10 | Post-tournament period=0.00 (narrative only)
ATM: ×0.91 top star | ×0.72 first XI | ×0.54 squad player | ×0.28 fringe
EURO NOTE: For European club tokens, apply Euros NCSI at ×1.10 vs World Cup.
Full skill: fan-token/football-token-intelligence/token-intelligence-football.md
```

## [COMPRESSED] Macro state

```
PHASES: BULL(modifier 1.20) | NEUTRAL(1.00) | BEAR(0.75) | EXTREME_BEAR(0.55)
RULE: Check macro before ALL fan token analysis. macro_modifier applies to every signal.
OVERRIDE: macro_modifier <0.75 = activate macro_override_active flag.
REFRESH: Every 4-8 hours in production. Run: python scripts/update_macro_state.py
SIGNAL SEPARATION: Prediction market signal ≠ fan token signal. Macro affects tokens only.
Full: platform/macro-state.json + macro/macro-crypto-market-cycles.md
```

## [COMPRESSED] Fan token lifecycle

```
PHASES: 1=Launch(novelty) → 2=ActiveUtility(sporting signals) → 3=Plateau(declining HAS)
        → 4=PostPartnership(prediction markets) → 5=RWA(tokenised revenue) → 6=Dormant
LTUI: Lifetime Token Utility Index. Phase 2 target: 60+. Phase 3 risk: <40.
HAS: Holder Activity Score. Declining HAS + Phase 3 = intervention required.
PHS: Partnership Health Score. <50 at 12 months = termination risk elevated.
AGENT RULE: Always check lifecycle phase before interpreting any token signal.
Full skill: fan-token/fan-token-lifecycle/
```

## [COMPRESSED] DeFi liquidity

```
TVL THRESHOLDS: >$5M=deep. $500k-$5M=moderate. $100k-$500k=thin. <$100k=very thin.
SLIPPAGE: Impact% ≈ (trade_size / pool_TVL) × 0.5. >3% = ABSTAIN or reduce significantly.
LP SIGNAL: Large LP additions before event = smart money positioning.
RULE: Check TVL BEFORE applying any signal. Thin liquidity invalidates standard sizing.
ABSTAIN conditions: liquidity_critical flag | slippage >3% | TVL <$100k.
Full skill: fan-token/defi-liquidity-intelligence/
```

## [COMPRESSED] Confidence output schema

```
REQUIRED FIELDS: adjusted_score, confidence_tier, composite_modifier, flags[], sportmind_score{}
SMS TIERS: HIGH_QUALITY(80+) | GOOD(60-79) | PARTIAL(40-59) | INCOMPLETE(20-39) | INSUFFICIENT(<20)
FLAGS: lineup_unconfirmed | macro_override_active | liquidity_warning | liquidity_critical | injury_warning | weather_risk
POSITION SIZE: HIGH_QUALITY=100% | GOOD=65% | lineup_unconfirmed=50% | INSUFFICIENT=0%
SCHEMA VERSION: 1.2 (includes sportmind_score + defi_context + sha256)
Full schema: core/confidence-output-schema.md
```

---


## [COMPRESSED] Rugby union domain

```
TIERS: RWC Final=1.00, RWC KO=0.75-0.95, Six Nations decider=0.80, standard=0.30-0.50.
KICKER PRIMACY: 40-50% of points from kicks. Kicker form = most predictive variable.
HOME ADVANTAGE: Strongest in sport (crowd noise affects lineout calls, scrum decisions).
REF BIAS: Load core/core-officiating-intelligence.md — union referee card rates vary widely.
CVC: CVC invested in Six Nations/Premiership/URC — commercial tokenisation pathway confirmed.
CYCLE: market/international-rugby-cycle.md — Six Nations Feb-Mar + World Cup (2027 next).
Full skill: sports/rugby/sport-domain-rugby.md
```

## [COMPRESSED] Rugby league domain

```
STATE OF ORIGIN: NCSI 0.90 (Game 3 decider). Most disruptive intra-national signal in library.
DOWNSTREAM: NRL clubs depleted by Origin → downstream congestion = highest-value underpriced signal.
NRL TIERS: Grand Final=0.90, Preliminary=0.75, Elimination Final=0.62, standard=0.20.
SUPER LEAGUE: ×0.75 vs NRL equivalent. Sky Sports + Channel 4 (UK) broadcast anchor.
SOO DISRUPTION: High-Origin clubs ×0.88; benefiting clubs ×1.04-1.07. Check before NRL analysis.
CYCLE: market/international-rugby-cycle.md — State of Origin May-July; RLWC every ~4 years.
Full skill: sports/rugby-league/sport-domain-rugby-league.md
```

## [COMPRESSED] AFL domain

```
TIERS: Grand Final (MCG)=1.00, Prelim Final=0.88, Semi-Final=0.75, standard=0.25.
FINALS FORMAT: Top 8; weeks 1-4 finals; Grand Final = highest Australian sport signal.
HOME GROUND: MCG vs other venues = significant advantage signal.
DRAFT: First overall pick = immediate franchise signal. Pre-draft: monitor bids.
INTERSTATE: Clubs outside VIC (Victoria) have larger road disadvantage.
WOMENS (AFLW): Growing signal — separate competition, overlapping period with AFL.
Full skill: sports/afl/sport-domain-afl.md
```

## [COMPRESSED] American football (NFL) domain

```
TIERS: Super Bowl=1.00, Conference Championship=0.85, Divisional=0.70, Wildcard=0.60.
QB PRIMACY: Quarterback is most important individual position in sport. QB absent = reload.
INJURY REPORT: NFL mandatory injury report (Wednesday/Thursday/Friday). Check before analysis.
BYE WEEKS: Each team has one bye. Teams coming off bye week = rest advantage.
TRADE DEADLINE: Nov 1 = NFL's transfer window. Buyer positive; seller disrupted.
DRAFT: April — franchise-altering; first round = token signal events for franchises with tokens.
Full skill: sports/american-football/sport-domain-american-football.md
```

## [COMPRESSED] Tennis domain

```
SLAMS: Wimbledon/Roland Garros/AO/US Open = Tier 1. ATP/WTA 1000 = Tier 2.
SURFACE: Grass/clay/hard — surface specialists exist (Nadal clay, Djokovic hard).
  Check: player's surface win% before applying form. Surface override > form.
RANKING: Top-4 seedings for draws. Seeding = context for upset probability.
RETIREMENTS: Mid-match retirements common — void all analysis if player retires.
WTA NOTE: Women's draw has more upsets. Form differential less predictive than ATP.
Full skill: sports/tennis/sport-domain-tennis.md
```

## [COMPRESSED] Baseball (MLB) domain

```
PITCHER FIRST: Starting pitcher controls 60-70% of game outcome. Identify before anything else.
PQS: Pitcher Quality Score ×0.75 (failed) to ×1.18 (dominant). Non-negotiable first step.
BULLPEN: Check workload last 3 games. High workload (3+ apps) = ×0.90. Fresh = ×1.05.
TIERS: WS clinch=1.00, WS Game=0.80-0.98, LCS=0.72, LDS=0.60, standard=0.20.
OHTANI: Dual signal (pitcher AND batter). Pitcher day: PQS ×1.08. Batter day: BQS + load.
CALENDAR: July 31 trade deadline = peak summer signal. Latin America + Japan = natural markets.
Full skill: sports/baseball/sport-domain-baseball.md
```

## [COMPRESSED] Ice hockey (NHL) domain

```
GOALTENDER FIRST: Morning skate (T-6h) = confirmation window. Not confirmed = lineup_unconfirmed.
GSAx: Goals Saved Above Expected. >+10 = elite ×1.18. <-5 = liability ×0.88.
B2B: Back-to-back second game = expect backup goaltender. Apply ×0.88 fatigue.
TIERS: SCF Game 7=1.00, SCF=0.75-0.92, Conference Final G7=0.85, standard=0.20.
CANADA: 7 franchises. 3× US per-capita viewership. ~30% crypto adoption. Leafs = highest value.
TRADE DEADLINE: March — primary non-playoff signal. Buyer positive; seller disrupted.
Full skill: sports/ice-hockey/sport-domain-ice-hockey.md
```

## [COMPRESSED] MotoGP domain

```
HARDWARE TIER: Most persistent signal. Tier 1 (works/champion manufacturer) ×1.15. Update at season start only.
WET RACE: Rain >40% → activate weather_risk. Hardware modifier -50%. Wet specialist overrides tier.
DORNA: Single commercial authority — one deal covers full championship. Fastest token pathway in motorsport.
RIDER-CENTRIC: Fan attachment to rider > constructor. Rider tokens (Márquez) > manufacturer tokens.
SOUTHEAST ASIA: Indonesia (80M+ fans), Thailand, Malaysia = 500M+ market. ×1.10-1.15 regional amplifier.
SPRINT: Saturday sprint = 40% weight. Separate signal from Sunday GP. Sprint crash → check injury for GP.
Full skill: sports/motogp/sport-domain-motogp.md
```

## [COMPRESSED] NASCAR domain

```
TRACK TYPE: Oval type matters more than team form. Superspeedway vs short track = different hierarchy.
SPONSOR LOYALTY: 72% of NASCAR fans buy from sponsors. Sponsor activation = direct token signal.
CHAMPIONSHIP 4: Final 4 drivers compete at Phoenix (November). ×1.25 motivation modifier.
CHARTER: Charter teams (financially secured) vs open teams. Charter = consistent signal.
DAYTONA 500: Season opener; highest single-race signal (February). Narrative ≠ form — lottery element.
PLAYOFFS: 16-driver playoff August-November. Elimination events = escalating signal.
Full skill: sports/nascar/sport-domain-nascar.md
```

## [COMPRESSED] Esports domain

```
TIERS: World Championship (LoL/Dota 2 The International)=1.00. Major=0.75. Standard=0.30.
ROSTER VOLATILITY: Rosters change frequently. lineup_unconfirmed is standard. Always check.
PATCH: Game balance patches change team meta. Recent patch = form data partially stale.
REGION: Korea/China dominate LoL; China/SEA dominate Dota 2. Regional form ≠ international form.
VIEWERSHIP: Peak concurrent viewers = signal quality proxy. Worlds > 75M viewers.
FORMAT: Best-of-3 vs best-of-5. BO5 = more skill-based, upsets less common.
Full skill: sports/esports/sport-domain-esports.md
```

## [COMPRESSED] Boxing domain

```
WEIGHT CLASS: Signal is per weight class. Heavyweight = highest casual engagement.
BELT CONTEXT: Unified champion (holds all 4 belts) vs interim = different narrative weight.
TRILOGY: Third fight between same opponents = maximum narrative signal.
JUDGING RISK: Controversial decisions common. Close fight = reduced signal confidence.
VENUE: Las Vegas vs UK venues vs Saudi Arabia — crowd composition affects judging perception.
REMATCH CLAUSE: Many contracts include rematch clause. Loser's token less negative if rematch likely.
Full skill: sports/boxing/sport-domain-boxing.md
```

## [COMPRESSED] Handball domain

```
GK PRIMACY: Save rate >40% = ×1.20 override. Most decisive single-variable in team sport.
FINANCIAL TIER: Barcelona, PSG, Kiel = Tier 1 (budget 3-5× average). ×1.12 vs Tier 2 in neutral venue.
EHF FINAL4: Budapest (June) = peak signal. PSG Handball in Final4 = +3% $PSG football token.
WORLD CHAMPIONSHIP: Odd years (Jan-Feb). France (6×), Denmark, Spain, Germany = top national signals.
HandTIS: (Competition_Tier×0.35)+(GK_Save_Rate×0.30)+(Financial_Tier_Gap×0.25)+(Market_Sentiment×0.10)
CYCLE: market/international-rugby-cycle.md is NOT applicable — use international-football-cycle.md for structure.
Full skill: sports/handball/sport-domain-handball.md
```

## [COMPRESSED] Kabaddi domain

```
STAR RAIDER: Kabaddi's version of the QB. Loss of star raider = reload analysis.
PKL: Pro Kabaddi League (India, July-October). JioCinema = digital infrastructure ready.
INDIA DOMINANCE: India national team wins most internationals. Strong national team = lower upset probability.
REGULATORY: VDA clarity in India = PKL token catalyst (same pathway as IPL).
DO OR DIE RAID: High-pressure tactical raid = individual skill signal within match.
ALL OUT: Scoring all opposition points (All Out event) = momentum signal mid-match.
Full skill: sports/kabaddi/sport-domain-kabaddi.md
```

## [COMPRESSED] Netball domain

```
TRANS-TASMAN: Australia vs New Zealand = Tier 1 signal. ×1.25 rivalry amplifier.
SHOOTER ACCURACY: Goal shooter + goal attack accuracy = primary predictive variable.
WORLD CUP: Every 4 years (2027 next). Fastest Tier 2→1 token transition in library.
CENTRE PASS: Centre pass conversion rate = secondary predictive metric.
AUSTRALIA/NZ DOMINANCE: Top-2 in world. Third nation upset = rare narrative event.
ANZ CHAMPIONSHIP: Trans-Tasman club competition = highest club-level signal in netball.
Full skill: sports/netball/sport-domain-netball.md
```

## [COMPRESSED] Golf domain

```
MAJORS: Masters/US Open/The Open/PGA Championship = Tier 1. ×3.0-4.0 vs regular tour.
CUT: 36-hole cut removes field to top-70ish. Post-cut signal much more predictive.
WEATHER: Wind most important variable in golf. Strong wind = scoring average up ~2 strokes.
WORLD RANKING: Top-10 vs top-50 vs outside = form tier. Recent tournament form ±4 weeks.
RYDER CUP: Europe vs USA; every 2 years. Highest-signal non-Major event. Team format = different model.
LIVE GOLF: LIV Golf changed competitive landscape. World Ranking implications affect seeding.
Full skill: sports/golf/sport-domain-golf.md
```

## [COMPRESSED] Horse racing domain

```
RACE CLASS: Group 1 (Classics, Cheltenham Gold Cup) = Tier 1. Group 3 = Tier 3.
GOING: Ground conditions (firm/good/soft/heavy) = primary variable. Check going before form.
DRAW: Starting position in field — stall draw = significant at some tracks (Chester, Ascot).
WEIGHT: Handicap weight assignment. Horses carry different weights; weight = direct performance modifier.
TRAINER/JOCKEY: Trainer win% at track + jockey win% at distance = combined signal.
ANTE-POST: Betting market as signal — significant drift (odds increase) = non-runner risk.
Full skill: sports/horse-racing/sport-domain-horse-racing.md
```

## [COMPRESSED] Darts domain

```
LEGS/SETS: Format matters. Legs (best-of-X) vs sets (best-of-Y sets, each Y legs).
AVERAGE: Three-dart average is the primary performance metric. 100+ = elite; 95-100 = solid.
CHECKOUT: Checkout percentage under pressure = secondary metric (especially in tight legs).
PREMIER LEAGUE: Top-8 nightly league (February-May) = sustained signal.
WORLD CHAMPIONSHIP: Ally Pally (December-January) = highest signal. BDO split now resolved (PDC dominant).
HOME CROWD: Prem League and ProTour — crowd reaction affects performer differently (Bristow effect).
Full skill: sports/darts/sport-domain-darts.md
```

## [COMPRESSED] Snooker domain

```
WORLD CHAMPIONSHIP: Crucible (April-May, 17 days) = Tier 1. 17-day format = longest sustained signal.
BREAKS: Century breaks (100+) = momentum signal mid-match.
RANKING EVENTS: 12 full-ranking events per season. Masters (non-ranking) = prestige Tier 1.
SAFETY PLAY: Safety battle = tactical chess; can extend match length unpredictably.
RONNIE O'SULLIVAN: Highest-ATM player in snooker. His matches = highest engagement regardless of tier.
FRAME FORMAT: Best-of-X frames. Late frames (last 3 in long match) = highest pressure signal.
Full skill: sports/snooker/sport-domain-snooker.md
```

## [COMPRESSED] Athletics domain

```
WORLD ATHLETICS CHAMPIONSHIPS: Biennial (odd years). Diamond League = annual series.
SPRINTS: 100m/200m = highest engagement events. World record attempts = maximum signal.
MARATHON: Olympic/Championship marathon = long narrative (2h+). Weather is primary variable.
DOPING: Higher doping history than most sports. Positive test = immediate signal collapse.
USAIN BOLT EFFECT: Post-Bolt era = reduced 100m signal. Monitor who holds 100m narrative.
OLYMPICS: Every 4 years. Athletics = largest Olympic programme. Medal table significance.
Full skill: sports/athletics/sport-domain-athletics.md
```

## [COMPRESSED] Cycling domain

```
GRAND TOURS: Tour de France/Giro/Vuelta = Tier 1. Classics (Roubaix, Flanders) = Tier 2.
STAGE TYPES: Sprint stages, mountain stages, TT (time trial) — different specialists win each.
GC vs STAGE HUNTERS: General Classification leader vs stage specialists = separate signal streams.
WEATHER: Mountains = weather risk. Rain on descents = crashes = results invalidated.
DOPING HISTORY: High historical doping. Positive test = significant retrospective signal collapse.
TOUR DE FRANCE: July. Highest signal in cycling. Champs-Élysées final = most-watched cycling event.
Full skill: sports/cycling/sport-domain-cycling.md
```

## [COMPRESSED] Swimming domain

```
WORLD CHAMPIONSHIPS: Biennial. Olympics = Tier 1 (every 4 years).
EVENTS: Butterfly/backstroke/breaststroke/freestyle over various distances. Medley = combined.
WORLD RECORDS: Most valuable single swimming signal. WR attempt = pre-event signal amplifier.
PHELPS/LEDECKY EFFECT: Dominant individual = franchise signal. Post-Phelps era shift in progress.
FATIGUE: Multi-event swimmers peak for specific events. Check day-of schedule.
RELAY: National relay = team combination signal — different from individual prediction.
Full skill: sports/swimming/sport-domain-swimming.md
```

## [COMPRESSED] Rowing domain

```
OLYMPICS: 4-year cycle. World Rowing Championships = annual equivalent.
BOAT CLASSES: Single scull (1 person) through eight (8+cox). Different competitive dynamics.
CONDITIONS: Head/tailwind and water conditions are primary variables. Check before analysis.
WORLD CHAMPIONSHIPS: September annually. Olympic year = less important than Games.
HENLEY: Prestigious British regatta (July). Club and national level. High engagement, lower signal.
ENDURANCE: Rowing = pure endurance sport. Form consistency higher than technical sports.
Full skill: sports/rowing/sport-domain-rowing.md
```

## [COMPRESSED] Winter sports domain

```
COVERS: Alpine skiing, biathlon, Nordic skiing, figure skating, speed skating, ski jumping.
WORLD CUP SERIES: Season-long points competitions (October-March). Overall title > individual event.
CONDITIONS: Snow/temperature/visibility = primary variable in outdoor disciplines.
FIGURE SKATING: Judged sport = subjective. Consistent technical programs > variable artistic.
BIATHLON: Shooting accuracy = primary signal. Shooting stage = match-defining moments.
WINTER OLYMPICS: 4-year cycle. Alpine skiing and biathlon = highest engagement disciplines.
Full skill: sports/winter-sports/sport-domain-winter-sports.md
```

## Compressed skill index

| Compressed skill | Full skill location | Tokens (approx) |
|---|---|---|
| Football domain | `sports/football/sport-domain-football.md` | 120 |
| Cricket domain | `sports/cricket/sport-domain-cricket.md` | 110 |
| Basketball domain | `sports/basketball/sport-domain-basketball.md` | 105 |
| MMA domain | `sports/mma/sport-domain-mma.md` | 100 |
| Formula 1 domain | `sports/formula1/sport-domain-formula1.md` | 105 |
| Football token intel | `fan-token/football-token-intelligence/` | 130 |
| Macro state | `platform/macro-state.json` | 95 |
| Fan token lifecycle | `fan-token/fan-token-lifecycle/` | 110 |
| DeFi liquidity | `fan-token/defi-liquidity-intelligence/` | 100 |
| Confidence schema | `core/confidence-output-schema.md` | 95 |

Total compressed stack (all 10): ~1,070 tokens
Total full stack (equivalent): ~32,000+ tokens
**Compression ratio: ~97%** — use compressed for overview; full for decision-quality analysis

---


---

## [COMPRESSED] Breaking news intelligence

**When to use:** Any live-match or time-sensitive analysis where news may arrive
mid-analysis. Load alongside realtime-integration-patterns.md.

```
CATEGORIES (1=RELOAD, 2=VOID, 3=MODIFY, 4-6=MODIFY/ESCALATE, 7-8=ESCALATE/OVERRIDE)
PROTOCOLS: RELOAD (key player absent T-0), MODIFY (disciplinary/transfer), VOID (postponement),
           ESCALATE (external events, macro breaking)
SOURCE TIERS: 1=official/confirmed, 2=Tier1-journalist, 3=social (monitor only), 4=ignore
INVALIDATION: Hard (player absent post-analysis, postponement) vs Soft (weather update, minor news)
```
~480 tokens → full file ~4,200 tokens

---

## [COMPRESSED] Fan sentiment intelligence

**When to use:** Projecting commercial duration of a sporting outcome. LTUI updates
post-match. CDI calculation for any winning/losing outcome.

```
ARC PHASES: Peak(0-24h) → Celebration(1-7d) → Sustain(1-4wk) → Normalise(1-3mo) → Memory → Legacy
CDI = Base_Duration × Outcome_Tier × Competition_Weight × Drought_Factor
DECAY: λ constants — standard win 0.69 (half-life 1d), trophy 0.05 (half-life 14d)
FAN TYPES: Core(CDI×1.30), Seasonal(×0.85), Event-driven(×0.60), New-market(×0.75)
LTUI: Standard trophy +8-12, First drought-ending trophy +15-20
```
~310 tokens → full file ~5,800 tokens

---

## [COMPRESSED] Skill bundles

**When to use:** Developer integration; selecting correct skill stack for a use case.
Not needed for content analysis — only for system configuration.

```
BUNDLES: ftier1-football(~8200t), ftier1-cricket(~7400t), ftier1-basketball(~7100t),
         prematch-football(~4200t), governance-brief(~3400t), transfer-intel(~5100t),
         macro-only(~800t), minimal-signal(~2100t)
RULE: macro first, confidence-output-schema last
API: GET /bundle/{bundle_id}
```
~180 tokens → full file ~4,100 tokens

---

## [COMPRESSED] On-chain event intelligence

**When to use:** Fan token Tier 1 analysis with DeFi context. When on-chain smart
money signals are relevant to signal quality.

```
CATEGORIES: (1)Large wallet >0.5% supply moved (2)LP add/remove >15% pre-event
            (3)Governance execution on-chain (4)Staking ratio trend >5%/7d
            (5)Cross-chain bridges >2%/48h (6)Wallet age as conviction proxy
MODIFIERS: Accumulation ×1.00-1.15, Distribution ×0.85-1.00, LP add pre-event ×1.03,
           LP removal pre-event ×0.94, Staking rising ×1.04, Staking falling ×0.96
CAUTION: correlation ≠ causation; wash trading risk; regulatory context applies
```
~290 tokens → full file ~3,900 tokens

---

## [COMPRESSED] KOL influence intelligence

**When to use:** When social media amplification of a token/club is relevant to
HAS or LTUI projections. Pre-match if major KOL activity detected.

```
TIERS: T1 >500k followers (KIS 1.00), T2 50-500k (0.65), T3 5-50k (0.30), T4 <5k (0.08)
KIS = Tier × Reach × Sentiment × Timing × Credibility_Discount
HAS IMPACT: T1 +12-25pts, T2 +5-12pts, T3 +2-5pts (organic); paid promotion: no HAS modifier
TIMING: T-48h to T-2h pre-match ×1.30, Post-win ×1.20, Off-cycle ×0.80
PAID DETECTION: #ad tag, timing correlation, cluster deployment = marketing_activity not signal
```
~260 tokens → full file ~3,600 tokens

---

## [COMPRESSED] Agent intelligence model

**When to use:** Developer onboarding; understanding what SportMind agents can and
cannot do; framing a SportMind deployment for stakeholders.

```
INTELLIGENCE TYPE: ANI (narrow excellence in sports domain) — intentional, not a limitation
REASONING: 6-step chain applied by LLM to SportMind domain knowledge — ~94% calibrated accuracy
PLANNING: Multi-cycle autonomous operation (Level 0-4 autonomy); goal-execution not goal-setting
LEARNING: Human-mediated calibration pipeline — validated improvement, not instant self-modification
CONTEXT: WHO-WE-ARE.md + autonomous-agent-framework.md provides full purpose/ecosystem context
ASPIRATION: Domain ASI — exceeds any individual expert through community calibration + collective knowledge
```
~220 tokens → full file ~3,200 tokens

---

## [COMPRESSED] World Cup 2026

**When to use:** Any analysis involving national team players during WC2026.
NCSI calculations for WC2026 matches. WC2026 token opportunity assessment.

```
FORMAT: 48 teams, 12 groups, best 2 + 8 best-3rd advance (104 matches)
TIERS: Final 1.00, SF 0.92, QF 0.85, R16 0.72, Group-3 0.60, Group-1/2 0.35-0.45
HOST MODIFIERS: USA ×1.30, Mexico ×1.35, Canada (diaspora signal)
RIVALRY: Brazil-Argentina ×1.85, England-Germany ×1.60, USA-Mexico ×1.55
CDI WINNER: 112.5 days. $RMFC dual-nation scenario: 168 days
AGENT DAILY CYCLE: Macro → Schedule → Token nations → NCSI → DeFi → Signal
```
~240 tokens → full file ~7,200 tokens

---

## [COMPRESSED] EuroLeague basketball intelligence

**When to use:** European basketball fan token analysis. EuroLeague Final Four
signal. Club commercial potential assessment for European basketball.

```
ELS = Fan_Base_Depth × Intl_Reach × Token_Readiness × Squad_ATM
TOP CLUBS: Real Madrid (0.94), Barcelona (0.90), Fenerbahçe (0.82), Olympiacos (0.80)
COMPETITION: Final Four ×1.75, G5 series ×1.08, 3 games/7 days ×0.88 fatigue
RIVALRIES: Greek derby (Oly vs Pana) ×1.65, Istanbul derby ×1.40, ACB Clásico ×1.50
NBA CONNECTION: Draft prospect departure ×0.90 club, NBA alumni signing LTUI +5-8
```
~210 tokens → full file ~3,800 tokens



---

## [COMPRESSED] SportMind purpose and context

**When to use:** Agent initialisation before any sport-specific analysis. Replaces loading
WHO-WE-ARE.md + agent-framework purpose sections separately. Single ~600 token load.

```
5 NON-NEGOTIABLE RULES: (1) macro first (2) loading order: macro→market→domain→athlete→token→schema
(3) intelligence separation — never execute (4) confidence honesty — state SMS < 60 as PARTIAL
(5) sport primary signal: football T-2h lineup / cricket FORMAT FIRST / MMA WEIGH-IN FIRST /
    F1 qualifying delta / NHL morning skate / NBA DNP-rest / rugby kicker / tennis surface win%
ECOSYSTEM: Data → SportMind intelligence → Application → Execution (SportMind never touches execution)
SMS TIERS: 80-100 HIGH_QUALITY | 60-79 GOOD | 40-59 PARTIAL | 20-39 INCOMPLETE | 0-19 INSUFFICIENT
AUTONOMY: Level 0 supervised → Level 4 autonomous; financial/governance always Level 0-1
```
~280 tokens → full file ~600 tokens

---

## [COMPRESSED] Agent goal framework

**When to use:** Building goal-directed agents that adapt over time. When agent needs to set
intermediate goals not just execute a fixed schedule. Long-horizon deployments.

```
3 GOAL LEVELS: Terminal (human-set; never changes) → Instrumental (agent-set; adapts) → Immediate (tasks)
6 GOAL STATES: PENDING → ACTIVE → ACHIEVED/BLOCKED/FAILED/OBSOLETE
5 GENERATION TRIGGERS: decomposition | achievement creates deps | observed signals | calendar scan | failure diagnostic
GoalDirectedAgent: _add_goal() / achieve_goal() / get_next_goal() / planning_cycle() / get_goal_status()
USE WHEN: open-ended objective + uncertain timeline; vs plan-directed for fixed repetitive tasks
```
~200 tokens → full file ~3,400 tokens

---

## [COMPRESSED] Modifier recalibration v3

**When to use:** When applying derby, post-tournament opener, or two-legged tie predictions.
Agents should load this to apply the three protocol updates.

```
DERBY DRAW PREMIUM (UPDATED): when derby_active AND form_differential < 0.10 AND no elimination stakes
  → direction = DRAW_LIKELY (not HOME/AWAY); position_size capped 50%
POST-TOURNAMENT OPENER (NEW): first match of new season within 30 days of major tournament final
  → expand draw window; reduce positional confidence by 1 tier
TWO-LEGGED TIE LEG 1 (UPDATED): European two-legged format + Leg 1 + closely matched
  → add tactical_draw_premium; output as wide range (draw + either team plausible)
CONFIRMED UNCHANGED: athlete_modifier | qualifying_delta | india_pakistan ×2.00 | morning_skate | competition_tier
NEXT RECAL: when athlete_modifier reaches 15 records (~v3.25-v3.27)
```
~220 tokens → full file ~3,800 tokens

---

## [COMPRESSED] SportMind purpose and context — AGENT INIT

**Ultra-compressed version for agents that need the minimum viable context:**

```
SportMind = sports intelligence framework. Teaches LLMs to reason about sports commercially.
LOAD ORDER: macro → market → domain → athlete → fan-token → confidence schema (always this order)
NEVER: execute trades/votes/financial actions (intelligence only)
ALWAYS: check macro first; output SMS; state confidence honestly
OUTPUT FORMAT: {direction, adjusted_score, confidence_tier, recommended_action, sms, flags}
MCP TOOLS: sportmind_signal | sportmind_macro | sportmind_stack | sportmind_verify | sportmind_agent_status
```
~120 tokens → use when context window is severely constrained



---

## [COMPRESSED] Modifier recalibration v3 (protocol updates)

**When to use:** Any European football prediction. Load to apply the 3 updated protocols.
Critical for derby, season opener, and two-legged tie predictions.

```
DERBY DRAW PREMIUM: derby_active AND form_diff < 0.10 AND no_elimination → DRAW_LIKELY; size 50%
POST_TOURNAMENT_OPENER: first match new season within 30d of major tournament → expand draw window
TWO_LEGGED_LEG1: European two-legged + Leg 1 + closely matched → tactical_draw_premium; wide range
HIGH_STAKES_SYMMETRY (v4 addition): both teams equal high stakes + quality_diff < 0.08 → DRAW_LIKELY
CONFIRMED STABLE: athlete_modifier | qualifying_delta | india_pakistan×2.00 | morning_skate | dew_factor
```
~160 tokens → full files: recalibration-v3 (~3,800t), recalibration-v4 (~1,200t)

---

## [COMPRESSED] Agent goal framework

**When to use:** Building long-horizon adaptive agents. When task is open-ended
rather than a fixed schedule. Multi-season deployments.

```
GOAL LEVELS: Terminal(human-set) → Instrumental(agent-set, adapts) → Immediate(cycle tasks)
GOAL STATES: PENDING → ACTIVE → ACHIEVED/BLOCKED/FAILED/OBSOLETE
TRIGGERS: decomposition | achievement creates deps | signal observation | calendar scan | failure
GoalDirectedAgent: _add_goal() achieve_goal() get_next_goal() planning_cycle() get_goal_status()
USE: open-ended objective + uncertain timeline → goal-directed; fixed schedule → plan-directed
```
~170 tokens → full file ~3,400 tokens



---

## [COMPRESSED] Cross-sport signal monitor (Pattern 7)

**When to use:** Portfolio monitoring across multiple tokens/sports. When macro conditions
create correlated opportunities. Multi-sport fund management.

```
4 CONVERGENCE PATTERNS:
  MACRO_BULL_MULTI_SIGNAL: macro ≥ 1.10 + 3+ actionable tokens + avg strength ≥ 0.72
    → PORTFOLIO_ENTER: scaled positions across all actionable tokens
  SAME_WINDOW_MULTI_SPORT: 2+ different sports with events in 48h window
    → TIMED_ENTRY: pre-event entry for all clustered tokens
  NCSI_AMPLIFICATION: national team event → 2+ club tokens active simultaneously
    → NCSI_ENTER: weighted by individual ATM per national team
  COUNTER_CYCLE_OPPORTUNITY: mild bear (0.80-0.92 macro) + SMS ≥ 78 sport signal
    → SELECTIVE_ENTER: 50% position only; quality outweighs moderate macro headwind

SIGNAL STRENGTH: total_signal_strength() = sms/100 + KOL_boost + onchain_boost + NCSI_boost
CYCLE: 6h | AUTONOMY: Level 2 | FEEDS: Portfolio Monitor + Pre-Match Chain + Signal Bus
```
~200 tokens → full file ~4,800 tokens

---

## [COMPRESSED] Governance monitoring agent (Pattern 8)

**When to use:** Fan token governance participation. Any token with active governance.
Portfolio governance oversight across multiple tokens.

```
DECISION WEIGHT: Structural(0.80-1.00) | Commercial(0.55-0.75) | Operational(0.30-0.55) | Cosmetic(theatre)
LTUI PROJECTIONS: Structural YES +6-12 | Commercial YES +2-6 | Operational YES +0.5-2 | Cosmetic ≈0
THEATRE KEYWORDS: kit colour, jersey design, mascot name, logo poll, song choice
STRUCTURAL KEYWORDS: stadium naming, share sale, ownership, merger, transfer budget
QUORUM RISK: alert when participation < 10% with < 6h remaining
SAFETY: Level 1 MANDATORY — never votes autonomously; per-vote human authorisation only
CYCLE: 2h | AUDIT: governance_outcomes.jsonl
```
~180 tokens → full file ~4,200 tokens

---

## [COMPRESSED] Data connector templates

**When to use:** Building a production SportMind agent that needs live data.
Copy-paste starting point for all three essential data sources.

```
CONNECTOR 1 — football-data.org lineups:
  FootballLineupConnector: get_lineup(match_id) → lineup_unconfirmed flag + key_player_status
  Competition IDs: PL, PD, BL1, SA, FL1, CL, EL | Free tier: 10 req/min

CONNECTOR 2 — KAYEN fan token market (no API key):
  FanTokenMarketConnector: TVL tier (DEEP≥$5M / MODERATE≥$500k / THIN≥$50k / MICRO)
  check_liquidity_gate() → proceed/blocked; spread flag; portfolio_snapshot()

CONNECTOR 3 — CoinGecko macro state (no API key):
  MacroStateConnector: BTC price → BULL×1.15 / NEUTRAL×1.00 / BEAR×0.75 / EXTREME_BEAR×0.50
  sportmind_startup_check() → phase + modifier + gate + BTC price; is_stale(4h threshold)

INTEGRATION: agent_with_connectors.py shows all 3 in correct SportMind loading order
```
~230 tokens → full file ~6,800 tokens



---

## [COMPRESSED] Modifier recalibration v5 (100-record milestone)

**When to use:** Understanding current accuracy claims; applying athlete_modifier
at preliminary calibration level; briefing stakeholders on library reliability.

```
athlete_modifier PRELIMINARY (15 records): 13/15 correct (87%) — CONFIRMED STABLE
  Non-football: 4/4 basketball, 3/3 MMA, 2/2 NHL, 1/1 rugby all 100%
  Football 75% (explained by draw protocols — not modifier failure)
  Range unchanged: 0.55-1.25

100-RECORD MILESTONE (95/100 = 95%):
  ALL 5 wrong = European football draws
  Zero wrong records in any other sport or prediction type
  Records 81-100: 20/20 correct direction (perfect 20-record run)

8 ZERO-WRONG MODIFIERS: qualifying_delta(F1) · india_pakistan×2.00 · morning_skate(NHL) ·
  dew_factor(cricket) · taper_modifier(swimming) · raider_primacy(kabaddi) ·
  goalkeeper_save_rate(handball) · superspeedway_specialist(NASCAR)
NEXT: athlete_modifier at 25 records → recalibration-v6
```
~180 tokens → full file ~3,200 tokens

---

## [COMPRESSED] Modifier recalibration v6 (120-record milestone)

**When to use:** Draw protocol application; athlete_modifier second preliminary;
understanding protocol confidence tiers before European football predictions.

```
athlete_modifier SECOND PRELIMINARY (25 records): 21/25 (84%) headline
  But: non-football 18/18 (100%), football with protocols 7/7 (100%)
  Protocol-override errors: 0/4 (0%) — NEVER OVERRIDE TIER 1 protocols
  Range unchanged: 0.55-1.25 — CONFIRMED STABLE

DRAW PROTOCOL TIERS:
  TIER 1 — NEVER OVERRIDE:
    two_legged_leg1: European + two-legged + Leg1 + quality_diff < 0.12 → DRAW_LIKELY
    high_stakes_symmetry: both teams equal stakes + quality_diff < 0.08 → DRAW_LIKELY
    Evidence: 4/4 correct when applied; 0/4 when overridden
  TIER 2 — APPLY CONSISTENTLY:
    derby_active + form_diff < 0.10 → DRAW_LIKELY; 50% cap
    post_tournament_opener → expand draw window; -1 confidence tier
  OVERRIDE RULE: requires SMS > 80 AND quality_diff > 0.20; max 30% position

120-RECORD MILESTONE (115/120 = 95.8%): Records 101-120 = 20/20 perfect run
NEXT: athlete_modifier at 40 records → recalibration-v7
```
~220 tokens → full file ~2,800 tokens



---

## [COMPRESSED] Gamified tokenomics intelligence — Fan Token Play

```
SOURCES: Chiliz official articles 09 Apr 2026 + 17 Apr 2026
CONFIRMED TRIAL: $AFC (Arsenal FC) — UCL vs Sporting Lisbon, 07 Apr 2026

SCOPE (CRITICAL): Only official men's first-team competitive matches trigger FTP.
  ❌ Friendlies | Pre-season | Exhibition | Academy | Women's — NO FTP mechanics

CORE MECHANICS (both paths):
  WIN  → tokens burned (supply decreases permanently)
  LOSS → tokens minted (supply increases / restored)
  DRAW → supply unchanged

PATH 1 — Protocol-Level Treasury Governance:
  Trigger: on-chain oracle confirms result → smart contract executes
  WIN: permanent burn at BASE RATE (binary — no goal-diff scaling confirmed)
  LOSS: new tokens minted to treasury (supply expands)
  Annual inflation: 1–5% variable linked to season win% (PART OF PROTOCOL, not fallback)
    Tiered model: 0% below 45% win rate; scales sharply above 60%
  Stop-loss: 75% net reduction OR treasury = 0% → burning ceases
  Burn credits: wins at stop-loss generate credits offsetting future minting
  Vesting cap: 12.5% treasury/year (NOT CURRENTLY ACTIVE for any token — Apr 2026)

PATH 2 — Prediction Market-Based (ACTIVE TRIAL — $AFC only):
  T-48h: treasury sells 1/400th of supply → USDT (0.25% pre-liquidation)
  Kickoff: USDT → WIN prediction on prediction market (ALWAYS bets WIN — mechanical)
  WIN (T+48h): 95% of proceeds → buyback + permanent burn (5% fee deducted)
  LOSS (T+48h): pre-liquidated amount minted back to treasury (supply-neutral)
  Path 2 asymmetry: WIN = permanent burn | LOSS = neutral (not Path 1's expansion)

48H EXECUTION WINDOWS (both directions, per official source):
  Liquidations (pre-match): within 48h of kickoff
  Buybacks (WIN): within 48h of final result
  Minting (LOSS): within 48h of final result
  Agent verification timing: T+30min minimum | T+6h recommended | T+24h → BURN_MISSING

AGENT HARD RULES:
  Pre-liquidation = PROTOCOL_EVENT (never bearish distribution signal)
  Protocol always bets WIN — its bet is NOT outcome intelligence
  Never apply burn modifier before T+15 post-match (AMM rebalancing)
  Verify gamified status via KAYEN API before applying this skill
```
REF: fan-token/gamified-tokenomics-intelligence/gamified-tokenomics-intelligence.md


## [COMPRESSED] Macro regulatory SportFi intelligence

**When to use:** Any analysis involving US market tokens, EU tokens, or Phase 5 RWA
tokens. Load alongside macro-overview.md for jurisdiction-aware signal generation.

```
EU — MiCA (FULLY ACTIVE January 2025):
  Pure utility fan tokens: utility token classification → regulatory_clarity = HIGH
  Revenue-sharing tokens: securities analysis required → regulatory_complexity_flag
  
US — Joint SEC/CFTC Guidance (LANDMARK 2026):
  Utility fan tokens classified as UTILITY DIGITAL COMMODITIES (CFTC, not SEC)
  This is the regulatory unlock for US market re-entry (Q1 2026 per Chiliz roadmap)
  First US partnership: Q1 2026; US sports (NFL, NBA, MLB, NHL) now viable
  Revenue-sharing / equity tokens: still require securities analysis
  
BRAZIL: First revenue-sharing RWA live on Chiliz Chain → Phase 5b confirmed real
UK: FCA utility token framework active; MEDIUM regulatory clarity

REGULATORY_DISCOUNT (apply to signal):
  HIGH clarity (EU/US utility): 0.00 discount
  MEDIUM_HIGH (UK, Brazil): 0.05 discount
  MEDIUM: 0.10 discount
  LOW: 0.20 discount
  RESTRICTED (China): ABSTAIN — do not generate signal
  
US_MARKET_ENTRY_SIGNAL: Tier 1 macro event when first US token launches
  CDI window: 45-60 days (longer than standard) across ecosystem
```
~210 tokens → full file ~4,200 tokens


---

## [COMPRESSED] Sequential thinking integration

**When to use:** Any agent running the five-phase SportMind chain. Load at
agent initialisation alongside sportmind_pre_match tool.

```
5 PHASES: (1)macro_gate → (2)pre_match_signal → (3)disciplinary_check
          → (4)fan_token_context → (5)signal_synthesis
STOP CONDITIONS: Phase 1: modifier<0.75→WAIT_MACRO_OVERRIDE
                 Phase 3: LEGAL_PROCEEDINGS_ACTIVE→ABSTAIN
                          COMMERCIAL_RISK_ACTIVE→reduce signal, continue
ENTER CONDITIONS (ALL): macro≥0.75 + SMS≥60 + no commercial flags + lifecycle Phase 2-3
WAIT CONDITIONS (ANY): SMS 40-59 | CITING_ACTIVE | lineup unconfirmed | Phase 4
PORTFOLIO RULE: Each token analysis is independent — WAIT on PSG does not flag BAR
FAILURE ANALYSIS: Phase→Value→Timeline→Monitor condition→Re-analysis trigger
```
~180 tokens → full file: platform/sequential-thinking-integration.md

---

## [COMPRESSED] Memory integration

**When to use:** Multi-session agents, portfolio monitoring, pattern detection.
Load at session start to retrieve prior state.

```
4 SCHEMAS: token_memory{signal_history, dsm_history, lifecycle, upcoming_events}
           macro_memory{modifier_history, phase_transitions}
           player_disciplinary{repeat_offender, resolution_timeline}
           portfolio_summary{all_recommendations, active_flags}
SESSION START: retrieve portfolio_summary → macro_state → per-token records → surface changes
SESSION END: update signal_history + dsm_history + consecutive_signals + upcoming_events
4 PATTERNS: (1)macro_recovery_detection (2)repeat_disciplinary_signal
            (3)consecutive_WAIT_detection (4)pre_event_preparation
DECAY: Clear on resolution | Archive >6mo | NEVER delete repeat_offence_history
```
~180 tokens → full file: platform/memory-integration.md

---

## [COMPRESSED] Fetch MCP disciplinary

**When to use:** Phase 3 of sequential chain. After sportmind_disciplinary
returns regulatory source URL — fetch it to verify current status.

```
SOURCES BY SPORT:
  Football:  thefa.com/football-rules-governance/disciplinary + UEFA.com/insideuefa/disciplinary
  Rugby:     world.rugby/the-game/judicial-decisions (PDF list, search player name)
  F1:        fia.com/documents/decisions (PDFs indexed; racefans.net for points tracker)
  MMA:       usada.org/testing/results/sanctions + ufc.com/news
  Cricket:   icc-cricket.com/about/cricket/rules-and-regulations/code-of-conduct
  NHL:       nhl.com/news/department-player-safety
WORKFLOW: sportmind_disciplinary → sportmind_verifiable_source → fetch(URL) → apply DSM → memory
ERRORS: unavailable→DSM_MODERATE precautionary | not found→NOT_FOUND_IN_DECISIONS flag
RULE: Fetch follows sportmind_verifiable_source. Does not explore freely.
```
~200 tokens → full file: platform/fetch-mcp-disciplinary.md

---

## [COMPRESSED] Chiliz Chain address intelligence

**When to use:** Fan token Tier 1 analysis. Before generating commercial signal —
check on-chain concentration and velocity via chiliscan API.

```
6 SIGNALS:
  (S1) Concentration: top-10 hold >70%=EXTREME(×0.80) >50%=HIGH(×0.90) >30%=MODERATE <30%=LOW(×1.05)
  (S2) Smart wallet: accumulation ×1.08-1.15 | distribution ×0.80-0.88 | consensus(3+) max multiplier
  (S3) Holder trend: +5%/7d=strong organic | -5%/7d=significant decline flag
  (S4) Velocity: >3×baseline=SPIKE(investigate) | <0.7×=QUIET
  (S5) Acquisition: >500 new wallets/week=HIGH | near zero=Phase 5/6 signal
  (S6) DSM calibration: measure holder_exit_rate post-disciplinary → calibrate DSM values
MODIFIER ORDER: macro × DSM × concentration × velocity = final
API: chiliscan.com Etherscan-compatible, no key required for basic queries
```
~200 tokens → full file: platform/chiliz-chain-address-intelligence.md

---

## [COMPRESSED] Social intelligence connector

**When to use:** KOL activity detected pre-match; sentiment snapshot needed;
AELS calculation for athlete. Choose X API or LunarCrush per scenario.

```
X API (real-time narrative):
  search_recent(query) → post volume + engagement scoring
  get_token_mindshare(ticker) → mention_count + mindshare_tier (VIRAL/HIGH/MODERATE/LOW/MINIMAL)
  get_ecosystem_sentiment() → top tokens by mention + ecosystem_tweet_count
  get_mindshare_trend(ticker, [1,7,30]) → trend_direction (ACCELERATING/GROWING/STABLE/DECLINING)

LUNARCRUSH (composite scores):
  get_token_galaxy_score(ticker) → Galaxy Score(0-100) + AltRank + social_volume_24h
  get_token_influencers(ticker) → ranked influencer list with KOL tier estimate
  get_topic_social_score(topic) → social health for sports without fan tokens (MMA/F1/golf)
  get_athlete_social_profile(id, network) → engagement_rate → AELS tier

GALAXY SCORE MODIFIER: ≥70=×1.08 | 50-69=×1.03 | 30-49=×0.97 | <30=×0.90 + Phase4 flag
RULE: Social modifier applied AFTER macro + DSM. Never overrides ABSTAIN.
```
~220 tokens → full file: platform/social-intelligence-connector.md

---

## [COMPRESSED] API providers guide

**When to use:** Connecting live data to a SportMind agent. Quick provider selection
before building connectors. Developer onboarding.

```
QUICKEST PATH (football, <1hr to signal):
  API-Football: dashboard.api-football.com → 100 req/day free → lineups + stats + standings

MULTI-SPORT (API-Sports suite, one account):
  football / basketball / baseball / rugby / cricket / handball
  URL pattern: https://v1.{sport}.api-sports.io/{endpoint}

FREE NO-KEY SOURCES:
  Jolpica F1: api.jolpi.ca/ergast/ → qualifying delta + results (unlimited)
  Open-Meteo: api.open-meteo.com → weather all sports (unlimited)
  balldontlie: balldontlie.io → NBA (60 req/min)

EXISTING TEMPLATES (data-connector-templates.md):
  football-data.org lineups | KAYEN fan tokens | CoinGecko macro state

END-TO-END FLOW: PSG vs Arsenal UCL QF → 8 phases in platform/api-providers.md
```
~180 tokens → full file: platform/api-providers.md

---

## [COMPRESSED] World Cup 2026 intelligence

```
TOURNAMENT: June 11 – July 19, 2026 | 48 teams | 104 matches | USA/Canada/Mexico
TIME SENSITIVE: tournament is active — load this before any WC2026 analysis

NCSI AMPLIFIER: ×3.5 group stage → ×4.0 final (vs ×1.0 standard domestic)
CQS CONTEXT: US primetime + sold-out venue = 1.35–1.40 (standard match = 1.00)

PATH_2 + WC2026:
  Protocol mechanics UNCHANGED — same 0.25% pre-liquidation, WIN=burn, LOSS=neutral
  What changes: commercial significance of each burn is 3.5–4× more impactful
  AGENT RULE: T-48h pre-liquidation during WC = PROTOCOL_EVENT (never bearish, same as domestic)

NATIONAL TOKENS (structural differences from club tokens):
  No domestic matches → HAS dormant outside tournaments → maximum spike at WC
  No PATH_2 (as of 2026) — supply is holder-driven only
  CDI windows: Group exit=18 days | QF exit=40 days | Winner=75 days
  Holder mix: higher Speculator share → elevated MRS risk at elimination
  Entry window: T-14 days to T-2h of first group match
  HARD RULE: NEVER enter/maintain national token within 4h of elimination match

CALENDAR_COLLAPSE on elimination:
  National token: HAS decay in 6h, Speculator exit in 24h, CDI reset
  Club token: REMOVE NCSI amplifier; domestic cycle continues; PATH_2 unchanged
  Signal chain: confirm elimination → raise CALENDAR_COLLAPSE → CDI reset → WAIT 72h

POST-TOURNAMENT RESET:
  Winner NCSI: ×1.5 at day 30 → ×1.0 at day 60
  Golden Boot/Ball winner: personal NCSI ×1.3 until Jan 2027
  Transfer window intersection: Aug 15–31 peak; ATM World Cup standout = elevated APS
  DOUBLE EVENT WARNING: PATH_2 club losing ATM World Cup winner = NCSI_WIN + LTUI_DEPARTURE

TOURNAMENT KNOCKOUT MULTIPLIERS:
  R32: ×1.4 vs group | R16: ×1.6 | QF: ×1.9 | SF: ×2.2 | Final: max
  Winner: +25–60% national token | Club star (Golden Boot): +12–22%

$ARG SPECIAL: defending champion + narrative amplifier ×1.25 (if Messi final WC confirmed)
```
REF: fan-token/world-cup-2026-intelligence/ · fan-token/gamified-tokenomics-intelligence/


## [COMPRESSED] Transfer window intelligence

**When to use:** During active transfer windows (summer Jul 1–Sep 1, Jan 1–Feb 1).
Load alongside football-token-intelligence/ for window-aware signal generation.

```
5 SUMMER PHASES: A=pre-window(+0-5%) B=early(+3-8%) C=peak-speculation(+5-12%)
                 D=deadline-day(WAIT 6h before close; ±15-20% volatility)
                 E=post-window(certainty premium +2-5%)
JANUARY: 60% of summer modifiers. Distress buying (3+ signings) = concern flag -2-4%.

4 CROSS-TOKEN CONTAGION TYPES:
  (1) Selling club -6-15% / buying club +4-12%
  (2) Competitor strengthening -1-3% indirect
  (3) Market valuation benchmark → APS recalibration
  (4) League-wide narrative: 3+ major signings same week → all active tokens +1-3% for 48h

LIFECYCLE INTERACTION: Phase 3 + strong window = sustained HAS
                       Phase 4 + window = temporary reversal, faster decay (CDI×0.50)
SOURCE TIERS: Romano "here we go"=Tier 1 | Athletic/Sky Sports=Tier 2 | tabloid=Tier 3(0.3×)
WC2026 OVERLAP (Jul 1-19): apply BOTH NCSI signal AND transfer speculation (cap: 1.25× either alone)
```
~210 tokens → full file: fan-token/transfer-window-intelligence/transfer-window-intelligence.md

---

## [COMPRESSED] Media intelligence

**When to use:** Any signal that depends on press conference availability statements,
transfer reports, or news velocity affecting CDI. Load alongside breaking-news-intelligence.

```
3 SIGNAL TYPES:
  TYPE 1 Breaking news: hard facts pre-official → Tier 2 confidence; verify Tier 1 ASAP
  TYPE 2 Directional: "manager plans rotation" → directional modifier only; 0.7× confidence
  TYPE 3 Narrative: coverage volume → CDI extension (feeds narrative-momentum.md)

JOURNALIST TIERS (football):
  TIER 1: Romano "here we go" = confirmed | official club/league sources
  TIER 2: The Athletic | L'Équipe | Marca/AS | Gazzetta | ESPN FC | Sport Bild (0.7× weight)
  TIER 3: UK tabloids | unverified social → monitoring flag only (0.3× weight)

PRESS CONF AVAILABILITY DECODER:
  "Fully fit" → CONFIRMED | "In contention" → PROBABLE(×0.95) | "Day by day" → DOUBTFUL(×0.80)
  "Had a knock" → DOUBT(×0.70) | "Long-term" → OUT extended | No mention → investigate

VELOCITY × CDI: VIRAL(>20 art/day 3+days) → CDI×1.40 | HIGH → ×1.20 | LOW → ×0.75
SATURATION: >3 weeks same narrative → reduce to ×1.00 (priced in)
```
~220 tokens → full file: core/media-intelligence.md

---

## Updated compressed skill index

| Compressed skill | Full skill location | Approx tokens |
|---|---|---|
| Sequential thinking | `platform/sequential-thinking-integration.md` | 180 |
| Memory integration | `platform/memory-integration.md` | 180 |
| Fetch MCP disciplinary | `platform/fetch-mcp-disciplinary.md` | 200 |
| Address intelligence | `platform/chiliz-chain-address-intelligence.md` | 200 |
| Social connector | `platform/social-intelligence-connector.md` | 220 |
| API providers | `platform/api-providers.md` | 180 |
| World Cup 2026 | `fan-token/world-cup-2026-intelligence/` | 210 |
| Transfer window | `fan-token/transfer-window-intelligence/` | 210 |
| Media intelligence | `core/media-intelligence.md` | 220 |


---

## [COMPRESSED] Post-match signal framework

**When to use:** Within 4h of any match result involving a held fan token.
Governs the commercial signal window after a result is confirmed.

```
TIME WINDOWS:
  T+0 to T+2h: confirmation only — do NOT generate commercial signal (price discovery)
  T+2h to T+24h: primary commercial signal generation window
  T+24h: CDI confirmation — is elevation sustained or mean-reverting?
  T+72h: decay assessment — update CDI estimate vs actual

RESULT MODIFIERS:
  Expected win:     standard CDI | Galaxy Score +8-15pts | ENTER T+2h
  Unexpected win:   CDI ×1.3-1.5 | Galaxy Score +15-25pts | ENTER T+2h (strongest signal)
  Expected loss:    negative CDI | WAIT T+24h minimum before reassessing
  Unexpected loss:  ABSTAIN | mandatory checklist | calibration record required
  Dominant win(5-0+): dominant_win_multiplier ×1.20-1.35 | NCSI amplification ×1.15-1.25

POST-MATCH NCSI: confirm ATM player performance tier → apply competition amplifier → club token impact
CALIBRATION: every match = opportunity. Wrong predictions = most valuable records.
SEQUENCE: verify result(Tier 1) → wait T+2h → macro check → sentiment_snapshot → result modifier → CDI clock
```
~200 tokens → full file: core/post-match-signal-framework.md

---

## [COMPRESSED] Prediction market intelligence

**When to use:** Any pre-match analysis for sports with Azuro/Betfair coverage.
Confirming or contradicting SportMind signal with market consensus.

```
DIVERGENCE FRAMEWORK:
  SportMind implied prob = adjusted_score / 100
  Market implied prob = 1 / decimal_odds

  <10% divergence: ALIGNMENT — full conviction, no adjustment
  10-20% divergence: INVESTIGATE — check lineup/injury/weather/breaking news
  >20% divergence: HIGH CONVICTION or MISSING INFO — mandatory 4-check protocol
  Direction contradiction (>30%): ENTER at 50% sizing only; all checks must pass

POOL DEPTH (market quality):
  >$500k TVL: INSTITUTIONAL — full weight
  $50k-$500k: RETAIL — 0.85× weight
  $5k-$50k: THIN — directional only, 0.5× weight
  <$5k: NEGLIGIBLE — ignore

AZURO: primary crypto prediction market (EVM, Chiliz-compatible)
BETFAIR: highest quality signal for football (sharpest peer-to-peer market)
GAMIFIED TOKENOMICS INTERACTION: prediction market → match outcome probability
                                 fan token signal → commercial sentiment (different signal)
RULE: prediction markets do NOT replace fan token commercial signal framework.
      They confirm/contradict pre-match match outcome probability only.
```
~210 tokens → full file: core/prediction-market-intelligence.md

---

## [COMPRESSED] Verifiable ML roadmap

**When to use:** Evaluating SportMind's long-term trust architecture.
Building on-chain applications requiring signal provenance. v4.0 planning.

```
CURRENT (v3.x): rules-based framework — social trust (calibration records public)
TARGET (v4.0+): trained model + ZK proofs — cryptographic trust

PATH:
  STEP 1: Train SportMind signal model (needs 500+ calibration records; current: 126)
  STEP 2: EZKL framework — converts ONNX → ZK circuit, EVM/Chiliz-compatible
  STEP 3: Proof generation → commitment on-chain → permissionless verification
  STEP 4: Chiliz Chain signal registry contract → queryable by Azuro/DeFi protocols

CRITICAL DEPENDENCY: 500+ calibration records (current: 126)
  Every v3.x record = training data for v4.x model
  Community calibration drive is the critical path item

TIMELINE: v4.0 target 2027 (conditional on calibration record milestone)
BENCHMARK: trained model must match/exceed current 96% direction accuracy

WHY IT MATTERS: verifiable provenance → on-chain signal markets → DeFi collateral
               → RWA/Phase 5 applications → signal quality commands price premium
```
~170 tokens → full file: platform/verifiable-ml-roadmap.md


*MIT License · SportMind · sportmind.dev*

## [COMPRESSED] Perceptual-Pressure Intelligence (PPI)

```
PPI = (clutch_record×0.35) + (high_stakes_history×0.30) + (experience_depth×0.20) + (recovery_rate×0.15)
SCALE: 80-100=Elite(×1.15) | 65-79=Strong(×1.08) | 50-64=Adequate(×1.00) | 35-49=Vulnerable(×0.93) | <35=Fragile(×0.86)
ELITE SIGNALS: Final-frame win rate >70% (snooker), Q4 passer rating >95 (NFL), major win rate >25% (golf/tennis).
KEY RULE: First appearance at iconic venue (Crucible, Ally Pally, Wembley final) → uncertainty flag. Never assume elite PPI.
FAN TOKEN: Elite PPI player = reduced LTUI volatility. Fragile PPI = amplified negative signal on shock loss.
Full skill: core/perceptual-pressure-intelligence.md
```

## [COMPRESSED] Game Tempo Intelligence (TCM)

```
TCM formula: (pace_advantage×0.35) + (transition_speed×0.25) + (set_piece_dependency_inv×0.20) + (congestion_factor×0.20)
BASKETBALL: Pace >103 possessions/48min = tempo team. Against slow opponent: ×1.06. B2B: ×0.93 (pace first to go).
CRICKET: DLS scenario = tempo disruption — reload signal. Over-rate <13/hr = slow team, affects last-over pressure.
FOOTBALL: High press PPDA <8 = tempo-forcing team. Second-half press decline at 60min = away team tempo window.
TENNIS: Serve+1 pattern (deliberate pace) vs baseline grinder = tempo mismatch. Advantage: server on fast surfaces.
Full skill: core/game-tempo-intelligence.md
```

## [COMPRESSED] Athlete Decision Intelligence (DQI)

```
DQI = (chance_creation_xA×0.30) + (possession_decision×0.25) + (shot_selection×0.25) + (defensive_anticipation×0.20)
SCALE: 85-100=Elite(×1.12) | 70-84=Strong(×1.06) | 55-69=Good(×1.00) | 40-54=Average(×0.95) | <40=Poor(×0.88)
SCOUTING: DQI feeds directly into Pattern 10 CVS formula — elite DQI adds ×1.08 to role-appropriate positions.
KEY METRICS: xA ≥0.20/90 (midfielder), progressive passes ≥7/90, press resistance ≥65% pass completion under pressure.
ANTI-TRAP: Assists count ≠ DQI. High assists + low xA = dependent on teammates finishing. Use xA only.
Full skill: core/athlete-decision-intelligence.md
```

---

## [COMPRESSED] Athlete Readiness Index (ARI)

```
FORMULA: ARI = weighted_product(fatigue×0.30, motivation×0.20, travel×0.20, injury_risk×0.20, availability×0.10)
RANGE: 0.60–1.10 | 1.00=baseline | 0.90=mild concern | 0.80=significant | 0.70=serious | 0.60=floor
APPLICATION: composite_athlete_modifier × ARI (final readiness gate — backward compatible)

FATIGUE (0.30): 7+days=1.05 | 3days=0.97 | B2B=0.92 | 3-in-7=0.88 | 4-in-10=0.80
  Age mult: <23=×0.97 | 29–32=×1.03 | 33+=×1.06
MOTIVATION (0.20): bridge from MI score → 1.08(peak) to 0.85(disengaged)
  CONTRACT_YEAR=+0.08 | REVENGE_MATCH=+0.06 | CONFIRMED_DEPARTURE=−0.10
TRAVEL (0.20): bridge from TIS → 1.00(domestic) to 0.82(floor)
  International returnee <72h=0.90 | <48h=0.86 | <24h=0.82
INJURY RISK (0.20): LAS×recurrence_mult | LAS(high_intensity): 0–25matches=0.00 | 46–50=0.18 | 51+=0.25
  Return <4wk=×1.40 | return <8wk=×1.20 | two soft-tissue=×1.35
AVAILABILITY (0.10): official_lineup=1.00 | tier2_source=0.93 | doubt=0.72 | out=0.00

FAN TOKEN: ARI<0.80 any ATM-tier player → FTIS dampener −5pts | two+ → −10pts
LABELS: ≥1.05=PEAK | 0.95–1.04=READY | 0.85–0.94=MINOR | 0.75–0.84=CONCERN | <0.75=ESCALATE
```
REF: core/athlete-readiness-index.md

---

## [COMPRESSED] Opponent Tendency Intelligence (OTP)

```
PURPOSE: Historical behavioural profiles of specific opponents (teams/coaches/athletes)
DISTINCT FROM TMAS: TMAS=structural system mismatches | OTP=what opponent actually does

FOUR DOMAINS:
1. COACH IN-GAME: substitution timing (early<55m | standard | late>71m) | formation shift triggers
   Trailing at 60min: does coach attack or wait? | Leading: does he drop deep?
2. SITUATIONAL: ELIMINATION_RISER vs ELIMINATION_FALLER | derby changes tendencies?
   When trailing late: all-out vs managed | win streak behaviour
3. SET PIECE: corner delivery (inswinger/outswinger, near-post %) | free kick zones
   PENALTY: direction bias — use privately only (half-life intelligence)
4. ATHLETE MICRO: dribble direction bias | serve pattern under pressure | grappling entry

SAMPLE MINIMUMS: team tendencies=20 matches | coach=15 matches | athlete=30 situations
Below minimum → classify as PRELIMINARY (lower confidence)

TENDENCY HALF-LIFE: set piece routines=4–8wk | formation shifts=6–12mo | must-win profile=persistent

SIGNAL CHAIN: Load OTP after TMAS. OTP CONFIRMS structural signal → proceed
  OTP CONTRADICTS structural signal → FLAG for human review (do not silently suppress)
```
REF: core/opponent-tendency-intelligence.md

---

## [COMPRESSED] Contextual Signal Environment (CQS)

```
FORMULA: CQS = weighted_avg(schedule_slot×0.25, venue_weight×0.20, audience×0.25,
                              density×0.15, season_position×0.10, territory×0.05)
RANGE: 0.60–1.40 | 1.00=standard mid-table afternoon match

APPLICATION: FTIS×CQS | CDI×CQS | HAS×√CQS (square root dampens HAS swings)
CRITICAL: CQS does NOT modify SMS. SMS=outcome probability. CQS=commercial magnitude.

SCHEDULE SLOT: UCL Final primetime=1.40 | Sat 5:30pm EPL=1.20 | Sun 2pm=1.00 | early Sun=0.75
VENUE: UCL Final neutral=1.35 | Wembley/Bernabeu=1.25 | full Tier1 stadium=1.10 | empty=0.70
AUDIENCE: UCL Final global=1.40 | international broadcast=1.20 | domestic only=1.00
DENSITY: isolated (no other top matches)=1.15 | standard weekend=1.00 | crowded=0.85
SEASON: title decider/relegation final day=1.30 | October–March standard=1.00 | pre-season=0.65
TERRITORY: US prime time=1.25 | European prime=1.10 | Asian morning=0.75

CANONICAL: UCL QF (Arsenal/PSG) = CQS 1.27 | Dead rubber = 0.73 | Standard PL = 1.00

DEAD_RUBBER_FLAG: if team cannot affect league position → CQS ceiling 0.75
BEHIND_CLOSED_DOORS: override → CQS floor 0.70 regardless of other dimensions
```
REF: core/contextual-signal-environment.md

---

## [COMPRESSED] Travel and Timezone Intelligence (TIS)

```
FORMULA: TIS = 1.00 − (timezone_penalty + haul_penalty + recovery_penalty − adaptation_bonus)
RANGE: 0.80–1.00 | 1.00=no impact | 0.85=significant | 0.80=severe
APPLICATION: athlete_modifier × TIS (per-player or team-wide)

ONLY APPLY when ONE team has materially more travel burden — cancel if both equal.

TIMEZONE PENALTY (eastward > westward rule):
  Eastward: 1–2TZ=0.00 | 3–4TZ=0.02 | 5–6TZ=0.05 | 7–8TZ=0.08 | 9+TZ=0.12
  Westward: 1–3TZ=0.00 | 4–6TZ=0.02 | 7–9TZ=0.04 | 10+TZ=0.07
  
HAUL PENALTY (flight duration, independent of TZ):
  <2h=0.00 | 2–4h=0.00 | 5–8h=0.03 | 9–12h=0.06 | 13–16h=0.09 | 17+h=0.12

RECOVERY PENALTY (time between arrival and match):
  Arrived 5+days before=0.00 | 3–4days=0.01 | 2days=0.04 | 1day=0.08 | same day=0.14

SPORT-SPECIFIC: F1 penalty=0.50× (car-dominated) | NBA B2B road trip=0.95×
INTERNATIONAL RETURNEE: 5+TZ, return <72h → TIS 0.90 | <48h → 0.86 | <24h → 0.82
Flag: INTERNATIONAL_RETURNEE_SHORT_PREP
```
REF: core/travel-timezone-intelligence.md

---

## [COMPRESSED] Agent Cognitive Architecture

```
PURPOSE: Maps SportMind to standard AI taxonomy for enterprise evaluation

ARCHITECTURE RATINGS (★=weak, ★★★★★=strong):
REACTIVE ★★★: breaking news triggers, freshness flags, macro override
  → Core files: breaking-news-intelligence.md, temporal-awareness.md

MODEL-BASED REFLEX ★★★★★ [PRIMARY]: Six-step chain, tendency profiles, lifecycle models
  → Skill library IS the world model. Hidden state reasoning is SportMind's core.
  → Files: reasoning-patterns.md, opponent-tendency-intelligence.md, fan-token-lifecycle/

GOAL-BASED ★★★★: Terminal→Instrumental→Immediate goal hierarchy. Autonomy levels 0–4.
  → Files: agent-goal-framework.md, autonomous-agent-framework.md

UTILITY-BASED ★★★★★: ENTER/WAIT/ABSTAIN is the terminal utility function.
  → TMAS, ARI, CQS, MRS are all utility functions. Multi-variable trade-off.

LEARNING ★★★ [INTENTIONALLY CONSTRAINED]: Library-level only (calibration→recalibration)
  → NOT agent-level. Deliberate — prevents unauditable drift.
  → Files: calibration-framework.md, modifier-recalibration-v3–v6.md

MAS ★★★★: Signal bus, conflict hierarchy, system orchestrator
  → Files: multi-agent-coordination.md, multi-agent-context-sharing.md

BDI ★★★★: Beliefs=skill library | Desires=goal framework | Intentions=six-step chain
  → Intention reconsideration on breaking news events

KEY HONEST STATEMENTS:
  SportMind is domain-specific AI (sports/fan tokens), not general-purpose
  Learning is constrained for auditability — this is a feature, not a weakness
  Agent boundary is architectural — produces intelligence, never executes
```
REF: core/agent-cognitive-architecture.md

---

## [COMPRESSED] Web Agent Connectors

```
ARCHITECTURE: SportMind returns targets+specs → web agent fetches → SportMind interprets
  Never auto-update library from web agent output. Human confirms all library changes.

CONNECTOR 1 — LINEUP CONFIRMATION:
  Football T-75min: club official X (@Arsenal etc) | Premier League /match/{id}/lineups
  NBA T-90min: nba.com/game/{id}/injury-report | status: Available/Questionable/Doubtful/Out
  Cricket: ESPNcricinfo post-toss | MMA: UFC weigh-in results T-24h
  Translation: confirmed_starter=1.00 | doubt=0.65–0.72 | absent=0.00
  On absence: re-run ARI, raise ABSENCE_CONFIRMED, reload TMAS if formation changed

CONNECTOR 2 — PATH_2 SUPPLY VERIFICATION:
  API: chiliscan.com/api?module=token&action=tokeninfo&contractaddress={contract}
  Burn tx: same API, address=0x0000...0000, sort=desc
  Timing: T+15min minimum | T+30min recommended | T+6h definitive | T+24h before BURN_MISSING
  WIN: delta/pre_supply ≈ 0.0024 (±0.05% tolerance) → BURN_CONFIRMED
  LOSS: delta = 0 expected → if supply increased: SUPPLY_ANOMALY flag immediately

CONNECTOR 3 — REGULATORY MONITORING:
  Tier 1 (act 24h): ESMA register | SEC/CFTC press releases | Chiliz blog | Chiliz Twitter
  Tier 2 (review 72h): Socios fan-tokens page | CoinDesk/The Block regulatory
  Files at risk: macro-regulatory-sportfi.md | sportmind_ft_mcp.py registry

FIVE NON-NEGOTIABLE RULES:
  Never treat web output as ground truth without source tier check
  Never auto-update library — human approves all changes
  Never apply burn modifier before T+15 post-match
  Always have fallback for unavailable sources
  Always log fetch URL + timestamp + extracted content
```
REF: platform/web-agent-connectors.md · scripts/sportmind_wa_mcp.py

---

## [COMPRESSED] Broadcast and commercial intelligence (Prompt 23)

```
PURPOSE: Commercial context, not match outcome. BVS, CQS, rights tier, audience reach.
TOOLS: bc_broadcast_value, bc_rights_tier, bc_audience_reach, bc_context_quality, bc_dts_effect
KEY FILES: market/broadcaster-media-intelligence.md · core/contextual-signal-environment.md

BVS (Broadcast Value Signal): commercial value to broadcasters/rights holders
CQS: 0.60–1.40 — modifies FTIS, CDI, HAS; NEVER modifies SMS
RIGHTS TIERS: UCL/WC Final=Tier 1 (global) → domestic mid-table=Tier 4
DTS EFFECT: documentary/streaming content amplifies commercial signals (Drive to Survive model)

CRITICAL: CQS = commercial magnitude. SMS = outcome probability. Keep strictly separate.
OUTPUT: BVS score, CQS score, audience reach tier, rights tier, fan token arc, plain English.
```
REF: agent-prompts/agent-prompts.md (Prompt 23) · scripts/sportmind_bc_mcp.py

---

## [COMPRESSED] Web agent live data pattern (Pattern 13)

```
PURPOSE: Autonomous real-time grounding — lineup, supply, regulatory. No manual step.

USE CASE A — LINEUP CONFIRMATION:
  1. sportmind_pre_match() → expected squad framework
  2. wa_lineup_target(sport, home_team, kickoff) → Tier 1 fetch URL + extraction spec
  3. fetch(URL at T-2h) → extract starting XI
  4. Compare vs expected → ABSENCE_CONFIRMED or LINEUP_CONFIRMED
  5. If ATM-tier absent: FTIS dampener −5pts, re-run ARI with availability=0.00

USE CASE B — PATH_2 SUPPLY VERIFICATION:
  1. ft_token_state(token) → confirm PATH_2, get contract_address
  2. wa_supply_verify(token, result, hours_since) → Chiliscan endpoints
  3. fetch(chiliscan endpoint at T+30min minimum, T+6h definitive)
  4. delta = pre_supply − post_supply; burn_pct ≈ 0.0024 (±0.0005) = BURN_CONFIRMED
  5. LOSS: supply_delta should be 0; if not → SUPPLY_ANOMALY (escalate)

USE CASE C — REGULATORY MONITORING:
  1. wa_macro_monitor(tier=1) → ESMA/SEC/CFTC/Chiliz targets
  2. fetch each URL on schedule (Chiliz daily; ESMA weekly)
  3. Classify: core/external-intelligence-intake.md framework
  4. Human review required → NO AUTO-UPDATES to library

NEVER: apply burn modifier before T+15 | auto-update library | use Tier 3 sources
MCP STACK: sportmind + sportmind-ft + sportmind-web-agent + fetch
```
REF: examples/agentic-workflows/web-agent-live-data.md · platform/web-agent-connectors.md

---

## [COMPRESSED] Narrative momentum intelligence

```
LOAD ORDER: After all quantitative modifiers (athlete, congestion, officiating, weather, macro)
MAXIMUM MODIFIER: ±8% — never exceed regardless of narrative intensity
RULE: Never override strong adverse signals with narrative alone

EIGHT TAXONOMY CATEGORIES:
Cat 1 REVENGE: Significant prior loss rematch | Home+4–6% | Away+3–5% | Valid ≤18 months
Cat 2 RECORD PROXIMITY: 1 away=+6–8% | 2–3 away=+4–6% | 4–5 away=+2–3%
Cat 3 COMEBACK: Major adversity return | +3–5% | Injury return: apply injury modifier FIRST then +2%
Cat 4 CAREER FIRST: Home debut, first trophy match, first cap | +3–5% home amplification
Cat 5 RIVALRY: Tier 1 (El Clásico, India-Pakistan): 40% discount on form differential
              Tier 2 (domestic derbies): 20% discount on form differential
Cat 6 MEMORIAL: Apply ZERO modifier; WIDEN confidence intervals by 15% — abstention signal
Cat 7 MUST-WIN: Elimination=+5% | Relegation=+4% | Career final=+3% (at-risk team only)
Cat 8 FATIGUE: Narrative 4+ weeks old → reduce 50% | Athlete addressing pressure → reduce to 0

TOURNAMENT KNOCKOUT AMPLIFIERS (applied to narrative modifier, not base signal):
  R16=×1.20 | QF=×1.45 | SF=×1.70 | Final=×2.00
  Defending champion: +5% all tournament matches
  First-time finalist: +4% breakthrough narrative
  Compound rule: Cat7 + knockout = Cat7 full + knockout at 70%

CHAMPIONSHIP DECIDER: Title race final 5 matches=×1.15 | Final 3=×1.30 | Last match=×1.50
  Season finale dead rubber: SUPPRESS narrative; apply DEAD_RUBBER flag instead

CROSS-SPORT DOMINANCE (World Cup active): Non-football AELS × 0.85 during WC group stage
  Social volume dominated by football; non-football signal compressed 15–25%

TRILOGY FIGHTS (MMA/boxing): × 1.50 narrative — maximum combat sports signal
  Controversial rematch: × 1.30 | Long gap (2y+): × 1.10

DTS EFFECT (documentary/streaming):
  DTS = commercial signal only (AELS, CDI) — NEVER modifies SMS
  Active DTS: × 1.15 AELS | Apply CAUTION flag on social volume (may be noise)

POST-TOURNAMENT: Phase 1 (days 1–7) = do NOT act on residual narrative
  Phase 2 (days 8–21) = apply 50% modifier | Phase 3 (day 22+) = reset fresh

FAN TOKEN: Narrative-rich WIN = larger token spike | Must-win LOSS = severe compound signal
  Record-breaking moment = fastest token signal in the library
```
REF: core/core-narrative-momentum.md


