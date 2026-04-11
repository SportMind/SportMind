---
name: pre-match-squad-intelligence
description: >
  The assembly layer for pre-match squad status intelligence. Pulls from
  core/injury-intelligence/, core/athlete-disciplinary-intelligence.md,
  core/core-fixture-congestion.md, core/media-intelligence.md, and
  platform/social-intelligence-connector.md to produce one coherent
  pre-match squad brief covering who is starting, who is doubtful, who
  is out and why, when they return, what the manager said, and what the
  social signal shows. Load alongside sport-specific athlete intel and
  injury intelligence files. Applies to all team and individual sports
  with squads, rosters, or fight cards. Used by Pattern 2 (Pre-Match
  Chain), Pattern 11 (Post-Match Analysis), and Prompt 21/22.
---

# Pre-Match Squad Intelligence — SportMind

**Everything a SportMind agent needs to know about who is available,
who is not, why, when they return, and what the manager is signalling —
assembled into one coherent brief before kickoff.**

The individual intelligence layers exist across multiple files. This skill
is the assembly layer: it defines the workflow for pulling them together,
the output schema for the squad brief, and the sport-specific intelligence
notes that make the brief accurate across football, MMA, cricket, basketball,
hockey, rugby, tennis, and more.

---

## Why a dedicated assembly layer

Without this layer, agents and developers have to know which of six files to
load, in what order, and how to synthesise them. That is friction that produces
incomplete squad briefs — the most common failure mode in SportMind pre-match
analysis.

The four things agents most commonly miss without this layer:

```
1. RETURN-FROM-INJURY IMPAIRMENT
   A player who is "fit and available" after a 10-week hamstring injury is
   not the same player they were before the injury. They are underperforming
   for 6-10 matches. The availability check says CONFIRMED; the signal says
   apply × 0.82 for the first 3 matches.

2. MANAGER LANGUAGE AMBIGUITY
   "He's back in full training" means 50-70% availability, not confirmed fit.
   Agents that treat this phrase as CONFIRMED are applying the wrong modifier.
   The football injury file has the full decoder; this skill applies it.

3. SUSPENSION ACCUMULATION PROXIMITY
   A key midfielder on 4 yellow cards is one booking away from a 1-match ban.
   This is not an injury, not a flag, not a press conference signal — it is
   a computable risk that agents should track and report pre-match.

4. SQUAD DEPTH CONTEXT
   Losing the same position affects different teams differently. A top-6 club
   missing their left back has cover. A bottom-3 club missing their only left
   back has an emergency converted midfielder filling in. The injury is the
   same; the signal is completely different.
```

---

## The squad brief assembly workflow

```
STEP 1 — CONFIRMED ABSENCES (from official sources)
  Sources: official club X/social account, official league injury list
  Timeline: T-72h to T-2h (update at each window)
  Output:   List of confirmed OUT players with:
              injury_type, tier (A/B/C), estimated_return, source_tier
  
  SUSPENSION ABSENCES (distinct from injury):
  Sources: official league disciplinary records, core/athlete-disciplinary-intelligence.md
  Include: ban_type, matches_remaining, return_match_date
  
  AGENT RULE: Never mix injury and suspension in the same modifier.
    Injury → applies athlete availability modifier
    Suspension → applies DSM modifier (different pipeline)

STEP 2 — DOUBTFUL PLAYERS (press conference signal)
  Sources: manager press conference (T-72h to T-24h), The Athletic, BBC Sport
  Decode:  Apply Manager Language Decoder (see below) to convert phrase → probability
  Output:  List of DOUBT players with:
              availability_probability (%), source, phrase_used, decoded_meaning
  
  SUSPENSION PROXIMITY (yellow card accumulation):
  Compute: How many yellows does each key player have this season?
           What is the threshold for the next automatic ban?
  Flag:    If key player is 1 yellow from ban → suspension_proximity_flag = True

STEP 3 — FITNESS CURVE ADJUSTMENT (return-from-injury players)
  Sources: core/injury-intelligence/injury-intel-{sport}.md
           core/injury-intelligence/core-injury-intelligence.md
  Apply:   If player has returned within last 6 matches from Tier B/C injury:
             Apply return-to-play curve modifier (first match back = impaired)
             See sport-specific file for position-specific curves
  Output:  AVAILABLE_IMPAIRED status with curve_modifier and matches_remaining

STEP 4 — PHYSICAL LOAD CHECK
  Sources: core/core-fixture-congestion.md, athlete/{sport}/ physical_load
  Flag:    Any player with 3+ high-intensity matches in 7 days
  Flag:    International duty players (travel, time zone, fixture overlap)
  Output:  HIGH_LOAD players with fatigue_index

STEP 5 — REPLACEMENT QUALITY DELTA
  Sources: core/injury-intelligence/core-injury-intelligence.md Step 5
  Compute: For each confirmed OUT player: who is their replacement?
           What is the quality gap between starter and replacement?
  Output:  RQD score per absence (0.00 = no loss, 0.55+ = structural problem)

STEP 6 — SOCIAL AND MEDIA SIGNAL
  Sources: platform/social-intelligence-connector.md
           core/media-intelligence.md
  Check:   X API — volume of injury/team news discussion last 4h
           LunarCrush — Galaxy Score movement vs baseline
           Late breaking news — any changes since press conference?
  Output:  SOCIAL_SIGNAL: STABLE | ELEVATED_CONCERN | BREAKING_UPDATE

STEP 7 — ASSEMBLE SQUAD BRIEF
  Combine all above into structured output (see schema below)
  Generate two formats:
    Technical: full JSON with all modifiers (for agents/developers)
    Plain English: readable brief (for fan token holders, via Prompt 21/22)
```

