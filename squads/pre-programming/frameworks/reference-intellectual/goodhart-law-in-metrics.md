# Goodhart: Quando Métrica Vira Meta

## Título e Propósito

Framework baseado na **Lei de Goodhart**: "Quando uma medida se torna uma meta, ela deixa de ser uma boa medida." O propósito é ajudar equipes de software a projetar métricas e incentivos que realmente medem o que importa — evitando que métricas se tornem alvos de otimização que distorcem comportamento.

## Quando Usar

- Ao definir métricas de sucesso para projetos, equipes ou produtos
- Quando comportamentos perversos surgem em resposta a métricas (gaming)
- Na avaliação de KPIs e OKRs de engenharia
- Quando métricas estão "ótimas" mas o resultado real não melhora
- Ao definir SLOs e critérios de qualidade

## Conceitos-Chave

1. **Lei de Goodhart**: Quando a métrica vira meta, pessoas otimizam a métrica, não o resultado que ela deveria representar.
2. **Gaming**: Comportamento que melhora a métrica sem melhorar o resultado real. Exemplo: inflar story points para "aumentar velocity".
3. **Proxy Metrics**: Métricas que são proxies imperfeitos do que realmente queremos medir. Cobertura de código é proxy de qualidade de testes — mas não é a mesma coisa.
4. **Métricas de Vaidade**: Números que parecem bons mas não indicam valor real. Exemplo: "deployamos 50 vezes por mês" sem medir se os deploys entregaram valor.
5. **Contra-métrica**: Métrica complementar que impede gaming. Se a meta é "resolver tickets rápido", a contra-métrica é "taxa de reabertura".

## Processo / Passos

### Passo 1 — Definir o Resultado Desejado
Antes de escolher métricas, defina: "Qual resultado real queremos ver?" Exemplo: "usuários satisfeitos" é o resultado; "NPS" é a métrica proxy.

### Passo 2 — Escolher Métricas Proxy
Selecione métricas que se correlacionam com o resultado desejado. Nenhuma será perfeita — reconheça as limitações.

### Passo 3 — Adicionar Contra-métricas
Para cada métrica principal, defina uma contra-métrica que detecta gaming:
- Velocity alta → contra-métrica: taxa de bugs pós-deploy
- Tempo de resolução baixo → contra-métrica: taxa de reabertura
- Cobertura de código alta → contra-métrica: taxa de testes que nunca falharam

### Passo 4 — Comunicar como Indicador, não Meta
Apresente métricas como "indicadores de saúde" que informam decisões, não como "metas" que determinam avaliações.

### Passo 5 — Revisitar Periodicamente
As métricas ainda estão correlacionadas com o resultado desejado? Surgiram comportamentos de gaming?

## Perguntas de Ativação

- "Se otimizarmos apenas essa métrica, o resultado real melhora?"
- "Como alguém poderia melhorar essa métrica sem melhorar o resultado?"
- "Qual é a contra-métrica que detectaria gaming?"
- "Estamos medindo o que é fácil medir ou o que realmente importa?"
- "Se essa métrica estiver ótima mas o produto estiver ruim, notaríamos?"

## Output Esperado

Métricas definidas com: resultado desejado, proxy escolhido, limitações reconhecidas, contra-métricas, plano de revisão.

## Armadilhas Comuns

1. **Métrica como meta**: Dizer "nossa meta é 90% de cobertura" incentiva testes triviais que atingem cobertura sem verificar comportamento.
2. **Sem contra-métrica**: Toda métrica unidimensional pode ser gamed. Contra-métricas criam equilíbrio.
3. **Métricas de vaidade**: "Temos 1000 testes!" — mas quantos detectam bugs reais? Quantidade sem qualidade é vaidade.
4. **Punição pela métrica**: Se a métrica é usada para punir, as pessoas manipulam. Se é usada para informar, as pessoas colaboram.
5. **Métrica estática**: O que funcionava como indicador em 2022 pode não funcionar em 2025. Revise.
