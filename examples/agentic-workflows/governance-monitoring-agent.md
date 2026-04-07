# Agentic Workflow Pattern 8 — Governance Monitoring Agent

**Continuously monitors fan token governance proposals across a portfolio,
analyses each proposal against the GSI framework, generates briefings before
votes close, and tracks participation rates and LTUI impacts.**

This pattern operationalises the governance intelligence skill
(`fan-token/sports-governance-intelligence/`) as a continuous agent.
It ensures token holders never miss a vote, always have a SportMind
intelligence brief before deciding, and can track governance health
over time through GSI trends.

---

## Why governance deserves dedicated monitoring

Fan token governance is the mechanism through which token holders exercise
their commercial relationship with clubs. Most holders miss most votes —
platforms do not alert effectively, vote windows are short (often 48-72h),
and there is no intelligence layer that explains what a vote actually means
for LTUI before the window closes.

The governance monitoring agent solves this:

1. Detects new proposals before they are publicly announced (on-chain)
2. Immediately classifies Decision_Weight (Cosmetic / Operational / Commercial / Structural)
3. Generates a governance brief: what is the vote, what does YES vs NO mean for LTUI
4. Monitors participation rate and alerts if quorum is at risk
5. Records governance execution on-chain and updates LTUI projections post-vote

---

## The agent implementation

