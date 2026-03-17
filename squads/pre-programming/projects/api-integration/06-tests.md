# Integração de API — Fase 06: Testes

## Objetivo da Fase

Definir estratégia de testes com foco em testes de contrato, resiliência e compatibilidade. Garantir que a integração funciona com a API real e sobrevive a falhas.

## Agentes Envolvidos

- **Agente de Testes** (líder da fase) — Desenha estratégia de testes de integração
- **Agente de Riscos** — Valida cobertura de cenários de falha

## Inputs

- Contratos formalizados (Fase 03)
- Arquitetura com circuit breaker e retry (Fase 04)
- Matriz de riscos (Fase 05)
- Acesso a sandbox da API

## Atividades

1. **Definir testes de contrato** — Testes que validam que a API retorna o formato esperado. Usar Pact ou similar para consumer-driven contracts. Detecta breaking changes automaticamente.
2. **Planejar testes com sandbox real** — Pelo menos 1 teste por endpoint usando sandbox real (não mock). Validar comportamento real vs. documentação.
3. **Planejar testes de resiliência** — Simular: API indisponível (circuit breaker abre), latência alta (timeout funciona), rate limit atingido (retry com backoff), resposta malformada (deserialização não crasha).
4. **Planejar testes de idempotência** — Enviar mesma request 2x. Resultado deve ser idêntico. Verificar que não há efeito colateral duplicado.
5. **Definir testes de mapeamento** — Validar que transformação de dados entre modelo externo e interno funciona para: campos obrigatórios, campos opcionais (null), formatos de data, caracteres especiais, Unicode.
6. **Planejar health check da integração** — Endpoint de health que verifica se a API está acessível e autenticação é válida. Base para alertas de monitoramento.

## Outputs

- Suite de testes de contrato (consumer-driven)
- Testes com sandbox real para endpoints críticos
- Testes de resiliência (indisponibilidade, timeout, rate limit)
- Testes de idempotência para operações de escrita
- Testes de mapeamento de dados
- Health check da integração

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Testes de contrato | Contract tests para cada endpoint integrado | Sim |
| Sandbox real | Pelo menos 1 teste por endpoint com API real | Sim |
| Resiliência testada | Cenários de falha (timeout, 429, 5xx) cobertos | Sim |
| Idempotência | Operações de escrita testadas com retry | Sim |
| Mapeamento validado | Transformações de dados testadas com edge cases | Sim |

## Próxima Fase

→ [07-readiness.md](./07-readiness.md) — Avaliação de prontidão para implementação da integração
