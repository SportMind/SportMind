# App 8 — Sports Governance Intelligence

**A SportMind-powered tool for fan token holders participating in on-chain governance
votes — surfacing commercial context, lifecycle implications, and signal analysis
for each vote before holders commit their tokens.**

---

## The problem this solves

Fan token governance votes currently offer holders a binary choice with minimal
context. "Should we sign this player?" or "Which kit should we wear?" are presented
without any analysis of what the decision means commercially, what it signals about
the club's direction, or what impact a yes/no outcome would have on the token's
lifecycle trajectory.

A holder who votes to sign an expensive player without knowing that player's APS
score is making a governance decision blind. A holder who votes on a commercial
partnership without knowing what the PHS (Partnership Health Score) implications
are is doing the same.

SportMind's Layer 3 commercial stack — APS, ABS, PHS, LTUI, AFS — was built
precisely to answer these questions. This application surfaces that intelligence
at the point of governance, not after the decision has already been made.

---

## Target users

**Primary:** Fan token holders participating in Socios or on-chain governance votes.

**Secondary:** Club commercial departments designing governance vote proposals
and wanting to understand how SportMind frames each option before presenting it.

**Tertiary:** Fan token platforms building governance UIs who want to embed
commercial intelligence into the voting experience.

---

## Core value proposition

> *"Before you vote, SportMind tells you what it means for your token's future."*

The LTUI (Lifetime Token Utility Index) is the governance differentiator. Every
governance decision either extends or reduces the expected lifetime utility of the
token. Signing a high-APS player extends it. Entering a partnership with a low
PHS outlook reduces it. SportMind can model this before the vote closes.

---

## SportMind skill stack

```
GOVERNANCE INTELLIGENCE STACK:

For PLAYER SIGNING votes:
  1. fan-token/transfer-signal/ → APS (how portable is this player's value?)
  2. fan-token/performance-on-pitch/ → PI (on-pitch justification)
  3. fan-token/athlete-social-activity/ → SHS, AGI (social engagement health)
  4. fan-token/athlete-social-lift/ → AELS (does this player move token holders?)
  5. fan-token/brand-score/ → ABS (composite commercial value)
  6. fan-token/fan-token-lifecycle/ → LTUI impact projection

For COMMERCIAL PARTNERSHIP votes:
  1. fan-token/fan-token-partnership-intelligence/ → PHS projection
  2. fan-token/sponsorship-match/ → AFS (audience fit for proposed partner)
  3. fan-token/sports-brand-sponsorship/ → market rate benchmarking
  4. fan-token/fan-token-lifecycle/ → LTUI impact (positive or negative)

For KIT / STADIUM / BRANDING votes:
  1. fan-token/fan-token-lifecycle/ → current phase (Phase 1 needs novelty;
     Phase 2 needs utility; Phase 3 needs re-engagement)
  2. fan-token/athlete-social-activity/ → SHS (will holders share this?)
  3. market/market-football.md → competitive context

Skills API shortcut:
  GET /stack?use_case=governance&sport=football
```

---

## Governance brief output format

```
SPORTMIND GOVERNANCE BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Vote: Should [Club] sign [Player] for €X?
Token: $[SYMBOL]
Closes: [Date]
SportMind Score (SMS): 79 / GOOD

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMMERCIAL ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ABS (Athlete Brand Score):    82 / 100 — strong commercial asset
APS (Portability Score):      0.76 — 76% of signal travels with the player
AELS (Engagement Lift):       0.71 — high; this player moves token holders
PI (Performance Index):       79.4 — top 18% for position this season
SHS (Social Health):          72 — consistent, no crisis flags

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOKEN LIFECYCLE IMPACT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Current LTUI:     54 (Phase 2 — Active Utility)
Projected LTUI if YES: 61 (+7) — meaningful uplift
Projected LTUI if NO:  54 (unchanged — no alternative signal identified)

Reasoning: APS 0.76 + AELS 0.71 = strong token engagement driver.
Club currently lacks a high-AELS player since last departure.
This signing fills the AELS gap. LTUI uplift is projected as sustained
(not speculative) because on-pitch PI (79.4) supports the commercial case.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RISK FLAGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  Injury history: 2 significant injuries in 3 seasons (TAI: 68)
    Recommendation: request medical clause in contract
    
⚠️  Fee (€X) vs market rate: load fan-token/sports-brand-sponsorship/
    for fee benchmarking — above market rate risks squad balance signal

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SPORTMIND RECOMMENDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Commercial case: STRONG — ABS 82, AELS 0.71 justify the investment
Token impact:    POSITIVE — LTUI +7 projected
Risk note:       Injury history warrants medical clause; fee warrants scrutiny

Note: SportMind provides intelligence context for governance decisions.
It does not vote on behalf of holders and does not constitute financial advice.
Final vote decision remains with each token holder.
```

