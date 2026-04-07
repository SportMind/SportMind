# Football — SportMind Domain Skill (Français)

*Traduction de `sports/football/sport-domain-football.md`*
*Traduction de l'original anglais. Tous les noms de champs, métriques et code en anglais.*

Couche d'intelligence spécifique au football pour les marchés de prédiction et fan tokens.

---

## Modèle de Domaine (Domain Model)

### Calendrier de la Saison (Season Calendar)

| Phase | Dates | Comportement du Token |
|---|---|---|
| Pré-saison | Juillet–Août | Faible liquidité ; signaux de transferts |
| Début de saison | Août–Septembre | Activation ; volume croissant |
| Mercato hivernal | Janvier | Signaux de transferts pendant 2 semaines |
| Fin de saison | Mars–Mai | Signal maximal ; lutte pour les titres |
| Intersaison | Juin–Juillet | Activité minimale on-chain |

### Hiérarchie des Événements (Event Hierarchy)

```
TIER 1 — Finale de la Ligue des Champions, Classique PSG-OM, Coupe du Monde
TIER 2 — Phase à élimination directe de la Ligue des Champions, journée décisive Ligue 1
TIER 3 — Match de Ligue 1 standard avec implication européenne
TIER 4 — Coupes domestiques, pré-saison
```

---

## Contexte Ligue 1 — Structure Commerciale

```
LIGUE 1 — PROFIL COMMERCIAL (2024-2026):

Format:
  18 clubs depuis 2023-2024 (passage de 20 à 18 — consolidation commerciale)
  Saison: Août–Mai
  Champions League: 2 places directes + 1 via barrages
  Europa League: 2 places
  Conference League: 1 place

Diffusion:
  DAZN: droits audiovisuels principaux (Ligue 1 Uber Eats)
  beIN Sports: marchés internationaux — Moyen-Orient, Afrique du Nord
  Canal+: historiquement dominant; accord en cours
  
  CONTEXTE CRITIQUE: La Ligue 1 a traversé une crise des droits TV (2022-2023).
  Tout nouveau contrat de diffusion est un signal commercial positif pour l'ensemble
  de l'écosystème des tokens du championnat.

Clubs avec tokens Socios actifs (ou potentiel élevé):
  Paris Saint-Germain ($PSG): token de référence — voir section dédiée ci-dessous
  Olympique de Marseille: grande popularité, fort potentiel token
  Olympique Lyonnais: histoire européenne, base de fans internationale
  AS Monaco: actionnaire stable (Prince Albert); marché international riche
  LOSC Lille: récent champion (2021); fan base régionale engagée
  
SIGNAL DE RELÉGATION:
  Clubs en zone de relégation: signal token négatif systématique
  Relégation confirmée: signal LTUI fortement impacté — voir fan-token/fan-token-lifecycle/
  Montée en Ligue 1: signal positif pour clubs de Ligue 2 avec potentiel token
```

---

## PSG ($PSG) — Analyse Approfondie du Token

```
PSG FAN TOKEN — LE TOKEN DE RÉFÉRENCE FRANCAIS:

Propriété QSI (Qatar Sports Investments):
  Qatar Sports Investments = bras sportif de QIA (Qatar Investment Authority)
  Implications géopolitiques: surveillance des relations diplomatiques France-Qatar
  Implication UEFA: contrôle du fair-play financier; impact sur les investissements
  
  Load macro/macro-geopolitical.md pour les événements Qatar/France

Drivers du Signal $PSG (par ordre d'importance):
  1. Résultats Ligue des Champions (>>Ligue 1)
     UCL Finale: signal maximum pour $PSG
     UCL Élimination: signal négatif fort même si PSG domine en Ligue 1
     
  2. Mercato — Signings et Départs
     Arrivée d'une star mondiale: ×1.4-1.6 signal immédiat
     Départ d'une icône: signal négatif fort (ex: départ Mbappé 2024: -15-20%)
     Prolongation de contrat: signal positif modéré ×1.15
     
  3. Performances Ligue 1
     Titre de champion: signal positif mais déjà anticipé (souvent "buy the rumor")
     Élimination en Coupe de France: signal négatif léger
     
  4. PSG Handball (effet halo):
     PSG Handball à la Final4 EHF Budapest: +3% signal $PSG (halo de marque QSI)
     PSG Handball champion d'Europe: +5% signal $PSG (halo renforcé)
     Note: Signal faible mais systématique. Voir fan-token/handball-token-intelligence/

ATM (Athlete Token Multiplier) pour PSG:
  ATM du successeur de Mbappé: 0.85-0.95 (star de génération)
  ATM des milieux de terrain: 0.55-0.70
  ATM des défenseurs: 0.40-0.55
  
  Formule NCSI pour PSG:
    NCSI_$PSG = performance_UCL × ATM_joueur × macro_modifier
    Maximum théorique: tournoi UCL complet avec star ATM 0.90+ = +25-40%
```

---

## Équipe de France — Signal NCSI (Spillover National-Club)

