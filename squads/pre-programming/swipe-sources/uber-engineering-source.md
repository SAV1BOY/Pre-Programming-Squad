# Uber Engineering — Fonte de Referência

## Fonte

**Organização**: Uber
**Prática**: Engenharia em escala extrema, migração de sistemas e design para resiliência
**Referências Principais**:
- Blog de engenharia da Uber (eng.uber.com)
- "Domain-Oriented Microservice Architecture" — DOMA framework
- Publicações sobre migração de monolito para microsserviços em escala

## URL de Referência

- https://www.uber.com/blog/engineering/
- https://www.uber.com/blog/microservice-architecture/
- https://www.uber.com/blog/domain-oriented-microservice-architecture/

---

## O que Aprender

### DOMA — Domain-Oriented Microservice Architecture

A Uber evoluiu de monolito para microsserviços e depois para DOMA, reconhecendo que microsserviços sem organização geram caos. DOMA introduz:

- **Domains**: Agrupamento lógico de microsserviços por domínio de negócio
- **Layers**: Hierarquia de serviços (infra, domínio, produto, edge)
- **Gateways**: Ponto de entrada único por domínio, encapsulando complexidade interna
- **Extensions**: Mecanismo para customização sem modificar serviços core

### Lições da Migração em Escala

A Uber migrou de um monolito Python para milhares de microsserviços em Go/Java. Lições documentadas:

- Migrações graduais com strangler fig pattern
- Dual-write como padrão de transição
- Investimento massivo em observabilidade antes de migrar
- Testes de carga com tráfego real duplicado (shadow traffic)

### Design para Falha

Com milhões de viagens por dia, a Uber projeta sistemas assumindo que falhas acontecerão:

- Circuit breakers em todas as chamadas entre serviços
- Fallbacks e degradação graceful em cascata
- Chaos engineering para validar resiliência

---

## Práticas Relevantes para Pré-Programação

1. **Organização por domínio, não por tecnologia**: Ao planejar a arquitetura, organizar serviços por domínio de negócio (pagamentos, viagens, usuários), não por camada técnica (API, worker, database). Isso produz bounded contexts naturais.

2. **Gateways de domínio**: Para projetos com múltiplos serviços, definir um gateway por domínio que encapsula a complexidade interna. Times externos interagem com o gateway, não com serviços internos.

3. **Plano de migração com strangler fig**: Para substituição de sistemas legados, planejar migração gradual onde o novo sistema "estrangula" o antigo funcionalidade por funcionalidade.

4. **Observabilidade antes da migração**: Antes de qualquer migração, garantir que monitoring, logging e tracing estão implementados. Não é possível migrar com segurança o que não se pode observar.

5. **Shadow traffic para validação**: Antes de migrar tráfego real, duplicar requests para o novo sistema sem impactar usuários. Comparar resultados entre sistemas antigo e novo.

6. **Design for failure como padrão**: Em todo design doc, seção obrigatória: "O que acontece quando X falha?" para cada dependência externa. Circuit breaker, retry, fallback devem estar no design, não no código de emergência.

7. **Layers como princípio organizacional**: Classificar cada componente em infra/domínio/produto/edge ajuda a definir contratos e responsabilidades claras.
