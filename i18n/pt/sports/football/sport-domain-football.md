# Futebol — SportMind Domain Skill (Português)

*Tradução de `sports/football/sport-domain-football.md`*
*Todos os nomes de campo, métricas e código permanecem em inglês.*

---

## Mercados Prioritários (Portugal e Brasil)

```
PORTUGAL — CONTEXTO DO MERCADO:
  Primeira Liga: 18 clubes
  Big Three: Benfica, Porto, Sporting CP — dominam a liga
  Contexto Europeu: Portugal regularmente classifica 3-4 clubes para a UEFA
  
  TOKENS ATIVOS / POTENCIAL:
    Benfica, Porto, Sporting: maior potencial de token no mercado português
    Base de adeptos: leal e internacionalmente dispersa (diáspora portuguesa)
    Mercados-chave: Portugal, Brasil, Moçambique, Angola
    
  NCSI SELEÇÃO PORTUGUESA:
    Euro/Mundial: multiplicador NCSI elevado para clubes com jogadores portugueses
    Cristiano Ronaldo era: ATM máximo durante 2003-2024
    Pós-CR7: nova geração (Leão, Vitinha, Gonçalo Ramos) — ATM em desenvolvimento

BRASIL — O MAIOR MERCADO DE FUTEBOL DO MUNDO:

  BRASILEIRÃO (Série A):
    20 clubes; temporada de Abril a Dezembro (verão austral)
    Flamengo: maior base de adeptos do Brasil (40M+); maior potencial de token
    Outros grandes: Corinthians, Palmeiras, São Paulo, Santos
    
  ATM BRASILEIRO:
    Tier 1: Neymar (mesmo pós-peak), Vinícius Júnior, Rodrygo
    Tier 2: Estrelas do Brasileirão com perfil digital forte
    NCSI Brasil: Copa América e Copa do Mundo — multiplicador ×1.40 para jogadores brasileiros
    
  ADOÇÃO CRIPTO NO BRASIL:
    Alta — Brasil tem uma das maiores taxas de adoção cripto da América Latina
    Enquadramento regulatório: Banco Central do Brasil (BCB) regulando ativos digitais
    Token Oportunidade: mercado maduro; base de adeptos digital-nativa
    
  COPAS NACIONAIS:
    Copa do Brasil: alta imprevisibilidade (formato eliminatório)
    Copa Libertadores: competição sul-americana mais importante para tokens brasileiros
    
RIVALIDADES REGIONAIS PRIORITÁRIAS:
  Brasil: Fla-Flu (Flamengo vs Fluminense) — ×1.80 multiplicador derby
         Fla-Minas (Flamengo vs Atlético-MG) — ×1.65
         Clássico da Saudade (Corinthians vs Santos) — ×1.60
  Portugal: O Clássico (Benfica vs Porto) — ×1.75
```

---

## Calendário da Temporada (Futebol Português)

| Fase | Datas | Comportamento do Token |
|---|---|---|
| Pré-temporada | Julho-Agosto | Liquidez baixa; sinais de transferências |
| Início da época | Agosto-Setembro | Ativação; volume crescente |
| Mercado de inverno | Janeiro | Sinais de transferências durante 2 semanas |
| Fase decisiva | Março-Maio | Sinal máximo; luta pelo título |
| Entressafra | Junho-Julho | Atividade mínima on-chain |

---

## NCSI Portugal — Seleção Nacional

```
EURO 2024 / EURO 2028:
  Base de adeptos: Portugal tem uma das diásporas mais distribuídas do mundo
  Mercados: UK, França, Suíça, EUA, Brasil, PALOP
  
  Jogadores chave para NCSI por clube:
    Jogador do Benfica na Seleção: multiplicador NCSI para token Benfica
    Jogador do Porto na Seleção: multiplicador para token Porto
    
  Cálculo NCSI Portugal:
    NCSI_clube = resultado_seleção × ATM_jogador × competition_weight
    Euro QF+: competition_weight 0.80-0.95
    Euro Final: 1.00

COPA DO MUNDO 2026 (EUA/Canadá/México):
  Portugal classificado (esperado)
  Jogadores portugueses em clubes com tokens europeus = NCSI ativo
  Aplicar: market/international-football-cycle.md para pesos de competição
```

---

## Prompts de Raciocínio do Agente

```
És um agente de inteligência de futebol SportMind para os mercados português e brasileiro.

ANTES DE QUALQUER ANÁLISE:

1. TIER DO JOGO — UEFA Champions League vs Primeira Liga vs Brasileirão?
   Multiplicador de sinal: ×3.0 (Final UCL) → ×1.0 (jogo padrão de liga)

2. DERBY — Clássico portugues ou rivalidade brasileira?
   Benfica vs Porto: reduzir diferencial de forma 45%
   Fla-Flu ou Fla-Minas: aplicar multiplicador de derby correto
   Carregar core/derby-intelligence.md

3. NCSI SELEÇÃO — Torneio internacional em curso?
   Euro ou Copa do Mundo: calcular NCSI para jogadores portugueses/brasileiros
   Mercado: international-football-cycle.md

4. BRASIL ESPECÍFICO:
   Copa Libertadores ativa? Maior peso para clubes brasileiros/argentinos
   Brasileirão fase final (Outubro-Dezembro)? Máximo sinal doméstico

5. CONTEXTO CRIPTO:
   Brasil: mercado maduro; adoção cripto alta
   Portugal: médio; crescente alinhamento com UE/MiCA
   Aplicar macro/macro-crypto-market-cycles.md
```

---

## Compatibilidade

**Skill de domínio (EN):** `sports/football/sport-domain-football.md`
**Ciclo internacional:** `market/international-football-cycle.md`
**Derby intelligence:** `core/derby-intelligence.md`
**Copa Libertadores:** `market/international-football-cycle.md` — secção América do Sul

*Tradução comunitária SportMind · Licença MIT · sportmind.dev*
