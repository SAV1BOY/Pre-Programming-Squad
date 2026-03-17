# Security & Trust Review Checklist

## Propósito
Garantir que aspectos de segurança, privacidade e confiança foram avaliados antes da implementação.

## Quando Usar
- Durante a fase correspondente do pipeline de pré-programação
- Em revisões de qualidade antes de avançar para a próxima fase
- Quando o Readiness Gatekeeper solicita verificação

---

## Checklist

### Segurança
- [ ] Autenticação e autorização estão definidas
- [ ] Dados sensíveis estão classificados e protegidos
- [ ] Input validation está especificada
- [ ] OWASP Top 10 foi verificado contra o design
- [ ] Secrets management está definido

### Privacidade e Compliance
- [ ] LGPD/GDPR requirements estão mapeados
- [ ] Data retention policy está definida
- [ ] Audit trail está planejado
- [ ] Misuse cases estão documentados
- [ ] Threat model está atualizado

---

## Critérios de Aprovação
- **Mínimo:** 80% dos itens marcados
- **Recomendado:** 100% dos itens marcados
- **Bloqueador:** Qualquer item crítico não atendido deve ser escalado

## Red Flags
- Mais de 3 itens não marcados sem justificativa
- Itens marcados sem evidência de verificação real
- Checklist preenchido em menos de 5 minutos (superficialidade)
