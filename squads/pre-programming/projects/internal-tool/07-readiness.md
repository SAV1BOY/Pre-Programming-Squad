# Ferramenta Interna — Fase 07: Readiness

## Objetivo da Fase

Avaliar prontidão para lançamento interno com critérios proporcionais à criticidade e vida útil da ferramenta.

## Agentes Envolvidos

- **Agente de Readiness** (líder da fase) — Avaliação de prontidão
- **Agente de Riscos** — Confirma proteções ativas

## Inputs

- Artefatos das fases 01-06
- Feedback do UAT
- Modelo de readiness com pesos para "Internal Tool"

## Atividades

1. **Avaliar dimensões com pesos adaptados:**
   - Clareza de Requisitos (peso: 20%)
   - Solidez Arquitetural (peso: 10%) — Ferramenta interna não precisa de arquitetura robusta
   - Cobertura de Riscos (peso: 30%) — Riscos de acesso a produção são críticos
   - Design de Testes (peso: 20%)
   - Plano de Rollout (peso: 10%)
   - Completude de Handoff (peso: 10%)
2. **Checklist de segurança** — Autenticação funciona, autorização correta, dados sensíveis protegidos, audit trail ativo.
3. **Verificar documentação operacional** — A ferramenta tem documentação mínima de uso? FAQ para operadores?
4. **Confirmar owner e manutenção** — Pessoa responsável definida, plano de manutenção para ferramenta permanente.

## Outputs

- Scorecard de readiness
- Checklist de segurança preenchido
- Decisão go/no-go (threshold >= 6.0 para ferramenta interna)
- Documentação de uso pronta

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Score ponderado | >= 6.0 (threshold menor que produtos externos) | Sim |
| Segurança | Autenticação e proteções ativas | Sim |
| Documentação | Instruções de uso disponíveis | Sim |
| Owner definido | Responsável por manutenção identificado | Sim |

## Próxima Fase

→ [08-handoff.md](./08-handoff.md) — Lançamento para usuários internos