---

## Manager language decoder — multi-sport

### Football / Soccer

```
PRESS CONFERENCE PHRASE → AVAILABILITY PROBABILITY:

"He'll be fine, just a knock"              → 85–95%  (minor, almost certainly playing)
"We'll assess him in the morning"          → 40–60%  (genuine doubt, 50/50)
"He won't be available for selection"      → 0%      (definite out)
"He's working hard in training"            → 5–15%   (not fit, not playing yet)
"We'll make a late decision"               → 40–65%  (unknown / opponent deception)
"He's not quite ready"                     → 0–20%   (returning but won't be rushed)
"We have to be careful with him"           → 15–30%  (recurrence risk concern)
"He's back in training with the group"     → 20–40%  (weeks from match fitness)
"He's back in full training"               → 50–70%  (close — 1-2 weeks likely)
"He looked sharp in training today"        → 70–85%  (likely playing)
"It's up to him to prove his fitness"      → 35–55%  (player willing, staff cautious)
"He came through training fine"            → 80–90%  (played, no reaction)
"There's no point risking him"             → 0–10%   (will be protected regardless)
"He's back but we won't rush him"          → 10–30%  (returning, bench at most)

SUSPENSION LANGUAGE:
"He's available" (when serving ban rumoured)  → verify disciplinary record independently
"He's not suspended" (manager claim)           → always verify via official source

AGENT RULE: Manager language is Tier 2. Always verify at Tier 1 (official
club account, league app) at T-2h before acting on any press conference signal.
```

### Basketball (NBA)

```
OFFICIAL DESIGNATION SYSTEM (act on immediately — Tier 1):

OUT (O)         → 0% availability. Do not modify signal — player is absent.
DOUBTFUL (D)    → 15–25% availability. Apply × 0.85 to team signal.
QUESTIONABLE (Q)→ 45–55% availability. Apply × 0.92 to team signal (hedge).
PROBABLE (P)    → 75–85% availability. Treat as CONFIRMED unless GTD.
GTD (Game-Time Decision) → Check 90 minutes before tipoff for update.

LOAD MANAGEMENT:
  REST designation:    Deliberate rest, not injury. No signal impact on health.
                       Commercial signal: reduced engagement for rested star.
  "DNP — Coach's Decision": may be disciplinary or tactical. Investigate.

NOTE: NBA injury report is the most structured official availability system
in major sports. Tier 1 from the moment it is published (Wednesday/Thursday
for weekend games, daily for back-to-back sequences).
```

### Ice Hockey (NHL)

```
MORNING SKATE PROTOCOL (primary availability signal):

Starter on ice, full drills:       lineup_unconfirmed = False → CONFIRMED
Starter absent from skate:         ≠ OUT. Usually resting. PROBABLE.
Backup takes all repetitions:      lineup_unconfirmed = True → backup starting

OFFICIAL DESIGNATIONS:
IR (Injured Reserve):              Minimum 7 days out. Apply full absence modifier.
LTIR (Long-Term IR):               Minimum 24 days / 10 games. Tier B/A injury likely.
Day-to-Day (DTD):                  Short-term, often concealed. Apply × 0.88 if key player.

COACH LANGUAGE:
"We'll wait and see after skate"   → 40–65% (GTD equivalent)
"He's a game-time decision"        → 40–65%
"He won't play tonight"            → 0%
"He looked good out there"         → 80–90%

KEY SIGNAL: The backup goaltender starting pre-warmup repetitions
is the highest-confidence NHL lineup signal. Do not wait for confirmation.
```

### Cricket

