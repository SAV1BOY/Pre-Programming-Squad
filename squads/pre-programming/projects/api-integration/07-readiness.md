# Integração de API — Fase 07: Readiness

## Objetivo da Fase

Avaliar prontidão para implementação da integração com foco especial em contratos, resiliência e acesso ao provedor.

## Agentes Envolvidos

- **Agente de Readiness** (líder da fase) — Avalia prontidão com pesos de integração
- **Todos os agentes** — Revisam artefatos de suas fases

## Inputs

- Todos os artefatos das fases 01-06
- Modelo de readiness com pesos para "API Integration"
- Confirmação de acesso à sandbox e credenciais

## Atividades

1. **Avaliar cada dimensão** — Scoring com pesos adaptados para integração:
   - Clareza de Requisitos (peso: 20%) — Contratos e mapeamentos definidos
   - Solidez Arquitetural (peso: 20%) — Resiliência e circuit breaker
   - Cobertura de Riscos (peso: 20%) — Indisponibilidade e breaking changes
   - Design de Testes (peso: 25%) — Testes de contrato e resiliência são críticos
   - Plano de Rollout (peso: 10%) — Deploy gradual com feature flag
   - Completude de Handoff (peso: 5%)
2. **Verificar pré-requisitos técnicos** — Credenciais de produção disponíveis? Rate limit de produção conhecido? Contato de suporte do provedor confirmado?
3. **Validar sandbox funcional** — Sandbox está acessível e reproduz comportamento de produção de forma confiável?
4. **Confirmar contratos estáveis** — A API não tem breaking changes planejadas durante o período de implementação?

## Outputs

- Scorecard de readiness para integração
- Checklist de pré-requisitos técnicos confirmados
- Decisão go/no-go (threshold >= 7.0)
- Recomendações específicas sobre resiliência

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Score ponderado | >= 7.0 | Sim |
| Credenciais disponíveis | Acesso a sandbox e produção confirmado | Sim |
| Contrato estável | Sem breaking changes planejadas no período | Sim |
| Testes dimensão | Score de Testes >= 6.0 | Sim |
| Suporte confirmado | Contato do provedor acessível | Sim |

## Próxima Fase

→ [08-handoff.md](./08-handoff.md) — Entrega do plano de integração ao time
