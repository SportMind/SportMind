---
name: fraud-signal-intelligence
description: >
  Structured manipulation detection framework for fan token signals —
  a taxonomy of six attack types with detection methods, confidence
  scoring (0–100), and agent decision rules at each threshold. Converts
  the library's scattered manipulation warnings (wash trading in DeFi,
  coordinated wallets in address intelligence, KOL paid promotion flags)
  into a unified Manipulation Risk Score (MRS) with clear TRUST / CAUTION
  / SUSPECT / COMPROMISED classifications. Critical as FTP PATH_2 grows
  and the financial stakes around pre-match token signals increase.
  An agent that detects coordinated pre-match pump attempts and correctly
  classifies them as noise rather than signal has direct commercial value.
  Platform-level: builds on chiliz-chain-address-intelligence.md and
  defi-liquidity-intelligence. Load before acting on any pre-match token
  signal that shows anomalous volume, unusual wallet patterns, or
  unusually large holder movements.
---

# Fraud Signal Intelligence — SportMind

**Not every signal is real. An agent that cannot distinguish genuine
holder engagement from coordinated manipulation will systematically
make wrong decisions at the worst possible moments.**

The financial stakes around fan token signals have increased significantly
with FTP PATH_2. A pre-match token spike could be: genuine fan excitement,
speculator entry anticipating a win burn, or coordinated pump to create
false signal. These require different responses. Only the third is manipulation.
This skill gives agents the structured framework to tell them apart.

---

## The six manipulation attack types

```
ATTACK TYPE 1 — WASH TRADING
  Definition: Simultaneous or rapid buy-and-sell transactions between
  wallets controlled by the same entity, creating artificial volume.
  Purpose: Inflate TVI and HAS metrics; trigger algorithmic trading responses.
  
  Detection signals:
    Volume spike with no corresponding on-pitch event or news trigger
    Transfer velocity × 3+ above 30-day baseline with no external catalyst
    Circular transaction patterns (wallet A → B → C → A within hours)
    Volume occurs at unusual hours for token's primary fan geography
    No social volume increase matching the on-chain volume increase
  
  MRS contribution: HIGH (35–50 points)
  Sources: GeckoTerminal, Chiliscan transfer history
  Agent rule: If wash trading detected → classify TVI spike as NOISE.
    Do not apply organic HAS modifier. Flag: VOLUME_INTEGRITY_COMPROMISED.

ATTACK TYPE 2 — COORDINATED WALLET ACCUMULATION (Sybil-adjacent)
  Definition: Large number of new wallets created in a short window,
  each acquiring small amounts — designed to inflate unique holder count
  and HAS without representing genuine new fans.
  Purpose: Inflate holder count metric; create false community growth signal.
  
  Detection signals:
    Burst of new wallet creation within 24–48h (>200% above baseline rate)
    New wallets have near-identical transaction patterns
    New wallets originated from same funding source (traceable on-chain)
    Unique holder count rises but governance participation stays flat
    Platform/chiliz-chain-address-intelligence.md Signal 5 triggered
  
  MRS contribution: HIGH (30–45 points)
  Agent rule: If coordinated accumulation detected → discount holder count
    growth. Apply: holder_count_integrity_flag. Do not count as organic growth.

ATTACK TYPE 3 — PRE-EVENT PUMP AND DUMP
  Definition: Coordinated buying before a predictable event (UCL match,
  PATH_2 WIN expected) to inflate price, followed by rapid selling after
  the event for profit, leaving late buyers at loss.
  Purpose: Extract profit from event-driven price movements.
  
  Detection signals:
    Smart wallet accumulation begins 48–72h before a high-stakes match
    (this alone is not suspicious — check if it follows organic social)
    Accumulation occurs across multiple coordinated wallets simultaneously
    No organic social volume increase matching the buying pattern
    After event: same wallets sell rapidly within 2–4h of result
    Pattern repeats across multiple consecutive matches
  
  MRS contribution: MEDIUM-HIGH (25–40 points)
  CRITICAL DISTINCTION: Pre-match speculator entry (Archetype 2 from
  fan-holder-profile-intelligence.md) is LEGITIMATE. Pump-and-dump is not.
  The difference: legitimate speculation is diffuse and tracks organic signals.
  Coordinated pump uses fewer wallets, moves faster, and has circular sourcing.
  Agent rule: If pump-and-dump pattern detected → flag PRICE_INTEGRITY_RISK.
    Do not apply FTP WIN burn modifier at full weight (market price compromised).

ATTACK TYPE 4 — KOL UNDISCLOSED PAID PROMOTION
  Definition: Key Opinion Leader (KOL) posts appear organic but are paid
  promotions without disclosure, creating false organic sentiment signals.
  Already covered partially by fan-token/kol-influence-intelligence/ (KIS × 0.50
  for undisclosed paid). This type formalises it as a fraud signal.
  
  Detection signals:
    Multiple KOLs post about the same token within hours of each other
    Posting pattern coordinated (same hashtags, similar language)
    KOLs who have no history of covering this sport or token suddenly active
    On-chain: new wallet creation correlates with KOL post timing
    No disclosure tags (#ad, #sponsored, #paidpartnership)
  
  MRS contribution: MEDIUM (20–30 points)
  Agent rule: If undisclosed coordinated KOL campaign detected → apply
    organic_signal_discount × 0.50. Flag: SENTIMENT_INTEGRITY_COMPROMISED.

ATTACK TYPE 5 — GOVERNANCE CAPTURE ATTEMPT
  Definition: Coordinated acquisition of tokens specifically to control
  governance votes on commercially sensitive decisions.
  Purpose: Influence token design, supply parameters, or commercial partnerships
  in favour of a specific actor at expense of genuine holders.
  
  Detection signals:
    Large single-entity accumulation before a governance vote announcement
    Accumulation reverses rapidly after vote closes
    Vote outcome significantly diverges from pre-vote community sentiment
    Single wallet or coordinated group controls >30% of voting power
    (Ante et al., 2025: "no club wants fans to have too much right of
    co-determination" — this attack exploits that tension)
  
  MRS contribution: HIGH (30–45 points)
  Agent rule: If governance capture detected → flag GOVERNANCE_INTEGRITY_RISK.
    Apply to Pattern 9 (Governance Delegate) output. Recommend ABSTAIN on
    commercial signals tied to governance outcomes until resolved.

ATTACK TYPE 6 — LIQUIDITY POOL MANIPULATION (MEV / Sandwich)
  Definition: Automated MEV bots executing sandwich attacks on fan token
  DEX trades, extracting value from legitimate traders.
  Already covered in defi-liquidity-intelligence. Formalised here as fraud type.
  
  Detection signals:
    Abnormal slippage on small trades (should not move price significantly)
    Block-level analysis shows buy/sell sandwiching pattern
    Gas prices spiking around fan token trades
    Pool price vs CEX price divergence > 2% without news catalyst
  
  MRS contribution: LOW-MEDIUM (10–20 points per incident)
  Agent rule: Apply liquidity_warning flag. Use CEX price as reference,
    not DEX price, when MEV manipulation is active.
```

