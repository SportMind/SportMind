---
name: cricket-ipl
description: >
  IPL-specific intelligence framework. The Indian Premier League is the highest
  fan token potential cricket competition globally and the richest cricket league
  by revenue. Covers season structure, toss advantage, home venue, player
  availability risk, auction intelligence, powerplay signals, and fan token pipeline.
---

# Cricket — IPL Sport Domain Intelligence

**How to reason about IPL matches and fan token signals.**
The IPL is the highest commercial value cricket competition and the highest fan token
opportunity in cricket globally.

---

## Season structure

```
COMPETITION: Indian Premier League
FORMAT: T20 franchise competition
TEAMS: 10 franchises
SEASON: March to May (overlaps UCL Final period and European football season end)
MATCHES: 74 league matches + 4 playoff matches

PLAYOFF FORMAT:
  Qualifier 1:  top 2 teams — winner goes to final
  Eliminator:   3rd vs 4th — loser eliminated
  Qualifier 2:  Eliminator winner vs Qualifier 1 loser
  Final:        Qualifier 1 winner vs Qualifier 2 winner

PLAYOFF SIGNAL WEIGHTS:
  Qualifier 1:  ×1.30
  Eliminator:   ×1.35 (knockout — loser's season ends)
  Qualifier 2:  ×1.40 (knockout — loser's season ends)
  Final:        ×1.80
```

---

## Core match modifiers

```
TOSS ADVANTAGE BY MATCH TYPE:
  Evening matches with dew (standard IPL primetime):
    Batting second structural advantage.
    Apply: ×1.06 — same dew factor as standard T20 framework.
    Reference: sports/cricket-t20.md for full dew framework.
  Afternoon matches (limited dew risk):
    Toss advantage minimal.
    Apply standard coin-flip assumption — no structural bias.

HOME VENUE ADVANTAGE:
  IPL franchises have genuine home advantages:
    Crowd noise, pitch preparation by home groundskeeping, travel reduction.
    Home team wins approximately 55% of IPL matches historically.
    Apply: ×1.04 home advantage modifier.

OVERSEAS PLAYER AVAILABILITY:
  IPL overlaps with international cricket calendar.
  National call-ups can remove key overseas players mid-tournament.
  Overseas players are typically the highest impact players in each squad.
  Overseas player confirmed unavailable (national duty):
    Apply: ×0.88 availability modifier — highest unavailability discount in cricket.
  Key overseas player (top-4 batter or lead pacer):
    Upgrade to ×0.84 if the player is in the top 2 impact roles.

PITCH CONDITIONS:
  IPL venues span the Indian subcontinent — significant pitch variation.
  High scoring venues (Wankhede, Chinnaswamy):
    Batting powerplay performance more predictive — apply powerplay signal below.
  Lower scoring venues (Chennai, Delhi):
    Bowling and fielding quality become relatively more predictive.
```

---

## Auction intelligence

```
IPL AUCTION SYSTEM (unique to IPL — no transfer fee structure):

MEGA AUCTION (every 3 years):
  Major squad restructuring — up to 25 players released and re-auctioned.
  High uncertainty period before mega auction.
  Post-mega-auction: full franchise signal reset required.
  Do not apply pre-auction form modifiers after mega auction.
  Treat each franchise as a new squad until minimum 5 matches of data.

MINI AUCTION (annual in non-mega years):
  Targeted gap-filling — typically 5-10 players per franchise.
  Signal: which positions each franchise targets reveals self-assessment of weaknesses.
  If a franchise bids aggressively for a specific position:
    Apply ×0.88 to that position's modifier for that franchise's pre-mini-auction form.
    (They identified their own weakness — it was real.)

PLAYER UNSOLD AT AUCTION:
  If a previously high-value player goes unsold:
    Significant decline in perceived quality — apply ×0.84 to that player's modifier.
    If the player previously had a high retention value and is now unsold:
    Apply: ×0.80 — sharp credibility decline.

HIGH RETENTION PRICE:
  Franchise retaining a player at their retention price cap signals confidence.
  Apply: ×1.05 to that player's contribution modifier.
  Rationale: franchise has full information on the player's training and fitness —
    high retention price means internal assessment is positive.
```

---

## Powerplay intelligence

```
POWERPLAY SIGNAL (first 6 overs — mandatory batting powerplay):
  Powerplay score above 55 runs: strongly correlates with final total.
  Teams with confirmed dominant powerplay batters at top of order:
    Apply: ×1.06 pre-match advantage modifier when powerplay specialist confirmed.
  Teams with dominant powerplay bowling (swing or pace):
    Apply: ×1.04 pre-match bowling advantage in powerplay conditions.

POWERPLAY RESTRICTION:
  Only 2 fielders permitted outside the ring during powerplay.
  Teams with batters who exploit this structurally (aggressive openers):
    Have a systematic advantage — apply ×1.05 powerplay modifier.

DEATH OVERS (overs 17-20):
  Quality of death bowling is the second most predictive element after powerplay.
  Franchise with top-3 IPL death bowlers in their squad:
    Apply: ×1.04 death bowling advantage modifier.
```

---

## Fan token pipeline

```
CURRENT STATUS: No IPL franchise fan tokens confirmed on Chiliz Chain
  (as of library compilation — monitor for announcements).

IPL FRANCHISE FAN TOKEN OPPORTUNITY:
  Mumbai Indians, Chennai Super Kings, Kolkata Knight Riders — fanbases
  exceeding most European football clubs in raw scale.
  Combined digital following of top 4 IPL franchises rivals the Premier League's
  largest clubs.

INDIA REGULATORY CONTEXT:
  Digital asset regulation in India is active and evolving.
  Reference: macro/macro-regulatory-sportfi.md for India jurisdiction framework.

WHEN IPL FAN TOKENS LAUNCH — apply:
  First mover premium: ×1.40 CDI (largest cricket market, no existing competition)
  India-specific demand: monitor macro/macro-regulatory-sportfi.md India section

IPL DEMAND CYCLE (for any future IPL token):
  Pre-auction (October-December): speculation peak — uncertainty about squad.
  Post-auction: squad clarity signal — apply updated form modifiers.
  Season opener (March): ×1.15 demand — new season signal.
  Playoff qualification confirmed: ×1.25 demand premium.
  Final appearance: ×1.60 demand premium.
  Championship win: ×2.00 demand premium (highest cricket single event signal).
```

---

## Compatibility

**T20 cricket framework:**    `sports/cricket-t20.md`
**Market intelligence:**      `market/market-cricket.md`
**International cycle:**      `market/international-cricket-cycle.md`
**Emerging pipeline:**        `fan-token/emerging-sports-pipeline.md`
**India regulatory:**         `macro/macro-regulatory-sportfi.md`

---

*SportMind v3.97.71 · MIT License · sportmind.dev*
*Overseas player unavailable: ×0.88 — highest unavailability discount in cricket.*
*IPL first mover fan token premium: ×1.40 CDI — largest cricket market.*
