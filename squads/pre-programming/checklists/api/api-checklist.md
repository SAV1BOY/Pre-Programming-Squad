# API Contract Quality Audit Checklist

## Propósito
Garantir que contratos de API foram definidos com completude, versionamento e tratamento de erros.

## Quando Usar
- Durante a fase correspondente do pipeline de pré-programação
- Em revisões de qualidade antes de avançar para a próxima fase
- Quando o Readiness Gatekeeper solicita verificação

---

## Checklist

### Contratos
- [ ] Endpoints estão documentados com método, path e descrição
- [ ] Payloads de request e response estão definidos
- [ ] Códigos de erro e mensagens estão padronizados
- [ ] Versionamento de API está definido
- [ ] Rate limiting e throttling estão especificados

### Compatibilidade
- [ ] Breaking changes estão identificados
- [ ] Backward compatibility está garantida ou migração planejada
- [ ] Contratos de eventos/webhooks estão documentados
- [ ] Autenticação e autorização estão especificadas
- [ ] Documentação OpenAPI/Swagger está gerada

---

## Critérios de Aprovação
- **Mínimo:** 80% dos itens marcados
- **Recomendado:** 100% dos itens marcados
- **Bloqueador:** Qualquer item crítico não atendido deve ser escalado

## Red Flags
- Mais de 3 itens não marcados sem justificativa
- Itens marcados sem evidência de verificação real
- Checklist preenchido em menos de 5 minutos (superficialidade)
