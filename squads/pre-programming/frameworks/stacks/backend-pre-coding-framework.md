# Backend Pre-Coding Framework

## Título e Propósito

O **Backend Pre-Coding Framework** é um checklist estruturado para garantir que todas as decisões e preparações necessárias para implementação backend estejam completas antes de escrever a primeira linha de código. O propósito é endereçar as dimensões específicas de projetos backend — modelo de dados, APIs, integrações, performance, segurança — que frequentemente geram retrabalho quando não planejadas.

## Quando Usar

- Antes de iniciar implementação de qualquer serviço ou API backend
- Em projetos que envolvem novo modelo de dados ou schema
- Ao projetar integrações server-to-server
- Em migrações ou refactors de backend existente
- Como checklist de readiness específico para trabalho backend

## Conceitos-Chave

1. **Contrato de API**: Definição completa de endpoints, payloads, códigos de status, autenticação — antes de implementar.
2. **Modelo de Dados**: Schema, relacionamentos, invariantes, índices, migrações — design before code.
3. **Padrão de Concorrência**: Como o sistema lida com acessos simultâneos: locks, transações, versionamento otimista.
4. **Estratégia de Cache**: O que cachear, TTL, invalidação, warm-up — decisões de design, não afterthoughts.
5. **Observabilidade Backend**: Logs estruturados, métricas RED, tracing distribuído — projetados junto com a feature.

## Processo / Passos

### Passo 1 — Definir Contratos de API
Antes de implementar, defina: endpoints, métodos HTTP, payloads (request/response), códigos de status, autenticação, rate limiting, versionamento.

### Passo 2 — Projetar Modelo de Dados
Defina: entidades, atributos, tipos, relacionamentos, invariantes, índices, estratégia de migração.

### Passo 3 — Mapear Integrações
Para cada dependência externa: contrato, SLA, timeout, retry, circuit breaker, fallback, mock para testes.

### Passo 4 — Definir Estratégia de Concorrência
Onde há acesso concorrente? Qual mecanismo: lock pessimista, versionamento otimista, fila? Testar com cenários concorrentes.

### Passo 5 — Planejar Cache
O que cachear? Qual TTL? Como invalidar? Cache em memória, Redis, CDN? Warming strategy?

### Passo 6 — Projetar Segurança
Autenticação, autorização, validação de input, sanitização, rate limiting, audit logging.

### Passo 7 — Definir Observabilidade
Logs: formato, campos, níveis. Métricas: RED por endpoint. Traces: spans e atributos. Alertas.

## Perguntas de Ativação

- "O contrato de API está definido e acordado com os consumidores?"
- "O modelo de dados suporta as queries que precisaremos fazer?"
- "O que acontece se dois usuários fizerem a mesma operação ao mesmo tempo?"
- "Onde está o gargalo de performance nesse fluxo?"
- "Se essa API receber 10x o tráfego esperado, o que acontece?"
- "Os logs terão informação suficiente para debugar em produção?"

## Output Esperado

Checklist preenchido com status de cada item e ações pendentes para itens incompletos. Serve como gate de readiness para iniciar implementação backend.

## Armadilhas Comuns

1. **API sem contrato**: Implementar o endpoint e "ver como fica" resulta em API inconsistente.
2. **Schema sem índices**: Funciona em desenvolvimento, trava em produção com dados reais.
3. **Concorrência ignorada**: "Funciona no meu teste" com 1 usuário. Explode com 100 simultâneos.
4. **Cache sem invalidação**: Dados stale servidos porque ninguém pensou em como invalidar.
5. **Segurança como afterthought**: Adicionar auth e validação depois é mais caro e mais propenso a furos.
6. **Logs sem contexto**: Logs que dizem "erro" sem dizer em qual request, para qual usuário, com quais dados.
