# Artes Marciales Mixtas (MMA) — SportMind Domain Skill (Español)

*Traducción de `sports/mma/sport-domain-mma.md`*

Capa de inteligencia específica para MMA para tokens de atletas y mercados de predicción.
Los tokens de MMA son impulsados por atletas individuales, no por equipos.

---

## La semana de pelea (Fight Week) — la señal más importante

```
CRONOLOGÍA DE LA SEMANA DE PELEA:
  Lunes–Miércoles: Sesiones de entrenamiento abiertas → indicadores de forma
  Miércoles: Pesaje oficial → señal binaria CRÍTICA
  Jueves: Acto de presentación → indicadores psicológicos
  Viernes: Pesaje → confirmación final
  Sábado: Noche de combate
```

### La señal del pesaje (Weigh-in Signal)

| Resultado del pesaje | Impacto en señal del token |
|---|---|
| Hace el peso cómodamente | Confirmación positiva; mantener señal base |
| Hace el peso (≤0.5 lb de diferencia) | Neutral |
| Falla el pesaje → 1 hora para cortar | modifier: ×0.75 (señal negativa) |
| Falla el pesaje definitivamente | modifier: ×0.72 — señal altamente negativa |

*[Este es un archivo de inicio de traducción. El archivo inglés completo debe
ser traducido por un contribuyente nativo en español.]*

---

*Traducción de la comunidad SportMind · Licencia MIT · sportmind.dev*
