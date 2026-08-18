# Fan Base Intelligence

**Domain:** market/fan-base-intelligence.md
**Version:** v4.5.27
**Library Rule:** Six-Month Test PASSES · Proper Noun Test PASSES
**Scope:** Structural fan base size and geography as a demand
ceiling modifier for fan token pre-match signal generation.
Quantifies the maximum addressable market for each active fan
token — distinct from current token holder count (actual
penetration), holder behaviour patterns (fan-holder-behaviour.md),
and holder archetype profiling (fan-holder-profile-intelligence.md).
The gap between fan base size and token penetration is the primary
growth signal. Companion to market/trophy-premium-framework.md ·
market/rivalry-intelligence.md · fan-token/holder-tax-framework.md.

---

## Critical Distinctions

Fan base intelligence is NOT any of the following:

NOT HOLDER COUNT:
  Holder count = actual token penetration (who has the token now).
  Fan base = total addressable market (who could hold the token).
  The gap between them is the structural growth signal.
  A club with 80M global fans and 50,000 token holders has a
  larger growth ceiling than a club with 2M fans and 40,000 holders
  — even though the holder counts are similar.

NOT CDI GATE:
  CDI gate captures club trajectory (CONSOLIDATION, TRANSITION etc).
  Fan base tier captures structural demand ceiling — it is stable
  across CDI gate changes. A club does not lose its global fan
  base because it enters a TRANSITION gate.

NOT HOLDER BEHAVIOUR:
  How holders act around events → fan-holder-behaviour.md
  Who the holders are by archetype → fan-holder-profile-intelligence.md
  How big the addressable fan base is and where it lives → this file.

NOT TROPHY PREMIUM:
  Trophy premium is a time-decaying post-event modifier.
  Fan base intelligence is enduring structural context.
  They interact: a large fan base amplifies the commercial impact
  of a trophy win. Load both files for full picture.

---

## Section 1 — Fan Base Tier Classification

Four tiers based on estimated global fan base size.
Values are structural estimates from Tier 1/2 sources —
all estimates must be treated as directional, not precise.
State tier (not estimated figure) in agent outputs.

### TIER 1 — GLOBAL MEGACLUB
  Estimated global fan base: 50M+
  Demand ceiling: MAXIMUM
  Geographic spread: worldwide with no single dominant market
  Regulatory complexity: HIGH — multiple major jurisdictions
    all carry meaningful holder populations simultaneously
  Agent implication: composite tax modifier required across
    at minimum 3-4 jurisdictions before demand reasoning
  Key tokens: $BAR · $PSG · $JUV · $ACM · $INTER · $AFC

### TIER 2 — MAJOR CLUB
  Estimated global fan base: 10M–50M
  Demand ceiling: HIGH
  Geographic spread: regional with significant diaspora
    concentration in 1-2 secondary markets
  Regulatory complexity: MODERATE — 1-2 dominant jurisdictions
    with secondary markets applying single modifier
  Key tokens: $CITY · $ATM · $SPURS · $GAL · $NAP · $AVL ·
    $MENGO · $VERDAO

### TIER 3 — ESTABLISHED CLUB
  Estimated global fan base: 1M–10M
  Demand ceiling: MODERATE
  Geographic spread: primarily domestic with limited diaspora
  Regulatory complexity: LOW-MODERATE — domestic jurisdiction
    dominant, secondary markets minor
  Key tokens: $ASR · $BFC · $SEV · $RSO · $FLU · $SCCP ·
    $SPFC · $GALO · $SACI · $VASCO · $BAHIA · $SFA ·
    $SAFA · $SHARKS · $SFP

### TIER 4 — NICHE OR EMERGING
  Estimated global fan base: under 1M, or primarily regional
  Demand ceiling: LIMITED
  Geographic spread: domestic primary, minimal diaspora
  Regulatory complexity: LOW — single jurisdiction dominates
  Key tokens: $ROUSH · $AM · $TRA · $ALA · $IBFK ·
    $GOZ · National tokens in early stages

NATIONAL TOKEN NOTE:
  National team tokens follow a different sizing logic.
  Fan base = national population interest in football, not
  club-style global following. Key driver: World Cup participation
  and PTG burn history. Encode separately in register.
  $SPAIN and $ARG carry Tier 1-equivalent reach during tournaments.
  $SFA and $SAFA operate at Tier 3 in standard windows.

