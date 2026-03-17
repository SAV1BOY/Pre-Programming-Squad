# Bugfix Crítico — Fase 05: Riscos

## Objetivo da Fase

Identificar riscos de que o fix piore a situação ou crie novos problemas. Em bugfix crítico, o risco principal é que o fix cause mais dano que o bug original.

## Agentes Envolvidos

- **Agente de Riscos** (líder da fase) — Avalia riscos do fix em si
- **Agente de Arquitetura** — Valida que rollback é viável

## Inputs

- Fix proposto com análise de impacto (Fases 03-04)
- Blast radius atual do bug
- Estado de dados corrompidos (se houver)
- Histórico de fixes anteriores no mesmo componente

## Atividades

1. **Avaliar risco do fix piorar situação** — O fix pode afetar caminhos de código saudáveis? Pode aumentar o blast radius?
2. **Identificar cenários de falha do fix** — O que acontece se o fix não funcionar? O que acontece se funcionar parcialmente?
3. **Definir plano de rollback do fix** — Como reverter o fix se ele piorar a situação. Tempo estimado de rollback. Feature flag para desabilitar rapidamente.
4. **Avaliar risco de dados** — Se há script de correção de dados, qual o risco de corrigir errado? Dry-run obrigatório com validação antes de execução.
5. **Definir critérios de sucesso do fix** — Métricas que confirmam que o fix resolveu o problema (error rate, latência, funcionalidade restaurada).
6. **Planejar monitoramento pós-fix** — Dashboard e alertas específicos para as primeiras 24h após deploy do fix.

## Outputs

- Análise de risco do fix (pode piorar? como?)
- Plano de rollback do fix com tempo estimado
- Critérios de sucesso mensuráveis
- Plano de monitoramento pós-fix (24h)
- Feature flag para desabilitar fix (se aplicável)

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Rollback viável | Fix pode ser revertido em <15 minutos | Sim |
| Critérios de sucesso | Métricas que confirmam resolução estão definidas | Sim |
| Monitoramento planejado | Dashboard e alertas para pós-fix definidos | Sim |
| Fix não amplia blast radius | Análise confirma que fix não afeta caminhos saudáveis | Sim |

**SLA:** Análise de riscos de Sev1 deve ser concluída em **30 minutos**.

## Próxima Fase

→ [06-tests.md](./06-tests.md) — Testes mínimos e obrigatórios para o fix
