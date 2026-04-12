# Verifiable Sources by Sport — SportMind Quick Reference

**The single-question answer to: "where do I verify this claim?"**

This is a use-case-first reference. Every SportMind signal should be
verifiable against a named, authoritative source. This file maps the
most common agent queries to the specific source that settles them.

For the comprehensive source catalogue by layer, see `core/data-sources.md`.
This file is the fast-lookup version — one question, one source.

---

## How to use this file

```
Agent needs to verify: "Is the player confirmed in the starting XI?"
→ Football: official club social channels (T-2h) or official league app
→ Rugby: team sheet released 1h before kick-off on official club site
→ NBA: beat reporter tweet or official injury report (ESPN/NBA.com)

Agent needs to verify: "What is the current ban length for this player?"
→ Check the sport-specific disciplinary section in this file
→ Cross-reference: core/athlete-disciplinary-intelligence.md for framework

Rule: If a source cannot be named, the claim cannot be used as a signal input.
```

---

## Football

### Match result and score
- **Official:** BBC Sport (bbc.co.uk/sport/football) — fastest UK mainstream
- **Official:** Premier League app / La Liga / Bundesliga official sites
- **Deep stats:** FBref (fbref.com) — xG, possession stats, all competitions

### Player availability and lineup
- **T-72h:** Manager press conference — club official YouTube/X
- **T-24h:** Training ground reports — The Athletic, BBC Sport
- **T-2h (official):** Club official X account or league app
- **Live:** BBC Sport match centre, Sky Sports match centre

### Player statistics (match-level)
- **Primary:** Sofascore (sofascore.com) — real-time match stats
- **Deep:** FBref — progressive passes, pressures, xG, per-90 metrics
- **Alternative:** WhoScored (whoscored.com) — match ratings + stats

### Player statistics (season-level / per 90)
- **FBref** — most comprehensive, freely accessible, all major leagues
- **Transfermarkt** (transfermarkt.com) — career stats, market value
- **Understat** (understat.com) — xG models, top European leagues only

### Transfer news (verifiable only)
- **Fabrizio Romano** (@FabrizioRomano on X) — "here we go" = confirmed
- **The Athletic** — verified long-form transfer reporting
- **Club official announcement** — definitive confirmation

### Disciplinary / bans
- **FA:** thefa.com/football-rules-governance/disciplinary
- **UEFA:** UEFA.com/insideuefa/disciplinary
- **FIFA:** FIFA.com/legal/disciplinary
- **Aggregator:** BBC Sport disciplinary section

### Referee assignment
- **UK:** Premier League official site (premierleague.com/referees)
- **European:** UEFA referee appointments page
- **FootyStats:** footystats.org/referees — historical referee stats

### Team and league strength (Elo ratings)
- **Global Football Rankings (GFR):** globalfootballrankings.com — True Elo ratings (0–100) for teams and leagues across 75 competitions, updated weekly. Use for opponent quality weighting in H2H analysis (core/historical-intelligence-framework.md) and commercial tier context (core/sports-trend-intelligence.md).
- **Club Elo:** clubelo.com — simple Elo ratings for top European club football. Free, well-maintained.
- **FIFA World Rankings:** fifa.com/ranking — official international team rankings. Use for national team H2H quality weighting.

### Odds and market
- **Sharp reference:** Pinnacle (pinnacle.com)
- **Historical odds:** Oddsportal (oddsportal.com)
- **Exchange:** Betfair (betfair.com/sport/football)

---

## Rugby Union

### Match result and score
- **Official:** World Rugby (world.rugby) — international
- **Domestic UK:** BBC Sport rugby union section
- **Premiership:** premiershiprugby.com
- **Six Nations:** sixnationsrugby.com

### Player availability and lineup
- **Team sheet:** Released 1h pre-match, official club site
- **Injury updates:** Official coach press conference (T-48h)
- **Rugby Pass** (rugbypass.com) — best specialist injury tracking

### Player statistics
- **ESPN Scrum** (espnscrum.com) — historical international stats
- **Rugby Reference** (rugbyreference.com) — career and season stats
- **itsrugby.co.uk** — domestic competition stats

### Disciplinary / citing decisions
- **World Rugby:** world.rugby/the-game/judicial-decisions — ALL decisions published
- **Premiership:** premiershiprugby.com/news/disciplinary
- **Search:** "[Player name] judicial decision" on Google — official PDFs indexed

### World rankings
- **Official:** world.rugby/rugby-world-rankings — updates weekly

---

## Rugby League

### Match result and score
- **Official NRL:** nrl.com
- **Official Super League:** superleague.co.uk
- **BBC Sport:** bbc.co.uk/sport/rugby-league

### Player availability and lineup
- **NRL:** nrl.com injury list — official Thursday update
- **Super League:** club official sites, coach press conferences (T-48h)

### Player statistics
- **NRL:** nrl.com/stats — official NRL stats
- **Super League:** superleague.co.uk/stats

### Disciplinary
- **NRL match review:** nrl.com/the-game/integrity-and-welfare/match-review-committee
- **Super League:** rfl.uk/the-game/discipline — Rugby Football League

