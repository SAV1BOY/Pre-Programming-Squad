# Auxiliares de Árvore de Decisão (Decision Tree Helpers)

## Propósito
Fornecer modelos de árvores de decisão para escolhas técnicas comuns na fase de pré-programação, ajudando equipes a tomar decisões estruturadas e documentáveis sobre arquitetura, tecnologia e abordagens de implementação.

## Fórmulas e Modelos

### Modelo de Avaliação de Decisão

```
Score_Opcao = sum(Ci * Pi * Ni)

Onde:
  Ci = Score do critério i (1-5)
  Pi = Peso do critério i (0-1, soma = 1)
  Ni = Fator de normalização (1 se favorável, -1 se desfavorável)
```

### Árvore 1: Monolito vs. Microsserviços

```
INÍCIO
  |
  +-- Equipe > 15 pessoas?
  |     SIM --> Considerar microsserviços
  |     |        +-- Domínios independentes?
  |     |        |     SIM --> Microsserviços por domínio
  |     |        |     NÃO --> Monolito modular
  |     |        +-- Deploy independente necessário?
  |     |              SIM --> Microsserviços
  |     |              NÃO --> Monolito modular
  |     NÃO --> Monolito
  |              +-- Escala > 10k req/s em parte do sistema?
  |                    SIM --> Monolito + serviço extraído
  |                    NÃO --> Monolito simples
```

### Árvore 2: SQL vs. NoSQL

```
INÍCIO
  |
  +-- Dados têm estrutura fixa e relacional?
  |     SIM --> SQL (PostgreSQL, MySQL)
  |     |        +-- Volume > 1TB?
  |     |        |     SIM --> PostgreSQL com particionamento
  |     |        |     NÃO --> PostgreSQL padrão
  |     NÃO
  |     +-- Dados são documentos flexíveis?
  |     |     SIM --> Document Store (MongoDB)
  |     +-- Dados são chave-valor com alta velocidade?
  |     |     SIM --> Key-Value (Redis, DynamoDB)
  |     +-- Dados são séries temporais?
  |     |     SIM --> TimeSeries DB (InfluxDB, TimescaleDB)
  |     +-- Dados são grafos com relações complexas?
  |           SIM --> Graph DB (Neo4j)
```

### Árvore 3: Comunicação Síncrona vs. Assíncrona

```
INÍCIO
  |
  +-- O chamador precisa da resposta imediatamente?
  |     SIM --> Síncrono (REST/gRPC)
  |     |        +-- Latência < 100ms necessária?
  |     |        |     SIM --> gRPC
  |     |        |     NÃO --> REST
  |     NÃO --> Assíncrono
  |              +-- Ordem de processamento importa?
  |              |     SIM --> Fila com ordenação (Kafka)
  |              |     NÃO --> Fila simples (RabbitMQ/SQS)
  |              +-- Múltiplos consumidores?
  |                    SIM --> Pub/Sub (Kafka/SNS)
  |                    NÃO --> Fila ponto-a-ponto
```

### Árvore 4: Estratégia de Cache

```
INÍCIO
  |
  +-- Dados mudam com que frequência?
  |     Raramente (> 1h) --> Cache longo (TTL 1-24h)
  |     Frequentemente (< 1min) --> Cache curto ou sem cache
  |     Moderadamente --> Cache com invalidação
  |
  +-- Consistência forte é necessária?
  |     SIM --> Cache-aside com invalidação por evento
  |     NÃO --> Cache com TTL + stale-while-revalidate
  |
  +-- Escala?
        Local (1 instância) --> Cache em memória (in-process)
        Distribuído --> Redis/Memcached
```

## Como Usar

1. Identificar a decisão técnica a ser tomada
2. Localizar a árvore de decisão correspondente
3. Percorrer as perguntas respondendo com dados do projeto
4. Documentar o caminho percorrido e a decisão resultante
5. Registrar como ADR com referência à árvore utilizada

## Inputs e Outputs

### Inputs
- Pergunta de decisão técnica
- Contexto do projeto (tamanho da equipe, volume de dados, SLAs)
- Restrições técnicas e organizacionais
- Requisitos não-funcionais relevantes

### Outputs
- Recomendação de decisão com justificativa
- Caminho percorrido na árvore documentado
- Critérios avaliados e seus valores
- Riscos da escolha identificados
- ADR gerado automaticamente

## Exemplos

### Exemplo: Decisão SQL vs. NoSQL para Catálogo de Produtos
```
Contexto:
  - Catálogo com 500k produtos
  - Atributos variáveis por categoria (roupas vs. eletrônicos)
  - Busca textual importante
  - Consistência necessária para preços e estoque

Percurso na árvore:
  1. "Dados têm estrutura fixa?" -> Parcialmente (atributos variáveis)
  2. "Dados são documentos flexíveis?" -> SIM para catálogo

Decisão: Abordagem híbrida
  - PostgreSQL para dados transacionais (pedidos, estoque, preços)
  - Elasticsearch para busca e catálogo (documentos flexíveis)
  - Sincronização via CDC (Change Data Capture)

ADR: ADR-0012-estrategia-persistencia-catalogo
```
