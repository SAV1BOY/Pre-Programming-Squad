# Kleppmann: Data-Intensive Design

## Título e Propósito

Framework baseado no trabalho de **Martin Kleppmann** (*Designing Data-Intensive Applications*). A tese central: **a maioria dos sistemas modernos são data-intensive, não compute-intensive** — e as decisões mais importantes são sobre como dados são armazenados, consultados, replicados e processados. O propósito é aplicar esse pensamento na pré-programação para projetar sistemas a partir dos dados, não do código.

## Quando Usar

- Em decisões de escolha de banco de dados e modelo de dados
- Ao projetar sistemas que processam, armazenam ou transmitem grandes volumes de dados
- Em decisões sobre consistência, disponibilidade e particionamento (CAP)
- Ao projetar pipelines de dados, event streaming ou ETL
- Quando performance de leitura/escrita é requisito crítico

## Conceitos-Chave

1. **Confiabilidade, Escalabilidade, Manutenibilidade**: Os três pilares de um bom sistema data-intensive. Toda decisão deve ser avaliada contra esses três.
2. **Modelo de Dados**: Relacional, documento, grafo, time-series — cada um otimizado para padrões de acesso diferentes. Escolha errada = performance ruim.
3. **Consistência vs. Disponibilidade**: Em sistemas distribuídos, não se pode ter tudo. Entenda o teorema CAP e onde seu sistema se posiciona.
4. **Stream Processing vs. Batch**: Processamento em tempo real vs. em lotes. A escolha afeta latência, complexidade e custo.
5. **Encoding e Evolução**: Formato dos dados (JSON, Protobuf, Avro) e como o schema evolui sem quebrar consumidores existentes.

## Processo / Passos

### Passo 1 — Caracterizar os Dados
Volume (quanto), velocidade (com que frequência muda), variedade (quantos formatos), veracidade (quão confiável).

### Passo 2 — Mapear Padrões de Acesso
Leitura-heavy ou escrita-heavy? Queries simples ou analíticas complexas? Acesso por chave ou por range? Isso determina a escolha de storage.

### Passo 3 — Decidir Modelo de Consistência
Precisa de consistência forte (ACID) ou eventual consistency é aceitável? Onde no sistema cada modelo se aplica?

### Passo 4 — Projetar para Evolução
Como o schema muda sem downtime? Como novos campos são adicionados sem quebrar leitores existentes?

### Passo 5 — Avaliar Trade-offs de Storage
Para cada tipo de dado, avalie: relacional, documento, key-value, time-series. Não existe "melhor banco" — existe o melhor para o caso de uso.

## Perguntas de Ativação

- "Qual é o padrão de acesso predominante: leitura ou escrita?"
- "Precisamos de consistência forte ou eventual é aceitável?"
- "Quanto dado teremos em 1 ano? Em 3 anos? A solução escala?"
- "Como o schema evolui quando requisitos mudam?"
- "Estamos escolhendo tecnologia por familiaridade ou por adequação ao problema?"

## Output Esperado

Decisões de storage documentadas com justificativa baseada em padrões de acesso, modelo de consistência definido, estratégia de evolução de schema, estimativas de volume.

## Armadilhas Comuns

1. **Uma tecnologia para tudo**: Usar o mesmo banco para transações, analytics e busca. Cada caso pode precisar de storage diferente.
2. **Ignorar evolução de schema**: Projetar como se o formato dos dados nunca fosse mudar.
3. **Consistência onde não precisa**: Exigir ACID para dados que toleram eventual consistency desperdiça performance.
4. **Eventual consistency onde não pode**: Usar eventual consistency para saldo financeiro é receita para fraude.
5. **Volume subestimado**: Schema que funciona com 10GB mas é impraticável com 10TB.
