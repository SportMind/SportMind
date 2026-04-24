# MMA Statistics Intelligence — SportMind Sub-Module

**Status: CORE** — Sub-module of `sport-domain-mma.md`. Load alongside the
main domain skill when fighter statistics are available.
$UFC is an active Chiliz fan token — statistics directly inform CDI signals.

Zero-dependency. Agents source data from UFC Stats (free) or their chosen
provider. See Data Sources.

---

## Overview

MMA statistics are unusually predictive at the individual level because they
capture technical skills that are stable across fights. A fighter's striking
accuracy doesn't change week to week. Their takedown defence percentage reflects
years of training that cannot be erased by a single loss.

The critical distinction from team sports: **in MMA, athlete statistics carry
100% of the statistical modifier weight**. There is no team to distribute the
signal across. This makes individual fighter statistics more powerful — and
more dangerous when used without context.

Load `core/match-statistics-intelligence.md` for universal modifier framework.

---

## Domain Model

### Statistics hierarchy for MMA signal impact

```
TIER 1 — OUTCOME-CORRELATED (apply as primary modifiers):

  SIGNIFICANT STRIKES LANDED PER MINUTE (SLpM):
    The most stable individual striking metric.
    Tier 1 because it correlates directly with finish rate and decision win rate.
    > 5.0 SLpM: elite striker — apply × 1.10 to striking finish probability
    3.5–5.0 SLpM: above average — apply × 1.05
    < 2.5 SLpM: low volume striker — apply × 0.92 (higher decision risk)

  STRIKING ACCURACY (significant strikes landed / attempts):
    > 55%: elite accuracy — apply × 1.08 (accuracy predicts damage output)
    45–55%: average accuracy — neutral modifier
    < 40%: below average — apply × 0.94

  STRIKING DEFENCE (% of significant strikes absorbed):
    > 65% defence: elite defensive skills — apply × 1.08 to durability signal
    55–65%: average — neutral modifier
    < 50% defence: takes high volume — apply × 0.90 durability signal

  TAKEDOWN ACCURACY (takedowns landed / attempted):
    > 50% accuracy: elite takedown capability — apply × 1.10 for grappling finish
    35–50%: average — neutral modifier
    < 30%: telegraphed takedowns — apply × 0.88 (sprawl-and-brawl risk)

  TAKEDOWN DEFENCE (% of opponent takedowns stopped):
    > 75% defence: elite sprawl — apply × 1.08 to signal vs takedown-heavy opponents
    60–75%: average — neutral modifier
    < 50% defence: takedown-vulnerable — apply × 0.88 vs high-volume wrestlers

TIER 2 — CONTEXTUAL STATISTICS:

  TOTAL STRIKES ATTEMPTED PER MINUTE:
    Volume indicator — meaningful only with accuracy and damage context.
    High volume + high accuracy = elite striker. High volume + low accuracy
    = sloppy but active (potential fatigue indicator in later rounds).

  SUBMISSION ATTEMPTS PER 15 MINUTES:
    High attempt rate + low success rate: predictable submission game — opponent adapts.
    High attempt rate + high success rate: genuine submission threat.
    Apply as Tier 1 equivalent only when success rate > 30%.

  KNOCKDOWN RATE:
    Knockdowns per 15 minutes. Volatile but high-signal when non-zero.
    > 0.5 knockdowns/15min: power threat — apply × 1.12 to finish probability.

TIER 3 — DESCRIPTIVE:
  Total fight time (useful for career durability context, not individual fight signal)
  Win streak length without quality-adjusted opponent analysis
  Number of finishes without style-matchup context
```

### Weight cut intelligence

```
WEIGHT CUT — MMA'S UNIQUE PRE-FIGHT VARIABLE:

  Already documented in sport-domain-mma.md (Weigh-In Risk section).
  This section extends it with statistical grounding.

  WEIGHT CUT SEVERITY INDICATORS:
    Making weight comfortably (< 0.5% above limit at earliest weigh-in):
      No modifier applied. Standard statistics proceed.
    
    Struggling to make weight (0.5–2% above limit at earliest weigh-in):
      Apply × 0.92 to all performance statistics. Dehydration affects output.
    
    Extreme cut (> 2% above limit, multiple sauna sessions, IV drip reported):
      Apply × 0.80 to all performance statistics.
      Category 2 breaking news event. Load breaking-news-intelligence.md.
    
    MISSED WEIGHT:
      Apply × 0.72 to all performance statistics.
      Category 1 breaking news event — signal rebuild required.
      $UFC token: missed weight is a CDI negative event (professionalism signal).
      Load breaking-news-intelligence.md immediately.

  REHYDRATION ADVANTAGE:
    A fighter who cuts significant weight and rehydrates can enter the cage
    physically larger than their opponent who fights at their natural weight.
    Monitor: weight-day vs fight-day reported sizes where available.
    Rehydration advantage in grappling-heavy matchups: × 1.06 grappling signal.

REACH AND PHYSICAL STATISTICS:
  Reach advantage > 4 inches: × 1.05 striking modifier (range control advantage)
  Reach disadvantage > 4 inches: × 0.96 striking modifier
  Height differential > 4 inches: context-dependent by style (striker vs grappler)
  Apply physical modifiers only when combined with Tier 1 statistical advantage.
```

