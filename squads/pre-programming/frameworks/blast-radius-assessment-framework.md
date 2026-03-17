# Blast Radius Assessment Framework

## Título e Propósito

O **Blast Radius Assessment Framework** é um sistema para avaliar e minimizar o impacto potencial de falhas, mudanças ou incidentes no sistema. O propósito é responder à pergunta "se isso der errado, o que mais quebra?" — permitindo que a equipe projete contenção antes que a explosão aconteça.

## Quando Usar

- Antes de qualquer mudança significativa em produção
- No design de novos componentes que interagem com sistemas existentes
- Na avaliação de risco de deploys e migrações
- Ao projetar estratégias de rollback
- Quando um componente tem muitos dependentes

## Conceitos-Chave

1. **Blast Radius**: O alcance do impacto quando algo falha — quantos usuários, serviços, funcionalidades ou dados são afetados.
2. **Contenção**: Mecanismos que limitam o blast radius — feature flags, canary releases, circuit breakers, isolamento de dados.
3. **Dependência Direta**: Componentes que consomem diretamente o componente em questão.
4. **Dependência Transitiva**: Componentes que dependem indiretamente, via cadeia de dependências.
5. **Zona de Impacto**: Agrupamento de componentes e funcionalidades afetados por uma falha específica.

## Processo / Passos

### Passo 1 — Identificar o Componente ou Mudança
Defina exatamente o que está sendo avaliado: deploy de novo código, mudança de schema, migração de infraestrutura, etc.

### Passo 2 — Mapear Dependentes Diretos
Liste todos os componentes, serviços e funcionalidades que dependem diretamente deste componente.

### Passo 3 — Mapear Dependentes Transitivos
Para cada dependente direto, mapeie quem depende dele. Continue até cobrir toda a cadeia.

### Passo 4 — Quantificar Impacto
Para cada dependente, estime: número de usuários afetados, funcionalidades degradadas, impacto financeiro, impacto reputacional.

### Passo 5 — Classificar o Blast Radius
- **Contido**: Afeta apenas o componente em questão
- **Local**: Afeta componentes adjacentes
- **Regional**: Afeta uma área funcional inteira
- **Global**: Afeta todo o sistema ou todos os usuários

### Passo 6 — Projetar Contenção
Para blast radius Regional ou Global, projete mecanismos de contenção: feature flags, deploys graduais, circuit breakers, isolamento de tenant.

### Passo 7 — Validar Contenção
Teste se os mecanismos de contenção realmente funcionam. Um circuit breaker que nunca foi testado pode não abrir quando necessário.

## Perguntas de Ativação

- "Se esse componente parar de funcionar agora, o que mais para?"
- "Quantos usuários são afetados se isso falhar?"
- "Podemos limitar o impacto a um subconjunto de usuários?"
- "Temos como desligar essa mudança sem reverter todo o deploy?"
- "Qual é a cadeia de dependências mais longa a partir desse componente?"
- "Já simulamos uma falha aqui para ver o que acontece?"

## Output Esperado

| Mudança/Componente | Dependentes Diretos | Dependentes Transitivos | Usuários Afetados | Blast Radius | Contenção Projetada |
|---|---|---|---|---|---|
| Novo motor de busca | Catálogo, API mobile, Recomendações | Checkout (via recomendações), Feed | 100% dos usuários | Global | Feature flag + fallback para motor antigo |
| Migração de schema de pedidos | Serviço de pedidos | Relatórios, Faturamento, Logística | Usuários com pedidos ativos | Regional | Migração reversível + canary 5% |
| Nova regra de validação de CPF | Cadastro | Onboarding, KYC | Novos usuários apenas | Local | Feature flag por cohort |

## Armadilhas Comuns

1. **Ignorar dependências transitivas**: Avaliar apenas dependentes diretos e ser surpreendido por cascatas.
2. **Contenção não testada**: Feature flags que nunca foram ativadas, circuit breakers que nunca foram exercitados.
3. **Subestimar blast radius**: "Só afeta um serviço" — mas esse serviço é dependência de outros 15.
4. **Contenção como desculpa**: "Temos feature flag" não significa que podemos ser descuidados com a mudança.
5. **Mapeamento estático**: Dependências mudam. O mapeamento deve ser atualizado regularmente.
6. **Não considerar dados**: Uma falha que corrompe dados pode ter blast radius permanente, mesmo após correção do código.
