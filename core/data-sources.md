# Data Sources — SportMind Reference

Centralised reference mapping every SportMind skill layer to its recommended
live data sources. Use this file to:
- Verify claims made in SportMind skill files
- Build data pipelines for agents requiring current data
- Understand where the intelligence in each skill originates
- Update signal inputs when SportMind files age

**Data currency note:** SportMind skill files contain intelligence current as of
their version date. Live data from the sources below always supersedes static
file content for current analysis.

---

## Layer 1 — Sport domain data sources

### Football / Soccer
```
Competition results and statistics:
  FBref (fbref.com) — deep Stathead stats, xG, progressive actions, all leagues
  WhoScored (whoscored.com) — match ratings, player stats, team stats
  Understat (understat.com) — xG models for top European leagues
  
Fixture and scheduling:
  BBC Sport fixtures (bbc.co.uk/sport/football)
  Sky Sports fixtures (skysports.com/football/fixtures)
  
Transfer intelligence:
  Transfermarkt (transfermarkt.com) — valuations, transfer history, contracts
  Fabrizio Romano (@FabrizioRomano) — primary transfer journalist, Twitter/X
  The Athletic (theathletic.com) — verified transfer reporting
  
Referee statistics:
  WhoScored referee section (whoscored.com/Referees)
  FootyStats referee stats (footystats.org/referees)
  TransferMarkt referee profiles (transfermarkt.com)
  
Odds and market data:
  Oddsportal (oddsportal.com) — historical odds across bookmakers
  Betfair Exchange (betfair.com) — live market prices
  Pinnacle (pinnacle.com) — sharp market reference
```

### American Football (NFL)
```
Official data:
  NFL.com — official scores, schedules, injury reports
  Pro Football Reference (pro-football-reference.com) — comprehensive historical stats
  
Advanced metrics:
  PFF (Pro Football Focus, pff.com) — grades, CPOE, EPA, O-line stats
  NextGenStats (nextgenstats.nfl.com) — official NFL tracking data
  Sharp Football Stats (sharpfootballstats.com) — situational stats
  
Injury reports:
  NFL.com/injuries — official Wednesday/Thursday/Friday designations
  Rotoworld / NBC Sports (rotoworld.com) — injury analysis
  
Officiating:
  FootballPerspective.com — penalty rate analysis by referee crew
  NFL.com/officials — crew assignments and stats
```

### Basketball (NBA)
```
Official data:
  NBA.com/stats — official stats, advanced metrics, tracking data
  Basketball Reference (basketball-reference.com) — comprehensive historical
  
Advanced metrics:
  Cleaning the Glass (cleaningtheglass.com) — shot quality, lineup data
  PBP Stats (pbpstats.com) — play-by-play derived metrics
  RPM / EPM: ESPN (espn.com), Dunks and Threes
  
Schedule / rest tracking:
  Basketball Reference schedule — B2B and rest day calculation
  Tankathon (tankathon.com) — schedule and draft lottery tracking
```

### Cricket
```
Official data:
  ESPNcricinfo (espncricinfo.com) — primary cricket data source globally
  Statsguru (stats.espncricinfo.com) — deepest cricket statistics database
  CricketArchive (cricketarchive.com) — historical records
  
Live scoring and conditions:
  Cricbuzz (cricbuzz.com) — live scores, pitch reports, weather
  ICC (icc-cricket.com) — official international records
  
DLS calculator:
  ICC DLS calculator (icc-cricket.com/dls)
  
Umpire data:
  ESPNcricinfo umpire profiles — career stats and DRS records
```

### Horse Racing
```
Primary sources (UK/Ireland):
  Racing Post (racingpost.com) — form guide, going reports, tips, trainer stats
  Timeform (timeform.com) — ratings, speed figures, horse profiles
  BHA (britishhorseracing.com) — official going reports, results
  
International:
  Equibase (equibase.com) — North American racing data
  JRA (jra.go.jp) — Japan Racing Association official data
  Racing.com — Australian thoroughbred racing
  
Going / weather:
  Met Office (metoffice.gov.uk) — UK weather (cross-reference with going reports)
  Racecourse going reports — published morning of race day
```

### MMA / Combat Sports
```
Statistics:
  UFC Stats (ufcstats.com) — official UFC significant strikes, takedowns, time
  Tapology (tapology.com) — comprehensive MMA results, judge scorecards
  Sherdog (sherdog.com) — historical fight records, fighter profiles
  FightMatrix (fightmatrix.com) — ranking algorithms and fight data
  
Judge analytics:
  MMADecisions.com — judge-by-judge scoring breakdown for every decision fight
  FightOdds.io — historical MMA odds tracking
  
Fighter social / camp signals:
  UFC.com — official fighter pages, rankings
  Fighter social media (Twitter/X, Instagram) — camp updates, weight cut signals
```