### Matchup-specific intelligence

```
STYLE MATCHUP MATRIX (most predictive H2H framework in MMA):

  Striker vs Wrestler:
    Striker: prioritise striking stats (SLpM, accuracy, knockdown rate)
    Wrestler: prioritise takedown accuracy and control time
    Decisive factor: wrestler's takedown accuracy vs striker's takedown defence
    If striker's TD defence > 75% AND striking SLpM > 4.0: apply × 1.10 striker
    If wrestler's TD accuracy > 50% AND control time > 3 min avg: apply × 1.10 wrestler

  Striker vs Striker:
    Apply SLpM differential as primary modifier
    Reach advantage becomes decisive at equal striking metrics
    Knockout history: both fighters with > 50% KO rate — high volatility × 0.85 confidence
    
  Grappler vs Grappler:
    Submission accuracy becomes Tier 1
    Cardio statistics (output in rounds 3-5 vs rounds 1-2) indicate conditioning
    Control time differential: > 2 min avg advantage = × 1.08

  Orthodox vs Southpaw:
    Stance mismatch historically produces 8–12% upset rate above expected
    Apply × 0.94 to favourite signal when style-orthodox faces style-southpaw
    This is one of the most stable cross-style modifiers in MMA statistics

  FIGHT CAMP INTELLIGENCE:
    Camp change for this fight (confirmed): × 0.88 statistics confidence
    Reason: training camp change affects established patterns. Statistics
    from previous camp may not reflect current technical state.
    Verified same camp, long-term training (5+ fights): full weight statistics.
```

### Career state and trajectory

```
CAREER STATE MODIFIERS:

  PRIME (24–32 for most combat sports, style-dependent):
    Full statistical weight. Peak athleticism + technical experience aligned.
    
  EARLY CAREER (< 10 professional fights):
    Apply 0.70× weight to all career statistics.
    Small sample, rapid development — historical stats are quickly outdated.
    
  VETERAN (> 35 years, or > 8 years professional):
    Apply 0.85× weight to recent positive statistics.
    Career durability is real but physical decline is also real.
    Monitor: rounds 3-5 performance vs rounds 1-2 (conditioning decline signal).
    
  RECENT STOPPAGE LOSS (last fight ended by KO/TKO to the head):
    Apply × 0.90 confidence modifier to all statistics.
    Chin damage is not reflected in statistics — this is a qualitative risk flag.
    Two consecutive KO/TKO losses to the head: × 0.80 confidence modifier.
    
  RETURN FROM LONG LAYOFF (> 18 months):
    Apply × 0.85 to all statistics as predictive inputs.
    Ring rust and potential physical decline not captured in historical stats.
    First fight back: treat as partial data until in-cage performance confirmed.

  TITLE CONTENDER PRESSURE (first title shot):
    Historical record shows underperformance on first title shot vs expectations.
    Apply × 0.94 to favourite signal for first-time title challengers.
    Not applicable to current champions defending or repeat challengers.
```

---

## Event Playbooks

### Playbook 1: Pre-fight statistical analysis
```
trigger:  Fight card confirmed with opponents named (typically 8 weeks out)
timing:   T-8 to T-1 weeks
protocol:
  1. Pull career statistics for both fighters (last 10 fights minimum)
  2. Run five-question protocol from match-statistics-intelligence.md
  3. Apply style matchup matrix
  4. Calculate statistical advantage by category (striking, grappling, cardio)
  5. Apply career state modifiers if applicable
  6. Generate pre-fight signal with statistical_edge field populated
output:   Pre-fight signal noting which category of advantage is most decisive
note:     This is the highest-confidence point for MMA statistics — before fight
          week variables (weight cut, camp reports) complicate the picture
```

### Playbook 2: Fight week statistical adjustment
```
trigger:  Fight week begins (Monday before UFC event)
timing:   Monday–Friday fight week
protocol:
  1. Monitor weigh-in reports and early morning weigh-in numbers
  2. Apply weight cut modifier if severity indicators present
  3. Check for camp change confirmation (social media, press conference)
  4. Reduce statistics confidence if camp change confirmed (× 0.88)
  5. Final weigh-in: apply missed weight protocol if applicable
output:   Fight week adjusted signal. Flag any weight cut concerns.
note:     Fight week often changes the signal more than the fight-day result
```

