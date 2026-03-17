# Exemplos Icônicos de ADRs (Architecture Decision Records)

## Objetivo

Documentar exemplos anotados de ADRs excepcionais que demonstram como registrar decisões arquiteturais de forma que sejam úteis no presente e no futuro. ADRs são a memória institucional do time de engenharia.

---

## Exemplo 1: ADR-027 — Adoção de Event Sourcing para o Domínio de Pedidos

### Contexto
Sistema de e-commerce onde auditoria completa de alterações em pedidos era requisito regulatório e o modelo CRUD estava gerando inconsistências em cenários de concorrência.

### Trecho Anotado Completo

> **Status:** Aceito
>
> **Contexto:**
> O domínio de pedidos sofre ~150 alterações de estado/segundo em pico. O modelo atual (CRUD com tabela de auditoria) apresenta 3 problemas: (1) Tabela de auditoria perde eventos em alta concorrência (race condition no trigger), (2) Reconstruir estado histórico requer joins complexos com latência >10s, (3) Regulação LGPD exige trilha de auditoria imutável que o modelo atual não garante.
>
> **Decisão:**
> Adotar Event Sourcing para o aggregate de Pedidos. Eventos são a fonte de verdade. Estado atual é projeção materializada. Utilizar EventStoreDB como event store.
>
> **Alternativas rejeitadas:**
> - CRUD + CDC (Change Data Capture): Resolve auditoria mas não concorrência. Adiciona complexidade de infraestrutura (Debezium + Kafka) sem resolver o problema fundamental.
> - Temporal tables (SQL Server): Resolve auditoria mas lock em temporal tables é o próprio gargalo de concorrência. Vendor lock-in no SQL Server.
> - Audit log application-level: Mais simples, mas não garante consistência entre estado e log em falhas parciais.
>
> **Consequências:**
> - Positivas: Auditoria imutável por design, replay de eventos para debug, possibilidade de projeções otimizadas por caso de uso.
> - Negativas: Curva de aprendizado do time (~3 semanas estimadas), complexidade de eventual consistency nas projeções, necessidade de lidar com schema evolution de eventos.
> - Riscos: Event store como single point of failure — mitigado com replicação multi-região.

*Anotação: Este ADR é excelente porque o contexto quantifica o problema (150 alterações/s, race condition, >10s), as alternativas são genuínas com motivos reais de rejeição, e as consequências são honestas sobre custos e riscos.*

### O Que Torna Este ADR Excelente
- Status claro (Aceito/Rejeitado/Superseded)
- Contexto com números e problemas específicos, não genéricos
- Alternativas rejeitadas com motivos técnicos concretos
- Consequências divididas em positivas, negativas e riscos
- Referência a requisitos regulatórios que motivaram a decisão
- Escopo limitado a um aggregate, não ao sistema inteiro

---

## Exemplo 2: ADR-041 — Migração de Monolito para Módulos Independentes (Modular Monolith)

### Contexto
Time de 25 devs trabalhando em monolito Rails com deploys conflitantes e tempo de build de 45 minutos. Pressão para microsserviços mas infraestrutura e maturidade do time não suportavam.

### Trecho Anotado Completo

> **Status:** Aceito
>
> **Contexto:**
> Deploy frequency caiu de 8/dia para 2/dia nos últimos 6 meses. Causa raiz: conflitos em código compartilhado (especialmente models/ e services/). 73% dos PRs tocam mais de 3 módulos de negócio. Build de CI leva 45min, impedindo fast feedback. Time solicitou microsserviços mas: (1) não temos plataforma de orquestração madura, (2) observabilidade distribuída não está implementada, (3) 60% do time não tem experiência com sistemas distribuídos.
>
> **Decisão:**
> Adotar Modular Monolith como passo intermediário. Cada módulo de negócio (Pedidos, Catálogo, Pagamentos, Usuários) terá: namespace próprio, banco de dados lógico separado (schemas), interface pública explícita, testes independentes. Comunicação entre módulos via interface Ruby, não chamadas diretas a classes internas.
>
> **Alternativas rejeitadas:**
> - Microsserviços imediatos: Time não tem maturidade operacional. Custo de infraestrutura estimado 4x maior. Risco de "distributed monolith" é alto.
> - Manter monolito + convenções: Tentado nos últimos 8 meses, não funcionou. Convenções não são enforcement.
> - Strangler fig pattern: Viável mas requer infraestrutura de roteamento que não temos. Considerado para fase 2.
>
> **Consequências:**
> - Positivas: Deploy independente por módulo (CI de 45min → ~12min por módulo), encapsulamento forçado por interface, caminho natural para microsserviços futuros.
> - Negativas: Refactor de 2-3 meses para extrair primeiro módulo, necessidade de ferramentas de lint para enforcement de boundaries.
> - Métricas de sucesso: Deploy frequency > 6/dia em 3 meses, build time < 15min por módulo, zero imports cross-module não autorizados.

