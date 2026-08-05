# MMA Intelligence Framework

Mixed Martial Arts requires a distinct signal reasoning framework
from football and other team sports. The pre-event window is
different, the key modifiers are unique to combat sports, and
the competition structure of the two active fan token promotions
($UFC and $PFL) differs significantly from league-based sports.

Agents applying football pre-match frameworks to MMA events will
systematically misclassify signals. This framework provides the
canonical MMA signal intelligence layer for SportMind.

---

## Active Fan Token Promotions

**$UFC — Ultimate Fighting Championship**
The world's premier MMA promotion. Active Chiliz fan token,
confirmed partnership. Year-round programming — no off-season.

**$PFL — Professional Fighters League**
Season-based MMA promotion with regular season, playoffs, and
championship. Active Chiliz fan token, confirmed partnership.
Distinct from UFC in format and stakes structure.

Both tokens qualify as valid SportMind calibration records
when the main event card is being analysed. Verify active
partnership status before any analysis per Agent rule 0
from fan-token/competition-calendar-framework.md.

---

## MMA Pre-Event Timeline

MMA has a distinct pre-event timeline that differs from football.
Apply this timeline instead of the generic pre-match window when
analysing MMA events.

| Phase | Timing | Signal type | Priority |
|---|---|---|---|
| Fight announcement | T-8 to T-4 weeks | Type 3 Structural | MEDIUM |
| Open workouts / media day | T-3 to T-2 days | Type 5 Operational | LOW |
| Weigh-ins | T-1 day (afternoon) | Type 5 Operational | CRITICAL |
| Early prelims | Event day | Type 5 Operational | LOW |
| Prelims | Event day | Type 5 Operational | LOW |
| Main card begins | Event start | Analysis window closes | — |

**Agent rule 1:** The MMA pre-event analysis window closes at
main card start — not at weigh-in completion. Post-weigh-in
signals (staredowns, press conference statements) are noise
unless a late cancellation occurs.

**Agent rule 2:** Weigh-in timing is the critical checkpoint
for MMA analysis. Always confirm weigh-in results before
finalising pre-event analysis. A weight miss discovered after
initial analysis invalidates the prior assessment — restart
the analysis with the new information.

---

## The Weigh-In Signal — Highest Priority Type 5

The weigh-in is the single most important pre-event signal
in MMA. It occurs the day before the event (T-1) and
determines whether fighters make their contracted weight class.

**Weight miss (failure to make weight):**

A weight miss immediately triggers a full reassessment of the
affected bout and its impact on the card.

**Consequences of a weight miss:**

| Outcome | Probability | Signal impact |
|---|---|---|
| Bout proceeds at catchweight | HIGH | Confidence tier reduction |
| Fighter given time to cut remaining weight | MEDIUM | Delay to confirmation |
| Bout cancelled — replacement sought | LOW-MEDIUM | Card restructure |
| Champion misses weight — title vacated | LOW | Maximum disruption |

**Agent rule 3:** A confirmed weight miss changes the confidence
tier of the entire pre-event analysis by one tier minimum:
HIGH → MEDIUM · MEDIUM → LOW · LOW → NO SIGNAL.
This is the only Type 5 Operational signal in SportMind that
automatically reduces confidence tier without further analysis.

**Agent rule 4:** When the main event fighter misses weight,
treat the entire card as REASSESSMENT REQUIRED. The main event
drives demand for the entire card — main event disruption
affects the full fan token demand signal, not just the bout.

**Agent rule 5:** Championship fight weight miss by the
champion has the highest possible disruption level. Title
vacated on scales = maximum uncertainty. Apply LOW confidence
to any pre-event fan token demand analysis in this scenario.

---

## Card Structure and Stakes Modifiers

Not all MMA events carry equal stakes. Card type is a structural
modifier that should be applied before all other modifiers.

### UFC Card Types

| Card type | Examples | Stakes level | Demand modifier |
|---|---|---|---|
| Numbered PPV event | UFC 300, UFC 310 | HIGHEST | +++ |
| Fight Night (major market) | UFC London, UFC Sydney | HIGH | ++ |
| Fight Night (standard) | UFC Fight Night [venue] | MEDIUM | + |
| Dana White Contender Series | DWCS | LOW | Neutral |

**Numbered PPV events** are the highest-profile UFC cards. Title
fights almost always headline numbered events. These produce the
strongest fan token demand signals.

**UFC Fight Night cards** are the weekly/bi-weekly staple of UFC
programming. London and Sydney events carry elevated significance
due to large regional fan bases and typically stronger European
fan token holder engagement.

**Agent rule 6:** Always identify the card type before applying
pre-event modifiers. A UFC Fight Night card with no title bout
is not equivalent to UFC 300. Apply the stakes modifier before
confidence tier assignment.

### PFL Card Types

