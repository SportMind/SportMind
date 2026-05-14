---
name: official-verification-framework
description: >
  Enduring reasoning framework for verifying whether a sports crypto asset is an
  officially licensed Fan Token™ versus an unofficial, unverified, or potentially
  fraudulent asset. Four-source verification methodology, national team token
  confirmation list, and registry reference. SportMind provides verification
  reasoning frameworks — not legal determinations.
---

# Official Fan Token™ Verification Framework

**How to reason about whether a sports crypto asset is an official Fan Token™.**
Verification reasoning frameworks only — not legal determinations.

> SportMind surfaces verification signals and flags risk indicators.
> Agents should recommend verification through official primary sources.
> They should not make definitive legal classifications.

---

## What an official Fan Token™ is

```
FAN TOKEN™ — TRADEMARK AND LEGAL BASIS:

  Fan Tokens™ are a trademarked product of Socios.com, operated by
  Mediarex Enterprises Limited. The trademark Fan Token™ applies
  specifically to tokens issued through the official Socios/Chiliz ecosystem.
  
  FOUR DEFINING CHARACTERISTICS OF AN OFFICIAL FAN TOKEN™:

  1. OFFICIAL PARTNERSHIP AGREEMENT:
     A confirmed agreement between the sports organisation (club, national
     team, or governing body) and Chiliz/Socios.
     Both parties announce the partnership through their own official channels.
     Neither party is anonymous. Both parties are named legal entities.
     
  2. VERIFIED ON CHILIZ CHAIN:
     All official Fan Tokens™ have confirmed contract addresses on
     chiliscan.com under the CAP20 token standard.
     V2.0 tokens are additionally live on Solana and Base via the official
     Chiliz bridge. All addresses are publicly verifiable and match official listings.
     
  3. LISTED ON OFFICIAL PLATFORM:
     All official Fan Tokens™ are listed on fantokens.com — the official
     Fan Tokens hub — with real-time price, supply, and holder data.
     Contract address on fantokens.com must match the chiliscan.com record.
     
  4. CLUB PRIMARY SOURCE CONFIRMATION:
     The sports organisation's official website, official social media accounts,
     or official press releases confirm the partnership.
     Third-party articles and media reports alone are NOT sufficient primary
     source confirmation. The organisation itself must have published confirmation.
```

---

## Four-source verification methodology

```
VERIFICATION SEQUENCE — COMPLETE ALL FOUR IN ORDER:

  SOURCE 1 — CLUB OR ORGANISATION OFFICIAL WEBSITE:
    Navigate to the club or organisation's official website.
    Look for: a Socios or Fan Token partnership page, press release, or
      announcement section that confirms the official partnership.
    If not present: NOT CONFIRMED OFFICIAL at this source.
    Note: an absence here is a significant risk signal, not just a gap.
    
  SOURCE 2 — SOCIOS.COM OFFICIAL LISTING:
    Navigate to socios.com.
    Confirm the token appears in the official club/organisation listing.
    If not present: NOT CONFIRMED OFFICIAL at this source.
    
  SOURCE 3 — CHILISCAN.COM CONTRACT VERIFICATION:
    Navigate to chiliscan.com/tokens.
    Look up the specific contract address associated with this token.
    Verify: contract address matches the one shown on socios.com and fantokens.com.
    If contract not on chiliscan.com: NOT AN OFFICIAL FAN TOKEN™ — this is critical.
    If contract present but addresses do not match: CRITICAL RED FLAG.
    
  SOURCE 4 — FANTOKENS.COM LISTING:
    Navigate to fantokens.com.
    Verify: the token is listed with consistent contract address, supply data,
      and price feed matching the socios.com and chiliscan.com records.
    If not present: NOT CONFIRMED OFFICIAL at this source.

VERIFICATION OUTCOME FRAMEWORK:

  Sources confirmed    Outcome                 Action
  ───────────────────────────────────────────────────────────────────────────
  All 4 confirmed      OFFICIAL FAN TOKEN™     Proceed with SportMind frameworks
  3 confirmed          LIKELY OFFICIAL         Verify the missing source
  2 or fewer           UNVERIFIED              High risk signal — flag and recommend verification
  0 confirmed          NOT AN OFFICIAL TOKEN   Surface immediately with fraud risk framework

AGENT RULE:
  Do not treat a token as official on the basis of a single source —
  even if that source is a major media outlet or prominent social media account.
  Fraudulent tokens routinely appear in legitimate media coverage.
  Four-source verification is the minimum standard.
```