---

## Agent system prompt

```
You are a sports governance intelligence agent powered by SportMind.
Your role is to provide commercial context for fan token governance votes
before holders submit their votes.

FOR EACH GOVERNANCE VOTE:

1. IDENTIFY VOTE TYPE:
   Player signing → load APS, PI, AELS, ABS, LTUI
   Commercial partnership → load PHS, AFS, market rates, LTUI
   Kit/branding/stadium → load lifecycle phase, SHS, competitive context

2. LTUI IMPACT PROJECTION:
   Always model the YES vs NO scenario for LTUI.
   "What does the token's lifetime utility look like with this decision?"
   "What does it look like without it?"
   Be honest when SportMind cannot determine a clear difference.

3. APS FOR PLAYER VOTES:
   APS is the most important metric for signing votes.
   A player with APS 0.40 brings less commercial value than their statistics suggest.
   A player with APS 0.80+ brings their commercial identity with them.

4. PHS FOR PARTNERSHIP VOTES:
   Project PHS at 12 months for the proposed partnership.
   Identify the top 2 risks and the primary termination trigger to watch.

5. RISK FLAGS:
   Always surface TAI (injury history), PS (professionalism), any crisis events.
   Never bury risks — they belong at the top of the brief, not the bottom.

6. TONE:
   This is a pre-vote intelligence brief, not a voting recommendation.
   Frame as "here is what SportMind shows" not "you should vote YES/NO."
   Holders make their own decisions. SportMind provides the commercial context.
```

---

## SportFi Kit integration

```typescript
// Governance vote widget using SportFi Kit + SportMind
import { useFanToken, useGovernanceVote } from '@sportfi-kit/core'
import { useSportMind } from '../hooks/useSportMind'

function GovernanceBrief({ voteId, sport, tokenSymbol }: Props) {
  const { isHolder, balance } = useFanToken({ symbol: tokenSymbol })
  const { signal } = useSportMind(sport, 'governance')
  const { vote, hasVoted } = useGovernanceVote({ voteId })

  if (!isHolder) return <TokenGate symbol={tokenSymbol} />

  return (
    <div className="governance-brief">
      <SMSBadge sms={signal?.sportmind_score?.sms} />
      <CommercialAssessment signal={signal} />
      <LTUIProjection current={signal?.ltui} projected={signal?.projected_ltui} />
      <RiskFlags flags={signal?.modifiers?.flags} />
      <VoteButtons
        onVote={(choice) => vote({ voteId, choice, signalHash: hashSignal(signal) })}
        disabled={hasVoted}
      />
      <Disclaimer>
        SportMind provides commercial context only. Vote decisions rest with you.
      </Disclaimer>
    </div>
  )
}
```

---

## References

- `fan-token/transfer-signal/` — APS (Athlete Portability Score)
- `fan-token/performance-on-pitch/` — PI, TAI
- `fan-token/athlete-social-activity/` — SHS, AGI
- `fan-token/athlete-social-lift/` — AELS
- `fan-token/brand-score/` — ABS
- `fan-token/fan-token-partnership-intelligence/` — PHS
- `fan-token/fan-token-lifecycle/` — LTUI
- `fan-token/sponsorship-match/` — AFS
- `examples/applications/app-07-sportfi-kit-integration.md` — SportFi Kit governance hooks

*MIT License · SportMind · sportmind.dev*
