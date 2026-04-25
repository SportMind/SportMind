---
name: skill-discovery-protocol
description: >
  Dynamic skill stack selection for SportMind agents. Use when an agent needs
  to determine which skills to load for a given query context at runtime —
  rather than using a static pre-defined bundle. Covers the context signal
  taxonomy, the scoring model for skill relevance, the loading order rules,
  and the token budget negotiation algorithm. Extends platform/skill-bundles.md
  (static bundles) with a dynamic discovery layer. Use for sophisticated agents
  handling varied or unpredictable query contexts; use static bundles for
  well-defined single-use-case deployments.
---

# Skill Discovery Protocol — SportMind

**How an agent determines which of 481 files to load for a given query context
at runtime, without hard-coding the skill stack.**

`platform/skill-bundles.md` solves the common cases: if you know you are always
doing football fan token tier 1 analysis, load `ftier1-football`. That covers
most single-use-case deployments well.

The discovery protocol solves the harder cases: a portfolio monitoring agent
that might encounter any sport, any token lifecycle phase, any macro condition,
an active transfer window, a World Cup in progress, a disciplinary event, and
Fan Token™ Play — all at once. Static bundles cannot handle this. Dynamic
discovery can.

---

## Why static bundles are insufficient for general agents

```
STATIC BUNDLE — what it assumes:
  sport:    football
  use_case: fan_token_tier1
  context:  standard (no modifying conditions)

WHAT IT MISSES when context is non-standard:

  Fan Token Play active ($AFC):
    → REQUIRES: fan-token/gamified-tokenomics-intelligence/
    → REQUIRES: platform/chiliz-chain-address-intelligence.md (FanTokenPlayMonitor)
    → Static bundle: NEITHER loaded

  Transfer window open (August):
    → REQUIRES: fan-token/transfer-window-intelligence/
    → Static bundle: NOT loaded

  World Cup 2026 in progress:
    → REQUIRES: fan-token/world-cup-2026-intelligence/
    → MODIFIES: NCSI calculations throughout
    → Static bundle: NOT loaded

  Macro bear market (modifier 0.75):
    → GATE: all fan token signals reduced
    → No additional skills needed but MODIFIES loading priority
    → Static bundle: macro-overview.md loaded but CHZ virtuous cycle NOT

  Disciplinary event on key player:
    → REQUIRES: core/athlete-disciplinary-intelligence.md
    → REQUIRES: platform/fetch-mcp-disciplinary.md
    → Static bundle: NOT loaded

An agent loading only ftier1-football for $AFC in August 2026 during the
World Cup and transfer window simultaneously — is missing 4+ critical skills
and will produce an incomplete signal.
```

---

## The context signal taxonomy

Before selecting skills, an agent must classify the active context signals.
Context signals are boolean or tiered indicators derived from the current
query and environment state.

```
CONTEXT SIGNAL TAXONOMY:

SPORT CONTEXT (always present):
  sport:              string — primary sport for analysis
  use_case:           string — fan_token_tier1 | fan_token_tier2 | pre_match | commercial
  token_tier:         int 1-4 — from registry or KAYEN API

TOKEN MECHANICS CONTEXT:
  fan_token_play_active:    bool — PATH_2 pre-liquidation detected OR PATH_1 rollout
  gamified_token:           bool — confirmed via KAYEN API gamified flag
  lifecycle_phase:          int 1-6 — from fan-token-lifecycle skill

CALENDAR CONTEXT:
  transfer_window_active:   bool — July 1-Sep 1 (summer) or Jan 1-Feb 1 (winter)
  world_cup_active:         bool — June 11-July 19, 2026 (and future World Cups)
  major_tournament_active:  bool — Euros, Copa América, World Cup, Super Bowl, etc.
  match_window:             enum — T-72h | T-48h | T-2h | LIVE | T+2h | T+48h

ATHLETE CONTEXT:
  disciplinary_flag_active: bool — any DSM flag on a key player in this analysis
  lineup_unconfirmed:       bool — T-2h threshold not yet reached
  injury_warning_active:    bool — key player unavailable or doubtful

MACRO CONTEXT:
  macro_phase:              enum — BULL | NEUTRAL | BEAR | EXTREME_BEAR
  macro_override_active:    bool — modifier < 0.75
  chz_burn_cycle:           enum — LOW | MODERATE | HIGH | VERY_HIGH (quarterly)

MARKET CONTEXT:
  defi_liquidity_warning:   bool — pool TVL < $50k
  prediction_market_open:   bool — active prediction market for this event
  smart_wallet_signal:      bool — Category 1-4 on-chain signal detected
```

