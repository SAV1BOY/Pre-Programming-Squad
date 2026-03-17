# Projeto de Automação — Fase 06: Testes

## Objetivo da Fase

Definir testes que validem regras de negócio automatizadas, resiliência a falhas e detecção de anomalias. Automação correta mas com regra errada é pior que processo manual.

## Agentes Envolvidos

- **Agente de Testes** (líder da fase) — Desenha estratégia de testes de automação
- **Agente de Requisitos** — Valida que regras de negócio estão cobertas

## Inputs

- Catálogo de regras de decisão (Fase 02)
- Exceções e tratamentos (Fases 02-03)
- Circuit breakers (Fase 05)
- Dados de execuções históricas do processo manual

## Atividades

1. **Testar cada regra de negócio** — Cada regra de decisão tem conjunto de testes: input que satisfaz a regra, input que não satisfaz, input no limite (boundary). Regras são a essência da automação.
2. **Testar tratamento de exceções** — Cada exceção catalogada tem teste: dados incompletos, formato errado, sistema indisponível. Verificar que exceção é tratada conforme definido.
3. **Testar com dados históricos** — Replay de execuções anteriores do processo manual. Resultado da automação deve coincidir com resultado manual.
4. **Testar circuit breakers** — Simular condições anômalas e verificar que automação para: taxa de erro alta, volume fora do range, resultado inesperado.
5. **Testar idempotência** — Reexecutar automação com mesmos dados. Resultado deve ser idêntico sem efeitos colaterais duplicados.
6. **Testar observabilidade** — Verificar que dashboard mostra execuções corretamente, alertas disparam em falha, logs têm informação suficiente para debug.

## Outputs

- Testes unitários para cada regra de negócio
- Testes de exceção para cada cenário catalogado
- Resultado de replay com dados históricos
- Testes de circuit breaker
- Testes de idempotência
- Validação de observabilidade

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Regras testadas | 100% das regras de decisão com testes | Sim |
| Exceções cobertas | Cada exceção tem cenário de teste | Sim |
| Replay histórico | Automação reproduz resultados manuais | Sim |
| Circuit breakers testados | Automação para em condições anômalas | Sim |
| Idempotência validada | Reexecução não causa efeitos duplicados | Sim |

## Próxima Fase

→ [07-readiness.md](./07-readiness.md) — Avaliação de prontidão para deploy da automação
