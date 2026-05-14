# Football — Intelligence Athlète (Français)

> ⚠️ **DEPRECATION NOTICE — Community Translation**
> This file may contain modifier values and frameworks from an earlier version
> of the SportMind library (pre-v3.97.x). For current modifier values, signal
> weights, and reasoning frameworks, always reference the English source files.
> Community translations are welcome — see [CONTRIBUTING.md](../../CONTRIBUTING.md).
> **Current version:** v3.97.46

---


*Traduction de `athlete/football/athlete-intel-football.md`*
*Tous les noms de champs, métriques et code en anglais.*

---

## Vue d'ensemble (Overview)

L'intelligence athlète au niveau du football produit un `athlete_modifier`
(0.55–1.25×) qui ajuste le score de signal de base.

**Variable la plus prédictive :** Disponibilité du joueur clé + forme récente (xG)

---

## Système de modificateur (Modifier System)

### Disponibilité (Availability)

| Statut | Modificateur |
|---|---|
| CONFIRMÉ (joueur clé, forme HOT) | ×1.15 |
| CONFIRMÉ (joueur clé, forme MOYENNE) | ×1.00 |
| PROBABLE | ×1.05 |
| DOUTE | ×0.85 |
| ABSENT (joueur clé) | ×0.70 |
| SUSPENDU | ×0.72 |

### Forme récente (Form — 5 derniers matchs)

| Score de forme | Label | Modificateur |
|---|---|---|
| 85–100 | DOMINANTE | ×1.20 |
| 70–84 | HOT | ×1.10 |
| 55–69 | BONNE | ×1.04 |
| 40–54 | MOYENNE | ×1.00 |
| 25–39 | MAUVAISE | ×0.92 |
| 0–24 | FROIDE | ×0.82 |

---

## Contexte PSG — modificateur spécifique

```
POUR LES AGENTS TRAVAILLANT SUR LES TOKENS PSG :

Gardien de but PSG :
  Le gardien est la variable la plus impactante pour les tokens de clubs de football.
  GK titulaire confirmé (Donnarumma) : modificateur standard
  GK remplaçant : ×0.80 (impact significatif sur la cote et le signal token)
  
Joueurs clés PSG pour le modificateur athlète :
  Attaquants (Mbappé-ère → successeurs) : load ATM metric depuis
    fan-token/football-token-intelligence/ pour l'impact individual→token
  Milieux créateurs : impact modéré sur signal token PSG
  
Règle NCSI (National-Club Spillover) :
  Joueurs convoqués en équipe nationale = signal PSG token amplifié
  Résultats équipe de France → token $PSG : voir NCSI dans football-token-intelligence
```

---

## Intégration (Integration Example)

```
# Workflow pré-match football (Français)

# Étape 1 : Contexte domaine
Charger sports/football/sport-domain-football.md

# Étape 2 : Vérifier disponibilité
get_availability token=[PSG] → confirmer lineup 2h avant le match

# Étape 3 : Évaluer forme
get_form_score token=[PSG] → xG sur 5 derniers matchs

# Étape 4 : Modificateur composite
get_athlete_signal_modifier token=[PSG]

# Décision :
# adjusted_score >= 68 + no flags → ENTER
# lineup_unconfirmed = true → ATTENDRE confirmation
```

---

## Compatibilité (Compatibility)

**Skill original (anglais) :** `athlete/football/athlete-intel-football.md`
**Bridge token :** `fan-token/football-token-intelligence/`
**Domaine :** `i18n/fr/sports/football/sport-domain-football.md`

*[Starter de traduction — à compléter par un contributeur francophone natif.]*

*Traduction SportMind · Licence MIT · sportmind.dev*
