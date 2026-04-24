# Cricket — SportMind Domain Skill

Sport-specific intelligence for cricket. Covers all three international formats
(Test, ODI, T20I) and major domestic leagues (IPL, The Hundred, BBL, PSL, CPL, SA20).

---

## Overview

Cricket has three distinct formats played by the same players but with completely
different token and prediction dynamics. The format must be identified before any
analysis begins. Additionally, the pitch type, toss outcome, and dew factor can
shift match probabilities more than team quality differences in many contests.

---

## Domain Model

### Format classification — the essential first step

| Format | Duration | Character | Token behaviour |
|---|---|---|---|
| Test | 5 days, 2 innings | Most analytical; narrative builds over days | Slow-building; series wins are sustained events |
| ODI (50-over) | 1 day | Single result; 6–8h | Moderate volatility per match |
| T20 / T20I | 3–4 hours | Highest volatility; entertainment-first | Fastest, largest per-match token moves |
| IPL | T20 franchise | Biggest cricket event globally | Franchise-specific; star player driven |

### Competition tier classification

**Tier 1:**
- ICC T20 World Cup (every 2 years, Oct-Nov) — highest T20 event
- ICC Cricket World Cup / ODI WC (every 4 years) — highest ODI event
- The Ashes (Eng vs Aus, every 2 years) — highest Test series
- ICC World Test Championship Final (every 2 years)
- IPL — Indian Premier League (annual, Mar-May)

**Tier 2:** ICC Champions Trophy, bilateral T20 series (major nations), Test series
(Top 6 nations), Big Bash League (BBL), The Hundred

**Tier 3:** PSL, CPL, SA20, ILT20

---

## Pitch and Conditions — the dominant variable

### Pitch type classification

```
BATTING PITCH (flat, true bounce):
  Favours: batters; high scores
  T20 typical: 180–220 | ODI typical: 320–370
  Toss: either choice viable

BOWLING / SEAM PITCH (green, damp, variable bounce):
  Favours: pace bowlers; low scores
  T20 typical: 130–160 | ODI typical: 220–270
  Toss: WIN and BOWL — use movement while pitch is fresh

SPIN PITCH (dry, dusty, turning):
  Favours: spin bowlers; gets harder to bat as match progresses
  Toss: WIN and BAT — score before pitch deteriorates
  Key question: which team has the better spin attack?

UNKNOWN / COVERED PITCH (first use):
  Highest variance — price wider ranges
  Watch first 3 overs for swing/seam clues
```

### Dew factor — the most underpriced variable in cricket

```
What it is: Moisture settling on the outfield in evening sessions
Why it matters: Wet ball doesn't swing or grip — batting becomes significantly
                easier in the second innings

When it applies:
  Evening T20 matches (after ~6pm local), tropical/subtropical venues
  High-risk venues: Eden Gardens (Kolkata), Wankhede (Mumbai), Lahore,
  Colombo, Bridgetown, Dubai, Abu Dhabi
  Minimal effect: UK, Australia, South Africa

Magnitude:
  Dew present:       Second innings bat = +15–20 run advantage
  Heavy dew likely:  +20–30 run advantage

Agent rule: At dew-affected venues, toss winner bowls first.
  Team batting second has structural advantage.
  A team winning toss and choosing to bat first at a known dew venue
  is giving away significant advantage — flag as a risk signal.
```

---

## The Toss — signal and impact

```
TOSS IMPACT BY PITCH TYPE:
  Batting pitch (flat):         +8–12% win probability to toss winner
  Bowling / seam pitch:         +15–20% — bowls first (exploit fresh pitch)
  Spin pitch (dry, turning):    +20–30% — bats first (before pitch deteriorates)
  Dew expected (evening):       +20–25% — bowls first (bats second in dew)
  Unknown pitch:                moderate; read the choice itself as a signal

TOSS CHOICE SIGNALS:
  Toss winner bowls on flat pitch: unusual — they have pitch intelligence
  Toss winner bats on known spin pitch: possible misjudgement — flag
```

