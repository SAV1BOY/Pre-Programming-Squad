# Exemplos de Design Docs

## O que e um Design Doc

Um design doc e um documento tecnico que descreve o problema, a solucao proposta, alternativas consideradas e plano de implementacao para uma mudanca significativa de software. E uma ferramenta de pensamento, comunicacao e registro historico.

## Template Padrao

```markdown
# [Titulo do Design Doc]

**Autor(es):** [Nomes]
**Revisores:** [Nomes]
**Status:** Rascunho | Em Revisao | Aprovado | Implementado | Obsoleto
**Ultima atualizacao:** [Data]

## 1. Contexto e Escopo

### Problema
[Descricao clara do problema que estamos resolvendo. Por que isso e importante agora?]

### Background
[Contexto necessario para entender o problema. Links para docs relacionados.]

### Escopo
[O que esta incluido e excluido desta proposta.]

## 2. Objetivos e Nao-Objetivos

### Objetivos
- [Objetivo mensuravel 1]
- [Objetivo mensuravel 2]

### Nao-Objetivos (explicitos)
- [O que nao estamos resolvendo neste design]
- [O que sera tratado em fases futuras]

## 3. Design Proposto

### Visao Geral
[Descricao de alto nivel da solucao. Diagrama de arquitetura.]

### Componentes Detalhados
[Para cada componente principal: responsabilidade, interface, dependencias.]

### APIs e Contratos
[Definicao de APIs, schemas, protocolos.]

### Modelo de Dados
[Schema de banco de dados, modelos de dominio, fluxos de dados.]

### Fluxos Criticos
[Diagramas de sequencia para os fluxos mais importantes.]

## 4. Alternativas Consideradas

### Alternativa A: [Nome]
**Descricao:** [...]
**Pros:** [...]
**Contras:** [...]
**Razao para rejeicao:** [...]

### Alternativa B: [Nome]
**Descricao:** [...]
**Pros:** [...]
**Contras:** [...]
**Razao para rejeicao:** [...]

## 5. Preocupacoes Transversais

### Seguranca
[Autenticacao, autorizacao, encriptacao, auditoria.]

### Observabilidade
[Metricas, logs, traces, alertas.]

### Performance
[SLIs/SLOs, estimativas de latencia e throughput.]

### Escalabilidade
[Estrategia de escala, limites esperados.]

## 6. Plano de Implementacao

### Fases
[Quebrando a entrega em incrementos.]

### Migracoes
[Plano de migracao de dados ou trafego.]

### Rollback
[Estrategia de rollback em cada fase.]

### Testes
[Estrategia de testes: unitarios, integracao, e2e, carga.]

## 7. Questoes em Aberto
[Decisoes que ainda nao foram tomadas e dependencias.]
```

## Exemplo 1: Sistema de Notificacoes

