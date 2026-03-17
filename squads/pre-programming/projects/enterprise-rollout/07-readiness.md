# Rollout Enterprise — Fase 07: Readiness

## Objetivo da Fase

Avaliar prontidão organizacional E técnica para rollout enterprise. Ambas devem estar prontas — tecnologia sem pessoas treinadas é inútil.

## Agentes Envolvidos

- **Agente de Readiness** (líder da fase) — Avalia prontidão bidimensional
- **Todos os agentes** — Revisam artefatos de suas fases

## Inputs

- Artefatos das fases 01-06
- Resultado de UAT e dry-runs
- Modelo de readiness com pesos para "Enterprise Rollout"
- Feedback de stakeholders e champions

## Atividades

1. **Avaliar readiness técnico** — Scoring com pesos adaptados:
   - Solidez Arquitetural (peso: 20%) — Coexistência e feature flags
   - Cobertura de Riscos (peso: 20%) — Rollback e compliance
   - Design de Testes (peso: 20%) — Migração, UAT, performance
   - Plano de Rollout (peso: 25%) — Faseamento com critérios
   - Completude de Handoff (peso: 15%) — Documentação e treinamento
2. **Avaliar readiness organizacional:**
   - Sponsor ativo e engajado?
   - Treinamento completo para fase 1?
   - Material de comunicação pronto?
   - Help desk preparado?
   - Champions mobilizados?
3. **Validar governance approvals** — Todas as aprovações necessárias obtidas (CAB, compliance, executivos)?
4. **Confirmar janela de rollout** — Sem conflitos com freeze periods, feriados ou outros projetos?

## Outputs

- Scorecard técnico e organizacional
- Checklist de governance approvals
- Confirmação de janela de rollout
- Decisão go/no-go (ambos scores >= 7.0)

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Score técnico | >= 7.0 | Sim |
| Score organizacional | >= 7.0 | Sim |
| Approvals obtidos | Todas as aprovações de governance | Sim |
| Treinamento fase 1 | Completo para usuários da primeira fase | Sim |
| Comunicação pronta | Material de comunicação revisado e aprovado | Sim |

## Próxima Fase

→ [08-handoff.md](./08-handoff.md) — Execução do rollout enterprise fase 1
