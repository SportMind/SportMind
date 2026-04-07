# SportMind Glossary

Central reference for sport-specific terminology used across the library.
Agents loading a sport skill for the first time should reference this file
to resolve any unfamiliar terminology.

Organised alphabetically within sport categories, then cross-sport terms.

---

## Cross-sport terms

| Term | Definition | Used in |
|---|---|---|
| **Adjusted signal score** | Base signal × composite modifier — the final output after all SportMind modifiers applied | `core/core-athlete-modifier-system.md` |
| **Bifurcated impact model** | The principle that macro events affect physical sports revenue and digital revenue differently — often in opposite directions | `macro/macro-overview.md` |
| **CHZ** | Chiliz — the blockchain token that powers the Socios fan token ecosystem; all fan tokens are priced relative to CHZ | `fan-token/fan-token-pulse/` |
| **Composite modifier** | Product of all individual modifiers (availability × form × fatigue × weather × officiating × narrative × macro) | `core/core-athlete-modifier-system.md` |
| **Counter-cyclical** | An asset that increases in value when the broader market declines — fan tokens showed counter-cyclical behaviour during the 2020 pandemic | `macro/macro-pandemic-public-health.md` |
| **Event playbook** | A pre-built decision framework for a recurring event type (e.g., Champions League final, fight week, Grand Tour Stage 1) | Each sport domain skill |
| **Fan token readiness tier** | Classification (1–4) of a sport's commercial readiness for fan tokens: 1=active, 2=near-term, 3=longer horizon, 4=niche | `market/market-overview.md` |
| **Non-contractual token** | A fan token that continues to exist on-chain after its official club/platform partnership has ended | `fan-token/fan-token-lifecycle/` |
| **Partnership Health Score (PHS)** | Five-indicator composite measuring the vitality of an active fan token partnership | `fan-token/fan-token-partnership-intelligence/` |
| **Signal weight** | The recommended proportion of overall signal score attributed to each component (social, sports catalyst, whale/market, price trend, macro) | `core/core-signal-weights-by-sport.md` |
| **Tier 1 sport** | Sport with an active fan token ecosystem on Chiliz/Socios — football, basketball, MMA, esports, F1, cricket (PSL) | `market/market-overview.md` |

---

## Football / Soccer

| Term | Definition |
|---|---|
| **xG (Expected Goals)** | Statistical measure of shot quality — the probability a given shot results in a goal based on location, shot type, and build-up. xG > goals = team due a positive correction; xG < goals = team likely to regress |
| **xA (Expected Assists)** | Probability that a given pass/cross results in an assist; measures chance creation quality beyond raw assist count |
| **Progressive carries** | Ball carries moving the ball at least 10m toward the opponent's goal; measure of a player's advancing contribution |
| **Pressures** | Number of times a player attempts to pressure an opponent in possession; measures pressing intensity |
| **PPDA (Passes Per Defensive Action)** | Measure of pressing intensity at team level — lower number = more aggressive press |
| **Competition tier** | Hierarchy of importance: UCL/WC = Tier 1; domestic league = Tier 2; domestic cup = Tier 3; friendly = Tier 4 |
| **Derby modifier** | Additional signal weight applied to local rivalry matches where form differential predicts less than usual |
| **NCSI (National-Club Spillover Index)** | Measure of how national team performances spill over into club fan token prices | `fan-token/football-token-intelligence/` |
| **ATM (Athlete Token Multiplier)** | Individual athlete's contribution to club-level token price movement | `fan-token/football-token-intelligence/` |
| **FTIS (Fan Token Impact Score)** | Competition-level token price impact signal | sport-specific bridge skills |

---

## Basketball (NBA)

| Term | Definition |
|---|---|
| **Load management** | Deliberate resting of star players (usually on back-to-back games) to preserve them for playoffs; creates immediate availability modifier |
| **On/off splits** | Team performance when a specific player is on vs off the court; measures individual impact on team outcome |
| **Clutch performance** | Performance in close games (within 5 points) in the final 5 minutes; distinct from overall performance |
| **TS% (True Shooting %)** | Shooting efficiency accounting for 2-point, 3-point, and free throws; most accurate shooting efficiency measure |
| **RPM (Real Plus-Minus)** | ESPN's estimate of a player's per-100-possession impact on team margin; contextualises counting stats |
| **VORP (Value Over Replacement Player)** | Player value above replacement level; useful for injury impact assessment |
| **Back-to-back (B2B)** | Two games on consecutive days; second game shows documented performance decline (~−3 points per 100 possessions) |

