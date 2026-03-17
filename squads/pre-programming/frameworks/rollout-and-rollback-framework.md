# Rollout and Rollback Framework

## Título e Propósito

O **Rollout and Rollback Framework** é um sistema para planejar lançamentos graduais e reversões seguras antes de fazer deploy. O propósito é garantir que toda mudança em produção tenha um plano de "ida" controlada e um plano de "volta" testado — porque deploys são a causa mais comum de incidentes em produção.

## Quando Usar

- Antes de qualquer deploy significativo em produção
- Em mudanças que afetam muitos usuários ou dados críticos
- Ao introduzir novas integrações ou dependências
- Em migrações de dados ou schema
- Quando o blast radius da mudança é alto

## Conceitos-Chave

1. **Rollout Gradual**: Expor a mudança progressivamente a percentuais maiores de usuários/tráfego.
2. **Canary Release**: Expor a mudança a um pequeno percentual primeiro e monitorar antes de expandir.
3. **Rollback**: Reverter a mudança ao estado anterior. Deve ser rápido, seguro e testado.
4. **Ponto de Não-Retorno**: O momento após o qual rollback se torna extremamente caro ou impossível (ex: migração de dados destrutiva).
5. **Critério de Progresso**: Métricas que indicam que é seguro expandir o rollout. Sem elas, a expansão é cega.
6. **Critério de Rollback**: Condições que disparam rollback automático ou manual. Definidas antes do deploy.

## Processo / Passos

### Passo 1 — Classificar a Mudança
Avalie: complexidade, blast radius, reversibilidade, impacto em dados. Mudanças de alto impacto exigem plano detalhado.

### Passo 2 — Projetar o Rollout
Defina estágios: 1% → 5% → 25% → 50% → 100%. Para cada estágio, defina duração mínima de observação.

### Passo 3 — Definir Critérios de Progresso
Quais métricas precisam estar saudáveis para avançar ao próximo estágio? Taxa de erro, latência, métricas de negócio.

### Passo 4 — Definir Critérios de Rollback
Quais condições disparam rollback? Aumento de erros acima de X%, latência acima de Y ms, alertas de Z.

### Passo 5 — Projetar o Rollback
Como reverter? Feature flag, redeploy da versão anterior, reverter migração de dados? Teste o rollback antes do rollout.

### Passo 6 — Identificar Ponto de Não-Retorno
Há algum ponto após o qual rollback é impossível ou muito caro? Se sim, valide exaustivamente antes desse ponto.

### Passo 7 — Documentar e Comunicar
Compartilhe o plano com a equipe e stakeholders. Todos devem saber quem decide rollback e como executá-lo.

## Perguntas de Ativação

- "Se precisarmos reverter em 5 minutos, conseguimos?"
- "O que observamos para saber se a mudança está saudável?"
- "Há um ponto de não-retorno? Se sim, o que acontece antes dele?"
- "Quem tem autoridade para decidir rollback?"
- "Já testamos o rollback ou estamos assumindo que funciona?"
- "O rollout afeta dados de forma irreversível?"

## Output Esperado

```
MUDANÇA: [descrição]
CLASSIFICAÇÃO: [baixo/médio/alto impacto]

PLANO DE ROLLOUT:
- Estágio 1: 1% dos usuários → observar 2h → critérios: [métricas]
- Estágio 2: 10% → observar 4h → critérios: [métricas]
- Estágio 3: 50% → observar 24h → critérios: [métricas]
- Estágio 4: 100% → monitoramento contínuo

CRITÉRIOS DE ROLLBACK:
- Taxa de erro > 1% (baseline: 0.3%)
- Latência p99 > 500ms (baseline: 200ms)
- Qualquer alerta de perda de dados

PLANO DE ROLLBACK:
- Método: [feature flag / redeploy / reverter migração]
- Tempo estimado: [X minutos]
- Responsável: [pessoa/equipe]
- Testado: [sim/não — data do teste]

PONTO DE NÃO-RETORNO: [descrição ou "não há"]
```

## Armadilhas Comuns

1. **Rollback não testado**: Assumir que rollback "é só reverter" sem testar é receita para desastre.
2. **Rollout direto para 100%**: Pular estágios graduais para "ganhar tempo" maximiza blast radius.
3. **Critérios ausentes**: Sem critérios claros, a decisão de avançar ou reverter se torna política, não técnica.
4. **Migração de dados sem volta**: Mudanças de schema destrutivas eliminam a possibilidade de rollback.
5. **Ninguém monitorando**: Deploy na sexta à tarde sem ninguém observando métricas no fim de semana.
6. **Decisão de rollback lenta**: Burocracia para aprovar rollback enquanto o incidente escala.