| Card type | Timing | Stakes level | Demand modifier |
|---|---|---|---|
| Regular season | April-August | HIGH | ++ |
| Playoffs | September | HIGHEST | +++ |
| Championship | October-November | MAXIMUM | ++++ |
| SuperFights | January-March | MEDIUM | + |

**PFL regular season** fighters are competing for playoff points
— elimination stakes apply from mid-season. This creates elevated
fighting intensity relative to exhibition events.

**PFL playoffs** are single-elimination — losers are eliminated
from title contention. Maximum competitive stakes.

**PFL Championship** is the season finale — million-dollar prize
per weight class. Highest stakes event in PFL calendar.

**PFL SuperFights** (off-season) feature high-profile matchups
but without playoff implications. Elevated profile but reduced
stakes relative to regular season.

**Agent rule 7:** PFL Championship events (October-November)
carry the maximum stakes modifier of any regular PFL card.
Apply MAXIMUM competition tier weight. PFL SuperFights carry
a reduced stakes modifier despite high-profile billing.

---

## Title Fight Modifier

Championship bouts carry a distinct signal profile from
non-title main events.

**Title fight characteristics:**
- Five rounds (vs three for non-title)
- Champion has significant advantage (experience, preparation,
  familiar with the pressure)
- Title defences carry home advantage equivalent for champions
- Interim titles carry reduced stakes vs undisputed titles
- Unified title fights (two belt unification) carry maximum stakes

**Agent rule 8:** Apply title fight modifier to championship
bouts. Interim title fights receive a reduced modifier — they
are significant but not equivalent to undisputed championship
stakes. Two-belt unification fights receive the maximum title
fight modifier.

---

## Performance Bonus Culture

Both UFC and PFL offer significant performance bonuses that
create incentive structures affecting fighting style and
therefore outcome probability.

**UFC performance bonuses:**
- Performance of the Night: awarded to the most impressive
  finish (KO, TKO, submission) — $50,000 standard award
- Fight of the Night: awarded to the most entertaining bout
  (often a competitive decision or back-and-forth war)
- These are post-event awards — they do not affect pre-event
  analysis directly

**PFL scoring system:**
- PFL uses a points system in regular season — 3 points for
  finish, 2 for decision win, 1 for a draw
- Fighters who need points to make playoffs have maximum
  incentive to finish — changes fighting style toward
  aggressive, high-risk approaches
- A fighter who needs 3 points (finish only) vs a fighter
  who needs 2 points (decision is sufficient) have
  fundamentally different game plan incentives

**Agent rule 9:** In PFL regular season, always assess each
fighter's current points standing and playoff position before
analysis. A fighter who needs a finish to make playoffs will
fight significantly more aggressively than a fighter who only
needs a decision win. This is a structural modifier unique to
PFL format.

---

## Fighter Profile Modifiers (Structural — No Named Individuals)

Fighter characteristics affect pre-event signal reliability
without requiring named individual analysis. These are
structural profile modifiers applicable at the archetype level.

**Finishing rate:**
- High finishing rate fighter (70%+ finishes) vs decision
  specialist affects round-based analysis and crowd engagement
- High finishing rate = higher demand signal volatility
  (exciting finishes drive real-time demand)

**Weight cutting history:**
- Fighter with documented weight cutting issues = elevated
  weight miss probability → apply elevated pre-weigh-in
  uncertainty modifier

**Regional popularity:**
- Fighters with large regional fan bases (home country) drive
  elevated local market demand signals — particularly relevant
  for $UFC international Fight Night events

**Fighting style:**
- Striker-dominant matchups tend to produce more exciting
  fan-engaging content → elevated demand signal potential
- Grappling-dominant matchups may produce less visually
  exciting content → reduced real-time demand signal

**Agent rule 10:** Apply fighter profile modifiers at the
archetype level only. Never name specific fighters in library
files or calibration records. The modifier is based on the
structural profile (finishing rate, regional popularity,
style) — not the individual.

---

## Dual Promotion Analysis

When a fight card features both $UFC and $PFL tokens (rare but
possible in exhibition or crossover events), apply dual fan
token framework from fan-token/use-cases.md.

In standard analysis, $UFC and $PFL are separate tokens for
separate events. They do not create compound signals unless
both are simultaneously in pre-event windows on the same date.

**Agent rule 11:** $UFC and $PFL are independent signal sources.
An outcome in a UFC event does not affect $PFL token demand
signals and vice versa — unless a compound macro signal
(CHZ regime shift, major regulatory announcement) affects
both simultaneously.

---

## Calibration Record Validity for MMA

MMA calibration records are valid under the following conditions:

**Valid:**
- Main event analysis submitted before main card begins
- At least one active fan token promotion involved ($UFC or $PFL)
- Prediction covers main event direction (FIGHTER A / FIGHTER B
  / DRAW — rare in MMA but possible via majority draw)
- Weigh-in results confirmed and incorporated before submission

**Invalid:**
- Record submitted after weigh-ins where a weight miss occurred
  and the record was not updated to reflect the new information
