# Balonmano — SportMind Domain Skill (Español)

*Traducción de `sports/handball/sport-domain-handball.md`*
*Todos los nombres de campos, métricas y código en inglés.*

Capa de inteligencia específica del balonmano para mercados de predicción.
España es una de las naciones dominantes del balonmano mundial — con uno
de los circuitos comerciales más ricos de Europa.

---

## Contexto del mercado español (Spanish Market Context)

```
BALONMANO EN ESPAÑA:
  Liga ASOBAL: la Liga española de balonmano masculino, una de las más fuertes de Europa
  Selección española (Los Gladiadores): 2× Campeones del Mundo (2005, 2021)
  Clubes destacados:
    FC Barcelona Handbol: 13× Campeones de Europa — el club más laureado
    BM Atlético de Madrid: participación EHF Champions League
    Fraikin BM Granollers, BM Logroño: competición europea regular

FC BARCELONA HANDBOL — señal de token especial:
  FC Barcelona opera equipos de alta élite en fútbol Y balonmano
  El token $BAR (Socios/Chiliz) es principalmente de fútbol
  Pero: victorias del Barcelona en EHF Champions League amplían la marca FCB
  Este halo de marca puede generar una señal marginal positiva para $BAR
  durante la semana del EHF Final4 (junio, Budapest)

  REGLA DEL AGENTE: Los tokens del FC Barcelona (fútbol) pueden recibir
  un señal de halo de +2-3% si el Barcelona de balonmano gana la Champions.
  Más débil que el efecto PSG ($PSG) pero estructuralmente similar.
```

---

## Variable clave: el portero (Key Variable: Goalkeeper)

```
REGLA CRÍTICA — la más importante en balonmano:
  Un portero con tasa de paradas > 35% puede revertir una ventaja de equipo.

  Tasas de parada de referencia (Liga ASOBAL):
    > 40%: Élite — modifier ×1.20 (anula diferencial de nivel de equipo)
    35–40%: Muy bueno — modifier ×1.10
    30–35%: Correcto — modifier ×1.00
    < 30%: Por debajo del promedio — modifier ×0.88

  REGLA DEL AGENTE: Comprueba siempre la tasa de paradas del portero titular
  antes de evaluar cualquier partido. Un portero suplente = señal significativamente reducida.
```

---

## Jerarquía de eventos (Event Hierarchy)

```
TIER 1 — Final EHF Champions League (Final4 Budapest), Final del Mundo
TIER 2 — Semifinales Final4, Semifinales Mundial
TIER 3 — Cuartos EHF, Final Liga ASOBAL
TIER 4 — Partidos regulares ASOBAL / EHF
```

---

## Diferencial financiero estructural (Financial Tier Gap)

```
FC Barcelona Handbol está en una liga aparte:
  Presupuesto estimado: 3-4× el de la mayoría de clubes de la ASOBAL
  Plantilla de nivel Champions con permanencia institucional
  
  REGLA: Barcelona vs cualquier otro club ASOBAL en campo neutral → ×1.12
  Barcelona vs otro Tier 1 europeo (Kiel, PSG): ×1.00 (se cancela la ventaja financiera)
```

---

## Prompts de razonamiento del agente (Agent Reasoning Prompts)

```
Eres un agente de inteligencia del balonmano. Antes de evaluar cualquier partido:

1. PORTERO PRIMERO — ¿Tasa de paradas en los últimos 5 partidos?
   La variable más decisiva en balonmano.

2. CONTEXTO EHF — ¿Es partido de la EHF Champions League?
   Aplica el tier de competición correcto (Final4 > cuartos > grupos).

3. SEÑAL BARCELONA — ¿Juega el FC Barcelona Handbol durante la Final4?
   Carga fan-token/football-token-intelligence/ para el halo de marca $BAR.

4. MUNDIAL — ¿Es año impar (enero/febrero)?
   Los Gladiadores (España) = señal nacional elevada durante torneos internacionales.

5. DIFERENCIAL FINANCIERO — ¿Es Tier 1 vs Tier 2?
   Aplica ×1.12 para el favorito de Tier 1 en campo neutral.
```

---

## Compatibilidad (Compatibility)

**Skill dominio (inglés):** `sports/handball/sport-domain-handball.md`
**Inteligencia atleta:** `athlete/handball/athlete-intel-handball.md`
**Bridge token:** `fan-token/handball-token-intelligence/`
**Mercado:** `market/market-handball.md`

*[Archivo inicial de traducción — completar por un contribuyente hispanohablante nativo.]*

*Traducción comunidad SportMind · Licencia MIT · sportmind.dev*
