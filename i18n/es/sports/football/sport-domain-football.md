# Fútbol — SportMind Domain Skill (Español)

*Traducción de `sports/football/sport-domain-football.md`*
*Todos los nombres de campo, métricas y código permanecen en inglés.*

---

## Mercados prioritarios (España y Latinoamérica)

```
ESPAÑA — CONTEXTO DEL MERCADO:
  LaLiga EA Sports: 20 clubes
  Los Tres Grandes: Real Madrid, FC Barcelona, Atlético de Madrid
  Presencia europea: España clasifica 3-4 clubes a UEFA regularmente
  
  TOKENS ACTIVOS ($BAR, $RM, $ATM):
    Base de aficionados: apasionada e internacionalmente distribuida
    Mercados clave: España, México, Argentina, Colombia, Chile, Perú
    Audiencia total hispanohablante: 500M+ potenciales seguidores
    
  EL CLÁSICO (Real Madrid vs FC Barcelona):
    El partido de clubes más visto del mundo
    Multiplicador de señal: × 1.75 (derby de máximo nivel)
    Compresión de forma: 50% aplicada — el resultado es genuinamente incierto
    Impacto en tokens: los dos tokens más activos reaccionan simultáneamente
    Duración comercial CDI: 8-10 días (contienda narrativa global)
    
  EL DERBI MADRILEÑO (Real Madrid vs Atlético):
    Derby local de alta intensidad
    Multiplicador de señal: × 1.50
    Contexto: La Liga + posibles eliminatorias UEFA
    
  SEVILLA DERBY (Sevilla vs Real Betis):
    Derby histórico del sur de España
    Multiplicador: × 1.45

LATINOAMÉRICA — EL MERCADO MÁS GRANDE DEL MUNDO EN ESPAÑOL:

  ARGENTINA:
    Superclásico (River Plate vs Boca Juniors): × 1.85 — derby más intenso del mundo
    Copa Libertadores: competición más importante para tokens sudamericanos
    Adopción cripto: MUY ALTA — la inestabilidad del peso impulsa la adopción
    Oportunidad de token: River Plate, Boca Juniors = mayor potencial en Sudamérica
    
  MÉXICO:
    Liga MX: liga más vista de las Américas (incluye EE.UU.)
    Clásico Nacional (América vs Guadalajara): × 1.65
    Mercado digital: TikTok + YouTube = audiencia digital nativa masiva
    Copa del Mundo 2026: México co-anfitrión → catalizador máximo para tokens mexicanos
    
  COLOMBIA / CHILE / PERÚ:
    Mercados emergentes con alta penetración digital
    Seguimiento de LaLiga y Liga MX desde estas regiones
    Potencial de token: clubs locales tienen bases de aficionados leales
```

---

## Copa del Mundo 2026 — Señal máxima para el mundo hispanohablante

```
COPA DEL MUNDO 2026 (EE.UU./Canadá/México):

Equipos hispanohablantes clasificados típicamente:
  España, México, Argentina, Colombia, Ecuador, Uruguay, Paraguay,
  Chile (clasificación pendiente), Perú, Bolivia

IMPACTO EN TOKENS:
  Jugador de LaLiga en la selección nacional:
    Multiplicador NCSI activo durante toda la competición
    Ejemplo: jugador de $BAR en España → NCSI(BAR) activo × 0.55-1.00 por fase
    
  Co-anfitrión México:
    NCSI máximo para tokens mexicanos durante el torneo
    Partidos en casa en estadios aztecas: aficionados sin desplazamiento
    × 1.20 multiplicador adicional para selección mexicana en sus partidos
    
  Argentina (campeona vigente, 2022):
    Narrativa de defensa del título activa
    ATM de Messi (si participa): máximo histórico
    
  El partido Spain vs Argentina (si se da):
    Sería el partido más visto de la Copa del Mundo 2026
    Todos los tokens hispanohablantes activos simultáneamente
```

---

## Calendario de temporada (LaLiga)

| Fase | Fechas | Comportamiento del token |
|---|---|---|
| Pretemporada | Julio-Agosto | Señales de fichajes; baja actividad |
| Inicio temporada | Agosto-Septiembre | Activación; volumen creciente |
| Mercado de invierno | Enero | Señales de transferencias 2 semanas |
| Fase decisiva | Marzo-Mayo | Señal máxima; carrera por el título |
| Final de temporada | Mayo-Junio | Resolución; inicio entresafra |

---

## NCSI — Cálculo para equipos españoles y latinoamericanos

```
FÓRMULA NCSI PARA LaLiga:
  NCSI_club = resultado_selección × ATM_jugador × peso_competición

  Peso por fase:
    Final Copa del Mundo:  1.00
    Semifinal:             0.90
    Cuartos:               0.75
    Octavos/Fase grupos:   0.40-0.55

JUGADORES CLAVE PARA NCSI (ejemplos por token):
  $BAR: jugadores de la selección española en el FC Barcelona
  $RM:  jugadores de las selecciones española, francesa, brasileña, etc.
  $ATM: jugadores de selecciones española, francesa, portuguesa, etc.
  
  Regla: cuantos más jugadores internacionales tenga un club,
  mayor es la amplitud del NCSI durante torneos internacionales.
```

---

## Prompts de razonamiento del agente

```
Eres un agente de inteligencia de fútbol SportMind para los mercados
hispanohablantes (España y Latinoamérica).

ANTES DE CUALQUIER ANÁLISIS:

1. TIER DEL PARTIDO:
   Champions League Final > El Clásico > LaLiga decisivo > partido estándar
   Aplicar multiplicador de señal correcto

2. DERBY ACTIVO:
   ¿Es El Clásico, Derbi Madrileño o Superclásico argentino?
   Reducir diferencial de forma en 50%
   Cargar core/derby-intelligence.md

3. COPA DEL MUNDO / EUROCOPA:
   ¿Hay torneo internacional activo?
   Calcular NCSI para jugadores de selecciones hispanohablantes
   market/international-football-cycle.md

4. ARGENTINA ESPECÍFICO:
   Superclásico: multiplicador × 1.85
   Copa Libertadores en fase KO: señal máxima para clubs argentinos
   
5. CONTEXTO CRIPTO:
   Argentina: adopción muy alta → base de holders digital-nativa fuerte
   España/México: media-alta → crecimiento sostenido
   Aplicar macro/macro-crypto-market-cycles.md

6. COPA DEL MUNDO 2026:
   México co-anfitrión: × 1.20 adicional para tokens mexicanos
   España/Argentina: narrativa activa durante toda la competición
```

---

## Compatibilidad

**Habilidad de dominio (EN):** `sports/football/sport-domain-football.md`
**Ciclo internacional:** `market/international-football-cycle.md`
**Derby intelligence:** `core/derby-intelligence.md`
**Copa del Mundo 2026:** `market/world-cup-2026.md`
**Sentimiento de fans:** `fan-token/fan-sentiment-intelligence/`

*Traducción comunitaria SportMind · Licencia MIT · sportmind.dev*
