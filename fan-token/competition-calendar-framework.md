# Fan Token Competition Calendar Framework

The competition calendar is a structural demand modifier. Fan token
demand signals operate within competition windows — and understanding
when those windows open and close is essential for correct signal
interpretation.

A pre-match PTG signal in February means something very different
for a Brazilian club token (off-season) than for a European club
token (mid-season). A Chilean fan token in November is in its
domestic playoff window. A Turkish fan token in June is in pre-season.

This framework documents the structural competition rhythm for active
fan token clusters. It covers domestic league seasons, continental
competition windows, and the intersections that create compound
signal opportunities.

**Scope:** Structural competition rhythms only. Specific fixtures,
dates, and results belong in SMI briefings — not the library.
Postponements and rescheduling are Type 5 Operational signals —
surface in SMI Section 1 as demand window reset signals.

---

## Partnership Verification Requirement

**This framework documents structural competition rhythms only.
It does not guarantee the current active status of any fan token.**

Partnership status changes independently of competition calendars.
A club may still be playing in its league while its Chiliz fan
token partnership has terminated.

Before applying any competition calendar intelligence:
1. Verify active partnership status on fantokens.com and
   socios.com for the specific token
2. Check logo colour — black or greyscale logo = potentially
   inactive partnership · do not proceed without verification
3. Cross-check chiliscan.com for recent on-chain activity
4. If status is uncertain — treat as UNCONFIRMED and flag in
   SMI briefing before any analysis

This verification applies to every cluster in this framework
without exception. The South American cluster (G) has the
highest historical rate of terminated partnerships — but
terminations can occur in any cluster at any time.

**Agent rule 0:** Partnership verification is a prerequisite for
every competition calendar application. No competition window
intelligence is valid for an unverified token.

---

## How to Use This Framework

**Step 1 — Identify the token cluster.** Which region and competition
tier does the fan token belong to?

**Step 2 — Identify the current competition window.** Is the domestic
league in season? Is the continental competition in group stage,
knockout, or off-season?

**Step 3 — Apply the window modifier.** Active competition window =
demand signals are meaningful. Off-season = reduced demand signal
reliability. Multiple overlapping windows = compound signal potential.

**Step 4 — Check for international break impact.** International
breaks affect squad availability as a Type 5 Operational signal,
but the break calendar is structural and belongs here.

---

## Token Cluster A — English Premier League

**Active fan tokens (registry verified, Chiliz Chain):**
$AFC (Arsenal) · $SPURS (Tottenham) · $CITY (Manchester City) ·
$CPFC (Crystal Palace) · $AVL (Aston Villa) · $EFC (Everton) ·
$LUFC (Leeds United)

**Domestic league rhythm:**
- Season: August to May (38 matchdays)
- Winter break: approximately 2 weeks in January
- No mid-season break in summer
- Peak fixture density: December (Christmas period — every 2-3 days)

**Continental competition windows:**
- UCL/Europa League/ECWC: September to May
  Group stage: September to December
  Knockout rounds: February to May
  Finals: late May
- $AFC note: UCL participation directly affects FTP PATH_2 signal
  windows — UCL knockout matches are primary PATH_2 activation events

**International break windows (approximate):**
- September · October · November · March
- Each break: approximately 10-14 days
- Squad availability impact: Type 5 Operational signal

**PTG relevance:** EPL clubs do not have PTG national team tokens.
However English players in national squads with fan tokens
(e.g. $SFA if Scottish players) create indirect signal intersections.

**Agent rule 1:** EPL season runs August to May. Demand signals
for English club tokens outside this window (June-July) occur
in pre-season — lower reliability, no competitive context.
Pre-season fixtures are not valid calibration records.

---

## Token Cluster B — Spanish La Liga

**Active fan tokens (registry verified, Chiliz Chain):**
$BAR (FC Barcelona) · $ATM (Atletico Madrid) ·
$SEVILLA (Sevilla FC) · $RSO (Real Sociedad) ·
$LEV (Levante UD) · $VCF (Valencia CF)

**Domestic league rhythm:**
- Season: August to May (38 matchdays)
- Winter break: approximately 2 weeks late December to early January
- Copa del Rey: August to April (knockout format)

**Continental competition windows:**
- UCL/Europa League: September to May (same as EPL cluster)
- $BAR and $ATM are regular UCL participants

**International break windows:**
- Same FIFA international calendar as EPL cluster
- Spanish national team ($SPAIN) intersects with La Liga clubs —
  major tournament windows (WC, Euros) affect squad availability

