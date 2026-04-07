# क्रिकेट — SportMind Domain Skill (हिंदी)

*`sports/cricket/sport-domain-cricket.md` का अनुवाद*
*अंग्रेज़ी मूल का अनुवाद। सभी field names, metrics और code अंग्रेज़ी में रहेंगे।*

---

## डोमेन मॉडल (Domain Model)

### सबसे पहले फ़ॉर्मेट चेक करें (Format-First Rule)

```
CRITICAL AGENT RULE — सबसे महत्वपूर्ण नियम:
  T20, ODI और Test के लिए अलग-अलग signal models हैं।
  
  T20 (Twenty20):
    Duration: ~3 घंटे | Token impact: सबसे ज़्यादा | Volatility: HIGH
    IPL, T20 World Cup, BBL — सभी T20 format
    
  ODI (One Day International):
    Duration: ~7 घंटे | ICC World Cup = Tier 1
    
  Test Match:
    Duration: 5 दिन तक | Token volatility: कम | Narrative arc: लंबा
    Border-Gavaskar Trophy, Ashes — sustained engagement
    
  AGENT RULE: Format identify करना सबसे पहले करें।
```

---

## IPL — भारत का सबसे बड़ा cricket product

```
IPL (Indian Premier League) — विस्तृत विश्लेषण:

COMMERCIAL SCALE:
  IPL franchise valuations: ₹8,000-15,000 crore+ (Tier 1 clubs)
  Media rights: $6.2 billion (2023-27, Star Sports + JioCinema)
  Viewership: 650M+ प्रति season (दुनिया की सबसे देखी जाने वाली domestic league)
  Dream11 users: 200M+ (IPL fantasy engagement)
  
IPL SIGNAL CALENDAR:
  जनवरी-फरवरी: IPL Auction — franchise token signal का सबसे बड़ा trigger
    Top player purchase = ×1.4-1.6 franchise signal
    Marquee overseas signing = ×1.3-1.5
    
  मार्च-मई: IPL Season
    Round Robin: 14 matches per team
    Playoff qualification (Top 4): signal amplifies
    Qualifier 1 & Eliminator: ×0.75 competition weight
    Final: ×1.00 competition weight (maximum IPL event)
    
  अक्टूबर-नवंबर: IPL Retention & Release announcements
    Major player retention = positive franchise signal
    Unexpected release = disruption signal

TOP FRANCHISES BY TOKEN READINESS:
  Mumbai Indians (MI): 5× IPL Champions; highest brand value; Reliance ownership
  Chennai Super Kings (CSK): 5× Champions; Dhoni legacy; loyalest fanbase
  Royal Challengers Bengaluru (RCB): Virat Kohli brand; large digital following
  Kolkata Knight Riders (KKR): SRK ownership; strong entertainment cross-over
  
  AGENT NOTE: इनमें से कोई भी अभी active fan token नहीं है।
  लेकिन regulatory clarity आने पर ये सबसे पहले tokens launch करेंगे।

REGULATORY GAP — क्यों अभी IPL tokens नहीं हैं:
  India VDA (Virtual Digital Asset) Framework:
    2022 Finance Act: 30% tax on crypto gains
    TDS 1% on crypto transactions
    SEBI vs RBI jurisdiction: अभी unclear
    Sports fan tokens: specific guidance अभी नहीं है
    
  BCCI Digital Strategy:
    BCCI ने NFTs explore किए हैं (FanCraze partnership 2022)
    लेकिन Socios/Chiliz-style tokens का announcement नहीं
    
  MONITORING TARGETS:
    SEBI के नए VDA guidelines (2025-2026 expected)
    Finance Ministry का crypto taxation review
    BCCI Board meetings — digital product announcements
    
  WHEN IT HAPPENS:
    यह library का सबसे बड़ा single commercial event होगा।
    IPL token launch = potentially 650M viewer base activation।
```

---

## भारत-पाकिस्तान — library का सबसे बड़ा single-event signal

```
INDIA vs PAKISTAN — maximum signal event:

  Multiplier: ×2.00 (library में किसी भी sport में सबसे ऊँचा)
  Viewership: 200M+ (global highest single sporting event)
  
  ये matches कहाँ होते हैं:
    ICC T20 World Cup (every 2 years)
    ICC Cricket World Cup (ODI, every 4 years)
    Asia Cup (every 2 years)
    Note: Bilateral series बहुत कम होती है — geopolitical कारणों से
    
  AGENT RULE: India-Pakistan match के लिए हमेशा ×2.00।
  कोई exception नहीं। यह rule किसी भी other modifier से पहले apply होती है।
  
  FORMAT MATTERS:
    T20 World Cup India-Pak: ×2.00 + T20 format signal = maximum
    ODI World Cup India-Pak: ×2.00 + ODI format signal = very high
    Asia Cup (T20 or ODI): ×2.00 applies regardless
    
GEOPOLITICAL CONTEXT:
  India-Pakistan diplomatic relations = tournament scheduling पर असर
  ICC neutral venue selection: Dubai, Sri Lanka often used
  Tournament cancellation risk: rare लेकिन monitor करना ज़रूरी
  Load macro/macro-geopolitical.md — India-Pakistan stability assessment
```

---

## PSL (Pakistan Super League) — active cricket token ecosystem