---

## Manipulation Risk Score (MRS)

```
MRS = sum of active attack type contributions, capped at 100

MRS INTERPRETATION AND AGENT ACTIONS:

  MRS 0–24: TRUST
    Signal is clean. No manipulation detected.
    Action: Apply signal at full confidence. No modification.

  MRS 25–49: CAUTION
    Some anomalous patterns present but below manipulation threshold.
    Action: Apply signal at 85% confidence. Note in output: SIGNAL_QUALITY: CAUTION.
    Add to monitoring queue. Do not change recommended_action alone.

  MRS 50–74: SUSPECT
    Multiple manipulation indicators. Signal integrity is compromised.
    Action: Apply signal at 60% confidence. Recommended action cannot be ENTER.
    Downgrade to WAIT regardless of underlying signal quality.
    Flag: MANIPULATION_SUSPECTED. Require additional organic confirmation.

  MRS 75–100: COMPROMISED
    High-confidence manipulation. Signal cannot be trusted.
    Action: ABSTAIN on any signal using this token's on-chain data.
    Flag: SIGNAL_COMPROMISED. Do not apply to any commercial decision.
    Report: note specific attack types detected in output.

DECAY RULE:
  MRS decays over time when no new manipulation signals detected.
  SUSPECT status: decay to CAUTION after 7 days clean.
  CAUTION status: decay to TRUST after 14 days clean.
  COMPROMISED status: requires manual review + 14 days clean before downgrade.
```

---

## Detection implementation

