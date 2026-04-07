#!/usr/bin/env python3
"""
SportMind Starter Pack — Example 05: SportFi Kit Integration
=============================================================
SportMind intelligence + SportFi Kit execution working together.

What this demonstrates:
  - The intelligence/execution boundary in practice
  - SportMind recommends; SportFi Kit executes; human or app logic approves
  - How recommended_action feeds token-gating decisions
  - The correct integration pattern for fan token applications
  - Why SportMind agents never directly trigger smart contract calls

What you need:
  pip install aiohttp
  python scripts/sportmind_api.py   # in another terminal
  SportFi Kit: https://github.com/sportfi/sportfi-kit

The key architectural insight:
  SportMind Layer  → generates intelligence (what does the signal say?)
  SportFi Kit Layer → manages contracts (token-gating, wagering, wallet detection)
  Application Layer → decides what to do (reads both; acts on human/logic approval)

See: examples/applications/app-07-sportfi-kit-integration.md for the full blueprint
See: platform/integration-partners.md — Partner 7 for SportFi Kit documentation
"""

import asyncio
import json
import logging
import os
from datetime import datetime, timezone
from dataclasses import dataclass
from typing import Optional

import aiohttp

SPORTMIND_API = os.environ.get("SPORTMIND_API", "http://localhost:8080")
log           = logging.getLogger("sportmind.sportfi-integration")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")


# ── Data structures ───────────────────────────────────────────────────────────

@dataclass
class SportMindSignal:
    """Intelligence output from SportMind."""
    event_id:           str
    sport:              str
    token_symbol:       str
    sms:                float
    sms_tier:           str
    recommended_action: str
    macro_modifier:     float
    macro_phase:        str
    flags:              dict
    reasoning_summary:  str
    generated_at:       str

@dataclass
class SportFiKitContext:
    """
    Context from SportFi Kit's environment detection.
    SportFi Kit detects: Socios App, Telegram Mini App, or standard browser.
    Each context has different UI and capability requirements.
    """
    environment:      str   # "socios_app" | "telegram_mini_app" | "browser"
    wallet_connected: bool
    token_balance:    float
    can_vote:         bool
    can_stake:        bool

@dataclass
class IntegrationDecision:
    """
    The application layer decision — reads both SportMind and SportFi Kit context.
    This is what YOUR application logic produces. Not SportMind. Not SportFi Kit.
    """
    show_signal:        bool
    signal_detail:      str   # "compact" | "full" | "none"
    enable_token_gate:  bool
    gate_threshold:     float # minimum token balance to access content
    show_governance:    bool  # show governance vote if relevant
    action_prompt:      str   # what to show the user
    requires_human:     bool  # flag for actions needing explicit human approval


# ── SportMind intelligence layer ─────────────────────────────────────────────

async def get_sportmind_signal(sport: str, event_id: str,
                                token_symbol: str) -> SportMindSignal:
    """
    Fetch SportMind signal for an event.
    This is the intelligence layer — it reasons, it does not act.
    """
    async with aiohttp.ClientSession() as session:

        # Step 1: Macro state (always first)
        async with session.get(f"{SPORTMIND_API}/macro-state") as r:
            macro  = await r.json()
            cycle  = macro["macro_state"]["crypto_cycle"]
            modifier = cycle["macro_modifier"]
            phase    = cycle["phase"]

        # Step 2: Signal
        async with session.get(
            f"{SPORTMIND_API}/stack",
            params={"sport": sport, "use_case": "fan_token_tier1"}
        ) as r:
            stack = await r.json()

        # Compute SMS
        layers = set()
        for skill in stack.get("stack", []):
            p = skill.get("skill_id","")
            if p.startswith("macro"):       layers.add(5)
            elif p.startswith("market"):    layers.add(4)
            elif p.startswith("sports"):    layers.add(1)
            elif p.startswith("athlete"):   layers.add(2)
            elif p.startswith("fan-token"): layers.add(3)

        sms = round(
            (len(layers)/5)*0.35*100 + (1.0 if modifier>=0.75 else 0.6)*0.25*100 +
            0.25*100 + min(modifier,1.0)*0.15*100, 1
        )
        sms_tier = "HIGH_QUALITY" if sms>=80 else "GOOD" if sms>=60 else "PARTIAL" if sms>=40 else "INSUFFICIENT"
        action   = "ENTER" if sms >= 60 and modifier >= 0.75 else "WAIT"

        return SportMindSignal(
            event_id           = event_id,
            sport              = sport,
            token_symbol       = token_symbol,
            sms                = sms,
            sms_tier           = sms_tier,
            recommended_action = action,
            macro_modifier     = modifier,
            macro_phase        = phase,
            flags              = {"macro_override_active": modifier < 0.75},
            reasoning_summary  = (
                f"{sport.capitalize()} signal for {token_symbol}. "
                f"Macro: {phase} ({modifier}). "
                f"SMS {sms} ({sms_tier}). "
                f"Recommended action: {action}."
            ),
            generated_at = datetime.now(timezone.utc).isoformat()
        )


