# Críquete — SportMind Domain Skill (Português)

*Tradução de `sports/cricket/sport-domain-cricket.md`*
*Todos os nomes de campo, métricas e código permanecem em inglês.*

---

## A Regra do Formato Primeiro

```
REGRA FUNDAMENTAL: IDENTIFICAR O FORMATO ANTES DE QUALQUER ANÁLISE.

T20 (Twenty20):
  Duração: ~3 horas | Impacto Token: MÁXIMO | Volatilidade: ALTA
  Aplicar: modificadores de fase específicos do T20
  
ODI (Um Dia Internacional):
  Duração: ~7 horas | Copa do Mundo ODI = nível máximo
  Aplicar: modelo de ancoragem + aceleração
  
Test (Cinco Dias):
  Duração: até 5 dias | Impacto Token: BAIXO-MÉDIO | Arco narrativo: LONGO
  
REGRA DO AGENTE: identificar o formato na primeira linha de qualquer análise.
```

---

## Mercado da língua portuguesa e críquete

```
PORTUGAL — CONTEXTO DE CRÍQUETE:
  Portugal tem comunidades de críquete crescentes (diáspora asiática)
  Jogadores de críquete portugueses participam em divisões mais baixas da ICC
  Potencial de mercado: diáspora indiana em Portugal (~20.000 pessoas)
  
  Para fãs portugueses que seguem a seleção indiana:
    Índia vs Paquistão: multiplicador × 2.00 (não tem exceções)
    Copa do Mundo T20: nível máximo de engajamento
    IPL: seguido por fãs da diáspora indiana em Portugal

BRASIL — MERCADO EMERGENTE DE CRÍQUETE:
  Brasil tem uma liga nacional de críquete em desenvolvimento
  Comunidades: indianos, paquistaneses, ingleses no Brasil
  
  Oportunidade de token: quando o Brasil desenvolver uma equipa competitiva da ICC,
  haverá uma base de seguidores potencial de 200M+ pessoas no maior país lusófono

ANGOLA / MOÇAMBIQUE:
  Mercados emergentes com interesse crescente em críquete
  Conexões históricas com a África do Sul (país vizinho com forte tradição de críquete)
  
PORTUGAL / BRASIL NO CONTEXTO GLOBAL DO CRÍQUETE:
  O principal ponto de contacto para falantes de português com o críquete é
  através das diásporas do Sul Asiático residentes em Portugal e no Brasil
  O IPL e os torneios internacionais com Índia e Paquistão têm a maior audiência
```

---

## Calendário ICC (contexto em português)

```
COPA DO MUNDO T20 (anos ímpares):
  Evento de maior impacto para tokens de críquete
  Se Índia vs Paquistão acontecer: maior audiência global de críquete
  
COPA DO MUNDO ODI (a cada 4 anos):
  Próxima: 2027 (África do Sul / Zimbábue / Namíbia)
  Copa do Mundo na África do Sul = contexto lusófono mais forte
  (Moçambique / Angola como mercados adjacentes)
  
IPL (Março-Maio):
  Campeonato mais assistido na TV por falantes de português na diáspora
  Tokens PSL (Liga Super do Paquistão) ativos no Chiliz
  Fator PSL para comunidades paquistanesas em Portugal: muito elevado

SÉRIE ÍNDIA-PAQUISTÃO:
  Qualquer jogo entre Índia e Paquistão é um evento de nível 1
  Audiência: 400-500 milhões de espectadores
  Multiplicador: × 2.00 sem exceções
  Duração comercial CDI: 3-5 dias (muito superior à média)
```

---

## Fator de orvalho (Dew Factor) em português

```
O FATOR DE ORVALHO É CRÍTICO EM PARTIDAS NOTURNAS T20 NA ÁSIA DO SUL:

Em estádios como Wankhede (Mumbai), Eden Gardens (Calcutá), Gaddafi (Lahore):
  Orvalho pesado durante partidas noturnas → a bola fica escorregadia
  Equipa a rebater em segundo lugar (perseguindo) tem vantagem significativa
  
  Quando o risco de orvalho for ALTO ou MUITO ALTO:
    Aplicar modificador de orvalho à equipa que rebate em segundo lugar
    Adicionar flag: dew_risk_active
    Nota: "Orvalho esperado — vantagem para a equipa que persegue +10-12%"
    
  Monitorização: verificar previsão meteorológica em T-4h para partidas noturnas
  
  DLS (Duckworth-Lewis-Stern) também pode ser ativado por chuva:
    Interrupção por chuva → alvo DLS recalculado
    Partidas mais curtas = maior variância → reduzir confiança × 0.88
```

---

## Prompts de raciocínio do agente

```
És um agente de inteligência de críquete SportMind para os mercados de língua portuguesa.

ANTES DE QUALQUER ANÁLISE:

1. FORMATO PRIMEIRO — T20, ODI ou Test?
   Nunca aplicar modificadores de T20 a uma partida de Test.

2. ÍNDIA ESTÁ A JOGAR?
   Jogo com a Índia: aplicar × 1.40
   Índia vs Paquistão: × 2.00 sem exceção

3. FATOR DE ORVALHO?
   Partida noturna em campo sul-asiático?
   Humidade > 70% + temperatura > 20°C: verificar risco de orvalho
   
4. TOKEN PSL ATIVO?
   Liga Super do Paquistão tem tokens ativos no Chiliz ($LAH, etc.)
   Final PSL: NCSI 0.60; Fase de grupos: 0.20-0.35
   
5. DLS / INTERRUPÇÃO POR CHUVA?
   Probabilidade de chuva > 40%: adicionar nota DLS
   Reduzir confiança da análise × 0.88 se interrupção provável

6. DIÁSPORA E MERCADO:
   Fãs portugueses: principalmente interessados nos torneios da Índia e Paquistão
   Brasil/PALOP: mercado emergente; acompanham IPL pela diáspora indiana
```

---

## Compatibilidade

**Habilidade de domínio (EN):** `sports/cricket/sport-domain-cricket.md`
**Ciclo internacional:** `market/international-cricket-cycle.md`
**Factor de orvalho:** `core/core-weather-match-day.md`
**Inteligência do atleta:** `athlete/cricket/athlete-intel-cricket.md`
**Sentimento dos fãs:** `fan-token/fan-sentiment-intelligence/`

*Tradução comunitária SportMind · Licença MIT · sportmind.dev*
