# SportMind Testing Scenarios

Forward-looking validation playbooks. Use these to verify that your SportMind
integration is producing correct reasoning before deploying in production.

Each scenario provides inputs, the correct SportMind reasoning chain, and the
expected output. Run your agent against these inputs. Compare its output to the
expected output. If they match, your integration is working correctly.

---

## How to use these scenarios

```
1. Copy the "AGENT INPUTS" section into your agent as the user query
2. Make sure you have loaded the correct SportMind skills (see "Skills to load")
3. Run your agent
4. Compare the output to "EXPECTED CORRECT OUTPUT"
5. Grade using the "PASS CRITERIA" checklist

A score of 7/7 on pass criteria = integration working correctly
A score of 4–6/7 = partial integration; identify which criteria fail
A score < 4/7 = review skill loading order; likely missing a key file
```

---

## Scenario T1 — Football pre-match: rivalry with congestion

**Difficulty:** Intermediate
**Skills to load:**
- `sports/football/sport-domain-football.md`
- `athlete/football/athlete-intel-football.md`
- `core/core-athlete-modifier-system.md`
- `core/core-fixture-congestion.md`
- `core/core-narrative-momentum.md`
- `core/confidence-output-schema.md`

**Agent inputs:**
```
Manchester City vs Manchester United, Premier League, Sunday 4pm kick-off.

Manchester City context:
- Playing their third match in 8 days (Tier 2 congestion)
- Kevin De Bruyne: DOUBT (hamstring, 60% fit — journalist report, unverified)
- Erling Haaland: CONFIRMED fit, 4 goals in last 3 games (HOT form)
- Manager confirmed "strong squad" at press conference (indirect)
- Base signal score from platform: 68

Manchester United context:
- Last match was 6 days ago
- Bruno Fernandes: CONFIRMED, AVERAGE form
- Squad fully available

Additional context:
- This is a Manchester derby
- City haven't lost at home to United in 4 Premier League matches
```

**Expected correct output:**

```
REASONING CHAIN:
1. Derby identification: Manchester derby = rivalry modifier active
   → Form differential discount: 40% of standard form signal
   → Adjusted form advantage for City: reduced

2. Congestion check: 3 matches in 8 days = Tier 2 (×0.93)
   → City team-level congestion modifier: 0.93

3. Athlete modifier for City:
   De Bruyne DOUBT (journalist, unverified): ×0.85 × source reliability 0.60 = ~0.91
   Haaland CONFIRMED HOT form: ×1.10
   Combined (non-knockout): composite around 1.00–1.02

4. Narrative check: "City haven't lost at home in 4" = streak narrative
   → Apply mild positive narrative modifier: +3% (record proximity, 5 away = notable)
   → Moderate category (not Category 1): 30% weight = +1%

5. Composite modifier calculation:
   base 68 × congestion(0.93) × athlete(~1.01) × narrative(~1.01) ≈ 64.8

EXPECTED OUTPUT:
  base_score: 68
  adjusted_score: 64–66 range
  direction: HOME (City favoured, reduced conviction)
  confidence_tier: MEDIUM
  flags:
    congestion_warning: true
    lineup_unconfirmed: true (De Bruyne doubt, source unverified)
    narrative_active: true
  reasoning:
    primary_signal_driver: "Congestion (Tier 2) compresses City advantage; derby form discount applied"
    risk_factors: ["De Bruyne doubt unverified", "Derby effect reduces form differential"]
  sizing:
    recommended_action: ENTER (or WAIT if preferred until De Bruyne confirmed)
    position_size_pct: 55–70% (medium confidence + congestion warning)
```

**Pass criteria (check 7/7 for full pass):**
- [ ] Derby modifier applied (form differential discounted)
- [ ] Congestion modifier applied (×0.93 or equivalent reduction)
- [ ] congestion_warning flag set TRUE
- [ ] lineup_unconfirmed flag set TRUE (De Bruyne unverified source)
- [ ] adjusted_score LOWER than base_score (congestion and derby compress it)
- [ ] confidence_tier MEDIUM (not HIGH — two active flags prevent HIGH)
- [ ] position_size_pct < 100% (active flags constrain sizing)

---

## Scenario T2 — MMA fight week: weigh-in miss

**Difficulty:** Advanced
**Skills to load:**
- `sports/mma/sport-domain-mma.md`
- `athlete/mma/athlete-intel-mma.md`
- `core/injury-intelligence/injury-intel-mma.md`
- `core/confidence-output-schema.md`