---

## The skill relevance scoring model

Each skill in the library has an implicit relevance score for a given context.
The discovery protocol makes this explicit.

```
RELEVANCE SCORE FORMULA:

relevance(skill, context) = base_score
                          + Σ context_signal_bonuses
                          - exclusion_penalty

BASE SCORES BY SKILL TYPE:
  macro/ files:           1.00  (always load — gates everything)
  market/{sport}.md:      0.90  (always load for the sport)
  sports/{sport}/:        0.85  (always load)
  athlete/{sport}/:       0.80  (always load)
  core/confidence-output-schema.md: 0.95  (always load last)

CONTEXT SIGNAL BONUSES (added to base score):

  fan_token_play_active = True:
    +0.90 → fan-token/gamified-tokenomics-intelligence/
    +0.85 → platform/chiliz-chain-address-intelligence.md
    +0.70 → fan-token/on-chain-event-intelligence/

  transfer_window_active = True:
    +0.85 → fan-token/transfer-window-intelligence/
    +0.60 → fan-token/transfer-intelligence/

  world_cup_active = True AND sport = football:
    +0.90 → fan-token/world-cup-2026-intelligence/
    +0.80 → market/world-cup-2026.md

  major_tournament_active = True:
    +0.70 → core/core-narrative-momentum.md
    +0.65 → fan-token/fan-sentiment-intelligence/

  disciplinary_flag_active = True:
    +0.90 → core/athlete-disciplinary-intelligence.md
    +0.80 → platform/fetch-mcp-disciplinary.md
    +0.75 → fan-token/disciplinary-sentiment-intelligence/

  macro_phase = BEAR OR EXTREME_BEAR:
    +0.70 → macro/macro-crypto-market-cycles.md (full, not just overview)

  chz_burn_cycle = HIGH OR VERY_HIGH:
    +0.65 → macro/macro-crypto-market-cycles.md (virtuous cycle section)

  prediction_market_open = True:
    +0.75 → core/prediction-market-intelligence.md

  smart_wallet_signal = True:
    +0.80 → fan-token/on-chain-event-intelligence/
    +0.70 → platform/chiliz-chain-address-intelligence.md

  match_window = T-48h AND fan_token_play_active:
    +0.95 → platform/chiliz-chain-address-intelligence.md
    (pre-liquidation window — highest priority)

EXCLUSION PENALTIES:
  lifecycle_phase = 5 OR 6:
    -0.50 → all fan-token commercial skills except lifecycle
    (token is post-partnership — commercial signals unreliable)

  macro_override_active = True:
    -1.00 → all sport domain and athlete skills
    (macro gate stops analysis — only macro file needed)

RELEVANCE THRESHOLD:
  score >= 0.70: LOAD (essential)
  score 0.40-0.69: LOAD IF BUDGET ALLOWS
  score < 0.40: SKIP (not relevant to this context)
```

---

## Token budget negotiation

Context-aware loading must respect the agent's token budget. The discovery
protocol negotiates between relevance and budget.

