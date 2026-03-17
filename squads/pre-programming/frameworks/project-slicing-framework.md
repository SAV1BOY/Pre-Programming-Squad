# Project Slicing Framework

## Título e Propósito

O **Project Slicing Framework** é um sistema para decompor projetos grandes em fatias (slices) verticais que entregam valor incrementalmente. O propósito é substituir a decomposição por camada técnica (backend, frontend, infra) por fatias que atravessam todas as camadas e entregam funcionalidade completa — permitindo feedback real mais cedo e reduzindo risco.

## Quando Usar

- No planejamento de qualquer projeto que dura mais de 2 semanas
- Quando o projeto foi decomposto em tarefas técnicas mas não em entregas de valor
- Quando stakeholders não veem progresso apesar de muito trabalho estar acontecendo
- Para sequenciar o trabalho de forma que cada entrega seja usável
- Quando a equipe precisa de feedback real antes de investir em todas as features

## Conceitos-Chave

1. **Fatia Vertical**: Uma porção do projeto que atravessa todas as camadas (UI, lógica, dados, infra) e entrega funcionalidade completa ao usuário.
2. **Fatia Horizontal**: Uma porção que cobre apenas uma camada (ex: "fazer toda a API" sem frontend). Não entrega valor isoladamente.
3. **Walking Skeleton**: A primeira fatia, mínima, que conecta todas as camadas end-to-end. Prova que a arquitetura funciona.
4. **Valor Incremental**: Cada fatia deve entregar valor que não existia antes. Valor pode ser: aprendizado, funcionalidade, redução de risco.
5. **Independência de Fatias**: Idealmente, fatias podem ser implementadas e entregues independentemente, em qualquer ordem.

## Processo / Passos

### Passo 1 — Mapear as Funcionalidades Completas
Liste todas as funcionalidades do projeto como o usuário as vê, não como o dev as implementa.

### Passo 2 — Ordenar por Valor e Risco
Para cada funcionalidade, avalie: valor de negócio (alto/médio/baixo) e risco técnico (alto/médio/baixo). Priorize: alto valor + alto risco primeiro.

### Passo 3 — Identificar o Walking Skeleton
Qual é a menor fatia que conecta todas as camadas end-to-end? Ela não precisa ter funcionalidade rica — precisa provar que a arquitetura funciona.

### Passo 4 — Fatiar Funcionalidades
Para cada funcionalidade, pergunte: "Posso entregar uma versão menor que já seja útil?" Exemplo: checkout completo para cartão de crédito antes de adicionar Pix e boleto.

### Passo 5 — Verificar Verticalidade
Para cada fatia, verifique: "Essa fatia entrega algo usável pelo usuário final ou é só uma camada técnica?" Se for horizontal, reformule.

### Passo 6 — Verificar Independência
As fatias podem ser entregues em qualquer ordem? Se há dependências, mapeie e ordene.

### Passo 7 — Criar Roadmap de Fatias
Sequencie: Walking Skeleton → Fatias de alto risco/valor → Fatias de médio risco/valor → Refinamentos e polimento.

## Perguntas de Ativação

- "Se entregássemos essa fatia amanhã, o usuário poderia fazer algo que não podia antes?"
- "Essa fatia é vertical (ponta a ponta) ou horizontal (só uma camada)?"
- "Qual é a menor fatia que prova que a arquitetura funciona?"
- "Podemos obter feedback real do usuário após essa fatia?"
- "Se cortássemos o projeto aqui, o que já foi entregue teria valor?"
- "Estamos fatiando por conveniência técnica ou por entrega de valor?"

## Output Esperado

```
PROJETO: [nome]

WALKING SKELETON (Fatia 0):
- Descrição: Fluxo de compra mínimo: 1 produto, cartão de crédito, sem cadastro
- Valor: Prova arquitetura end-to-end
- Camadas: UI (1 tela) + API (2 endpoints) + DB (2 tabelas) + Gateway pagamento
- Estimativa: 1 semana

FATIA 1: Cadastro e login
- Valor: Usuários podem criar conta e manter histórico
- Dependências: Walking Skeleton
- Estimativa: 3 dias

FATIA 2: Catálogo com busca
- Valor: Usuários encontram produtos por busca
- Dependências: Walking Skeleton
- Estimativa: 4 dias

FATIA 3: Múltiplos meios de pagamento (Pix + boleto)
- Valor: Aumenta conversão em ~30%
- Dependências: Fatia 0 (checkout existente)
- Estimativa: 5 dias

[...]

SEQUÊNCIA: Fatia 0 → Fatia 1 → Fatia 2 (paralelo com 1) → Fatia 3 → ...
```

## Armadilhas Comuns

1. **Fatias horizontais disfarçadas**: "Criar toda a API" parece produtivo mas não entrega valor até o frontend estar pronto.
2. **Walking Skeleton adiado**: "Primeiro precisamos de toda a infraestrutura" — o walking skeleton existe para validar isso cedo.
3. **Fatias muito grandes**: Se uma fatia leva mais de 2 semanas, ela pode ser fatiada ainda mais.
4. **Valor assumido**: "O usuário vai gostar dessa fatia" sem validação. Entregar cedo justamente para descobrir.
5. **Dependências não mapeadas**: Fatias que parecem independentes mas compartilham dependência que vira gargalo.
6. **Polimento cedo**: Investir em perfeição na primeira fatia em vez de cobrir mais funcionalidades rapidamente.
