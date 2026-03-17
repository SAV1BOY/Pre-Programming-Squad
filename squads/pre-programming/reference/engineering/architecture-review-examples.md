# Exemplos de Architecture Reviews

## O que e uma Architecture Review

Uma architecture review e uma avaliacao estruturada de uma proposta de design arquitetural. O objetivo nao e aprovar ou rejeitar, mas identificar riscos, trade-offs nao considerados, e oportunidades de melhoria. E uma conversa colaborativa que melhora o design.

## Framework de Avaliacao

### Dimensoes de Avaliacao

| Dimensao | Perguntas-Chave |
|---|---|
| **Adequacao ao Problema** | O design resolve o problema certo? O escopo esta correto? |
| **Trade-offs** | Os trade-offs estao explicitos? Sao aceitaveis? |
| **Escalabilidade** | O design suporta o crescimento projetado? |
| **Resiliencia** | O que acontece quando componentes falham? |
| **Operabilidade** | O sistema e observavel e operavel? |
| **Seguranca** | Ameacas foram identificadas e mitigadas? |
| **Evolvabilidade** | O design pode evoluir sem reescrita? |
| **Testabilidade** | O design e testavel em todos os niveis? |
| **Simplicidade** | E a solucao mais simples que atende aos requisitos? |
| **Custo** | O custo e proporcional ao valor entregue? |

## Exemplo 1: Review de Microsservicos para E-commerce

### Contexto
Proposta de decompor o monolito de e-commerce em 8 microsservicos: Catalogo, Carrinho, Pedidos, Pagamentos, Estoque, Usuarios, Busca, Notificacoes.

### Feedback da Architecture Review

```markdown
# Architecture Review: Decomposicao em Microsservicos

**Revisor:** Ana Costa (Staff Engineer)
**Data:** 2025-03-01
**Design Doc Revisado:** DD-2025-012

## Resumo da Avaliacao
O design demonstra bom entendimento do dominio e alinhamento com
bounded contexts. No entanto, ha riscos significativos na estrategia
de migracao e na complexidade operacional.

## Pontos Positivos
- Bounded contexts bem identificados, alinhados com areas de negocio.
- Comunicacao assincrona entre dominios (via eventos) e correta.
- SLOs definidos por servico, nao globais.
- Estrategia de feature flags para rollout gradual.

## Riscos Identificados

### RISCO ALTO: Migracao Big-Bang de Dados
O design propoe migrar todos os dados de uma vez. Com 200M de registros,
isso pode levar 8-12 horas de downtime.
**Recomendacao:** Adotar dual-write + CDC (Change Data Capture) para
migracao online sem downtime. Custo adicional: ~2 semanas.

### RISCO ALTO: 8 Servicos Simultaneos para Equipe de 6 Pessoas
A equipe nao tem capacidade para operar 8 servicos simultaneamente.
Carga cognitiva excessiva (referencia: Team Topologies, carga cognitiva).
**Recomendacao:** Comecar com 3-4 servicos (Catalogo, Pedidos, Pagamentos
como modular monolith; Busca como servico separado). Expandir conforme
equipe cresce.

### RISCO MEDIO: Transacoes Distribuidas em Pedidos
O fluxo de criacao de pedido envolve Pedidos + Estoque + Pagamentos.
O design nao especifica como garantir consistencia.
**Recomendacao:** Implementar Saga pattern (coreografia via eventos)
com compensacao explicita. Documentar cenarios de falha parcial.

### RISCO MEDIO: Observabilidade Insuficiente
O design menciona "logs e metricas" sem detalhar. Com 8 servicos,
debugging distribuido e critico.
**Recomendacao:** Definir: tracing distribuido (OpenTelemetry),
metricas por servico (4 sinais dourados), dashboards de fluxos
de negocio end-to-end. Planejar antes de implementar.

### RISCO BAIXO: Schema Registry para Eventos
Eventos entre servicos usam JSON sem schema. Risco de breaking changes
silenciosas.
**Recomendacao:** Adotar schema registry (Avro ou Protobuf) com
compatibility checking.

## Questoes para Discussao
1. Qual e o criterio para decidir quando um servico e grande demais
   e deve ser dividido?
2. Como sera feito o roteamento durante a migracao (monolito vs.
   microsservico para a mesma funcionalidade)?
3. Existe estimativa de custo operacional mensal para a infra de
   8 servicos vs. monolito atual?

## Decisao
**Status:** Aprovado com condicoes.
**Condicoes:**
- Reduzir escopo inicial para 4 servicos.
- Documentar Saga patterns para fluxos criticos.
- Definir estrategia de observabilidade antes da implementacao.
- Apresentar plano de migracao de dados sem downtime.
```