**PTG relevance:** $SPAIN is the primary national token for this
cluster. WC2026 PTG series completed 9 burns — CLOSED.
Next PTG tournament: UEFA Nations League Finals or Euro 2028.

**Agent rule 2:** La Liga season structure mirrors EPL (Aug-May).
El Clásico ($BAR vs Real Madrid — no Real Madrid fan token) and
Madrid derby ($ATM vs Real Madrid) are high-profile fixtures but
only one fan token side applies. Apply single-token fixture rules.

---

## Token Cluster C — Italian Serie A

**Active fan tokens (registry verified, Chiliz Chain):**
$JUV (Juventus) · $INTER (Inter Milan) · $ACM (AC Milan) ·
$NAP (Napoli) · $ASR (AS Roma) · $BFC (Bologna) · $UDI (Udinese)

**Domestic league rhythm:**
- Season: August to May (38 matchdays)
- Winter break: approximately 2 weeks late December to January
- Coppa Italia: September to May

**Continental competition windows:**
- UCL/Europa Conference: September to May
- $INTER and $ACM are regular UCL participants
- $JUV: UCL status varies by season — always verify current
  competition tier before analysis

**PTG relevance:** $ITA (FIGC — Italy national team) is the
primary national token for this cluster. Active on Chiliz Chain.

**Agent rule 3:** Italian dual-token derbies: $INTER vs $ACM
(Milan derby) is a confirmed dual fan token fixture — apply
dual fan token framework when both clubs are active participants.
$JUV vs $INTER — verify current competition tier for both
before applying compound modifier.

---

## Token Cluster D — French Ligue 1

**Active fan tokens (registry verified, Chiliz Chain):**
$PSG (Paris Saint-Germain) · $ASM (AS Monaco)

**Domestic league rhythm:**
- Season: August to May (34 matchdays)
- Winter break: approximately 3 weeks late December to January
- Coupe de France: August to May

**Continental competition windows:**
- UCL: September to May ($PSG regular participant)
- $PSG UCL fixtures are high-profile demand signal events

**PTG relevance:** No French national team fan token currently
confirmed on Chiliz Chain.

**Agent rule 4:** $PSG dominates French Ligue 1. French league
fixtures involving $PSG are effectively single-token fixtures
(no other active Ligue 1 fan token at Tier A). Apply single-
token fixture rules for domestic league matches.

---

## Token Cluster E — Turkish Süper Lig

**Active fan tokens (registry verified, Chiliz Chain):**
$GAL (Galatasaray) · $TRA (Trabzonspor) · $ALA (Alanyaspor) ·
$IBFK (İstanbul Başakşehir) · $GOZ (Göztepe) · $SAM (Samsunspor)
Note: $BJK (Beşiktaş) on Ethereum — not Chiliz Chain

**Domestic league rhythm:**
- Season: August to May (34 matchdays)
- Winter break: approximately 6 weeks December to February
  (longer than Western European leagues)
- Turkish Cup: September to May

**Continental competition windows:**
- UCL/Europa League: $GAL is the primary continental participant
- Europa League group stage: September to December
- Knockout rounds: February to May

**Dual token opportunity:** Multiple active Chiliz tokens in the
same league creates frequent dual-token fixture potential.
Istanbul derby ($GAL vs $IBFK, $GAL vs $TRA in cup) — verify
both tokens active before applying dual-token framework.

**Agent rule 5:** Turkish Süper Lig has the longest winter break
of any major European league with active fan tokens (~6 weeks).
Demand signals during December-February window are reduced
competition context — apply lower confidence modifier.

---

## Token Cluster F — Brazilian Série A

**Active fan tokens (registry verified, Chiliz Chain):**
$MENGO (Flamengo) · $VERDAO (SE Palmeiras) · $FLU (Fluminense) ·
$SCCP (SC Corinthians) · $SPFC (São Paulo FC) · $BAHIA ·
$GALO (Clube Atlético Mineiro) · $SACI (SC Internacional) ·
$VASCO (Vasco da Gama)

**CRITICAL:** Brazilian football calendar is INVERTED relative
to European leagues. Season runs approximately March to December.
January-February is the Brazilian off-season.

**Domestic league rhythm:**
- Brasileirão Série A: approximately April to December
- State Championships (Campeonatos Estaduais): January to April
  (overlaps with off-season and early Brasileirão)
- Copa do Brasil: March to November (knockout format)

**Continental competition windows:**
- Copa Libertadores: February to November
  Group stage: February to May
  Knockout rounds: June to November
  Final: typically late October/November