```
BUDGET TIERS:

FULL BUDGET (>80,000 tokens available):
  Load all skills with relevance >= 0.70
  Load compressed versions of skills 0.40-0.69
  Load confidence output schema last
  Typical result: 12-18 files

STANDARD BUDGET (40,000-80,000 tokens):
  Load all skills with relevance >= 0.70
  Skip skills 0.40-0.69 unless critical context signal active
  Use compressed versions for Layer 4 (market) and Layer 2 (athlete) if tight
  Typical result: 8-12 files

CONSTRAINED BUDGET (20,000-40,000 tokens):
  Load only skills with relevance >= 0.80
  Use compressed versions for all skills where available
  Load confidence schema in compressed form
  Typical result: 5-8 files (compressed)

MINIMAL BUDGET (<20,000 tokens):
  Load only: macro-overview.md + sport domain (compressed) + output schema
  Flag: SMS will be LOW — partial coverage only
  Typical result: 3 files (all compressed)

BUDGET NEGOTIATION ALGORITHM:
  1. Score all skills for current context
  2. Sort by relevance score descending
  3. Add skills to stack greedily until budget exhausted
  4. If budget exceeded: switch top skills to compressed versions
  5. If still exceeded: drop lowest-relevance skills above threshold
  6. Always keep: macro files + sport domain + output schema (non-negotiable)
  7. Return final stack with SMS estimate
```

---

## Discovery protocol implementation

