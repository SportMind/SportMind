---
name: performance-off-pitch
description: >
  Athlete development intelligence skill covering training load and adaptation, loan
  spell performance and return readiness, pre-season fitness trajectories, psychological
  resilience signals, youth academy progression, rehabilitation journeys, and holistic
  athlete wellbeing indicators. Use this skill when the user asks about a player's
  development pathway, training performance, whether a loan spell is working, loan
  return readiness, pre-season form, youth academy players and their progression,
  a player's mentality or professionalism signals, injury rehabilitation progress,
  how a player is adapting to a new club or league, or any question about what is
  happening with an athlete away from match day. Also trigger for questions about
  whether a young player is ready to step up, whether a fringe player deserves more
  opportunities, or what a player's trajectory looks like beyond raw match stats.
  Works closely with performance-on-pitch (which covers match data) and feeds
  transfer-intelligence (loan analysis) and brand-score (character premium).
---

# Performance Off-Pitch

Athlete development and off-pitch intelligence — training, loan spells, psychology,
rehabilitation, and everything that shapes performance before the whistle blows.

## What this skill produces

- **Development Trajectory Score (DTS)** — Rate and direction of athlete improvement (0–100)
- **Loan Spell Report** — Full analysis of loan performance, development value, return readiness
- **Training Adaptation Index (TAI)** — How well is an athlete adapting to a new environment?
- **Readiness Score** — Is this athlete ready for the next level? (first team / promotion / return)
- **Professionalism Signal** — Indirect indicators of mentality, attitude, commitment
- **Rehabilitation Progress** — Post-injury return timeline and readiness assessment
- **Youth Academy Pathway** — For academy players: development milestones and projection

---

## Data sources

### Performance over time
- **API-Football**: season-by-season stats for trajectory analysis
- **Transfermarkt**: loan history, career timeline, market value trajectory
- **FBref**: per-90 metric progression year-on-year (where available)

### Physical and training load (where partnership allows)
- **STATSports / Catapult GPS**: session load data — requires direct club partnership
- **FIFA TMS / club databases**: training minutes, session intensity (direct partnership)
- For most external analyses: use publicly available match load as proxy
  (minutes played per week, congested fixture involvement, rest periods)

### Loan and development signals
- **Transfermarkt**: loan history, parent club, loan club tier, minutes at loan club
- **API-Football**: stats at loan club vs. parent club league level context
- **Football Talents** / **WhoScored**: youth ratings and development tracking
- **UEFA Youth League / competition APIs**: for academy-level data

### Psychological and professionalism signals (indirect)
These cannot be measured directly but can be inferred from:
- Social media posting patterns during difficult periods (consistency = resilience signal)
- Media appearances (interviews, press conferences — sentiment and body language analysis)
- Training ground attendance signals (public training sessions, pre-match media)
- Agent activity (unusually quiet = stable; hyper-active = unsettled)
- Manager and club quotes (positive specific mentions = trusted; vague = concern)

---

## Workflow

### Step 1 — Establish developmental context
Accept: athlete name + optional context (loan club / parent club / academy / rehabilitation)

Classify the query type:
```
"loan_analysis"        → player currently at loan club
"return_readiness"     → assessing whether player should return from loan
"youth_progression"    → academy or U23 player development
"new_club_adaptation"  → player recently transferred (within 6 months)
"injury_rehabilitation"→ player returning from significant injury (>4 weeks)
"training_load"        → in-season load management and performance
"career_development"   → long-term trajectory and potential ceiling
```

### Step 2 — Development Trajectory Score (DTS)
Compare current season metrics vs. same metrics 1 and 2 seasons ago:

```
DTS = (
  performance_metric_improvement    * 0.35 +   # core stats improving YoY
  minutes_progression               * 0.20 +   # getting more playing time
  level_of_competition_delta        * 0.25 +   # playing at higher tier
  value_trajectory                  * 0.20     # market value direction
) * 100

where:
  performance_metric_improvement = avg(
    (current_PI - prior_year_PI) / prior_year_PI
  ) normalised to 0–1

  level_of_competition_delta: promotion to higher league/tier = +0.3 bonus
```

