# Calcio — SportMind Skill di Dominio (Italiano)

> ⚠️ **AVVISO DI DEPRECAZIONE — Traduzione della Comunità**
> Questo file potrebbe contenere valori dei modificatori e framework
> di una versione precedente della libreria SportMind (pre-v4.1.87).
> Per i valori dei modificatori aggiornati, i pesi dei segnali e i
> framework di ragionamento, fare sempre riferimento ai file sorgente
> in inglese. Le traduzioni della comunità sono benvenute — vedi
> [CONTRIBUTING.md](../../../../CONTRIBUTING.md).
> **Versione corrente:** v4.1.87

---

*Traduzione di `sports/football/sport-domain-football.md`*
*Tutti i nomi di campo, le metriche e il codice rimangono in inglese.*

---

## Serie A Market Context

```
SERIE A — LA LEGA ITALIANA D'ÉLITE:
  20 club; stagione Agosto-Maggio
  Lega più seguita in Italia · cinque club tra i più titolati d'Europa

  FAN TOKEN CHILIZ CONFERMATI (7 token):
  $ACM · $INTER · $ITA · $JUV · $NAP · $ASR · $BFC
  Catene: Chiliz Chain · Solana · Base (omnichian)

  $INTER (FC Internazionale Milano):
    Campioni di Serie A 2025-26
    CDI Gate: CONSOLIDATION
    UCL 2026-27: confermato
    Token di riferimento primario per il mercato italiano
    Caricare inter.md prima di ogni analisi $INTER

  $ACM (AC Milan):
    CDI Gate: TRANSITION
    Europa League 2026-27: confermato
    Finire 2025-26: verificare posizione finale di Serie A
    Caricare acm.md prima di ogni analisi $ACM

  $JUV (Juventus FC):
    CDI Gate: TRANSITION
    Europa League 2026-27: confermato (6° posto Serie A)
    Storica fanbase globale · narrativa di ripresa in corso
    Caricare juv.md prima di ogni analisi $JUV

  $NAP (SSC Napoli):
    CDI Gate: TRANSITION
    UCL 2026-27: confermato
    Forte identità regionale · Napoli città come segnale
    Caricare nap.md prima di ogni analisi $NAP

  $ASR (AS Roma):
    Profilo e tier di competizione corrente: verificare prima di applicare
    Derby della Capitale: fixture a TOKEN SINGOLO ($ASR solo — vedi Derby)
    Caricare file di intelligenza di mercato aggiornato prima dell'analisi

  $BFC (Bologna FC 1909):
    Profilo e tier di competizione corrente: verificare prima di applicare
    Club storico · prima qualificazione UCL recente
    Caricare file di intelligenza di mercato aggiornato prima dell'analisi

  $ITA (FIGC — Squadra Nazionale Italiana):
    Italia NON qualificata a WC2026 — zero burn PTG a WC2026
    Ciclo di qualificazione EURO 2028 ora attivo (HP-10)
    Eleggibilità PTG per EURO 2028: NON RISOLTA
    Non applicare modificatori WC2026 a $ITA — Italia non ha partecipato

CONTESTO REGOLATORIO ITALIANO:
  CGT: 33% aliquota sostitutiva piatta (Legge 199/2025, dal 1° gennaio 2026)
    Applicata a tutte le plusvalenze crypto realizzate dai residenti italiani.
    Nessuna soglia — ogni euro di guadagno è imponibile.
    Metodo di calcolo del costo: LIFO (Last In, First Out).
    L'Italia è la giurisdizione a più alta attrito per i detentori nel
    SportMind — 33% CGT vs Germania 0% dopo 12 mesi.
    
  DAC8: attivo dal 2026
    D.Lgs. 194/2025 traspone la Direttiva UE 2023/2226.
    Scambio automatico di dati per tutti i detentori italiani
    su piattaforme autorizzate MiCA.
    Primo anno di rendicontazione: 2026.
    Prima scadenza: 30 giugno 2027.
    Piena visibilità delle transazioni per le autorità fiscali.
    
  Trattamento fiscale burn PTG: NON RISOLTO
    Non assumere realizzazione né non-realizzazione fiscale.
    Escalare a Strategia & Brainstorm su qualsiasi segnale Tier 1.
    Contesto completo: macro/regulatory/italy.md

  MiCA: pienamente operativo · piattaforme UE autorizzate attive
```

---

## Coppa Italia e Segnali Internazionali

