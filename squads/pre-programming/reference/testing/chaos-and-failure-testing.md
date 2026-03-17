# Chaos Engineering e Testes de Falha

## O que e Chaos Engineering

Chaos engineering e a disciplina de experimentar em sistemas distribuidos para construir confianca na capacidade do sistema de suportar condicoes turbulentas em producao. Em vez de esperar que falhas acontecam, injetamos falhas controladamente para descobrir fraquezas antes que afetem usuarios.

## Principios do Chaos Engineering

### 1. Construir uma Hipotese sobre o Comportamento Steady-State
Definir o que "normal" significa em termos de metricas observaveis (latencia, error rate, throughput). Essa e a baseline contra a qual medimos o impacto de falhas.

### 2. Variar Eventos do Mundo Real
Injetar falhas que realmente acontecem: servidores caem, rede particiona, disco enche, dependencias ficam lentas, DNS falha, certificados expiram.

### 3. Executar Experimentos em Producao
Idealmente, testar em producao porque ambientes de staging nao reproduzem a complexidade real. Comecar com blast radius pequeno (canary, % do trafego).

### 4. Automatizar e Executar Continuamente
Chaos experiments devem rodar automaticamente e continuamente, nao apenas uma vez. Sistemas degradam ao longo do tempo.

### 5. Minimizar o Blast Radius
Comecar pequeno. Ter kill switch. Monitorar continuamente. Parar se impacto excede o esperado.

## Tipos de Falhas para Testar

### Falhas de Infraestrutura
| Falha | Simulacao | Ferramenta |
|---|---|---|
| Servidor indisponivel | Terminar instancia/pod | Chaos Monkey, LitmusChaos |
| Disco cheio | Preencher filesystem | stress-ng, Gremlin |
| CPU saturada | CPU stress | stress-ng |
| Memoria esgotada | Memory pressure | stress-ng |

### Falhas de Rede
| Falha | Simulacao | Ferramenta |
|---|---|---|
| Latencia alta | Adicionar delay em pacotes | tc (traffic control), Toxiproxy |
| Perda de pacotes | Drop aleatorio de pacotes | tc, Pumba |
| Particao de rede | Bloquear trafego entre servicos | iptables, Chaos Mesh |
| DNS falha | Bloquear resolucao DNS | Chaos Mesh |

### Falhas de Dependencia
| Falha | Simulacao | Ferramenta |
|---|---|---|
| Banco de dados lento | Adicionar latencia em queries | Toxiproxy |
| API externa indisponivel | Bloquear chamadas HTTP | WireMock, Toxiproxy |
| Cache indisponivel | Parar Redis/Memcached | Docker stop, Chaos Mesh |
| Message broker lento | Adicionar latencia no broker | Toxiproxy |

### Falhas de Aplicacao
| Falha | Simulacao | Ferramenta |
|---|---|---|
| Memory leak | Alocacao crescente de memoria | Custom, Gremlin |
| Thread exhaustion | Bloquear threads | Custom |
| Exception storms | Injecao de excecoes | byteman, Chaos Monkey for Spring Boot |

## Chaos Engineering na Pre-Programacao

### Identificar Hipoteses de Resiliencia no Design Doc

Durante a pre-programacao, para cada componente e integracao, documentar:

```markdown
## Analise de Resiliencia

### Hipotese 1: Falha do Servico de Pagamento
**Cenario:** Servico de pagamento fica indisponivel por 5 minutos.
**Comportamento esperado:** Pedidos sao aceitos e enfileirados.
  Pagamento e processado quando servico retorna.
**Mecanismos:** Circuit breaker (fallback para fila), retry com backoff.
**Metrica de validacao:** Taxa de pedidos perdidos = 0.
**Quando testar:** Apos implementacao do circuit breaker.

### Hipotese 2: Latencia Alta no Banco de Dados
**Cenario:** Latencia de queries aumenta de 10ms para 2000ms.
**Comportamento esperado:** Timeouts acionam apos 500ms. Respostas
  parciais retornam dados do cache. Alerta dispara.
**Mecanismos:** Timeout 500ms, cache-aside com TTL de 5min, alerta.
**Metrica de validacao:** Latencia p99 do servico < 1000ms mesmo
  com banco degradado.
```

### Definir Game Days no Plano de Lancamento

```markdown
## Plano de Game Days

### Pre-lancamento (staging)
- [ ] Simular falha de cada dependencia externa individualmente.
- [ ] Simular falha simultanea de cache + banco (pior caso).
- [ ] Simular spike de trafego 3x acima do normal.

### Pos-lancamento (producao, blast radius controlado)
- [ ] Semana 2: Terminar uma instancia do servico em horario de pico.
- [ ] Semana 4: Adicionar 500ms de latencia na dependencia mais critica.
- [ ] Mensalmente: Chaos experiment automatizado aleatorio.
```

### Criterios de Readiness Relacionados a Resiliencia
- "Modos de falha de cada dependencia estao documentados?"
- "Mecanismos de resiliencia (timeout, circuit breaker, retry, fallback) estao definidos?"
- "Hipoteses de resiliencia estao documentadas para chaos testing?"
- "Game days estao planejados no cronograma de lancamento?"
- "Kill switches e rollback estao definidos?"

## Ferramentas de Chaos Engineering

### Netflix Chaos Monkey / Simian Army
Ferramenta original. Termina instancias aleatoriamente em producao. A "Simian Army" inclui Latency Monkey, Conformity Monkey, etc.

### Gremlin
Plataforma comercial de chaos engineering. Suporta multiplos tipos de ataque com UI amigavel e blast radius controlado.

### Chaos Mesh (CNCF)
Plataforma open-source para Kubernetes. Suporta pod failure, network chaos, I/O chaos, time chaos, stress testing.

### LitmusChaos (CNCF)
Framework de chaos engineering cloud-native para Kubernetes. Catálogo de experimentos pre-definidos.

### Toxiproxy (Shopify)
Proxy TCP para simular condicoes de rede adversas. Excelente para testes de integracao locais.

## Relacao com Outros Testes

| Tipo de Teste | Objetivo | Quando |
|---|---|---|
| Unitario | Logica correta | Desenvolvimento |
| Integracao | Componentes se comunicam | CI |
| E2E | Fluxos de negocio funcionam | CI/CD |
| Performance | Sistema suporta carga | Pre-lancamento |
| **Chaos** | **Sistema resiste a falhas** | **Pos-lancamento continuo** |
