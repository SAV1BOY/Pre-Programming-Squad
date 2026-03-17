# Observability by Design

## Título e Propósito

O **Observability by Design** é um framework para incorporar observabilidade como requisito de design desde o início, não como feature de operações adicionada depois. O propósito é garantir que o sistema, uma vez em produção, possa ser compreendido, diagnosticado e monitorado sem precisar de redesign — porque sistemas que não podem ser observados não podem ser operados de forma confiável.

## Quando Usar

- Durante design de arquitetura de qualquer sistema que irá para produção
- Quando incidentes são difíceis de diagnosticar por falta de visibilidade
- Ao projetar novos serviços, APIs ou integrações
- Antes de definir SLOs e SLAs
- Quando a equipe reclama que não consegue entender o que o sistema está fazendo

## Conceitos-Chave

1. **Três Pilares**: Logs (eventos discretos), Métricas (valores numéricos ao longo do tempo), Traces (rastreamento de requisições entre serviços).
2. **Observabilidade vs. Monitoramento**: Monitoramento verifica condições conhecidas. Observabilidade permite investigar problemas desconhecidos.
3. **Cardinalidade**: O número de valores únicos de uma dimensão. Alta cardinalidade (ex: user_id) é essencial para debug mas cara para armazenar.
4. **SLI (Service Level Indicator)**: Métrica que indica a saúde do serviço do ponto de vista do usuário.
5. **Contexto Propagado**: Informações (trace ID, user ID, request ID) que acompanham uma requisição através de todos os serviços.

## Processo / Passos

### Passo 1 — Definir o que Precisa Ser Observável
Para cada componente, pergunte: "Quando der problema em produção, que perguntas vou querer responder?" Projete a instrumentação para responder essas perguntas.

### Passo 2 — Definir SLIs
Identifique os indicadores que refletem a experiência do usuário: latência, taxa de erro, throughput, disponibilidade.

### Passo 3 — Projetar Logging Estruturado
Defina: formato de logs (JSON estruturado), campos obrigatórios (timestamp, trace_id, level, service, message), níveis de log e quando usar cada um.

### Passo 4 — Projetar Métricas
Defina métricas por componente: RED (Rate, Errors, Duration) para serviços, USE (Utilization, Saturation, Errors) para recursos.

### Passo 5 — Projetar Tracing Distribuído
Defina: como trace IDs são gerados e propagados, quais spans são criados, quais atributos são registrados em cada span.

### Passo 6 — Definir Dashboards e Alertas
Projete dashboards que respondam às perguntas do Passo 1. Defina alertas com thresholds baseados em SLIs.

### Passo 7 — Incluir no Definition of Done
Adicione "instrumentação implementada e verificada" como critério de done para toda feature.

## Perguntas de Ativação

- "Se esse serviço ficasse lento às 3h da manhã, como descobriríamos a causa?"
- "Conseguimos rastrear uma requisição do usuário final até o banco de dados?"
- "Quais perguntas vamos querer fazer ao sistema em produção?"
- "Temos métricas que refletem a experiência real do usuário?"
- "Se adicionarmos um novo serviço, o tracing vai funcionar automaticamente?"
- "Os logs têm informação suficiente para debugar sem reproduzir o problema?"

## Output Esperado

| Componente | SLIs | Logs | Métricas | Traces | Dashboard | Alertas |
|---|---|---|---|---|---|---|
| API Gateway | Latência p99, Taxa de erro 5xx | Request/Response, erros, auth | RED: req/s, erros/s, latência | Span: ingress | Overview de tráfego | p99 > 500ms, erro > 1% |
| Serviço de Pedidos | Tempo de processamento, taxa de falha | Eventos de estado, erros de integração | Pedidos/min, falhas/min, duração | Span: processamento | Funil de pedidos | Taxa de falha > 2% |
| Banco de Dados | Query latency p95, conexões ativas | Slow queries, deadlocks | Conexões, query time, throughput | Span: query | Performance DB | Conexões > 80%, slow queries > 10/min |

## Armadilhas Comuns

1. **Observabilidade como afterthought**: "Depois a gente adiciona logs" resulta em instrumentação insuficiente ou inconsistente.
2. **Logging sem estrutura**: Logs em texto livre são impossíveis de consultar em escala. Use JSON estruturado.
3. **Métricas de vaidade**: Medir coisas fáceis (uptime do servidor) em vez de relevantes (experiência do usuário).
4. **Alertas demais**: Alert fatigue — tantos alertas que todos são ignorados.
5. **Trace sem contexto**: Spans sem atributos relevantes não ajudam no diagnóstico.
6. **Custo não planejado**: Observabilidade gera dados. Dados custam armazenamento. Planeje retenção e amostragem.
