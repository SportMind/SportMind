# Draft Intelligence — SportMind Core

Drafts are among the highest-engagement annual events in North American and
Australian sports and in esports — with immediate impact on squad composition,
athlete value, fan token prices, and commercial narratives. This skill gives AI
agents a framework for reasoning about drafts as signal-generating events.

---

## Why drafts are a fan token and prediction signal

```
DRAFT AS A SIGNAL EVENT:
  A high draft pick entering a squad:
  → Raises expectation for the team's future performance
  → Creates immediate narrative around the drafted player
  → Shifts the position-level modifier for incumbent players
    (a highly-rated incoming QB threatens the starter's token value)
  → Generates commercial activity: jerseys, merchandise, brand deals
  → Can immediately affect team fan token price (positive for team)
    and incumbent player token value (negative if directly threatened)

DRAFT AS A COMMERCIAL INTELLIGENCE EVENT:
  Draft selections are the first commercial moment for an athlete's career
  The draft pick number, team, and media narrative determine initial brand value
  → feeds directly into the athlete commercial pipeline (Layer 3)
```

---

## NFL Draft — the highest-profile annual draft event

```
DRAFT STRUCTURE:
  7 rounds, 257+ picks total
  Order: Worst record picks first (reverse standings order)
  Compensatory picks: Added for free agent losses in previous offseason

KEY TIMING:
  Draft held: Late April (3 days; rounds 1, 2–3, 4–7)
  Pre-draft: Combine (February), Pro Days (March), Top 30 visits (April)
  Trade deadline during draft: Significant picks traded in real-time

ROUND 1 PICKS — TOKEN SIGNAL:
  Picks 1–5: Franchise-altering; immediate team fan token uplift expected
  Expected CHZ signal: +8–15% for team token if pick fills critical need
  
  Picks 6–15: High-quality starters; meaningful impact
  Expected CHZ signal: +4–8% for team token
  
  Picks 16–32: Good starters; incremental
  Expected CHZ signal: +1–4% for team token

QUARTERBACK PICKS — HIGHEST SIGNAL:
  Top QB drafted = immediate uncertainty for incumbent starter's token value
  If incumbent starter has an individual token → apply −15 to −25% signal
  
  Non-QB Round 1: Position-specific; apply to incumbent in that position
  Example: Top WR drafted = small negative for incumbent WR1; positive for QB token

TRADE UP SIGNAL:
  Team trading multiple picks to move up for a player = very high conviction
  from the front office; amplifies positive signal for that player/team
  
  Team trading down = less urgent need; diluted positive signal

DATA SOURCES:
  NFL.com/draft, ESPN Draft Center, PFF Draft grades,
  NFL Mock Draft database (track consensus over pre-draft period)
```

---

## NBA Draft — franchise-building event

```
DRAFT STRUCTURE:
  2 rounds, 60 picks total
  Lottery (picks 1–14): Weighted random for non-playoff teams
  Picks 15–30: Reverse standings order of playoff teams

LOTTERY ANNOUNCEMENT:
  Held in May (before draft)
  Moving up in lottery = significant positive for team token
  "Lottery luck" for rebuilding teams is a documented token catalyst
  Expected CHZ signal for lottery winner (top pick): +10–20%

SUPERSTAR POTENTIAL PICKS (Projected top 3):
  Athletes projected as franchise players drive narrative for 12+ months
  Draft night social volume for projected top picks: 2–5× normal
  
SECOND ROUND — UNDRAFTED PLAYERS:
  Some high-value players fall to 2nd round or go undrafted
  When a highly-regarded prospect falls unexpectedly: narrative opportunity

IMMEDIATE READINESS vs DEVELOPMENTAL PICKS:
  Ready-now picks: Immediate positive modifier for next season prediction
  Project picks (high upside, need development): Delayed signal; 2–3 seasons
  
  Agent rule: For prediction markets covering the upcoming season,
  discount developmental picks heavily in modifier calculation

DATA SOURCES:
  NBA.com/draft, ESPN Draft, The Athletic draft coverage,
  NBADraft.net prospect tracking
```

---

## NHL Draft — goaltender special case

```
DRAFT STRUCTURE:
  7 rounds, 217 picks
  Age: 18-year-olds primarily; some 19-year-olds
  CHL (Canada), NCAA, European leagues are primary development paths

NHL DRAFT SIGNAL NOTES:
  NHL prospects take longest to develop of any major North American sport
  First round picks typically debut 2–4 years after draft
  Goaltenders: 3–6 years to NHL readiness
  
  For token signal purposes: NHL draft picks have DELAYED impact
  Apply to team token: +2–5% for top 5 pick; primarily sentiment, not performance
  
EXCEPTION — GENERATIONAL TALENT:
  When a player is considered exceptional (Connor McDavid 2015, Jack Hughes 2019)
  Team fan sentiment and future expectations create immediate token signal
  Exceptional pick: +8–12% team token sentiment signal

DATA SOURCES:
  NHL.com/draft, EliteProspects.com (European scouting data)
```

