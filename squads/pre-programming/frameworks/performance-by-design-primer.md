# Performance by Design Primer

## Título e Propósito

O **Performance by Design Primer** é um framework para incorporar considerações de performance na fase de design, antes de escrever código. O propósito é evitar o padrão "construir, descobrir que é lento, otimizar às pressas" — porque problemas de performance nascidos em decisões arquiteturais são ordens de magnitude mais caros de corrigir do que aqueles nascidos em implementação.

## Quando Usar

- Durante decisões arquiteturais que afetam latência, throughput ou uso de recursos
- Ao projetar APIs, consultas de dados e fluxos de processamento
- Quando há requisitos não-funcionais de performance (SLA de latência, throughput mínimo)
- Ao dimensionar infraestrutura e escolher tecnologias
- Quando o sistema precisa escalar para volumes significativamente maiores

## Conceitos-Chave

1. **Latência**: Tempo para processar uma única operação. Medida em percentis (p50, p95, p99), não em média.
2. **Throughput**: Número de operações por unidade de tempo. Limitado pelo gargalo mais lento do pipeline.
3. **Lei de Amdahl**: O speedup de um sistema é limitado pela porção que não pode ser paralelizada.
4. **Localidade de Dados**: Acessar dados perto de onde são processados é ordens de magnitude mais rápido que acessar remotamente.
5. **Back-of-Envelope Calculation**: Estimativas rápidas usando ordens de magnitude para validar viabilidade antes de implementar.
6. **Gargalo (Bottleneck)**: O componente mais lento que limita a performance do sistema inteiro. Otimizar qualquer outra coisa é desperdício.

## Processo / Passos

### Passo 1 — Definir Requisitos de Performance
Quantifique: latência máxima aceitável (p95), throughput necessário, volume de dados, número de usuários concorrentes.

### Passo 2 — Fazer Cálculos de Envelope
Antes de projetar, calcule: quantos bytes por request? Quantos requests por segundo? Quanto storage por dia/mês/ano? Os números fazem sentido com a infra disponível?

### Passo 3 — Identificar o Caminho Crítico
Qual é o fluxo mais importante e mais sensível a latência? Esse fluxo recebe atenção especial de performance.

### Passo 4 — Mapear Gargalos Potenciais
Para o caminho crítico, identifique: chamadas de rede, consultas ao banco, operações de I/O, processamento pesado. Cada um é um gargalo potencial.

### Passo 5 — Projetar para Performance
Para cada gargalo potencial, decida na fase de design: cache, batch, async, denormalização, particionamento, índices, CDN.

### Passo 6 — Definir Budget de Latência
Distribua o budget de latência total entre os componentes do caminho crítico. Exemplo: 200ms total = 50ms API + 80ms DB + 30ms cache + 40ms rede.

### Passo 7 — Planejar Validação
Defina: benchmark de performance como parte do CI, testes de carga antes do launch, monitoramento de SLIs de performance em produção.

## Perguntas de Ativação

- "Quantos requests por segundo esse endpoint vai receber no pico?"
- "Qual é o volume de dados por dia/mês/ano? Cabe na infra planejada?"
- "Onde está o gargalo nesse fluxo? Rede, CPU, I/O ou memória?"
- "Estamos fazendo N+1 queries? Chamadas sequenciais que poderiam ser paralelas?"
- "Esse cálculo precisa acontecer em tempo real ou pode ser pré-computado?"
- "O que acontece quando o volume dobrar? E quando decuplicar?"

## Output Esperado

```
REQUISITOS DE PERFORMANCE:
- Latência: p95 < 200ms para API principal
- Throughput: 500 req/s no pico
- Dados: ~10GB/dia de ingestão

CÁLCULOS DE ENVELOPE:
- 500 req/s × 2KB avg = 1MB/s de bandwidth
- 10GB/dia ÷ 86400 = ~115KB/s de ingestão
- 10GB/dia × 365 × 3 anos = ~11TB de storage

CAMINHO CRÍTICO: Busca de produtos → API → Cache → DB → Serialização → Response

BUDGET DE LATÊNCIA:
| Componente | Budget | Estratégia |
|---|---|---|
| API processing | 20ms | Código otimizado, sem bloqueio |
| Cache lookup | 5ms | Redis local |
| DB query | 80ms | Índices compostos, query otimizada |
| Serialização | 10ms | Formato eficiente |
| Rede (CDN) | 50ms | CDN com edge caching |
| **Total** | **165ms** | **Margem: 35ms** |

GARGALOS E MITIGAÇÕES:
- DB: índices compostos, read replica para queries analíticas
- Cache: Redis com TTL de 5min para catálogo
- Rede: CDN para assets estáticos e respostas cacheáveis
```

## Armadilhas Comuns

1. **Otimizar sem medir**: Assumir onde está o gargalo em vez de medir. "O banco deve ser lento" — será mesmo?
2. **Otimização prematura**: Otimizar tudo antes de ter dados de uso real. Mas design para performance não é otimização prematura.
3. **Médias enganosas**: Latência média de 100ms pode esconder p99 de 5 segundos. Sempre use percentis.
4. **Ignorar volume futuro**: Projetar para o volume de hoje sem considerar crescimento. O sistema precisa escalar com o negócio.
5. **Cache sem invalidação**: Cache resolve performance mas cria problemas de consistência se a invalidação não for projetada.
6. **Microbenchmarks sem contexto**: Comparar performance de frameworks em benchmarks que não refletem o uso real do sistema.
