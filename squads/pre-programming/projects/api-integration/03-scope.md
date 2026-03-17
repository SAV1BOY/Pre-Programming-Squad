# Integração de API — Fase 03: Escopo

## Objetivo da Fase

Definir quais endpoints serão integrados, a estratégia de comunicação (síncrona/assíncrona) e os contratos formais entre os sistemas.

## Agentes Envolvidos

- **Agente de Escopo** (líder da fase) — Define quais endpoints integrar e prioridade
- **Agente de Requisitos** — Valida que escopo atende necessidades de negócio

## Inputs

- Relatório de discovery com testes em sandbox (Fase 02)
- Gaps funcionais identificados
- Requisitos de negócio priorizados
- SLA e limites da API

## Atividades

1. **Selecionar endpoints** — Definir quais endpoints serão integrados na primeira versão. Priorizar por valor de negócio e viabilidade técnica.
2. **Definir estratégia de comunicação** — Para cada endpoint: síncrono (request-response) ou assíncrono (fila/evento)? Considerar criticidade, latência e tolerância a falha.
3. **Formalizar contratos** — Para cada endpoint integrado, documentar: URL, método, headers, body, response esperado, códigos de erro tratados.
4. **Definir mapeamento de dados** — Transformações explícitas entre modelo da API e modelo interno. Incluir: conversões de tipo, valores default, campos opcionais.
5. **Estabelecer política de retry** — Para cada endpoint: quantas tentativas, intervalo entre tentativas, backoff exponencial, quando desistir.
6. **Definir tratamento de indisponibilidade** — O que acontece quando a API está fora do ar? Fila para processamento posterior? Fallback? Degradação graceful?

## Outputs

- Lista de endpoints integrados com priorização
- Estratégia de comunicação por endpoint (sync/async)
- Contratos formalizados para cada endpoint
- Mapeamento de dados com transformações
- Política de retry por endpoint
- Estratégia de tratamento de indisponibilidade

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Endpoints selecionados | Lista com justificativa de priorização | Sim |
| Contratos formalizados | Request/response documentados para cada endpoint | Sim |
| Mapeamento de dados | Transformações entre modelos definidas | Sim |
| Retry definido | Política de retry por endpoint | Sim |
| Fallback planejado | Comportamento em indisponibilidade definido | Sim |

## Próxima Fase

→ [04-architecture.md](./04-architecture.md) — Arquitetura da camada de integração