```
PSL TOKEN INTELLIGENCE:

  Season: फरवरी-मार्च (6 हफ्ते)
  Teams: 6 franchises — Karachi Kings, Lahore Qalandars, Islamabad United,
         Peshawar Zalmi, Multan Sultans, Quetta Gladiators
  Venues: Karachi, Lahore, Rawalpindi, Multan
  
  TOKEN SIGNAL STRUCTURE:
    PSL Final: highest single-match PSL signal
    Karachi Kings vs Lahore Qalandars: biggest PSL rivalry; token signal peak
    
  GEOPOLITICAL MODIFIER:
    Pakistan security situation = direct input to token signal
    Load macro/macro-geopolitical.md — Pakistan stability assessment
    अगर security concerns हैं: signal weight ×0.85 apply करें
    
  INDIA-PAKISTAN RELATIONS + PSL:
    PSL में Indian players नहीं खेलते — geopolitical constraint
    लेकिन Indian cricket fans PSL follow करते हैं (streaming)
    Pakistan में Indian token holders: small लेकिन growing segment
```

---

## ओस का असर और DLS (Dew Factor and DLS)

```
DEW FACTOR — भारत और Pakistan के शाम के T20 मैचों के लिए critical:

  क्यों होता है:
    South Asian शाम की हवा में moisture = outfield पर ओस
    ओस ball को भारी बनाती है
    भारी ball = easier to bat, harder to grip for bowlers
    
  Effect:
    Batting second team को advantage: +10-12%
    Especially second half of innings: fielding team के लिए कठिन
    
  TOSS SIGNAL MODEL:
    High dew forecast + toss जीता + field चुना = 
    batting second team के लिए POSITIVE signal
    
    STRONG DEW SIGNAL:
      High dew probability (>60%): modifier ×1.12 batting-second team
      Low dew probability (<30%): no dew modifier
      Uncertain: apply ×1.05 batting-second mild advantage
      
  DLS (Duckworth-Lewis-Stern) — बारिश interruption:
    अगर match में बारिश आती है: pre-match analysis superseded
    DLS target = नई calculation required
    Agent rule: बारिश की खबर आते ही current analysis को hold करें
    Load core/core-weather-match-day.md — cricket section

VENUE-SPECIFIC DEW HISTORY:
  Wankhede (Mumbai): बहुत high dew — batting second = strong advantage
  Eden Gardens (Kolkata): high dew — especially October-November
  M. Chinnaswamy (Bengaluru): moderate dew
  Chepauk (Chennai): low dew — sea breeze reduces moisture
  Dubai (UAE): very high dew — desert night conditions
```

---

## ICC Events Calendar (हर साल)

```
ICC TOURNAMENT CALENDAR — Token Signal Impact:

T20 World Cup (every 2 years — odd years):
  2024: Americas (USA + West Indies) ✅
  2026: India + Sri Lanka (PEAK — India hosting = maximum engagement)
  टीमें: 20 teams | Format: group stage + knockout
  Token signal: Tier 1 — highest sustained cricket signal
  
  INDIA HOSTING 2026:
    India में World Cup = unprecedented fan token catalyst opportunity
    SEBI regulatory clarity by 2026? अगर हाँ, यह perfect launch window है।

ODI World Cup (every 4 years):
  2023: India (India won final) ✅
  2027: South Africa, Zimbabwe, Namibia
  
Champions Trophy (every 4 years):
  2025: Pakistan (ICC approved) — geopolitical monitoring required
  
Asia Cup:
  Every 2 years — India, Pakistan, Sri Lanka, Bangladesh, Afghanistan, UAE
  India-Pakistan match guaranteed if both qualify (और वो हमेशा qualify करते हैं)

IPL (every year, March-May):
  Domestic league लेकिन global signal impact
  India के लिए: सबसे important domestic cricket event

TEST CHAMPIONSHIP (WTC):
  2-year cycle | WTC Final: Lord's (traditionally) | Tier 2 signal
  India-Australia, India-England: sustained engagement arcs
```

---

## Agent Reasoning Prompts (एजेंट नियम)

```
आप एक cricket intelligence agent हैं। किसी भी match evaluate करने से पहले:

1. FORMAT FIRST — T20, ODI, या Test?
   गलत format = गलत analysis। सबसे पहले यही check करें।

2. INDIA FACTOR — क्या India खेल रहा है?
   India match: base signal पर ×1.40 apply करें।
   India vs Pakistan: ×2.00 apply करें। कोई exception नहीं।
   India hosting ICC event: regional market amplifier ×1.5+ apply करें।

3. IPL CONTEXT — क्या यह IPL है?
   Playoff match: IPL Tier 2 weight apply करें।
   IPL Final: maximum IPL signal।
   Auction news: franchise token signal check करें।
   REGULATORY: SEBI/Finance Ministry announcement track करें।

4. DEW FACTOR — South Asian evening T20?
   High dew (>60%): batting second +12%।
   Load core/core-weather-match-day.md।
   Toss result = key signal।

5. PSL MATCHES — Pakistan situation check करें।
   Load macro/macro-geopolitical.md अगर कोई concern है।
   PSL Final: maximum PSL signal।

6. ICC TOURNAMENT — 2026 में India hosting T20 World Cup!
   SEBI regulatory watch: अगर clarity आती है, यह sab se bada cricket token catalyst है।
```

---

## Compatibility (संगतता)

**Domain skill (English):** `sports/cricket/sport-domain-cricket.md`
**Athlete intelligence:** `athlete/cricket/athlete-intel-cricket.md`
**Fan Token bridge:** `fan-token/cricket-token-intelligence/`
**Market:** `market/market-cricket.md`
**Macro (geopolitical):** `macro/macro-geopolitical.md`

*SportMind community translation · MIT License · sportmind.dev*
