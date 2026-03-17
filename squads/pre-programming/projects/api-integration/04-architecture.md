# Integração de API — Fase 04: Arquitetura

## Objetivo da Fase

Desenhar a arquitetura da camada de integração, incluindo client HTTP, tratamento de erros, circuit breaker, cache e adaptadores de dados.

## Agentes Envolvidos

- **Agente de Arquitetura** (líder da fase) — Desenha camada de integração
- **Agente de Riscos** — Avalia resiliência da arquitetura proposta

## Inputs

- Contratos formalizados (Fase 03)
- Estratégia de comunicação e retry (Fase 03)
- SLA e limites da API (Fase 01)
- Arquitetura atual do sistema

## Atividades

1. **Desenhar camada de integração** — Componentes: HTTP Client, Serializer/Deserializer, Adapter (traduz modelo externo para interno), Error Handler, Circuit Breaker.
2. **Definir circuit breaker** — Thresholds: quantas falhas para abrir circuito, tempo de recovery, comportamento em half-open. Evitar cascata de falhas.
3. **Planejar cache de respostas** — Quais endpoints são cacheáveis? TTL por endpoint? Invalidação manual? Cache miss behavior?
4. **Definir observabilidade** — Métricas: latência por endpoint, taxa de erro, circuit breaker state, rate limit consumption. Alertas: latência p99 > threshold, error rate > threshold.
5. **Projetar idempotência** — Para operações de escrita: como garantir que retry não cause efeito duplicado? Idempotency key? Deduplicação?
6. **Avaliar rate limiting** — Taxa de consumo projetada vs. rate limit da API. Buffer de segurança (usar no máximo 80% do limite). Queue para suavizar picos.
7. **Planejar versionamento do client** — Como o client se adapta a mudanças na API? Feature flags por versão? Header de versão?

## Outputs

- Diagrama de arquitetura da camada de integração
- Configuração de circuit breaker (thresholds e comportamentos)
- Estratégia de cache por endpoint
- Plano de observabilidade (métricas, logs, alertas)
- Design de idempotência para operações de escrita
- Projeção de consumo de rate limit
- Estratégia de versionamento do client

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Circuit breaker | Configuração de thresholds e fallback definida | Sim |
| Observabilidade | Métricas e alertas por endpoint planejados | Sim |
| Idempotência | Operações de escrita são idempotentes | Sim |
| Rate limiting | Projeção de consumo dentro de 80% do limite | Sim |
| Cache planejado | Endpoints cacheáveis identificados com TTL | Condicional |

## Próxima Fase

→ [05-risks.md](./05-risks.md) — Riscos específicos de integração com API externa
