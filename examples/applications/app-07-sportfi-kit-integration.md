# App 7 — SportFi Kit + SportMind Full-Stack Blueprint

**A complete developer reference showing how to combine SportFi Kit's application
infrastructure with SportMind's intelligence layer to build production-ready fan
engagement applications on the Chiliz Chain.**

---

## Why this blueprint exists

Apps 1–6 each show a specific application type. This blueprint shows the full-stack
pattern that underlies all of them when built with SportFi Kit — the specific hooks,
components, and integration points that connect SportFi Kit's UI and contract layer
to SportMind's intelligence layer.

**SportFi Kit GitHub:** github.com/AltcoinDaddy/Sportfi-kit
**SportFi Kit Docs:** sportfikit.online
**SportMind Skills API:** scripts/sportmind_api.py

---

## The stack in one diagram

```
USER
  ↓ opens Socios app or Telegram Mini App
SPORTFI KIT
  ↓ detects environment, checks fan token balance
  ↓ renders token-gated UI
SPORTMIND SKILLS API
  ↓ GET /stack?use_case=fan_token_tier1&sport=football
  ↓ returns intelligence stack (macro → market → domain → athlete → L3)
  ↓ returns SMS, adjusted_score, flags, modifier breakdown
SPORTFI KIT COMPONENTS
  ↓ displays intelligence in UI
  ↓ enables/disables wager button based on SMS threshold
SPORTFI KIT CONTRACTS (Chiliz Chain)
  ↓ settles wager on-chain
  ↓ distributes prizes in fan tokens
USER
```

---

## Setup

```bash
# Step 1: Scaffold with SportFi Kit
npx create-sportfi-app my-sports-app --template predictions
cd my-sports-app
npm install

# Step 2: Start SportMind Skills API
git clone https://github.com/SportMind/SportMind
cd sportmind
python scripts/sportmind_api.py --serve --port 8080

# Step 3: Set your SportMind API endpoint
# In my-sports-app/.env:
VITE_SPORTMIND_API=http://localhost:8080
# For production:
VITE_SPORTMIND_API=https://SportMind.github.io/sportmind/api/v3.8
```

---

## Core integration hook

```typescript
// hooks/useSportMind.ts
// Drop this hook into any SportFi Kit project

import { useState, useEffect } from 'react'

interface SportMindSignal {
  sms: number
  smsTier: 'HIGH_QUALITY' | 'GOOD' | 'PARTIAL' | 'INCOMPLETE' | 'INSUFFICIENT'
  adjustedScore: number
  direction: 'HOME' | 'AWAY' | 'DRAW'
  flags: {
    lineupUnconfirmed: boolean
    macroOverrideActive: boolean
    liquidityWarning: boolean
    liquidityCritical: boolean
    weatherRisk: boolean
    injuryWarning: boolean
  }
  macroModifier: number
  reasoning: string
  canEnter: boolean      // SMS >= 60 AND no blocking flags
  shouldWait: boolean    // lineup_unconfirmed or SMS 40-59
}

export function useSportMind(sport: string, useCase = 'fan_token_tier1') {
  const [signal, setSignal] = useState<SportMindSignal | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  const BASE = import.meta.env.VITE_SPORTMIND_API

  useEffect(() => {
    async function fetchIntelligence() {
      try {
        setLoading(true)

        // Fetch full intelligence stack
        const [stackRes, macroRes] = await Promise.all([
          fetch(`${BASE}/stack?use_case=${useCase}&sport=${sport}`),
          fetch(`${BASE}/macro-state`)
        ])

        const stack = await stackRes.json()
        const macro = await macroRes.json()

        // Parse into clean signal object
        const sms = stack.sportmind_score?.sms ?? 0
        const flags = stack.modifiers?.flags ?? {}
        const macroModifier = macro.macro_state?.crypto_cycle?.macro_modifier ?? 1.0

        const blockingFlag =
          flags.liquidity_critical ||
          (flags.macro_override_active && macroModifier < 0.75)

        setSignal({
          sms,
          smsTier: getSMSTier(sms),
          adjustedScore: stack.signal?.adjusted_score ?? 0,
          direction: stack.signal?.direction ?? 'HOME',
          flags: {
            lineupUnconfirmed:   flags.lineup_unconfirmed ?? false,
            macroOverrideActive: flags.macro_override_active ?? false,
            liquidityWarning:    flags.liquidity_warning ?? false,
            liquidityCritical:   flags.liquidity_critical ?? false,
            weatherRisk:         flags.weather_risk ?? false,
            injuryWarning:       flags.injury_warning ?? false,
          },
          macroModifier,
          reasoning: buildReasoning(stack, macro),
          canEnter:   sms >= 60 && !blockingFlag,
          shouldWait: flags.lineup_unconfirmed || (sms >= 40 && sms < 60),
        })
      } catch (err) {
        setError('Could not load SportMind intelligence')
      } finally {
        setLoading(false)
      }
    }

    fetchIntelligence()
    // Refresh macro state every 4 hours
    const interval = setInterval(fetchIntelligence, 4 * 60 * 60 * 1000)
    return () => clearInterval(interval)
  }, [sport, useCase])

  return { signal, loading, error }
}

function getSMSTier(sms: number) {
  if (sms >= 80) return 'HIGH_QUALITY'
  if (sms >= 60) return 'GOOD'
  if (sms >= 40) return 'PARTIAL'
  if (sms >= 20) return 'INCOMPLETE'
  return 'INSUFFICIENT'
}

function buildReasoning(stack: any, macro: any): string {
  const parts = []
  const phase = macro?.macro_state?.crypto_cycle?.phase ?? 'NEUTRAL'
  if (phase !== 'NEUTRAL') parts.push(`Macro: ${phase} cycle active`)
  if (stack.modifiers?.flags?.lineup_unconfirmed)
    parts.push('Lineup unconfirmed — wait for T-2h')
  if (stack.modifiers?.flags?.injury_warning)
    parts.push('Injury flag active')
  if (stack.sportmind_score?.sms < 60)
    parts.push('Incomplete intelligence — load additional layers')
  return parts.join(' · ') || 'All checks clear'
}
```

