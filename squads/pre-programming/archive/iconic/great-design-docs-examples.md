# Exemplos Icônicos de Design Docs

## Objetivo

Compilar exemplos anotados de documentos de design técnico que representam excelência na fase de pré-programação. Estes exemplos mostram como comunicar decisões técnicas de forma clara antes de escrever código.

---

## Exemplo 1: Design Doc do Sistema de Filas com Priorização Dinâmica

### Contexto
Sistema de processamento de pedidos que precisava evoluir de FIFO simples para priorização dinâmica baseada em SLA do cliente, tipo de pedido e capacidade disponível.

### Trechos Anotados

**Seção de Contexto e Motivação:**
> "O sistema atual processa 45K pedidos/hora em ordem de chegada. Clientes Enterprise (12% dos pedidos, 68% da receita) têm SLA de 30min mas frequentemente esperam 2h+ em picos. O custo de violação de SLA é R$15K/mês em créditos."

*Anotação: Conecta decisão técnica a impacto financeiro. O leitor entende imediatamente por que essa mudança importa.*

**Seção de Alternativas Consideradas:**

> "Alternativa 1: Filas separadas por tier — Simples, mas causa starvation de clientes básicos em picos. Alternativa 2: Priority queue com aging — Resolve starvation mas não considera capacidade. Alternativa 3 (escolhida): Weighted Fair Queuing adaptado — Garante SLA sem starvation, complexidade moderada. Alternativa 4: ML-based scheduling — Over-engineering para o volume atual, considerar em >200K pedidos/hora."

*Anotação: Cada alternativa tem prós, contras e motivo de rejeição. A alternativa escolhida não é apresentada como óbvia — o leitor entende o raciocínio.*

**Seção de Diagramas:**
> Diagrama de sequência mostrando fluxo do pedido desde ingresso até conclusão, com pontos de decisão de prioridade claramente marcados. Diagrama de componentes mostrando PriorityCalculator, QueueManager, WorkerPool e CapacityMonitor com interfaces entre eles.

*Anotação: Diagramas focados na interação entre componentes, não na implementação interna. O nível de abstração é adequado para revisão de design.*

### O Que Torna Este Design Doc Excelente
- Motivação financeira clara — não é exercício técnico sem contexto
- Alternativas genuínas com análise honesta (não strawman)
- Diagramas no nível correto de abstração
- Seção de riscos com mitigações específicas
- Métricas de sucesso técnico (latência p50, p99, throughput)
- Plano de teste de carga antes do deploy

---

## Exemplo 2: Design Doc da Camada de Cache Distribuído

### Contexto
Aplicação com latência crescente conforme a base de usuários cresceu de 50K para 500K MAU. Necessidade de camada de cache distribuído sem invalidação inconsistente.

### Trechos Anotados

**Seção de Invariantes:**
> "Invariante 1: Leitura após escrita pelo mesmo usuário SEMPRE retorna o valor mais recente (read-your-writes). Invariante 2: Cache miss nunca deve retornar erro — deve fazer fallback transparente ao banco. Invariante 3: TTL máximo de 5 minutos para dados financeiros, sem exceção."

*Anotação: Invariantes são as regras que nunca podem ser violadas. Defini-las no design doc cria um contrato claro para implementação e testes.*

**Seção de Failure Modes:**
> "Modo de falha 1: Redis primary down — Sentinel promove replica em <30s, aplicação retenta com circuit breaker. Modo de falha 2: Rede particionada entre app e Redis — App opera sem cache (degradação graceful, latência sobe ~3x). Modo de falha 3: Cache poisoning por bug — Flush total via admin endpoint + alerta automático se hit rate cai abaixo de 20%."

*Anotação: Cada modo de falha tem comportamento esperado definido. Isso permite testar resiliência antes do deploy.*

### O Que Torna Este Design Doc Excelente
- Invariantes explícitos que guiam implementação e testes
- Failure modes com comportamento esperado definido
- Benchmark comparativo (com cache vs. sem cache vs. cache local)
- Cálculo de custo de infraestrutura incluído
- Diagrama de invalidação de cache em cenários distribuídos
- Seção de observabilidade (métricas, logs, alertas)

---

## Exemplo 3: Design Doc do Pipeline de Processamento de Eventos

### Contexto
Migração de processamento síncrono de eventos de auditoria para pipeline assíncrono com garantia de entrega e ordenação por entidade.

### Trechos Anotados

**Seção de Garantias:**
> "Garantia de entrega: at-least-once. Consumidores DEVEM ser idempotentes. Garantia de ordem: por partition key (entity_id). Eventos da mesma entidade são processados em ordem. Eventos de entidades diferentes podem ser processados fora de ordem. Latência máxima end-to-end: 5 segundos no p99 em operação normal."

*Anotação: Garantias de sistema distribuído explícitas. Não assume que o leitor sabe as implicações — descreve o que cada garantia significa na prática.*

**Seção de Schema Evolution:**
> "Eventos usam schema registry com compatibilidade backward. Novos campos são sempre opcionais. Campos removidos passam por período de deprecação de 90 dias. Versão do schema incluída no header do evento para roteamento."

*Anotação: Evolução de schema planejada desde o design, não como afterthought. Isso previne breaking changes em produção.*

### O Que Torna Este Design Doc Excelente
- Garantias de sistema distribuído documentadas formalmente
- Schema evolution planejada como cidadão de primeira classe
- Dead letter queue com estratégia de reprocessamento
- Cálculo de throughput e sizing de infraestrutura
- Plano de migração de eventos históricos
- Runbook operacional incluído como apêndice

---

## Lições Aplicáveis

### Para o Pre-Programming Squad

1. **Exija alternativas reais** — Design docs com apenas a solução escolhida são argumentos, não análises. Mínimo de 3 alternativas genuínas.

2. **Valide invariantes** — Se o design doc não tem invariantes, o Agente de Arquitetura deve solicitá-los. Invariantes são a base dos testes.

3. **Verifique failure modes** — Todo design doc deve responder: "o que acontece quando X falha?" para cada componente externo.

4. **Confirme nível de abstração** — Design docs muito detalhados viram código; muito abstratos não guiam implementação. O nível correto descreve interações entre componentes.

5. **Busque métricas de sucesso técnico** — Além das métricas de produto, deve haver métricas técnicas (latência, throughput, error rate) com valores-alvo.

6. **Valide custo de infraestrutura** — Soluções elegantes que custam 10x mais que alternativas simples precisam de justificativa explícita.

7. **Exija plano de observabilidade** — Se não está no design doc, não será implementado. Métricas, logs estruturados e alertas devem ser planejados.
