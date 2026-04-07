# MMA (Artes Marciais Mistas) — SportMind Domain Skill (Português)

*Tradução de `sports/mma/sport-domain-mma.md`*
*Todos os nomes de campos, métricas e código em inglês.*

Camada de inteligência específica para MMA para tokens de atletas e mercados de previsão.
Os tokens de MMA são impulsionados por atletas individuais — não por equipes.

---

## Contexto do Mercado Brasileiro (Brazilian Market Context)

```
ESPECIAL PARA O MERCADO BRASILEIRO:

Brasil no MMA mundial:
  Brasil é o segundo maior mercado global para UFC (atrás apenas dos EUA)
  Lutadores brasileiros: historicamente 25-30% do roster principal do UFC
  Ativos notáveis: Anderson Silva, José Aldo, Lyoto Machida (legado)
  Ativos atuais (2024+): Poatan (Alex Pereira), Pantoja, etc.

Alex Pereira ($POATAN — caso de estudo):
  Campeão de duas divisões UFC (Middleweight + Light Heavyweight)
  Campeão de kickboxing antes do MMA (história comercialmente única)
  Base de fãs: forte no Brasil + Turquia + EUA
  Sinal de token: maior multiplicador individual no MMA brasileiro

Sinal de briga (Fight Week Signal) para lutadores brasileiros:
  Pesagem no Brasil (Copa Podio, Jungle Fight): diferentes padrões
  UFC no Brasil (Rio, São Paulo): evento de sinal premium
  Lutador brasileiro no Brasil: home crowd effect — aplica modificador ×1.15
```

---

## A Semana de Luta (Fight Week)

```
CRONOGRAMA DA SEMANA DE LUTA:
  Segunda–Quarta: Treinos abertos → indicadores de forma
  Quarta: Pesagem oficial → sinal BINÁRIO CRÍTICO
  Quinta: Face-off / Open workouts → indicadores psicológicos
  Sexta: Pesagem → confirmação final
  Sábado: Noite da luta
```

### O Sinal da Pesagem (Weigh-in Signal)

| Resultado da pesagem | Impacto no signal |
|---|---|
| Faz o peso confortavelmente | Confirmação positiva |
| Faz o peso (≤0.5 lb de diferença) | Neutro |
| Falha na pesagem → 1 hora para cortar | modifier: ×0.75 |
| Falha definitivamente | modifier: ×0.72 — sinal negativo forte |
| Mudança de lutador (< 3 semanas) | Floor modifier: ×0.75 |

---

## Sistema de Sinal por Estilo (Style Matchup Signal)

```
PARA LUTADORES BRASILEIROS — contexto de estilo:
  Jiu-Jitsu brasileiro (BJJ): piso dominante = desvantagem se adversário tem
                               excelente TDD (Takedown Defense)
  Muay thai/Kickboxing: vantagem no striking de longa distância
  Wrestle-boxing (estilo americano): vantagem no controle do octógono
  
REGRA DO AGENTE: Sempre avaliar matchup de estilo antes de aplicar
  modificador de forma. Forma recente sem contexto de estilo = análise incompleta.
```

---

## Compatibilidade (Compatibility)

**Skill original (inglês):** `sports/mma/sport-domain-mma.md`
**Inteligência de atleta:** `athlete/mma/athlete-intel-mma.md`
**Bridge token:** `fan-token/mma-token-intelligence/`

*[Este é um arquivo inicial de tradução. A versão completa deve ser traduzida
por um contribuidor nativo em português.]*

*Tradução da comunidade SportMind · Licença MIT · sportmind.dev*
