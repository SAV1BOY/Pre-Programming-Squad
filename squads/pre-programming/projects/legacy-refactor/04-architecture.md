# Refatoração de Legado — Fase 04: Arquitetura

## Objetivo da Fase

Definir a arquitetura-alvo do código refatorado e o plano de transição do estado atual para o desejado, mantendo o sistema funcional em todos os estados intermediários.

## Agentes Envolvidos

- **Agente de Arquitetura** (líder da fase) — Desenha arquitetura-alvo e caminho de transição
- **Agente de Riscos** — Avalia riscos de cada estado intermediário
- **Agente de Escopo** — Valida que arquitetura está dentro do boundary definido

## Inputs

- Boundary e estratégia de isolamento (Fase 03)
- Mapa de dependências atual (Fase 02)
- Contratos de compatibilidade (Fase 03)
- Fases incrementais definidas (Fase 03)

## Atividades

1. **Desenhar arquitetura-alvo** — Como o código refatorado se organiza. Focar em: separação de responsabilidades, interfaces limpas, testabilidade.
2. **Mapear caminho de transição** — Para cada fase incremental, definir o estado intermediário do sistema. Cada estado deve ser deployável e funcional.
3. **Definir anti-corruption layer** — Camada que isola código novo do legado durante a transição. Traduz entre modelos antigo e novo.
4. **Planejar migração de dados** — Se o refactoring muda modelo de dados, definir estratégia: dual-write, migração online, ETL batch.
5. **Definir feature flags de transição** — Flags que permitem alternar entre código legado e refatorado por cenário, facilitando rollback parcial.
6. **Avaliar impacto em observabilidade** — Métricas e logs do legado devem ser mantidos durante transição. Novas métricas adicionadas para código refatorado.

## Outputs

- Diagrama de arquitetura-alvo
- Plano de transição estado-por-estado
- Design do anti-corruption layer
- Estratégia de migração de dados (se aplicável)
- Mapa de feature flags de transição
- Plano de observabilidade durante e após transição

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Arquitetura-alvo definida | Diagrama com interfaces e responsabilidades claras | Sim |
| Estados intermediários viáveis | Cada estado é deployável e funcional | Sim |
| Anti-corruption layer | Isolamento entre legado e novo durante transição | Sim |
| Feature flags de transição | Alternância entre legado e novo por cenário | Sim |
| Migração de dados planejada | Se aplicável, estratégia com rollback definida | Condicional |

## Próxima Fase

→ [05-risks.md](./05-risks.md) — Riscos específicos de refatoração de legado