```markdown
# Design Doc: Sistema Unificado de Notificacoes

**Autor:** Maria Santos
**Revisores:** Joao Silva (backend), Ana Costa (infra), Pedro Lima (produto)
**Status:** Aprovado
**Ultima atualizacao:** 2025-03-15

## 1. Contexto e Escopo

### Problema
Atualmente, cada servico implementa sua propria logica de notificacao
(email, push, SMS). Isso resulta em: templates inconsistentes, logica
de deduplicacao duplicada em 4 servicos, impossibilidade de gerenciar
preferencias de usuario centralmente, e custo de manutencao multiplicado.

### Escopo
Criar um servico centralizado de notificacoes que receba eventos de
dominio e entregue notificacoes pelos canais configurados pelo usuario.

## 2. Objetivos e Nao-Objetivos

### Objetivos
- Centralizar envio de notificacoes em um unico servico.
- Suportar email, push e SMS como canais de entrega.
- Permitir que usuarios gerenciem preferencias de canal por tipo.
- Latencia p99 < 5s para notificacoes nao-urgentes, < 1s para urgentes.

### Nao-Objetivos
- Notificacoes in-app (sera tratado na fase 2).
- Integracao com WhatsApp (avaliacao futura).
- Substituicao de emails transacionais existentes (migracao gradual).

## 3. Design Proposto

### Visao Geral
Arquitetura event-driven: servicos publicam domain events em topicos
Kafka. O Notification Service consome eventos, aplica regras de roteamento,
resolve templates e despacha para providers de entrega (SES, FCM, Twilio).

### Componentes
- **Event Consumer:** Consome eventos de dominio do Kafka.
- **Router:** Aplica regras de preferencia do usuario e prioridade.
- **Template Engine:** Resolve templates Handlebars com dados do evento.
- **Delivery Manager:** Gerencia envio para providers com retry e circuit breaker.
- **Preference Store:** Armazena preferencias de canal por usuario/tipo.

### APIs
POST /api/v1/notifications/send (envio sincrono para casos urgentes)
GET /api/v1/users/{id}/preferences
PUT /api/v1/users/{id}/preferences

## 4. Alternativas Consideradas

### Alternativa A: Biblioteca Compartilhada
Extrair logica comum em uma lib compartilhada por todos os servicos.
**Pros:** Menor mudanca arquitetural.
**Contras:** Nao centraliza preferencias, deploy acoplado, n+1 instancias.
**Rejeitada porque:** Nao resolve o problema de gerenciamento centralizado.

### Alternativa B: SaaS Externo (Customer.io, OneSignal)
**Pros:** Sem desenvolvimento, features prontas.
**Contras:** Custo mensal alto (~$15k/mes), lock-in, dados de usuarios
em terceiros, latencia adicional.
**Rejeitada porque:** Custo e concerns de privacidade de dados.

## 5. Preocupacoes Transversais

### Observabilidade
- Metricas: taxa de envio por canal, latencia de entrega, taxa de falha.
- Alertas: taxa de falha > 5% em janela de 5 min.
- Tracing: correlation ID do evento original ate a entrega.

### Escalabilidade
- Kafka consumer groups para escala horizontal.
- Estimativa: 500k notificacoes/dia (fase 1), 2M/dia (fase 2).
```

## Exemplo 2: Migracao de Banco de Dados

```markdown
# Design Doc: Migracao de PostgreSQL para Aurora Serverless v2

**Autor:** Carlos Oliveira
**Status:** Em Revisao

## 1. Contexto
O servico de catalogo usa PostgreSQL on-premise com picos de carga
variando 10x entre horario comercial e madrugada. Pagamos por
capacidade de pico 24/7. Aurora Serverless v2 oferece auto-scaling.

## 2. Objetivos
- Reduzir custo de infra em ~40% (de $8k para ~$5k/mes).
- Eliminar manutencao manual de replicas de leitura.
- Manter latencia p99 < 50ms para queries de catalogo.

## 3. Design: Migracao em 3 Fases
Fase 1: Provisionar Aurora, configurar replicacao DMS.
Fase 2: Shadow traffic (ler de ambos, comparar resultados).
Fase 3: Cutover com fallback para PostgreSQL por 2 semanas.

## 4. Alternativas
A: Migrar para AlloyDB (Google Cloud) — rejeitada, estamos em AWS.
B: Manter PostgreSQL com auto-scaling via Kubernetes — mais complexo operacionalmente.

## 7. Riscos
- Incompatibilidade de extensoes PostgreSQL (pg_trgm confirmado compativel).
- Cold start do Aurora Serverless apos periodo de inatividade (~25s).
  Mitigacao: manter capacidade minima de 0.5 ACU.
```

## Boas Praticas para Design Docs

### Escreva para o Leitor, nao para Voce
- Assuma que o leitor nao conhece o contexto. Inclua links e background.
- Use diagramas — uma imagem vale mais que paragrafos de texto.
- Seja conciso mas completo — cada secao deve justificar sua existencia.

### Alternativas sao Obrigatorias
- No minimo duas alternativas genuinas (nao straw man).
- Inclua a opcao "nao fazer nada" quando relevante.
- Explique claramente por que a opcao escolhida e preferida.

### Non-Goals Previnem Scope Creep
- Liste explicitamente o que nao esta no escopo.
- Referencie futuras fases quando apropriado.

### Revisao e Colaboracao, nao Aprovacao
- Revisores devem adicionar valor, nao apenas aprovar.
- Feedback deve ser especifico e construtivo.
- Desacordos devem ser resolvidos por dados e argumentos, nao hierarquia.
