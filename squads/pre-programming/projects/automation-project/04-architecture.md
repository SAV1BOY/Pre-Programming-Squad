# Projeto de Automação — Fase 04: Arquitetura

## Objetivo da Fase

Definir a arquitetura de orquestração da automação, escolher engine de workflow, planejar integrações e definir modelo de execução.

## Agentes Envolvidos

- **Agente de Arquitetura** (líder da fase) — Desenha arquitetura de orquestração
- **Agente de Riscos** — Avalia resiliência e observabilidade

## Inputs

- Diagrama de fluxo com níveis de automação (Fases 02-03)
- Integrações e APIs necessárias (Fase 01)
- Guardrails e limites definidos (Fase 03)

## Atividades

1. **Escolher engine de orquestração** — Avaliar: cron jobs (simples), Airflow/Prefect (DAGs), Temporal/Conductor (workflows durables), Step Functions (cloud-native). Complexidade proporcional à necessidade.
2. **Definir modelo de execução** — Schedule-based (cron), event-driven (trigger), ou on-demand (manual trigger com parâmetros)?
3. **Planejar integrações** — Para cada sistema: API REST, message queue, database query, file transfer, email parsing? Definir client e tratamento de erro.
4. **Definir tratamento de falhas** — Retry automático (com limite), dead letter para falhas permanentes, alertas para taxa de falha acima do threshold.
5. **Planejar observabilidade** — Dashboard de execuções: sucesso, falha, exceção, em andamento. Logs estruturados por execução. Alertas proativos.
6. **Definir modelo de dados** — Rastreabilidade end-to-end: cada execução tem ID, inputs, outputs, decisões tomadas, exceções encontradas.
7. **Planejar escalabilidade** — A automação suporta crescimento de volume? Pode escalar horizontalmente? Há bottleneck em algum sistema?

## Outputs

- Arquitetura de orquestração com engine escolhida
- Modelo de execução (schedule, event, on-demand)
- Design de integrações por sistema
- Estratégia de tratamento de falhas (retry, DLQ, alertas)
- Plano de observabilidade (dashboard, logs, alertas)
- Modelo de dados para rastreabilidade

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Engine justificada | Complexidade proporcional à necessidade | Sim |
| Falhas tratadas | Retry, DLQ e alertas configurados | Sim |
| Observabilidade | Dashboard e logs por execução planejados | Sim |
| Rastreabilidade | Cada execução rastreável end-to-end | Sim |

## Próxima Fase

→ [05-risks.md](./05-risks.md) — Riscos específicos de automação de processos