### Formula 1 / MotoGP
```
F1:
  Formula1.com — official race results, timing, championship standings
  Autosport (autosport.com) — technical analysis, team news
  The Race (the-race.com) — in-depth F1 journalism
  F1metrics.net — statistical modelling, team performance

MotoGP:
  MotoGP.com — official results, standings, technical data
  GPone.com — paddock news and analysis
```

### Baseball (MLB)
```
Official data:
  MLB.com — official results, standings, rosters
  Baseball Reference (baseball-reference.com) — comprehensive historical stats
  
Statcast / advanced metrics:
  Baseball Savant (baseballsavant.mlb.com) — official Statcast data, xBA, xSLG
  FanGraphs (fangraphs.com) — advanced metrics, WAR, projections
  Baseball Prospectus (baseballprospectus.com) — PECOTA projections, DRC+
  
Park factors:
  Baseball Reference park factors
  Statcast park data (baseballsavant.mlb.com)
```

### Ice Hockey (NHL)
```
Official data:
  NHL.com — official stats, schedule, injury reports
  Hockey Reference (hockey-reference.com) — historical comprehensive stats
  
Advanced metrics:
  Natural Stat Trick (naturalstattrick.com) — Corsi, Fenwick, xG, line data
  MoneyPuck (moneypuck.com) — xG, GSAx, win probability models
  Evolving Hockey (evolving-hockey.com) — WAR, RAPM, goaltender analytics
```

### Golf
```
Official data:
  PGA Tour (pgatour.com) — official stats, Strokes Gained, ShotLink data
  European Tour / DP World Tour (europeantour.com) — European stats
  Masters.com, USOpen.com, TheOpen.com, PGAChampionship.com — Major data
  
Advanced analytics:
  DataGolf (datagolf.com) — rankings, predictions, course fit models
  Shot Scope (shotscope.com) — community-sourced strokes gained data
  Golf Insights (golfinsights.app) — course history and performance models
```

### Tennis
```
Official data:
  ATP (atptour.com) — official ATP rankings, stats, results
  WTA (wtatennis.com) — official WTA rankings, stats
  ITF (itftennis.com) — international records
  
Advanced analytics:
  Tennis Abstract (tennisabstract.com / Jeff Sackmann) — serve stats, H2H, surface splits
  Match Charting Project (github.com/JeffSackmann/tennis_MatchChartingProject) — detailed shot data
  ultimatetennisstatistics.com — comprehensive historical records
```

### Cycling
```
Official data:
  ProCyclingStats (procyclingstats.com) — comprehensive results, rankings
  FirstCycling (firstcycling.com) — stage results, historical data
  Velon (velon.cc) — real-time race data (participating teams)
  
Power data / performance:
  Strava (strava.com) — athlete activity segments (public professional data)
  CyclingTips (cyclingtips.com) — technical and race analysis
```

### Esports
```
CS2:
  HLTV (hltv.org) — primary CS2 statistics source: ratings, team stats, maps
  
League of Legends:
  Leaguepedia (lol.fandom.com) — comprehensive LoL esports database
  Oracle's Elixir (oracleselixir.com) — LoL advanced statistics
  
Dota2:
  Dotabuff (dotabuff.com) — hero stats, player profiles
  OpenDota (opendota.com) — open-source match data
  
General esports:
  Liquipedia (liquipedia.net) — multi-game tournament and roster data
  GRID (grid.gg) — official esports data platform
  Esports Charts (escharts.com) — viewership and audience data
```

---

## Layer 2 — Athlete intelligence sources

### Injury tracking (cross-sport)
```
Football: physioroom.com, premierinjuries.com
NFL: Pro Football Reference injury reports, Rotoworld
NBA: ESPN injury tracker (espn.com), Basketball Reference
Cricket: ESPNcricinfo injury updates
MMA: MMA Fighting injury reports, UFC.com medical suspensions
Horse racing: BHA medical rule book, Racing Post vet reports
```

### Form tracking (cross-sport)
```
Football: FBref rolling stats, WhoScored recent form tables
Tennis: Tennis Abstract current form filters
Golf: DataGolf last 24 rounds stats, PGA Tour current season leaders
Horse racing: Racing Post form guide (last 6 runs default)
MMA: Tapology fight log with method of victory tracking
```

---

## Layer 3 — Fan token and on-chain sources

