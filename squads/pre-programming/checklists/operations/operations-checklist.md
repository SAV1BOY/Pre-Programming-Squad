# Operational Readiness Checklist

## Propósito
Garantir que aspectos operacionais (observabilidade, alertas, runbooks) estão planejados antes do código.

## Quando Usar
- Durante a fase correspondente do pipeline de pré-programação
- Em revisões de qualidade antes de avançar para a próxima fase
- Quando o Readiness Gatekeeper solicita verificação

---

## Checklist

### Observabilidade
- [ ] Métricas de negócio e técnicas estão definidas
- [ ] Logs estruturados estão especificados
- [ ] Distributed tracing está planejado
- [ ] Dashboards estão desenhados
- [ ] Health checks estão definidos

### Operação
- [ ] Alertas e thresholds estão configurados
- [ ] Runbooks de incidente estão rascunhados
- [ ] On-call responsibilities estão definidas
- [ ] Deployment strategy está documentada (blue-green, canary)
- [ ] Disaster recovery está planejado

---

## Critérios de Aprovação
- **Mínimo:** 80% dos itens marcados
- **Recomendado:** 100% dos itens marcados
- **Bloqueador:** Qualquer item crítico não atendido deve ser escalado

## Red Flags
- Mais de 3 itens não marcados sem justificativa
- Itens marcados sem evidência de verificação real
- Checklist preenchido em menos de 5 minutos (superficialidade)