```
SQUAD AND AVAILABILITY SIGNALS:

OFFICIAL SQUAD ANNOUNCEMENT (T-24h via ESPNcricinfo):
  Squad named → primary source. Player not in squad = OUT.
  Playing XI not announced until toss (T-0).

REST / WORKLOAD MANAGEMENT (distinct from injury):
  "Rested for this series"  → Available next series. No injury concern.
  "Managing his workload"   → Possibly will play; board/coach decision.
  "Precautionary"           → Minor concern, available if needed.

INJURY SIGNALS (coach press conference T-24h):
  "Fitness test this morning"  → 30–60% — genuine doubt
  "He's not 100%"              → 15–40% — likely rested
  "He bowled in the nets"      → 50–70% for bowlers specifically

WORKLOAD NOTES:
  - Fast bowlers: overs bowled last 7 days is the primary load signal
  - Batters: rarely managed for load; injury signals are genuine
  - T20 specialists may be excluded from Test squads (selection, not injury)

RETURN FROM INJURY:
  First match back → apply × 0.88 (batting) / × 0.82 (fast bowling)
  Fast bowlers returning from side strain: high recurrence risk (30-40%)
  Apply × 0.85 for 3 matches regardless of reported fitness
```

### MMA / Boxing

```
FIGHT CONFIRMATION SIGNALS (see core/injury-intelligence/injury-intel-mma.md):

CONFIRMED FIGHTING:
  Made weight at official weigh-in: CONFIRMED.
  SEVERE weight cut (>8% body weight): Apply weight cut modifier (0.72–0.85)

LATE REPLACEMENT SIGNALS:
  Fight announced < 2 weeks before event: REPLACEMENT FLAG.
  Apply: × 0.80 (short camp) to × 0.65 (< 1 week notice, weight class jump)

FIGHT WEEK LANGUAGE:
  "I'm 100%" (fighter statement)         → Weight poorly — fighters always say this.
                                            Check weight cut history, not statement.
  "Camp has been perfect"                → Standard. Verify via sparring partner posts.
  "A few niggles but nothing serious"    → 60–80% chance of fight proceeding normally.
  "I'm not sure he can make weight"      → opponent statement → high credibility signal.
  Promoter: "there are no injury concerns" → Tier 3 only — promoter interest in fight proceeding.

AGENT RULE: In MMA/boxing, official fight confirmation comes at weigh-in.
All pre-fight camp signals are Tier 2-3. Treat fight as confirmed until
official withdrawal; apply modifiers for camp quality, not withdrawal risk.
```

### Rugby (Union and League)

```
TEAM ANNOUNCEMENT (T-48h for Test matches, T-24h for club):

OFFICIAL DESIGNATION:
  Named in starting XV/XIII: CONFIRMED (unless late withdrawal)
  Named on bench: Available. Starting probability 0%.
  Not in 23/squad: OUT for this match.

COACH LANGUAGE:
  "He's in contention"              → 40–65% (shortlist, not confirmed)
  "We'll see how he pulls up"       → 30–55% (post-match fatigue assessment)
  "He'll be fine for the weekend"   → 70–85%
  "He's carrying something"         → 15–35% (playing hurt / risk managed)
  "It's a suspension-free game for us" → verify card counts independently

CITING RISK (post-match, pre-next-fixture):
  Players cited after last match: suspension decision within 48h.
  Flag: any player with citing pending → suspension_pending_flag = True
  Apply: × 0.50 to that player's availability until citing resolved

NOTE: Rugby has the most complex citing and disciplinary system of any
sport in this library. Always check citing commissioner decisions
(World Rugby / RFL / PRO14) as a separate signal to team announcements.
```

### Tennis

```
PRE-MATCH FITNESS SIGNALS:

OFFICIAL WITHDRAWAL (tournament website, ATP/WTA):
  Withdrawal confirmed → player out, walkover or replacement.
  Late withdrawal (< 1h before match): rare but follow ATP/WTA social channels.

PRACTICE SESSION SIGNALS:
  Player visible practicing: PROBABLE (cannot confirm fitness fully)
  Player absent from practice: mild concern — could be tactical rest
  Player practicing with heavy strapping/taping: DOUBT — monitor

COACH AND PLAYER LANGUAGE:
  "I'm not 100% but I'll give it my best"  → Retirement risk 25–40% mid-match
  "I had to retire in practice yesterday"   → High withdrawal risk
  "Just some fatigue from the last match"   → Usually plays; reduced modifier × 0.92
  "My {body part} has been troubling me"    → Research specific injury type; apply RTP curve

RETIREMENT RISK MODIFIER:
  If player has retired mid-match in last 3 tournaments: × 0.85 (retirement risk)
  Apply to first set prediction; reduce through match as player proves fitness
```