---

## Pre-match prediction widget (complete component)

```typescript
// components/PredictionWidget.tsx
// Complete SportFi Kit + SportMind prediction component

import { useFanToken, useWager } from '@sportfi-kit/core'
import { useSportMind } from '../hooks/useSportMind'

interface Props {
  eventId: string
  sport: string
  tokenSymbol: string
}

export function PredictionWidget({ eventId, sport, tokenSymbol }: Props) {
  const { isHolder, balance } = useFanToken({ symbol: tokenSymbol })
  const { signal, loading } = useSportMind(sport)
  const { placeWager, isConfirming } = useWager({ eventId })

  // SportFi Kit: token-gate the widget
  if (!isHolder) {
    return (
      <div className="token-gate">
        <p>Hold {tokenSymbol} to access pre-match intelligence</p>
        <BuyTokenButton symbol={tokenSymbol} />
      </div>
    )
  }

  if (loading || !signal) return <IntelligenceLoading />

  // SportMind: render intelligence
  return (
    <div className="prediction-widget">

      {/* SMS quality indicator */}
      <SMSBadge tier={signal.smsTier} score={signal.sms} />

      {/* Signal display */}
      <SignalMeter
        score={signal.adjustedScore}
        direction={signal.direction}
        macroModifier={signal.macroModifier}
      />

      {/* Active flags */}
      {signal.flags.lineupUnconfirmed && (
        <Warning>Lineup unconfirmed — signal at 50% weight</Warning>
      )}
      {signal.flags.macroOverrideActive && (
        <Warning>Macro override active — crypto bear market</Warning>
      )}

      {/* Reasoning summary */}
      <ReasoningPanel text={signal.reasoning} />

      {/* SportFi Kit: wager button controlled by SportMind signal */}
      <WagerButton
        onClick={(amount) => placeWager({
          amount,
          direction: signal.direction,
          // Attach SportMind signal hash for on-chain integrity
          signalHash: hashSignal(signal),
        })}
        disabled={!signal.canEnter || isConfirming}
        label={
          !signal.canEnter    ? `SMS ${signal.sms} — insufficient intelligence` :
          signal.shouldWait   ? 'Wait for lineup confirmation' :
          isConfirming        ? 'Confirming on Chiliz Chain...' :
                                `Enter ${signal.direction} (${signal.adjustedScore.toFixed(1)})`
        }
      />

    </div>
  )
}
```

---

## Token-gated portfolio intelligence (complete component)