---

## MLB Draft — Statcast-driven scouting

```
DRAFT STRUCTURE:
  20 rounds (reduced from 40 in 2021 CBA)
  Competitive balance rounds add picks for smaller market teams

MLB DRAFT SIGNAL:
  Like NHL, MLB prospects require 2–4 years to reach MLB (minor league development)
  Immediate signal is modest; primarily affects long-term franchise outlook
  
  #1 Overall pick: +3–6% team fan sentiment token signal
  
  COLLEGE vs HIGH SCHOOL picks:
  College players: Ready sooner (1–3 years); more predictable
  High school players: Higher ceiling, higher variance; 3–5 years to MLB
  
FINANCIAL BONUS POOL:
  Teams drafting early receive larger bonus pools for signing bonuses
  Failure to sign a top pick = forfeiture of pool money + lost prospect
  Monitor: Player/team signing agreement confirmation within August deadline

DATA SOURCES:
  MLB.com/draft, Baseball America draft rankings,
  FanGraphs draft prospect evaluations
```

---

## AFL Draft — Australian Rules

```
DRAFT STRUCTURE:
  National Draft (November): Primary mechanism; reverse ladder order
  Father-Son, Academy, and Rookies: Additional selection mechanisms
  
  Points system: Clubs accumulate points for pick trades

AFL DRAFT SIGNAL:
  AFL players transition to senior football faster than North American drafts
  Round 1 picks can debut in Year 1 or early Year 2
  #1 Overall pick: Significant immediate expectation; +6–10% team token sentiment
  
  FATHER-SON SELECTIONS:
  When a high-profile father's son is available: Large narrative event
  Clubs pay premium compensation picks for Father-Son selections
  
  ACADEMY SELECTIONS:
  Pre-announced; signal is lower (known outcome)

INTERSTATE CLUBS:
  GWS Giants, Gold Coast: Use early picks to build expansion clubs
  Their token potential is tied directly to draft success over multiple years

DATA SOURCES:
  AFL.com.au/draft, DraftGuru.com.au, AFL Tables historical data
```

---

## Esports Draft — League of Legends LCS/LEC Relegation and Roster Builds

```
ESPORTS ROSTER CONSTRUCTION (different from traditional draft):
  Most esports don't have formal drafts — players sign free agent contracts
  Exception: Some leagues have expansion drafts when new teams enter

  The equivalent event to a draft in esports:
  → Free agency signings (transfer window equivalent)
  → Academy to main roster promotions
  → Import player announcements

ESPORTS DRAFT-EQUIVALENT SIGNAL:
  Star player signing = team token positive (+8–15% for top-tier signing)
  Franchise player retirement announcement = team token negative (−10–20%)
  
  See: fan-token/esports-token-intelligence — for roster change modifiers (GRM, RSI)

LCS/LEC ACADEMY PROMOTIONS:
  When an Academy player is promoted to main roster:
  → Positive signal if highly-rated prospect
  → Negative signal if forced by underperforming main roster (crisis signal)

DATA SOURCES:
  Leaguepedia.com, HLTV.org transfers, Liquipedia rosters
```

---

## Draft calendar — annual agent monitoring schedule

```
ANNUAL DRAFT EVENTS (approximate dates):

February:
  NFL Combine (Indianapolis) — prospect measurements/interviews
  NBA Draft Combine invitations announced

March:
  NFL Pro Days (team facility visits)
  AFL Academy selections announced
  
April:
  NFL Draft (late April, 3 days)
  
May:
  NBA Draft Lottery (mid-May)
  
June:
  NBA Draft (late June)
  NHL Draft (late June)
  
July:
  MLB Draft (mid-July, during All-Star week)
  
October/November:
  AFL National Draft (November)
  NHL free agency (October onwards)

AGENT MONITORING RULE:
  Load draft intelligence 2 weeks before any major draft event
  Apply team and player signal modifiers immediately upon pick announcement
  Team tokens: monitor for 48h post-draft for full signal absorption
  Player commercial value: Update brand score (ABS) within 24h of pick announcement
```

---

## Draft intelligence and fan token interaction

```
DRAFT PICK → TOKEN SIGNAL CHAIN:

Team fan token:
  High pick selected: Positive sentiment → typically +3–15% depending on pick tier
  Mid-round picks: Minimal immediate signal unless high-profile player
  Failed pick (highly-touted player busts): Lagging negative 12–24 months later

Incumbent player token (if individual tokens exist):
  Same position selected high: Negative signal → career uncertainty
  Different position: Neutral
  Trade up for a player = specific incumbent threatened: Significant negative

National team tokens:
  Draft picks who project for national team duty (World Cup, Olympics):
  Deferred positive signal for national team tokens in 2–4 years

AGENT RULE: Create a draft watchlist 30 days before each major draft.
Monitor pick announcements in real-time. Apply signal modifiers
within 1 hour of each pick for maximum timing advantage.
Team tokens absorb draft news faster than individual player tokens.
```

*MIT License · SportMind · sportmind.dev*