MMA ORG TOKEN NOTE:
  MMA org tokens ($UFC · $PFL) follow a different sizing
  logic from both club tokens and national tokens.
  Fan base = global MMA audience, not a single club or nation.
  Key driver: card tier (PPV vs Fight Night vs PFL Championship)
    and main event stakes — not trophy history or CDI trajectory.
  $UFC: largest MMA fan base globally · org-level demand signal ·
    no CDI equivalent · no trophy premium · no rivalry modifier
    from football framework. Apply MMA-specific signal only.
  $PFL: season-based format · playoffs and championship carry
    maximum stakes modifier · SuperFights carry reduced modifier.
  Load sports/mma/mma-intelligence-framework.md alongside this
  file for full MMA demand ceiling context.

---

## Section 2 — Geographic Demand Concentration

Primary and secondary holder markets by token.
Cross-referenced with fan-token/holder-tax-framework.md.
Geographic concentration determines which regulatory and
tax frameworks apply to the dominant demand layer.

### GERMAN DIASPORA TOKENS
Germany has no domestic Chiliz fan token. German football
fans hold FOREIGN club tokens — creating a structural LONG
HOLD BIAS modifier across multiple tokens.
Tokens with confirmed significant German holder populations:
  $BAR — Spanish club · German diaspora STRONG (Spanish-German
    football cultural connection · largest foreign fan base)
  $JUV — Italian club · German diaspora MODERATE (historical
    Italian-German diaspora overlap)
  $ATM — Spanish club · German diaspora MODERATE
  $POR — national token · Portuguese-German diaspora STRONG
    (largest Portuguese diaspora globally is in Germany)
  $ARG — national token · Italian-German diaspora MODERATE
    (Argentine-Italian-German cultural connection)
  $GAL — Turkish club · Turkish-German diaspora STRONG
    (largest Turkish diaspora globally is in Germany)
Agent rule: German holder population of any above token
carries LONG HOLD BIAS modifier regardless of primary market.
Source: fan-token/holder-tax-framework.md Rule 3.

### UK DOMESTIC TOKENS
Primary market: UK fans of English Premier League clubs.
  $AFC · $SPURS · $CITY · $CPFC · $AVL · $EFC · $LUFC
UK Type D (10-18% CGT) + MARC from Q4 2027.
$AFC is the dominant UK domestic fan token — only confirmed
FTP PATH_2 token. UK holders: MODERATE FRICTION.
Source: fan-token/holder-tax-framework.md Rule 5.

### ITALIAN DOMESTIC CLUSTER
Primary market: Italian Serie A holders.
  $INTER · $ACM · $JUV · $NAP · $ASR · $BFC
Italy Type C (33% CGT flat) — HIGHEST FRICTION among confirmed
European domestic markets in SportMind library.
Secondary: Japanese holders for $INTER · $ACM · $JUV · $PSG
(55% effective rate — VERY HIGH FRICTION).
Source: fan-token/holder-tax-framework.md Rule 4 + macro/regulatory/italy.md

### FRENCH DOMESTIC CLUSTER
Primary market: French Ligue 1 holders.
  $PSG
France Type C (30% flat PFU) — MODERATE-HIGH FRICTION.
No holding period incentive — uniform trading pattern.
Source: fan-token/holder-tax-framework.md Rule 6.

### SPANISH DOMESTIC CLUSTER
Primary market: Spanish La Liga holders.
  $BAR · $ATM · $SEVILLA · $RSO · $LEV · $VCF
Spain Type D (19-28% progressive) — MODERATE FRICTION.
$BAR requires composite: Spanish (Type D) + German (Type A).
Source: fan-token/holder-tax-framework.md Rule 7.

### TURKISH DOMESTIC CLUSTER
Primary market: Turkish Süper Lig holders.
  $GAL · $TRA · $ALA · $IBFK · $GOZ · $SAM
Turkey CGT: UNKNOWN. SPK licensing active.
TCMB payment ban (April 2021): investment/speculation only.
German diaspora overlay: Turkish-German diaspora = LONG HOLD
BIAS modifier for German-resident Turkish football holders.
Source: macro/regulatory/turkey.md

