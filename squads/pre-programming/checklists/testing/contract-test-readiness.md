# Checklist: Prontidão de Testes de Contrato

## Propósito
Garantir que contratos entre sistemas/serviços são verificáveis automaticamente, detectando quebras de compatibilidade antes de chegar em produção.

## Quando Usar
- Quando a solução envolve comunicação entre serviços ou sistemas
- Ao definir APIs que serão consumidas por outros times
- Quando há histórico de quebras de integração em deploy

---

## Checklist

### Identificação de Contratos
- [ ] Todos os contratos entre serviços internos estão listados
- [ ] Contratos com sistemas externos/terceiros estão listados
- [ ] Provider (quem fornece) e consumer (quem consome) de cada contrato estão definidos
- [ ] Versão atual de cada contrato está documentada
- [ ] Contratos implícitos (não documentados mas existentes) foram identificados

### Definição de Contratos
- [ ] Schema de request e response está especificado formalmente (OpenAPI, Protobuf, etc.)
- [ ] Campos obrigatórios vs opcionais estão definidos
- [ ] Tipos de dados e formatos estão especificados
- [ ] Códigos de erro e seus significados estão documentados
- [ ] Headers e metadados relevantes estão incluídos no contrato

### Ferramenta e Processo
- [ ] Ferramenta de contract testing está escolhida (Pact, Spring Cloud Contract, etc.)
- [ ] Processo de publicação e verificação de contratos está definido
- [ ] Broker de contratos (se aplicável) está configurado
- [ ] Testes de contrato rodam no pipeline de CI automaticamente
- [ ] Falha no teste de contrato bloqueia o deploy

### Consumer-Driven Contracts
- [ ] Consumers definem o que esperam do provider (contratos do consumidor)
- [ ] Provider valida que atende todos os contratos dos consumers
- [ ] Novo consumer pode adicionar seu contrato sem impactar existentes
- [ ] Processo para consumer notificar mudança de expectativa está definido
- [ ] Provider tem visibilidade de todos os consumers e seus contratos

### Evolução de Contratos
- [ ] Regras para mudanças backward-compatible estão definidas
- [ ] Processo para breaking changes está definido (versionamento, deprecação)
- [ ] Período de aviso para deprecação de contrato está acordado
- [ ] Testes verificam compatibilidade com versão anterior do contrato
- [ ] Changelog de mudanças no contrato é mantido

---

## Critérios de Aprovação
- **Mínimo**: Identificação e Definição de Contratos completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Contratos críticos sem verificação automatizada planejada

## Sinais de Alerta (Red Flags)
- "A gente testa a integração em staging" (sem contract test no CI)
- Contratos definidos verbalmente ou por exemplo, sem schema formal
- Provider não sabe quem são seus consumers
- Breaking changes descobertas apenas em produção
- Nenhum contract test em arquitetura de microsserviços

## Agente Responsável
**Agente de Test & Quality Design** — responsável por garantir que contratos são testáveis e testados.
