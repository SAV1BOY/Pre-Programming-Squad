# Refatoração de Legado — Fase 06: Testes

## Objetivo da Fase

Definir estratégia de testes focada em garantir equivalência comportamental entre código legado e refatorado. Testes de caracterização são o pilar central.

## Agentes Envolvidos

- **Agente de Testes** (líder da fase) — Desenha estratégia de testes de caracterização e equivalência
- **Agente de Requisitos** — Valida que comportamentos críticos estão cobertos
- **Agente de Riscos** — Garante que cenários de risco têm cobertura

## Inputs

- Suite de testes de caracterização inicial (Fase 02)
- Critérios de equivalência (Fase 03)
- Perfil de risco por fase (Fase 05)
- Dados de produção (padrões de uso real)

## Atividades

1. **Expandir testes de caracterização** — Complementar golden tests da Fase 02 com cenários adicionais descobertos durante discovery e análise de riscos.
2. **Definir testes de equivalência** — Testes que rodam o mesmo input no código legado e refatorado, comparando outputs. Ideal: parallel run automatizado.
3. **Planejar parallel run** — Se a estratégia permite, rodar legado e novo em paralelo em produção, comparando resultados sem afetar usuários.
4. **Definir testes de contrato para interfaces preservadas** — Interfaces que devem ser mantidas (contratos de compatibilidade) precisam de testes de contrato explícitos.
5. **Criar testes para cada fase incremental** — Cada fase tem seus próprios testes de validação. Falha em uma fase não bloqueia rollback.
6. **Planejar cobertura de caminhos reais** — Usar dados de produção para identificar os caminhos mais executados e garantir cobertura prioritária.

## Outputs

- Suite expandida de testes de caracterização
- Suite de testes de equivalência (legado vs. refatorado)
- Plano de parallel run (se aplicável)
- Testes de contrato para interfaces preservadas
- Testes de validação por fase incremental
- Mapa de cobertura por caminhos reais de uso

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Testes de caracterização | Comportamento atual capturado para cenários-chave | Sim |
| Testes de equivalência | Mesmos inputs, mesmos outputs entre legado e novo | Sim |
| Contratos de interface | Interfaces preservadas têm testes de contrato | Sim |
| Cobertura por uso real | Top 20 caminhos mais executados em produção cobertos | Sim |
| Testes por fase | Cada fase incremental tem validação independente | Sim |

## Próxima Fase

→ [07-readiness.md](./07-readiness.md) — Avaliação de prontidão para iniciar refatoração
