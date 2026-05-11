---
name: governance-intelligence
description: >
  Fan token governance reasoning framework — proposal classification, voter
  turnout intelligence, quorum mechanics, and governance calendar as a
  community health signal. Agent-facing interface extending
  fan-token/sports-governance-intelligence/. All demand-only signals —
  governance does not affect FTP PATH_2 supply mechanics directly.
---

# Fan Token Governance Intelligence

**Reasoning framework for governance as a community health and demand signal.**
Governance events affect demand signals only — not FTP supply mechanics.

> Related: `fan-token/sports-governance-intelligence/` — full on-chain governance model

---

## Governance proposal classification

```
PROPOSAL TYPE — DEMAND MODIFIER TABLE:

  HIGH ENGAGEMENT PROPOSALS (fan-facing, emotionally resonant):
    Examples: kit design votes, player-related decisions (squad number allocation,
      pre-match music, mascot selection), exclusive experience allocation
    Demand modifier: ×1.05 during voting window (typically 48-72h)
    Mechanism: fans who are not current holders may acquire tokens to vote;
      existing holders become more active traders during high-engagement votes
    Post-vote: sentiment spike ×1.02 for 24h on result announcement
    
  MEDIUM ENGAGEMENT PROPOSALS (commercial or structural):
    Examples: partnership approvals, training ground feature decisions,
      stadium naming input, charity initiative selection
    Demand modifier: ×1.02 during voting window
    Post-vote: minimal additional signal (×1.00)
    
  LOW ENGAGEMENT PROPOSALS (administrative):
    Examples: minor platform features, policy updates, technical parameter changes
    Demand modifier: ×1.00 — neutral
    These do not generate meaningful demand signal; do not apply modifier
    
  EMERGENCY / REACTIVE PROPOSALS (governance under pressure):
    Examples: unexpected situation requiring urgent holder vote, dispute resolution
    Signal: depends on context
      If emergency vote demonstrates club/platform responsiveness: ×1.03 positive
      If emergency vote reveals underlying dysfunction: ×0.94 negative structural
    Classify based on what triggered the emergency vote, not the vote itself

AGENT RULE:
  Identify proposal type before applying modifier.
  Source: Socios platform official vote announcement.
  Apply modifier only during confirmed active voting window.
  Remove modifier immediately on vote close.
```

---

## Voter turnout intelligence

```
TURNOUT AS COMMUNITY HEALTH SIGNAL:

  HIGH TURNOUT (above 20% of eligible holders voting):
    Signal: strong community health
    Modifier: ×1.03 sustained demand modifier (not just during vote window)
    Duration: 2 weeks post-vote (community engagement persists beyond event)
    
  STANDARD TURNOUT (5-20% of holders voting):
    Signal: normal — apply no additional modifier
    
  LOW TURNOUT (below 5% of holders voting):
    Signal: community disengagement
    Modifier: ×0.97 sustained (mild negative; community is not active)
    Duration: 4 weeks post-vote (persistent signal)
    Remove when: next vote shows higher turnout
    
  TURNOUT TREND — THREE CONSECUTIVE VOTES:
    Declining turnout across three consecutive votes:
      Meaningful community health warning signal
      Apply: community_health_flag = CAUTION
      Modifier: ×0.95 sustained (stronger than single low-turnout vote)
      Remove when: two consecutive votes show recovery
      
    Increasing turnout across three consecutive votes:
      Positive community health trajectory
      Apply: community_health_momentum = POSITIVE
      Modifier: ×1.03 sustained

QUORUM MECHANICS REASONING:
  Some governance systems require minimum participation to be valid (quorum).
  
  QUORUM RISK (approaching vote close with participation below threshold):
    Pre-vote quorum risk is a demand signal:
      Holders may acquire tokens specifically to vote → temporary demand boost ×1.02
      This is speculative buying and typically reverses post-vote
      
  FAILED QUORUM:
    Vote did not reach minimum participation threshold — result invalid
    Signal: negative community health signal regardless of what vote was about
    Modifier: ×0.96 for 1 week (mild negative; community failed to engage)
    Club/platform response matters:
      Clear re-vote scheduled: modifier recovers to ×0.99 on announcement
      Silence or unclear response: extend modifier at ×0.96 for 2 weeks
```

---

## Governance calendar as signal

```
GOVERNANCE FREQUENCY AND COMMUNITY HEALTH:

  MONTHLY VOTES (high governance activity):
    Signal: active engagement culture; holders have regular participation opportunities
    Structural modifier: ×1.02 baseline community health modifier
    Apply: to all CDI calculations for this token
    
  QUARTERLY VOTES (standard governance activity):
    Signal: normal governance cadence
    Structural modifier: ×1.00 — baseline, no adjustment
    
  IRREGULAR / INFREQUENT VOTES (low governance activity):
    Signal: passive governance; holders have limited voice
    Structural modifier: ×0.98 baseline
    Note: infrequent governance often signals that the club is not
      prioritising community engagement — longer-term CDI concern
      
  GOVERNANCE FREQUENCY ASSESSMENT:
    Count votes in trailing 12 months.
    12+ votes: MONTHLY category (×1.02)
    4-11 votes: QUARTERLY category (×1.00)
    <4 votes: IRREGULAR category (×0.98)

GOVERNANCE CALENDAR INTERACTION WITH MATCH CALENDAR:
  Governance votes scheduled around high-profile match dates tend to see:
    Higher turnout (fans already engaged with the club)
    Elevated demand during voting window (stacks with match pre-match signal)
  When governance vote overlaps with major match (48h window):
    Apply both governance demand modifier AND pre-match demand signal
    These are independent signals — apply multiplicatively, not additively.
    Cap at ×1.10 combined maximum during overlap window.
```

---

## Governance signal interaction with CDI

```
HOW GOVERNANCE INTEGRATES INTO CDI CALCULATION:

  GOVERNANCE IS A COMMUNITY DEPTH SIGNAL:
    Governance activity indicates the depth of the holder community.
    Deep communities (high governance engagement) have:
      More stable demand (less likely to sell on first negative event)
      Higher resilience to temporary negative signals
      
  CDI ADJUSTMENT FROM GOVERNANCE:
    Standard governance (×1.00): no CDI adjustment
    High engagement governance (×1.02-1.05): apply community_depth_bonus to CDI
      community_depth_bonus = +2 to +5 points on CDI score
    Low engagement governance (×0.97-0.98): apply community_depth_penalty
      community_depth_penalty = −2 to −3 points on CDI score
      
  PATH_2 NOTE:
    Governance signals do NOT directly affect FTP PATH_2 supply mechanics.
    PATH_2 is triggered by match results (WIN burns, LOSS mints).
    Governance does not change the supply event itself.
    Governance affects DEMAND signals only.
    
  AGENT RULE:
    Integrate governance modifier into CDI calculation, not into match signal.
    Governance modifier is applied at the CDI layer, not the SMS (match signal) layer.
```

---

## Compatibility

**Full governance model:** `fan-token/sports-governance-intelligence/`
**Sentiment integration:** `core/social-sentiment-intelligence.md`
**CDI framework:**         `fan-token/fan-token-lifecycle/`
**PATH_2 mechanics:**      `fan-token/ftp-path2.md`

---

*SportMind v3.97.28 · MIT License · sportmind.dev*
*Governance affects demand signals only — does not directly affect FTP supply mechanics*