```
COPPA ITALIA:
  Formato ad eliminazione diretta · Agosto-Maggio
  Finale: Stadio Olimpico di Roma · venue neutro
  Peso segnale finali: × 1.40
  La vittoria in Coppa Italia contribuisce al CDI del club

UEFA CHAMPIONS LEAGUE:
  $INTER (Inter Milan): confermato UCL 2026-27
    UCL è la finestra di segnale a più alto profilo per $INTER
    UCL Final occasion weight: × 2.00
    UCL turno di qualificazione/playoff: × 1.60
    UCL fase a gironi/lega: × 1.20

  $NAP (SSC Napoli): confermato UCL 2026-27
    UCL partecipazione = trigger di rivalutazione CDI
    Applicare pesi UCL come sopra

UEFA EUROPA LEAGUE:
  $ACM (AC Milan): confermato Europa League 2026-27
  $JUV (Juventus): confermato Europa League 2026-27
  Occasion weight Europa League: × 1.30
  Vittoria Europa League = CDI positivo significativo

$ITA — SQUADRA NAZIONALE ITALIANA:
  WC2026: NON QUALIFICATA — zero burn PTG a WC2026
  Questa è una standing fact della libreria — non contraddire mai.
  Ciclo di qualificazione EURO 2028: ora attivo (HP-10)
  Eleggibilità PTG burn EURO 2028: NON RISOLTA
  Nessun modificatore burn PTG applicabile finché EURO 2028
    non è confermato e il trattamento fiscale non è risolto.
  Escalare a Strategia & Brainstorm su qualsiasi segnale Tier 1 $ITA.

FINESTRA DI MERCATO:
  Chiusura: 31 agosto
  Finestra invernale: Gennaio-Febbraio
  Trasferimenti ad alto profilo = trigger di rivalutazione CDI
  Monitorare i cambiamenti nell'archetipo della rosa
```

---

## Derby Context

```
DERBY DELLA MADONNINA ($INTER vs $ACM):
  Peso segnale: × 1.80
  Derby della città di Milano · fixture DUAL-TOKEN confermato
  Entrambi i token su Chiliz Chain · amplificazione dual-token applicabile
  Sconto di familiarità × 0.5 si applica (narrativa H2H ampiamente nota)
  Caricare core/h2h-framework.md per le regole di amplificazione dual-token
  
  SAN SIRO — STADIO CONDIVISO:
    $INTER e $ACM condividono San Siro come stadio principale
    Tipo venue: CONDIVISO — modificatore × 0.5 obbligatorio
    Nessun club detiene il pieno vantaggio territoriale
    Caricare core/venue-intelligence-framework.md prima di applicare
      il modificatore home advantage per qualsiasi fixture San Siro
    
DERBY DELLA CAPITALE ($ASR vs Lazio):
  Solo AS Roma ha il token Chiliz
  Lazio NON ha token Chiliz confermato al 2026-08-02
  Fixture a TOKEN SINGOLO ($ASR soltanto) finché Lazio non confermato
  Non applicare amplificazione dual-token — regola token singolo attiva
  Se token Lazio confermato: escalare a Strategia & Brainstorm urgentemente
  
DERBY D'ITALIA ($INTER vs $JUV):
  Peso segnale: × 1.65
  Fixture DUAL-TOKEN confermato · rivalità di prestigio nazionale
  Applicare regole dual-token standard (h2h-framework.md)
  Sconto di familiarità: verificare — narrativa nota ma meno satura
    rispetto al Derby della Madonnina
    
$NAP vs $INTER / $NAP vs $JUV:
  Fixture dual-token · Napoli in trasferta porta forti segnali
  di identità regionale
  Rivalità nord-sud marcata nel contesto culturale italiano
  Applicare regole dual-token standard con contesto narrativo regionale
  
$BFC DERBY:
  Verificare il contesto di rivalità corrente prima di applicare
  il peso del segnale derbi
  Bologna ha rivalità storiche — verificare rilevanza attuale
```

---

## Serie A Stagione — Calendario

| Fase della stagione | Date | Segnale token |
|---|---|---|
| Pre-stagione / Mercato | Luglio-Agosto | Notizie di mercato; monitorare chiusura finestra (31 agosto) |
| Inizio stagione | Agosto-Settembre | Aumento attività; primi segnali di classifica |
| Prima metà | Settembre-Dicembre | Segnale continuo; si sovrappone alla fase a gironi UCL/EL |
| Pausa invernale / Mercato | Dicembre-Gennaio | Attenzione a finestra trasferimenti; bassa attività |
| Seconda metà | Gennaio-Maggio | Corsa scudetto e salvezza; finestra di segnale critica |
| Turni UCL / EL knockout | Febbraio-Maggio | Massima intensità segnale per $INTER, $NAP, $ACM, $JUV |
| Finale di stagione | Aprile-Maggio | Massimo engagement · decisioni scudetto, salvezza, coppe |