## Exemplo 2: Review de Escolha Tecnologica

```markdown
# Architecture Review: Adocao de GraphQL para BFF

**Revisor:** Marcos Souza (Tech Lead)
**Data:** 2025-03-10

## Resumo
Proposta de substituir APIs REST do BFF (Backend for Frontend) por
GraphQL para reduzir over-fetching e numero de roundtrips do app mobile.

## Pontos Positivos
- Problema de over-fetching e real: app mobile baixa 3x mais dados que usa.
- GraphQL resolve o problema de composicao de dados de multiplos servicos.
- Federation permite cada equipe gerenciar seu subgrafo.

## Riscos Identificados

### RISCO ALTO: Complexidade de Caching
REST tem caching HTTP nativo (CDN, browser). GraphQL POST requests nao
sao cacheaveis por CDN por default.
**Recomendacao:** Avaliar persisted queries + GET requests para queries
frequentes. Estimar impacto no custo de CDN.

### RISCO MEDIO: N+1 Problem no Resolver
Resolvers de GraphQL podem gerar N+1 queries ao banco sem DataLoader.
**Recomendacao:** Exigir DataLoader em todos os resolvers. Incluir
testes de performance que detectam N+1.

### RISCO MEDIO: Curva de Aprendizado
Equipe nao tem experiencia com GraphQL. Estimativa de ramp-up: 3-4 semanas.
**Recomendacao:** Comecar com um subgrafo nao-critico (ex: FAQ, conteudo
editorial) antes de migrar catalogo de produtos.

## Alternativa Sugerida
Considerar REST com campos selecionaveis (sparse fieldsets / JSON:API)
como alternativa de menor risco que resolve o over-fetching sem a
complexidade de GraphQL.
```

## Checklist de Architecture Review

### Antes da Review
- [ ] Design doc completo e disponivel com 48h de antecedencia.
- [ ] Revisores selecionados com expertise relevante.
- [ ] Autores prepararam apresentacao de 15 minutos.

### Durante a Review
- [ ] Problema e escopo sao claros para todos.
- [ ] Trade-offs estao explicitos e discutidos.
- [ ] Alternativas foram genuinamente consideradas.
- [ ] Riscos foram classificados por severidade.
- [ ] Modos de falha foram analisados.
- [ ] Estrategia de rollback existe.
- [ ] Observabilidade esta planejada.
- [ ] Impacto em outras equipes foi avaliado.

### Apos a Review
- [ ] Feedback documentado e compartilhado.
- [ ] Condicoes para aprovacao estao claras.
- [ ] Action items tem owners e prazos.
- [ ] Design doc atualizado com base no feedback.
- [ ] ADR criado para decisoes significativas.

## Anti-padroes em Architecture Reviews

### O Rubber Stamp
Aprovar sem questionar. Review como formalidade. Nao agrega valor.

### O Bloqueador
Buscar perfeição. Bloquear design por questoes menores. Paralisar progresso.

### O HiPPO (Highest Paid Person's Opinion)
Decisao pela hierarquia, nao por argumentos tecnicos.

### A Revisao Tardia
Revisar quando o design ja esta implementado. Custo de mudanca alto demais.

### O Escopo Infinito
Expandir a review para questionar decisoes ja tomadas em ADRs anteriores.
