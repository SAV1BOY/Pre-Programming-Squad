# SRE (Site Reliability Engineering) — Resumo de Autoridade

## Autor

**Organização**: Google (originadores), comunidade SRE global
**Contribuidores Notáveis**: Ben Treynor Sloss (VP Engineering, Google — "fundador" do SRE), Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Murphy
**Obras Principais**: "Site Reliability Engineering" (2016), "The Site Reliability Workbook" (2018), "Building Secure and Reliable Systems" (2020)
**Área de Expertise**: Confiabilidade de sistemas em escala, operações, observabilidade, gestão de incidentes

---

## Tese Central

SRE é "o que acontece quando você pede a um engenheiro de software para resolver problemas de operações". Em vez de times de operações separados, o Google criou uma disciplina onde engenheiros de software aplicam princípios de engenharia para operações: automação, mensuração, error budgets e eliminação de toil. O princípio fundamental é que **confiabilidade é a feature mais importante** — se o sistema não funciona, nenhuma outra feature importa.

---

## Conceitos-Chave

### 1. SLIs, SLOs e Error Budgets
- **SLI**: A métrica (latência p99, taxa de erro, throughput)
- **SLO**: A meta (p99 < 200ms, erro < 0.1%)
- **Error Budget**: O quanto pode falhar (se SLO é 99.9%, budget é 0.1% = 43.8 min/mês)
- Error budget gasto = priorizar confiabilidade. Budget sobrando = liberdade para inovar.

### 2. Toil
Trabalho manual, repetitivo, automatizável, reativo, sem valor duradouro. SRE tem como meta manter toil abaixo de 50% do tempo. O restante é investido em engenharia que elimina toil futuro.

### 3. Monitoring e Observabilidade
Quatro sinais dourados para monitorar qualquer serviço:
- **Latência**: Tempo de resposta para requests bem-sucedidos e com erro
- **Tráfego**: Volume de requests ao serviço
- **Erros**: Taxa de requests que falham
- **Saturação**: Quão "cheio" o serviço está (CPU, memória, disco, conexões)

### 4. Incident Management
Processo estruturado de resposta a incidentes:
- Incident Commander (IC): Coordena a resposta
- Comunicação estruturada: Canais definidos, atualizações regulares
- Postmortem obrigatório: Para todo incidente significativo
- Action items rastreados: Nenhum postmortem sem ações concretas

### 5. Capacity Planning
Previsão e provisionamento de recursos:
- Organic growth: Crescimento natural de adoção
- Inorganic growth: Lançamento de features, marketing, sazonalidade
- Load testing: Validar que o sistema suporta a carga planejada

---

## Aplicação ao Squad

- **SLIs/SLOs no design doc**: Para cada serviço, definir SLIs e SLOs durante a pré-programação. Isso influencia decisões de caching, redundância e degradação.

- **Four Golden Signals como requisito de observabilidade**: Todo serviço entregue deve ter monitoring para latência, tráfego, erros e saturação. Definir dashboards no plano de pré-programação.

- **Error budget no go/no-go**: Considerar error budget atual ao decidir se um deploy arriscado deve prosseguir. Budget esgotado = freeze de features.

- **Toil assessment**: Identificar toil atual que o novo sistema deveria eliminar. Quantificar horas economizadas como justificativa do projeto.

- **Capacity planning como seção obrigatória**: Todo design doc deve incluir: carga esperada (atual e projetada), dimensionamento de recursos, limites de escala conhecidos.

- **Incident response no plano de rollout**: Definir antes do deploy: quem é o IC, qual o canal de comunicação, qual o processo de escalação, qual o critério de rollback.

---

## Citações Relevantes

> "Hope is not a strategy."

> "100% is the wrong reliability target for basically everything."

> "If a human operator needs to touch your system during normal operations, you have a bug."

> "SRE is what happens when you ask a software engineer to design an operations team."

> "The cost of reliability is not having it."

> "Monitoring is for asking pre-defined questions. Observability is for asking questions you didn't know you needed to ask."
