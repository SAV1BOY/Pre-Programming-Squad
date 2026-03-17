# Projeto de Automação — Fase 07: Readiness

## Objetivo da Fase

Avaliar prontidão para ativação da automação com foco em confiabilidade de regras, observabilidade e capacidade de fallback manual.

## Agentes Envolvidos

- **Agente de Readiness** (líder da fase) — Avalia prontidão
- **Agente de Riscos** — Confirma circuit breakers e monitoramento

## Inputs

- Artefatos das fases 01-06
- Resultado de replay com dados históricos
- Modelo de readiness com pesos para "Automation Project"

## Atividades

1. **Avaliar dimensões com pesos adaptados:**
   - Clareza de Requisitos (peso: 20%) — Regras de negócio explícitas
   - Solidez Arquitetural (peso: 15%) — Orquestração e integrações
   - Cobertura de Riscos (peso: 25%) — Falha silenciosa e amplificação de erros
   - Design de Testes (peso: 25%) — Regras testadas e replay validado
   - Plano de Rollout (peso: 10%) — Ativação gradual
   - Completude de Handoff (peso: 5%)
2. **Validar replay histórico** — Automação reproduz resultados do processo manual com taxa de concordância >= 98%
3. **Confirmar observabilidade** — Dashboard, alertas e logs configurados e testados
4. **Verificar fallback manual** — Processo manual documentado, praticado e acessível

## Outputs

- Scorecard de readiness
- Taxa de concordância do replay histórico
- Confirmação de observabilidade ativa
- Decisão go/no-go (threshold >= 7.0)

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Score ponderado | >= 7.0 | Sim |
| Replay >= 98% | Taxa de concordância com processo manual | Sim |
| Observabilidade ativa | Dashboard e alertas funcionando | Sim |
| Fallback pronto | Processo manual documentado e praticado | Sim |
| Circuit breakers ativos | Automação para em condições anômalas | Sim |

## Próxima Fase

→ [08-handoff.md](./08-handoff.md) — Ativação da automação em produção