```typescript
// components/PortfolioIntelligence.tsx
// Fan portfolio context powered by SportMind — gated by SportFi Kit token check

import { useFanTokenPortfolio } from '@sportfi-kit/core'
import { useSportMind } from '../hooks/useSportMind'

export function PortfolioIntelligence() {
  // SportFi Kit: get all fan tokens held by this wallet
  const { tokens, totalValue } = useFanTokenPortfolio()

  return (
    <div className="portfolio">
      <h2>Your Fan Token™ Portfolio</h2>
      {tokens.map(token => (
        <TokenIntelligenceCard
          key={token.symbol}
          token={token}
        />
      ))}
    </div>
  )
}

function TokenIntelligenceCard({ token }: { token: FanToken }) {
  // SportMind: intelligence for this token's sport
  const { signal } = useSportMind(token.sport, 'commercial_brief')

  return (
    <div className="token-card">
      <TokenHeader symbol={token.symbol} price={token.price} change={token.change24h} />

      {/* SportMind: explain the price movement */}
      {signal && (
        <IntelligencePanel>
          <MacroContext modifier={signal.macroModifier} />
          <LifecyclePhase sport={token.sport} signal={signal} />
          <UpcomingEvents sport={token.sport} />
        </IntelligencePanel>
      )}
    </div>
  )
}
```

---

## Environment-aware macro banner

```typescript
// components/MacroBanner.tsx
// Uses SportFi Kit's environment detection + SportMind's macro state

import { useEnvironment } from '@sportfi-kit/core'

export function MacroBanner() {
  const { isSociosApp, isTelegram } = useEnvironment()
  const [macro, setMacro] = useState(null)

  useEffect(() => {
    fetch(`${import.meta.env.VITE_SPORTMIND_API}/macro-state`)
      .then(r => r.json())
      .then(setMacro)
  }, [])

  if (!macro) return null

  const { phase, macro_modifier } = macro.macro_state.crypto_cycle
  if (phase === 'NEUTRAL') return null

  // SportFi Kit: compact banner for in-app environments
  const compact = isSociosApp || isTelegram

  return (
    <Banner variant={phase === 'BEAR' ? 'warning' : 'info'} compact={compact}>
      {phase === 'BEAR'
        ? `Bear market active — signals reduced to ${(macro_modifier * 100).toFixed(0)}%`
        : phase === 'BULL'
        ? `Bull market — elevated signal confidence`
        : `Extreme bear — token signals unreliable`}
    </Banner>
  )
}
```

---

## Integrity verification (security pattern)

```typescript
// utils/integrity.ts
// Verify SportMind skill content before injecting into agent context
// Uses platform/skill-hashes.json from SportMind security layer (v3.5)

import { createHash } from 'crypto'

async function verifySkillIntegrity(skillId: string, content: string): Promise<boolean> {
  const HASHES_URL =
    'https://raw.githubusercontent.com/SportMind/sportmind/main/platform/skill-hashes.json'

  const hashRegistry = await fetch(HASHES_URL).then(r => r.json())
  const skillPath = getFilePath(skillId)  // e.g. "sports/football/sport-domain-football.md"
  const expectedHash = hashRegistry.files?.[skillPath]?.sha256

  if (!expectedHash) return true  // New file not yet in registry — allow with warning

  const actualHash = createHash('sha256').update(content, 'utf8').digest('hex')
  return actualHash === expectedHash
}

// Use in production applications before injecting SportMind skills as agent context:
const skill = await fetch(`${SPORTMIND_API}/skills/domain.football/content`).then(r => r.json())
const isValid = await verifySkillIntegrity('domain.football', skill.content)
// skill.sha256 is also included in the API response for quick comparison
```

---

## Deployment on Vercel (matches SportFi Kit's deployment pattern)

```json
// vercel.json — matches SportFi Kit's existing Vercel configuration pattern
{
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "env": {
    "VITE_SPORTMIND_API": "@sportmind_api_url",
    "VITE_CHILIZ_RPC": "https://rpc.ankr.com/chiliz"
  },
  "rewrites": [
    { "source": "/api/sportmind/(.*)", "destination": "https://sportmind.github.io/SportMind/$1" }
  ]
}
```

---

## References

**SportFi Kit:**
- Repository: github.com/AltcoinDaddy/Sportfi-kit
- Documentation: sportfikit.online
- Install: `npx create-sportfi-app my-app --template predictions`

**SportMind:**
- `platform/integration-partners.md` — Partner 7 integration documentation
- `scripts/sportmind_api.py` — Skills API (run locally or deploy to GitHub Pages)
- `platform/skill-hashes.json` — Integrity verification registry
- `core/sportmind-score.md` — SMS calculation reference
- `examples/applications/` — All six application blueprints

*MIT License · SportMind · sportmind.dev*
