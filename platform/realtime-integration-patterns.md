# Real-Time Data Integration Patterns

**How to integrate live data sources with SportMind's static intelligence framework.**

SportMind provides the reasoning models. Live data provides the current values to
reason about. This document shows exactly how to connect real-time data sources to
SportMind's skill stack — with working code patterns for the five highest-value
live signal types.

---

## The integration model

```
SPORTMIND INTELLIGENCE + LIVE DATA = PRODUCTION-QUALITY SIGNAL

SportMind provides (permanent, loaded once):
  → The reasoning framework (what matters and why)
  → The modifier models (how to weight each signal)
  → The confidence schema (how to express uncertainty)

Live data provides (fetched per-analysis):
  → Current macro state (BTC/CHZ price, cycle phase)
  → Current lineup (who is actually playing)
  → Current token price and TVL (what the market says)
  → Current weather (what conditions will be like)
  → Current injury status (who is available)

The agent applies the framework to the live data.
SportMind is the brain. Live data is the sensory input.
```

---

## Pattern 1 — Macro state webhook

The macro modifier is the most important live signal in SportMind. It gates
every fan token analysis. Keeping it current is the highest-priority real-time
integration.

```python
# patterns/macro_webhook.py
"""
Webhook receiver that updates macro-state.json when crypto market conditions change.
Deploy as a serverless function or background service.
"""
import json
import hashlib
import aiohttp
import asyncio
from datetime import datetime, timezone
from pathlib import Path

MACRO_STATE_PATH = Path("platform/macro-state.json")
KAYEN_API        = "https://api.kayen.finance/v1/market/global"
COINGECKO_BTC    = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_200day_ma=true"
CHZ_ADDRESS      = "0x3506424f91fd33084466f402d5d97f05f8e3b4af"

async def fetch_market_data() -> dict:
    async with aiohttp.ClientSession() as session:
        # BTC vs 200-day MA
        async with session.get(COINGECKO_BTC) as r:
            btc_data = await r.json()
        btc_price   = btc_data["bitcoin"]["usd"]
        btc_200d_ma = btc_data["bitcoin"].get("usd_200day_moving_average", btc_price)
        
        # CHZ market data from KAYEN
        try:
            async with session.get(f"{KAYEN_API}?token=CHZ") as r:
                chz_data = await r.json()
            chz_price = chz_data.get("price_usd", 0)
        except Exception:
            chz_price = None  # Graceful degradation
    
    return {"btc_price": btc_price, "btc_200d_ma": btc_200d_ma, "chz_price": chz_price}


def classify_cycle(btc_price: float, btc_200d_ma: float) -> tuple:
    ratio = btc_price / btc_200d_ma
    
    if ratio >= 1.15:
        return "BULL", 1.20, "BTC significantly above 200-day MA — bull market conditions"
    elif ratio >= 0.95:
        return "NEUTRAL", 1.00, "BTC near 200-day MA — neutral market conditions"
    elif ratio >= 0.75:
        return "BEAR", 0.75, "BTC below 200-day MA — bear market conditions"
    else:
        return "EXTREME_BEAR", 0.55, "BTC far below 200-day MA — extreme bear conditions"


async def update_macro_state():
    data = await fetch_market_data()
    cycle, modifier, note = classify_cycle(data["btc_price"], data["btc_200d_ma"])
    
    # Load existing state to preserve non-market fields
    existing = {}
    if MACRO_STATE_PATH.exists():
        existing = json.loads(MACRO_STATE_PATH.read_text())
    
    state = {
        **existing,
        "macro_state": {
            "crypto_cycle": {
                "phase":           cycle,
                "macro_modifier":  modifier,
                "btc_price_usd":   data["btc_price"],
                "btc_200d_ma_usd": data["btc_200d_ma"],
                "btc_vs_200d_ma":  "above" if data["btc_price"] > data["btc_200d_ma"] else "below",
                "chz_price_usd":   data["chz_price"],
                "signal_note":     note,
            },
            "active_events":  existing.get("macro_state", {}).get("active_events", []),
            "last_updated":   datetime.now(timezone.utc).isoformat(),
            "next_update_due": "in 6 hours"
        }
    }
    
    MACRO_STATE_PATH.write_text(json.dumps(state, indent=2))
    print(f"[{datetime.now().isoformat()}] Macro updated: {cycle} (modifier {modifier})")
    
    # Alert if modifier changed significantly
    old_modifier = existing.get("macro_state", {}).get("crypto_cycle", {}).get("macro_modifier", 1.00)
    if abs(modifier - old_modifier) >= 0.25:
        await send_alert(f"MACRO SHIFT: {old_modifier} → {modifier} ({cycle})")
    
    return state


async def send_alert(message: str):
    """Send alert via webhook (configure your endpoint)."""
    ALERT_WEBHOOK = "https://your-webhook-endpoint.com/alerts"
    async with aiohttp.ClientSession() as session:
        await session.post(ALERT_WEBHOOK, json={"text": message})


if __name__ == "__main__":
    asyncio.run(update_macro_state())
```

