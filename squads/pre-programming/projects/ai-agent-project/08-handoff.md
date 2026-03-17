# Projeto de Agente IA — Fase 08: Handoff

## Objetivo da Fase

Lançar o agente de forma gradual com monitoramento intensivo, coletar feedback humano e estabelecer processo de melhoria contínua de prompts e evals.

## Agentes Envolvidos

- **Agente Coordenador** (líder da fase) — Coordena lançamento gradual
- **Agente de Riscos** — Monitora métricas de segurança
- **Agente de Testes** — Monitora scores de evals em produção

## Inputs

- Agente aprovado no readiness (Fase 07)
- Evals e guardrails configurados
- Plano de observabilidade ativo

## Atividades

1. **Lançamento interno (dogfooding)** — Time interno usa o agente por 1-2 semanas. Feedback qualitativo e quantitativo coletado.
2. **Lançamento beta** — Grupo pequeno de usuários reais (5-10%) com banner de "beta". Monitorar: qualidade de respostas, escalação para humano, feedback negativo.
3. **Monitorar evals em produção** — Evals automáticos em amostra de interações reais. Comparar com scores de pré-lançamento. Alerta se degradação > 5%.
4. **Coletar feedback humano** — Mecanismo de feedback em cada interação (thumbs up/down + comentário opcional). Agregar e analisar semanalmente.
5. **Iterar prompts** — Baseado em feedback e evals, iterar system prompt e guardrails. Cada iteração passa por evals antes de deploy.
6. **Escalar gradualmente** — 10% → 25% → 50% → 100% com gates de qualidade em cada nível. Rollback se scores caírem abaixo do threshold.
7. **Estabelecer ciclo de melhoria** — Processo mensal: revisar evals, atualizar golden examples, ajustar prompts, avaliar novos modelos.

## Outputs

- Relatório de dogfooding com feedback
- Métricas de beta (qualidade, escalação, feedback)
- Dashboard de evals em produção
- Processo de iteração de prompts documentado
- Plano de escalonamento gradual com gates
- Ciclo de melhoria contínua definido

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Dogfooding validado | Feedback interno positivo, sem issues de segurança | Sim |
| Beta estável | Scores de evals mantidos em beta | Sim |
| Feedback positivo | Taxa de thumbs up > 80% (ou threshold definido) | Sim |
| Segurança confirmada | Zero incidentes de PII, injection ou toxicity em beta | Sim |
| Ciclo de melhoria | Processo de iteração mensal definido | Sim |

## Próxima Fase

→ Operação contínua com ciclo de melhoria mensal.

**Nota:** Agentes de IA requerem monitoramento contínuo permanente. Diferente de software tradicional, a qualidade pode degradar com atualizações do modelo base ou mudanças no padrão de uso. Evals em produção são obrigatórios indefinidamente.
