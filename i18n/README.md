# SportMind — Multi-language Support

SportMind skills are available in English (primary) and community-translated
languages. Translated skills allow agents to reason in the user's language
while maintaining the same intelligence quality as the English originals.

---

## Available languages

| Language | Code | Status | Skills available |
|---|---|---|---|
| English | `en` | Primary | All skills (211+ files) |
| Spanish | `es` | Beta | football, mma, cricket, handball |
| Portuguese | `pt` | Beta | football, mma, cricket |
| French | `fr` | Beta | football (Ligue 1/PSG context), handball (EHF French clubs), athlete/handball |
| Arabic | `ar` | Beta | football (Saudi Pro League, MENA context), handball (PSG/QSI context) |
| Hindi | `hi` | Beta | cricket (IPL/India context), kabaddi (PKL context), mma (UFC India) |

---

## How to use translated skills

```python
# Load the translated skill instead of the English version
import os

lang = "es"  # or "pt", "fr", etc.
sport = "football"

# Try translated version first; fall back to English
skill_path = f"i18n/{lang}/sports/{sport}/sport-domain-{sport}.md"
if not os.path.exists(skill_path):
    skill_path = f"sports/{sport}/sport-domain-{sport}.md"

with open(skill_path) as f:
    skill_content = f.read()
```

---

## Contributing a translation

1. Pick an English skill file from `sports/`, `athlete/`, or `fan-token/`
2. Create the equivalent path under `i18n/{lang}/`
3. Translate the content — keep all structured elements (tables, code blocks,
   JSON, field names) in English; translate prose and explanations
4. Submit PR with label: `translation`, `lang-{code}`
5. A language reviewer will validate within 14 days

**Important:** Translated skills must preserve:
- All field names, metric names, and code examples in English
- All numerical values exactly (modifier ranges, thresholds)
- All skill file structure and section headings (translated but same structure)
- The MIT License footer

*See community/leaderboard.md — translations earn +8 leaderboard points per skill.*