---

## India vs Pakistan — special treatment

The India vs Pakistan fixture in any format is the highest-viewership cricket event
and the only cricket match that generates football UCL Final-level token responses.

```
Agent rule: India vs Pakistan in any competition tier = ALWAYS treat as Tier 1.
  All other competition context is secondary for fan token purposes.
  This fixture generates ±15–35% token moves regardless of format.
  Token holders for both nations include the largest diaspora communities
  globally — the match is a cultural event, not just a sporting one.
```

---

## Event Playbooks

### Playbook 1: T20 — Post-Powerplay Entry
```
trigger:  First 6 overs (Powerplay) complete; score context established
entry:    Re-evaluate after seeing first innings scoring rate
exit:     End of first innings confirmation
filter:   Pitch playing as expected vs pre-match assessment
sizing:   1.0× — higher conviction than pre-match after powerplay confirms pitch
note:     The powerplay reveals true pitch conditions. Below expected = bowling
          pitch; above expected = batting pitch. Adjust accordingly.
```

### Playbook 2: T20 World Cup — Knockout Stage
```
trigger:  Team advances to Semi-Final or Final
entry:    Day after group stage qualification confirmed
exit:     Result of knockout match
filter:   Token HAS > 50 | Nation has strong token holder presence
sizing:   1.25× Semi-Final; 1.50× Final
note:     Highest FTIS events in cricket. India vs Pakistan group stage match
          exceeds these levels — treat separately as maximum signal event.
```

### Playbook 3: Test Series — Series Clinch
```
trigger:  Team takes unassailable series lead (e.g. 3-0 in 5-match series)
entry:    After clinching match completes
exit:     +72h (narrative peak)
filter:   Token holder base includes relevant national community
sizing:   1.25× home series; 1.10× away series (smaller audience)
note:     Test series wins are the longest-sustaining token signals in cricket.
          Ashes win in Australia: 5–7 day elevated HAS for England or Australia token.
```

### Playbook 4: IPL — Top-2 Establishment
```
trigger:  Franchise establishes top-2 position after 8+ league stage matches
entry:    After match confirming consistent position
exit:     Tournament end or team elimination
filter:   Franchise has associated token or high-ATM player in squad
sizing:   1.0× — IPL is franchise; national token correlation is lower
note:     IPL star player performance creates AELS for their national token,
          not the IPL franchise token. Track star player availability closely.
```

---

## Result Impact Matrix

| Result / Event | Token impact |
|---|---|
| T20I win (expected) | +3–6% |
| T20I win (upset vs top-3 nation) | +8–18% |
| T20 World Cup win | +25–50% |
| ODI World Cup win | +30–55% |
| Ashes win (away) | +20–40% |
| Test series win (home) | +10–22% |
| Key player injury mid-series | -8–20% |
| India vs Pakistan result (any format) | ±15–35% |
| Rain — match abandoned (important) | -3–8% |

---

## Sport-Specific Risk Variables

### Rain and Duckworth-Lewis-Stern (DLS)

```
HIGH RAIN RISK VENUES: Manchester, Dunedin (NZ), Colombo (monsoon)
LOW RAIN RISK: Dubai, Abu Dhabi, most Indian venues (dry season)

MATCH ABANDONMENT MINIMUM:
  T20: Below 5 overs = no result
  ODI: Below 20 overs = no result

Agent rule: At high-risk rain venues in wet season, reduce FTIS by 10–15 points
and reduce position sizing. Rained-off matches generate negative token sentiment
even without a result.
```

### Player rotation and format separation

Most top nations rotate squads across formats. Never assume a player's availability
in one format applies to another. Always confirm the specific squad for the format
being analysed.

---

## Signal Weight Adjustments

