# System Design Interview

## Informações Gerais

- **Titulo:** System Design Interview: An Insider's Guide (Volumes 1 e 2)
- **Autor:** Alex Xu
- **Ano:** 2020 (Vol. 1), 2022 (Vol. 2)

## Tese Central

O design de sistemas em larga escala segue um framework sistematico: entender requisitos, estimar escala, propor design de alto nivel, detalhar componentes criticos, identificar gargalos e propor mitigacoes. Cada decisao de design deve ser justificada por numeros concretos (back-of-the-envelope estimation) e fundamentada em trade-offs explicitos.

## Conceitos-Chave para Pre-Programacao

### 1. Framework de 4 Passos
1. **Entender os requisitos:** Funcionais e nao-funcionais. Perguntar antes de projetar.
2. **Estimativa de envelope:** Quantificar usuarios, QPS, storage, bandwidth.
3. **Design de alto nivel:** Diagrama de componentes, fluxos de dados, APIs.
4. **Deep dive:** Detalhar componentes criticos, identificar gargalos.

Na pre-programacao, esse framework estrutura a analise de qualquer problema de design.

### 2. Back-of-the-Envelope Estimation
Estimar ordens de grandeza: latencia de operacoes, tamanho de dados, throughput de rede. Numeros de referencia: leitura de memoria ~100ns, SSD random read ~100us, rede 1Gbps, disco sequencial ~30MB/s. Na pre-programacao, estimativas de envelope evitam over-engineering e under-engineering.

### 3. Padroes Recorrentes de System Design
- **Rate limiting:** Token bucket, leaky bucket, sliding window.
- **Consistent hashing:** Distribuicao uniforme de carga entre nos.
- **URL shortener / ID generator:** Snowflake, UUID, sequence.
- **Cache:** Cache-aside, read-through, write-through, write-behind.
- **Message queues:** Desacoplamento, buffering, ordenacao.
- **CDN e load balancing:** Distribuicao geografica, health checks.

### 4. Escalabilidade Horizontal vs. Vertical
Quando escalar verticalmente (mais poder em um servidor) vs. horizontalmente (mais servidores). Implicacoes para estado, sessao, persistencia. Na pre-programacao, a estrategia de escala deve ser definida antecipadamente.

### 5. CAP Theorem e PACELC
Na presenca de particao de rede, escolher entre Consistencia e Disponibilidade. PACELC estende: mesmo sem particao, ha trade-off entre Latencia e Consistencia. Na pre-programacao, explicitar a escolha.

### 6. Data Partitioning e Sharding
Estrategias de sharding: por range, por hash, por diretorio. Problemas: hotspots, resharding, joins cross-shard. Na pre-programacao, definir estrategia de particionamento quando o volume justifica.

## Como Aplicar no Squad

### Na Estimativa de Escala
- Para cada projeto, fazer estimativas de envelope: usuarios, QPS, storage, bandwidth.
- Usar numeros de referencia para validar premissas de performance.
- Documentar premissas de escala no design doc com horizontes temporais (6 meses, 1 ano, 3 anos).

### Na Definicao de Arquitetura
- Aplicar o framework de 4 passos como estrutura para design docs.
- Identificar componentes criticos para deep dive.
- Documentar padroes aplicados (cache, rate limiting, sharding) com justificativa.
- Incluir diagrama de alto nivel e diagramas de sequencia para fluxos criticos.

### Na Avaliacao de Trade-offs
- Explicitar escolhas CAP/PACELC para cada servico.
- Documentar trade-offs de cache (consistencia vs. latencia).
- Justificar escolha de comunicacao sincrona vs. assincrona.

### Nos Criterios de Readiness
- "Estimativas de envelope foram calculadas e documentadas?"
- "Componentes criticos foram detalhados com deep dive?"
- "Estrategia de escalabilidade esta definida?"
- "Trade-offs CAP/PACELC estao explicitos?"

## Citacoes Importantes

> "The most important thing in system design is to ask the right questions before jumping to a solution."

> "Back-of-the-envelope estimation helps you get a good sense of which design will work and which won't."

> "There are no 'correct' answers in system design. There are only good trade-offs."

> "The key to system design is understanding requirements deeply enough to make the right trade-offs."

## Relacao com Outros Livros de Referencia

- **DDIA (Kleppmann):** Kleppmann fornece a fundamentacao teorica profunda; Xu fornece a aplicacao pratica e frameworks.
- **Fundamentals of Software Architecture:** Richards/Ford focam em estilos arquiteturais; Xu foca em padroes de infraestrutura e escala.
- **SRE (Google):** Princípios de confiabilidade e estimativas de capacidade alinham-se diretamente.