---

## Pattern 2 — Lineup confirmation webhook

The T-2h lineup window is the highest-value moment in pre-match intelligence.
This pattern watches for lineup announcements and updates the signal automatically.

```python
# patterns/lineup_webhook.py
"""
Receives lineup announcements and updates pending pre-match analyses.
Integrates with the Pre-Match Intelligence Chain (agentic-workflows Pattern 2).
"""
from dataclasses import dataclass
from datetime import datetime, timezone
import json, asyncio, aiohttp
from typing import Optional

@dataclass
class LineupEvent:
    event_id:          str
    home_team:         str
    away_team:         str
    home_lineup:       list[str]
    away_lineup:       list[str]
    confirmed_at:      str
    key_player_absent: Optional[str] = None  # player name if notable absence

class LineupWebhookHandler:
    """
    Listens for lineup confirmation events and triggers signal updates.
    
    Integrates with:
      - Pre-match signal chain (update lineup_unconfirmed flag)
      - Portfolio monitor (alert if watched player absent)
      - Fan token signal (activate injury_warning if key player missing)
    """
    
    def __init__(self, signal_store: dict, watched_players: list[str]):
        self.signal_store    = signal_store   # {event_id: current_signal}
        self.watched_players = watched_players  # list of high-ATM players to watch
    
    async def handle_lineup_event(self, event: LineupEvent):
        """Process a lineup confirmation event."""
        
        # Check if this affects any watched players
        all_players = event.home_lineup + event.away_lineup
        absent_watched = [p for p in self.watched_players if p not in all_players]
        
        if absent_watched:
            await self.handle_key_player_absent(event, absent_watched)
            return
        
        # Standard lineup confirmation — update flag
        if event.event_id in self.signal_store:
            signal = self.signal_store[event.event_id]
            signal["modifiers"]["flags"]["lineup_unconfirmed"] = False
            signal["modifiers"]["flags"]["position_size_recommendation"] = "100%"
            signal["lineup_confirmed_at"] = event.confirmed_at
            self.signal_store[event.event_id] = signal
            print(f"[{event.event_id}] Lineup confirmed — position size upgraded to 100%")
    
    async def handle_key_player_absent(self, event: LineupEvent, absent_players: list):
        """Key player absent — reload analysis entirely."""
        print(f"[{event.event_id}] KEY PLAYER ABSENT: {absent_players}")
        
        # Activate injury_warning flag
        if event.event_id in self.signal_store:
            signal = self.signal_store[event.event_id]
            signal["modifiers"]["flags"]["injury_warning"] = True
            signal["modifiers"]["flags"]["key_player_absent"] = absent_players
            signal["modifiers"]["flags"]["position_size_recommendation"] = "RELOAD"
            self.signal_store[event.event_id] = signal
        
        # Alert
        await self.send_alert(
            f"⚠️ RELOAD REQUIRED: {', '.join(absent_players)} absent for {event.event_id}"
        )
    
    async def send_alert(self, message: str):
        print(f"ALERT: {message}")
        # Implement your notification (Slack, email, push notification)


# Webhook endpoint (FastAPI example)
# from fastapi import FastAPI
# app = FastAPI()
# handler = LineupWebhookHandler(signal_store={}, watched_players=["Vinicius Jr", "Erling Haaland"])
#
# @app.post("/webhook/lineup")
# async def receive_lineup(event: LineupEvent):
#     await handler.handle_lineup_event(event)
#     return {"status": "processed"}
```

