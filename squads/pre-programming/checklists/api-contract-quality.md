# Checklist: Qualidade do Contrato de API

## Propósito
Garantir que contratos de API estão completos, consistentes, versionados e preparados para evolução, antes que qualquer implementação comece.

## Quando Usar
- Ao definir contratos entre serviços, módulos ou sistemas
- Antes de iniciar implementação de endpoints
- Em revisões de contrato com times consumidores

---

## Checklist

### Endpoints e Recursos
- [ ] Todos os endpoints necessários estão listados com método HTTP e path
- [ ] Nomenclatura de recursos segue padrão consistente (plural, kebab-case, etc.)
- [ ] Verbos HTTP estão usados corretamente (GET lê, POST cria, PUT atualiza, DELETE remove)
- [ ] Recursos aninhados têm profundidade razoável (máximo 2-3 níveis)
- [ ] Existe documentação de cada endpoint com descrição do propósito

### Payloads (Request/Response)
- [ ] Schema de request está definido com tipos, formatos e validações
- [ ] Schema de response está definido com exemplos concretos
- [ ] Campos obrigatórios vs opcionais estão diferenciados
- [ ] Formatos de data, moeda, enums estão padronizados
- [ ] Paginação está definida para listagens (cursor, offset, limite)

### Versionamento
- [ ] Estratégia de versionamento está definida (URL path, header, query param)
- [ ] Regras de deprecação estão estabelecidas
- [ ] Período de suporte para versões antigas está definido
- [ ] Breaking changes vs non-breaking changes estão categorizados
- [ ] Processo de migração entre versões está documentado

### Tratamento de Erros
- [ ] Formato padrão de erro está definido (código, mensagem, detalhes)
- [ ] Códigos HTTP de erro estão mapeados corretamente (400, 401, 403, 404, 409, 422, 500)
- [ ] Mensagens de erro são úteis para o consumidor (não genéricas)
- [ ] Erros de validação retornam detalhes por campo
- [ ] Rate limiting e seus códigos de resposta estão documentados

### Compatibilidade e Evolução
- [ ] Contrato é backward-compatible com consumidores existentes
- [ ] Estratégia para adicionar campos sem quebrar consumidores está definida
- [ ] Headers de cache, CORS e content-type estão especificados
- [ ] Autenticação e autorização por endpoint estão documentadas
- [ ] Limites de tamanho de payload estão definidos

---

## Critérios de Aprovação
- **Mínimo**: Endpoints, Payloads e Erros completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Payloads sem schema ou erros sem mapeamento

## Sinais de Alerta (Red Flags)
- Endpoints que fazem coisas demais (API "canivete suíço")
- Ausência de tratamento de erros ("sempre retorna 200")
- Contratos definidos depois da implementação
- Nenhum versionamento planejado
- Payloads com campos genéricos tipo "data", "info", "metadata" sem schema

## Agente Responsável
**Agente de Solution Architecture** — responsável por definir e validar contratos de API.
