# API-First Readiness Framework

## Título e Propósito

O **API-First Readiness Framework** é um checklist para garantir que APIs sejam projetadas como produtos (contratos-primeiro) antes de implementar qualquer lógica. O propósito é evitar APIs que são subprodutos da implementação — mal desenhadas, inconsistentes e difíceis de consumir — promovendo APIs projetadas deliberadamente para seus consumidores.

## Quando Usar

- Ao projetar qualquer API que será consumida por outros times, apps ou parceiros
- Em projetos que adotam abordagem API-first
- Quando múltiplos clientes (web, mobile, terceiros) consumirão a mesma API
- Na revisão de APIs existentes antes de versionamento
- Ao definir padrões de API para a organização

## Conceitos-Chave

1. **Contract-First**: O contrato da API (OpenAPI/Swagger) é definido antes da implementação. O código implementa o contrato, não o contrário.
2. **Consumer-Driven**: O design da API é guiado pelas necessidades dos consumidores, não pela estrutura interna do backend.
3. **Consistência**: Todas as APIs seguem os mesmos padrões de naming, paginação, erros, autenticação. Previsibilidade é feature.
4. **Evolvability**: A API pode evoluir (novos campos, novos endpoints) sem quebrar consumidores existentes.
5. **Developer Experience (DX)**: A API é fácil de entender, documentada, com exemplos, erros claros.

## Processo / Passos

### Passo 1 — Identificar Consumidores
Quem vai consumir essa API? Web app, mobile, parceiros, outros serviços? Cada consumidor tem necessidades diferentes.

### Passo 2 — Definir Contrato
Escreva a especificação OpenAPI/Swagger antes de implementar: endpoints, métodos, payloads, status codes, autenticação.

### Passo 3 — Definir Padrões de Consistência
Naming (camelCase vs. snake_case), paginação (cursor vs. offset), erros (formato padronizado), filtering, sorting, versionamento.

### Passo 4 — Projetar Tratamento de Erros
Formato padronizado de erro com: código, mensagem human-readable, detalhes para debug. Não expor internos.

### Passo 5 — Validar com Consumidores
Compartilhe o contrato com consumidores antes de implementar. Feedback nessa fase custa minutos; após implementação, custa dias.

### Passo 6 — Gerar Mocks
A partir do contrato, gere mocks para que consumidores desenvolvam em paralelo sem depender do backend.

### Passo 7 — Definir Estratégia de Versionamento
Como a API evolui sem quebrar clientes? Header versioning, URL versioning, additive changes only?

## Perguntas de Ativação

- "O contrato da API está definido e validado com os consumidores?"
- "Todas as APIs seguem os mesmos padrões ou cada endpoint é diferente?"
- "Se o consumidor receber um erro, a mensagem o ajuda a resolver?"
- "Podemos adicionar campos à API sem quebrar clientes existentes?"
- "A documentação está atualizada e tem exemplos?"
- "Os consumidores podem desenvolver contra mocks enquanto o backend não está pronto?"

## Output Esperado

Especificação OpenAPI completa, validada com consumidores, com mocks disponíveis e padrões documentados.

## Armadilhas Comuns

1. **API como reflexo do banco**: Endpoints que espelham tabelas em vez de casos de uso do consumidor.
2. **Implementação-first**: Construir o backend e depois "ver como fica a API". Resulta em API inconsistente.
3. **Sem padrão de erros**: Cada endpoint retorna erros em formato diferente. Consumidores enlouquecem.
4. **Breaking changes sem versionamento**: Mudar campo ou formato sem aviso quebra consumidores em produção.
5. **Documentação desatualizada**: Swagger gerado automaticamente mas que não reflete o comportamento real.
6. **Over-fetching / under-fetching**: Endpoints que retornam dados demais ou de menos para o caso de uso.