- Copa Sudamericana: February to November (same structure)

**PTG relevance:** No Brazilian national team fan token currently
confirmed on Chiliz Chain ($BFT on BITCI — not applicable).

**Dual token opportunity:** Brazilian cluster has the highest
concentration of active fan tokens of any country in the registry
(9 tokens). Domestic fixtures between any two active tokens are
potential dual-token calibration records. Libertadores and
Sudamericana inter-club fixtures (e.g. $MENGO vs $VERDAO) are
the richest dual-token continental opportunities.

**Agent rule 6:** Brazilian off-season is January-February. Do
not apply competitive fixture demand modifiers during this window.
State championships run during this period but are lower-stakes
fixtures — apply reduced competition tier modifier.

**Agent rule 7:** Copa Libertadores is the primary PTG-equivalent
competition window for Brazilian tokens. The 2025 Libertadores
Final ($MENGO vs $VERDAO) established the dual fan token final
as Precedent #1 (see fan-token/use-cases.md). Monitor August-
November window for knockout stage dual-token fixture potential.

---

## Token Cluster G — Other South American

**Active fan tokens (registry verified, Chiliz Chain):**
$ARG (Argentina national) · $CAI (Club Atletico Independiente —
verify status) · $RACING (Racing Club — verify status) ·
$MFC (Millonarios FC — Colombia) · $UCH (Universidad de Chile
— verify status) · $SACI (SC Internacional — covered in F)

**Calendar note:** South American club football broadly follows
the inverted calendar (March-November season) with country
variations. Argentina's Primera División runs February to
December with a winter break in July.

**PTG relevance:** $ARG (Argentina national team) is an active
PTG token. WC2026 series: 7 burns, finalist, eliminated. Next
PTG opportunity: Copa América or WC2030 qualification.

**Agent rule 8:** Always verify active partnership status for
South American club tokens before any analysis — this cluster
has the highest rate of terminated partnerships in the registry.
Apply black logo verification rule before any fixture analysis.

---

## Token Cluster H — MMA

**Active fan tokens (registry verified, Chiliz Chain):**
$UFC (Ultimate Fighting Championship) · $PFL (Professional
Fighters League)

**Competition rhythm:**
UFC card cadence:
- Numbered events (UFC 300, 301 etc): approximately monthly
- Fight Night cards: weekly to bi-weekly
- No fixed season — year-round programming
- Major cards typically Saturday · UK/BST time usually late
  night (main card starts ~03:00 BST for US-based events)

PFL season structure:
- Regular season: approximately April to August
- Playoffs: September
- World Championship: October/November
- PFL SuperFights: January-March (off-season exhibition format)

**PTG relevance:** Neither $UFC nor $PFL are PTG tokens — PTG
is for national football team tokens in tournaments only.
$UFC and $PFL are calibration-valid for fan token
sports intelligence — both qualify as valid calibration records
when the main event card features named fighters.

**Pre-event window:** MMA weigh-in occurs the day before the
event (T-1). Weigh-in miss is a Type 5 Operational signal —
highest priority operational modifier in SportMind.

**Agent rule 9:** UFC and PFL operate year-round with no off-
season. Demand signals are valid across all calendar months.
Apply MMA-specific pre-event window (T-48h to T-weigh-in)
rather than football pre-match window.

**Agent rule 10:** PFL regular season (April-August) produces
the richest calibration opportunities — fighters are competing
for playoff seeding, creating higher stakes than exhibition
events. Apply elevated competition stakes modifier during
regular season vs SuperFights window.

---

## Token Cluster I — Formula 1

**Active fan tokens (registry verified, Chiliz Chain):**
$AM (Aston Martin) · $ROUSH (Roush Fenway — NASCAR, see below)

**F1 season rhythm:**
- Season: approximately March to November (23-24 races)
- Winter break: December to February (testing in February)
- Sprint weekends: select rounds only
- No mid-season break

**Note:** Alpine F1 ($ALPINE) is on BNB Chain — not Chiliz Chain.
Alfa Romeo/Sauber ($SAUBER) partnership ended.

**Agent rule 11:** F1 season runs March to November. No demand
signals applicable during December-February winter break.
Sprint weekend format changes qualifying-to-race signal
dynamics — apply sprint race modifier when applicable.

---

## Token Cluster J — NASCAR

**Active fan tokens (registry verified, Chiliz Chain):**
$ROUSH (Roush Fenway Keselowski)

**NASCAR season rhythm:**
- Cup Series: February (Daytona 500) to November (Championship)
- Playoffs: September to November (10 races, elimination format)
- Winter break: December to January