### Playbook 3: Title fight signal
```
trigger:  UFC title fight (main event)
timing:   Full pre-fight + fight week protocol
protocol:
  1. Full statistical analysis (Playbook 1)
  2. Apply first-title-shot modifier for challenger if applicable (× 0.94)
  3. Check champion's last 3 title defences — pattern analysis
  4. Apply championship pressure context to CDI calculation
  5. For $UFC token: title fight is highest CDI event of calendar year
note:     $UFC token CDI extension for title fight win: maximum window
          Load fan-token/mma-token-intelligence/ for full $UFC protocol
```

### Playbook 4: Post-fight statistical update
```
trigger:  Fight result confirmed
timing:   Immediately post-fight (within 30 min of result)
protocol:
  1. Update statistical profile with confirmed fight data
  2. Check: did the result match the statistical prediction? Log outcome.
  3. If KO/TKO finish: apply chin damage flag for future signals
  4. CDI extension or contraction calculation per result
  5. Contribute to SportMind calibration record if pre-submitted
output:   Post-fight updated signal with calibration note
```

---

## Signal Weight Adjustments

For MMA statistics sub-module — adds to the `sport-domain-mma.md` weights:

| Statistical modifier | Weight | Cap |
|---|---|---|
| SLpM differential (Tier 1) | 14% additional weight | ±8 pts |
| Striking accuracy differential | 8% additional weight | ±5 pts |
| Takedown matchup (accuracy vs defence) | 8% additional weight | ±5 pts |
| Weight cut severity | 6% additional weight | ±6 pts (negative only) |
| Career state modifier | 4% additional weight | ±4 pts |
| Stance mismatch | 3% additional weight | ±3 pts |

**Combined MMA statistical modifier cap: ±12 points on adjusted_score.**

---

## Autonomous Execution

**Trigger conditions:**
- Early weigh-in report showing fighter above weight limit
- Official weigh-in result: missed weight or expressed concern
- Fight camp change confirmed (social media / press conference)
- Fight result confirmed (post-event CDI update)

**Execution at autonomy Level 2:**
- Weigh-in concern: apply weight cut modifier. Notify with severity classification.
- Camp change: apply 0.88× confidence flag. Notify operator.
- Fight result: recalculate CDI with result modifier. Notify.

**Execution at autonomy Level 3–4:**
- Auto-monitor UFC official social media for early weigh-in numbers
- Missed weight: trigger Category 1 RELOAD protocol automatically
- Post-fight: auto-update statistical profile and CDI within 30 min of result

**Hard boundaries:**
- Missed weight is always Category 1 — requires human review of new signal
- KO/TKO finish to the head: apply chin damage flag for ALL future signals
  This flag persists until manually cleared by operator (after 2+ confirmed wins)
- Weight cut severity from Tier 2 source only: reduce confidence by additional 0.90×

---

## Key Commands

| Action | Command | Notes |
|---|---|---|
| Pre-fight analysis | Load this + sport-domain-mma.md | 8 weeks out |
| Fight week update | Playbook 2 | Monday–Friday fight week |
| Title fight | Playbook 3 + mma-token-intelligence | $UFC CDI protocol |
| Weigh-in response | Playbook 2 + breaking-news | Missed weight = Category 1 |

---

## Agent Reasoning Prompts

- "Style matchup first: striker vs wrestler is more predictive than raw statistics alone."
- "Missed weight: Category 1 event. Reload signal from scratch with × 0.72 modifier."
- "Southpaw vs orthodox: apply × 0.94 to favourite — stance mismatch is a stable modifier."
- "Recent KO/TKO loss to head: chin concern flag. Apply × 0.90 confidence across all stats."
- "First title shot: apply × 0.94 challenger modifier — consistent historical pattern."

---

## Data Sources

- UFC Stats (free): ufcstats.com — official career and fight statistics (Tier 1)
- Tapology (free): tapology.com — records, rankings, weigh-in results (Tier 2)
- MMA Decisions (free): mmadecisions.com — judging history, decision analysis (Tier 2)
- FightMetric: fightmetric.com — official UFC data provider (Tier 1 via UFC Stats)
- Sherdog: sherdog.com — career records (Tier 2 — verify against UFC Stats)

---

## Compatibility

**Load alongside:** `sports/mma/sport-domain-mma.md`
**Universal framework:** `core/match-statistics-intelligence.md`
**Fan token layer:** `fan-token/mma-token-intelligence/token-intelligence-mma.md`
**Athlete layer:** `athlete/athlete-modifier-mma.md`
**Breaking news:** `core/breaking-news-intelligence.md` (missed weight = Category 1)

---

*SportMind v3.89.0 · MIT License · sportmind.dev*
