# Template: Plano de Performance

## Título
Performance Plan — Planejamento e Metas de Performance

## Propósito
Definir requisitos de performance, estratégias de otimização, cenários de teste e metas mensuráveis antes da implementação, evitando gargalos descobertos tarde demais.

## Quando Usar
- Após definição de arquitetura e antes de implementar.
- Quando há requisitos não-funcionais de performance críticos.
- Em sistemas com alta volumetria ou baixa tolerância a latência.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Responsável | `[nome]` |
| Data | `[YYYY-MM-DD]` |

### 2. Metas de Performance
| Métrica | Valor Alvo | Valor Aceitável | Inaceitável | Método de Medição |
|---------|-----------|----------------|-------------|------------------|
| Latência p50 | `[ms]` | `[ms]` | `[ms]` | `[ferramenta]` |
| Latência p95 | `[ms]` | `[ms]` | `[ms]` | `[ferramenta]` |
| Latência p99 | `[ms]` | `[ms]` | `[ms]` | `[ferramenta]` |
| Throughput | `[req/s]` | `[req/s]` | `[req/s]` | `[ferramenta]` |
| Tempo de resposta da página | `[s]` | `[s]` | `[s]` | `[Lighthouse/WebPageTest]` |
| Uso de memória | `[MB]` | `[MB]` | `[MB]` | `[ferramenta]` |

### 3. Cenários de Carga
| Cenário | Usuários Simultâneos | Requests/s | Duração | Padrão |
|---------|---------------------|-----------|---------|--------|
| Normal | `[N]` | `[req/s]` | `[contínuo]` | `[padrão típico]` |
| Pico | `[N]` | `[req/s]` | `[minutos]` | `[horário de pico]` |
| Stress | `[N]` | `[req/s]` | `[minutos]` | `[acima do esperado]` |
| Spike | `[N]` | `[req/s]` | `[segundos]` | `[explosão súbita]` |

### 4. Endpoints Críticos
| Endpoint | Latência Alvo | Volume Esperado | Estratégia de Otimização |
|----------|-------------|----------------|------------------------|
| `[endpoint]` | `[ms]` | `[req/s]` | `[cache/index/async/etc.]` |

### 5. Estratégias de Otimização
| Estratégia | Componente | Ganho Esperado | Complexidade |
|-----------|-----------|---------------|-------------|
| `[Cache em Redis]` | `[API de listagem]` | `[reduzir latência em 80%]` | `[Média]` |
| `[Índice composto]` | `[Query de busca]` | `[reduzir tempo de query em 90%]` | `[Baixa]` |
| `[CDN]` | `[Assets estáticos]` | `[reduzir TTFB em 70%]` | `[Baixa]` |

### 6. Plano de Testes de Performance
| Teste | Ferramenta | Ambiente | Dados | Critério de Sucesso |
|-------|-----------|----------|-------|---------------------|
| `[Load test]` | `[k6/Gatling/JMeter]` | `[staging]` | `[volume realista]` | `[metas atingidas]` |

### 7. Baseline e Benchmarks
| Métrica | Baseline Atual | Meta | Benchmark da Indústria |
|---------|---------------|------|----------------------|
| `[métrica]` | `[valor atual]` | `[valor alvo]` | `[referência]` |

### 8. Plano de Ação
| Ação | Impacto | Esforço | Prioridade | Responsável |
|------|---------|---------|-----------|-------------|
| `[ação]` | `[Alto/Médio/Baixo]` | `[Alto/Médio/Baixo]` | `[1-5]` | `[nome]` |

## Exemplo de Preenchimento

### 2. Metas de Performance
| Métrica | Alvo | Aceitável | Inaceitável | Medição |
|---------|------|-----------|-------------|---------|
| Latência p50 | 100ms | 200ms | >500ms | Datadog APM |
| Latência p99 | 500ms | 1000ms | >3000ms | Datadog APM |
| Throughput | 1000 req/s | 500 req/s | <200 req/s | k6 load test |
| TTFB | 200ms | 500ms | >1000ms | Lighthouse |

## Dicas de Qualidade
- **Medir antes de otimizar:** Sem baseline, não há como saber se melhorou.
- **Otimize o que importa:** Foque nos endpoints mais usados e mais lentos.
- **Teste com dados realistas:** 100 registros não simula um banco com 10 milhões.
- **Performance é contínua:** Não é um teste único. Monitore continuamente.
- **Não otimize prematuramente:** Resolva problemas reais, não hipotéticos.
