# Cricket — SportMind Domain Skill (Español)

*Traducción de `sports/cricket/sport-domain-cricket.md`*
*Todos los nombres de campos, métricas y código en inglés.*

Capa de inteligencia específica del cricket para mercados de predicción.
El cricket está creciendo rápidamente en Latinoamérica, especialmente en:
Argentina, México, Chile y la comunidad de la diáspora india/paquistaní.

---

## Contexto del mercado latinoamericano (LATAM Cricket Context)

```
CRICKET EN LATINOAMÉRICA — estado actual:

Argentina:
  El país latinoamericano con mayor historia en cricket
  Miembro asociado del ICC (International Cricket Council)
  Liga nacional: Argentine Cricket Association
  
México:
  Liga emergente con fuerte comunidad de diáspora india/paquistaní
  México City T20 competition — crecimiento documentado
  
Diáspora India/Paquistaní en LATAM:
  Comunidades en Brasil, Argentina, México, Chile
  Alto interés en IPL, PSL, ICC events
  Fan token potential: esta comunidad tiene alta adopción de cripto
  
NOTA: Latinoamérica es mercado SECUNDARIO para cricket.
  Los signals principales vienen de India, Pakistan, Australia, Inglaterra.
  Para análisis de fan tokens de cricket, el contexto LATAM es relevante
  principalmente para: identificar token holders, comunidades de fans digitales.
```

---

## Regla del Formato Primero (Format-First Rule)

```
CRÍTICO — La regla más importante en cricket:

T20 (Twenty20):
  Duración: ~3 horas | Volatilidad: ALTA | Impacto token: MÁXIMO
  Dew factor: Importante en noches en Asia del Sur

ODI (One Day International):
  Duración: ~7 horas | Copa del Mundo ODI = Tier 1
  
Test:
  Duración: hasta 5 días | Volatilidad token: BAJA | Narrativa: sostenida

REGLA DEL AGENTE: Identificar el formato ANTES de cualquier análisis.
Aplicar el modelo de señal correcto para cada formato.
```

---

## India vs Pakistan — el multiplicador máximo

```
INDIA vs PAKISTAN:
  Multiplicador: ×2.00 — el más alto de toda la biblioteca
  Audiencia: 200M+ (el evento deportivo individual más visto globalmente)
  En torneos ICC: este partido SIEMPRE genera el pico de señal del torneo
  
  REGLA DEL AGENTE: Para India vs Pakistan, siempre aplicar ×2.00
  independientemente de cualquier otro contexto. No hay excepciones.
```

---

## Factor de Rocío (Dew Factor — T20 Nocturno)

```
CRÍTICO para T20 nocturnos en el subcontinente asiático:
  Rocío alto = ventaja para el equipo que batea segundo (+10-12%)
  
  Señal del saque (Toss Signal):
    Rocío alto previsto + ganó el saque + eligió FIELD = 
    señal positiva para el equipo que batea segundo
    
  Cargar: core/core-weather-match-day.md → sección cricket
```

---

## Compatibilidad (Compatibility)

**Skill dominio (inglés):** `sports/cricket/sport-domain-cricket.md`
**Inteligencia atleta:** `athlete/cricket/athlete-intel-cricket.md`
**Bridge token:** `fan-token/cricket-token-intelligence/`
**Mercado:** `market/market-cricket.md`

*[Este archivo es un starter de traducción. Debe ser completado por un
contribuyente nativo en español con conocimiento del cricket.]*

*Traducción de la comunidad SportMind · Licencia MIT · sportmind.dev*
