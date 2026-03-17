# Ótimos Contratos de API — Exemplos Anotados

## Introdução

Um contrato de API excepcional permite que times trabalhem em paralelo com confiança. Ele define não apenas os endpoints e formatos de dados, mas também comportamento em cenários de erro, versionamento, autenticação, rate limits e SLAs. APIs mal definidas são a causa número um de problemas de integração — o custo de corrigi-las depois de implementadas é exponencialmente maior.

---

## Exemplo 1 — Contrato REST para Serviço de Pedidos

### O Contrato

> **Base URL**: `https://api.internal.company.com/orders/v1`
> **Autenticação**: Bearer token JWT (emitido pelo Auth Service)
> **Rate Limit**: 1000 req/min por service account
> **Content-Type**: `application/json; charset=utf-8`
>
> **POST /orders**
> - Request: `{customer_id: string(uuid), items: [{sku: string, quantity: int(>0), unit_price_cents: int(>0)}], shipping_address_id: string(uuid)}`
> - Response 201: `{order_id: string(uuid), status: "pending", total_cents: int, created_at: string(ISO8601)}`
> - Response 400: `{error: {code: "VALIDATION_ERROR", message: string, details: [{field: string, issue: string}]}}`
> - Response 409: `{error: {code: "INSUFFICIENT_STOCK", message: string, items: [{sku: string, available: int, requested: int}]}}`
>
> **Idempotência**: Header `Idempotency-Key: {uuid}` obrigatório. Requests com mesma key retornam mesmo resultado sem efeito colateral.
>
> **Paginação**: Cursor-based. `GET /orders?cursor={opaque}&limit=20`. Response inclui `next_cursor` (null se última página).

### Por que funciona

- **Tipos explícitos**: `string(uuid)`, `int(>0)` — não apenas "string" ou "number"
- **Códigos de erro com semântica**: `INSUFFICIENT_STOCK` com detalhes por SKU, não genérico 400
- **Idempotência definida**: Essencial para payments e orders, definida no contrato
- **Paginação cursor-based**: Mais robusta que offset para dados que mudam

---

## Exemplo 2 — Contrato de Evento Assíncrono (Kafka)

### O Contrato

> **Tópico**: `orders.lifecycle.v1`
> **Formato**: Avro com Schema Registry
> **Particionamento**: Por `order_id` (garante ordenação por pedido)
>
> **Schema**:
> ```
> {
>   event_id: string(uuid),
>   event_type: enum("order.created", "order.confirmed", "order.shipped", "order.delivered", "order.cancelled"),
>   order_id: string(uuid),
>   timestamp: string(ISO8601),
>   version: int,
>   payload: { /* varia por event_type */ }
> }
> ```
>
> **Garantias**: At-least-once delivery. Consumers devem ser idempotentes.
> **Ordenação**: Garantida dentro da mesma partition (mesmo order_id).
> **Retenção**: 7 dias no tópico principal. Indefinida no tópico compactado.
> **Schema Evolution**: Backward compatible apenas. Novos campos opcionais com defaults.

### Por que funciona

- **Particionamento justificado**: order_id garante ordenação por pedido
- **Garantia de entrega explícita**: At-least-once com responsabilidade do consumer
- **Regra de evolução de schema**: Backward compatible previne quebra de consumers existentes
- **Retenção documentada**: 7 dias operacionais + compactado para replay

---

## Exemplo 3 — Contrato gRPC para Serviço de Precificação

### O Contrato

> **Proto**:
> ```protobuf
> service PricingService {
>   rpc CalculatePrice(PriceRequest) returns (PriceResponse);
>   rpc GetPriceHistory(PriceHistoryRequest) returns (stream PriceEvent);
> }
>
> message PriceRequest {
>   string sku = 1;
>   int32 quantity = 2;
>   string customer_tier = 3; // "standard", "premium", "enterprise"
>   string coupon_code = 4;   // opcional
> }
>
> message PriceResponse {
>   int64 base_price_cents = 1;
>   int64 discount_cents = 2;
>   int64 final_price_cents = 3;
>   string currency = 4; // ISO 4217
>   repeated PriceBreakdown breakdown = 5;
> }
> ```
>
> **SLA**: p50 < 5ms, p99 < 25ms, disponibilidade 99.99%
> **Circuit Breaker**: Consumers devem implementar circuit breaker. Fallback sugerido: último preço em cache.

### Por que funciona

- **Proto com comentários**: Campos documentados inline
- **SLA com percentis**: p50 e p99, não "latência média" que esconde outliers
- **Fallback sugerido**: Contrato orienta o consumer sobre degradação graceful

---

## Lições Extraídas

1. **Tipos precisos, não genéricos**: `string(uuid)` é 10x melhor que `string`
2. **Erros são parte do contrato**: Cada código de erro com semântica e payload definido
3. **Idempotência é obrigatória para mutações**: Rede falha, retries acontecem
4. **Documente garantias de entrega**: At-least-once, at-most-once, exactly-once
5. **Defina paginação antes da implementação**: Mudar paginação depois de lançar é breaking change
6. **Versione desde o dia 1**: `/v1/` no path ou header — nunca lance sem versão
7. **Inclua SLAs no contrato**: Latência e disponibilidade são parte da interface
8. **Defina regras de evolução**: Como o schema pode mudar sem quebrar consumers