```python
# examples/agentic-workflows/governance_monitor.py
"""
SportMind Governance Monitoring Agent
Pattern 8: Continuous governance intelligence for fan token holders.

Monitors: Any Chiliz Chain fan tokens with governance
Cycle: Every 2 hours (governance votes can close quickly)
Autonomy: Level 1 (advisory — generates briefs; never votes autonomously)
"""
import asyncio
import logging
import json
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import aiohttp

SPORTMIND_API = "http://localhost:8080"
ALERT_WEBHOOK = ""
GOVERNANCE_CYCLE_HOURS = 2

log = logging.getLogger("sportmind.governance-monitor")


# ── Governance proposal model ──────────────────────────────────────────────────

@dataclass
class GovernanceProposal:
    """A single governance proposal with full SportMind intelligence context."""
    proposal_id:      str
    token_symbol:     str
    club_name:        str
    title:            str
    description:      str
    vote_opens:       str
    vote_closes:      str
    yes_votes:        float = 0.0
    no_votes:         float = 0.0
    total_supply:     float = 0.0

    # SportMind classification
    decision_weight:  Optional[float] = None  # 0.00-1.00
    decision_type:    Optional[str] = None    # Cosmetic/Operational/Commercial/Structural
    ltui_yes:         Optional[float] = None  # projected LTUI change if YES passes
    ltui_no:          Optional[float] = None  # projected LTUI change if NO passes
    governance_theatre: bool = False
    gsi_score:        Optional[float] = None

    # Tracking
    brief_generated:  bool = False
    brief_sent_at:    Optional[str] = None
    outcome:          Optional[str] = None    # YES/NO/QUORUM_FAILED
    outcome_recorded: bool = False

    def hours_remaining(self) -> float:
        closes = datetime.fromisoformat(self.vote_closes.replace('Z', '+00:00'))
        return max(0, (closes - datetime.now(timezone.utc)).total_seconds() / 3600)

    def participation_rate(self) -> float:
        if self.total_supply == 0:
            return 0.0
        return (self.yes_votes + self.no_votes) / self.total_supply

    def is_urgent(self) -> bool:
        return self.hours_remaining() <= 12

    def is_quorum_at_risk(self, quorum_threshold: float = 0.10) -> bool:
        """Returns True if current participation is below quorum threshold."""
        return self.participation_rate() < quorum_threshold and self.hours_remaining() <= 6


# ── Decision weight classifier ─────────────────────────────────────────────────

class DecisionWeightClassifier:
    """
    Classifies governance proposals by Decision Weight and type.
    Based on fan-token/sports-governance-intelligence/ framework.
    """

    # Keywords indicating governance theatre (do not act as signal)
    THEATRE_KEYWORDS = [
        "kit colour", "jersey design", "mascot name", "logo poll",
        "song choice", "nickname", "warm-up playlist"
    ]

    # Keywords indicating structural (highest weight) decisions
    STRUCTURAL_KEYWORDS = [
        "stadium naming", "share sale", "ownership", "merger",
        "administration", "transfer budget allocation", "major sponsor"
    ]

    # Keywords indicating commercial decisions
    COMMERCIAL_KEYWORDS = [
        "sponsorship", "partnership", "commercial", "revenue",
        "broadcast", "licensing", "merchandise exclusive"
    ]

    # Keywords indicating operational decisions
    OPERATIONAL_KEYWORDS = [
        "ticket allocation", "training ground", "community programme",
        "academy", "staff", "facility"
    ]

    def classify(self, title: str, description: str) -> dict:
        """
        Returns decision_weight, decision_type, governance_theatre flag,
        and LTUI_YES / LTUI_NO projections.
        """
        text = (title + " " + description).lower()

        # Theatre check first
        for keyword in self.THEATRE_KEYWORDS:
            if keyword in text:
                return {
                    "decision_weight":    0.05,
                    "decision_type":      "Cosmetic",
                    "governance_theatre": True,
                    "ltui_yes":           0.5,
                    "ltui_no":            0.5,
                    "gsi_note":           "Cosmetic governance — no LTUI signal"
                }

        # Structural
        for keyword in self.STRUCTURAL_KEYWORDS:
            if keyword in text:
                return {
                    "decision_weight":    0.90,
                    "decision_type":      "Structural",
                    "governance_theatre": False,
                    "ltui_yes":           8.0,  # Structural decisions significantly move LTUI
                    "ltui_no":            -3.0,
                    "gsi_note":           "Structural governance — major LTUI signal"
                }

        # Commercial
        for keyword in self.COMMERCIAL_KEYWORDS:
            if keyword in text:
                return {
                    "decision_weight":    0.70,
                    "decision_type":      "Commercial",
                    "governance_theatre": False,
                    "ltui_yes":           4.0,
                    "ltui_no":            -1.0,
                    "gsi_note":           "Commercial governance — meaningful LTUI signal"
                }

        # Operational
        for keyword in self.OPERATIONAL_KEYWORDS:
            if keyword in text:
                return {
                    "decision_weight":    0.45,
                    "decision_type":      "Operational",
                    "governance_theatre": False,
                    "ltui_yes":           2.0,
                    "ltui_no":            -0.5,
                    "gsi_note":           "Operational governance — moderate LTUI signal"
                }

        # Default: unknown operational
        return {
            "decision_weight":    0.35,
            "decision_type":      "Operational",
            "governance_theatre": False,
            "ltui_yes":           1.5,
            "ltui_no":            -0.3,
            "gsi_note":           "Classification uncertain — moderate weight applied"
        }


# ── Governance brief generator ─────────────────────────────────────────────────

class GovernanceBriefGenerator:
    """
    Generates SportMind governance intelligence briefs for proposals.
    Level 1 advisory — always states clearly that the vote decision is the holder's.
    """

    def generate(self, proposal: GovernanceProposal) -> str:
        """Generate a complete governance intelligence brief."""

        hours = proposal.hours_remaining()
        participation = proposal.participation_rate() * 100

        lines = [
            f"═══════════════════════════════════════════════════",
            f"GOVERNANCE INTELLIGENCE BRIEF",
            f"SportMind Pattern 8 — Level 1 Advisory",
            f"═══════════════════════════════════════════════════",
            f"",
            f"Token:      ${proposal.token_symbol}  ({proposal.club_name})",
            f"Proposal:   {proposal.title}",
            f"Vote closes: {proposal.vote_closes} ({hours:.1f}h remaining)",
            f"",
            f"═══════════════════════════════════════════════════",
            f"SPORTMIND CLASSIFICATION",
            f"═══════════════════════════════════════════════════",
            f"",
            f"Decision type:   {proposal.decision_type}",
            f"Decision weight: {proposal.decision_weight:.2f} / 1.00",
        ]

        if proposal.governance_theatre:
            lines += [
                f"",
                f"⚠️  GOVERNANCE THEATRE DETECTED",
                f"This proposal is cosmetic — it has no material impact on",
                f"token utility or club commercial decisions.",
                f"SportMind does not generate LTUI signals for cosmetic votes.",
                f"Participating is fine; this vote does not affect your holding thesis.",
            ]
        else:
            lines += [
                f"",
                f"═══════════════════════════════════════════════════",
                f"LTUI IMPACT PROJECTIONS",
                f"═══════════════════════════════════════════════════",
                f"",
                f"If YES passes: LTUI {'+' if proposal.ltui_yes >= 0 else ''}{proposal.ltui_yes:.1f}",
                f"If NO passes:  LTUI {'+' if proposal.ltui_no >= 0 else ''}{proposal.ltui_no:.1f}",
                f"",
                f"What this means:",
            ]
            if proposal.decision_type == "Structural":
                lines += [
                    f"  This is a structural governance decision.",
                    f"  It will materially affect the club's commercial trajectory.",
                    f"  The LTUI impact is significant and long-lasting.",
                    f"  Read the full proposal carefully before voting.",
                ]
            elif proposal.decision_type == "Commercial":
                lines += [
                    f"  This commercial decision affects token holder utility.",
                    f"  YES creates a new partnership/revenue stream for holders.",
                    f"  Consider whether the commercial terms benefit token holders.",
                ]
            else:
                lines += [
                    f"  This operational decision has moderate token utility impact.",
                    f"  Standard governance participation — vote according to your view.",
                ]

        lines += [
            f"",
            f"═══════════════════════════════════════════════════",
            f"PARTICIPATION STATUS",
            f"═══════════════════════════════════════════════════",
            f"",
            f"Current participation: {participation:.1f}%",
            f"Current: YES {proposal.yes_votes:,.0f} / NO {proposal.no_votes:,.0f}",
        ]

        if proposal.is_quorum_at_risk():
            lines += [
                f"",
                f"⚠️  QUORUM AT RISK",
                f"Participation is below 10% with less than 6 hours remaining.",
                f"If quorum is not reached, the vote may fail regardless of YES/NO split.",
                f"Alerting all monitored holders.",
            ]

        if hours <= 12:
            lines += [
                f"",
                f"🔔 URGENT: Vote closes in {hours:.1f} hours",
            ]

        lines += [
            f"",
            f"═══════════════════════════════════════════════════",
            f"IMPORTANT",
            f"═══════════════════════════════════════════════════",
            f"",
            f"This is a Level 1 advisory. SportMind provides intelligence",
            f"context. The vote decision is yours. SportMind never submits",
            f"governance votes autonomously — that would be Level 0 only.",
            f"",
            f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        ]

        return "\n".join(lines)


# ── The governance monitoring agent ───────────────────────────────────────────

class GovernanceMonitorAgent:
    """
    Continuous governance monitoring agent.
    Detects, classifies, briefs, and tracks governance proposals.
    Level 1 autonomy — advisory only; never votes.
    """

    def __init__(self, monitored_tokens: list[str]):
        self.tokens      = monitored_tokens
        self.proposals   = {}   # {proposal_id: GovernanceProposal}
        self.classifier  = DecisionWeightClassifier()
        self.brief_gen   = GovernanceBriefGenerator()
        self.cycle_count = 0
        self.briefs_sent = 0

    async def run(self):
        """Main monitoring loop."""
        log.info(f"Governance Monitor — {self.tokens}")
        while True:
            try:
                await self._run_cycle()
            except Exception as e:
                log.error(f"Cycle error: {e}")
            await asyncio.sleep(GOVERNANCE_CYCLE_HOURS * 3600)

    async def _run_cycle(self):
        """Single governance monitoring cycle."""
        self.cycle_count += 1
        log.info(f"── Governance Cycle {self.cycle_count} ──")

        for token in self.tokens:
            # Check for new proposals (on-chain or platform API)
            new_proposals = await self._fetch_new_proposals(token)
            for proposal in new_proposals:
                await self._process_new_proposal(proposal)

            # Check open proposals for urgency
            open_proposals = [p for p in self.proposals.values()
                              if p.token_symbol == token
                              and p.outcome is None
                              and p.hours_remaining() > 0]
            for proposal in open_proposals:
                await self._check_urgency(proposal)

            # Record closed proposal outcomes
            closed = [p for p in open_proposals if p.hours_remaining() <= 0]
            for proposal in closed:
                await self._record_outcome(proposal)

    async def _process_new_proposal(self, proposal: GovernanceProposal):
        """Classify and brief a new proposal."""
        # Classify the decision
        classification = self.classifier.classify(
            proposal.title, proposal.description
        )
        proposal.decision_weight    = classification["decision_weight"]
        proposal.decision_type      = classification["decision_type"]
        proposal.governance_theatre = classification["governance_theatre"]
        proposal.ltui_yes           = classification["ltui_yes"]
        proposal.ltui_no            = classification["ltui_no"]

        self.proposals[proposal.proposal_id] = proposal

        # Generate and send brief for non-theatre proposals
        if not proposal.governance_theatre:
            brief = self.brief_gen.generate(proposal)
            await self._send_brief(proposal, brief)

        log.info(
            f"NEW PROPOSAL: ${proposal.token_symbol} — {proposal.title} "
            f"({proposal.decision_type}, weight={proposal.decision_weight:.2f})"
        )

    async def _check_urgency(self, proposal: GovernanceProposal):
        """Alert on urgent proposals."""
        if proposal.is_urgent() and not proposal.brief_generated:
            brief = self.brief_gen.generate(proposal)
            await self._send_brief(proposal, brief, urgent=True)

        if proposal.is_quorum_at_risk():
            log.warning(f"QUORUM AT RISK: ${proposal.token_symbol} — {proposal.title}")
            await self._send_alert({
                "type":     "quorum_at_risk",
                "token":    proposal.token_symbol,
                "proposal": proposal.title,
                "hours_remaining": proposal.hours_remaining(),
                "participation": proposal.participation_rate()
            })

    async def _record_outcome(self, proposal: GovernanceProposal):
        """Record the outcome of a closed proposal."""
        # Fetch final vote counts (from on-chain or platform API)
        # REPLACE with your live governance data source
        if proposal.yes_votes > proposal.no_votes:
            proposal.outcome = "YES"
        else:
            proposal.outcome = "NO"

        proposal.outcome_recorded = True

        log.info(
            f"OUTCOME: ${proposal.token_symbol} — {proposal.title}: "
            f"{proposal.outcome} "
            f"(participation: {proposal.participation_rate()*100:.1f}%)"
        )

        # Log for calibration
        record = {
            "token":          proposal.token_symbol,
            "proposal":       proposal.title,
            "decision_type":  proposal.decision_type,
            "outcome":        proposal.outcome,
            "participation":  proposal.participation_rate(),
            "ltui_impact":    (proposal.ltui_yes if proposal.outcome == "YES"
                               else proposal.ltui_no),
            "recorded_at":    datetime.now(timezone.utc).isoformat()
        }
        Path("governance_outcomes.jsonl").open("a").write(
            json.dumps(record) + "\n"
        )

    async def _fetch_new_proposals(self, token: str) -> list[GovernanceProposal]:
        """
        Fetch new governance proposals for a token.
        REPLACE with your governance data source:
        - Chiliz Chain governance contract events
        - Socios API (if available)
        - Your own governance database
        """
        # STUB — replace with live governance detection
        return []

    async def _send_brief(self, proposal: GovernanceProposal, brief: str,
                           urgent: bool = False):
        """Send governance brief to holders."""
        proposal.brief_generated = True
        proposal.brief_sent_at   = datetime.now(timezone.utc).isoformat()
        self.briefs_sent += 1

        prefix = "🚨 URGENT — " if urgent else ""
        log.info(f"{prefix}GOVERNANCE BRIEF SENT: ${proposal.token_symbol} — {proposal.title}")

        if ALERT_WEBHOOK:
            try:
                async with aiohttp.ClientSession() as s:
                    await s.post(ALERT_WEBHOOK, json={
                        "text":     f"{prefix}Governance Brief: ${proposal.token_symbol}",
                        "brief":    brief,
                        "urgent":   urgent
                    })
            except Exception as e:
                log.error(f"Alert failed: {e}")

    async def _send_alert(self, alert: dict):
        if ALERT_WEBHOOK:
            try:
                async with aiohttp.ClientSession() as s:
                    await s.post(ALERT_WEBHOOK, json=alert)
            except: pass

    def get_status(self) -> dict:
        """Observable state for sportmind_agent_status MCP tool."""
        open_proposals = [p for p in self.proposals.values() if p.outcome is None]
        structural     = [p for p in open_proposals if p.decision_type == "Structural"]
        return {
            "agent_id":          "governance-monitor-001",
            "agent_type":        "governance_monitor",
            "state":             "MONITORING",
            "autonomy_level":    1,
            "tokens_monitored":  len(self.tokens),
            "open_proposals":    len(open_proposals),
            "structural_open":   len(structural),
            "total_proposals":   len(self.proposals),
            "briefs_sent":       self.briefs_sent,
            "cycle_count":       self.cycle_count,
        }


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")
    agent = GovernanceMonitorAgent(tokens=["PSG", "BAR", "CITY"])
    asyncio.run(agent.run())
```

