# Bugfix Crítico — Fase 08: Handoff

## Objetivo da Fase

Entregar o fix para deploy, monitorar as primeiras horas pós-deploy e garantir documentação para post-mortem.

## Agentes Envolvidos

- **Agente Coordenador** (líder da fase) — Coordena deploy e comunicação
- **Agente de Riscos** — Monitora métricas de sucesso pós-deploy

## Inputs

- Fix aprovado no readiness (Fase 07)
- Plano de rollback pronto
- Plano de monitoramento configurado
- Critérios de sucesso definidos

## Atividades

1. **Coordenar deploy** — Executar deploy seguindo protocolo (staging validado, canary se possível, rollout gradual para Sev2/Sev3).
2. **Monitorar métricas de sucesso** — Nas primeiras 2 horas pós-deploy, verificar: error rate voltou ao normal? Funcionalidade restaurada? Latência dentro do esperado?
3. **Executar validação pós-deploy** — Rodar cenário de validação definido na Fase 06 em produção.
4. **Comunicar resolução** — Notificar stakeholders, suporte e clientes afetados que o problema foi resolvido.
5. **Executar correção de dados** — Se há dados corrompidos, executar script de correção (após dry-run validado).
6. **Agendar post-mortem** — Em até 48h para Sev1, 1 semana para Sev2. Post-mortem deve atualizar archive de falhas do squad.
7. **Registrar lições** — Documentar: o que causou, o que preveniria, que checklist deve ser atualizado.

## Outputs

- Confirmação de deploy bem-sucedido com métricas
- Comunicação de resolução para stakeholders
- Relatório de correção de dados (se aplicável)
- Post-mortem agendado com participantes
- Lições aprendidas para archive do squad

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Métricas normalizadas | Error rate e latência dentro do esperado por 2h+ | Sim |
| Validação em produção | Cenário principal confirmado em produção | Sim |
| Stakeholders notificados | Comunicação de resolução enviada | Sim |
| Post-mortem agendado | Data, hora e participantes definidos | Sim |
| Archive atualizado | Lições registradas no archive de falhas | Sim |

**SLA total Sev1:** Da intake ao deploy, máximo de **6 horas**. Da intake à confirmação de resolução, máximo de **8 horas**.

## Próxima Fase

→ Post-mortem (em até 48h) alimenta o archive do Pre-Programming Squad com lições aprendidas e atualização de checklists.