```python
# platform/connectors/skill_discovery.py
"""
SportMind Skill Discovery Protocol
Dynamic context-aware skill stack selection.

Replaces hard-coded skill loading for agents handling variable contexts.
Use skill-bundles.md for fixed single-use-case deployments.

Requirements: pip install aiohttp
"""

from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum

ROOT = Path(__file__).parent.parent.parent  # SportMind repo root


class MacroPhase(str, Enum):
    BULL         = "BULL"
    NEUTRAL      = "NEUTRAL"
    BEAR         = "BEAR"
    EXTREME_BEAR = "EXTREME_BEAR"


class MatchWindow(str, Enum):
    T_MINUS_72H = "T-72h"
    T_MINUS_48H = "T-48h"
    T_MINUS_2H  = "T-2h"
    LIVE        = "LIVE"
    T_PLUS_2H   = "T+2h"
    T_PLUS_48H  = "T+48h"
    NONE        = "NONE"


@dataclass
class DiscoveryContext:
    """
    Context signals for skill discovery.
    Populate from MCP tool outputs and calendar state before calling discover().
    """
    # Required
    sport:    str
    use_case: str = "fan_token_tier1"

    # Token mechanics
    fan_token_play_active:  bool = False
    gamified_token:         bool = False
    lifecycle_phase:        int  = 3       # Default: assume active

    # Calendar
    transfer_window_active: bool  = False
    world_cup_active:       bool  = False
    major_tournament_active:bool  = False
    match_window:           MatchWindow = MatchWindow.NONE

    # Athlete
    disciplinary_flag_active: bool = False
    lineup_unconfirmed:       bool = False
    injury_warning_active:    bool = False

    # Macro
    macro_phase:          MacroPhase = MacroPhase.NEUTRAL
    macro_override_active:bool = False
    chz_burn_tier:        str  = "MODERATE"  # LOW|MODERATE|HIGH|VERY_HIGH

    # Market
    defi_liquidity_warning:  bool = False
    prediction_market_open:  bool = False
    smart_wallet_signal:     bool = False

    # Budget
    token_budget: int = 60_000   # Default: standard budget

    @classmethod
    def from_mcp_outputs(cls, macro_result: dict, lookup_result: dict,
                          sentiment_result: dict, sport: str,
                          use_case: str = "fan_token_tier1",
                          **calendar_kwargs) -> "DiscoveryContext":
        """
        Build context from MCP tool outputs.
        Call after: sportmind_macro(), sportmind_fan_token_lookup(),
                    sportmind_sentiment_snapshot()
        """
        macro_state  = macro_result.get("macro_state", {})
        crypto_cycle = macro_state.get("crypto_cycle", {})
        phase_str    = crypto_cycle.get("phase", "NEUTRAL")
        modifier     = crypto_cycle.get("macro_modifier", 1.0)

        token_data  = {}
        if lookup_result.get("found") and lookup_result.get("tokens"):
            token_data = lookup_result["tokens"][0]

        supply_mech = sentiment_result.get("sentiment_snapshot", {}).get(
            "supply_mechanics", {}
        )
        ftp_active  = supply_mech.get("status") == "GAMIFIED_CONFIRMED"

        lifecycle = 3
        fan_sent  = sentiment_result.get("sentiment_snapshot", {}).get(
            "fan_sentiment", {}
        )
        if "Phase" in fan_sent.get("note", ""):
            import re
            m = re.search(r"Phase (\d)", fan_sent["note"])
            if m:
                lifecycle = int(m.group(1))

        return cls(
            sport                  = sport,
            use_case               = use_case,
            fan_token_play_active  = ftp_active,
            gamified_token         = ftp_active,
            lifecycle_phase        = lifecycle,
            macro_phase            = MacroPhase(phase_str),
            macro_override_active  = modifier < 0.75,
            **calendar_kwargs,
        )


@dataclass
class ScoredSkill:
    path:      Path
    skill_id:  str
    relevance: float
    required:  bool = False   # True = cannot be dropped regardless of budget
    compressed_available: bool = False


class SkillDiscovery:
    """
    Dynamic skill stack selector for SportMind agents.

    Usage:
        ctx = DiscoveryContext(
            sport                 = "football",
            use_case              = "fan_token_tier1",
            fan_token_play_active = True,
            transfer_window_active= True,
            match_window          = MatchWindow.T_MINUS_48H,
            token_budget          = 50_000,
        )
        discovery = SkillDiscovery(root=ROOT)
        stack     = discovery.discover(ctx)

        for skill in stack.skills:
            print(skill.skill_id, skill.relevance)
    """

    def __init__(self, root: Path = ROOT):
        self.root = root

    def _p(self, *parts) -> Path:
        return self.root.joinpath(*parts)

    def discover(self, ctx: DiscoveryContext) -> "DiscoveredStack":
        """
        Return the optimal skill stack for the given context and token budget.
        """
        if ctx.macro_override_active:
            # Macro gate: only load macro files
            return DiscoveredStack(
                skills=[
                    ScoredSkill(
                        path      = self._p("macro", "macro-overview.md"),
                        skill_id  = "macro.overview",
                        relevance = 1.00,
                        required  = True,
                    )
                ],
                context        = ctx,
                sms_estimate   = 0,
                gate_reason    = "MACRO_OVERRIDE_ACTIVE — analysis halted",
            )

        candidates = self._score_all(ctx)
        stack      = self._negotiate_budget(candidates, ctx)
        sms        = self._estimate_sms(stack, ctx)

        return DiscoveredStack(
            skills       = stack,
            context      = ctx,
            sms_estimate = sms,
        )

    def _score_all(self, ctx: DiscoveryContext) -> list:
        slug = ctx.sport.replace("_", "-")
        scored = []

        def add(path, skill_id, base, required=False):
            if not Path(path).exists():
                return
            score = base

            # Context signal bonuses
            if ctx.fan_token_play_active:
                if "gamified-tokenomics" in str(path):
                    score += 0.90
                if "chiliz-chain-address" in str(path):
                    score += 0.85
                if "on-chain-event" in str(path):
                    score += 0.70
                # T-48h pre-liquidation window — maximum priority
                if "chiliz-chain-address" in str(path) and \
                   ctx.match_window == MatchWindow.T_MINUS_48H:
                    score += 0.10

            if ctx.transfer_window_active:
                if "transfer-window-intelligence" in str(path):
                    score += 0.85
                if "transfer-intelligence" in str(path) and \
                   "window" not in str(path):
                    score += 0.60

            if ctx.world_cup_active and ctx.sport == "football":
                if "world-cup-2026" in str(path):
                    score += 0.90
                if "market/world-cup" in str(path):
                    score += 0.80

            if ctx.major_tournament_active:
                if "narrative-momentum" in str(path):
                    score += 0.70
                if "fan-sentiment" in str(path):
                    score += 0.65

            if ctx.disciplinary_flag_active:
                if "athlete-disciplinary" in str(path):
                    score += 0.90
                if "fetch-mcp-disciplinary" in str(path):
                    score += 0.80
                if "disciplinary-sentiment" in str(path):
                    score += 0.75

            if ctx.macro_phase in (MacroPhase.BEAR, MacroPhase.EXTREME_BEAR):
                if "macro-crypto-market-cycles" in str(path):
                    score += 0.70

            if ctx.chz_burn_tier in ("HIGH", "VERY_HIGH"):
                if "macro-crypto-market-cycles" in str(path):
                    score += 0.65

            if ctx.prediction_market_open:
                if "prediction-market" in str(path):
                    score += 0.75

            if ctx.smart_wallet_signal:
                if "on-chain-event" in str(path):
                    score += 0.80
                if "chiliz-chain-address" in str(path):
                    score += 0.70

            # Exclusion penalties
            if ctx.lifecycle_phase in (5, 6):
                if "fan-token" in str(path) and \
                   "lifecycle" not in str(path) and \
                   "rwa" not in str(path):
                    score -= 0.50

            scored.append(ScoredSkill(
                path      = Path(path),
                skill_id  = skill_id,
                relevance = min(1.0, score),
                required  = required,
                compressed_available = Path(str(path).replace(
                    str(self.root), ""
                )).stem in self._compressed_index(),
            ))

        # ── Core non-negotiable skills (always loaded) ────────────────
        add(self._p("macro","macro-overview.md"),
            "macro.overview", 1.00, required=True)
        add(self._p("market",f"market-{slug}.md"),
            f"market.{slug}", 0.90, required=True)
        add(self._p("sports",slug,f"sport-domain-{slug}.md"),
            f"domain.{slug}", 0.85, required=True)
        add(self._p("core","confidence-output-schema.md"),
            "core.output-schema", 0.95, required=True)

        # ── Athlete layer ──────────────────────────────────────────────
        athlete_dir = self._p("athlete", slug)
        if athlete_dir.is_dir():
            for f in sorted(athlete_dir.glob("athlete-intel-*.md")):
                add(f, f"athlete.{slug}", 0.80)

        # ── Fan token layer ────────────────────────────────────────────
        if ctx.use_case in ("fan_token_tier1", "fan_token_tier2"):
            bridge = self._p("fan-token", f"{slug}-token-intelligence")
            if bridge.is_dir():
                for f in sorted(bridge.glob("*.md")):
                    add(f, f"fantoken.{slug}", 0.80)
            for skill_dir, skill_id, base in [
                ("defi-liquidity-intelligence",         "fantoken.defi",         0.75),
                ("fan-token-lifecycle",                 "fantoken.lifecycle",     0.75),
                ("fan-token-pulse",                     "fantoken.pulse",         0.70),
                ("on-chain-event-intelligence",         "fantoken.onchain",       0.55),
                ("gamified-tokenomics-intelligence",    "fantoken.gamified",      0.40),
                ("fan-sentiment-intelligence",          "fantoken.sentiment",     0.55),
                ("kol-influence-intelligence",          "fantoken.kol",           0.45),
                ("transfer-window-intelligence",        "fantoken.transfer-win",  0.30),
                ("world-cup-2026-intelligence",         "fantoken.wc2026",        0.20),
                ("disciplinary-sentiment-intelligence", "fantoken.dsm-sentiment", 0.30),
            ]:
                d = self._p("fan-token", skill_dir)
                if d.is_dir():
                    for f in sorted(d.glob("*.md")):
                        add(f, skill_id, base)

        # ── Core framework skills ──────────────────────────────────────
        for fname, skill_id, base in [
            ("core-athlete-modifier-system.md",   "core.modifier-system",  0.70),
            ("core-signal-weights-by-sport.md",   "core.signal-weights",   0.65),
            ("core-result-impact-matrices.md",    "core.result-matrices",  0.60),
            ("athlete-disciplinary-intelligence.md","core.dsm",            0.40),
            ("breaking-news-intelligence.md",     "core.breaking-news",    0.45),
            ("media-intelligence.md",             "core.media",            0.40),
            ("post-match-signal-framework.md",    "core.post-match",       0.40),
            ("prediction-market-intelligence.md", "core.prediction-mkt",   0.35),
        ]:
            add(self._p("core", fname), skill_id, base)

        # ── Platform skills ────────────────────────────────────────────
        for fname, skill_id, base in [
            ("chiliz-chain-address-intelligence.md","platform.address-intel", 0.35),
            ("fetch-mcp-disciplinary.md",           "platform.fetch-dsm",    0.30),
            ("social-intelligence-connector.md",    "platform.social",       0.30),
        ]:
            add(self._p("platform", fname), skill_id, base)

        # ── Macro deep dives ──────────────────────────────────────────
        for fname, skill_id, base in [
            ("macro-crypto-market-cycles.md",  "macro.crypto-cycles",  0.50),
            ("macro-geopolitical.md",          "macro.geopolitical",   0.40),
            ("macro-regulatory-sportfi.md",    "macro.regulatory",     0.35),
        ]:
            add(self._p("macro", fname), skill_id, base)

        return sorted(scored, key=lambda x: x.relevance, reverse=True)

    def _negotiate_budget(self, candidates: list, ctx: DiscoveryContext) -> list:
        """Select skills within token budget, respecting required skills."""
        # Estimate tokens per file (rough heuristic: 3 tokens per word, ~80 words/KB)
        def estimate_tokens(path: Path) -> int:
            try:
                size = path.stat().st_size
                return max(200, int(size / 4))
            except:
                return 800

        budget    = ctx.token_budget
        selected  = []
        used      = 0
        threshold = 0.70

        # First pass: required + above threshold
        for skill in candidates:
            if skill.relevance < threshold and not skill.required:
                continue
            tokens = estimate_tokens(skill.path)
            if used + tokens <= budget or skill.required:
                selected.append(skill)
                used += tokens

        # Second pass: if budget remaining, add 0.40-0.69 range
        if used < budget * 0.85:
            for skill in candidates:
                if skill.relevance >= 0.40 and skill.relevance < threshold:
                    if skill not in selected:
                        tokens = estimate_tokens(skill.path)
                        if used + tokens <= budget:
                            selected.append(skill)
                            used += tokens

        return sorted(selected, key=lambda x: x.relevance, reverse=True)

    def _estimate_sms(self, stack: list, ctx: DiscoveryContext) -> float:
        """Rough SMS estimate from loaded layers."""
        layer_coverage = len(stack) / 10.0  # rough proxy
        return min(100.0, layer_coverage * 70 + 20)

    def _compressed_index(self) -> set:
        """Skill IDs with compressed versions available."""
        # Read compressed/README.md to build index
        compressed_readme = self.root / "compressed" / "README.md"
        if not compressed_readme.exists():
            return set()
        content = compressed_readme.read_text()
        import re
        return set(re.findall(r'Full skill:\s*(\S+)', content))


@dataclass
class DiscoveredStack:
    """Output of skill discovery: ordered skill list + metadata."""
    skills:        list
    context:       DiscoveryContext
    sms_estimate:  float
    gate_reason:   str = ""

    @property
    def skill_paths(self) -> list:
        return [s.path for s in self.skills]

    @property
    def total_skills(self) -> int:
        return len(self.skills)

    def summary(self) -> dict:
        return {
            "total_skills":    self.total_skills,
            "sms_estimate":    round(self.sms_estimate, 1),
            "gate_reason":     self.gate_reason or None,
            "context_signals": {
                "fan_token_play_active":   self.context.fan_token_play_active,
                "transfer_window_active":  self.context.transfer_window_active,
                "world_cup_active":        self.context.world_cup_active,
                "disciplinary_flag_active":self.context.disciplinary_flag_active,
                "macro_phase":             self.context.macro_phase.value,
                "macro_override":          self.context.macro_override_active,
                "match_window":            self.context.match_window.value,
            },
            "skills": [
                {"skill_id": s.skill_id, "relevance": round(s.relevance, 2),
                 "required": s.required}
                for s in self.skills
            ],
        }


# ── Usage example ──────────────────────────────────────────────────────────

def example_afc_august():
    """
    $AFC analysis in August 2026:
    - Football fan token Tier 1
    - Fan Token Play PATH_2 active
    - Summer transfer window open
    - Post-World Cup (world_cup_active = False, tournament ended July 19)
    - Standard macro (NEUTRAL)
    """
    import json

    ctx = DiscoveryContext(
        sport                  = "football",
        use_case               = "fan_token_tier1",
        fan_token_play_active  = True,    # AFC PATH_2 confirmed
        gamified_token         = True,
        transfer_window_active = True,    # August = summer window
        world_cup_active       = False,   # Ended July 19
        match_window           = MatchWindow.T_MINUS_48H,  # Pre-liquidation window
        macro_phase            = MacroPhase.NEUTRAL,
        token_budget           = 60_000,
    )

    discovery = SkillDiscovery()
    stack     = discovery.discover(ctx)

    print(json.dumps(stack.summary(), indent=2))
    print(f"\nSkills that would NOT be loaded by static ftier1-football bundle:")
    standard_bundle = {
        "macro-overview", "market-football", "sport-domain-football",
        "athlete-intel-football", "token-intelligence-football",
        "defi-liquidity", "fan-token-lifecycle", "confidence-output-schema"
    }
    for skill in stack.skills:
        if not any(s in skill.skill_id for s in standard_bundle):
            if skill.relevance >= 0.70:
                print(f"  + {skill.skill_id} (relevance {skill.relevance:.2f})")


if __name__ == "__main__":
    example_afc_august()
```