---

## Pattern 3 — Fan token on-chain signal monitor

```python
# patterns/token_monitor.py
"""
Monitors fan token on-chain signals in real time.
Watches HAS (Holder Activity Score) and TVL for portfolio tokens.
"""
import asyncio, aiohttp, json
from datetime import datetime, timezone

KAYEN_API = "https://api.kayen.finance/v1"

# Token contract addresses on Chiliz Chain
TOKEN_ADDRESSES = {
    "PSG":  "0x...",  # $PSG
    "BAR":  "0x...",  # $BAR
    "CITY": "0x...",  # $CITY
    "JUV":  "0x...",  # $JUV
}

class TokenSignalMonitor:
    
    def __init__(self, tokens: dict, alert_callback):
        self.tokens           = tokens
        self.alert_callback   = alert_callback
        self.baseline         = {}  # {symbol: {price, tvl, holder_count}}
        self.has_history      = {}  # {symbol: [last 24 values]}
    
    async def fetch_token_data(self, address: str) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{KAYEN_API}/tokens/{address}") as r:
                return await r.json()
    
    async def compute_has(self, symbol: str, current: dict) -> float:
        """
        HAS (Holder Activity Score) — proprietary SportMind calculation.
        Derived from: transfer_volume, unique_address_activity, social_sentiment.
        This simplified version uses on-chain proxies.
        """
        baseline = self.baseline.get(symbol, current)
        
        price_change   = (current["price"] - baseline["price"]) / max(baseline["price"], 0.001)
        volume_change  = (current["volume_24h"] - baseline.get("volume_24h", current["volume_24h"])) \
                         / max(baseline.get("volume_24h", 1), 0.001)
        
        # HAS: normalised composite of price momentum and volume activity
        has = 50 + (price_change * 30) + (volume_change * 20)
        return max(0, min(100, has))  # Clamp to 0-100
    
    async def check_tvl_threshold(self, symbol: str, tvl: float) -> str:
        """Check TVL against SportMind thresholds."""
        if tvl > 5_000_000:  return "DEEP"
        if tvl > 500_000:    return "MODERATE"
        if tvl > 100_000:    return "THIN"
        return "CRITICAL"
    
    async def monitor_cycle(self):
        """Single monitoring cycle — runs every 15 minutes."""
        for symbol, address in self.tokens.items():
            try:
                data     = await self.fetch_token_data(address)
                has      = await self.compute_has(symbol, data)
                tvl_tier = await self.check_tvl_threshold(symbol, data.get("tvl_usd", 0))
                
                # Detect HAS spike (> 15 point increase from last reading)
                last_has = self.has_history.get(symbol, [50])[-1]
                if has - last_has > 15:
                    await self.alert_callback(
                        f"🔼 HAS SPIKE: {symbol} HAS {last_has:.1f} → {has:.1f} "
                        f"(+{has-last_has:.1f}). Pre-event signal likely."
                    )
                
                # Detect liquidity warning
                if tvl_tier in ("THIN", "CRITICAL"):
                    await self.alert_callback(
                        f"⚠️ LIQUIDITY: {symbol} TVL tier = {tvl_tier}. "
                        f"Activate liquidity_warning flag."
                    )
                
                # Update history
                if symbol not in self.has_history:
                    self.has_history[symbol] = []
                self.has_history[symbol].append(has)
                if len(self.has_history[symbol]) > 96:  # keep 24h of 15-min readings
                    self.has_history[symbol].pop(0)
                
                # Update baseline
                self.baseline[symbol] = data
                
            except Exception as e:
                print(f"Monitor error for {symbol}: {e}")
    
    async def run(self, interval_seconds: int = 900):
        """Run monitor continuously."""
        print(f"Token monitor started. {len(self.tokens)} tokens, {interval_seconds}s interval.")
        while True:
            await self.monitor_cycle()
            await asyncio.sleep(interval_seconds)
```

---

## Pattern 4 — Weather integration

