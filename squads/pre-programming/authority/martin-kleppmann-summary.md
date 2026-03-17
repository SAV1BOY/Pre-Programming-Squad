# Martin Kleppmann — Resumo de Autoridade

## Autor

**Nome**: Martin Kleppmann
**Afiliação**: Pesquisador, University of Cambridge (anteriormente LinkedIn, Rapportive)
**Obra Principal**: "Designing Data-Intensive Applications" (O'Reilly, 2017)
**Área de Expertise**: Sistemas distribuídos, modelagem de dados, consistência, streaming de dados

---

## Tese Central

A maioria das aplicações modernas são **data-intensive** (limitadas por complexidade e volume de dados) e não **compute-intensive** (limitadas por processamento). As decisões mais importantes de arquitetura envolvem como dados são armazenados, consultados, transformados e transmitidos entre sistemas. Entender profundamente os trade-offs entre consistência, disponibilidade, latência e durabilidade é essencial para projetar sistemas confiáveis.

---

## Conceitos-Chave

### 1. Modelos de Dados e Linguagens de Query
A escolha do modelo de dados (relacional, documento, grafo, key-value) tem impacto profundo no código da aplicação. Não existe modelo universalmente melhor — cada um otimiza para padrões de acesso diferentes.

### 2. Replicação e Particionamento
- **Replicação**: Manter cópias dos dados em múltiplos nós. Trade-offs entre síncrona (durável mas lenta) e assíncrona (rápida mas risco de perda).
- **Particionamento/Sharding**: Dividir dados entre nós. Estratégias por range ou hash. Rebalanceamento é operação perigosa.

### 3. Consistência e Consenso
O teorema CAP é frequentemente mal interpretado. Na prática, o trade-off real é entre **consistência e latência** dentro de uma partição. Linearizabilidade tem custo de performance. Modelos mais fracos (eventual consistency, causal consistency) são aceitáveis para muitos casos.

### 4. Stream Processing
Dados são naturalmente um log de eventos ao longo do tempo. Sistemas baseados em logs (Kafka, event sourcing) permitem:
- Reconstrução de estado em qualquer ponto
- Integração entre sistemas via CDC (Change Data Capture)
- Processamento em tempo real e batch no mesmo pipeline

### 5. Transações Distribuídas
Transações distribuídas (2PC, Saga) são custosas e complexas. Quando possível, projetar sistemas que evitem a necessidade de transações distribuídas — usando bounded contexts e eventual consistency.

---

## Aplicação ao Squad

- **Análise de padrões de acesso antes da escolha de banco**: Na pesquisa de stack, documentar os padrões de acesso (reads vs writes, volume, latência, relações entre dados) antes de escolher o banco de dados. A escolha deve ser driven por dados, não por familiaridade.

- **Trade-offs de consistência no design doc**: Para cada componente que envolve dados distribuídos, explicitar qual modelo de consistência é necessário e por quê. "Precisamos de linearizabilidade?" é pergunta de design, não de implementação.

- **Estratégia de particionamento planejada**: Se o volume de dados justifica particionamento, a estratégia deve ser definida na pré-programação. Mudar a chave de particionamento depois é migração arriscada.

- **CDC como padrão de integração**: Para integração entre serviços que compartilham dados, avaliar CDC como alternativa a chamadas síncronas. Documentar no design doc.

---

## Citações Relevantes

> "An application has to meet various requirements in order to be useful. There are functional requirements (what it should do) and nonfunctional requirements (general properties like security, reliability, compliance, scalability, compatibility, and maintainability)."

> "Many applications today are data-intensive, as opposed to compute-intensive. Raw CPU power is rarely a limiting factor — bigger problems are usually the amount of data, the complexity of data, and the speed at which it is changing."

> "There is no one-size-fits-all solution for data storage. Different data models serve different purposes, and the choice of data model has a profound effect on the software that is written on top of it."

> "Distributed systems are fundamentally different from single-node systems. You can't just take a single-node algorithm and deploy it across multiple nodes."

> "The truth is that there are no right answers in systems design — only trade-offs."
