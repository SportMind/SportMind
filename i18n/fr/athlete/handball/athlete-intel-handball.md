# Handball — Intelligence Athlète (Français)

*Traduction de `athlete/handball/athlete-intel-handball.md`*
*Tous les noms de champs, métriques et code en anglais.*

---

## Vue d'ensemble (Overview)

L'intelligence athlète au niveau du handball produit un `athlete_modifier`
(0.55–1.25×) qui ajuste le score de signal de base.

**Variable la plus prédictive : Taux d'arrêt du gardien de but (GK save rate)**

Le gardien de but est la variable individuelle la plus décisive en handball —
plus que dans tout autre sport de l'équipe dans la bibliothèque SportMind.
Un gardien avec un taux d'arrêt > 35% peut renverser un déséquilibre de niveau
entre deux équipes.

---

## Système de modificateur — Gardien de but (GK Modifier)

| Taux d'arrêt (derniers 5 matchs) | Label | Modificateur |
|---|---|---|
| > 40% | ELITE — peut renverser le match | ×1.20 |
| 35–40% | TRÈS BON | ×1.10 |
| 30–35% | MOYEN (moyenne Starligue/EHF) | ×1.00 |
| < 30% | FAIBLE | ×0.88 |
| Gardien remplaçant (titulaire blessé) | DÉGRADATION | ×0.80 |

**Règle de dérogation (Override Rule) :**
Un gardien avec un taux d'arrêt > 40% sur les 5 derniers matchs **supplante**
l'avantage d'équipe calculé. Même face à Barcelona ou PSG Handball, une
performance de gardien d'élite redéfinit les probabilités.

---

## Système de modificateur — Joueur clé (Key Player Modifier)

| Poste | Statut | Modificateur |
|---|---|---|
| Gardien titulaire confirmé, forme ELITE | CONFIRMÉ+ | ×1.20 |
| Pivot (ligne d'attaque) | CONFIRMÉ | ×1.05 |
| Ailier gauche/droit (spécialiste fast break) | CONFIRMÉ | ×1.04 |
| Demi-centre (organisation du jeu) | CONFIRMÉ | ×1.06 |
| Gardien ABSENT (titulaire) | ABSENT | ×0.78 |
| Pivot principal ABSENT | ABSENT | ×0.85 |
| Ailier principal ABSENT | ABSENT | ×0.88 |

---

## Contexte PSG Handball — modificateurs spécifiques

```
POUR LES AGENTS ANALYSANT PSG HANDBALL ET LE TOKEN $PSG :

Gardien de but PSG (variable la plus critique) :
  Le gardien PSG en forme d'élite = signal positif non seulement pour PSG
  mais aussi potentiellement pour le token $PSG Football (effet de halo de marque)
  
  Règle signal croisé (EHF Final4 uniquement) :
    PSG Handball GK save rate > 38% au Final4 → signal $PSG Football +2–3%
    PSG Handball victoire Champions League → signal $PSG Football +5%
    
Pivot PSG :
  La ligne de pivot PSG détermine la cadence offensive
  Modifier pivot confirmé + gardien élite = ×1.25 composite (combinaison maximale)
  
Fast break spécialistes PSG :
  PSG investit massivement dans des ailiers rapides
  Fast break conversion rate > 75% = forte probabilité de victoire finale
```

---

## Intégration avec HandTIS (Integration Example)

```
# Workflow pré-match handball (Français) — EHF Champions League

# Étape 1 : Contexte de compétition
Charger fan-token/handball-token-intelligence/handball-token-intelligence.md
→ HandTIS tier : EHF Final4 = 1.00

# Étape 2 : Taux d'arrêt du gardien
get_athlete_signal_modifier token=[PSG_HB]
→ GK save rate : 38% (4 derniers matchs)
→ athlete_modifier : ×1.10 (Très bon)

# Étape 3 : Analyse du pivot et des ailiers
→ Pivot confirmé : ×1.05
→ Ailier gauche confirmé : ×1.04

# Étape 4 : Modificateur composite
composite_modifier = 1.10 × 1.05 × 1.04 = 1.20

# Étape 5 : Signal token $PSG (si EHF Final4)
→ PSG Handball en Final4 → signal $PSG Football : +3%

# Sortie (Output) :
adjusted_score = base_score × 1.20
flags : ["narrative_active"] si PSG en finale
```

---

## Compatibilité (Compatibility)

**Skill original (anglais) :** `athlete/handball/athlete-intel-handball.md`
**Bridge token :** `fan-token/handball-token-intelligence/`
**Domaine français :** `i18n/fr/sports/handball/sport-domain-handball.md`
**Signal croisé :** `fan-token/football-token-intelligence/` (PSG brand halo)

*[Starter de traduction — à compléter par un contributeur francophone natif.]*

*Traduction SportMind · Licence MIT · sportmind.dev*
