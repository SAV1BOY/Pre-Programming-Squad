# Stripe Engineering — Fonte de Referência

## Fonte

**Organização**: Stripe
**Prática**: Rigor em design de APIs, contratos e confiabilidade
**Referências Principais**:
- Blog de engenharia da Stripe (stripe.com/blog/engineering)
- "Designing APIs that Last" — princípios de API design da Stripe
- Documentação pública da API Stripe (referência de excelência em API docs)

## URL de Referência

- https://stripe.com/blog/engineering
- https://stripe.com/docs/api
- https://stripe.com/blog/payment-api-design

---

## O que Aprender

### Excelência em Design de API

A API da Stripe é considerada referência mundial em design de APIs REST. Princípios que a tornam excepcional:

- **Consistência absoluta**: Todos os endpoints seguem os mesmos padrões de nomenclatura, paginação, tratamento de erro e versionamento.
- **Idempotência nativa**: Toda operação de mutação suporta Idempotency-Key, permitindo retries seguros.
- **Versionamento por data**: Em vez de v1/v2, a Stripe versiona por data (2023-10-16). Cada conta pode "pinar" uma versão e migrar no seu ritmo.
- **Expand para relações**: Em vez de endpoints aninhados complexos, usa `?expand[]=customer` para incluir objetos relacionados.

### Abordagem para Confiabilidade

A Stripe processa trilhões de dólares. Sua abordagem de confiabilidade inclui:

- **Idempotência em tudo**: Operações financeiras nunca podem ser duplicadas
- **Reconciliação contínua**: Processos batch verificam consistência entre sistemas
- **Degradação gradual**: Em caso de falha, features não-críticas são desativadas mantendo o core

### Documentação como Produto

A documentação da API Stripe é tão polida quanto o produto. Isso não é acidente — na Stripe, documentação é prioridade de engenharia, não afterthought.

---

## Práticas Relevantes para Pré-Programação

1. **Padrões de API antes da implementação**: Definir guia de estilo de API do projeto (nomenclatura, paginação, erros, versionamento) durante a pré-programação. Toda API do projeto segue os mesmos padrões.

2. **Idempotência como requisito padrão**: Todo endpoint de mutação deve suportar idempotência. Definir isso no contrato, não como melhoria futura.

3. **Versionamento desde o dia 1**: Nunca lançar API sem estratégia de versionamento definida. O custo de adicionar depois é proibitivo.

4. **Documentação como critério de handoff**: API não está "pronta" para handoff se não tem documentação (OpenAPI/Swagger spec). Incluir exemplos de request/response reais.

5. **Tratamento de erro padronizado**: Definir formato de erro (código, mensagem, detalhes) e catálogo de códigos de erro antes da implementação. Todos os serviços usam o mesmo formato.

6. **Testes de contrato**: Incluir testes de contrato no plano de testes. Consumidor e provedor validam que a API corresponde ao contrato especificado.

7. **Reconciliação como padrão arquitetural**: Para operações financeiras ou dados críticos, planejar processos de reconciliação desde o design, não como reação a inconsistências.
