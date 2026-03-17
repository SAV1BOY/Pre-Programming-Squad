# Estilo Handoff para Outro Squad

## Formato

Pacote de transferência de contexto completo entre squads. Autocontido — o squad receptor deve conseguir agir sem reuniões adicionais de esclarecimento (embora possam optar por fazê-las). Inclui tudo que foi decidido, o que está pendente, e o que o squad receptor precisa saber mas pode não saber perguntar.

## Estrutura

```
# Handoff: [Nome do Projeto/Entregável]
## De: [Squad origem] → Para: [Squad destino]

### Metadata
- Data do handoff: [data]
- Contato no squad origem: [pessoa, canal]
- Disponibilidade para dúvidas: [período e formato]

### 1. Contexto do Projeto
[O que, por quê, para quem — em linguagem do squad receptor]

### 2. O que Foi Feito (pelo squad origem)
[Lista do que foi produzido, decidido, validado]

### 3. O que Precisa Ser Feito (pelo squad receptor)
[Escopo claro com critérios de aceitação]

### 4. Decisões Tomadas (e por quê)
[Decisões que o squad receptor deve respeitar, com justificativa]

### 5. Decisões Pendentes (para o squad receptor)
[O que ainda precisa ser decidido, com contexto para decidir]

### 6. Riscos e Armadilhas Conhecidas
[O que pode dar errado e o que o squad receptor deve vigiar]

### 7. Artefatos Entregues
[Lista com links para todos os documentos, diagramas, specs]

### 8. Critérios de Sucesso
[Como sabemos que o trabalho foi bem feito]

### 9. Checklist de Recebimento
[Itens que o squad receptor deve confirmar antes de aceitar]
```

## Tom

- Empático — considera o que o squad receptor precisa saber
- Completo — não assume conhecimento prévio do receptor
- Honesto — inclui dificuldades encontradas e riscos reais
- Organizado — informação fácil de encontrar e referenciar
- Respeitoso — transfere trabalho, não problemas

## Audiência

- Tech lead do squad receptor (ponto focal)
- Engenheiros que vão executar o trabalho
- PM do squad receptor (contexto de negócio)
- Engineering manager (para planejamento de capacidade)

## Exemplo

```
# Handoff: Motor de Regras de Precificação Dinâmica
## De: Pre-Programming Squad → Para: Squad de Pricing

### Metadata
- Data: 14/mar/2025
- Contato: Ana Costa (@ana.costa no Slack), disponível para
  dúvidas por 2 semanas após handoff (Slack assíncrono ou
  slot de 30min seg/qua/sex 14h)
- Canal de dúvidas: #proj-dynamic-pricing

### 1. Contexto do Projeto

O negócio precisa ajustar preços de produtos automaticamente com
base em demanda, estoque e sazonalidade. Hoje, ajustes são manuais
(planilha + deploy) e levam 2-3 dias. O objetivo é reduzir para
ajuste em tempo real com guardrails de variação máxima.

Impacto esperado: +8-12% na margem bruta (estimativa do time
de pricing, baseada em benchmark do setor).

### 2. O que Foi Feito

- [x] Análise de requisitos com stakeholders (PM, Pricing, Finance)
- [x] Arquitetura do motor de regras (ADR-058)
- [x] Definição de contratos de API (OpenAPI spec)
- [x] Modelagem de dados com DBA review
- [x] Análise de segurança (pre-check aprovado)
- [x] Análise de performance (load test spec definida)
- [x] Design de testes (cenários documentados)
- [x] Estimativa de esforço: 4 sprints (detalhamento abaixo)

### 3. O que Precisa Ser Feito

**Sprint 1 — Fundação**
- Criar serviço com scaffold padrão
- Implementar modelo de dados (migration + entities)
- CRUD de regras via API admin
- Critério: API admin funcional em staging

**Sprint 2 — Motor de Regras**
- Engine de avaliação de regras (lógica core)
- Integração com serviço de catálogo (leitura de preço base)
- Guardrails de variação (min/max configurável por categoria)
- Critério: regra simples executando corretamente em staging

**Sprint 3 — Integrações**
- Integração com serviço de estoque (input de estoque atual)
- Integração com analytics (input de demanda)
- Webhook para serviço de catálogo (output de preço ajustado)
- Critério: fluxo completo end-to-end em staging

**Sprint 4 — Hardening**
- Load test conforme spec
- Observabilidade completa (métricas, alertas, dashboards)
- Runbook operacional
- Feature flag para rollout gradual
- Critério: go/no-go checklist verde

### 4. Decisões Tomadas

| Decisão | Justificativa | ADR |
|---|---|---|
| PostgreSQL (não Redis) para persistência de regras | Volume baixo (<10k regras), queries complexas de auditoria | ADR-058 |
| Avaliação síncrona (não event-driven) | Latência de resposta < 100ms é requisito; volume cabe em síncrono | ADR-058 |
| Guardrail de ±20% de variação máxima | Requisito de Finance para evitar erros de precificação catastróficos | REQ-PRICING-007 |
| Audit log imutável de toda alteração de preço | Requisito regulatório (nota fiscal vinculada a preço) | REQ-PRICING-012 |

### 5. Decisões Pendentes

| Decisão | Contexto | Sugestão | Prazo |
|---|---|---|---|
| Estratégia de cache de preço calculado | TTL curto (1min) vs. invalidação por evento. Depende do volume real. | Começar com TTL de 5min, ajustar com dados de produção | Sprint 2 |
| Formato de export para Finance | CSV vs. integração direta com ERP. Finance ainda não definiu. | Agendar reunião com @carlos.finance | Sprint 3 |

### 6. Riscos e Armadilhas Conhecidas

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Serviço de catálogo não suporta webhook | Média | Alto (bloqueia Sprint 3) | Falar com @lead-catalogo na Sprint 1 para confirmar |
| Regras conflitantes entre categorias | Alta | Médio | Engine deve detectar conflito e rejeitar; testar com cenários do doc de testes |
| Volume de auditoria crescer rápido | Média | Médio | Particionamento por mês desde o início |
| Stakeholder de Finance mudar requisitos | Alta | Alto | Congelar requisitos até fim do Sprint 2; mudanças depois vão para v2 |

### 7. Artefatos Entregues

- ADR-058: /docs/adrs/058-pricing-engine.md
- OpenAPI Spec: /docs/contracts/pricing-engine-api.yaml
- Diagrama C4: /docs/diagrams/pricing-engine-c4.png
- Modelo de dados: /docs/models/pricing-engine-erd.sql
- Cenários de teste: /docs/testing/pricing-engine-scenarios.md
- Security pre-check: /docs/reviews/pricing-security-precheck.md
- Estimativa detalhada: /docs/estimates/pricing-engine-estimate.md

### 8. Critérios de Sucesso

- Motor aplica regras corretamente em 100% dos cenários documentados
- Latência p99 < 100ms para avaliação de preço
- Zero erros de precificação em produção no primeiro mês
- Auditoria completa de toda alteração de preço
- Rollout gradual via feature flag sem incidentes

### 9. Checklist de Recebimento

- [ ] Tech lead do squad Pricing revisou este documento
- [ ] Acesso ao repositório e ambientes confirmado
- [ ] Dúvidas sobre ADR-058 esclarecidas
- [ ] Sprint 1 planejado e no backlog
- [ ] Canal #proj-dynamic-pricing com membros de ambos os squads
- [ ] Reunião de kickoff agendada (sugestão: 30min com Ana)
```
