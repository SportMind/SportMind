# App Blueprint 10 — Fan Digital Twin

**An AI agent that builds, maintains, and updates a dynamic fan identity
NFT based on a fan's engagement behaviour, sporting outcomes, and
SportMind intelligence signals.**

This is the tenth SportMind application blueprint. It represents the
intersection of fan identity, AI intelligence, and on-chain dynamic NFTs —
the "Agentic Fan Identity" model first outlined in the SportFi ecosystem.

---

## The concept

A fan's relationship with their club evolves over time. They watch matches,
vote on governance proposals, hold tokens through trophy wins and relegations,
attend games, and engage with content. Currently, none of this history is
captured in a form that (a) belongs to the fan, (b) updates dynamically,
and (c) generates commercial value based on the depth of that history.

A Fan Digital Twin changes this. It is a dynamic NFT whose metadata is
updated by a SportMind agent based on:
- Sporting outcomes (trophies, relegations, historic matches)
- Fan behaviour (governance participation, token holding duration, event attendance)
- Commercial context (what the fan's engagement history is worth commercially)

The SportMind agent provides the intelligence layer — it knows what outcomes
are significant, how long commercial windows last, and what a fan's historical
engagement means in terms of LTUI and CDI. The dynamic NFT is the on-chain
record. The fan owns both.

---

## Architecture

```
FAN DIGITAL TWIN STACK:

DATA LAYER (inputs to the SportMind agent):
  → Token holding history (wallet data from Chiliz Chain)
  → Governance vote record (on-chain — transparent and verifiable)
  → Match attendance (stadium NFC check-in or QR scan — off-chain)
  → Content engagement (optional — app SDK or social API)
  → Commercial event context (SportMind library — what events matter)

INTELLIGENCE LAYER (SportMind agent):
  → Evaluates what fan activity is commercially significant
  → Applies CDI model to determine how long events remain relevant
  → Computes Fan Loyalty Score (FLS) from engagement history
  → Determines NFT tier eligibility based on current FLS
  → Generates narrative description of the fan's history

ON-CHAIN LAYER (Chiliz Chain):
  → Dynamic NFT (ERC-1155 or equivalent) with updateable metadata
  → Metadata stored off-chain (IPFS) with on-chain hash
  → Agent updates metadata; fan owns the NFT; nobody else can modify it

DISPLAY LAYER (SportFi Kit or custom):
  → Renders the fan's digital twin in their profile
  → Shows evolution over time (past trophies, governance history)
  → Token-gated content access based on FLS tier
```

---

## Fan Loyalty Score (FLS)

```
FLS measures the depth and duration of a fan's engagement with their club.

FLS = (Holding_Duration × 0.30) + (Governance_Participation × 0.25)
    + (Outcome_Engagement × 0.25) + (Commercial_Participation × 0.20)

HOLDING_DURATION:
  < 30 days:      0.20 (new holder)
  30-180 days:    0.50 (developing)
  180-365 days:   0.75 (committed)
  > 365 days:     0.90 (loyal)
  > 2 years:      1.00 (core fan)
  
  Bonus: holding through a relegation without selling: × 1.20
  (shows genuine club loyalty, not pure speculation)

GOVERNANCE_PARTICIPATION:
  0 votes cast:                   0.00
  Voted in < 25% of proposals:    0.30
  Voted in 25-75% of proposals:   0.65
  Voted in > 75% of proposals:    0.90
  Voted in all proposals:         1.00
  
  Quality modifier: voted on Structural decisions (not just cosmetic): × 1.15

OUTCOME_ENGAGEMENT:
  Tracked by SportMind CDI events active during the fan's holding period.
  Each major outcome contributes based on its CDI and whether the fan
  was a holder at the time.
  
  Trophy win during holding period:   + 0.20 (FLS permanent component)
  Relegation survived as holder:      + 0.15 (loyalty signal)
  Derby victory as holder:            + 0.05 per derby
  Maximum: 1.00 (capped)

COMMERCIAL_PARTICIPATION:
  Used token for merchandise/event access:  + 0.25
  Participated in sponsored experience:     + 0.25
  Referred new token holder (verified):     + 0.15
  Attended stadium event as token holder:   + 0.20
  
  Maximum: 1.00 (capped)

FLS TIERS:
  0.00 - 0.25: Prospect (new or inactive)
  0.25 - 0.50: Supporter
  0.50 - 0.70: Enthusiast
  0.70 - 0.85: Loyalist
  0.85 - 0.95: Ultra
  0.95 - 1.00: Legend
```

---

## Dynamic NFT metadata structure

```json
{
  "name": "PSG Fan Twin — [FAN_ID]",
  "description": "Dynamic fan identity NFT updated by SportMind agent",
  "image": "ipfs://[CURRENT_VISUAL_HASH]",
  
  "attributes": [
    {"trait_type": "Club", "value": "Paris Saint-Germain"},
    {"trait_type": "Fan Loyalty Score", "value": 0.82, "display_type": "number"},
    {"trait_type": "Fan Tier", "value": "Loyalist"},
    {"trait_type": "Holder Since", "value": "2023-09-15", "display_type": "date"},
    {"trait_type": "Holding Duration Days", "value": 568, "display_type": "number"},
    {"trait_type": "Governance Votes Cast", "value": 14},
    {"trait_type": "Governance Participation Rate", "value": "87%"},
    {"trait_type": "Trophies Witnessed", "value": 1, "note": "Ligue 1 2024-25"},
    {"trait_type": "Derbies Witnessed", "value": 3},
    {"trait_type": "Commercial Events", "value": 2}
  ],
  
  "sportmind_context": {
    "ltui_contribution": 12.4,
    "fls": 0.82,
    "fls_tier": "Loyalist",
    "narrative": "This fan has held $PSG through one trophy, three Paris derbies, and 14 governance votes. Their loyalty was tested during the exit from the UCL Round of 16 and they held. That history is recorded here, permanently.",
    "last_updated": "2026-04-05T10:00:00Z",
    "next_update_trigger": "After next significant event or 30 days",
    "sportmind_version": "3.21.0"
  }
}
```

---

## The SportMind agent implementation

```python
# fan_digital_twin_agent.py
"""
SportMind Fan Digital Twin Agent.
Monitors fan engagement and updates dynamic NFT metadata.
Level 2 autonomy: updates metadata autonomously; alerts for significant milestones.
"""
import asyncio
import json
import hashlib
from datetime import datetime, timezone
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import aiohttp

SPORTMIND_API = "http://localhost:8080"

@dataclass
class FanProfile:
    """Complete fan engagement profile for FLS computation."""
    fan_id:              str
    token_symbol:        str
    wallet_address:      str
    
    # Engagement data (fetched from Chiliz Chain + application database)
    holder_since:        str
    holding_days:        int
    current_balance:     float
    governance_votes:    int
    total_proposals:     int
    trophies_as_holder:  list = field(default_factory=list)
    derbies_as_holder:   int = 0
    commercial_events:   int = 0
    survived_relegation: bool = False
    
    # Computed by agent
    fls:                 float = 0.0
    fls_tier:            str = "Prospect"
    narrative:           str = ""

class FanDigitalTwinAgent:
    """
    SportMind agent that monitors fan engagement and maintains
    dynamic NFT metadata for fan digital twins.
    """

    def __init__(self, club_config: dict):
        self.club         = club_config["club"]
        self.token        = club_config["token_symbol"]
        self.sport        = club_config["sport"]
        self.fans         = {}  # {wallet_address: FanProfile}
        self.macro_modifier = 1.00

    async def compute_fls(self, fan: FanProfile) -> float:
        """Compute Fan Loyalty Score from engagement data."""
        # Holding duration component
        if fan.holding_days >= 730:      holding = 1.00
        elif fan.holding_days >= 365:    holding = 0.90
        elif fan.holding_days >= 180:    holding = 0.75
        elif fan.holding_days >= 30:     holding = 0.50
        else:                            holding = 0.20

        if fan.survived_relegation:
            holding = min(1.00, holding * 1.20)

        # Governance participation
        if fan.total_proposals == 0:     governance = 0.00
        else:
            rate = fan.governance_votes / fan.total_proposals
            if rate >= 1.0:             governance = 1.00
            elif rate >= 0.75:          governance = 0.90
            elif rate >= 0.25:          governance = 0.65
            else:                       governance = 0.30

        # Outcome engagement (from SportMind CDI events)
        outcome = min(1.00,
            len(fan.trophies_as_holder) * 0.20 +
            (0.15 if fan.survived_relegation else 0) +
            fan.derbies_as_holder * 0.05
        )

        # Commercial participation
        commercial = min(1.00, fan.commercial_events * 0.25)

        # Weighted sum
        fls = (holding * 0.30 + governance * 0.25 +
               outcome * 0.25 + commercial * 0.20)
        return round(fls, 3)

    def classify_fls_tier(self, fls: float) -> str:
        if fls >= 0.95:    return "Legend"
        elif fls >= 0.85:  return "Ultra"
        elif fls >= 0.70:  return "Loyalist"
        elif fls >= 0.50:  return "Enthusiast"
        elif fls >= 0.25:  return "Supporter"
        else:              return "Prospect"

    async def generate_narrative(self, fan: FanProfile) -> str:
        """Generate a narrative description of the fan's history using SportMind context."""
        parts = [f"This fan has held ${fan.token_symbol} for {fan.holding_days} days."]

        if fan.trophies_as_holder:
            parts.append(f"They witnessed {len(fan.trophies_as_holder)} trophy win(s): {', '.join(fan.trophies_as_holder)}.")

        if fan.governance_votes > 0:
            parts.append(f"They have voted in {fan.governance_votes} governance proposals — their voice has shaped club decisions.")

        if fan.survived_relegation:
            parts.append("They held through relegation. That loyalty is recorded here permanently.")

        if fan.derbies_as_holder > 0:
            parts.append(f"They have witnessed {fan.derbies_as_holder} derby match(es) as a token holder.")

        return " ".join(parts)

    async def update_fan_nft(self, fan: FanProfile):
        """Compute FLS, generate metadata, update NFT."""
        fan.fls       = await self.compute_fls(fan)
        fan.fls_tier  = self.classify_fls_tier(fan.fls)
        fan.narrative = await self.generate_narrative(fan)

        metadata = {
            "name": f"{self.club} Fan Twin — {fan.fan_id}",
            "description": "Dynamic fan identity NFT updated by SportMind agent",
            "attributes": [
                {"trait_type": "Club",                "value": self.club},
                {"trait_type": "Fan Loyalty Score",   "value": fan.fls,             "display_type": "number"},
                {"trait_type": "Fan Tier",            "value": fan.fls_tier},
                {"trait_type": "Holding Duration Days","value": fan.holding_days,   "display_type": "number"},
                {"trait_type": "Governance Votes",    "value": fan.governance_votes},
                {"trait_type": "Trophies Witnessed",  "value": len(fan.trophies_as_holder)},
            ],
            "sportmind_context": {
                "fls":               fan.fls,
                "fls_tier":          fan.fls_tier,
                "narrative":         fan.narrative,
                "last_updated":      datetime.now(timezone.utc).isoformat(),
                "sportmind_version": "3.21.0"
            }
        }

        # In production: upload to IPFS, update on-chain hash
        metadata_hash = hashlib.sha256(json.dumps(metadata).encode()).hexdigest()
        print(f"[{fan.fan_id}] FLS: {fan.fls} ({fan.fls_tier}) | Metadata hash: {metadata_hash[:16]}...")

        # Milestone alerts
        if fan.fls >= 0.85 and fan.fls_tier == "Ultra":
            print(f"🏆 MILESTONE: {fan.fan_id} reached Ultra tier!")

        return metadata

    async def run(self, update_interval_hours: int = 24):
        """Run continuous update cycle."""
        while True:
            for fan in self.fans.values():
                await self.update_fan_nft(fan)
            await asyncio.sleep(update_interval_hours * 3600)
```

---

## Token-gated experiences based on FLS tier

```
FLS TIER → ACCESS RIGHTS:

Prospect (< 0.25):
  Basic: Token holder content (standard token-gating)
  
Supporter (0.25-0.50):
  + Priority governance notification (24h before public announcement)
  + Supporter Discord channel access
  
Enthusiast (0.50-0.70):
  + Reduced merchandise discount (5%)
  + Enthusiast-only voting events
  
Loyalist (0.70-0.85):
  + Priority match ticket access
  + Loyalist exclusive content (behind the scenes)
  + 10% merchandise discount
  
Ultra (0.85-0.95):
  + Player meet-and-greet ballot eligibility
  + 15% merchandise discount
  + Training ground visit ballot
  + Named in club's digital history records
  
Legend (> 0.95):
  + Permanent record in club history (on-chain, unremovable)
  + 20% merchandise discount
  + Priority for rare experiences (final day access, stadium naming input)
  + Physical commemoration (club sends physical memento)

IMPLEMENTATION (SportFi Kit):
  Use FLS tier from NFT metadata as the token-gating parameter
  Replace simple "holds token" checks with "FLS tier >= X" checks
  See: examples/applications/app-07-sportfi-kit-integration.md
```

---

## Ethical considerations

```
DATA OWNERSHIP AND PRIVACY:

The fan OWNS their digital twin NFT.
  The club cannot delete it. The platform cannot modify it.
  It is on-chain, immutable (except when the fan's own agent updates it).

What data the SportMind agent accesses:
  → On-chain: wallet balance, governance votes (fully public)
  → App-reported: attendance (fan provides this via check-in)
  → Application: commercial events (fan consents at point of purchase)
  → NOT accessed: social media private data, financial information, location

Opt-out:
  Fan can choose not to have a digital twin
  Fan can request their digital twin be burned (token destroyed)
  Historical records remain on-chain even after burn (this is the blockchain)
  
Transparency:
  Every update to the NFT metadata is triggered by the SportMind agent
  and the trigger event is logged. Fans can see exactly why their FLS
  changed (which governance vote, which trophy, which attendance event).
  
The design principle: this system should make fans feel recognised,
not surveilled. The narrative generated by SportMind should read like
a record of their loyalty, not a commercial profile.
```

---

## Compatibility

**Autonomous agent framework:** `core/autonomous-agent-framework.md`
**Fan sentiment CDI:** `fan-token/fan-sentiment-intelligence/` — outcome engagement scoring
**Governance intelligence:** `fan-token/sports-governance-intelligence/` — governance participation
**On-chain events:** `fan-token/on-chain-event-intelligence/` — wallet behaviour data
**SportFi Kit:** `examples/applications/app-07-sportfi-kit-integration.md` — execution layer
**Chiliz Agent Kit:** `platform/chiliz-agent-kit-integration.md` — NFT update execution

*MIT License · SportMind · sportmind.dev*