---

## Integration with the sequential reasoning chain

```
RECOMMENDED AGENT STARTUP SEQUENCE WITH DISCOVERY:

1. Call sportmind_macro()
   → Extract macro_phase, macro_modifier, macro_override_active

2. Call sportmind_fan_token_lookup(token)
   → Extract lifecycle_phase, fan_token_play field

3. Call sportmind_sentiment_snapshot(token)
   → Extract supply_mechanics, fan_token_play_active

4. Build DiscoveryContext from MCP outputs:
   ctx = DiscoveryContext.from_mcp_outputs(
       macro_result    = macro,
       lookup_result   = lookup,
       sentiment_result= sentiment,
       sport           = "football",
       use_case        = "fan_token_tier1",
       # Add calendar context manually:
       transfer_window_active = is_august_or_january(),
       world_cup_active       = is_between("2026-06-11", "2026-07-19"),
       match_window           = get_match_window(kickoff_time),
   )

5. Run discovery:
   stack = SkillDiscovery().discover(ctx)

6. Load skills in discovered order:
   for skill_path in stack.skill_paths:
       load_skill(skill_path)

7. Proceed with standard five-phase chain (platform/sequential-thinking-integration.md)
```

---

## When to use discovery vs static bundles

```
USE STATIC BUNDLE (platform/skill-bundles.md) WHEN:
  → Single sport, fixed use case, standard conditions
  → High-frequency agent (many calls/hour) — discovery adds latency
  → Developer wants predictable, auditable skill loading
  → Building a focused single-purpose application

USE DISCOVERY PROTOCOL WHEN:
  → Portfolio agent covering multiple sports and tokens
  → Long-running autonomous agent spanning multiple calendar conditions
  → Agent must handle Fan Token Play + transfer window + tournament simultaneously
  → Context changes frequently and skills should adapt automatically
  → Building a general-purpose SportMind agent
```

---

## Connection to verifiable ML roadmap

```
DISCOVERY AS A STEP TOWARD v4.0:

The skill discovery protocol is the precursor to the trained model (v4.0).

Current (v3.x): Rules-based scoring — context signals → relevance scores → stack
v4.0 target:    Trained model — learns optimal skill selection from calibration outcomes

The calibration records community is collecting are training data for both:
  1. Modifier values (direct)
  2. Skill selection quality (indirect — which context + skill combinations
     produced the highest calibration accuracy?)

Every context-tagged discovery run that produces a calibration record is
a data point toward a trained skill selector that replaces the scoring rules
with learned weights.

See: platform/verifiable-ml-roadmap.md
```

---

*SportMind v3.46 · MIT License · sportmind.dev*
*See also: platform/skill-bundles.md · platform/sequential-thinking-integration.md*
*core/multi-agent-coordination.md · platform/memory-integration.md*
*platform/verifiable-ml-roadmap.md*