---

## Squad brief output schema

```json
{
  "squad_brief": {
    "token":       "AFC",
    "team":        "Arsenal",
    "opponent":    "Bournemouth",
    "competition": "Premier League",
    "kickoff":     "2026-04-11T14:00:00Z",
    "generated_at": "2026-04-11T10:30:00Z",
    "source_window": "T-4h"
  },

  "confirmed_absent": [
    {
      "player":           "Gabriel Jesus",
      "position":         "ST",
      "absence_type":     "INJURY",
      "injury_type":      "ACL",
      "injury_tier":      "A",
      "estimated_return": "2026-12-01",
      "matches_remaining": null,
      "source":           "official_club_x",
      "source_tier":      1,
      "rqd":              0.40,
      "plain_english":    "Jesus is out long-term (ACL). Out for the rest of the season."
    },
    {
      "player":           "Thomas Partey",
      "position":         "CM",
      "absence_type":     "SUSPENSION",
      "ban_type":         "yellow_card_accumulation",
      "matches_remaining": 1,
      "return_match":     "next_fixture",
      "source":           "premier_league_official",
      "source_tier":      1,
      "plain_english":    "Partey is suspended — picked up his 5th yellow last week."
    }
  ],

  "doubtful": [
    {
      "player":             "Bukayo Saka",
      "position":           "RW",
      "availability_pct":   60,
      "source":             "press_conference",
      "source_tier":        2,
      "manager_phrase":     "We'll make a late decision",
      "decoded_meaning":    "Genuine doubt — manager doesn't know or keeping opponent guessing",
      "verify_at":          "T-2h via @Arsenal official account",
      "plain_english":      "Saka is 50/50. Arteta wouldn't commit. Check Arsenal's official account at 12pm."
    }
  ],

  "available_impaired": [
    {
      "player":          "Declan Rice",
      "position":        "CM",
      "injury_history":  "hamstring_grade2",
      "matches_since_return": 2,
      "return_curve_modifier": 0.90,
      "matches_remaining_on_curve": 4,
      "plain_english":   "Rice is back and playing but still building back to full sharpness — he's on his second game back from a hamstring issue."
    }
  ],

  "high_load_flags": [
    {
      "player":       "Martin Odegaard",
      "flag":         "HIGH_LOAD",
      "context":      "3 matches in 8 days including international duty",
      "fatigue_index": 0.78,
      "plain_english": "Odegaard has played a lot of football recently — watch if he's managed in this one."
    }
  ],

  "suspension_proximity": [
    {
      "player":       "Gabriel Magalhaes",
      "yellow_cards": 4,
      "threshold":    5,
      "gap":          1,
      "flag":         "ONE_YELLOW_FROM_BAN",
      "plain_english": "Gabriel is on 4 yellows — one more and he misses the next game. Worth watching if he's cautious in the tackle today."
    }
  ],

  "social_signal": {
    "status":            "ELEVATED_CONCERN",
    "driver":            "High volume of Saka injury discussion on X — 47 posts last 2h",
    "galaxy_score_delta": -3,
    "breaking_update":   false,
    "plain_english":     "A lot of noise about Saka on social media. Nothing confirmed yet but worth keeping an eye on the official account."
  },

  "composite_squad_modifier": 0.86,
  "modifier_drivers": [
    "Saka doubt (−0.06 weighted)",
    "Rice return curve (−0.04)",
    "Odegaard high load (−0.03)",
    "Jesus long-term absent (absorbed by RQD 0.40 already in baseline)"
  ],

  "plain_english_summary": "Arsenal are without Jesus long-term (ACL) and Partey (suspended). The big question mark is Saka — Arteta wouldn't commit at the press conference. Rice is playing but still finding his form after a hamstring injury. Check the official Arsenal account around 12pm for the confirmed lineup."
}
```

---

## Sport-specific squad intelligence notes

### When squad intelligence matters most (priority by sport)

