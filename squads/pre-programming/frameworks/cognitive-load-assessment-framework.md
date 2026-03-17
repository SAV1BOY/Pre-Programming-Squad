# Cognitive Load Assessment Framework

## Propósito
Avaliar e reduzir a carga cognitiva de decisões durante o pipeline de pré-programação. Baseado em Team Topologies (Skelton & Pais), Ousterhout (complexity management) e Sweller (cognitive load theory).

## Problema que Resolve
Times tomam decisões piores quando sobrecarregados cognitivamente. Quando 15 decisões arquiteturais competem por atenção ao mesmo tempo, nenhuma recebe análise adequada. Este framework sequencia e simplifica decisões para maximizar qualidade.

## Quando Usar
- Ao iniciar phase de architecture (muitas decisões simultâneas)
- Quando time reporta fadiga de decisão ou análise paralysis
- Em projetos G/XG com alta complexidade
- Quando há prazo apertado e risco de decisões apressadas

## Tipos de Carga Cognitiva

### Intrínseca (inerente ao problema)
- Complexidade do domínio de negócio
- Número de integrações e dependências
- Requisitos regulatórios
- **Não pode ser eliminada**, apenas gerenciada

### Extrínseca (causada por processos ruins)
- Documentação confusa ou ausente
- Ferramentas mal configuradas
- Reuniões sem agenda ou output claro
- Checklists genéricos que não se aplicam ao contexto
- **Deve ser eliminada** — é desperdício puro

### Germana (investimento em aprendizado)
- Entender novo domínio ou tecnologia
- Absorver learnings de projetos anteriores
- **Deve ser facilitada** — gera retorno futuro

## Processo

### Passo 1 — Inventariar Decisões Pendentes
Listar todas as decisões que o pipeline precisa tomar neste projeto.

Exemplo:
| # | Decisão | Tipo | Carga | Reversível? |
|---|---------|------|-------|-------------|
| 1 | Escolha de database | Arquitetura | Alta | Não |
| 2 | REST vs GraphQL | Interface | Média | Sim (parcialmente) |
| 3 | Monolito vs microservices | Arquitetura | Alta | Não |
| 4 | Provider de auth | Build vs Buy | Média | Sim |
| 5 | Estratégia de cache | Performance | Baixa | Sim |

### Passo 2 — Classificar por Carga e Reversibilidade
- **Alta + Irreversível:** Requer deep work session dedicada, mínimo 2 reviewers, ADR obrigatório
- **Alta + Reversível:** Timebox de 2h, decidir com 80% de certeza, registrar em ADR
- **Média:** Pode ser decidida em design review normal
- **Baixa:** Pode ser delegada ou decidida assincronamente

### Passo 3 — Sequenciar para Minimizar Carga Simultânea
Regras:
1. **Máximo 2 decisões de alta carga por dia**
2. **Decisões irreversíveis primeiro** (quando mente está fresca)
3. **Não misturar decisões de domínios diferentes** na mesma sessão
4. **Agrupar decisões relacionadas** (database + cache na mesma sessão)

### Passo 4 — Simplificar Decisões Complexas
Técnicas:
- **Decomposição:** Quebrar decisão grande em sub-decisões menores
- **Eliminação de opções:** Reduzir de 5 opções para 2-3 viáveis antes da análise profunda
- **Timeboxing:** Decisões reversíveis não merecem mais que 2h de análise
- **Reference class:** Consultar decisões similares em projetos anteriores

### Passo 5 — Documentar para Reduzir Re-decisão
Toda decisão documentada em ADR elimina carga cognitiva futura. A próxima vez que alguém perguntar "por que escolhemos X?", a resposta está documentada.

## Indicadores de Sobrecarga
- Time pede "mais tempo para pensar" repetidamente sem output
- Reuniões de decisão terminam sem decisão
- Mesma decisão é rediscutida em múltiplas sessões
- Qualidade de decisões cai no final do dia/semana
- Aumento de decisões "por default" sem análise

## Armadilhas
- **Subestimar context-switching:** Alternar entre 3 projetos diferentes no mesmo dia é carga extrínseca pura
- **Tratar todas as decisões como igualmente pesadas:** Decisões reversíveis de baixo impacto não merecem deep analysis
- **Não considerar experiência do time:** Carga intrínseca é menor para times experientes no domínio
- **Análise paralysis como sintoma:** Se o time não decide, a carga pode estar alta demais — simplificar antes de pressionar
