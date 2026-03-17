# Template: Contrato de API

## Título
API Contract — Definição de Contratos de Interface

## Propósito
Especificar contratos claros entre serviços e componentes, incluindo endpoints, payloads, códigos de resposta e comportamentos esperados, antes da implementação.

## Quando Usar
- Antes de implementar APIs ou integrações entre serviços.
- Quando equipes diferentes precisam trabalhar em paralelo contra a mesma interface.
- Na definição de fronteiras entre bounded contexts.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Serviço | `[nome do serviço]` |
| Versão da API | `[v1.0]` |
| Responsável | `[nome]` |
| Data | `[YYYY-MM-DD]` |
| Protocolo | `[REST / GraphQL / gRPC / Evento]` |

### 2. Base URL e Autenticação
- **Base URL:** `[https://api.exemplo.com/v1]`
- **Autenticação:** `[Bearer Token / API Key / OAuth 2.0]`
- **Rate Limiting:** `[limites aplicáveis]`

### 3. Endpoints
#### `[METHOD] [/path]`
- **Descrição:** `[o que este endpoint faz]`
- **Autenticação:** `[requerida/pública]`
- **Permissões:** `[papéis que podem acessar]`

**Request:**
```json
{
  "[campo]": "[tipo] — [descrição]",
  "[campo]": "[tipo] — [descrição]"
}
```

**Response (200):**
```json
{
  "[campo]": "[tipo] — [descrição]",
  "[campo]": "[tipo] — [descrição]"
}
```

**Códigos de Resposta:**
| Código | Significado | Quando Ocorre |
|--------|------------|---------------|
| 200 | `[Sucesso]` | `[condição]` |
| 400 | `[Requisição inválida]` | `[condição]` |
| 401 | `[Não autenticado]` | `[condição]` |
| 404 | `[Não encontrado]` | `[condição]` |
| 500 | `[Erro interno]` | `[condição]` |

### 4. Modelos de Dados (Schemas)
#### `[NomeDoSchema]`
| Campo | Tipo | Obrigatório | Descrição | Validação |
|-------|------|------------|-----------|-----------|
| `[campo]` | `[string/number/boolean/object]` | `[Sim/Não]` | `[descrição]` | `[regras de validação]` |

### 5. Paginação
- **Estratégia:** `[Offset / Cursor / Keyset]`
- **Parâmetros:** `[page, limit, cursor, etc.]`
- **Formato de Resposta:** `[como vem a paginação na resposta]`

### 6. Tratamento de Erros
```json
{
  "error": {
    "code": "[código do erro]",
    "message": "[mensagem legível]",
    "details": "[detalhes adicionais]"
  }
}
```

### 7. Versionamento
- **Estratégia:** `[URL path / Header / Query param]`
- **Política de Deprecação:** `[como e quando versões antigas são removidas]`

### 8. Contratos de Evento (se aplicável)
| Evento | Tópico/Fila | Payload | Produtor | Consumidor |
|--------|-------------|---------|----------|-----------|
| `[nome]` | `[tópico]` | `[schema]` | `[serviço]` | `[serviço]` |

## Exemplo de Preenchimento

### 3. Endpoints
#### `GET /orders`
- **Descrição:** Lista pedidos do usuário autenticado com filtros e paginação.
- **Autenticação:** Requerida (Bearer Token)
- **Permissões:** customer, admin

**Request (Query Params):**
```
?status=pending&from=2026-01-01&limit=20&cursor=abc123
```

**Response (200):**
```json
{
  "data": [
    {
      "id": "ord_123",
      "status": "pending",
      "total": 150.00,
      "created_at": "2026-03-17T10:00:00Z"
    }
  ],
  "pagination": {
    "next_cursor": "def456",
    "has_more": true
  }
}
```

## Dicas de Qualidade
- **Contract-first:** Defina o contrato antes de implementar. Nunca o contrário.
- **Seja explícito sobre erros:** Cada código de erro deve ter documentação clara.
- **Versionamento desde o início:** Evita breaking changes não planejadas.
- **Valide com consumidores:** Quem vai consumir a API deve revisar o contrato.
- **Use exemplos reais:** Payloads de exemplo com dados verossímeis facilitam o entendimento.
