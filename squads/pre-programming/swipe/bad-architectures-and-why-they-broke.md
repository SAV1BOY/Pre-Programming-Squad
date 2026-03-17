# Arquiteturas Ruins e Por Que Quebraram — Exemplos Anotados

## Introdução

Arquiteturas não falham de uma vez — elas degradam gradualmente até um ponto de ruptura. Estudar arquiteturas que quebraram revela padrões de decisões que pareciam razoáveis no momento mas levaram a sistemas frágeis, lentos ou impossíveis de manter. Este documento analisa falhas arquiteturais reais com foco em como poderiam ter sido prevenidas na fase de pré-programação.

---

## Exemplo 1 — O Monolito Distribuído

### A Arquitetura

> 12 "microsserviços" que compartilham o mesmo banco de dados PostgreSQL. Todos os serviços fazem JOIN direto nas tabelas dos outros. Deploy é feito em conjunto porque mudança de schema em um afeta todos. Comunicação síncrona via REST entre todos os serviços para operações simples.

### Por que quebrou

- **Banco compartilhado**: Elimina o principal benefício de microsserviços — independência de deploy e escala. Um ALTER TABLE bloqueia todos os serviços.
- **Acoplamento temporal**: Chamadas síncronas em cadeia. Se o serviço C está lento, A e B também ficam lentos. Latência é aditiva.
- **Resultado**: Complexidade de microsserviços com nenhum benefício. Deploy leva 2 horas (antes levava 20 minutos no monolito). Incidentes cascateiam entre serviços.

### O que a pré-programação deveria ter feito

- Definir bounded contexts antes de definir serviços
- Exigir que cada serviço tenha seu próprio banco
- Questionar: "Se não podemos deployar independentemente, por que separar?"

---

## Exemplo 2 — Event Sourcing para CRUD Simples

### A Arquitetura

> Sistema de gerenciamento de catálogo de produtos implementado com Event Sourcing + CQRS. Cada alteração de produto gera um evento. Estado reconstruído via replay. Read models projetados para cada query diferente. Event store com 500M de eventos após 6 meses.

### Por que quebrou

- **Complexidade desproporcional**: O domínio era CRUD puro — produtos com nome, preço, descrição. Nenhuma necessidade de auditoria temporal ou reconstrução de estado.
- **Performance de replay**: Reconstruir estado de produtos com muitas alterações levava segundos. Snapshots resolvem parcialmente, mas adicionam mais complexidade.
- **Event store inchado**: 500M de eventos em 6 meses para 50K produtos. Custos de storage e manutenção explodiram.
- **Resultado**: Time de 4 devs gastava 30% do tempo mantendo a infraestrutura de event sourcing em vez de entregar features.

### O que a pré-programação deveria ter feito

- Perguntar: "Quais requisitos justificam Event Sourcing?" (auditoria? temporal queries? event-driven?)
- Avaliar complexidade vs benefício: Se é CRUD, use CRUD
- Aplicar YAGNI: não implementar padrões "para o futuro"

---

## Exemplo 3 — API Gateway como Gargalo Único

### A Arquitetura

> Todos os requests de todos os clientes passam por um único API Gateway que faz: autenticação, rate limiting, transformação de payload, orquestração de chamadas para múltiplos backends, caching, logging, compressão, e validação de schema. Gateway customizado em Java com 80K linhas de código.

### Por que quebrou

- **Single point of failure**: Gateway caiu, todo o sistema caiu. 100% de downtime.
- **Complexidade concentrada**: 80K linhas de lógica de negócio disfarçada de infraestrutura. Bugs no Gateway afetam todos os endpoints.
- **Bottleneck de deploy**: Qualquer mudança no Gateway requer deploy completo. Time de plataforma vira gargalo de todas as features.
- **Resultado**: Gateway tinha 99.7% de uptime — mas como todo request passava por ele, o sistema inteiro tinha 99.7% de uptime. Em escala, isso significava 26 horas de downtime por ano.

### O que a pré-programação deveria ter feito

- Separar preocupações: Gateway só para cross-cutting (auth, rate limit). Lógica nos serviços
- Avaliar alternativas gerenciadas (Kong, Envoy, AWS API Gateway)
- Definir SLA do Gateway como requisito antes de implementar

---

## Exemplo 4 — Microservices Prematuros

### A Arquitetura

> Startup com 3 desenvolvedores iniciou com 8 microsserviços separados, cada um com seu banco de dados, mensageria Kafka para comunicação assíncrona e Kubernetes para orquestração. O produto tinha 200 usuários.

### Por que quebrou

- **Overhead operacional**: 3 devs gastavam mais tempo mantendo infra do que desenvolvendo produto
- **Custo de cloud**: Kubernetes, Kafka, 8 bancos de dados, monitoring para 8 serviços — custo mensal de R$15K para servir 200 usuários
- **Velocidade de desenvolvimento**: Feature simples que cruzava 3 serviços levava 1 semana. No monolito, levaria 1 dia.
- **Resultado**: Startup ficou sem runway antes de validar product-market fit. Reescreveram como monolito em 2 meses, o que deveria ter sido o ponto de partida.

### O que a pré-programação deveria ter feito

- Avaliar escala atual vs escala projetada
- Aplicar a regra: "Comece com monolito, extraia serviços quando doer"
- Calcular custo operacional da arquitetura proposta

---

## Lições Extraídas

1. **Complexidade tem custo**: Toda abstração arquitetural tem overhead. O benefício deve justificar o custo
2. **Microsserviços não são default**: Monolito bem estruturado é superior a microsserviços mal implementados
3. **Banco compartilhado anula microsserviços**: Se os serviços compartilham o banco, são um monolito distribuído
4. **Evite single points of failure**: Qualquer componente por onde passa 100% do tráfego é um SPOF
5. **Adeque ao contexto**: Arquitetura de startup de 3 pessoas é diferente de empresa de 300
6. **Event Sourcing não é para tudo**: Reserve para domínios que realmente precisam de histórico temporal
7. **Questione "por que não mais simples?"**: A resposta deve ser concreta, não "porque é melhor prática"