DTS interpretation:
- 80–100: Exceptional development — outpacing expected curve
- 60–79: On track — developing as expected for age/level
- 40–59: Plateau — neither regressing nor improving
- 20–39: Stalling — intervention or change of environment needed
- 0–19: Regression — investigate cause urgently

### Step 3 — Loan Spell Report

**Loan viability assessment:**
```
loan_value_score = (
  minutes_per_match / 90          * 0.30 +   # are they actually playing?
  performance_delta_vs_parent     * 0.25 +   # better than parent club showed?
  league_tier_match               * 0.20 +   # appropriate development level
  tactical_role_match             * 0.15 +   # playing their position properly
  form_trajectory_at_loan_club    * 0.10     # improving during the loan?
) * 100
```

**Loan purpose check** (against initial objective):
```
IF loan purpose was "get regular minutes":
  → check minutes %. Below 60%? Loan is failing.

IF loan purpose was "try higher level":
  → check PI vs. league benchmark. Below 40th pct? Too big a step.

IF loan purpose was "loan-to-buy relationship":
  → check if destination club's manager references player positively in press
```

**Return readiness score:**
```
return_readiness = (
  current_PI_at_loan_club          * 0.30 +
  loan_club_tier_vs_parent_tier    * 0.25 +
  minutes_consistency              * 0.20 +
  trajectory_in_last_10_games      * 0.15 +
  parent_squad_need                * 0.10   # is there a gap in parent squad?
) * 100
```

Readiness bands:
- 75+: Ready to return and compete for first team place
- 55–74: Ready to return as squad player / rotation
- 35–54: Another loan window recommended
- <35: Loan not working — reassess pathway (loan elsewhere / sell)

### Step 4 — New Club Adaptation Index (TAI)
For players who transferred within the last 6 months:

```
TAI = (
  minutes_trend (weeks 1-4 vs weeks 8-12) * 0.30 +  # manager trust building?
  PI_trend (same window)                   * 0.25 +  # improving or declining?
  error_rate_trend                         * 0.20 +  # costly mistakes reducing?
  community_integration_signals            * 0.15 +  # social, language, local ties
  physical_load_adjustment                 * 0.10    # playing full matches?
) * 100
```

Context flags:
- Language barrier: overseas move → slower adaptation expected (add 4–8 week buffer)
- League physicality jump (e.g. Championship → Premier League): harder adaptation
- Manager rotation (manager changed since signing): reset adaptation clock
- Winter signing: no pre-season together → typically slower integration

### Step 5 — Youth Academy Pathway
For U21 and academy players:

**Development milestones:**
```
AGE-BASED BENCHMARKS:
  U17: Regular U18 minutes (>45min/match average) ✓/✗
  U18: U23/reserve minutes > 50% of available ✓/✗
  U19: First team involvement (training, bench, cup games) ✓/✗
  U21: 500+ first team minutes in senior professional football ✓/✗
  U23: Regular senior starter OR significant loan minutes ✓/✗
```

**Projection:**
Based on development velocity (DTS) + position + comparable player pathways:
```
potential_ceiling = current_PI_at_age × (development_velocity × remaining_development_years)
```
Flag: which comparable player does this athlete's profile most resemble at the same age?

### Step 6 — Injury Rehabilitation Progress
For players returning from injury (>4 weeks out):

**Rehabilitation phases:**
```
Phase 1 (0–30% return): Medical clearance, no contact training
Phase 2 (30–60%):       Ball work, individual training, load building
Phase 3 (60–80%):       Team training, limited contact
Phase 4 (80–100%):      Full training, available for selection
Phase 5:                Match sharpness recovery (typically 3–6 matches)
```