*Anotação: A honestidade sobre a maturidade do time é rara e valiosa. Em vez de seguir hype (microsserviços), a decisão reconhece limitações reais e escolhe um caminho pragmático com métricas de validação.*

### O Que Torna Este ADR Excelente
- Admite que a solução "desejada" (microsserviços) não é viável e explica por quê
- Referencia tentativa anterior que falhou (convenções por 8 meses)
- Métricas de sucesso concretas com prazo
- Plano de evolução implícito (modular monolith → microsserviços)
- Considera maturidade do time como fator de decisão

---

## Exemplo 3: ADR-058 — Escolha de PostgreSQL sobre DynamoDB para Novo Serviço de Inventário

### Contexto
Novo serviço de controle de inventário em tempo real. Pressão para usar DynamoDB "porque é serverless" versus PostgreSQL que o time já domina.

### Trecho Anotado Completo

> **Status:** Aceito
>
> **Contexto:**
> Serviço de inventário precisa suportar: (1) ~500 escritas/segundo de atualizações de estoque, (2) queries complexas para relatórios (JOINs entre inventário, SKUs, warehouses), (3) transações ACID para reserva de estoque (decrement + reservation atômicos), (4) integração com sistema de relatórios que usa SQL.
>
> **Decisão:**
> Usar PostgreSQL 15 com connection pooling (PgBouncer). Particionamento por warehouse_id para distribuir carga. Read replicas para relatórios.
>
> **Alternativas rejeitadas:**
> - DynamoDB: Atende escrita mas queries complexas requerem GSIs caros e limitados. Transações multi-item limitadas a 100 items. Time precisaria aprender novo modelo de dados. Custo estimado 3x maior para o padrão de acesso (muitas reads complexas).
> - DynamoDB + Aurora para reads: Complexidade de sincronização entre dois datastores supera benefícios para nosso volume.
> - CockroachDB: Distribuído por default mas overkill para single-region. Custo de licença enterprise para features necessárias.
>
> **Consequências:**
> - Positivas: Time já domina PostgreSQL (0 curva de aprendizado), queries complexas nativas, ecossistema maduro de tooling, custo previsível.
> - Negativas: Scaling vertical tem limite (~10K writes/s sem particionamento). Necessidade de gerenciar infraestrutura (vs serverless DynamoDB).
> - Trigger de revisão: Se writes ultrapassarem 5K/s consistentemente por 30 dias, reavaliar esta decisão.

*Anotação: O "trigger de revisão" é uma prática avançada. A decisão não é permanente — ela define condições sob as quais deve ser reexaminada. Isso evita tanto premature optimization quanto lock-in por inércia.*

### O Que Torna Este ADR Excelente
- Padrões de acesso definidos antes da escolha de tecnologia
- Análise de custo comparativa (não apenas técnica)
- Reconhece limites da decisão com trigger de revisão
- Não cai na armadilha de "nova tecnologia = melhor"
- Valida familiaridade do time como critério legítimo

---

## Lições Aplicáveis

### Para o Pre-Programming Squad

1. **Todo projeto deve gerar pelo menos um ADR** — Decisões arquiteturais não documentadas são decisões perdidas. O Agente de Arquitetura deve produzir ADRs.

2. **Exija alternativas reais** — ADR com apenas a solução escolhida não é ADR, é justificativa post-hoc. Mínimo de 2 alternativas genuínas.

3. **Inclua consequências negativas** — ADRs que só listam benefícios são propaganda. Consequências negativas honestas constroem confiança e preparam o time.

4. **Defina triggers de revisão** — Decisões devem ter condições sob as quais são reexaminadas. Isso evita tanto over-engineering quanto inércia.

5. **Considere maturidade do time** — A melhor solução técnica que o time não consegue operar é a pior solução prática. Esse critério é legítimo.

6. **Numere e versione ADRs** — ADRs devem ter ID único e status. ADR superseded deve referenciar o ADR que a substitui.

7. **Conecte ADRs a contexto de negócio** — ADRs puramente técnicos perdem relevância. O "por que agora" deve incluir pressão de negócio ou risco.
