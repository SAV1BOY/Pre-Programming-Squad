# Ótimos Design Docs — Exemplos Anotados

## Introdução

Um design doc excepcional serve como o "contrato intelectual" entre quem pensou a solução e quem vai implementá-la. Ele não é documentação pós-facto — é o artefato que guia a implementação, registra trade-offs e permite que revisores identifiquem problemas antes de uma linha de código ser escrita. O formato popularizado pelo Google, onde design docs são pré-requisito para projetos significativos, é referência mundial.

---

## Exemplo 1 — Design Doc de Serviço de Notificações

### Estrutura Anotada

> **Contexto e Escopo**: O sistema atual envia notificações de forma síncrona dentro do monolito. Com 2M de usuários e previsão de 10M em 12 meses, o envio síncrono já causa timeouts em picos. Este design propõe um serviço de notificações assíncrono e multi-canal.
>
> **Objetivos e Não-Objetivos**:
> - Objetivo: Suportar 100K notificações/minuto com latência p99 < 5s
> - Objetivo: Multi-canal (push, e-mail, SMS, in-app) com template unificado
> - Não-objetivo: Analytics de engajamento (será outro serviço)
> - Não-objetivo: Personalização por ML (fase futura)
>
> **Design Proposto**: Arquitetura event-driven com Kafka como backbone. Producers publicam eventos de notificação. Consumers por canal (push, email, SMS) processam em paralelo. DLQ para falhas. Rate limiting por usuário e canal.
>
> **Alternativas Consideradas**: (1) Serviço síncrono com filas internas — descartado por acoplamento. (2) Uso de SaaS (OneSignal/Braze) — descartado por custo em escala e lock-in. (3) Design atual com otimizações — descartado por limitação de escala.
>
> **Trade-offs**: Eventual consistency na entrega (aceitável para notificações). Complexidade operacional de Kafka. Necessidade de idempotência nos consumers.

### Por que funciona

- **Não-objetivos tão claros quanto objetivos**: Evita scope creep durante implementação
- **Números concretos**: 100K/min, p99 < 5s — o time sabe exatamente o que construir
- **Alternativas com justificativa de descarte**: Mostra que o design foi uma escolha, não a primeira ideia
- **Trade-offs explícitos**: Reconhece o custo da decisão, não vende a solução como perfeita

---

## Exemplo 2 — Design Doc de Migração de Banco de Dados

### Estrutura Anotada

> **Contexto**: Migrar de MySQL 5.7 single-instance para PostgreSQL 15 com read replicas. Motivação: necessidade de JSONB para dados semi-estruturados, full-text search nativo e melhor suporte a particionamento.
>
> **Estratégia de Migração**: Dual-write com Shadow Traffic. Fase 1: PostgreSQL como secondary (writes duplicados, reads do MySQL). Fase 2: PostgreSQL como primary (reads migrados gradualmente). Fase 3: Descomissionamento do MySQL.
>
> **Plano de Dados**: pgloader para migração inicial. Mapeamento de tipos (TEXT -> TEXT, DATETIME -> TIMESTAMPTZ, JSON -> JSONB). Stored procedures reescritas como funções PL/pgSQL. Triggers recriadas com lógica equivalente.
>
> **Rollback**: Em cada fase, rollback é possível revertendo a configuração de primary/secondary. Dados criados no PostgreSQL durante dual-write são replicados de volta via CDC.
>
> **Riscos**: Diferenças sutis de comportamento entre MySQL e PostgreSQL (collation, NULL handling, auto-increment vs sequences). Mitigação: suite de testes de compatibilidade com 500+ assertions.

### Por que funciona

- **Migração em fases reversíveis**: Cada fase tem rollback, não é aposta tudo-ou-nada
- **Detalhes de mapeamento de dados**: Mostra que quem escreveu entende as nuances
- **Riscos com diferenças sutis**: Reconhece que a dificuldade está nos detalhes, não na mudança em si
- **Critério de validação quantificado**: 500+ assertions de compatibilidade

---

## Exemplo 3 — Design Doc de Sistema de Permissões (RBAC)

### Estrutura Anotada

> **Modelo de Dados**: Entidades — Users, Roles, Permissions, Resources. Relações M:N entre Users-Roles e Roles-Permissions. Resources com hierarquia (org > team > project > resource).
>
> **Algoritmo de Resolução**: Deny-by-default. Permissões avaliadas de baixo para cima na hierarquia. Deny explícito em qualquer nível sobrescreve allows. Cache em Redis com TTL de 5min e invalidação por evento.
>
> **API**: `POST /authorize` aceita {user_id, action, resource_id} e retorna {allowed: bool, reason: string}. Latência target: p99 < 10ms (com cache hit), p99 < 50ms (cache miss).
>
> **Segurança**: Audit log de toda verificação de permissão. Princípio do menor privilégio por default. Roles predefinidas (admin, editor, viewer) com possibilidade de roles customizadas.

### Por que funciona

- **Modelo mental claro**: Hierarquia de recursos visualizável
- **Regra de resolução inequívoca**: Deny-by-default, deny sobrescreve allow
- **Performance com números**: Diferencia cache hit de miss
- **Segurança como first-class citizen**: Audit log e menor privilégio desde o design

---

## Lições Extraídas

1. **Comece pelos não-objetivos**: Delimitar o que não será feito previne 80% do scope creep
2. **Inclua alternativas descartadas**: Design docs sem alternativas sugerem que não houve análise
3. **Quantifique tudo**: Requisitos vagos como "rápido" ou "escalável" são inúteis
4. **Explicite trade-offs**: Toda decisão técnica tem custo — documentar isso é honestidade intelectual
5. **Planeje o rollback no design, não no incidente**: Se o rollback é uma reflexão tardia, o design está incompleto
6. **Use diagramas**: Um diagrama de arquitetura vale mais que mil palavras
7. **Revise com quem vai implementar**: Design doc não revisado é ficção
