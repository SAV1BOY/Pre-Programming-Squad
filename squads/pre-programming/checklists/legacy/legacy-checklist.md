# Legacy Impact Audit Checklist

## Propósito
Garantir que impactos em sistemas legados foram mapeados, com estratégia de migração e rollback.

## Quando Usar
- Durante a fase correspondente do pipeline de pré-programação
- Em revisões de qualidade antes de avançar para a próxima fase
- Quando o Readiness Gatekeeper solicita verificação

---

## Checklist

### Análise de Impacto
- [ ] Sistemas legados afetados estão identificados
- [ ] Dependências do legado estão mapeadas
- [ ] Backward compatibility está avaliada
- [ ] Dados históricos estão preservados
- [ ] Integrações existentes foram verificadas

### Migração
- [ ] Estratégia de migração está definida (big bang vs incremental)
- [ ] Rollback plan está documentado e testável
- [ ] Characterization tests existem para comportamento atual
- [ ] Período de coexistência está planejado
- [ ] Comunicação de deprecation está agendada

---

## Critérios de Aprovação
- **Mínimo:** 80% dos itens marcados
- **Recomendado:** 100% dos itens marcados
- **Bloqueador:** Qualquer item crítico não atendido deve ser escalado

## Red Flags
- Mais de 3 itens não marcados sem justificativa
- Itens marcados sem evidência de verificação real
- Checklist preenchido em menos de 5 minutos (superficialidade)
