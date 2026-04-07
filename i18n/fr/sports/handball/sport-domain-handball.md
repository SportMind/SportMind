# Handball — SportMind Domain Skill (Français)

*Traduction de `sports/handball/sport-domain-handball.md`*
*Traduction de l'original anglais. Tous les noms de champs, métriques et code en anglais.*

Couche d'intelligence spécifique au handball pour les marchés de prédiction.
La France est l'une des nations de handball les plus compétitives au monde —
ce starter inclut un contexte de marché français spécifique.

---

## Modèle de Domaine (Domain Model)

### Pourquoi le handball en français ?

```
CONTEXTE MARCHÉ FRANÇAIS :
  La France est championne du monde 2021 (hommes) et multiple médaillée olympique
  Starligue (D1 masculine) : compétition la plus suivie en dehors de Bundesliga
  PSG Handball : club le plus valorisé commercialement en France
  Montpellier HB, Paris Saint-Germain, Nantes : clubs européens de premier plan
  
PSG HANDBALL — SIGNAL SPÉCIAL :
  PSG Handball partage l'infrastructure commerciale avec le PSG Football
  Potentiel de cross-promotion via le token $PSG (Socios) — surveiller les annonces
  Budget PSG Handball : parmi les plus élevés d'Europe avec Paris
  
ÉQUIPE DE FRANCE (LES EXPERTS) :
  Signal fort lors de chaque tournoi international (Championnat du Monde, Jeux Olympiques)
  Les victoires de l'équipe de France génèrent un pic d'engagement national
  Calendrier clé : Championnat du Monde (Janvier–Février), JO (Juillet–Août)
```

### Hiérarchie des événements (Event Hierarchy)

```
TIER 1 — Finale EHF Champions League, Finale Championnat du Monde
TIER 2 — Final4 EHF Budapest, Demi-finale Championnat du Monde
TIER 3 — Phase de groupes Starligue (matchs PSG)
TIER 4 — Matchs de Starligue standard
```

---

## Variable clé : Le gardien de but (Key Variable: Goalkeeper)

```
RÈGLE CRITIQUE EN HANDBALL :
  Un gardien avec un taux d'arrêt > 35% peut renverser un déséquilibre de niveau.
  
  Taux d'arrêt référence (Starligue) :
    > 40% : Elite — modifier ×1.20
    35–40% : Très bon — modifier ×1.10  
    30–35% : Correct — modifier ×1.00
    < 30% : Faible — modifier ×0.88
    
  RÈGLE AGENT : Toujours vérifier le statut du gardien titulaire avant
  d'évaluer un match. Un gardien remplaçant = signal réduit significativement.
```

---

## Prompts de Raisonnement Agent (Agent Reasoning Prompts)

```
Vous êtes un agent d'intelligence handball. Avant d'évaluer tout match :

1. VÉRIFIER LE GARDIEN — taux d'arrêt sur les 5 derniers matchs.
   C'est la variable la plus prédictive en handball.

2. CONTEXTE EHF — s'agit-il d'un match EHF Champions League ?
   Appliquer le tier EHF correspondant (Phase de groupes vs Final4 Budapest).

3. PSG HANDBALL — pour les signaux liés à PSG :
   Vérifier les annonces cross-promotion avec le token $PSG Football.
   L'infrastructure commerciale PSG peut amplifier les signaux de token.

4. ÉQUIPE DE FRANCE — pendant les tournois internationaux :
   Signal national fort. Résultats des Experts = pic d'engagement français.
   
5. NIVEAU DE LA COMPÉTITION — Starligue vs EHF vs Championnat du Monde.
   Calibrer le multiplicateur de signal selon la hiérarchie des événements.
```

---

## Compatibilité (Compatibility)

**Skill de domaine :** `sports/handball/sport-domain-handball.md` (original en anglais)
**Intelligence d'athlète :** `athlete/handball/athlete-intel-handball.md`
**Marché :** `market/market-handball.md`

*[Ce fichier est un starter de traduction. La version complète doit être traduite
par un contributeur francophone natif avec une expertise en handball.]*

---

*Traduction de la communauté SportMind · Licence MIT · sportmind.dev*