---

## Cricket

### Match result and scorecard
- **Primary:** ESPNcricinfo (espncricinfo.com) — definitive global cricket source
- **Secondary:** Cricbuzz (cricbuzz.com) — faster live scoring

### Player statistics
- **Statsguru:** stats.espncricinfo.com — deepest cricket stats database globally
- **CricketArchive:** cricketarchive.com — historical records

### Playing conditions / pitch / weather
- **Cricbuzz:** pitch reports, toss, live weather at ground
- **Weather:** timeanddate.com or local met office for ground location

### Dew factor verification
- **timeanddate.com/weather** for humidity at match venue
- **Cricbuzz pitch report** — commentators reference dew explicitly in evening T20s

### Team selection and lineup
- **ESPNcricinfo:** squad and XI announced pre-match
- **ICC:** icc-cricket.com — international team announcements

### Disciplinary (ICC Code of Conduct)
- **Official:** icc-cricket.com/about/cricket/rules-and-regulations/code-of-conduct
- **ESPNcricinfo news:** search player name + "code of conduct"

### Rankings
- **Official ICC:** icc-cricket.com/rankings — Test, ODI, T20I (all formats)

---

## Formula 1

### Race result
- **Official:** formula1.com/en/results — definitive results including post-race penalties
- **Note:** results may change post-race from steward decisions — check 3h after race

### Qualifying result and delta
- **Official:** formula1.com/en/results — qualifying tab
- **Motorsport Stats:** motorsportstats.com — sector times and gaps

### Driver availability
- **Official:** formula1.com news — team statements on driver fitness
- **Motorsport.com** — most reliable Formula 1 specialist news source

### Steward decisions
- **FIA:** fia.com/documents/decisions — ALL steward documents published
- **Autosport:** autosport.com — fastest reputable reporting of decisions

### Super licence penalty points
- **Official FIA:** fia.com/documents/decisions — cumulative points in each decision PDF
- **Current totals:** formula1.com driver profiles (updated periodically)
- **Specialist tracking:** racefans.net/f1-penalties/super-licence-penalty-points

### Constructor and driver standings
- **Official:** formula1.com/en/results/standings

### Weather at circuit
- **Weather.com** or **timeanddate.com** for circuit location
- **F1 Weather** apps — race weekend specialist forecast

---

## MMA / UFC

### Fight result
- **Official:** ufc.com/results — fastest official source
- **MMA Fighting:** mmafighting.com — reliable live results + post-fight detail

### Fighter availability / weigh-in
- **Official weigh-in:** ufc.com (live weigh-in results on event page)
- **Twitter/X:** @UFC official for immediate weigh-in results
- **MMA Fighting:** live weigh-in coverage

### Fighter statistics
- **UFC Stats:** ufcstats.com — official fight-level stats (all UFC bouts)
- **Tapology:** tapology.com — fighter records, stats, amateur history
- **Sherdog:** sherdog.com — historical MMA fighter database

### USADA / doping
- **USADA:** usada.org/testing/results/sanctions — all sanctions published
- **UFC:** ufc.com/news — UFC-issued suspension announcements

### Rankings
- **Official UFC:** ufc.com/rankings — divisional rankings (updated weekly)

---

## Ice Hockey (NHL)

### Game result
- **Official:** nhl.com/scores
- **ESPN NHL:** espn.com/nhl

### Morning skate / lineup confirmation
- **TSN:** tsn.ca (Canadian teams — fastest coverage)
- **The Athletic:** theathletic.com/nhl — beat reporter morning skate reports
- **Daily Faceoff:** dailyfaceoff.com — morning skate specialist
- **Twitter/X:** beat reporters tweet morning skate lineups T-3h to T-1h

### Player statistics
- **Official:** nhl.com/stats — official NHL stats
- **Natural Stat Trick:** naturalstattrick.com — Corsi, Fenwick, xG, all situations
- **Hockey Reference:** hockey-reference.com — comprehensive historical

### GSAx (Goals Saved Above Expected)
- **Money Puck:** moneypuck.com — GSAx and advanced goaltender metrics
- **Evolving Hockey:** evolving-hockey.com — GSAA and xG models

### Injury / roster
- **Official:** nhl.com/injury-reserve — official IR list
- **Daily Faceoff:** dailyfaceoff.com/projected-lineups — lineup projections

### Disciplinary
- **NHL DOPS:** nhl.com/news/department-player-safety — all suspensions and fines
- **Official:** nhl.com/videos/dops (video review of incidents)

---

## Tennis

### Match result
- **Official ATP:** atptour.com/en/scores
- **Official WTA:** wtatennis.com/scores
- **Tennis Abstract:** tennisabstract.com — granular match stats

### Player statistics (surface win rates)
- **Tennis Abstract:** tennisabstract.com/cgi-bin/player.cgi — by surface
- **Ultimate Tennis Statistics:** ultimatetennisstatistics.com — comprehensive

### Ranking
- **Official ATP:** atptour.com/en/rankings
- **Official WTA:** wtatennis.com/rankings