### DeFi and liquidity pool data
```
Pool TVL and real-time DEX data:
  GeckoTerminal (geckoterminal.com) — real-time DEX pool data, price, volume, transactions
  DeFiLlama (defillama.com) — TVL across all DeFi protocols; yields database

LP activity and on-chain analytics:
  The Graph Protocol (thegraph.com) — index and query Chiliz Chain LP events
  Dune Analytics (dune.com) — custom SQL on on-chain data; fan token LP dashboards
  Moralis (moralis.io) — multi-chain LP position tracking API
  Covalent (covalenthq.com) — historical LP transaction data

Prediction market data:
  Azuro SDK (azuro.org/docs) — sports prediction market liquidity
  Polymarket CLOB API (docs.polymarket.com) — conditional prediction markets

Yield tracking:
  DeFiLlama yields (defillama.com/yields) — APR/APY across all protocols
```

### On-chain data (primary)
```
Chiliz Chain explorer:
  explorer.chiliz.com — transactions, holder data, token contracts, validators

Fan token holder data:
  Chiliz Chain API — holder counts, wallet distribution, transfer volume
  Dune Analytics (dune.com) — community-built Chiliz dashboards
  Nansen (nansen.ai) — wallet labelling, smart money tracking

Token price data:
  CoinGecko (coingecko.com) — prices, market cap, volume, historical data
  CoinMarketCap (coinmarketcap.com) — alternative price reference
  Binance (binance.com) — primary CEX for most fan tokens

CHZ (Chiliz) data:
  CoinGecko: coingecko.com/en/coins/chiliz
  CoinMarketCap: coinmarketcap.com/currencies/chiliz/
```

### Socios platform
```
Socios.com — official fan token platform
  - Active token list and utility event calendar
  - Voting history and participation rates
  - Partnership announcements
  Fan Token Intel (fantokenintel.com) — primary third-party signal platform
```

### Validator intelligence
```
Chiliz Chain validator registry:
  explorer.chiliz.com/validators — current validator set
  Chiliz Chain governance contracts — on-chain governance participation
  Chiliz docs: docs.chiliz.com — validator documentation

Validator monitoring:
  Dune Analytics — custom dashboards for validator stake tracking
  Chiliz Chain RPC (rpc.ankr.com/chiliz) — direct chain queries
```

### Social intelligence (athlete and club)
```
Twitter/X API — follower counts, engagement rates, mention volume
Instagram Graph API — follower growth, post engagement
TikTok Research API — video performance, follower growth
YouTube Data API — subscriber counts, view counts
Brandwatch / Meltwater — sentiment analysis, social listening
SocialBlade (socialblade.com) — growth tracking for YouTube, Twitter
```

---

## Layer 4 — Market intelligence sources

### Sports industry revenue
```
Deloitte Annual Review of Football Finance (deloitte.com/uk/football-money-league)
PwC Sports Survey (pwc.com) — annual sports industry outlook
Sportico (sportico.com) — franchise valuations, media rights deals
SportsBusiness Journal (sportsbusinessjournal.com) — commercial intelligence
Forbes Sports valuations (forbes.com/sports) — team and athlete values
```

### Fan token market
```
Messari (messari.io) — crypto market research including fan token sector
The Block (theblock.co) — on-chain analytics, fan token market reports
DeFiLlama (defillama.com) — TVL and on-chain metrics
Nansen fan token dashboards (nansen.ai)
```

### Broadcasting and media rights
```
Rights deals documentation:
  Sports Business Journal — media rights deal database
  Guardian Sport — UK rights coverage
  Variety / Deadline — US media/sports rights coverage
  
Streaming data:
  Nielsen Media Research — sports viewership data
  Parrot Analytics (parrotanalytics.com) — streaming demand data
  
RSN / regional sports networks:
  Sports Media Watch (sportsmediawatch.com) — ratings, rights analysis
```

### Demographic data
```
Statista (statista.com) — sports demographic surveys
Nielsen Fan Insights — sports fan demographic research
Morning Consult (morningconsult.com) — brand tracking, fan surveys
YouGov Sport (yougov.com) — sports fan surveys
```

---

## Layer 5 — Macro intelligence sources

### Crypto market data
```
BTC/CHZ price and correlation:
  CoinGecko (coingecko.com) — historical price data for correlation analysis
  TradingView (tradingview.com) — charting, 200-day MA, correlation tools
  Glassnode (glassnode.com) — on-chain Bitcoin metrics, market cycle indicators
  
Crypto market cycle:
  Fear and Greed Index (alternative.me/crypto/fear-and-greed-index/)
  Bitcoin Rainbow Chart (blockchaincenter.net)
```

### Geopolitical and macro economic
```
Reuters (reuters.com) — primary wire service for breaking geopolitical news
Bloomberg (bloomberg.com) — financial markets and macro data
IMF World Economic Outlook (imf.org) — global economic projections
World Bank (worldbank.org) — country-level economic data
Oxford Economics (oxfordeconomics.com) — economic forecasting
```

