# Refatoração de Legado — Fase 07: Readiness

## Objetivo da Fase

Avaliar prontidão para iniciar refatoração com threshold mais alto que projetos greenfield, dado o risco inerente de mexer em sistema legado.

## Agentes Envolvidos

- **Agente de Readiness** (líder da fase) — Avalia prontidão com pesos de legado
- **Todos os agentes** — Revisam artefatos de suas fases

## Inputs

- Todos os artefatos das fases 01-06
- Modelo de readiness com pesos para "Legacy Refactor"
- Histórico de refactorings anteriores (sucessos e falhas)

## Atividades

1. **Avaliar cada dimensão** — Scoring com pesos adaptados para legado:
   - Clareza de Requisitos (peso: 15%) — Em legado, requisitos são frequentemente implícitos no código
   - Solidez Arquitetural (peso: 25%) — Arquitetura-alvo e plano de transição
   - Cobertura de Riscos (peso: 25%) — Peso mais alto que feature nova por risco inerente
   - Design de Testes (peso: 25%) — Testes de caracterização e equivalência são críticos
   - Plano de Rollout (peso: 5%) — Fases incrementais com rollback
   - Completude de Handoff (peso: 5%)
2. **Verificar dimensões bloqueantes** — Para legado, Testes e Riscos devem estar >= 6.0
3. **Validar que testes de caracterização existem** — Sem testes de caracterização, refactoring não começa
4. **Confirmar conhecedores disponíveis** — Pelo menos 1 pessoa com conhecimento do legado disponível durante as primeiras semanas
5. **Verificar timebox acordado** — Refactoring sem timebox é refactoring infinito

## Outputs

- Scorecard de readiness com pesos de legado
- Decisão go/no-go (threshold >= 7.5 para legado)
- Lista de pré-condições obrigatórias confirmadas
- Recomendações específicas para o time

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Score ponderado | >= 7.5 (threshold mais alto que feature nova) | Sim |
| Testes dimensão | Score de Testes >= 6.0 | Sim |
| Riscos dimensão | Score de Riscos >= 6.0 | Sim |
| Testes de caracterização | Suite existente e executável | Sim |
| Conhecedor disponível | Pessoa com contexto histórico acessível | Sim |
| Timebox acordado | Prazo e critérios de "good enough" definidos | Sim |

## Próxima Fase

→ [08-handoff.md](./08-handoff.md) — Entrega do plano de refatoração ao time
