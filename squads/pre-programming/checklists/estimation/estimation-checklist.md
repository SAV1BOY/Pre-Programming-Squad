# Estimation Quality Audit Checklist

## Propósito
Garantir que estimativas são baseadas em evidências, com buffers adequados e riscos quantificados.

## Quando Usar
- Durante a fase correspondente do pipeline de pré-programação
- Em revisões de qualidade antes de avançar para a próxima fase
- Quando o Readiness Gatekeeper solicita verificação

---

## Checklist

### Estimativa
- [ ] Breakdown de tarefas está granular o suficiente
- [ ] Cada tarefa tem estimativa de esforço
- [ ] Buffer de incerteza foi adicionado por camada
- [ ] Reference class forecasting foi aplicado
- [ ] Dependências externas têm buffer adicional

### Validação
- [ ] Estimativa foi revisada por pelo menos 2 pessoas
- [ ] Histórico de projetos similares foi consultado
- [ ] Riscos de prazo estão quantificados
- [ ] Milestones estão definidos com critérios de verificação
- [ ] Plano de contingência existe para atrasos

---

## Critérios de Aprovação
- **Mínimo:** 80% dos itens marcados
- **Recomendado:** 100% dos itens marcados
- **Bloqueador:** Qualquer item crítico não atendido deve ser escalado

## Red Flags
- Mais de 3 itens não marcados sem justificativa
- Itens marcados sem evidência de verificação real
- Checklist preenchido em menos de 5 minutos (superficialidade)