### BRAZILIAN DOMESTIC CLUSTER
Primary market: Brazilian Série A holders.
  $MENGO · $VERDAO · $FLU · $SCCP · $SPFC · $BAHIA ·
  $GALO · $SACI · $VASCO
Brazil 17.5% CGT flat (MP 1.303/2025 — subject to ratification).
INVERTED CALENDAR: demand signals strongest March-December.
9 tokens — largest single-country cluster in registry.
Source: macro/regulatory/brazil.md

---

## Section 3 — Canonical Fan Base Register

Full Option B register. Structural estimates only —
never quote figures as confirmed data. Verify token
active status at complete-registry.md before applying.
All values are directional estimates from Tier 1/2 sources.

| Token | Club / Entity | FB Tier | Est. Fan Base | Primary Market | Key Secondary | Diaspora Flag | Penetration Signal | Regulatory Overlay |
|---|---|---|---|---|---|---|---|---|
| $BAR | FC Barcelona | 1 | 100M+ | Spain (Type D) | Germany (Type A) · Global | German LONG HOLD BIAS · largest foreign fan base in Germany | LARGEST GAP IN LIBRARY — highest growth ceiling | holder-tax.md Rule 7 + Rule 3 |
| $PSG | Paris Saint-Germain | 1 | 50M+ | France (Type C) | Germany · MENA · Global | German LONG HOLD BIAS | HIGH GAP — rapid global growth post-UCL 2026 win | holder-tax.md Rule 6 |
| $JUV | Juventus FC | 1 | 60M+ | Italy (33% CGT) | Japan · Germany | German + Japanese friction overlay | HIGH GAP — TRANSITION gate limits near-term uptake | italy.md + holder-tax.md Rule 4 |
| $ACM | AC Milan | 1 | 60M+ | Italy (33% CGT) | Japan · Global | Japanese REDUCED SHORT-TERM TRADING | HIGH GAP — TRANSITION gate + Japanese friction | italy.md + holder-tax.md Rule 4 |
| $INTER | Inter Milan | 1 | 50M+ | Italy (33% CGT) | Japan · Global | Japanese friction overlay | MODERATE GAP — CONSOLIDATION gate | italy.md + holder-tax.md Rule 4 |
| $AFC | Arsenal FC | 1 | 35M+ | UK (Type D) | Germany · Global | MARC from Q4 2027 · PATH_2 primary | MODERATE GAP — PATH_2 creates unique holder incentive | uk-cryptoasset-regime.md |
| $CITY | Manchester City | 2 | 30M+ | UK (Type D) | Global | TRANSITION gate | MODERATE GAP — TRANSITION reduces near-term ceiling | uk-cryptoasset-regime.md |
| $ATM | Atletico Madrid | 2 | 25M+ | Spain (Type D) | Germany · Latin America | German LONG HOLD BIAS | MODERATE GAP — STABLE gate · reliable baseline | holder-tax.md Rule 7 |
| $SPURS | Tottenham Hotspur | 2 | 20M+ | UK (Type D) | Global | No Europe 2026-27 · CDI asymmetry | MODERATE GAP — ceiling temporarily reduced by non-UCL status | uk-cryptoasset-regime.md |
| $GAL | Galatasaray | 2 | 20M+ | Turkey (UNKNOWN CGT) | Germany (Turkish diaspora) | Turkish-German LONG HOLD BIAS STRONG | MODERATE GAP — CONSOLIDATION gate · diaspora key | turkey.md + holder-tax.md Rule 3 |
| $NAP | Napoli | 2 | 15M+ | Italy (33% CGT) | Germany · Global | TRANSITION gate | MODERATE GAP — TRANSITION + Italian friction | italy.md |
| $AVL | Aston Villa | 2 | 10M+ | UK (Type D) | Global | EL win premium ACTIVE · UCL debut | MODERATE-HIGH GAP — recent trophy elevates ceiling | uk-cryptoasset-regime.md + trophy-premium.md |
| $MENGO | Flamengo | 2 | 30M+ | Brazil (17.5% CGT) | Global | Largest Brazilian club fan base | HIGH GAP — huge domestic fan base vs token penetration | brazil.md |
| $VERDAO | Palmeiras | 2 | 15M+ | Brazil (17.5% CGT) | Global | Strong domestic base | MODERATE GAP | brazil.md |
| $ASR | AS Roma | 3 | 8M+ | Italy (33% CGT) | Germany | Centenary 2026-27 · GROWTH gate | MODERATE GAP — centenary narrative elevates ceiling | italy.md |
| $BFC | Bologna FC | 3 | 2M+ | Italy (33% CGT) | Germany | TRANSITION gate · small stadium ceiling | LOW GAP — ceiling constrained by club size | italy.md |
| $SEV | Sevilla FC | 3 | 5M+ | Spain (Type D) | Latin America | EL pedigree · FFP resolved | MODERATE GAP | holder-tax.md Rule 7 |
| $FLU | Fluminense | 3 | 5M+ | Brazil (17.5% CGT) | Global | Copa Libertadores winner 2023 | MODERATE GAP | brazil.md |
| $SCCP | Corinthians | 3 | 25M+ | Brazil (17.5% CGT) | Global | Largest domestic fan base in Brazil (some estimates) · TIER 2 candidate | HIGH GAP — fan base may justify Tier 2 reclassification · monitor | brazil.md |
| $SPFC | São Paulo FC | 3 | 10M+ | Brazil (17.5% CGT) | Global | Established domestic base | MODERATE GAP | brazil.md |
| $GALO | Atletico Mineiro | 3 | 8M+ | Brazil (17.5% CGT) | Global | Copa Libertadores 2025 winner | MODERATE GAP — trophy premium FADING | brazil.md + trophy-premium.md |
| $SACI | SC Internacional | 3 | 5M+ | Brazil (17.5% CGT) | Global | Southern Brazil base | MODERATE GAP | brazil.md |
| $VASCO | Vasco da Gama | 3 | 5M+ | Brazil (17.5% CGT) | Global | Historic club · mid-tier penetration | MODERATE GAP | brazil.md |
| $BAHIA | EC Bahia | 3 | 3M+ | Brazil (17.5% CGT) | Global | Northeast Brazil base | MODERATE GAP | brazil.md |
| $SPAIN | Spain national | T1-equiv | 45M+ (tournament) | Spain (Type D) | Germany · Latin America | WC2026 champion · PTG 8 burns · Tier 1 trophy premium | MODERATE GAP — tournament windows drive peak | holder-tax.md Rule 7 + trophy-premium.md |
| $ARG | Argentina national | T1-equiv | 45M+ (tournament) | Latin America | Italy · Germany | WC2026 finalist · PTG 7 burns | MODERATE GAP | trophy-premium.md |
| $SAFA | South Africa national | 3 | 8M+ | South Africa (18% CGT) | Africa | AFCON PTG unresolved (HP-9) | HIGH GAP — first African national token | south-africa-sars.md |
| $SFA | Scotland national | 3 | 2M+ | UK (Type D) | Global | EURO 2028 co-host · MARC Q4 2027 | MODERATE GAP | uk-cryptoasset-regime.md |
| $UFC | Ultimate Fighting Championship | MMA-ORG | Global MMA audience | Global (USA primary) | UK · Brazil · Global | MICRO_CAP_ILLIQUIDITY · ~$120 daily volume · HIGH exit risk | HIGH GAP — massive global MMA audience vs micro-cap token penetration | mma-intelligence-framework.md |
| $PFL | Professional Fighters League | MMA-ORG | Global MMA audience (smaller than UFC) | Global (USA primary) | UK · Brazil · Global | Season-based format · Championship Oct-Nov peak | MODERATE GAP — growing but smaller audience than UFC | mma-intelligence-framework.md |