- Preliminary bout analysis (only main event qualifies)
- Analysis of a card with no active fan token promotion
- Fighter name included in the record (Library Rule failure)

**Agent rule 12:** MMA calibration records must incorporate
confirmed weigh-in results. A record submitted before weigh-ins
that is not updated after a weight miss is invalid — the
analysis was based on incomplete information.

**Agent rule 13:** Always state the card type (UFC numbered,
UFC Fight Night, PFL regular season, PFL playoffs, PFL
championship) in the calibration record. Card type is a
structural modifier that must be documented.

---

## CHZ Macro Regime Interaction

The CAPITULATION ×0.70 macro regime applies to MMA fan token
signals exactly as it does to football fan token signals.

Under CAPITULATION:
- Pre-event demand signals are suppressed regardless of card
  quality or title fight status
- PTG burns do not apply to MMA (PTG is national football
  team tournament only)
- FTP PATH_2 does not apply to MMA ($AFC only)
- HOLD conditions from macro regime override event signals

**Agent rule 14:** MMA fan token signals are subject to the
full macro gate. A UFC 300-equivalent card does not override
CAPITULATION ×0.70. Apply macro layer before event layer,
consistent with layer hierarchy in
core/contradiction-resolution-framework.md Resolution Rule 3.

---

## Known MMA Signal Failure Modes

**MMA-FM1 — Weigh-in miss not incorporated**
Pre-event analysis completed before weigh-ins, weight miss
occurs, analysis not updated. The original analysis is now
invalid but treated as current. Fix: always confirm weigh-in
results before finalising any MMA pre-event analysis.

**MMA-FM2 — Card type conflation**
UFC Fight Night treated as equivalent to numbered PPV event.
Stakes modifier not applied. Fix: always identify card type
first and apply the appropriate stakes modifier.

**MMA-FM3 — PFL format misapplication**
PFL regular season analysis conducted without checking fighter
points standing and playoff position. Fix: in PFL regular
season, always check current standings before analysis.

**MMA-FM4 — Fighter name in record**
Named fighter appears in calibration record or library file.
Automatic Library Rule failure — named individuals fail the
Proper Noun Test. Fix: use archetype descriptors only
(champion, challenger, finishing specialist, decision fighter).

---

## MIND DIMENSIONS

| Dimension | Sub-dimensions engaged | Status |
|---|---|---|
| 1. Intelligence | 1a Domain Knowledge · 1b Signal Awareness · 1c Pattern Recognition · 1d Gap Awareness | ACTIVE |
| 2. Reasoning | 2a Causal · 2b Probabilistic · 2d Temporal | ACTIVE |
| 3. Context | 3b Event Context · 3c Historical Context | ACTIVE |
| 4. Memory | 4b Semantic Memory · 4d Procedural Memory | ACTIVE |
| 5. Judgment | 5a Uncertainty Weighting · 5b Risk Assessment · 5d Priority Judgment | ACTIVE |
| 6. Attention | 6a Signal Detection · 6b Urgency Detection · 6c Noise Filtering | ACTIVE |
| 7. Communication | 7a Output Clarity · 7b Confidence Expression · 7c Format Compliance | ACTIVE |
| 8. Verification | 8a Source Tier Assessment · 8c On-Chain Verification · 8d Recency Validation | ACTIVE |
| 9. Learning | 9a Modifier Updating · 9b Error Attribution · 9c Pattern Reinforcement | ACTIVE |
| 10. Integration | 10a Cross-Layer Synthesis | ACTIVE |
| 11. Calibration | 11a Direction Accuracy · 11b Confidence Calibration · 11c Modifier Validation · 11d Coverage Tracking | ACTIVE |
| 12. Adaptation | 12b Context Switching · 12c Signal Reweighting | ACTIVE |
| 13. Ethics | 13a Fabrication Prevention · 13b User Safety · 13d Representation Accuracy | ACTIVE |
| 14. Transparency | 14a Reasoning Chain Visibility · 14b Modifier Disclosure · 14d Limitation Acknowledgement | ACTIVE |
| Execution | ACTIVE | Autonomous execution triggers, entry/exit conditions, and hard boundaries defined |
| Collaboration | ACTIVE | Integrates with core frameworks, athlete intelligence, macro layer, and fan token registry |
| 15. Execution | 15a Entry Discipline · 15b Exit Discipline · 15d Playbook Adherence | ACTIVE |
| 16. Collaboration | [NOT APPLICABLE] | — |

---

## COMPATIBILITY

Compatible with: Claude · GPT-4 · Gemini · any LLM ·
sportmind_pre_match · sportmind_macro · sportmind_fan_token_lookup ·
fan-token/competition-calendar-framework.md ·
fan-token/registry/complete-registry.md ·
core/temporal-reasoning-framework.md ·
core/signal-classification-framework.md ·
core/contradiction-resolution-framework.md ·
core/mind-dimensions-framework.md ·
fan-token/agent-failure-modes-fan-token.md

© 2026 SportMind