**Agent inputs:**
```
UFC 300 main event: Alex Pereira (champion) vs Jamahal Hill (challenger)

Wednesday weigh-in results:
- Pereira: 204.5 lbs (makes weight comfortably, Light Heavyweight limit 205 lbs)
- Hill: 207.8 lbs — MISSES weight by 2.8 lbs
  Hill given one hour to cut remaining weight
  After one hour: Hill at 207.0 lbs — STILL misses, bout proceeds at catchweight
  Hill penalised 20% of purse; title cannot change hands

Fight context:
- Both fighters confirmed healthy going into fight week
- Hill has a history of weight cut issues (missed weight once before in UFC)
- Pereira is a KO specialist (92% finish rate)
- Base signal score from platform: 72 (Pereira favoured)
```

**Expected correct output:**

```
REASONING CHAIN:
1. Weigh-in analysis:
   Hill misses by 2.8 lbs, still 2 lbs over after one hour
   → Severe weight cut: body has been dehydrated significantly
   → Historical weight cut issue: elevated risk marker
   
2. Weight miss modifier (from MMA domain skill):
   Severe miss (>2 lbs over after cut period): ×0.72–0.75 for Hill
   Title cannot change hands: Hill has reduced motivation (cannot win belt)
   Combined Hill modifier: ≈ ×0.72

3. Pereira modifier: No negative factors; challenger is weakened
   → Pereira modifier: slight positive ≈ ×1.08 (opponent compromised)

4. Signal adjustment:
   Base 72 (Pereira) × Pereira modifier(1.08) = ~78
   Hill's weight miss acts as opposing team negative, amplifying Pereira signal

EXPECTED OUTPUT:
  base_score: 72
  adjusted_score: 77–80
  direction: HOME (Pereira, champion favoured significantly)
  confidence_tier: HIGH
  flags:
    injury_warning: false
    lineup_unconfirmed: false
  reasoning:
    primary_signal_driver: "Hill severe weight miss (2.8 lbs over) with historical cut issues"
    supporting_factors: ["Title cannot change hands (Hill reduced motivation)", 
                         "Pereira KO specialist vs compromised opponent"]
    risk_factors: ["Hill may have rehydrated unusually fast (some fighters recover well)"]
  sizing:
    recommended_action: ENTER
    position_size_pct: 85–95%
  token_signal:
    token_direction: POSITIVE (for Pereira-linked assets)
    token_signal_strength: STRONG
```

**Pass criteria:**
- [ ] Weight miss identified as significant negative modifier for Hill
- [ ] Historical weight cut issue flagged as additional risk marker
- [ ] Title cannot change hands noted (motivation impact)
- [ ] adjusted_score HIGHER than base_score (opponent compromise amplifies signal)
- [ ] confidence_tier HIGH (weight miss is a concrete confirmed signal)
- [ ] position_size_pct > 80% (high confidence, concrete information)
- [ ] token_signal direction POSITIVE for Pereira (if token exists)

---

## Scenario T3 — Fan token with DeFi liquidity constraint

**Difficulty:** Advanced
**Skills to load:**
- `fan-token/fan-token-why.md`
- `fan-token/fan-token-pulse/`
- `fan-token/football-token-intelligence/`
- `fan-token/defi-liquidity-intelligence/`
- `core/confidence-output-schema.md`

**Agent inputs:**
```
Scenario: Barcelona vs Real Madrid, El Clásico, Champions League quarter-final, 
first leg, 9pm CET.

$BAR token data:
  Current price: $3.42
  24h volume (Binance): $2.1M
  HAS score: 0.78 (healthy holder activity)
  TVI: 0.65 (moderate velocity)
  
DEX liquidity check:
  Chiliz DEX $BAR/CHZ pool TVL: $340,000
  GeckoTerminal shows: $BAR/USDC Uniswap (bridged): TVL $89,000
  Primary DEX pool combined: ~$430,000
  Estimated slippage on $15,000 trade: 3.5%
  
Match context:
  Base signal score: 74 (Barcelona at home favoured)
  El Clásico = rivalry match (Tier 1 narrative)
```

**Expected correct output:**