```python
# patterns/weather_integration.py
"""
Fetches match-day weather and applies SportMind weather modifiers.
Critical for: cricket dew factor, F1 wet race, outdoor athletics.
"""
import aiohttp
from dataclasses import dataclass
from typing import Optional

OPENWEATHER_API = "https://api.openweathermap.org/data/2.5/forecast"
# Set your API key: export OPENWEATHER_KEY=your_key_here
import os
API_KEY = os.environ.get("OPENWEATHER_KEY", "")

@dataclass
class WeatherSignal:
    venue:             str
    match_time_utc:    str
    rain_probability:  float   # 0.0 - 1.0
    wind_speed_ms:     float
    temperature_c:     float
    humidity_pct:      float
    dew_risk:          str     # LOW / MODERATE / HIGH / VERY_HIGH
    weather_modifier:  float   # SportMind modifier to apply
    sport_notes:       list[str]

async def get_weather_signal(lat: float, lon: float, sport: str,
                              match_time_utc: str, venue: str) -> WeatherSignal:
    """
    Fetch weather forecast and return SportMind weather signal.
    """
    params = {
        "lat": lat, "lon": lon,
        "appid": API_KEY,
        "units": "metric",
        "cnt": 8  # 24 hours of 3-hour forecasts
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(OPENWEATHER_API, params=params) as r:
            data = await r.json()
    
    # Find forecast closest to match time
    target_dt = match_time_utc
    forecast = data["list"][0]  # Simplified: use next forecast
    
    rain_prob = forecast.get("pop", 0)
    wind      = forecast.get("wind", {}).get("speed", 0)
    temp      = forecast["main"]["temp"]
    humidity  = forecast["main"]["humidity"]
    
    # Sport-specific weather intelligence
    notes    = []
    modifier = 1.00
    dew_risk = "LOW"
    
    if sport == "cricket":
        # Dew factor for evening T20s in South Asia
        if humidity > 70 and temp > 20:
            dew_risk = "HIGH" if humidity > 80 else "MODERATE"
            notes.append(f"DEW RISK {dew_risk}: batting second advantage +10-12%")
            modifier = 1.00  # Modifier applied to second-innings team, not overall
        if rain_prob > 0.4:
            notes.append(f"DLS RISK: rain {rain_prob*100:.0f}% → pre-match analysis may be superseded")
            modifier *= 0.88  # Uncertainty discount
    
    elif sport == "formula1":
        if rain_prob > 0.4:
            notes.append(f"WET RACE SIGNAL: rain {rain_prob*100:.0f}% → hardware tier reset")
            notes.append("Apply wet-race modifier: specialist advantage overrides constructor tier")
            modifier = 0.70  # Hardware advantage compressed significantly in wet
    
    elif sport in ("football", "rugby"):
        if wind > 15:  # m/s (~35mph)
            notes.append(f"HIGH WIND: {wind:.1f}m/s → kicking game affected; apply × 0.92 to goal-based modifiers")
            modifier *= 0.95
        if rain_prob > 0.6:
            notes.append(f"HEAVY RAIN LIKELY: {rain_prob*100:.0f}% → slippery surface; physical teams advantaged")
    
    elif sport == "golf":
        if wind > 8:  # m/s (~18mph)
            notes.append(f"SIGNIFICANT WIND: {wind:.1f}m/s → scoring average +{wind*0.2:.1f} strokes")
            modifier *= 0.90  # Form-based prediction less reliable
    
    return WeatherSignal(
        venue=venue,
        match_time_utc=match_time_utc,
        rain_probability=rain_prob,
        wind_speed_ms=wind,
        temperature_c=temp,
        humidity_pct=humidity,
        dew_risk=dew_risk,
        weather_modifier=modifier,
        sport_notes=notes
    )
```

---

## Pattern 5 — Complete pre-match integration pipeline

