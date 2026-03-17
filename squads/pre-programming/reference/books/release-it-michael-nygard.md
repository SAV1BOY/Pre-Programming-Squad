# Release It!

## Informações Gerais

- **Titulo:** Release It! Design and Deploy Production-Ready Software
- **Autor:** Michael T. Nygard
- **Ano:** 2007 (1a edicao), 2018 (2a edicao)

## Tese Central

A maioria dos problemas de software nao e causada por bugs logicos, mas por falhas na interacao entre componentes em producao. Sistemas de producao enfrentam carga inesperada, falhas de rede, timeouts, cascatas de falhas e comportamentos emergentes que nenhum teste unitario detecta. Design para producao requer padroes de estabilidade, capacidade e seguranca que devem ser planejados antes da implementacao.

## Conceitos-Chave para Pre-Programacao

### 1. Antipadroes de Estabilidade
- **Integration Points:** Cada ponto de integracao e um ponto de falha. Sockets, HTTP calls, database connections — todos podem travar, retornar lixo ou nunca responder.
- **Chain Reactions:** Falha em um no sobrecarrega os restantes, causando cascata.
- **Cascading Failures:** Falha em um servico propaga para seus dependentes.
- **Users / Unbalanced Capacities:** Usuarios reais se comportam diferente de testes de carga.
- **Blocked Threads:** O assassino silencioso — threads bloqueadas por I/O que esgotam pools.
- **Self-Denial Attacks:** O proprio sistema gera carga que o derruba (ex: cache stampede).

### 2. Padroes de Estabilidade
- **Timeouts:** Toda chamada externa deve ter timeout. Sem excecao.
- **Circuit Breaker:** Detectar falhas em dependencias e falhar rapido em vez de propagar.
- **Bulkheads:** Isolar componentes para que falha em um nao derrube todos.
- **Steady State:** Sistemas devem auto-gerenciar seus recursos (logs, cache, conexoes).
- **Fail Fast:** Se uma operacao vai falhar, falhar imediatamente em vez de desperdicar recursos.
- **Handshaking:** Permitir que servicos sinalizem quando estao sobrecarregados.
- **Shed Load:** Rejeitar requisicoes quando sobrecarregado, em vez de degradar para todos.

### 3. Padroes de Deploy e Operacao
- Blue-green deployment, canary releases, feature flags.
- Zero-downtime deployment como requisito, nao luxo.
- Rollback como operacao de primeira classe.

### 4. Transparencia e Observabilidade
- Logs estruturados, metricas, health checks, tracing distribuido.
- Se voce nao pode ver o que o sistema esta fazendo, nao pode opera-lo.

### 5. Design para Falha
Aceitar que falhas vao ocorrer e projetar o sistema para funcionar apesar delas (graceful degradation), nao para evita-las completamente.

## Como Aplicar no Squad

### Na Analise de Pontos de Integracao
- Mapear todos os integration points do sistema proposto.
- Para cada integracao, definir: timeout, retry policy, circuit breaker, fallback.
- Identificar potenciais cascading failures e definir bulkheads.
- Documentar modos de falha para cada dependencia externa.

### Na Definicao de Requisitos Nao-Funcionais
- Exigir que design docs incluam estrategia de falha para cada componente.
- Definir SLAs de disponibilidade com base em analise de pontos de falha.
- Planejar graceful degradation para cenarios de falha parcial.
- Especificar capacidade e limites de cada componente.

### Na Avaliacao de Design Docs
- Verificar presenca de timeouts em todas as chamadas externas.
- Confirmar circuit breakers para dependencias criticas.
- Avaliar estrategia de deploy (blue-green, canary, feature flags).
- Validar que observabilidade esta planejada (logs, metricas, traces).

### Nos Criterios de Readiness
- "Todos os integration points tem timeouts e circuit breakers definidos?"
- "Modos de falha estao documentados para cada dependencia?"
- "Estrategia de graceful degradation esta definida?"
- "Estrategia de deploy e rollback esta definida?"
- "Observabilidade (logs, metricas, traces) esta planejada?"

## Citacoes Importantes

> "The only sure thing about production is that it will surprise you."

> "Every integration point will eventually fail in some way, and you need to be prepared for that failure."

> "Use timeouts. Use timeouts. Use timeouts."

> "The worst thing a system can do is to fail slowly."

> "Design for production means designing for the real world, not the test lab."

> "Cynical software expects bad things to happen and is never surprised when they do."

## Relacao com Outros Livros de Referencia

- **DDIA (Kleppmann):** Kleppmann fornece a teoria de sistemas distribuidos; Nygard fornece os padroes praticos de estabilidade.
- **SRE (Google):** Ambos focam em confiabilidade de producao, com perspectivas complementares.
- **Continuous Delivery:** Nygard complementa com padroes de deploy em producao.