### Climate and weather
```
Weather data:
  Weather.com (weather.com) — global forecasts, historical data
  Dark Sky API (now Apple Weather) — hyperlocal forecasting
  BBC Weather (bbc.co.uk/weather) — UK and global forecasts
  National Weather Service (weather.gov) — US forecasts

Climate risk:
  Swiss Re Institute (swissre.com/institute) — climate risk modelling
  Aon Weather, Climate and Catastrophe Insight (aon.com)
```

### Governance and scandal
```
BBC Sport investigative (bbc.co.uk/sport) — governance reporting
The Guardian Sport (theguardian.com/sport) — investigative sports journalism
Reuters investigative — corruption and doping coverage
WADA (wada-ama.org) — official anti-doping sanctions and testing
CAS (tas-cas.org) — Court of Arbitration for Sport rulings
FIFA Ethics Committee reports (fifa.com) — football governance
```

### Public health
```
WHO (who.int) — global health emergency declarations
CDC (cdc.gov) — US public health guidance (travel implications)
ECDC (ecdc.europa.eu) — European disease surveillance
```

---

## Developer tooling — API quick reference

```
FREE / OPEN DATA APIS:
  OpenDota API (docs.opendota.com) — Dota2 match data
  HLTV undocumented scraping — CS2 (unofficial; check ToS)
  Tennis Abstract API (jeffsackmann.com) — tennis data files (GitHub)
  Baseball Reference Stathead — requires subscription
  FBref (via StatHead, fbref.com) — football statistics

COMMERCIAL APIS:
  Opta Sports (statsperform.com) — professional sports data (licensed)
  Stats Perform (statsperform.com) — comprehensive sports data platform
  SportRadar (sportradar.com) — sports data for commercial applications
  Genius Sports (geniussports.com) — official league data partnerships
  Sportradar (sportradar.com) — official NFL/NBA/NHL data partner

BLOCKCHAIN APIS:
  Chiliz Chain RPC: rpc.ankr.com/chiliz (free tier available)
  Alchemy (alchemy.com) — EVM-compatible node access (Chiliz compatible)
  Moralis (moralis.io) — multi-chain APIs including fan token data
  Covalent (covalenthq.com) — multi-chain data API

SOCIAL APIS:
  Twitter/X API v2 (developer.twitter.com) — requires developer account
  Instagram Graph API (developers.facebook.com) — business account required
  YouTube Data API v3 (developers.google.com/youtube) — free quota available
```

---

## Source quality hierarchy

```
When multiple sources conflict, apply this hierarchy:

TIER 1 — OFFICIAL / ON-CHAIN (highest authority):
  Official league/federation websites
  On-chain blockchain data (explorer.chiliz.com, etc.)
  Official regulatory filings (SEC, Companies House, etc.)
  Court/arbitration rulings (CAS, FIFA Ethics)

TIER 2 — PRIMARY JOURNALISM AND LICENSED DATA:
  Licensed data providers (Opta, Sportradar, Stats Perform)
  Established investigative sports journalism (The Athletic, Guardian, BBC)
  Peer-reviewed academic sports science research
  Official annual reports and financial filings

TIER 3 — SECONDARY ANALYTICS AND COMMUNITY:
  Advanced analytics sites (FBref, Basketball Reference, etc.)
  Respected community research (Dune Analytics dashboards)
  Established sports business media (SportsBusiness Journal, Sportico)

TIER 4 — SOCIAL AND REAL-TIME SIGNALS:
  Transfer journalist reports (Romano, Di Marzio — high reliability)
  Official club/athlete social media posts
  Aggregated sentiment data

NEVER USE AS PRIMARY SOURCE:
  Anonymous forum posts (Reddit, Discord) without corroboration
  Prediction market prices as facts (they are sentiment, not data)
  AI-generated content (including SportMind itself) as its own source
  Press releases without independent verification for factual claims
```

---

## Citation format for SportMind skills

When adding data to SportMind skill files, use this format:

```
Single source:
  SOURCE: [Source name] ([url]) — [what it provides]
  
Multiple sources:
  SOURCES:
    Primary:   [Source 1] ([url1])
    Secondary: [Source 2] ([url2])
    
Time-sensitive data (always flag):
  SOURCE: [Source] ([url]) — data current as of [month/year]; verify before use

Example (correct):
  CHZ/BTC correlation ~0.80 (2022–2024 bear market data)
  SOURCE: CoinGecko historical data (coingecko.com) — correlation calculated
          from 2022–2024 weekly closing prices; recalculate quarterly
```

---

*Data sources change. URLs move. APIs deprecate. This file should be reviewed
and updated with each major SportMind version.*

*MIT License · SportMind · sportmind.dev*