**Agent rule 12:** NASCAR playoff window (September-November)
is the highest-stakes competition period for $ROUSH. Apply
elevated competition tier modifier during playoff rounds.

---

## Token Cluster K — Rugby

**Active fan tokens (registry verified, Chiliz Chain):**
$SFP (Stade Français Paris) · $SHARKS (The Sharks)

**Rugby union season rhythm:**
- European club competitions (Top 14, URC): September to June
- Stade Français: Top 14 season September to June
- The Sharks: United Rugby Championship September to June ·
  also Champions Cup (European) October to May
- International windows: November (Autumn Nations) · February-
  March (Six Nations) · June (Summer tours) · July (Lions tours)

**Agent rule 13:** Rugby international windows create squad
availability signals (Type 5 Operational). National call-ups
during Top 14 or URC rounds are a meaningful pre-match modifier
for $SFP and $SHARKS.

---

## Token Cluster L — Esports

**Active fan tokens (registry verified, Chiliz Chain):**
$OG · $ALL (Alliance) · $DOJO (Ninjas in Pyjamas) ·
$TH (Team Heretics) · $MIBR

**Esports calendar:**
- No fixed season equivalent to traditional sports
- Major tournament calendar varies by game title
- Roster lock dates are the esports equivalent of transfer
  deadlines — significant Type 5 Operational signal
- Patch cycles affect team performance — structural modifier
  for teams specialising in meta-dependent titles

**Agent rule 14:** Esports demand signals require game-title
context. A tournament in CS2 does not affect a team's Dota 2
performance signals. Always identify the game title and
tournament tier before applying competition modifier.

---

## Postponement and Rescheduling Protocol

When a fixture involving an active fan token is postponed or
rescheduled:

1. **Demand window reset:** The pre-match demand window resets
   to the new fixture date. Any demand signals accumulated for
   the original date are no longer valid.

2. **SMI flag:** Surface in Section 1 as a Type 5 Operational
   signal — "demand window reset."

3. **Calibration record impact:** If a calibration record was
   submitted before the postponement, it remains valid only if
   resubmitted with the new fixture date before the rescheduled
   kickoff. Original submission is void.

4. **PTG impact:** PTG burns do not execute on postponed matches
   — no burn event until the match is played and completed.

**Agent rule 15:** Postponement = demand window reset signal.
Always check for postponement before applying pre-match demand
modifiers. A stale pre-match signal from a postponed fixture
is a Type 5 misclassification risk.

---

## MIND DIMENSIONS

| Dimension | Sub-dimensions engaged | Status |
|---|---|---|
| 1. Intelligence | 1a Domain Knowledge · 1b Signal Awareness · 1c Pattern Recognition | ACTIVE |
| 2. Reasoning | 2a Causal · 2d Temporal | ACTIVE |
| 3. Context | 3a Macro Context · 3b Event Context · 3c Historical Context | ACTIVE |
| 4. Memory | 4b Semantic Memory · 4c Working Memory | ACTIVE |
| 5. Judgment | 5a Uncertainty Weighting · 5d Priority Judgment | ACTIVE |
| 6. Attention | 6b Urgency Detection · 6c Noise Filtering | ACTIVE |
| 7. Communication | 7a Output Clarity | ACTIVE |
| 8. Verification | 8a Source Tier Assessment · 8d Recency Validation | ACTIVE |
| 9. Learning | 9c Pattern Reinforcement | ACTIVE |
| 10. Integration | 10a Cross-Layer Synthesis | ACTIVE |
| 11. Calibration | 11d Coverage Tracking | ACTIVE |
| 12. Adaptation | 12b Context Switching · 12d Framework Switching | ACTIVE |
| 13. Ethics | 13a Fabrication Prevention | ACTIVE |
| 14. Transparency | 14d Limitation Acknowledgement | ACTIVE |
| 15. Execution | 15a Entry Discipline | ACTIVE |
| 16. Collaboration | [NOT APPLICABLE] | — |

---

## COMPATIBILITY

Compatible with: Claude · GPT-4 · Gemini · any LLM ·
sportmind_pre_match · sportmind_macro · sportmind_fan_token_lookup ·
fan-token/registry/complete-registry.md ·
fan-token/burn-to-glory-framework.md ·
fan-token/use-cases.md ·
fan-token/holder-tax-framework.md ·
core/temporal-reasoning-framework.md ·
core/signal-classification-framework.md ·
core/contradiction-resolution-framework.md ·
market/club-intelligence/

© 2026 SportMind