| Component | Weight | Rationale |
|---|---|---|
| Sports catalyst | 35% | Match result and conditions dominate |
| Price trend | 20% | Longer formats create trend opportunities |
| Market / whale | 20% | Informed money follows form closely |
| Macro | 10% | India market correlation during IPL window |
| Social sentiment | 15% | More analytical audience than contact sports |

---

## Agent Reasoning Prompts

```
1. IDENTIFY FORMAT FIRST. Test, ODI, T20 require completely different frameworks.

2. ASSESS PITCH TYPE. A spin pitch in Chennai is a different match to a seam
   pitch in Dunedin even with the same teams.

3. DEW FACTOR at evening matches in tropical venues shifts second innings
   advantage by +15–30 runs. Check venue, start time, and weather forecast.

4. THE TOSS is informative. Which choice the toss winner makes tells you
   something about what the pitch looks like to the captains.

5. INDIA vs PAKISTAN is always Tier 1 regardless of competition context.
   It is the only cricket match that generates UCL-Final-level token moves.

6. RAIN RISK must be assessed before any match at a high-risk venue.
```

---

## Injury Intelligence

Load `core/injury-intelligence/core-injury-intelligence.md` for the full injury
framework. Cricket-specific notes:
- Fast bowlers are most injury-prone: stress fractures (back), side strains
- Batter hand/finger injuries from pace bowling are common and often undisclosed
- Player rotation is often managed rest, not injury — distinguish carefully


---

## Key Commands

| Action | Skill | When to use |
|---|---|---|
| Domain intelligence | `sports/cricket/sport-domain-cricket.md` | Every analysis |
| Athlete modifier | `athlete/cricket/` | After domain load |
| Injury check | `core/injury-intelligence/core-injury-intelligence.md` | Injury concern |
| Market context | `market/market-cricket.md` | Commercial decisions |

## Data Sources

- **Primary:** ESPNcricinfo (espncricinfo.com)
- **Stats:** Statsguru (stats.espncricinfo.com)
- **Live:** Cricbuzz (cricbuzz.com)
- **Odds and prediction:** Betfair Exchange, Oddschecker


## Autonomous Execution

**Trigger conditions:**
- Evening T20 match scheduled + humidity forecast > 70% (dew protocol)
- Toss result confirmed: team elects to field first (dew signal)
- Rain interruption begins during match (DLS risk activation)
- Match result confirmed for CDI update
- India vs Pakistan fixture confirmed in any tournament draw

**Execution at autonomy Level 2:**
- Dew conditions met: apply dew modifier automatically. Flag DEW_PROTOCOL_ACTIVE. Notify.
- Toss field + evening + humidity: confirm and apply modifier. Notify.
- Rain begins: flag WEATHER_DLS_RISK. Reduce confidence. Notify operator.
- Match result: recalculate CDI. Notify.
- Ind vs Pak confirmed: activate dual-signal protocol. Notify.

**Execution at autonomy Level 3–4:**
- Auto-check humidity forecast at T-6h for ALL evening T20 matches
- Auto-apply dew modifier when both conditions met (calibrated 5/5 — high confidence)
- Auto-dispatch match result CDI updates within 20 min of confirmed result
- Dew confirmed in-match by commentary: auto-update with DEW_CONFIRMED_IN_MATCH flag

**Hard boundaries:**
- Dew modifier requires BOTH conditions: evening > 20:00 local AND humidity > 70%.
  Neither alone is sufficient. Both must be confirmed.
- India vs Pakistan × 2.00 CDI: applies to commercial signal ONLY.
  Never apply to match outcome prediction — they are entirely separate calculations.
- DLS scenario: all batting statistics carry 0.70× weight maximum. Hard floor.

---

## Compatibility

**Athlete intelligence:** `athlete/cricket/athlete-intel-cricket.md`
**Injury intelligence:** `core/injury-intelligence/core-injury-intelligence.md`

---

*MIT License · SportMind · sportmind.dev*
