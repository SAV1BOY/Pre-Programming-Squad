# Refatoração de Legado — Fase 05: Riscos

## Objetivo da Fase

Identificar riscos específicos de refatoração de legado — aqueles que não existem em projetos greenfield: dependências ocultas, lógica não documentada, Chesterton's fence.

## Agentes Envolvidos

- **Agente de Riscos** (líder da fase) — Identifica riscos de legado
- **Agente de Arquitetura** — Valida viabilidade das mitigações
- **Agente de Requisitos** — Verifica riscos de lógica de negócio perdida

## Inputs

- Mapa de dependências multi-camada (Fase 02)
- Inventário de lógica de negócio no código (Fase 02)
- Plano de transição (Fase 04)
- Archive de falhas de legacy-impact

## Atividades

1. **Avaliar risco de Chesterton's Fence** — Código que parece desnecessário pode existir por motivo não documentado. Para cada bloco que será removido: existe motivo oculto para sua existência?
2. **Identificar dependências ocultas** — Revisar: database links, triggers, views materializadas, cron jobs, scripts de ETL, planilhas com queries diretas, webhooks.
3. **Avaliar risco de perda de lógica de negócio** — Regras hardcoded, magic numbers, workarounds para bugs de terceiros. Cada uma precisa ser preservada ou explicitamente descartada.
4. **Mapear risco por fase** — Cada fase incremental tem seu próprio perfil de risco. Identificar a fase com maior risco e reforçar testes/rollback nela.
5. **Avaliar risco de "refactoring infinito"** — Escopo creep em refactoring é endêmico. Definir timebox e critérios de "bom o suficiente".
6. **Planejar rollback por fase** — Cada fase incremental deve ter rollback independente. Feature flags permitem reverter sem redeploy.

## Outputs

- Lista de Chesterton's Fences identificados (código que não se sabe por que existe)
- Inventário de dependências ocultas por camada
- Lista de lógica de negócio a preservar vs. descartar (com justificativa)
- Perfil de risco por fase incremental
- Timebox definido com critérios de "bom o suficiente"
- Plano de rollback por fase

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Chesterton's Fence avaliado | Código a ser removido foi questionado sobre motivo de existência | Sim |
| Dependências ocultas checadas | Todas as camadas (banco, ETL, integrações) verificadas | Sim |
| Lógica de negócio inventariada | Cada regra de negócio no código tem decisão: preservar ou descartar | Sim |
| Rollback por fase | Cada fase tem mecanismo de rollback independente | Sim |
| Timebox definido | Prazo máximo para refactoring com critérios de "good enough" | Sim |

## Próxima Fase

→ [06-tests.md](./06-tests.md) — Estratégia de testes com foco em caracterização e equivalência
