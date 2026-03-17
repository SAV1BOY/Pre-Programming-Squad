# Standard para Pré-check de Performance

## Propósito

Avaliar se o design proposto atende aos requisitos de performance antes da implementação. Identifica gargalos potenciais, valida premissas de capacidade e define metas mensuráveis que serão verificadas durante e após a implementação.

## Escopo

Projetos que envolvam: endpoints com SLA de latência, processamento de alto volume, operações batch, integrações com sistemas de alta demanda, ou mudanças em caminhos críticos (checkout, login, busca).

## Definições

| Termo | Definição |
|---|---|
| Latência | Tempo de resposta de uma operação (medido em p50, p95, p99) |
| Throughput | Volume de operações por unidade de tempo (RPS, mensagens/segundo) |
| Saturação | Percentual de utilização de um recurso (CPU, memória, conexões, I/O) |
| SLA | Service Level Agreement — compromisso de nível de serviço |
| SLO | Service Level Objective — meta interna de nível de serviço |
| Headroom | Margem entre capacidade atual e limite do sistema |

## Processo

### 1. Definir Metas de Performance

Coletar e documentar metas para cada caminho crítico:

| Caminho | Latência p50 | Latência p99 | Throughput | Disponibilidade |
|---|---|---|---|---|
| [Ex: POST /checkout] | < 200ms | < 500ms | 100 RPS | 99.9% |
| [Ex: GET /search] | < 100ms | < 300ms | 500 RPS | 99.9% |

**Fontes das metas:**
- SLAs contratuais com clientes
- Requisitos não-funcionais do escopo
- Benchmarks do sistema atual (baseline)
- Expectativas de produto (ex: "busca deve ser instantânea")

### 2. Análise de Capacidade

Para cada componente do design:

**Banco de Dados:**
- Volume de dados esperado em 6 e 12 meses
- Padrão de acesso (read-heavy, write-heavy, mixed)
- Queries mais frequentes com estimativa de custo (EXPLAIN)
- Índices necessários e impacto em escritas
- Connection pool sizing (conexões necessárias vs. disponíveis)

**Serviço/API:**
- Tráfego esperado (RPS médio, pico, sazonalidade)
- Recursos por request (CPU, memória, I/O)
- Dependências externas e sua latência
- Concorrência esperada (requests simultâneos)

**Infraestrutura:**
- Sizing de instâncias/pods (CPU, memória)
- Auto-scaling configuração (min, max, trigger)
- Rede (bandwidth, latência inter-serviço)
- Storage (IOPS necessários, tipo de disco)

**Cache:**
- Dados cacheáveis identificados
- Estratégia de invalidação
- Hit rate esperado
- Sizing de memória

### 3. Identificação de Gargalos

Analisar o caminho de cada request crítico e identificar pontos de estrangulamento:

- Chamadas síncronas a serviços externos (latência adicionada)
- Queries N+1 (multiplicação de queries por registro)
- Locks de banco (contenção em operações concorrentes)
- Serialização/deserialização de payloads grandes
- Falta de paginação em listagens
- Processamento síncrono que poderia ser assíncrono

### 4. Recomendações

Para cada gargalo identificado:

```
### Gargalo [N] — [Descrição]
- **Localização:** [Componente, endpoint, query]
- **Impacto estimado:** [Quanto de latência/throughput é afetado]
- **Recomendação:** [Ação técnica concreta]
- **Esforço:** [Estimativa de implementação]
- **Prioridade:** [Bloqueante / Pré-lançamento / Pós-lançamento]
```

### 5. Definir Plano de Validação

- Quais testes de carga executar e com quais cenários
- Ferramenta recomendada (k6, Locust, JMeter)
- Ambiente de teste (staging com sizing similar a produção)
- Métricas a coletar durante o teste
- Critérios de aprovação/reprovação do teste

## Critérios de Qualidade

- Metas de performance definidas para todo caminho crítico
- Análise de capacidade cobre banco, serviço, infra e cache
- Gargalos identificados com recomendação concreta
- Plano de validação definido com critérios objetivos
- Baseline do sistema atual documentado (quando aplicável)
- Sizing de infraestrutura estimado e justificado

## Responsáveis

| Papel | Responsabilidade |
|---|---|
| Membro do squad | Executar análise, documentar achados e recomendações |
| Tech Lead | Validar premissas de capacidade, revisar sizing |
| SRE/Infra | Fornecer dados de capacidade atual, validar sizing |
| Autor da proposta | Ajustar design conforme recomendações |

## Referências

- Standard de Arquitetura: `docs/architecture-review-standard.md`
- Standard de Design de Testes: `docs/test-design-standard.md`
- Standard de Go/No-Go: `docs/go-no-go-standard.md`