---

## American Football (NFL)

| Term | Definition |
|---|---|
| **CPOE (Completion % Over Expected)** | QB completion rate vs statistical expectation given difficulty of throws; best single QB efficiency metric |
| **EPA (Expected Points Added)** | Points value added on each play; measures play-level contribution to game outcome |
| **Injury designation system** | Wednesday/Thursday/Friday practice reports: LP (Limited Participation), FP (Full Participation), DNP (Did Not Practice). Friday designation most predictive for Sunday availability |
| **O-line** | Offensive line — the five players protecting the QB; their health is the most underpriced NFL signal in prediction markets |
| **QB tier system** | Hierarchy of QB importance: Franchise QB (loss = Tier A modifier), Solid Starter, Game Manager, Backup |
| **Snap count** | Number of plays a player participated in; declining snap count = injury signal or role change |
| **ATS (Against The Spread)** | Performance relative to the point spread; the primary prediction market metric in NFL |

---

## Cricket

| Term | Definition |
|---|---|
| **DLS (Duckworth-Lewis-Stern)** | Mathematical method for recalculating targets in rain-reduced limited-overs games; generally favours chasing teams |
| **Dew factor** | Moisture settling on outfield in evening/night matches (especially in tropical climates); dramatically reduces swing and spin, benefiting batting second |
| **Pitch report** | Pre-match assessment of pitch conditions: Green (bowler-friendly), Dry (spinner-friendly), Flat (batting), Two-paced (inconsistent bounce) |
| **WBGT (Wet Bulb Globe Temperature)** | Heat stress index; above 35°C triggers event modifications or cancellations |
| **Test cricket** | 5-day format; most prestigious; not covered by DLS (over-per-side targets don't apply) |
| **T20** | Twenty-over format; fastest format; most DLS exposure; most dew factor exposure |
| **ODI** | 50-over format; medium length; both DLS and dew factor relevant |
| **H2H (Head-to-Head)** | Batter vs bowler historical matchup data; significant predictive variable at player level |
| **DRS (Decision Review System)** | Technology-based review of on-field umpiring decisions; impacts LBW and caught-behind calls |
| **Powerplay** | Fielding restriction overs (1–6 in T20; 1–10 in ODI) where batting is typically easier |

---

## Horse Racing

| Term | Definition |
|---|---|
| **Going** | Ground conditions at a racecourse. Scale (UK): Firm → Good to Firm → Good → Good to Soft → Soft → Heavy. Primary horse-level modifier |
| **Going preference** | A horse's documented preferred going conditions; horses perform significantly better on preferred going |
| **C&D record (Course and Distance)** | A horse's historical performance at this specific course at this specific distance; strongest single form indicator |
| **Draw bias** | Statistical tendency for horses in specific starting positions (stalls 1–X on a particular track) to outperform; varies by course and going |
| **Trainer/jockey combination** | Strike rate of a specific trainer–jockey pairing; consistently profitable partnerships are documented signals |
| **Handicap mark** | Official rating assigned to horses to equalise competition; horses rated below their true ability = value plays |
| **Morning line** | Early odds offered; movement from morning line to race time indicates professional money signals |
| **Form figures** | Code summarising recent race results: 1=win, 2=second, etc. P=pulled up, F=fell, U=unseated |
| **EIPH (Exercise-Induced Pulmonary Haemorrhage)** | Bleeding in lungs after hard exercise; horses with EIPH history are higher risk |
| **Paddock assessment** | Visual inspection of horse before race; coat condition, behaviour, muscle tone are signal inputs |

---

## MMA / Combat Sports

| Term | Definition |
|---|---|
| **10-point must system** | Standard MMA and boxing scoring: winner of round scores 10, loser scores 9 (or 8 for dominant round) |
| **Significant strikes** | Strikes counted by statistical systems (UFC Stats, FightMatrix); subset of total strikes |
| **Takedown accuracy/defence %** | Percentage of takedown attempts that succeed (offense) or are stopped (defence) |
| **Submission rate** | Frequency of fights ending by submission; measures grappling finish tendency |
| **Weight cut** | Process of reducing weight to make competition limit; extreme cuts correlate with performance decline post-weigh-in |
| **Rehydration** | Recovery of weight after weigh-in; fighters who rehydrate well perform better; fighters who struggle to rehydrate = performance risk |
| **Fight camp** | Training preparation period for an upcoming fight; typical duration 8–12 weeks |
| **Late replacement** | Fighter taking a bout on short notice (< 4 weeks); documented performance decline, especially for grapplers |
| **CRI (Career Risk Index)** | SportMind metric measuring fighter career longevity and token permanence risk | `fan-token/mma-token-intelligence/` |
| **FighterTIS** | Fan Token Impact Score for individual MMA fighters | `fan-token/mma-token-intelligence/` |

---

## Golf

| Term | Definition |
|---|---|
| **Strokes Gained (SG)** | Family of metrics measuring performance vs field average in specific areas: SG:OTT (off the tee), SG:APR (approach), SG:ARG (around the green), SG:PUTT |
| **Cut line** | Score below which players are eliminated after 36 holes; making/missing the cut is the primary event playbook trigger in golf |
| **Major** | One of four highest-prestige tournaments: The Masters, US Open, The Open Championship, PGA Championship. Tier 1 signal events |
| **Strokes gained: total (SGT)** | Composite of all SG metrics; best single-number player quality measure |
| **Course history** | Player's historical scoring at this specific course; documented to be more predictive than recent form alone |
| **Course fit** | How a player's strengths match a course's demands (e.g., long hitter at Augusta vs iron player at Open links) |
| **Bogey-free round** | Completing a round without a score above par on any hole; indicates mental consistency |
| **World Golf Ranking (OWGR)** | Official world ranking; used for event entry; not directly correlated with form |

---

## Esports

| Term | Definition |
|---|---|
| **Meta** | The dominant strategies and character/weapon choices at a given point in a game's competitive evolution |
| **Patch** | Game update that modifies character abilities, weapon statistics, or map configurations; major patches shift meta |
| **HLTV Rating** | Counter-Strike player performance metric (0–2.0 scale; >1.00 = above average); most widely used CS2 player statistic |
| **Ban/pick phase** | Pre-match selection process where teams choose maps/characters and ban opponents' choices; high skill-expression moment |
| **Roster stability** | How long a team's core lineup has remained unchanged; longer stability = better team cohesion |
| **OrgTIS** | Organisation-level token impact score | `fan-token/esports-token-intelligence/` |
| **GRM (Game Roster Multiplier)** | Multi-game roster depth's impact on organisation token value | `fan-token/esports-token-intelligence/` |
| **PRS (Patch Risk Score)** | Risk that an upcoming patch disrupts a team's competitive approach | `fan-token/esports-token-intelligence/` |
| **RSI (Roster Stability Index)** | Turnover risk and its effect on org token continuity | `fan-token/esports-token-intelligence/` |
| **CS2 Major** | Valve-organised CS2 tournament; highest prestige in CS2; 2× per year |
| **LoL Worlds** | Annual League of Legends World Championship; highest single-tournament viewership in esports |
| **TI (The International)** | Annual Dota2 World Championship; historically highest single prize pool in esports |

---

## Formula 1 / MotoGP

| Term | Definition |
|---|---|
| **Qualifying** | One-lap time trial determining grid starting positions; heavily influences race outcome |
| **Undercut / Overcut** | Pit stop strategy: Undercut = pit earlier than rival to jump them on faster tyres; Overcut = stay out longer then pit for track position |
| **DRS (Drag Reduction System)** | F1 adjustable rear wing that reduces drag on straight; activated within 1 second of car ahead; increases overtaking |
| **Safety car / VSC** | Safety Car (full pace car): Bunches field; creates strategic opportunity. Virtual Safety Car (VSC): Speed limit; smaller bunching effect |
| **Constructor standings** | F1 points accumulated by both drivers for the same constructor; determines constructor championship |
| **Regulation cycle** | Periods between major technical regulation changes; team competitiveness changes dramatically with new regulations |
| **Hardware tier (MotoGP)** | Factory bikes (Honda, Yamaha, Ducati, Aprilia, KTM) vs Satellite bikes (less developed machinery); major performance gap |
| **Wet race specialist** | Rider/driver who significantly outperforms their normal pace in wet conditions; identified and trackable |
| **CTI (Constructor Token Index)** | Constructor-level F1 token commercial health metric | `fan-token/formula1-token-intelligence/` |
| **DTM (Driver Token Multiplier)** | Individual driver contribution to constructor token movement | `fan-token/formula1-token-intelligence/` |

---

## Baseball (MLB)

| Term | Definition |
|---|---|
| **Statcast** | MLB's proprietary tracking system measuring exit velocity, launch angle, spin rate, sprint speed, and other physical metrics |
| **Exit velocity** | Speed of ball off the bat; high exit velocity correlates with hard contact and positive offensive outcomes |
| **Launch angle** | Vertical angle of ball off bat; optimal 10–30° for extra-base hits |
| **xBA (Expected Batting Average)** | Batting average expected based on quality of contact; useful for regression analysis |
| **WAR (Wins Above Replacement)** | Comprehensive player value metric combining all contributions; standard cross-position comparison tool |
| **PQS (Pitcher Quality Score)** | SportMind composite metric for starting pitcher quality | `athlete/baseball/` |
| **BQS (Batter Quality Score)** | SportMind composite metric for batter performance | `athlete/baseball/` |
| **Platoon splits** | Performance differential vs left-handed vs right-handed pitchers/batters; significant modifier for matchup analysis |
| **Rotation cycle** | Starting pitcher turn in the rotation (every 5th game); determines who pitches in each game |
| **Bullpen** | Relief pitchers; bullpen health and usage patterns affect late-game performance predictions |
| **Park factor** | Statistical adjustment for how a specific ballpark affects run scoring (Coors Field in Colorado is the most extreme park factor in baseball) |

---

## Ice Hockey (NHL)

| Term | Definition |
|---|---|
| **GSAx (Goals Saved Above Expected)** | Goaltender performance metric; positive = goals saved above statistical expectation. Most important single-player metric in hockey |
| **Corsi / CF%** | Shot attempt differential metric; proxy for possession and pressure |
| **Fenwick** | Like Corsi but excludes blocked shots; considered slightly more predictive |
| **Expected Goals (xG) — hockey** | Similar to football xG; estimates shot quality to predict goals more accurately than raw shot count |
| **Special teams: PP% / PK%** | Power Play % (team scoring on power play) and Penalty Kill % (stopping opponent on power play); significant match outcome predictor |
| **Back-to-back** | NHL two games on consecutive days; goaltender change very likely; one of the most reliable lineup change signals in any sport |
| **Line matching** | Tactical deployment of specific forward lines against specific opponent lines; key to understanding ice time allocation |
| **GSAx** | See above — the defining stat for goaltender assessment and the single most important variable in NHL prediction |

---

## Rugby (Union and League)

| Term | Definition |
|---|---|
| **Set piece** | Scrums and lineouts — structured restarts; dominant set piece teams win a disproportionate number of close matches |
| **Kicker zone accuracy** | Accuracy of goal kicking by zone (the pitch is divided into areas; some zones are higher-probability than others) |
| **Gainline** | Notional line at the point of breakdown; teams that win the gainline consistently win matches |
| **Half-back partnership** | Scrum-half + fly-half relationship; strongest predictor of attacking continuity |
| **State of Origin (NRL)** | Annual representative series between NSW Blues and QLD Maroons; highest-intensity series in rugby league |
| **PAS (Player Availability Score)** | SportMind metric for rugby league player availability and fitness | `athlete/rugby-league/` |
| **PIS (Positional Impact Score)** | SportMind metric for positional criticality in rugby league | `athlete/rugby-league/` |
| **Ruck speed** | How quickly the ball is presented from a tackle situation; faster ruck = better attacking momentum |

---

## Snooker / Darts

| Term | Definition |
|---|---|
| **147 maximum break** | A snooker player potting all 36 balls (15 reds with blacks, then all colours) for the maximum score of 147; rarest and most celebrated individual achievement |
| **The Crucible effect** | Documented tendency for certain snooker players to significantly outperform their general form specifically at the World Championship venue (Sheffield Crucible) |
| **Triple Crown** | The three most prestigious snooker events: UK Championship, Masters, World Championship |
| **9-dart finish** | A darts player winning a leg in the minimum possible 9 darts; equivalent to a cricket century or hole-in-one in terms of rarity and fan engagement |
| **3-dart average** | Primary darts player performance metric; average score per 3-dart visit to the board; 100+ = competitive professional level |
| **Checkout %** | Percentage of times a player successfully finishes (checks out) when at a winnable score; measures composure under pressure |

---

## Cycling

| Term | Definition |
|---|---|
| **GC (General Classification)** | Overall time standings in a stage race; GC leaders race differently from stage hunters |
| **Grand Tour** | Three-week stage races: Tour de France, Giro d'Italia, Vuelta a España. Highest prestige in road cycling |
| **DNF (Did Not Finish)** | Rider abandons a race; common in Grand Tours due to crash, illness, or team tactics |
| **Domestique** | Rider who sacrifices their own result to support a team leader; different fatigue profile from GC riders |
| **Peloton** | Main group of riders; leaving the peloton is referred to as a "breakaway" |
| **Classics** | One-day races (Paris-Roubaix, Flanders, etc.); completely different skill set from stage racers |
| **VAM (Velocità Ascensionale Media)** | Vertical metres climbed per hour; used to compare climbing performances across different ascents |
| **Strava segment** | Training data publically visible on Strava; professional riders' segments provide training load signals |

---

## Athletics

| Term | Definition |
|---|---|
| **Wind legal** | For sprints and horizontal jumps, a result is wind-legal (record-eligible) only if tailwind is ≤ +2.0 m/s |
| **Diamond League** | Annual international athletics circuit; highest-prestige meets outside Championships |
| **World Athletics Record** | World record; must be set in a legal condition (no altitude assistance, legal wind, drug-tested) |
| **Personal Best (PB)** | An athlete's best career performance in an event |
| **Season Best (SB)** | An athlete's best performance in the current season |
| **Combined events** | Decathlon (men) / Heptathlon (women); multi-discipline events over two days |
| **WBGT (Wet Bulb Globe Temperature)** | Heat stress index used by World Athletics to modify or cancel events above threshold |

---

## SportMind metrics — complete reference

| Metric | Full name | Skill | What it measures |
|---|---|---|---|
| HAS | Holder Activity Score | fan-token-pulse | On-chain holder engagement velocity |
| TVI | Token Velocity Index | fan-token-pulse | Token movement speed and liquidity health |
| PI | Performance Index | performance-on-pitch | Position-weighted on-pitch performance |
| DTS | Development Trajectory Score | performance-off-pitch | Athlete development curve |
| TAI | Training Adaptation Index | performance-off-pitch | Response to training load |
| PS | Professionalism Score | performance-off-pitch | Off-pitch conduct |
| AELS | Athlete Engagement Lift Score | athlete-social-lift | Social→token correlation |
| SHS | Social Health Score | athlete-social-activity | Social channel quality |
| AGI | Audience Growth Index | athlete-social-activity | Follower/engagement growth rate |
| TVS | Transfer Viability Score | transfer-intelligence | Transfer probability and value |
| DLVS | Domestic Loan Value Score | transfer-intelligence | Loan spell value assessment |
| APS | Athlete Portability Score | transfer-signal | Token value transfer to new club |
| TSI | Transfer Signal Index | transfer-signal | Rumour confidence aggregation |
| ABS | Athlete Brand Score | brand-score | Composite commercial brand value |
| AFS | Audience Fit Score | sponsorship-match | Brand-to-athlete audience alignment |
| FTIS | Fan Token Impact Score | sport bridge skills | Competition-level token impact |
| NCSI | National-Club Spillover Index | football-token-intel | National team → club token effect |
| ATM | Athlete Token Multiplier | football-token-intel | Individual athlete → club token effect |
| CTI | Constructor Token Index | formula1-token-intel | Constructor commercial health |
| DTM | Driver Token Multiplier | formula1-token-intel | Driver → constructor token effect |
| FTM | Fighter Token Multiplier | mma-token-intel | Fighter impact on MMA token pricing |
| CRI | Career Risk Index | mma-token-intel | Fighter career longevity risk |
| OrgTIS | Organisation Token Impact Score | esports-token-intel | Org-level tournament token impact |
| GRM | Game Roster Multiplier | esports-token-intel | Multi-game roster depth impact |
| PRS | Patch Risk Score | esports-token-intel | Game patch competitive disruption risk |
| RSI | Roster Stability Index | esports-token-intel | Roster turnover token continuity risk |
| PQS | Pitcher Quality Score | athlete/baseball | Starting pitcher quality composite |
| BQS | Batter Quality Score | athlete/baseball | Batter performance composite |
| PAS | Player Availability Score | athlete/rugby-league | Availability and fitness composite |
| PIS | Positional Impact Score | athlete/rugby-league | Positional criticality modifier |
| PHS | Partnership Health Score | fan-token-partnership-intel | Partnership health and termination risk |
| LTUI | Lifetime Token Utility Index | fan-token-lifecycle | Cumulative utility event quality |
| VSI | Validator Status Indicator | blockchain-validator-intelligence | Sixth PHS component; validator node health and stake stability for validator clubs |
| NBATIS | NBA Token Impact Score | basketball-token-intelligence | Composite NBA signal: game importance, star player status, playoff position, market sentiment |
| CricTIS | Cricket Token Impact Score | cricket-token-intelligence | Composite cricket signal: format weight, match importance, India factor, token ecosystem status |
| GSAx | Goals Saved Above Expected | (NHL domain) | Goaltender performance vs expectation |

---

---

## DeFi terms (as applied to sports assets)

| Term | Definition |
|---|---|
| **AMM** | Automated Market Maker — DEX pricing algorithm using pool reserve ratios (x × y = k) |
| **TVL** | Total Value Locked — dollar value of assets in a liquidity pool; SportMind liquidity threshold: $500k (warning), $100k (critical) |
| **LP** | Liquidity Provider — wallet depositing assets into a pool to earn trading fees |
| **LP token** | Receipt token representing a share of a liquidity pool position |
| **Impermanent loss** | Value loss for LP providers when token price diverges significantly from entry price |
| **Slippage** | Price impact of a trade; estimated as (trade size) / (TVL/2) × 100% |
| **DEX** | Decentralised Exchange — exchange running via smart contracts (Uniswap, Chiliz DEX) |
| **CEX** | Centralised Exchange — exchange with central operator (Binance, Bybit) |
| **Sandwich attack** | MEV strategy where attacker front-runs and back-runs a detected pending DEX trade |
| **MEV** | Maximal Extractable Value — profit extracted by reordering blockchain transactions |
| **Prediction market** | Protocol where participants bet on outcomes settled by on-chain oracles |
| **Oracle** | Service bringing real-world data (match results, prices) on-chain for smart contracts |
| **Azuro** | Sports prediction market infrastructure protocol; Chiliz-adjacent; enables sports dApps |
| **Polymarket** | General prediction market platform with significant sports coverage |
| **DeFi yield** | Passive income earned from DeFi activities: LP fees, staking rewards, prediction market provision |
| **APR/APY** | Annual Percentage Rate / Annual Percentage Yield — annualised yield from DeFi positions |
| **CEX/DEX divergence** | When a token's price differs significantly across exchanges; signals lifecycle phase transition |
| **liquidity_warning** | SportMind flag: pool TVL < $500k; apply max 40% position size |
| **liquidity_critical** | SportMind flag: pool TVL < $100k or slippage > 3%; apply max 20% or ABSTAIN |

*See `fan-token/defi-liquidity-intelligence/` for full DeFi framework.*


*This glossary covers terms used across the SportMind library as of v2.2.0.
For sport-specific detail, see the relevant sport domain skill.*


---

## Web3 and DeFi sports terminology

Terms used in the fan token, on-chain, and Web3 sports intelligence layers.
Agents loading `fan-token/` skills should reference this section.

| Term | Definition | Used in |
|---|---|---|
| **AMM (Automated Market Maker)** | Smart contract that sets token prices algorithmically using a liquidity pool rather than an order book. KAYEN on Chiliz Chain is an AMM. Price moves as the pool ratio changes from buys and sells. | `fan-token/defi-liquidity-intelligence/` |
| **APS (Athlete Portability Score)** | Measures how much of an athlete's commercial value transfers to a new club. 0.00-1.00 scale. APS 0.85 = 85% of commercial value is club-independent. | `fan-token/transfer-signal/` |
| **ATM (Athlete Token Multiplier)** | How much a specific athlete's performance amplifies or depresses their club's fan token commercial signals. ATM 0.90 = elite commercial driver. | `fan-token/transfer-signal/` |
| **BVS (Broadcast Value Signal)** | Measures a competition's commercial value to broadcasters. Composite of audience reach, engagement depth, rights scarcity, and commercial premium. | `market/broadcaster-media-intelligence.md` |
| **CDI (Commercial Duration Index)** | Days of commercially valuable fan engagement an outcome generates above baseline. CDI 45 = 45 days of elevated engagement. | `fan-token/fan-sentiment-intelligence/` |
| **CHI (Club Health Index)** | Composite index measuring a club's institutional health: financial stability, academy pipeline, community engagement, ownership quality, infrastructure. | `market/club-operations-intelligence.md` |
| **CHZ (Chiliz)** | The native token of the Chiliz blockchain. Fan tokens are priced and traded in CHZ (and sometimes USDC) on the Socios platform and KAYEN exchange. | `macro/macro-crypto-market-cycles.md` |
| **Conviction voting** | Governance mechanism where votes accumulate weight over time. Holding your vote longer = stronger vote. Rewards long-term holders; reduces governance mercenaries. | `fan-token/sports-governance-intelligence/` |
| **DeFi (Decentralised Finance)** | Financial services built on blockchain smart contracts without traditional intermediaries. Fan token liquidity pools are DeFi infrastructure. | `fan-token/defi-liquidity-intelligence/` |
| **DTM (Driver Token Multiplier)** | F1-specific. Measures how a driver's individual performance amplifies or depresses their constructor's token signal. Qualifier: DTM always requires constructor context. | `athlete/formula1/athlete-intel-formula1.md` |
| **Farming (yield farming)** | Providing liquidity to a DeFi pool and earning fee revenue in return. Fan token LPs earn fees on every trade. TVL growth often driven by farming incentives. | `fan-token/defi-liquidity-intelligence/` |
| **Flash loan** | A DeFi loan that must be borrowed and repaid within the same transaction. Used in arbitrage. Relevant for monitoring large on-chain price movements that may be artificial. | `fan-token/on-chain-event-intelligence/` |
| **FTIS (Fan Token Interest Score)** | Composite score measuring how much interest a fan token is generating: social mentions + search volume + on-chain activity + price momentum. | `fan-token/fan-token-pulse/` |
| **Gas** | Transaction fees paid on a blockchain to execute smart contracts. High gas on Ethereum encourages using Chiliz Chain (lower fees) for fan token operations. | `fan-token/blockchain-validator-intelligence/` |
| **GSAx (Goals Saved Above Expected)** | NHL goaltender metric. Measures goals prevented beyond what an average goaltender would save against the same shot quality. Primary individual signal in ice hockey analysis. | `athlete/nhl/athlete-intel-nhl.md` |
| **GSI (Governance Signal Index)** | Composite index measuring fan token governance quality: participation rate, decision weight, transparency, execution track record. | `fan-token/sports-governance-intelligence/` |
| **HAS (Holder Activity Score)** | Measures active engagement of fan token holders: trading volume, governance participation, staking, social activity. 0-100 scale. HAS > 70 = active community. | `fan-token/fan-token-pulse/` |
| **KAYEN** | Decentralised exchange (DEX) on Chiliz Chain. Primary trading venue for fan tokens. Provides TVL, price, and liquidity data for SportMind's DeFi layer. | `fan-token/defi-liquidity-intelligence/` |
| **Liquidity mining** | Incentive programme where protocols reward LPs with extra tokens for providing liquidity. Can temporarily inflate TVL metrics — flag if mining rewards are present. | `fan-token/defi-liquidity-intelligence/` |
| **LP (Liquidity Provider)** | Entity that deposits tokens into a liquidity pool to enable trading. LPs earn trading fees proportional to their pool share. Pre-match LP additions are smart money signals. | `fan-token/on-chain-event-intelligence/` |
| **LTUI (Lifetime Token Utility Index)** | Measures the accumulated lifetime commercial utility a fan token delivers to holders. Affected by every governance event, sporting outcome, and partnership. | `fan-token/fan-token-lifecycle/` |
| **MiCA (Markets in Crypto-Assets)** | EU regulatory framework for crypto assets including fan tokens. Applies to all 27 EU member states. Fan tokens may be classified as financial instruments under MiCA if they confer economic rights. | `fan-token/fan-token-lifecycle/` |
| **NCSI (National-Club Spillover Index)** | Measures how much a national team's international performance affects a player's club fan token. NCSI = competition_weight × ATM × macro_modifier. | `market/international-football-cycle.md` |
| **On-chain** | Data or activity recorded directly on a blockchain. On-chain signals (wallet movements, LP activity, governance votes) are transparent and tamper-resistant. | `fan-token/on-chain-event-intelligence/` |
| **Quadratic voting** | Governance mechanism where vote cost is proportional to the square of votes cast (e.g., 4 votes cost 16 tokens, not 4). Reduces whale dominance vs simple one-token-one-vote. | `fan-token/sports-governance-intelligence/` |
| **RWA (Real World Asset)** | A physical or traditional financial asset tokenised on a blockchain. In sports: tokenised stadium revenue, broadcast rights, merchandise income. Phase 5 of the fan token lifecycle. | `fan-token/rwa-sportfi-intelligence/` |
| **Slippage** | The difference between the expected and actual trade price due to pool imbalance. High slippage = low liquidity = liquidity_warning flag in SportMind. | `fan-token/defi-liquidity-intelligence/` |
| **Smart contract** | Self-executing code on a blockchain that runs automatically when conditions are met. Fan token governance votes and staking are implemented as smart contracts. | `fan-token/sports-governance-intelligence/` |
| **Socios** | Platform built on Chiliz Chain for fan tokens. Manages the relationship between clubs and their token holders. Primary fan token marketplace for major European clubs. | `fan-token/fan-token-lifecycle/` |
| **Staking** | Locking tokens in a smart contract to earn rewards or access privileges. Higher staking ratio = fewer tokens available to trade = lower sell pressure signal. | `fan-token/on-chain-event-intelligence/` |
| **Token-gating** | Using token ownership as a requirement to access content, events, or experiences. SportFi Kit's primary mechanism; SportMind provides the signal; the gate determines eligibility. | `examples/applications/app-07-sportfi-kit-integration.md` |
| **TVL (Total Value Locked)** | Total value of tokens deposited in a DeFi protocol or liquidity pool. In SportMind: TVL is the primary liquidity tier classifier (DEEP > $5M, MODERATE $500K-$5M, THIN < $500K). | `fan-token/defi-liquidity-intelligence/` |
| **VDA (Virtual Digital Asset)** | Indian regulatory classification for cryptocurrencies and digital assets including fan tokens. VDA framework clarity in India would unlock the world's largest untapped fan token market. | `market/international-cricket-cycle.md` |
| **Wallet age** | Average age of token-holding wallets, measured in days since first holding. Rising wallet age = long-term holders not selling = conviction signal. | `fan-token/on-chain-event-intelligence/` |
| **Wash trading** | Artificial trading activity where the same entity buys and sells to itself to inflate volume metrics. Cross-reference on-chain volume with exchange volume to detect. | `fan-token/on-chain-event-intelligence/` |
| **Whale** | Wallet holding ≥ 0.5% of circulating token supply. Whale movements are Category 1 on-chain signals. Whale accumulation before a match = smart money signal. | `fan-token/on-chain-event-intelligence/` |


*MIT License · SportMind · sportmind.dev*