### Player availability / withdrawals
- **ATP/WTA official site** — withdrawal notices
- **The Tennis Podcast** / specialist tennis Twitter accounts

### Disciplinary
- **ATP:** atptour.com/en/players/integrity-program
- **WTA:** wtatennis.com (code of conduct section)
- **ITF:** itftennis.com/en/about-us/governance/rules-and-regulations

---

## AFL

### Match result
- **Official:** afl.com.au/matches — definitive
- **AFL Tables:** afltables.com — comprehensive historical

### Player statistics
- **Champion Data:** championdata.com.au (subscription) — official AFL data partner
- **AFL Tables:** afltables.com — freely accessible historical
- **Footywire:** footywire.com — match stats, player stats, fantasy data

### Player availability
- **AFL official:** afl.com.au (team selection released Thursday)
- **Zero Hanger:** zerohanger.com — specialist AFL news

---

## Basketball (NBA)

### Game result
- **Official:** nba.com/scores
- **Basketball Reference:** basketball-reference.com

### Player availability / DNP
- **Official:** nba.com/players/injuries — official injury report
- **ESPN:** espn.com/nba/injuries
- **The Athletic beat reporters:** fastest for DNP-rest notifications

### Advanced statistics
- **Cleaning the Glass:** cleaningtheglass.com — shot quality, filtered stats
- **Natural Stat Trick (NBA equivalent):** pbpstats.com — play-by-play derived
- **Second Spectrum:** (official NBA tracking) — via NBA.com/stats

### Net rating / team statistics
- **NBA.com/stats:** official — team and player advanced stats
- **Basketball Reference:** per-100 possession stats, BPM, VORP

---

## Kabaddi

### Match result
- **Official PKL:** prokabaddi.com — Pro Kabaddi League official
- **Kabaddi Adda:** kabaddiadda.com — specialist coverage

### Player statistics
- **PKL official:** prokabaddi.com/statistics
- **Kabaddi Adda:** player profiles and stats

### Raider primacy verification
- **PKL stats:** raid points, successful raids, raid strike rate — prokabaddi.com

---

## Darts

### Match result
- **PDC official:** pdc.tv/results
- **BDO / WDF:** wdf.sport (world governing body)
- **Darts Database:** dartsdatabase.co.uk — historical results and statistics

### Player statistics / averages
- **Darts Database:** dartsdatabase.co.uk — average, checkout %, 180s
- **PDC:** pdc.tv/players — official PDC stats

---

## Snooker

### Match result
- **Official:** worldsnooker.com/results
- **CueTracker:** cuetracker.net — most comprehensive snooker stats database

### Player statistics
- **CueTracker:** century breaks, win rates by tournament type, head-to-head

---

## Cross-sport: what counts as a verifiable source

```
TIER 1 — GROUND TRUTH (always accept):
  Official governing body announcements (FA, World Rugby, ICC, FIA, etc.)
  Official club/team announcements (direct from club website or verified social)
  Official league/competition results (Premier League, NRL, UFC, etc.)
  
TIER 2 — RELIABLE (accept with standard confidence):
  Established specialist outlets: The Athletic, ESPN, BBC Sport, Sky Sports
  Verified beat reporters: named journalists covering specific teams
  Official aggregators: Transfermarkt, FBref, Basketball Reference
  
TIER 3 — USABLE WITH CAUTION (corroborate before using):
  General sports media: Guardian, Telegraph, Mail Sport — verify with Tier 1/2
  Social media (non-verified accounts): corroborate before treating as signal
  Aggregator sites pulling from multiple sources: check primary source chain
  
TIER 4 — DO NOT USE AS SIGNAL INPUT:
  Anonymous sources ("sources close to the club")
  Unverified social media accounts
  Tabloid speculation (transfer rumours pre-Romano confirmation)
  Fan sites and blogs (unless citing Tier 1/2 primary source)
  
RULE: An agent generating a signal from a Tier 4 source
must flag: SOURCE_UNVERIFIED. Do not treat as confirmed input.
```

---

## Fastest verification paths by query type

| Query | Fastest verifiable source | Tier |
|---|---|---|
| Final score | BBC Sport / official league app | 1 |
| Starting lineup | Club official X account (T-2h) | 1 |
| Transfer confirmed | Fabrizio Romano "here we go" + club announcement | 1+2 |
| Player banned | Governing body disciplinary page | 1 |
| Weigh-in result | UFC.com event page | 1 |
| Qualifying gap (F1) | formula1.com/results | 1 |
| Morning skate (NHL) | Beat reporter tweet + Daily Faceoff | 2 |
| xG stats | FBref | 2 |
| Surface win rate (tennis) | Tennis Abstract | 2 |
| Dew conditions | Cricbuzz pitch report + local weather | 2+3 |
| Super licence points | FIA decisions (PDF) | 1 |
| Doping suspension | USADA.org or governing body | 1 |
| Criminal charge | National news outlet + club statement | 1+2 |

---

*SportMind v3.33 · MIT License · sportmind.dev*
*See also: core/data-sources.md (full catalogue) · core/temporal-awareness.md (freshness)*
*core/athlete-disciplinary-intelligence.md (disciplinary source detail)*
