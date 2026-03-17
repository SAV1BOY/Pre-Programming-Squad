# Integração de API — Fase 01: Intake

## Objetivo da Fase

Receber e validar a solicitação de integração com API externa ou interna, identificar o provedor, avaliar documentação disponível e classificar a criticidade da integração.

## Agentes Envolvidos

- **Agente de Requisitos** (líder da fase) — Valida escopo e requisitos da integração
- **Agente Coordenador** — Registra projeto e identifica pontos de contato do provedor

## Inputs

- Solicitação de integração com contexto de negócio
- Documentação da API alvo (swagger, docs, sandbox)
- Contrato ou SLA com o provedor (se externo)
- Requisitos de dados que fluem pela integração

## Atividades

1. **Identificar tipo de integração** — Consumir API existente, expor nova API, bidirecional, webhook, event-driven. Cada tipo tem riscos diferentes.
2. **Avaliar documentação disponível** — A API tem documentação atualizada? Swagger/OpenAPI? Sandbox disponível? Exemplos de request/response?
3. **Verificar SLA e limites** — Rate limits, quota, disponibilidade garantida, latência esperada, política de breaking changes.
4. **Identificar ponto de contato técnico** — Quem do lado do provedor pode resolver dúvidas técnicas? Qual o tempo de resposta esperado?
5. **Classificar criticidade** — A integração é no caminho crítico do usuário (síncrona) ou background (assíncrona tolera falhas)?
6. **Verificar requisitos de segurança** — Autenticação (OAuth, API key, mTLS), autorização, criptografia de dados em trânsito e repouso.

## Outputs

- Registro do projeto de integração com metadados
- Avaliação de documentação da API (completa, parcial, ausente)
- SLA e limites documentados
- Ponto de contato técnico do provedor
- Classificação de criticidade (síncrona crítica, assíncrona tolerante)
- Requisitos de segurança listados

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Documentação avaliada | Status da documentação da API classificado | Sim |
| SLA verificado | Rate limits, disponibilidade e latência documentados | Sim |
| Contato técnico | Pessoa do provedor identificada para suporte | Sim |
| Segurança avaliada | Método de autenticação e requisitos de segurança definidos | Sim |

## Próxima Fase

→ [02-discovery.md](./02-discovery.md) — Análise detalhada da API, contratos e compatibilidade
