# Contract-First Design Framework

## Propósito
Definir contratos de API e interface antes de iniciar implementação, garantindo alinhamento entre consumer e provider e reduzindo retrabalho de integração.

## Problema que Resolve
Quando provider e consumer desenvolvem em paralelo sem contrato definido, a integração final é dolorosa: formatos incompatíveis, campos faltando, semântica diferente. Contract-first elimina esse retrabalho.

## Quando Usar
- Em todo projeto com integrações (API, eventos, filas)
- Quando múltiplos times desenvolvem em paralelo
- Obrigatório quando o Interface Designer está no pipeline
- Em projetos API-first

## Princípios
1. **Consumer drives the contract** — O contrato é definido pela necessidade de quem consome, não pela conveniência de quem implementa
2. **Contract antes do código** — Nenhuma linha de código é escrita antes do contrato estar aceito por ambos os lados
3. **Contrato é testável** — Toda cláusula do contrato pode ser verificada automaticamente (contract tests)
4. **Versionamento desde o dia 1** — Contratos têm versão e estratégia de evolução

## Processo

### Passo 1 — Mapear Integrações
| Consumer | Provider | Tipo | Protocolo |
|----------|----------|------|-----------|
| Frontend | User API | REST | HTTPS |
| Order Service | Payment API | REST | HTTPS |
| Payment Service | Notification | Event | Kafka |
| Admin Dashboard | Analytics | GraphQL | HTTPS |

### Passo 2 — Definir Contrato por Integração
Para REST:
```yaml
endpoint: POST /api/v1/payments
request:
  content_type: application/json
  body:
    order_id: string (required, UUID)
    amount: number (required, > 0)
    currency: string (required, ISO 4217)
    method: enum [credit_card, pix, boleto]
response:
  success: # 201 Created
    payment_id: string (UUID)
    status: enum [pending, confirmed, failed]
    created_at: datetime (ISO 8601)
  errors:
    400: { code: "INVALID_REQUEST", message: string }
    402: { code: "INSUFFICIENT_FUNDS", message: string }
    422: { code: "UNSUPPORTED_METHOD", message: string }
    500: { code: "PROVIDER_ERROR", message: string }
  headers:
    X-Request-Id: string (UUID, for tracing)
  sla:
    p95_latency: 500ms
    availability: 99.9%
```

### Passo 3 — Validar com Ambos os Lados
- Consumer confirma: "este contrato atende meu caso de uso?"
- Provider confirma: "consigo implementar este contrato?"
- Negociar se houver gap

### Passo 4 — Gerar Artefatos
- OpenAPI/Swagger spec para REST
- AsyncAPI spec para eventos
- GraphQL schema para GraphQL
- Contract tests (Pact, Spring Cloud Contract)

### Passo 5 — Definir Evolução
- Backward compatible changes: add-only (novos campos opcionais)
- Breaking changes: nova versão (v1 → v2) com deprecation period
- Consumer migration plan para breaking changes

## Armadilhas
- **Definir contrato apenas pelo provider** → Consumer precisa dizer o que precisa
- **Não versionar desde o início** → Mudança sem versão quebra consumers silenciosamente
- **Ignorar cenários de erro** → Happy path é 50% do contrato; erros são os outros 50%
- **Contract tests opcionais** → Sem teste automático, contrato é só documento que envelhece