```
FOOTBALL — Very high
  Lineup is the single highest-impact pre-match variable.
  The goalkeeper position alone can shift the modifier by ×0.12-0.22.
  Load: full squad brief at T-48h, update at T-2h.

NBA / BASKETBALL — Very high
  Structured injury report (Q/D/O) is the most reliable availability
  system in sport. Acts as Tier 1 from publication.
  Star player load management is as important as injury.
  Load: check official injury report Thursday/Friday; GTD at T-90min.

NHL / ICE HOCKEY — Very high for goaltenders specifically
  Morning skate is the primary signal window.
  Non-GK injuries are Tier B/C; GK injury is always Tier A in NHL context.
  Load: morning skate report T-3h to T-1h.

RUGBY UNION / LEAGUE — High
  Team of 23 announced T-48h for Test / T-24h for club.
  Citing (post-match discipline) creates unique pre-match uncertainty.
  Load: official team announcement + citing commissioner check.

CRICKET — Moderate (team sports variable; individual variable)
  Squad announced T-24h; playing XI at toss (T-0).
  Workload management (resting) is more common than injury.
  Fast bowler overs count is primary load variable.
  Load: squad announcement + T-0 toss update.

MMA / BOXING — Fight confirmation at weigh-in
  All pre-weigh-in squad intelligence is Tier 2-3.
  Fight card status: confirmed / replacement / cancelled.
  Load: fight camp signals through camp; definitive at official weigh-in.

FORMULA 1 — Low (drivers rarely unavailable)
  Grid penalty is the primary availability-adjacent signal (not injury).
  Reserve driver activation is rare but significant when it occurs.
  Load: official FIA entry list for grid penalties; driver fitness only if crash.

TENNIS — Individual; low frequency but high when active
  Official withdrawal is Tier 1. Practice signals are Tier 2.
  Retirement risk mid-match is a unique signal type.
  Load: draw/schedule check + practice session reports if concern flagged.
```

---

## Integration with SportMind patterns and prompts

```
PATTERN 2 (Pre-Match Chain):
  Load this skill at T-48h and again at T-2h.
  T-48h: manager language decoder, confirmed absences, doubtful list
  T-2h:  update with official lineup confirmation
  Connection: squad_modifier feeds directly into adjusted_score calculation

PATTERN 11 (Post-Match Analysis):
  After full-time: update return timelines for newly injured players
  Add any new suspensions (red cards, citing)
  Update yellow card counts
  Feed into next Pattern 2 cycle via Memory MCP

PATTERN 9 (Governance Delegate):
  Player signing votes: cross-reference APS against this skill's
  return-from-injury curves. A player returning from ACL has reduced
  APS for first 12 matches — governance brief should note this.

PATTERN 10 (Scouting Agent):
  Injury history is an input to DTS (Development Trajectory Score).
  Players with recurring Tier B injuries have elevated TAI risk.
  Scouting brief should include last 24-month injury record.

PROMPT 21 (Fan-facing pre-match brief):
  plain_english_summary from this skill feeds directly into the
  "WHAT TO CHECK BEFORE KICKOFF" section of the fan brief.

PROMPT 22 (Pre-match build-up agent):
  This skill is the primary source for the squad section of the build-up.
  Load alongside social-intelligence-connector.md for the full picture.
```

---

## Connecting the data sources

```
CONFIRMED ABSENCES:
  Football:    Official club X/social → Tier 1
  NBA:         NBA.com injury report → Tier 1
  NHL:         NHL.com injured reserve → Tier 1
  Rugby:       Official team announcement (World Rugby / club site) → Tier 1
  Cricket:     ESPNcricinfo squad page → Tier 1
  MMA:         UFC.com/PFL card page → Tier 1

DOUBTFUL / PRESS CONFERENCE:
  All sports: Official club/team press conference (YouTube, X)
  Football T-72h to T-24h: manager availability press conference
  NBA:        Post-practice availability interviews
  NHL:        Post-practice media availability (T-24h)
  Rugby:      Head coach pre-match press conference (T-48h)
  MMA:        Open workout (T-5 days), fighter media day (T-4 days)

SOCIAL INTELLIGENCE:
  All sports: platform/social-intelligence-connector.md
  Primary:    Official team/club X accounts
  Secondary:  Beat reporters (Tier 2)
  Tertiary:   Fan accounts, aggregators (Tier 3-4 — noise detection only)

INJURY CLASSIFICATION:
  core/injury-intelligence/core-injury-intelligence.md (all sports)
  core/injury-intelligence/injury-intel-{sport}.md (sport-specific)

DISCIPLINARY / SUSPENSION:
  core/athlete-disciplinary-intelligence.md (all sports)
  Official governing body pages (Tier 1 for suspensions)
```

---

*SportMind v3.49 · MIT License · sportmind.dev*
*See also: core/injury-intelligence/ · core/athlete-disciplinary-intelligence.md*
*core/media-intelligence.md · platform/social-intelligence-connector.md*
*core/core-fixture-congestion.md · core/verifiable-sources-by-sport.md*
*Patterns: 2 (Pre-Match Chain), 11 (Post-Match Analysis)*
*Prompts: 21 (Fan Brief), 22 (Pre-Match Build-Up Agent)*