```
REASONING CHAIN:
1. Liquidity assessment:
   Primary trading is CEX (Binance $2.1M/day volume) — CEX is source of truth
   DEX pools are supplementary, NOT primary venue for $BAR
   BUT: $15k trade at 3.5% slippage exceeds 3% threshold → liquidity_critical
   
2. Signal calculation:
   Base 74 + El Clásico narrative (+5% Category 1 rivalry) = ~78
   HAS 0.78 = healthy; TVI 0.65 = moderate; no negative on-chain signal
   
3. Liquidity override:
   Even though signal is HIGH confidence (78, high HAS, rivalry amplified),
   liquidity_critical flag OVERRIDES to max 20% position size
   This is the key test: signal quality does not override liquidity reality

EXPECTED OUTPUT:
  base_score: 74
  adjusted_score: 77–79
  direction: LONG ($BAR token)
  confidence_tier: HIGH (signal quality)
  flags:
    liquidity_critical: true  ← CRITICAL: this is the pass/fail flag
    narrative_active: true
  defi_context:
    primary_venue: CEX
    pool_tvl_usd: 430000
    estimated_slippage_pct: 3.5
    lp_activity_signal: NEUTRAL
  reasoning:
    primary_signal_driver: "El Clásico UCL QF amplified by high HAS and clean on-chain state"
    risk_factors: ["DEX slippage 3.5% exceeds threshold; position size constrained by liquidity"]
  sizing:
    recommended_action: ENTER (but heavily size-reduced)
    position_size_pct: 20  ← CRITICAL: must be max 20% due to liquidity_critical
```

**Pass criteria:**
- [ ] liquidity_critical flag set TRUE (slippage 3.5% > 3% threshold)
- [ ] position_size_pct at or below 20% (liquidity override applies)
- [ ] adjusted_score still reflects HIGH quality signal (77–79 range)
- [ ] confidence_tier HIGH (signal quality separate from execution constraint)
- [ ] defi_context object populated with TVL and slippage values
- [ ] Narrative modifier applied for El Clásico (adjusted_score > base_score)
- [ ] CEX identified as primary venue (not DEX — this is an active partnership token)

---

## Scenario T4 — Cricket: DLS event mid-match

**Difficulty:** Intermediate
**Skills to load:**
- `sports/cricket/sport-domain-cricket.md`
- `core/core-weather-match-day.md`
- `core/confidence-output-schema.md`

**Agent inputs:**
```
IPL 2024: Mumbai Indians vs Chennai Super Kings
Wankhede Stadium, Mumbai, 7:30pm IST evening match

Pre-match:
  Base signal: 60 (even match)
  Dew forecast: HIGH (tropical evening venue, humidity 82%)
  Toss: Mumbai Indians win toss and choose to FIELD FIRST
  Agent pre-match assessment: CSK batting first disadvantaged by dew (×0.88)

Match situation (in-progress — Rain interruption):
  CSK innings: 18 overs completed, 147/4
  Rain stops play; 4 overs lost
  DLS revised target: Mumbai Indians need 142 from 16 overs
  
New assessment needed: Has the DLS event changed the match dynamics?
```

**Expected correct output:**

```
REASONING CHAIN:
1. Pre-match assessment is now SUPERSEDED by DLS event
   → Create a new confidence output object for the revised match

2. DLS target analysis:
   Original par: CSK 147 in 20 = 7.35 runs/over
   Mumbai target: 142 in 16 overs = 8.875 runs/over required
   DLS has SET a challenging but achievable target
   
3. Dew factor: Still applies to Mumbai's chase
   16 overs starting around 9pm+ = FULL dew advantage for Mumbai batting
   Dew modifier for chasing team: +10–12% applies (tropical evening venue)
   
4. Revised signal:
   Slightly higher run rate required (×0.95) but dew advantage (×1.10)
   Net: Mumbai advantage from dew exceeds the DLS rate challenge
   Signal shifts TOWARD Mumbai (chasing team with dew)

EXPECTED OUTPUT:
  NOTE: New confidence output generated; prior analysis superseded
  base_score: 55 (reset; match situation rebaselined)
  adjusted_score: 60–65 (dew advantage for Mumbai offsets run rate)
  direction: HOME/CHASE (Mumbai Indians)
  confidence_tier: MEDIUM (DLS adds variance; weather can still change)
  flags:
    weather_risk: false (rain has passed; dew now the factor)
  reasoning:
    primary_signal_driver: "DLS target achievable + dew advantage strongly favours Mumbai chase"
    supporting_factors: ["Tropical evening = full dew for entire chase"]
    risk_factors: ["DLS targets are approximations; actual required rate above CSK's pace"]
  note: "Pre-match analysis SUPERSEDED. Generate new output object for DLS match."
```

