# Ótimos ADRs — Exemplos Anotados

## Introdução

Architecture Decision Records (ADRs) são documentos curtos que capturam uma decisão de arquitetura significativa junto com seu contexto e consequências. Popularizados por Michael Nygard, ADRs criam um registro histórico imutável de por que o sistema é como é. Os melhores ADRs são concisos, objetivos e escritos no momento da decisão — não meses depois.

---

## Exemplo 1 — ADR: Adotar Event Sourcing para Domínio de Pedidos

### O ADR

> **Status**: Aceita
>
> **Contexto**: O sistema de pedidos precisa de auditoria completa de todas as mudanças de estado, suporte a "desfazer" operações e reconstrução do estado em qualquer ponto no tempo. O modelo CRUD atual perde o histórico a cada UPDATE.
>
> **Decisão**: Adotar Event Sourcing para o bounded context de Pedidos. Cada mudança de estado será registrada como um evento imutável. O estado atual será derivado do replay dos eventos. CQRS será usado para separar leitura e escrita.
>
> **Consequências**:
> - Positiva: Auditoria completa sem código adicional
> - Positiva: Possibilidade de reconstruir estado em qualquer ponto
> - Positiva: Eventos podem alimentar outros sistemas via pub/sub
> - Negativa: Complexidade de implementação significativamente maior
> - Negativa: Queries sobre estado atual requerem read models (CQRS)
> - Negativa: Curva de aprendizado alta para o time
> - Neutra: Event store requer estratégia de snapshot para performance

### Por que funciona

- **Contexto com necessidade real**: Auditoria e "desfazer" são requisitos concretos, não "porque é moderno"
- **Consequências honestas**: 3 negativas declaradas — ADR não é propaganda
- **Escopo limitado**: Event Sourcing apenas para Pedidos, não para todo o sistema

---

## Exemplo 2 — ADR: Usar PostgreSQL em vez de MongoDB

### O ADR

> **Status**: Aceita
>
> **Contexto**: O novo serviço precisa de banco de dados. Dados são predominantemente relacionais (usuários, pedidos, produtos com relações complexas). Alguns campos têm estrutura semi-variável (atributos de produto por categoria). Time tem 5 anos de experiência com PostgreSQL e 6 meses com MongoDB.
>
> **Decisão**: Usar PostgreSQL 16 com JSONB para campos semi-estruturados. Não adotar MongoDB.
>
> **Alternativas descartadas**:
> - MongoDB: Flexibilidade de schema é atraente, mas dados são fundamentalmente relacionais. JSONB resolve a necessidade de campos flexíveis. Experiência do time é insuficiente para operação em produção.
> - MySQL 8: Viável, mas JSONB do PostgreSQL é superior ao JSON do MySQL. Full-text search nativo do PostgreSQL elimina necessidade de Elasticsearch para buscas simples.
>
> **Consequências**:
> - Positiva: Time produtivo desde o dia 1
> - Positiva: JSONB resolve necessidade de flexibilidade sem banco NoSQL separado
> - Positiva: Ecossistema maduro de ferramentas e monitoramento
> - Negativa: Schema migrations mais rígidas que NoSQL
> - Negativa: Escalabilidade horizontal mais complexa que MongoDB

### Por que funciona

- **Decisão baseada em experiência do time**: Fator humano pesou adequadamente
- **JSONB como compromisso pragmático**: Resolve a necessidade real sem mudar o paradigma
- **Alternativas com justificativa detalhada**: Cada descarte é fundamentado

---

## Exemplo 3 — ADR: Adotar Monorepo com Turborepo

### O ADR

> **Status**: Aceita
>
> **Contexto**: Temos 4 serviços frontend (app web, admin, landing pages, docs) e 3 bibliotecas compartilhadas (design system, utils, API client). Hoje cada um é um repositório separado. Mudanças em bibliotecas compartilhadas requerem PRs em 4 repos, com versões frequentemente out-of-sync.
>
> **Decisão**: Consolidar em monorepo usando Turborepo para orquestração de builds. Cada pacote mantém independência de deploy. Workspace do pnpm para gerenciar dependências.
>
> **Consequências**:
> - Positiva: Mudanças atômicas em biblioteca + consumidores no mesmo PR
> - Positiva: Cache inteligente do Turborepo reduz tempo de CI em ~60%
> - Positiva: Refactoring cross-projeto muito mais fácil
> - Negativa: Repositório maior, clone inicial mais lento
> - Negativa: CI precisa ser smart sobre quais pacotes rebuildar
> - Negativa: Curva de aprendizado com workspaces e Turborepo

### Por que funciona

- **Problema concreto**: PRs em 4 repos e versões out-of-sync são dores reais
- **Benefício quantificado**: ~60% de redução no tempo de CI
- **Tooling específico**: Turborepo + pnpm, não apenas "monorepo"

---

## Lições Extraídas

1. **Escreva no momento da decisão**: ADRs escritos depois perdem contexto e são revisões históricas enviesadas
2. **Mantenha curto**: Um ADR não deve ter mais que 1-2 páginas. Se precisar de mais, é um design doc
3. **Seja honesto nas consequências negativas**: ADRs que só listam positivos perdem credibilidade
4. **Documente o "não escolhido"**: As alternativas descartadas são tão valiosas quanto a decisão
5. **ADRs são imutáveis**: Quando a decisão muda, crie um novo ADR que referencia o anterior
6. **Numere sequencialmente**: ADR-001, ADR-002... cria timeline navegável
7. **Use status claros**: Proposta, Aceita, Depreciada, Superada — cada ADR tem um estado
8. **Vincule ao contexto**: Referencie tickets, métricas, incidentes que motivaram a decisão