---

## Registry reference

```
SPORTMIND VERIFIED REGISTRY:

  SportMind maintains registry files of confirmed official Fan Tokens™:
    fan-token/registry/bridge-supported.md  — V2.0 BRIDGE_LIVE tokens
    fan-token/registry/complete-registry.md — full confirmed token list
    
  REGISTRY POSITIVE MATCH:
    If a token appears in these registry files: it has been confirmed
    as an official Fan Token™ through primary source verification in
    SportMind's dataset. Proceed with standard intelligence frameworks.
    
  REGISTRY ABSENCE SIGNAL:
    If a token claiming sports affiliation does NOT appear in registry files:
    This is a RISK SIGNAL — not a definitive fraud classification.
    Proceed to four-source verification methodology.
    
  REGISTRY UPDATE PROTOCOL:
    Registry files are updated when new official partnerships are confirmed
    through Tier 1 primary sources.
    An asset absent from the registry may be a new legitimate token
    not yet documented, or it may be unverified.
    Treat registry absence as a trigger for verification, not a conclusion.
```

---

## National team token verification

```
NATIONAL TEAM TOKENS — ADDITIONAL VERIFICATION REQUIRED:

  WHY ADDITIONAL VERIFICATION IS NEEDED:
    National football associations are distinct legal entities from clubs.
    They have separate partnership agreements with Chiliz/Socios.
    National team tokens are particularly vulnerable to fraud during major
    tournaments — more details in fraud-risk-intelligence.md.
    
  CONFIRMED OFFICIAL NATIONAL TEAM FAN TOKENS™ (SportMind verified dataset):
  
    $ARG — Argentina National Team
      Verification: socios.com + chiliscan.com + AFA official channels confirmed
      Integration status: OFFICIAL_INTEGRATED — AFA partnership fully embedded
      Classification: confirmed official Fan Token™ · national team category
      
    $POR — Portugal National Team
      Verification: socios.com + chiliscan.com + FPF official channels confirmed
      
    $SNFT — Spain National Team
      Verification: socios.com + chiliscan.com + RFEF official channels confirmed
      
    $BFT — Brazil National Team
      Verification: socios.com + chiliscan.com + CBF official channels confirmed
      
  IMPORTANT — SCOPE OF THIS LIST:
    As of current library state, no other national team Fan Tokens™ have been
    confirmed in SportMind's verified dataset.
    Any token claiming to represent a national team not in this list should be
    treated as UNVERIFIED until confirmed through the four-source methodology.
    
  WORLD CUP AND MAJOR TOURNAMENT RISK:
    The highest-risk period for fraudulent national team tokens is the 4 weeks
    before and during major international tournaments.
    During these windows: apply additional verification steps for any national
    team token claim not on the above list.
    See: fan-token/fraud-risk-intelligence.md for tournament fraud amplification.

NATIONAL ASSOCIATION VERIFICATION STEP (additional to four-source):
  Step 5 (national teams only):
    Verify through the national football association's official channels
    (e.g. AFA, FPF, RFEF, CBF) independently of Socios/Chiliz.
    The national association should have published confirmation of the partnership.
    If the association has not independently confirmed: elevated risk signal.
```

---

## Compatibility

**Red flag framework:**  `fan-token/fraud-risk-intelligence.md`
**Registry files:**      `fan-token/registry/bridge-supported.md`
**Ecosystem health:**    `fan-token/ecosystem-health-intelligence.md`
**Agent chain:**         `core/agent-reasoning-chains.md`

---

*SportMind v3.97.44 · MIT License · sportmind.dev*
*Verification reasoning frameworks only — not legal determinations. Always verify through official primary sources.*