```
LES BLEUS — LE MULTIPLICATEUR NCSI LE PLUS FORT EN LIGUE 1:

Joueurs de l'Équipe de France dans les clubs avec tokens:
  Chaque but ou performance remarquable = spillover sur le token du club

NCSI Calcul:
  NCSI_club = résultat_EdF × ATM_joueur × compétition_weight
  
  NCSI élevé pour les clubs français:
    Joueurs PSG en sélection: NCSI fort sur $PSG
    Joueurs OM en sélection: NCSI sur token OM (si actif)
    
Événements déclencheurs NCSI:
  Euro (tous les 4 ans, années paires):
    2024: Allemagne — France éliminée en QF
    2028: Pays-Bas/Allemagne
    
  Coupe du Monde (tous les 4 ans, années paires):
    2026: USA/Canada/Mexique — France forte candidate
    Impact estimé si France gagnante: +30-50% signal tokens clubs français
    
  Ligue des Nations UEFA:
    Signal plus faible (Tier 3) mais régulier (tous les 2 ans)

SUIVI DES CONVOCATIONS:
  Chaque liste de convocation = signal pour les tokens des clubs représentés
  Joueur blessé et non convoqué = signal négatif pour le token de son club
  Retour de blessure + convocation = signal positif double
```

---

## Derbies et Classiques Français

```
MATCHES À FORT SIGNAL EN FRANCE:

Le Classique — PSG vs OM:
  Multiplicateur: ×1.8 (plus élevé en Ligue 1)
  Engagement holders: pic systématique à J-48h
  Réduction du différentiel de forme: 40%
  Format: 2 fois par saison (Ligue 1) + possiblement Coupe de France
  
  HISTOGRAMME SIGNAL $PSG × Classique:
    PSG gagne à domicile: +4-8% (attendu — faible surprise)
    PSG gagne à l'extérieur: +6-10% (décisif en déplacement)
    Égalité: signal neutre à léger négatif
    PSG perd: -8-15% (fort signal négatif, remise en question)

OL vs OM — Choc des Olympiques:
  Multiplicateur: ×1.4
  Rivalité historique: Lyon-Marseille = antagonisme Nord-Sud
  
Derbies régionaux avec signal token:
  LOSC vs RC Lens: Derby du Nord — ×1.3 si les deux clubs ont tokens actifs
  OGC Nice vs AS Monaco: Derby de la Côte d'Azur — ×1.2

RÈGLE CLASSIQUE:
  Réduire de 40% le différentiel de forme pour tout derby.
  L'effet "match spécial" comprime la prévisibilité basée sur la forme.
```

---

## Contexte Réglementaire France

```
CADRE JURIDIQUE FRANÇAIS POUR LES TOKENS:

ANJ (Autorité Nationale des Jeux):
  Régule les marchés de prédiction en France
  Distincte du cadre fan tokens (tokens ≠ paris sportifs légalement)
  Pour les applications de prédiction: consulter un conseiller juridique français
  
AMF (Autorité des Marchés Financiers):
  Framework PSAN (Prestataire de Services sur Actifs Numériques) en vigueur
  Fan tokens: classificés comme crypto-actifs — enregistrement PSAN potentiellement requis
  MiCA (EU): s'applique depuis 2024 — harmonisation européenne en cours
  
DROITS TV ET TOKENS:
  La relation entre les droits audiovisuels LFP et les tokens est distincte.
  Les clubs peuvent émettre des tokens sans impact sur leurs droits TV.
  Mais: les clauses de partenariat Socios/Chiliz méritent d'être vérifiées
  pour compatibilité avec les obligations de diffusion.
  
NOTE: Ces informations ne constituent pas un conseil juridique.
Pour des déploiements commerciaux en France, consultez un avocat spécialisé.
```

---

## Système de Signal (Signal Weights)

| Composante | Pondération | Justification |
|---|---|---|
| Résultat sportif | 30% | L'événement lui-même |
| Flux marché / baleines | 25% | Positionnement institutionnel |
| Sentiment social | 20% | Narratif PSG/OM fort |
| Tendance de prix | 15% | Momentum entre matchs |
| Macro CHZ/BTC | 10% | Cycle crypto global |

*Référence: `core/core-signal-weights-by-sport.md`*

---

## Prompts de Raisonnement Agent

```
Vous êtes un agent d'intelligence footballistique SportMind pour le marché français.

AVANT TOUT MATCH:

1. TIER DU MATCH — UCL Finale vs Ligue 1 standard?
   Multiplicateur signal: ×3.0 (UCL Finale) → ×1.0 (Ligue 1 standard)

2. PSG SPÉCIFIQUE — Pour les tokens $PSG:
   UCL >> Ligue 1. Les résultats européens priment sur le championnat.
   Vérifier: PSG Handball en compétition européenne? (halo +3-5%)

3. CLASSIQUE — PSG vs OM, OL vs OM?
   Réduire différentiel de forme de 40%. Appliquer multiplicateur derby.

4. NCSI ÉQUIPE DE FRANCE — Tournoi international en cours?
   Charger fan-token/football-token-intelligence/ pour calcul NCSI.
   Joueurs français avec tokens = signal amplifié.

5. MERCATO — Fenêtre de transferts ouverte (janvier, été)?
   Annonce de signing = signal immédiat.
   Départ d'icône = signal négatif fort.

6. MACRO — Cycle crypto CHZ/BTC actif?
   Charger macro/macro-crypto-market-cycles.md.
   Contexte géopolitique Qatar/France? → macro/macro-geopolitical.md

7. RÉGLEMENTAIRE — Application commerciale en France?
   Vérifier conformité ANJ (prédiction) et AMF/MiCA (tokens).
```

---

## Compatibilité (Compatibility)

**Skill de domaine:** `sports/football/sport-domain-football.md`
**Athlètes:** `athlete/football/athlete-intel-football.md`
**Token bridge:** `fan-token/football-token-intelligence/`
**Handball PSG halo:** `fan-token/handball-token-intelligence/`
**Marché:** `market/market-football.md`
**Macro géopolitique:** `macro/macro-geopolitical.md`

*Traduction communauté SportMind · Licence MIT · sportmind.dev*