---

## Decision Weight in practice

```
EXAMPLES BY DECISION TYPE:

STRUCTURAL (weight 0.80-1.00) — always generate brief, maximum LTUI signal:
  "Vote on whether to allow a partial share sale to new investors"
  "Approve stadium naming rights deal with [Sponsor]"
  "Vote on executive board composition change"
  LTUI impact: YES +6-12, NO -3-8

COMMERCIAL (weight 0.55-0.75) — generate brief, significant LTUI signal:
  "Approve official kit sponsor for 2027-28 season"
  "Vote on exclusive NFT partnership with [Platform]"
  "Approve community foundation donation budget"
  LTUI impact: YES +2-6, NO -1-3

OPERATIONAL (weight 0.30-0.55) — brief on request, moderate LTUI signal:
  "Approve new training ground facilities development"
  "Vote on community match ticket allocation policy"
  LTUI impact: YES +0.5-2, NO -0.5-1

COSMETIC (weight 0.00-0.30) — governance_theatre flag, no LTUI signal:
  "Choose new kit colour for third strip"
  "Vote on mascot name change"
  "Select warm-up playlist for home games"
  LTUI impact: negligible (0.5 each direction maximum)
```

---

## Safety principles for governance agents

```
LEVEL 1 AUTONOMY IS MANDATORY FOR GOVERNANCE.
This is a hard limit regardless of deployment context.

Why:
  Governance votes are legal attestations. In jurisdictions where fan tokens
  are regulated financial instruments (MiCA applies from Jan 2025 in EU),
  an autonomous vote could constitute a regulated financial action.
  Even where tokens are clearly utility tokens, voting someone else's tokens
  without explicit, per-vote authorisation is fundamentally wrong.

What this means:
  The governance monitor generates briefs, tracks proposals, and alerts on urgency.
  It NEVER submits votes, NEVER pre-commits votes, NEVER votes "on the holder's behalf"
  even if the holder has said "always vote YES on commercial proposals."
  
  Per-vote authorisation is the only acceptable model.
  
  If a holder wants automation: they should vote themselves after reviewing the brief.
  If they want an agent to vote: Level 0 (supervised) only — human confirms each vote.
```

---

## Compatibility

**Governance intelligence:** `fan-token/sports-governance-intelligence/` — GSI, Decision_Weight
**Fan sentiment CDI:** `fan-token/fan-sentiment-intelligence/` — post-vote engagement arc
**On-chain events:** `fan-token/on-chain-event-intelligence/` — pre-vote on-chain signals
**Agent framework:** `core/autonomous-agent-framework.md` — Level 1 autonomy constraints
**Chiliz Agent Kit:** `platform/chiliz-agent-kit-integration.md` — Pattern 3 (vote execution when approved)

*MIT License · SportMind · sportmind.dev*
