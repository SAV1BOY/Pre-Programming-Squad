# Projeto de Agente IA — Fase 07: Readiness

## Objetivo da Fase

Avaliar prontidão do agente para lançamento com critérios rigorosos em segurança e qualidade. Agentes de IA em produção são difíceis de controlar — readiness deve ser alto.

## Agentes Envolvidos

- **Agente de Readiness** (líder da fase) — Avalia prontidão com pesos de IA
- **Agente de Riscos** — Confirma guardrails e red team
- **Agente de Testes** — Apresenta scores de evals

## Inputs

- Artefatos das fases 01-06
- Scores de evals (qualidade, segurança, red team)
- Modelo de readiness com pesos para "AI Agent Project"

## Atividades

1. **Avaliar dimensões com pesos adaptados:**
   - Clareza de Requisitos (peso: 15%) — Capacidades e limites explícitos
   - Solidez Arquitetural (peso: 15%) — RAG, tools, guardrails técnicos
   - Cobertura de Riscos (peso: 25%) — Alucinação, injection, bias, custo
   - Design de Testes (peso: 30%) — Evals são a defesa principal
   - Plano de Rollout (peso: 10%) — Lançamento gradual com monitoramento
   - Completude de Handoff (peso: 5%)
2. **Verificar scores de evals** — Accuracy >= threshold, red team blocking rate >= 95%, PII leakage = 0%, latency p99 dentro do SLA.
3. **Confirmar guardrails ativos** — Todos os guardrails testados e funcionando: input filtering, output filtering, cost cap, escalação.
4. **Validar observabilidade** — Dashboard de qualidade em tempo real, alertas de degradação, logs de interação.

## Outputs

- Scorecard de readiness com pesos de IA
- Relatório de scores de evals
- Confirmação de guardrails ativos
- Decisão go/no-go (threshold >= 7.5 para agentes de IA)

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Score ponderado | >= 7.5 (threshold alto por risco de IA) | Sim |
| Evals de segurança | Red team >= 95% bloqueado, PII leakage = 0% | Sim |
| Evals de qualidade | Accuracy acima do threshold definido por cenário | Sim |
| Guardrails ativos | Todos os guardrails testados e funcionando | Sim |
| Observabilidade | Dashboard e alertas de degradação ativos | Sim |

## Próxima Fase

→ [08-handoff.md](./08-handoff.md) — Lançamento gradual do agente