# ── SportFi Kit context layer ─────────────────────────────────────────────────

def detect_sportfi_context(request_headers: dict = None) -> SportFiKitContext:
    """
    Detect SportFi Kit environment.
    In production: SportFi Kit provides detectEnvironment() in its SDK.
    See: https://github.com/sportfi/sportfi-kit — environment detection docs.

    Environments:
      socios_app:         Socios Browser — full token functionality
      telegram_mini_app:  Telegram — compact UI, limited wallet interaction
      browser:            Standard web — full feature set
    """
    headers = request_headers or {}
    user_agent = headers.get("User-Agent", "")

    # SportFi Kit's actual detection logic (simplified)
    if "SociosBrowser" in user_agent:
        env = "socios_app"
    elif "TelegramWebApp" in user_agent:
        env = "telegram_mini_app"
    else:
        env = "browser"

    # In production: read from SportFi Kit's wallet detection hook
    # const { isConnected, balance } = useFanToken({ symbol: "PSG" })
    return SportFiKitContext(
        environment      = env,
        wallet_connected = True,   # Replace with SportFi Kit wallet detection
        token_balance    = 50.0,   # Replace with SportFi Kit balance query
        can_vote         = True,
        can_stake        = env != "telegram_mini_app"
    )


# ── Application layer — the integration decision ──────────────────────────────

def make_integration_decision(
    signal:   SportMindSignal,
    kit_ctx:  SportFiKitContext
) -> IntegrationDecision:
    """
    The application layer decision.

    This reads BOTH SportMind intelligence AND SportFi Kit context to decide
    what to show the user and what actions to enable.

    KEY PRINCIPLE: SportMind recommends. SportFi Kit enables.
    Neither one acts alone. The application layer coordinates both.
    Humans approve meaningful financial actions.
    """

    # ── Token-gating decision ──────────────────────────────────────────────
    # Show the full SportMind signal only to token holders.
    # Non-holders see a teaser to incentivise token acquisition.

    has_tokens        = kit_ctx.token_balance > 0
    has_enough_tokens = kit_ctx.token_balance >= 10.0  # Threshold for full signal

    # ── Signal display decision ────────────────────────────────────────────
    if not kit_ctx.wallet_connected:
        signal_detail = "none"
        action_prompt = "Connect your wallet to access SportMind intelligence"
    elif not has_tokens:
        signal_detail = "none"
        action_prompt = f"Hold {signal.token_symbol} tokens to unlock pre-match analysis"
    elif not has_enough_tokens:
        signal_detail = "compact"  # Show SMS tier but not full signal
        action_prompt = f"Hold 10+ {signal.token_symbol} for full SportMind intelligence"
    elif kit_ctx.environment == "telegram_mini_app":
        signal_detail = "compact"  # Compact view in Telegram
        action_prompt = signal.reasoning_summary
    else:
        signal_detail = "full"     # Full signal in browser or Socios app
        action_prompt = signal.reasoning_summary

    # ── Governance decision ────────────────────────────────────────────────
    # Show governance vote prompt if:
    # - Signal is HIGH_QUALITY and holder has voting rights
    # - There is an active governance event for this token
    show_governance = (
        signal.sms >= 80 and
        kit_ctx.can_vote and
        has_tokens
        # + check if there is an active governance vote for this token
    )

    # ── Financial action decision ──────────────────────────────────────────
    # IMPORTANT: any action involving financial execution ALWAYS requires
    # explicit human approval. SportMind never triggers this autonomously.
    requires_human = signal.recommended_action == "ENTER" and has_enough_tokens

    # ── Environment-specific adjustments ──────────────────────────────────
    if kit_ctx.environment == "socios_app":
        enable_token_gate = True
        gate_threshold    = 1.0   # Standard Socios threshold
    elif kit_ctx.environment == "telegram_mini_app":
        enable_token_gate = False  # Simplified: no gating in Telegram
        gate_threshold    = 0.0
    else:
        enable_token_gate = True
        gate_threshold    = 10.0  # Higher threshold in browser

    return IntegrationDecision(
        show_signal       = signal_detail != "none",
        signal_detail     = signal_detail,
        enable_token_gate = enable_token_gate,
        gate_threshold    = gate_threshold,
        show_governance   = show_governance,
        action_prompt     = action_prompt,
        requires_human    = requires_human
    )