```python
# patterns/full_integration.py
"""
Full integration: SportMind stack + live macro + live lineup + live weather.
The complete production pre-match signal pipeline.
"""
import asyncio
from datetime import datetime, timezone

async def full_prematch_signal(
    sport:      str,
    event_id:   str,
    home_team:  str,
    away_team:  str,
    venue_lat:  float,
    venue_lon:  float,
    match_utc:  str
) -> dict:
    """
    Generate a complete pre-match signal integrating all live data sources.
    """
    
    print(f"[{event_id}] Starting full pre-match integration...")
    
    # Step 1: Load SportMind stack (static — loaded once per session or fetched from API)
    stack = load_sportmind_stack(sport, "fan_token_tier1")
    
    # Step 2: Fetch all live data in parallel
    macro_task   = asyncio.create_task(update_macro_state())
    weather_task = asyncio.create_task(
        get_weather_signal(venue_lat, venue_lon, sport, match_utc, f"{home_team} venue")
    )
    
    macro, weather = await asyncio.gather(macro_task, weather_task)
    
    # Step 3: Apply SportMind reasoning chain
    macro_modifier   = macro["macro_state"]["crypto_cycle"]["macro_modifier"]
    macro_phase      = macro["macro_state"]["crypto_cycle"]["phase"]
    weather_modifier = weather.weather_modifier
    
    # Composite modifier
    composite = round(macro_modifier * weather_modifier, 3)
    
    # SMS calculation
    layers_present = count_loaded_layers(stack)
    sms = round(
        (layers_present/5) * 0.35 * 100 +
        (1.0 if macro_modifier >= 0.75 else 0.6) * 0.25 * 100 +
        0.25 * 100 +
        min(macro_modifier, 1.0) * 0.15 * 100,
        1
    )
    
    # Flags
    hours_to_match = (datetime.fromisoformat(match_utc.replace("Z","+00:00")) -
                      datetime.now(timezone.utc)).total_seconds() / 3600
    
    flags = {
        "lineup_unconfirmed":    hours_to_match > 2,
        "macro_override_active": macro_modifier < 0.75,
        "weather_risk":          weather.rain_probability > 0.4,
        "dew_risk_active":       weather.dew_risk in ("HIGH","VERY_HIGH"),
        "position_size": "50%" if hours_to_match > 2 else "100%"
    }
    
    return {
        "event_id":    event_id,
        "sport":       sport,
        "home_team":   home_team,
        "away_team":   away_team,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        
        "signal": {
            "adjusted_score": round(55.0 * composite, 1),
            "composite_modifier": composite,
            "confidence_tier": "MEDIUM" if sms >= 60 else "LOW",
            "recommended_action": "WAIT" if flags["macro_override_active"] else "ENTER"
        },
        
        "sportmind_score": {"sms": sms, "sms_tier": "GOOD" if sms >= 60 else "PARTIAL"},
        
        "live_inputs": {
            "macro":   {"phase": macro_phase, "modifier": macro_modifier},
            "weather": {"modifier": weather_modifier, "notes": weather.sport_notes}
        },
        
        "modifiers": {"flags": flags},
        
        "data_freshness": {
            "macro_last_updated": macro["macro_state"]["last_updated"],
            "weather_fetched_at": datetime.now(timezone.utc).isoformat(),
            "lineup_confirmed":   not flags["lineup_unconfirmed"]
        }
    }


# Placeholder implementations (replace with actual implementations)
def load_sportmind_stack(sport, use_case): return {"files": [], "sport": sport}
def count_loaded_layers(stack): return 4  # Placeholder
```

---

## Integration with the MCP server

```python
# Add live data integration to sportmind_mcp.py
# Extend build_signal() to incorporate real-time weather and macro

async def build_signal_with_live_data(sport, event_id, use_case,
                                       home_team, away_team, include_defi,
                                       venue_lat=None, venue_lon=None,
                                       match_utc=None):
    """Extended build_signal that fetches live data if coordinates provided."""
    
    # Base signal from SportMind stack
    base = build_signal(sport, event_id, use_case, home_team, away_team, include_defi)
    
    # Add live weather if venue provided
    if venue_lat and venue_lon and match_utc:
        weather = await get_weather_signal(venue_lat, venue_lon, sport, match_utc, "venue")
        base["live_weather"] = {
            "modifier": weather.weather_modifier,
            "notes":    weather.sport_notes,
            "rain_probability": weather.rain_probability
        }
        # Apply weather modifier
        base["signal"]["adjusted_score"] = round(
            base["signal"]["adjusted_score"] * weather.weather_modifier, 1
        )
    
    return base
```

---

*MIT License · SportMind · sportmind.dev*
*See `core/temporal-awareness.md` for data freshness tiers that govern integration patterns.*
*See `platform/live-signals.md` for the complete live signal category taxonomy.*
