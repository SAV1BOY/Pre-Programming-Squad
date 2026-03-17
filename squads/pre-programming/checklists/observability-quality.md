# Checklist: Qualidade da Observabilidade

## Propósito
Garantir que logs, métricas, tracing e alertas estão planejados antes da implementação, permitindo debuggability e operação confiável desde o primeiro deploy.

## Quando Usar
- Após definição de arquitetura e antes da implementação
- Ao planejar a operação do sistema em produção
- Em revisões de operabilidade e SRE readiness

---

## Checklist

### Logs
- [ ] Estratégia de logging está definida (o que logar, em que nível)
- [ ] Formato de log está padronizado (structured logging, JSON)
- [ ] Dados sensíveis são excluídos ou mascarados nos logs
- [ ] Correlation ID está planejado para rastrear fluxos entre serviços
- [ ] Retenção e rotação de logs estão definidas

### Métricas
- [ ] Métricas de negócio (RED: Rate, Errors, Duration) estão definidas
- [ ] Métricas de infraestrutura estão identificadas (CPU, memória, disco, rede)
- [ ] Métricas customizadas do domínio estão planejadas
- [ ] Ferramenta de coleta e visualização está definida (Prometheus, Grafana, etc.)
- [ ] Dashboards principais estão especificados (o que mostram)

### Tracing Distribuído
- [ ] Tracing está planejado para fluxos que cruzam múltiplos serviços
- [ ] Ferramenta de tracing está escolhida (Jaeger, Zipkin, OpenTelemetry)
- [ ] Spans principais estão identificados por serviço
- [ ] Propagação de contexto entre serviços está definida
- [ ] Sampling strategy está definida (não trace 100% em produção de alta carga)

### Alertas
- [ ] Alertas para cenários críticos estão definidos
- [ ] Thresholds de alerta estão baseados em SLOs, não em valores arbitrários
- [ ] Severidade dos alertas está categorizada (P1, P2, P3)
- [ ] Canais de notificação estão definidos (Slack, PagerDuty, email)
- [ ] Runbooks estão vinculados a cada alerta crítico

### Debuggability
- [ ] É possível reproduzir problemas a partir dos dados de observabilidade
- [ ] Feature flags estão planejadas para ativar debug extra quando necessário
- [ ] Acesso a logs e métricas em produção está definido (quem pode acessar)
- [ ] Existe forma de correlacionar logs, métricas e traces de um mesmo evento
- [ ] Health check endpoints estão definidos para cada serviço

---

## Critérios de Aprovação
- **Mínimo**: Logs e Alertas completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Nenhum log estruturado planejado ou zero alertas definidos

## Sinais de Alerta (Red Flags)
- "Vamos ver o que logar quando tiver o código" (reativo demais)
- Logs que expõem dados sensíveis (PII, tokens, senhas)
- Alertas sem runbook ("alerta disparou, e agora?")
- Nenhum tracing em arquitetura de microsserviços
- Dashboard que ninguém olha regularmente

## Agente Responsável
**Agente de Solution Architecture** — em colaboração com o time de SRE/Operações.
