# Data Modeling Quality Checklist

## Propósito
Garantir que modelagem de dados está completa, consistente e alinhada com o domínio.

## Quando Usar
- Durante a fase correspondente do pipeline de pré-programação
- Em revisões de qualidade antes de avançar para a próxima fase
- Quando o Readiness Gatekeeper solicita verificação

---

## Checklist

### Modelo de Dados
- [ ] Schema principal está definido
- [ ] Relações e cardinalidades estão documentadas
- [ ] Índices críticos estão identificados
- [ ] Estratégia de migração de dados está definida
- [ ] Dados sensíveis estão classificados

### Consistência
- [ ] Constraints de integridade estão documentados
- [ ] Estratégia de concorrência está definida
- [ ] Backup e recovery estão planejados
- [ ] Retenção de dados está definida
- [ ] LGPD/GDPR compliance está verificado

---

## Critérios de Aprovação
- **Mínimo:** 80% dos itens marcados
- **Recomendado:** 100% dos itens marcados
- **Bloqueador:** Qualquer item crítico não atendido deve ser escalado

## Red Flags
- Mais de 3 itens não marcados sem justificativa
- Itens marcados sem evidência de verificação real
- Checklist preenchido em menos de 5 minutos (superficialidade)