Signals from public data:
- Training ground sightings / photos (first appearance = Phase 3+)
- Manager press conference language: "day-to-day", "progressing well", "weeks away"
- Match squad involvement (bench inclusion = Phase 4 complete)
- Minutes management pattern on return (sub appearances, max 45min initially)

**Match sharpness forecast:**
After returning to play, expect PI recovery curve:
- Match 1–3: 15–25% below pre-injury PI (rust period)
- Match 4–8: 5–15% below (sharpening)
- Match 9–12: Return to baseline (if no setbacks)

### Step 7 — Professionalism Signal Assessment

These signals inform character and mentality — relevant for brand-score character premium
and for clubs assessing cultural fit:

**Positive signals:**
- Consistent training attendance in public (club media, photographers)
- Positive specific manager quotes ("He sets the standard in training")
- Players publicly mentored by or mentioning this athlete as influence
- Voluntary community/charity activity (not just club-mandated)
- Consistent recovery routine visibility (gym posts, diet content)
- Returns from international duty on time, no controversies

**Negative signals:**
- Late or absent from pre-season (public reports)
- Training ground incidents (reported by credible sources)
- Club placing player on transfer list (signals squad harmony issue)
- Unusual agent hyperactivity (contract standoff signal)
- Social media activity inconsistent with injured/rehabilitating status
- Multiple manager or captain quotes avoiding or vague about player

**Professionalism Score (PS):**
```
PS = (positive_signal_count × 8) - (negative_signal_count × 15)
Clamped to 0–100. Weighted more negatively — one bad signal outweighs multiple positives.
```

### Step 8 — Format output

```
PERFORMANCE OFF-PITCH — [ATHLETE NAME]
Context: [Loan at CLUB B / Rehabilitation / New club adaptation / Development]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Development Trajectory Score (DTS):    74 / 100  [On track]
Professionalism Signal:                 Positive  (PS: 81)
Injury risk (load context):             Low — no recent injury history

[IF LOAN]
LOAN SPELL REPORT — [CLUB B]
  Loan purpose:           Development (regular minutes at Championship level)
  Minutes per match:      72 (80% of available minutes) ✓
  PI at loan club:        67 / 100 (71st pct for position in Championship) ✓
  Loan value score:       78 / 100 — loan working well
  Form trajectory:        Rising — best 5 games came in last 6 weeks ↑

  Return Readiness:       62 / 100  [Ready as squad player, not first-choice yet]
  Recommendation:         Complete this season at loan club. Review in summer.
                          If trajectory continues, return-and-compete probable.

[IF NEW CLUB]
ADAPTATION INDEX (TAI): 68 / 100  [Good adaptation — week 14 post-signing]
  Manager trust:          Growing (started 7 of last 9 matches)
  PI trend:               +11 points vs first 4 matches
  Key challenge:          Physical intensity step up — high-intensity distance
                          still 12% below squad median. Normal for this timeline.

PROFESSIONALISM SIGNALS
  Positive: 4 observed (specific manager praise × 2, community activity, early pre-season)
  Negative: None flagged
  Assessment: High character signal — consistent professional conduct

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Run performance-on-pitch for match stat validation
→ Professionalism score feeds brand-score character premium (+6 to ABS)
→ Run transfer-intelligence for loan-to-permanent pathway assessment
```

---

## Reference files

- `references/loan-case-studies.md` — Historical loan outcomes for calibration *(planned)*
- `references/transfer-adaptation-timelines.md` — Expected adaptation curves by transfer type
- `references/injury-phases.md` — Rehabilitation phase language patterns and timelines *(planned)*
- `references/youth-benchmarks.md` — Age-group development benchmarks by position *(planned)*

---

## Environment variables

```
RAPIDAPI_KEY=<key>              # API-Football
# Physical/GPS data requires direct club partnership agreements
# No standard commercial API available for training load
```
