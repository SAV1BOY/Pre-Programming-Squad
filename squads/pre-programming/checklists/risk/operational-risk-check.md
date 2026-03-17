# Checklist: Verificação de Risco Operacional

## Propósito
Avaliar riscos de operação, suporte e monitoramento do sistema em produção, garantindo que a solução não é apenas construível mas também operável.

## Quando Usar
- Ao planejar a operação do sistema após go-live
- Antes de handoff para o time de operações/SRE
- Quando o sistema será operado 24x7

---

## Checklist

### Operação
- [ ] Procedimentos operacionais rotineiros estão documentados
- [ ] Manutenção preventiva está planejada (rotação de logs, limpeza de cache, etc.)
- [ ] Janelas de manutenção estão definidas e acordadas
- [ ] Automação de tarefas operacionais repetitivas está planejada
- [ ] Capacidade da equipe de operação é suficiente para o sistema

### Suporte
- [ ] Níveis de suporte estão definidos (L1, L2, L3)
- [ ] Runbooks para problemas comuns estão planejados
- [ ] Escalação entre níveis de suporte está definida
- [ ] Base de conhecimento para suporte está planejada
- [ ] SLA de suporte por severidade está definido

### Monitoramento
- [ ] Dashboard operacional com métricas-chave está planejado
- [ ] Alertas para condições críticas estão definidos
- [ ] Alertas para degradação gradual estão definidos (não só falha total)
- [ ] Monitoramento de dependências externas está incluído
- [ ] Alertas têm dono e rotina de resposta

### Incidentes
- [ ] Processo de gestão de incidentes está definido (detecção, resposta, resolução)
- [ ] Roles durante incidentes estão definidos (incident commander, comunicação)
- [ ] Comunicação durante incidentes está definida (canais, templates)
- [ ] Post-mortem é obrigatório para incidentes de alta severidade
- [ ] Métricas de incidentes são rastreadas (MTTD, MTTR)

### Capacidade e Custos
- [ ] Custos operacionais mensais estão estimados
- [ ] Crescimento de custos com escala está projetado
- [ ] Processo de capacity planning está definido
- [ ] Limites de alerta para custos inesperados estão configurados
- [ ] Otimizações de custo são revisadas periodicamente

---

## Critérios de Aprovação
- **Mínimo**: Operação e Monitoramento completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Nenhum monitoramento planejado ou sem processo de incidentes

## Sinais de Alerta (Red Flags)
- "O time de dev opera" sem capacidade ou rotação definida
- Sistema 24x7 sem monitoramento fora do horário comercial
- Nenhum runbook para o dia 1 de operação
- Custos operacionais não estimados ("vemos depois")
- Alertas que disparam 50 vezes por dia (alert fatigue)

## Agente Responsável
**Agente de Risk & Failure Analysis** — em colaboração com SRE e time de operações.
