# Nova Feature — Fase 07: Readiness

## Objetivo da Fase

Avaliar se todos os artefatos de pré-programação estão completos e com qualidade suficiente para que o time de desenvolvimento possa iniciar a implementação com confiança.

## Agentes Envolvidos

- **Agente de Readiness** (líder da fase) — Avalia prontidão multidimensional
- **Todos os agentes** — Revisam seus respectivos artefatos

## Inputs

- Todos os artefatos das fases anteriores (01-06)
- Modelo de readiness com pesos para "Nova Feature"
- Histórico de scores de projetos similares

## Atividades

1. **Avaliar cada dimensão** — Scoring de 0-10 para cada dimensão usando rubricas operacionais:
   - Clareza de Requisitos (peso: 30%)
   - Solidez Arquitetural (peso: 25%)
   - Cobertura de Riscos (peso: 15%)
   - Design de Testes (peso: 15%)
   - Plano de Rollout (peso: 10%)
   - Completude de Handoff (peso: 5%)
2. **Calcular score ponderado** — Score final = soma de (score x peso) por dimensão
3. **Verificar dimensões bloqueantes** — Nenhuma dimensão pode estar abaixo de 5.0 independente do score ponderado
4. **Comparar com histórico** — Verificar se score está compatível com projetos similares. Investigar outliers.
5. **Identificar gaps** — Listar itens que precisam ser resolvidos antes do handoff
6. **Decisão de go/no-go** — Score >= 7.0 com nenhuma dimensão < 5.0: aprovado para handoff

## Outputs

- Scorecard de readiness com score por dimensão e ponderado
- Lista de gaps identificados (se houver)
- Decisão de go/no-go com justificativa
- Recomendações para o time de desenvolvimento

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Score ponderado | >= 7.0 para nova feature | Sim |
| Dimensões mínimas | Nenhuma dimensão abaixo de 5.0 | Sim |
| Gaps resolvidos | Todos os gaps bloqueantes resolvidos | Sim |
| Comparação histórica | Score compatível com projetos similares (+/- 1.5) | Informativo |

## Próxima Fase

→ [08-handoff.md](./08-handoff.md) — Entrega formal dos artefatos ao time de desenvolvimento
