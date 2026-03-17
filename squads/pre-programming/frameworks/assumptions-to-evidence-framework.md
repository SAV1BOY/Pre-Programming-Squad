# Assumptions-to-Evidence Framework

## Título e Propósito

O **Assumptions-to-Evidence Framework** é um sistema para identificar, catalogar e converter suposições em evidências verificáveis antes de comprometer recursos em implementação. O propósito é reduzir o risco de construir sobre fundações falsas — cada suposição não validada é uma bomba-relógio no projeto.

## Quando Usar

- Antes de iniciar qualquer projeto ou feature significativa
- Quando estimativas são baseadas em "achismos" ou experiência passada em contextos diferentes
- Quando há alto grau de incerteza técnica ou de negócio
- Em revisões de pré-planejamento para identificar riscos ocultos
- Quando decisões arquiteturais dependem de premissas não comprovadas

## Conceitos-Chave

1. **Suposição**: Algo que a equipe trata como verdade sem ter verificado. Pode ser técnica, de negócio, de comportamento do usuário ou organizacional.
2. **Risco da Suposição**: O impacto se a suposição estiver errada. Suposições de alto risco precisam ser validadas primeiro.
3. **Evidência**: Dados concretos, testes, protótipos ou confirmações que transformam uma suposição em fato conhecido.
4. **Custo de Validação**: O esforço necessário para transformar a suposição em evidência. Nem toda suposição vale o custo de validação.
5. **Decisão Dependente**: A decisão de projeto que muda se a suposição estiver errada. Suposições sem decisões dependentes são irrelevantes.

## Processo / Passos

### Passo 1 — Coleta de Suposições
Reúna a equipe e pergunte: "O que estamos assumindo como verdade sem ter verificado?" Cubra as categorias: técnicas, de negócio, de usuário, de infraestrutura, de integração e organizacionais.

### Passo 2 — Classificar por Risco
Para cada suposição, avalie: "Se isso estiver errado, qual é o impacto no projeto?" Classifique como **Crítico** (projeto falha), **Alto** (retrabalho significativo), **Médio** (ajustes necessários) ou **Baixo** (impacto mínimo).

### Passo 3 — Mapear Decisões Dependentes
Para cada suposição, identifique quais decisões do projeto dependem dela. Se nenhuma decisão depende, a suposição é irrelevante — remova.

### Passo 4 — Estimar Custo de Validação
Para cada suposição relevante, estime o esforço para validá-la: spike técnico, conversa com stakeholder, análise de dados, protótipo, etc.

### Passo 5 — Priorizar Validações
Use a fórmula: Prioridade = Risco × Número de Decisões Dependentes ÷ Custo de Validação. Valide primeiro as de maior prioridade.

### Passo 6 — Executar Validações
Para cada suposição priorizada, execute o método de validação definido e registre o resultado como **Confirmada**, **Refutada** ou **Parcial**.

### Passo 7 — Atualizar Decisões
Para suposições refutadas, revise as decisões dependentes. Para parciais, adicione condições ou planos de contingência.

## Perguntas de Ativação

- "O que acontece com nosso plano se essa suposição estiver errada?"
- "De onde veio essa 'certeza'? É dado, experiência ou intuição?"
- "Qual é o jeito mais rápido e barato de verificar isso?"
- "Quantas decisões do projeto mudam se isso não for verdade?"
- "Estamos assumindo que o comportamento atual do sistema/usuário vai se manter?"
- "Alguém já testou isso no nosso contexto específico?"

## Output Esperado

| Suposição | Categoria | Risco | Decisões Dependentes | Custo de Validação | Método de Validação | Status | Resultado |
|---|---|---|---|---|---|---|---|
| API do parceiro suporta 1000 req/s | Técnica | Crítico | Arquitetura de integração, sizing | 4h | Teste de carga contra sandbox | Validada | Suporta 800 req/s — ajustar design |
| Usuários preferem fluxo em etapas | Negócio | Alto | Design de UX, número de telas | 2 dias | Teste de usabilidade com 5 usuários | Pendente | — |
| Time de infra pode provisionar em 1 semana | Organizacional | Médio | Cronograma de deploy | 30min | Conversa com lead de infra | Confirmada | Confirmou 5 dias úteis |

## Armadilhas Comuns

1. **Não identificar suposições**: A equipe trata suposições como fatos óbvios e nem percebe que está assumindo algo.
2. **Validar tudo**: Tentar validar cada suposição gera paralisia. Foque nas de alto risco com decisões dependentes.
3. **Validação superficial**: "Perguntei para o Fulano e ele disse que sim" não é evidência robusta para suposições críticas.
4. **Não atualizar decisões**: Validar a suposição e descobrir que está errada, mas seguir com o plano original por inércia.
5. **Suposições tardias**: Descobrir suposições críticas apenas quando a implementação falha. O momento de mapear é antes de começar.
6. **Viés de confirmação na validação**: Desenhar testes que tendem a confirmar a suposição em vez de tentar refutá-la.
