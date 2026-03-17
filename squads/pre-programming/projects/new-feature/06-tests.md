# Nova Feature — Fase 06: Testes

## Objetivo da Fase

Desenhar a estratégia de testes para a feature antes da implementação, definindo cenários, camadas de teste e critérios de cobertura que validem requisitos e riscos identificados.

## Agentes Envolvidos

- **Agente de Testes** (líder da fase) — Desenha estratégia e cenários de teste
- **Agente de Requisitos** — Valida que cenários de teste cobrem requisitos
- **Agente de Riscos** — Valida que riscos identificados têm cobertura de teste

## Inputs

- Cenários de uso com critérios de aceitação (Fase 03)
- Design doc e contratos (Fase 04)
- Matriz de riscos (Fase 05)
- Plano de rollback (Fase 05)

## Atividades

1. **Derivar cenários de teste dos requisitos** — Cada critério de aceitação gera pelo menos um cenário de teste. Incluir happy path, sad path e edge cases.
2. **Definir pirâmide de testes** — Distribuir cenários entre unitários, integração, contrato e E2E. Justificar a camada escolhida para cada cenário.
3. **Planejar testes de integração reais** — Definir quais componentes externos serão testados com instância real (Testcontainers) vs. mock/stub.
4. **Planejar testes de concorrência** — Para operações de estado (check-then-act), definir cenários de acesso concorrente.
5. **Planejar testes de performance** — Se há requisitos de latência ou throughput, definir cenários de carga com valores-alvo.
6. **Definir dados de teste** — Estratégia de criação de dados: factories, fixtures, seeds. Incluir dados com caracteres especiais, Unicode, valores limítrofes.
7. **Definir critérios de aprovação** — Coverage mínimo por camada, mutation score, cenários obrigatórios que devem passar para merge.

## Outputs

- Documento de estratégia de testes com pirâmide definida
- Lista de cenários de teste por camada
- Plano de testes de integração com componentes reais
- Plano de testes de concorrência e performance
- Estratégia de dados de teste
- Critérios de aprovação para merge

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Cobertura de requisitos | Cada critério de aceitação P0 tem cenário de teste | Sim |
| Cobertura de riscos | Cada risco High tem cenário de teste associado | Sim |
| Testes de integração reais | Integrações críticas testadas com componente real | Sim |
| Concorrência coberta | Operações de estado têm teste de concorrência | Condicional |
| Dados de teste robustos | Inputs degenerados e edge cases incluídos | Sim |

## Próxima Fase

→ [07-readiness.md](./07-readiness.md) — Avaliação de prontidão para implementação