**Pass criteria:**
- [ ] Explicitly notes that pre-match analysis is superseded by DLS event
- [ ] Creates a NEW confidence output (not modifies old one)
- [ ] Dew factor still applied to the chase (tropical evening + dew)
- [ ] Adjusted signal SHIFTS toward chasing team (Mumbai)
- [ ] confidence_tier MEDIUM (DLS variance acknowledged)
- [ ] DLS target analysis included (run rate comparison)
- [ ] weather_risk flag correctly set FALSE (rain has passed; dew is separate)

---

## Scenario T5 — Macro override: crypto bear market signal

**Difficulty:** Beginner
**Skills to load:**
- `macro/macro-overview.md`
- `macro/macro-crypto-market-cycles.md`
- `core/confidence-output-schema.md`

**Agent inputs:**
```
Macro environment check before placing any fan token positions today.

Current market data:
  BTC price: $38,500
  BTC 200-day moving average: $46,200
  CHZ price: $0.071
  CHZ 30-day average: $0.095 (CHZ down 25% in 30 days)
  BTC/CHZ 90-day correlation: 0.82

Question: Should the macro modifier be applied today?
What modifier, and what does it mean for fan token positions?
```

**Expected correct output:**

```
REASONING CHAIN:
1. BTC vs 200-day MA check:
   BTC at $38,500 vs 200-day MA $46,200
   BTC is 16.7% BELOW its 200-day MA
   → Crypto bear market confirmed (BTC below 200-day MA)

2. CHZ confirmation:
   CHZ down 25% in 30 days; tracking BTC (0.82 correlation confirms)
   → CHZ in bear market conditions

3. Macro modifier selection:
   Crypto bear market (BTC below 200-day MA): ×0.75
   NOT extreme bear (would require capitulation; -40%+ from peak or BTC <$25k range)

4. Application:
   Apply ×0.75 multiplier to ALL fan token signal scores today
   This does NOT affect prediction market positions (different asset class)

EXPECTED OUTPUT:
  macro_override_active: true
  macro_modifier: 0.75
  macro_category: "Crypto bear market"
  
  Example application:
    Any fan token signal of 70 → 70 × 0.75 = 52.5 → confidence_tier: LOW
    Any fan token signal of 80 → 80 × 0.75 = 60 → confidence_tier: MEDIUM
    Any fan token signal of 90 → 90 × 0.75 = 67.5 → confidence_tier: MEDIUM
    
  Recommendation: Reduce all fan token position sizes. Strong sporting signals
  can still justify entry but at reduced size due to macro headwind.
  Prediction market positions not affected by this modifier.
```

**Pass criteria:**
- [ ] BTC below 200-day MA correctly identified as bear market signal
- [ ] Correct modifier selected: ×0.75 (bear, not extreme bear)
- [ ] macro_override_active flag set TRUE
- [ ] Modifier applied to fan token signals (any sport)
- [ ] Prediction markets explicitly noted as NOT affected
- [ ] position size reduction recommended (bear market = reduced conviction)
- [ ] CHZ confirmation used to validate BTC signal (0.82 correlation)

---

## Grading your integration

```
INTEGRATION HEALTH SCORING:

Run all 5 scenarios. Score each on its 7-point checklist.

35/35: Full pass — integration is production ready
28–34: Strong — minor calibration needed on specific modifier calculations
21–27: Partial — likely missing a core file or misapplying one modifier type
14–20: Weak — review skill loading order and modifier pipeline
<14:  Restart — fundamental integration issue; work through agent-prompts/ first

COMMON FAILURE PATTERNS:

"Adjusted score is always the same as base score"
  → Not loading or applying core-athlete-modifier-system.md correctly

"Liquidity flags never trigger"  
  → Not loading defi-liquidity-intelligence; or not running pre-execution check

"Confidence tier is always HIGH"
  → Not processing flag states before determining tier

"DLS scenario produces same output as pre-match"
  → Agent not detecting mid-match event; add event detection to workflow

"Macro modifier not applied"
  → Not loading macro-overview.md; or loading but not checking BTC vs 200-day MA
```

---

*Run these scenarios before deploying any SportMind-based agent in production.*

*See `examples/worked-scenarios/` for historical examples showing correct SportMind
reasoning applied to real past events.*

*MIT License · SportMind · sportmind.dev*
