# Contract Testing

## O que e Contract Testing

Contract testing e uma tecnica de teste que verifica se dois sistemas (provider e consumer) podem se comunicar corretamente, sem necessidade de executar ambos simultaneamente. Cada lado verifica independentemente que cumpre sua parte do contrato. E particularmente valioso em arquiteturas de microsservicos onde testes E2E sao lentos e frageis.

## Por que Contract Testing e Relevante para Pre-Programacao

Na fase de pre-programacao, definimos contratos entre servicos — APIs, eventos, schemas. Contract testing e o mecanismo que garante que esses contratos definidos no design doc serao respeitados durante e apos a implementacao. Planejar contract testing na pre-programacao:
- Forca definicao precisa de contratos antes da implementacao.
- Permite desenvolvimento paralelo de provider e consumer.
- Detecta breaking changes automaticamente no CI.

## Tipos de Contract Testing

### 1. Consumer-Driven Contract Testing (CDC)
O consumer define o contrato baseado no que ele precisa. O provider verifica que atende a todos os contratos de seus consumers.

**Fluxo:**
1. Consumer escreve um teste que descreve o que espera do provider.
2. O teste gera um contrato (pact file).
3. O contrato e compartilhado com o provider.
4. O provider roda o contrato contra sua implementacao real.
5. Se passa, o contrato esta satisfeito.

**Quando usar:** Quando o consumer sabe exatamente o que precisa e o provider deve atender multiplos consumers.

### 2. Provider-Driven Contract Testing
O provider define o contrato e os consumers devem se adequar. Comum com APIs publicas ou APIs com muitos consumers desconhecidos.

**Quando usar:** APIs publicas, plataformas, servicos com >10 consumers.

### 3. Bidirectional Contract Testing
Tanto provider quanto consumer definem expectativas. Um broker (como Pactflow) verifica compatibilidade.

**Quando usar:** Quando ambos os lados evoluem independentemente e a compatibilidade deve ser verificada continuamente.

## Ferramentas

### Pact
A ferramenta mais popular para CDC testing. Suporta multiplas linguagens (Java, JavaScript, Python, Go, Ruby, .NET). Usa Pact Broker para compartilhar contratos.

### Spring Cloud Contract
Especifico para ecossistema Spring. Provider define contratos em Groovy/YAML; stubs sao gerados automaticamente para consumers.

### Specmatic (antigo Qontract)
Contract testing baseado em OpenAPI specs. Usa a especificacao da API como contrato.

## Contract Testing para Eventos/Mensagens

### O Desafio
Alem de APIs HTTP, microsservicos se comunicam via eventos (Kafka, SQS, etc.). O contrato inclui: formato da mensagem, schema, campos obrigatorios, semantica.

### Como Testar
1. **Producer contract:** Producer envia mensagem no formato esperado.
2. **Consumer contract:** Consumer consegue deserializar e processar a mensagem.
3. **Schema compatibility:** Schema registry verifica compatibilidade (backward, forward, full).

### Exemplo de Contrato de Evento
```json
{
  "event_type": "order.created",
  "version": "1.0",
  "required_fields": ["order_id", "customer_id", "items", "total", "created_at"],
  "schema": {
    "order_id": "string (UUID)",
    "customer_id": "string (UUID)",
    "items": "array of {product_id, quantity, unit_price}",
    "total": "decimal",
    "created_at": "ISO 8601 datetime"
  }
}
```

## Contract Testing na Pre-Programacao

### Na Definicao de APIs
- Definir OpenAPI spec antes da implementacao.
- Especificar exemplos de request/response para cada endpoint.
- Documentar campos obrigatorios vs. opcionais.
- Definir versionamento de API (URL path, header, ou content negotiation).

### Na Definicao de Eventos
- Definir schema de cada evento com schema registry.
- Especificar campos obrigatorios e tipos.
- Definir estrategia de compatibilidade (backward-compatible por default).
- Documentar semantica de cada evento.

### No Design Doc
Incluir secao de contratos:
```markdown
## Contratos

### API: POST /api/v1/orders
- Request: {customer_id, items[], shipping_address}
- Response 201: {order_id, status, estimated_delivery}
- Response 400: {error_code, message, details[]}
- Contract testing: Pact CDC com checkout-frontend e mobile-app

### Evento: order.created
- Schema: Avro, registrado em Schema Registry
- Compatibility: backward
- Consumers: inventory-service, notification-service, analytics
- Contract testing: Pact message contract com cada consumer
```

### Nos Criterios de Readiness
- "Contratos de API estao definidos com OpenAPI spec?"
- "Contratos de eventos estao definidos com schemas?"
- "Estrategia de contract testing esta definida?"
- "Estrategia de versionamento e compatibilidade esta definida?"
- "Consumers conhecidos estao listados para cada contrato?"

## Armadilhas Comuns

### Contrato muito restritivo
Especificar formato exato de resposta quando o consumer so precisa de 3 campos. Resultado: qualquer mudanca no provider quebra o contrato.

### Ignorar eventos
Focar contract testing apenas em APIs HTTP e ignorar contratos de eventos. Mensagens sem contrato sao bugs esperando acontecer.

### Nao versionar contratos
Mudar um contrato sem comunicar ou versionar. Resultado: breaking changes silenciosas em producao.

### Testes que nao rodam no CI
Contract tests que so rodam manualmente. Resultado: contratos divergem da implementacao gradualmente.