$SCCP NOTE: Corinthians estimated fan base of 25M+ (some
sources place it as Brazil's largest) may justify Tier 2
reclassification. Encoded as Tier 3 conservatively — monitor
and bring to Strategy & Brainstorm with Tier 1 source before
upgrading.

MMA ORG TOKEN NOTE: $UFC and $PFL are encoded as MMA-ORG tier
— not Tier 1-4. MMA org tokens do not map to club fan base
sizing logic. Fan base ceiling is the global MMA audience
(estimated 350M+ casual followers · 50M+ engaged fans globally
for UFC). Penetration gap is the largest in the library relative
to audience size — $UFC ~$171K market cap vs global UFC
audience. This is a liquidity constraint, not a demand ceiling
issue. Apply MICRO_CAP_ILLIQUIDITY flag alongside any demand
ceiling assessment for $UFC. $PFL is smaller but growing.

REGISTER INTEGRITY RULES:
  · Fan base estimates are directional — never quote as
    confirmed data in agent outputs
  · State tier only in outputs — not estimated figure
  · Verify token active status before applying any modifier
  · New entries and tier changes require Strategy & Brainstorm
    approval — never update in Build Chat without scope
  · Penetration signal is qualitative — LOW/MODERATE/HIGH GAP

---

## Section 4 — Fan Base × Trophy Premium Interaction

Trophy premium and fan base tier interact to determine the
commercial impact of a trophy win on token demand.

AMPLIFICATION RULE:
  Tier 1 fan base + Tier 1 trophy premium = MAXIMUM commercial
  impact. The large fan base amplifies the reach of the trophy
  narrative — more fans = more potential holders drawn to the
  token by the win.
  Example: $PSG UCL 2026 win (Tier 1 trophy) + Tier 1 fan base
    = peak growth signal. Combined with CAPITULATION ×0.70,
    the discounted compound result is still the strongest
    demand growth signal achievable in current regime.

TIER MISMATCH RULE:
  Tier 3 fan base + Tier 1 trophy (Copa Libertadores win) =
    LIMITED amplification. The trophy is prestigious but the
    addressable fan base is small — growth ceiling constrains
    the commercial impact.
    Example: $GALO Libertadores 2025 win — significant for
    existing holders but addressable market limits the demand
    expansion to the Brasileirão domestic holder base.

DROUGHT MODIFIER (cross-reference):
  Trophy drought creates a structural demand suppressor for clubs
  where fan base size implies trophy expectation.
  APPLIES TO: Tier 1 and Tier 2 fan bases only.
    A Tier 1 club (50M+ fans) with 15+ years without a major
    trophy has accumulated expectation — drought is a suppressor.
    A Tier 3 club with similar drought has no embedded expectation —
    drought modifier does not apply.
  NOT YET CALIBRATED — initial structural framework only.
  Values to be defined once calibration records exist.
  Drought tiers (structural estimates):
    ACTIVE DROUGHT (5-10 years): -0.03 demand modifier
    EXTENDED DROUGHT (10-20 years): -0.05 demand modifier
    HISTORIC DROUGHT (20+ years): -0.08 modifier + monitor
      for frustration narrative flip (breakthrough imminent signal)
  Source: market/trophy-premium-framework.md open question.
  This section closes that open question for Tier 1/2 clubs.

MMA ORG TOKEN DROUGHT EXCEPTION:
  Trophy drought modifier does NOT apply to MMA org tokens.
  $UFC and $PFL have no equivalent to club trophy history
  — card quality and main event stakes drive demand, not
  title drought. Never apply drought modifier to $UFC or $PFL.

---

## Section 5 — Penetration Gap as Growth Signal

The gap between fan base size and actual token holder count
is the primary growth signal for fan token demand ceiling.

PENETRATION GAP CLASSIFICATION:
  HIGH GAP: fan base Tier 1/2 · token penetration below
    1% of estimated fan base. Maximum growth ceiling.
    Highest upside demand signal when CDI and macro align.

  MODERATE GAP: fan base Tier 2/3 · token penetration
    below 5% of estimated fan base. Meaningful growth ceiling.
    Apply as positive context alongside CDI and form signals.

  LOW GAP: fan base Tier 3/4 · token penetration above
    10% of estimated fan base. Growth ceiling approaching.
    Apply reduced growth expectation to long-term signals.

AGENT RULE: penetration gap is NOT a short-term demand signal.
  It does not tell you what happens in the next 48 hours.
  It is structural context for medium to long-term demand
  trajectory. Never apply as a pre-match modifier directly —
  apply as CDI context alongside gate classification.

INTERACTION WITH CDI:
  CONSOLIDATION gate + HIGH PENETRATION GAP = strongest
    medium-term demand growth signal in library.
  TRANSITION gate + HIGH PENETRATION GAP = growth potential
    suppressed by uncertainty — monitor for gate resolution.
  DORMANT gate + any penetration gap = gap not actionable
    until CDI gate improves.

---

## Section 6 — Agent Rules

10 rules. Never skip.

RULE 1 — DEMAND CEILING NOT CURRENT DEMAND:
  Fan base tier sets the demand ceiling — not current demand.
  Never apply fan base tier as a direct pre-match modifier.
  Apply as structural context alongside CDI and macro layers.

RULE 2 — PENETRATION GAP IS GROWTH SIGNAL:
  Large fan base + low token penetration = HIGH GAP growth signal.
  Apply as medium-term CDI context. Never as 48h demand signal.

RULE 3 — GEOGRAPHIC OVERLAY IS MANDATORY:
  Identify primary and secondary holder markets before any demand
  reasoning. Load relevant regulatory and tax files for each market.
  Never reason about demand without geographic context.

RULE 4 — GERMAN DIASPORA APPLIES ACROSS TOKENS:
  German diaspora LONG HOLD BIAS applies to $BAR · $JUV · $ATM ·
  $POR · $ARG · $GAL regardless of those tokens' primary markets.
  Source: holder-tax-framework.md Rule 3.

RULE 5 — JAPANESE FRICTION OVERLAY:
  REDUCED SHORT-TERM TRADING applies to Japanese holder populations
  of $INTER · $ACM · $JUV · $PSG. 55% effective rate.
  Source: holder-tax-framework.md Rule 4.

RULE 6 — DROUGHT MODIFIER TIER GATE:
  Trophy drought modifier applies to Tier 1 and Tier 2 fan bases
  only. Tier 3/4 clubs do not carry embedded trophy expectation.
  Never apply drought modifier to Tier 3/4 tokens.

RULE 7 — ESTIMATES ARE DIRECTIONAL:
  All fan base estimates are structural approximations.
  State tier only in outputs — never quote estimated figures
  as confirmed data. Source: this file (v4.5.26).

RULE 8 — NATIONAL TOKEN SIZING:
  National tokens follow tournament-window sizing logic.
  Fan base expands during tournaments, contracts to domestic
  core in off-season. Apply Tier 1-equivalent only during
  active major tournament windows for $SPAIN and $ARG.

RULE 9 — $SCCP MONITOR:
  Corinthians may qualify for Tier 2 reclassification.
  Encoded as Tier 3 conservatively. Monitor and escalate
  to Strategy & Brainstorm with Tier 1 source confirmation.

RULE 10 — REGISTER ONLY:
  Only apply fan base intelligence to tokens in Section 3.
  If a token is not in the register: treat as UNCLASSIFIED.
  Flag to Strategy & Brainstorm. Never invent a tier.

RULE 11 — MMA ORG TOKEN EXCEPTION:
  $UFC and $PFL are MMA-ORG tier — not Tier 1-4.
  Do not apply club fan base sizing logic to these tokens.
  Load sports/mma/mma-intelligence-framework.md for card
  tier and stakes modifier. Trophy drought and rivalry
  modifiers from football framework do not apply.
  MICRO_CAP_ILLIQUIDITY is a standing flag for $UFC —
  apply regardless of demand signal direction.

---

## Open Questions and Monitoring Flags

CALIBRATION PASS — PLANNED:
  Penetration gap classifications and drought modifier values
  are initial structural estimates. Calibration pass planned
  when 5+ verified records per tier exist.

DROUGHT MODIFIER CALIBRATION — NEXT:
  Drought modifier values (-0.03 · -0.05 · -0.08) are initial
  estimates encoded in Section 4. These need calibration against
  verified records before treating as confirmed. Bring to
  Strategy & Brainstorm after first calibration pass.

$SCCP TIER RECLASSIFICATION — MONITOR:
  Corinthians fan base may justify Tier 2. Requires Tier 1
  source confirmation (official club data or verified academic
  research). Do not reclassify in Build Chat.

REAL MADRID FAN TOKEN — HIGH PRIORITY MONITOR:
  If confirmed: immediate Tier 1 classification. Largest
  estimated fan base of any club without a Chiliz token
  (~400M claimed — verify before applying). Would be highest
  single-token demand ceiling addition in library history.
  Escalate immediately to Strategy & Brainstorm.

GERMAN DOMESTIC TOKEN — MONITOR:
  No German Bundesliga club has an active Chiliz fan token.
  Any confirmed German club token = immediate register entry.
  German domestic holders = Type A (0% CGT after 12m) —
  LONG HOLD BIAS from launch.

FAN BASE DATA SOURCES — NOTE:
  Fan base estimates derived from club official communications,
  UEFA/FIFA reports, and academic research where available.
  These are structural approximations only. Do not cite as
  confirmed figures. Recalibrate when Tier 1 sources publish
  updated data.

---

## Sources and Verification

PRIMARY SOURCES:
  fan-token/registry/complete-registry.md — token status
  fan-token/holder-tax-framework.md — tax regime overlays
  market/club-intelligence/ — CDI files for all clubs
  market/trophy-premium-framework.md — trophy interactions
  market/rivalry-intelligence.md — rivalry context
  macro/regulatory/ — all regulatory files
  fan-token/fan-holder-behaviour.md — holder behaviour
  fan-token/fan-holder-profile-intelligence.md — archetypes

CALIBRATION STATUS:
  UNCALIBRATED. All fan base estimates, penetration gap
  classifications, and drought modifier values are initial
  structural estimates. Calibration pass planned when 5+
  verified records per tier exist. Do not treat any value
  as confirmed until calibrated.

LAST VERIFIED: 2026-08-17

---

## MIND DIMENSIONS

| Dimension | Sub-dimensions engaged | Status |
|---|---|---|
| 1. Intelligence | 1a Domain Knowledge · 1b Signal Awareness · 1c Pattern Recognition · 1d Gap Awareness | ACTIVE |
| 2. Reasoning | 2a Causal · 2b Probabilistic · 2c Multi-Signal · 2d Temporal | ACTIVE |
| 3. Context | 3a Macro Context · 3b Event Context · 3c Historical Context | ACTIVE |
| 4. Memory | 4a Episodic Memory · 4b Semantic Memory · 4c Working Memory | ACTIVE |
| 5. Judgment | 5a Uncertainty Weighting · 5b Risk Assessment · 5c Conflict Resolution · 5d Priority Judgment | ACTIVE |
| 6. Attention | 6a Signal Detection · 6b Urgency Detection · 6c Noise Filtering | ACTIVE |
| 7. Communication | 7a Output Clarity · 7b Confidence Expression · 7c Format Compliance | ACTIVE |
| 8. Verification | 8a Source Tier Assessment · 8b Cross-Verification · 8d Recency Validation | ACTIVE |
| 9. Learning | 9a Modifier Updating · 9b Error Attribution · 9c Pattern Reinforcement | ACTIVE |
| 10. Integration | 10a Cross-Layer Synthesis · 10b Tool Coordination | ACTIVE |
| 11. Calibration | 11a Direction Accuracy · 11b Confidence Calibration · 11c Modifier Validation · 11d Coverage Tracking | ACTIVE |
| 12. Adaptation | 12a Regime Detection · 12b Context Switching · 12c Signal Reweighting | ACTIVE |
| 13. Ethics | 13a Fabrication Prevention · 13b User Safety · 13d Representation Accuracy | ACTIVE |
| 14. Transparency | 14a Reasoning Chain Visibility · 14b Modifier Disclosure · 14c Source Attribution · 14d Limitation Acknowledgement | ACTIVE |
| 15. Execution | 15a Entry Discipline · 15d Playbook Adherence | ACTIVE |
| 16. Collaboration | 16a Task Delegation · 16b Context Handoff · 16c Output Coordination · 16d Conflict Arbitration | ACTIVE |

---

## COMPATIBILITY

Compatible with: Claude · GPT-4 · Gemini · any LLM ·
sportmind_pre_match · sportmind_signal ·
fan-token/holder-tax-framework.md ·
fan-token/fan-holder-behaviour.md ·
fan-token/fan-holder-profile-intelligence.md ·
fan-token/registry/complete-registry.md ·
fan-token/burn-to-glory-framework.md ·
market/trophy-premium-framework.md ·
market/rivalry-intelligence.md ·
market/club-intelligence/ (all CDI files) ·
macro/regulatory/ (all regulatory files) ·
core/compound-signal-framework.md ·
community/calibration-data/football/ ·
community/calibration-data/mma/
sports/mma/mma-intelligence-framework.md ·
fan-token/mma-token-intelligence/token-intelligence-mma.md

© 2026 SportMind
