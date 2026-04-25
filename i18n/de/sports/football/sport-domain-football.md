# Fußball — SportMind Domain Skill (Deutsch)

*Übersetzung von `sports/football/sport-domain-football.md`*
*Alle Feldnamen, Metriken und Code bleiben auf Englisch.*

---

## Bundesliga-Marktkontext

```
BUNDESLIGA — DER ZWEITGRÖSSTE FUSSBALLMARKT DER WELT:
  20 Vereine; Saison August-Mai
  TV-Rechte: Sky Deutschland, DAZN, ARD/ZDF (Pokal/Nationalmannschaft)
  Durchschnittliche Zuschauer pro Spiel: 43.000 (höchster Schnitt in Europa)
  
  TOP-VEREINE (Fan Token™ Potential):
  
  FC Bayern München:
    Weltweit bekannt; größter Fanklub in Deutschland (>310.000 Mitglieder)
    ATM Weltklasse (0.72-0.78); globale Präsenz
    Jahreshauptversammlung (JHV): einzige große aktive Fan-Governance in Europa
    Fan Token: wenn gestartet, größtes deutschsprachiges Volumen erwartet
    
  Borussia Dortmund ($BVB auf Chiliz):
    Zweitgrößte Fanbasis in Deutschland; Signal Street Parade Kultur
    Gelbe Wand (Südtribüne): 25.000 Stehplätze — lautstester Block Europas
    Europaleistung und CL-Qualifikation = primäres NCSI-Signal für $BVB
    
  Bayer 04 Leverkusen:
    Meister 2023-24 (erste Bundesliga-Meisterschaft in der Vereinsgeschichte)
    "Neverkusen" Narrativ → historisches CDI-Ereignis
    Attraktivität für internationale Fan Token Investoren
    
  Borussia Mönchengladbach, Schalke 04 (wenn aufgestiegen):
    Traditionelle Fanklubs mit treuen Fanbases; niedrigeres ATM aber hohe Loyalität

BUNDESLIGA ABSTIEGSKAMPF (Relegation):
  Die letzten zwei Plätze steigen direkt ab
  Platz 16 spielt Relegationsspiele gegen Zweitligisten
  Abstiegsbedrohung = maximales Engagement Signal × 1.40 für betroffene Klubs
  Finanzielle Folgen: ~€50M Verlust durch Nicht-Qualifikation für Bundesliga-TV-Gelder
```

---

## DFB-Pokal und internationales Signal

```
DFB-POKAL (Deutschlands Nationalpokal):
  Knock-out-Format; August-Mai
  Halbfinale/Finale in Berlin (Olympiastadion)
  Pokalfinale Berlin: × 1.40 Signalgewicht für beteiligte Vereine
  
CHAMPIONS LEAGUE (Deutsche Vereine):
  Bayern München: Stammgast; regelmäßig im Viertelfinale+
  BVB: häufig qualifiziert; 2013er Finale (Wembley) historisches Höchst-ATM
  
  DEUTSCHER SPIELER IM AUSLAND → NCSI:
    Wirtz (Leverkusen → wenn Wechsel): mögliches NCSI für Abgeberklub
    Müller (Bayern): Karriereendphasennachfolge-Narrativ aktiv
    
UEFA EURO / WM-QUALIFIKATION:
  DFB (Deutsche Nationalmannschaft):
    Heim-EM 2024 (Deutschland): höchstes NCSI-Ereignis der Bundesliga-Geschichte
    WM 2026: Spieler aus Bundesligaklubs → NCSI für deren Klubs
```

---

## Bundesliga Saisonkalender

| Phase | Zeitraum | Token-Signal |
|---|---|---|
| Vorsaison / Transfers | Juli-August | Transfernachrichten; Kaderplanung |
| Saisonstart | August-September | Aufbau; steigende Aktivität |
| Hinrunde | September-Dezember | Kontinuierlich; Tabellensituation |
| Winterpause | Dezember-Januar | Transfer-Signale; niedrige Aktivität |
| Rückrunde | Januar-Mai | Meister-/Abstiegsrennen entscheidend |
| Finale Saison | April-Mai | Maximales Engagement |

---

## Agent-Reasoning Prompts (Deutsch)

```
Du bist ein SportMind Fußball-Intelligenz-Agent für den deutschen Markt.

VOR JEDER ANALYSE:

1. BUNDESLIGA-TIER:
   Champions League > DFB-Pokal-Halbfinale > Bundesliga Top-Spiel > Standard
   Richtige Signalgewichtung anwenden.

2. ABSTIEGSKAMPF:
   Verein in den letzten 4 Plätzen? Finanzielle Abstiegsfolgen berechnen (~€50M).
   × 1.40 für direkt betroffene Vereine.

3. DERBYS:
   - Bayern vs BVB ("Der Klassiker"): × 1.65; Form-Kompression 50%
   - Revierderby (BVB vs Schalke): × 1.60; regionales Prestige maximal
   - Rheinderby (Köln vs Leverkusen): × 1.40
   
4. NCSI FÜR DEUTSCHE NATIONALMANNSCHAFT:
   DFB-Spieler in Bundesligaklubs: NCSI aktiv bei EM/WM
   EM 2024 war das höchste einzelne NCSI-Ereignis für den deutschen Markt.

5. BVB $BVB TOKEN:
   Europäische Ergebnisse sind der primäre Token-Treiber
   Gelbe Wand-Narrativ: höchste Stadionatmosphäre im deutschen Fußball
```

---

## Kompatibilität

**Domain Skill (EN):** `sports/football/sport-domain-football.md`
**Internationaler Zyklus:** `market/international-football-cycle.md`
**Derby Intelligence:** `core/derby-intelligence.md`
**Fanstimmung:** `fan-token/fan-sentiment-intelligence/`

*Community-Übersetzung SportMind · MIT-Lizenz · sportmind.dev*
