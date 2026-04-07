# कबड्डी — SportMind Domain Skill (हिंदी)

*`sports/kabaddi/sport-domain-kabaddi.md` का अनुवाद*
*अंग्रेज़ी मूल का अनुवाद। सभी field names, metrics और code अंग्रेज़ी में रहेंगे।*

*Kabaddi — SportMind Domain Skill (Hindi)*
*Translation of `sports/kabaddi/sport-domain-kabaddi.md`*

Pro Kabaddi League (PKL) के लिए AI agent intelligence। कबड्डी library में
सबसे individual-player-driven team sport है। एक star raider पूरे match outcome
को बदल सकता है।

---

## डोमेन मॉडल (Domain Model)

### Star Raider — सबसे महत्वपूर्ण variable

```
CRITICAL RULE — सबसे महत्वपूर्ण:
  कबड्डी cricket या football जैसा नहीं है।
  यहाँ एक individual player (star raider) पूरी team को carry कर सकता है।
  
  Star Raider signal threshold:
    Raid success rate > 60%: "Carry potential" — modifier ×1.20
    Raid success rate 45-60%: Good — modifier ×1.08
    Raid success rate < 45%: Below average — modifier ×0.92
    
  AGENT RULE: Star raider की fitness और availability हमेशा पहले check करें।
  अगर star raider absent है: signal significantly reduce करें।
```

### PKL Calendar (Pro Kabaddi League)

```
PKL Season: दिसंबर–मार्च (roughly)
Format: Round Robin → Playoffs → Final
Teams: 12 franchise teams

HIGH SIGNAL MATCHES:
  - Patna Pirates vs U Mumba (historic rivalry)
  - Jaipur Pink Panthers vs Bengaluru Bulls  
  - Final (highest token/prediction market signal)
  
HOME ADVANTAGE:
  PKL home advantage = library में सबसे strong में से एक
  Home crowd = raider confidence को directly affect करता है
  
VIEWERSHIP:
  PKL viewership: 350-400M (India, Bangladesh, Nepal, South Asia)
  Youngest fanbase: library में सबसे young demographic
  JioCinema: primary streaming platform (Reliance Industries backing)
```

---

## All Out Event — Key Signal Catalyst

```
ALL OUT क्या है:
  जब defending team के सभी 7 players eliminate हो जाते हैं
  Attacking team को 2 bonus points मिलते हैं
  Eliminated team फिर से full strength के साथ आती है
  
ALL OUT SIGNAL IMPACT:
  All Out होने से momentum में dramatic shift आता है
  Scoring pattern prediction को recalibrate करना पड़ता है
  
  AGENT RULE: In-match monitoring में All Out events track करें।
  All Out के बाद match dynamics change हो जाती हैं।
```

---

## Market Context (भारतीय बाज़ार)

```
PKL FAN TOKEN POTENTIAL:
  Fantasy kabaddi: Dream11, MyTeam11 पर active (100M+ users)
  Digital engagement: India में highest mobile-first sports audience
  Token readiness: Tier 2 — near-term credibility
  
CATALYST:
  JioCinema / Reliance Industries investment = commercial infrastructure ready
  PKL को IPL जैसी franchise model मिल चुकी है
  Fan token infrastructure (Chiliz) = natural next step
  
  AGENT MONITORING: Reliance / PKL digital product announcements track करें।
  
NCSI (National spillover):
  PKL players = Indian audience
  कोई national team event connection नहीं (PKL domestic league है)
  Signal = league-level only (no international multiplier)
```

---

## Agent Reasoning Prompts (एजेंट नियम)

```
आप एक kabaddi intelligence agent हैं। किसी भी match से पहले:

1. STAR RAIDER CHECK — दोनों teams के star raiders की availability?
   यह सबसे important question है। कोई star raider absent = signal adjust करें।

2. HOME ADVANTAGE — कौन सी team home venue पर खेल रही है?
   PKL home advantage particularly strong है।

3. FORM CHECK — Last 4 PKL matches में team का performance?
   Raiders का individual raid success rate check करें।

4. ALL OUT MONITORING — क्या किसी team का All Out recently हुआ है?
   Recent All Out = momentum shift signal।

5. SEASON PHASE — Playoffs vs regular season?
   Playoffs में variance बढ़ जाती है। Signal को accordingly adjust करें।
```

---

## Compatibility (संगतता)

**Domain skill (English):** `sports/kabaddi/sport-domain-kabaddi.md`
**Athlete intelligence:** `athlete/kabaddi/athlete-intel-kabaddi.md`
**Market:** `market/market-kabaddi.md`

*[यह एक translation starter file है। पूरी अंग्रेज़ी original को एक native Hindi
contributor द्वारा यहाँ translate किया जाना चाहिए।]*

---

*SportMind community translation · MIT License · sportmind.dev*