---

## Agent Reasoning Prompts (Italiano)

```
Sei un Agente di Intelligenza Calcistica SportMind per il mercato italiano.

PRIMA DI OGNI ANALISI:

1. GERARCHIA DELLE COMPETIZIONI DI SERIE A:
   UCL > Finale Coppa Italia > Derby della Madonnina / Derby d'Italia >
   Europa League > Partita di vertice Serie A > Partita standard Serie A
   Applicare il peso del segnale corretto.

2. SETTE TOKEN ITALIANI — CARICARE IL CDI APPROPRIATO:
   Prima di qualsiasi analisi, caricare il file CDI del club specifico:
   $INTER → inter.md · $ACM → acm.md · $JUV → juv.md · $NAP → nap.md
   $ASR → file intelligenza di mercato aggiornato
   $BFC → file intelligenza di mercato aggiornato
   $ITA → nessun CDI club · contesto nazionale separato
   Non produrre segnali senza CDI gate confermato.

3. CGT 33% — GIURISDIZIONE AD ALTO ATTRITO:
   L'Italia è la giurisdizione a più alta attrito nel SportMind.
   33% CGT (Legge 199/2025) · nessuna soglia · metodo LIFO.
   Applicare modificatore di attrito fiscale ad ogni analisi
   coinvolgente detentori italiani residenti.
   Caricare macro/regulatory/italy.md per contesto completo.

4. CONFORMITÀ DAC8:
   I detentori italiani hanno piena visibilità delle transazioni
   per le autorità fiscali dal 2026.
   DAC8 aumenta la consapevolezza della conformità fiscale —
   considerare nell'analisi del comportamento dei detentori.
   Non assumere che l'evasione fiscale sia possibile su
   piattaforme MiCA-autorizzate.

5. BURN PTG — NON RISOLTO:
   Il trattamento fiscale dei burn PTG in Italia è NON RISOLTO.
   Non assumere realizzazione né non-realizzazione fiscale.
   Non applicare modificatori burn PTG senza risoluzione confermata.
   Escalare qualsiasi segnale Tier 1 su PTG a Strategia & Brainstorm.

6. $ITA — ZERO BURN WC2026:
   L'Italia NON si è qualificata a WC2026.
   Zero burn PTG a WC2026 per $ITA — standing fact della libreria.
   Non contraddire mai questa fact in nessun output.
   Ciclo qualificazione EURO 2028 attivo (HP-10).
   Eleggibilità PTG EURO 2028: NON RISOLTA — escalare su segnale Tier 1.

7. DERBY DELLA MADONNINA — DUAL-TOKEN · STADIO CONDIVISO:
   Fixture dual-token confermato: $INTER vs $ACM.
   Sconto familiarità × 0.5 (narrativa H2H ampiamente nota).
   San Siro = stadio condiviso: modificatore home advantage × 0.5 obbligatorio.
   Caricare ENTRAMBI: core/h2h-framework.md + core/venue-intelligence-framework.md
   prima di produrre qualsiasi output per Derby della Madonnina.

8. DERBY DELLA CAPITALE — TOKEN SINGOLO:
   Lazio NON ha token Chiliz confermato al 2026-08-02.
   $ASR vs Lazio = fixture a TOKEN SINGOLO ($ASR soltanto).
   Non applicare amplificazione dual-token — regola token singolo attiva.
   Se token Lazio confermato: escalare a Strategia & Brainstorm urgentemente.

9. DERBY D'ITALIA — DUAL-TOKEN:
   $INTER vs $JUV = fixture dual-token confermato · × 1.65.
   Applicare regole dual-token standard via h2h-framework.md.

10. $ASR E $BFC — VERIFICARE SEMPRE:
    Verificare CDI gate e tier di competizione prima di ogni analisi.
    Non assumere status di qualificazione europea — verificare fonti primarie.
    Caricare file di intelligenza di mercato aggiornato prima dell'output.
```

---

## Compatibilità

**Domain Skill (EN):** `sports/football/sport-domain-football.md`
**Contesto regolatorio italiano:** `macro/regulatory/italy.md`
**Framework H2H:** `core/h2h-framework.md`
**Intelligenza venue:** `core/venue-intelligence-framework.md`
**File CDI:** `market/club-intelligence/acm.md` · `market/club-intelligence/inter.md` · `market/club-intelligence/juv.md` · `market/club-intelligence/nap.md`
**Registro fan token:** `fan-token/registry/complete-registry.md`

*Traduzione della comunità · SportMind · Licenza MIT · sportmind.dev*

© 2026 SportMind