```python
# Simplified detection workflow — load alongside fan-token-pulse and
# chiliz-chain-address-intelligence for full signal chain

class ManipulationDetector:
    def __init__(self, token: str):
        self.token  = token
        self.mrs    = 0
        self.flags  = []
        self.attacks = []

    def check_wash_trading(self, tvi_ratio: float, social_ratio: float,
                           has_catalyst: bool) -> None:
        """TVI spike with no social/news catalyst = wash trading risk."""
        if tvi_ratio > 3.0 and not has_catalyst and social_ratio < 1.5:
            score = min(50, int((tvi_ratio - 3.0) * 10 + 35))
            self.mrs += score
            self.attacks.append({
                'type':       'WASH_TRADING',
                'confidence': min(95, score * 2),
                'signal':     f'TVI ×{tvi_ratio:.1f} with no organic catalyst'
            })
            self.flags.append('VOLUME_INTEGRITY_COMPROMISED')

    def check_coordinated_wallets(self, new_wallet_ratio: float,
                                  governance_delta: float) -> None:
        """Wallet burst with flat governance = Sybil-adjacent attack."""
        if new_wallet_ratio > 2.0 and governance_delta < 0.02:
            score = min(45, int((new_wallet_ratio - 2.0) * 15 + 30))
            self.mrs += score
            self.attacks.append({
                'type':       'COORDINATED_WALLET_ACCUMULATION',
                'confidence': min(90, score * 2),
                'signal':     f'New wallet rate ×{new_wallet_ratio:.1f}, governance flat'
            })
            self.flags.append('HOLDER_COUNT_INTEGRITY_COMPROMISED')

    def check_pump_and_dump(self, smart_wallet_buys: int,
                            organic_social: bool,
                            wallets_coordinated: bool) -> None:
        """Smart wallets accumulating without organic signal = pump risk."""
        if smart_wallet_buys > 3 and not organic_social and wallets_coordinated:
            self.mrs += 35
            self.attacks.append({
                'type':       'PRE_EVENT_PUMP_DUMP',
                'confidence': 75,
                'signal':     f'{smart_wallet_buys} smart wallets coordinating without organic signal'
            })
            self.flags.append('PRICE_INTEGRITY_RISK')

    def get_classification(self) -> dict:
        capped_mrs = min(100, self.mrs)
        if capped_mrs < 25:
            label, action = 'TRUST',       'Full signal confidence'
        elif capped_mrs < 50:
            label, action = 'CAUTION',     'Apply at 85% confidence'
        elif capped_mrs < 75:
            label, action = 'SUSPECT',     'Downgrade to WAIT'
        else:
            label, action = 'COMPROMISED', 'ABSTAIN — signal cannot be trusted'
        return {
            'mrs_score':      capped_mrs,
            'mrs_label':      label,
            'agent_action':   action,
            'active_attacks': self.attacks,
            'active_flags':   self.flags
        }
```

---

## Integration with SportMind signal chain

```
WHEN TO LOAD THIS SKILL:
  Load before applying any pre-match fan token signal when:
    → TVI is significantly above baseline without a clear news trigger
    → New wallet count has spiked in the last 48h
    → Multiple KOLs have posted about the token in a coordinated window
    → The match carries unusually high PATH_2 commercial stakes (UCL final, etc.)
    → MRS from a previous session was CAUTION or above

PATTERN 2 (Pre-Match Chain):
  Step 4 check: Before applying athlete modifier to fan token signal,
  run MRS check. If MRS ≥ 50 (SUSPECT), downgrade recommended_action to WAIT.
  If MRS ≥ 75 (COMPROMISED), recommended_action = ABSTAIN regardless of SMS.

PATTERN 8 (FTP Monitor):
  Pre-liquidation detection + MRS check together.
  A T-48h pre-liquidation event PLUS elevated MRS = compounded uncertainty.
  Pre-liquidation is never bearish (PROTOCOL_EVENT) but MRS can still indicate
  that the price signal around the pre-liquidation is being manipulated.

FTP PATH_2 SPECIFIC RULE:
  Do not apply PATH_2 WIN burn commercial uplift if MRS ≥ 50.
  The supply reduction is real (on-chain verifiable) but the market price
  signal may be compromised. The burn happened; what the market does with
  it is uncertain. Apply: burn_confirmed: true, price_signal: SUSPECT.

GOVERNANCE INTELLIGENCE (Pattern 9):
  If GOVERNANCE_INTEGRITY_RISK flag is active, governance delegate output
  must note that vote outcome may not reflect genuine community preference.
  Recommend: hold on commercial decisions tied to governance outcomes.
```

---

## MRS output schema

```json
{
  "fraud_signal_brief": {
    "token":       "AFC",
    "assessed_at": "2026-04-12T00:00:00Z"
  },

  "mrs_score":  22,
  "mrs_label":  "TRUST",
  "agent_action": "Full signal confidence — no manipulation detected",

  "active_attacks": [],
  "active_flags":   [],

  "monitoring": {
    "tvi_ratio_24h":       1.4,
    "new_wallet_ratio_48h": 1.1,
    "social_organic_ratio": 1.8,
    "governance_delta":     0.03,
    "assessment": "All indicators within normal range. Pre-match TVI elevated but tracks organic social volume — legitimate speculator entry."
  },

  "plain_english": "No manipulation signals on $AFC right now. The pre-match volume increase is tracking social media activity, which is what you'd expect before a UCL quarter-final. The on-chain data looks clean.",

  "sportmind_version": "3.62.0"
}
```

---

*SportMind v3.62 · MIT License · sportmind.dev*
*See also: platform/chiliz-chain-address-intelligence.md*
*fan-token/defi-liquidity-intelligence/ · fan-token/kol-influence-intelligence/*
*fan-token/fan-token-pulse/ · fan-token/gamified-tokenomics-intelligence/*
*fan-token/fan-holder-profile-intelligence.md*