# ── TypeScript equivalent (for SportFi Kit React components) ──────────────────

TYPESCRIPT_EQUIVALENT = '''
// The same integration in SportFi Kit React/TypeScript
// See: examples/applications/app-07-sportfi-kit-integration.md

import { useFanToken, useGovernanceVote } from "@sportfi-kit/core"
import { useSportMind } from "../hooks/useSportMind"

function SportMindWidget({ sport, eventId, tokenSymbol }) {
  const { isHolder, balance }  = useFanToken({ symbol: tokenSymbol })
  const { signal, loading }    = useSportMind(sport, "fan_token_tier1")
  const { vote, hasVoted }     = useGovernanceVote({ eventId })

  // Token-gating: only holders see full intelligence
  if (!isHolder) return <TokenGate symbol={tokenSymbol} />

  return (
    <div className="sportmind-widget">
      <SMSBadge sms={signal?.sportmind_score?.sms} />

      {/* Full signal for 10+ token holders */}
      {balance >= 10 && <FullSignal signal={signal} />}
      {balance < 10  && <CompactSignal sms={signal?.sportmind_score?.sms} />}

      {/* Governance: only when signal quality warrants it */}
      {signal?.sportmind_score?.sms >= 80 && !hasVoted && (
        <GovernancePrompt
          onVote={(choice) => vote({ eventId, choice })}
          signal={signal}
          // Note: vote is submitted by the holder, triggered by human action
          // SportMind provides the intelligence context; holder decides
        />
      )}

      <Disclaimer>
        SportMind provides intelligence context. Financial decisions are yours.
      </Disclaimer>
    </div>
  )
}
'''


# ── Demo run ─────────────────────────────────────────────────────────────────

async def demo():
    """Demonstrate the full integration flow."""
    print("── SportMind + SportFi Kit Integration Demo ──")
    print()

    # 1. Get SportMind signal
    print("Step 1: Fetching SportMind signal...")
    signal = await get_sportmind_signal(
        sport="football", event_id="ucl-qf-psg-arsenal", token_symbol="PSG"
    )
    print(f"  SMS: {signal.sms} ({signal.sms_tier})")
    print(f"  Macro: {signal.macro_phase} ({signal.macro_modifier})")
    print(f"  Recommended: {signal.recommended_action}")
    print()

    # 2. Detect SportFi Kit environment
    print("Step 2: Detecting SportFi Kit environment...")
    kit_ctx = detect_sportfi_context({"User-Agent": "Mozilla/5.0"})
    print(f"  Environment: {kit_ctx.environment}")
    print(f"  Token balance: {kit_ctx.token_balance}")
    print()

    # 3. Application layer decision
    print("Step 3: Application layer decision...")
    decision = make_integration_decision(signal, kit_ctx)
    print(f"  Show signal: {decision.show_signal} ({decision.signal_detail})")
    print(f"  Token gate: {decision.enable_token_gate} (threshold: {decision.gate_threshold})")
    print(f"  Show governance: {decision.show_governance}")
    print(f"  Requires human: {decision.requires_human}")
    print(f"  User sees: {decision.action_prompt}")
    print()

    print("─────────────────────────────────────────────")
    print("Key points:")
    print("  SportMind generated the signal — it did not act on it")
    print("  SportFi Kit provided the context — it did not decide")
    print("  The application layer coordinated both")
    print("  Human approval required for any financial action")
    print()
    print("TypeScript equivalent for SportFi Kit React components:")
    print(TYPESCRIPT_EQUIVALENT)


if __name__ == "__main__":
    asyncio.run(demo())
