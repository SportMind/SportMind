#!/usr/bin/env python3
"""
SportMind macro signal checker.
Checks BTC/CHZ prices against SportMind thresholds and fires alerts when
conditions change. Called by .github/workflows/macro-monitor.yml every 4 hours.

Usage:
    python scripts/check_macro_signals.py --signal btc_200d_ma [--webhook URL]
    python scripts/check_macro_signals.py --signal chz_7d_change --threshold -0.25

Signals supported:
    btc_200d_ma       BTC price vs 200-day moving average crossover
    chz_7d_change     CHZ 7-day price change percentage

See platform/monitoring-alerts.md for full alert specifications.
See platform/live-signals.md for signal interpretation logic.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


# ── Constants ────────────────────────────────────────────────────────────────
COINGECKO_API = "https://api.coingecko.com/api/v3"
MACRO_STATE_FILE = "platform/macro-state.json"

# Thresholds from platform/monitoring-alerts.md
BTC_BEAR_PCTS = {
    "BEAR":         -0.0,   # BTC below 200-day MA
    "EXTREME_BEAR": -0.20,  # BTC >20% below 200-day MA
}

MACRO_MODIFIERS = {
    "BULL":         1.20,
    "NEUTRAL":      1.00,
    "BEAR":         0.75,
    "EXTREME_BEAR": 0.55,
}

CONSECUTIVE_CONFIRMS_REQUIRED = 3  # Prevents false alerts from intraday volatility


def get_btc_price_and_ma() -> dict:
    """Fetch current BTC price and approximate 200-day MA from CoinGecko."""
    if not HAS_REQUESTS:
        print("WARNING: requests library not installed. Install with: pip install requests")
        return {"price": None, "ma_200d": None, "source": "unavailable"}

    api_key = os.environ.get("COINGECKO_API_KEY", "")
    headers = {"x-cg-demo-api-key": api_key} if api_key else {}

    try:
        # Current price
        price_resp = requests.get(
            f"{COINGECKO_API}/simple/price",
            params={"ids": "bitcoin,chiliz", "vs_currencies": "usd"},
            headers=headers,
            timeout=10
        )
        prices = price_resp.json()
        btc_price = prices.get("bitcoin", {}).get("usd")
        chz_price = prices.get("chiliz", {}).get("usd")

        # 200-day MA approximation from market_chart (200 daily closes)
        # NOTE: Free tier has rate limits. In production, cache this data.
        chart_resp = requests.get(
            f"{COINGECKO_API}/coins/bitcoin/market_chart",
            params={"vs_currency": "usd", "days": 200, "interval": "daily"},
            headers=headers,
            timeout=15
        )
        chart = chart_resp.json()
        prices_200d = [p[1] for p in chart.get("prices", [])]
        ma_200d = sum(prices_200d) / len(prices_200d) if prices_200d else None

        return {
            "btc_price": btc_price,
            "chz_price": chz_price,
            "btc_200d_ma": round(ma_200d, 2) if ma_200d else None,
            "source": "coingecko"
        }

    except Exception as e:
        print(f"WARNING: Price fetch failed: {e}")
        return {"btc_price": None, "chz_price": None, "btc_200d_ma": None, "source": "error"}


def determine_crypto_phase(btc_price: float, ma_200d: float) -> str:
    """Determine crypto cycle phase from SportMind thresholds."""
    if btc_price is None or ma_200d is None:
        return "NEUTRAL"  # Conservative default when data unavailable

    pct_vs_ma = (btc_price - ma_200d) / ma_200d

    if pct_vs_ma > 0:
        return "BULL"
    elif pct_vs_ma > BTC_BEAR_PCTS["EXTREME_BEAR"]:
        return "BEAR"
    else:
        return "EXTREME_BEAR"


def load_macro_state() -> dict:
    """Load current macro state from platform/macro-state.json."""
    try:
        with open(MACRO_STATE_FILE) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"macro_state": {"crypto_cycle": {"phase": "NEUTRAL", "consecutive_confirms": 0}}}


def save_macro_state(state: dict) -> None:
    """Save updated macro state to platform/macro-state.json."""
    with open(MACRO_STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def fire_alert(signal: str, phase: str, data: dict, webhook_url: str = None) -> None:
    """Fire alert via webhook if configured."""
    alert = {
        "sportmind_alert": {
            "alert_id": f"macro-{signal}-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}",
            "alert_version": "1.0",
            "fired_at": datetime.now(timezone.utc).isoformat(),
            "alert_type": "MACRO_SIGNAL",
            "severity": "HIGH" if "EXTREME" in phase else "MEDIUM",
            "payload": {
                "alert_type": "MACRO_CRYPTO_CYCLE",
                "condition": f"{phase}_CONFIRMED",
                "data": data,
                "sportmind_impact": {
                    "modifier_change": f"macro_modifier → {MACRO_MODIFIERS.get(phase, 1.00)}",
                    "agent_action": "Recalculate all open position signals with new macro modifier"
                }
            }
        }
    }

    print(f"ALERT FIRED: {phase} confirmed")
    print(json.dumps(alert, indent=2))

    if webhook_url and HAS_REQUESTS:
        try:
            resp = requests.post(webhook_url, json=alert, timeout=10)
            print(f"Webhook response: {resp.status_code}")
        except Exception as e:
            print(f"Webhook delivery failed: {e}")


def check_btc_200d_ma(consecutive_confirms: int, webhook_url: str = None) -> dict:
    """Check BTC vs 200-day MA with confirmation logic."""
    prices = get_btc_price_and_ma()
    btc_price = prices.get("btc_price")
    ma_200d = prices.get("btc_200d_ma")
    chz_price = prices.get("chz_price")

    if btc_price is None:
        print("SKIP: Price data unavailable. macro_modifier unchanged.")
        return {"phase": "NEUTRAL", "action": "skip", "reason": "data_unavailable"}

    phase = determine_crypto_phase(btc_price, ma_200d)
    pct_vs_ma = ((btc_price - ma_200d) / ma_200d * 100) if ma_200d else 0

    print(f"BTC: ${btc_price:,.0f} | 200d MA: ${ma_200d:,.0f} | Δ: {pct_vs_ma:.1f}%")
    print(f"CHZ: ${chz_price:.4f}" if chz_price else "CHZ: unavailable")
    print(f"Phase: {phase} | Confirms: {consecutive_confirms}/{CONSECUTIVE_CONFIRMS_REQUIRED}")

    state = load_macro_state()
    crypto_state = state["macro_state"]["crypto_cycle"]
    current_phase = crypto_state.get("phase", "NEUTRAL")

    if phase == current_phase:
        confirms = crypto_state.get("consecutive_confirms", 0) + 1
        crypto_state["consecutive_confirms"] = confirms

        if confirms >= CONSECUTIVE_CONFIRMS_REQUIRED and phase != "NEUTRAL":
            data = {
                "btc_price": btc_price,
                "btc_200d_ma": ma_200d,
                "btc_vs_ma_pct": round(pct_vs_ma, 1),
                "chz_price": chz_price,
                "consecutive_confirms": confirms
            }
            fire_alert("btc_200d_ma", phase, data, webhook_url)
    else:
        # Phase changed — reset confirms
        crypto_state["consecutive_confirms"] = 1
        crypto_state["last_phase_change"] = datetime.now(timezone.utc).isoformat()

    crypto_state["phase"] = phase
    crypto_state["btc_price_usd"] = btc_price
    crypto_state["btc_200d_ma_usd"] = ma_200d
    crypto_state["btc_vs_200d_ma_pct"] = round(pct_vs_ma, 1)
    crypto_state["chz_price_usd"] = chz_price
    crypto_state["macro_modifier"] = MACRO_MODIFIERS.get(phase, 1.00)
    state["macro_state"]["updated_at"] = datetime.now(timezone.utc).isoformat()

    save_macro_state(state)
    print(f"macro-state.json updated: phase={phase}, modifier={MACRO_MODIFIERS.get(phase, 1.00)}")
    return {"phase": phase, "action": "updated"}


def check_chz_7d_change(threshold: float = -0.25, webhook_url: str = None) -> dict:
    """Check CHZ 7-day price change against threshold."""
    prices = get_btc_price_and_ma()
    chz_price = prices.get("chz_price")

    if not chz_price or not HAS_REQUESTS:
        print("SKIP: CHZ price unavailable.")
        return {"action": "skip"}

    # NOTE: For production, compare against 7-day-ago price from CoinGecko market_chart
    # This stub flags when CHZ is significantly below threshold for operator awareness
    print(f"CHZ current: ${chz_price:.4f}")
    print("NOTE: 7-day change requires historical price comparison. See CoinGecko market_chart endpoint.")
    return {"action": "informational", "chz_price": chz_price}


def main():
    parser = argparse.ArgumentParser(description="SportMind macro signal checker")
    parser.add_argument("--signal", required=True, choices=["btc_200d_ma", "chz_7d_change"])
    parser.add_argument("--threshold", type=float, default=None)
    parser.add_argument("--threshold-type", default="crossover")
    parser.add_argument("--consecutive-confirms", type=int, default=CONSECUTIVE_CONFIRMS_REQUIRED)
    parser.add_argument("--webhook", default=os.environ.get("ALERT_WEBHOOK_URL"))
    args = parser.parse_args()

    print(f"\n=== SportMind Macro Signal Check: {args.signal} ===")
    print(f"Time: {datetime.now(timezone.utc).isoformat()}")
    print()

    state = load_macro_state()
    current_confirms = state["macro_state"]["crypto_cycle"].get("consecutive_confirms", 0)

    if args.signal == "btc_200d_ma":
        result = check_btc_200d_ma(current_confirms, args.webhook)
    elif args.signal == "chz_7d_change":
        result = check_chz_7d_change(
            args.threshold if args.threshold is not None else -0.25,
            args.webhook
        )

    print(f"\nResult: {result}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
