# Nova Feature — Fase 03: Escopo

## Objetivo da Fase

Definir com precisão o que será construído e o que ficará de fora, priorizar cenários de uso e estabelecer critérios de aceitação mensuráveis.

## Agentes Envolvidos

- **Agente de Escopo** (líder da fase) — Define fronteiras e prioridades
- **Agente de Requisitos** — Garante que escopo é consistente com discovery

## Inputs

- Documento de discovery (Fase 02)
- Cenários de uso documentados
- Restrições conhecidas
- Contexto de prioridade de negócio (prazo, budget, dependencies)

## Atividades

1. **Priorizar cenários de uso** — Classificar cada cenário como Must Have (P0), Should Have (P1), Nice to Have (P2) usando critério de impacto x esforço estimado
2. **Definir MVP** — Conjunto mínimo de cenários que entrega valor. Deve ser deployável e usável independentemente.
3. **Documentar não-escopo** — Para cada item fora do escopo, registrar motivo e quando será reconsiderado (próximo quarter, nunca, sob demanda)
4. **Estabelecer critérios de aceitação** — Para cada cenário P0 e P1, definir critérios mensuráveis de aceitação (Given-When-Then ou equivalente)
5. **Estimar tamanho relativo** — Sizing alto nível (S/M/L/XL) para calibrar expectativas de prazo com stakeholder
6. **Validar escopo com stakeholder** — Apresentar escopo, não-escopo e priorização para aprovação formal

## Outputs

- Documento de escopo com cenários priorizados (P0, P1, P2)
- Definição de MVP
- Lista de não-escopo com justificativas
- Critérios de aceitação para P0 e P1
- Sizing relativo do projeto
- Aprovação formal do stakeholder

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| MVP definido | Conjunto mínimo de cenários que entrega valor identificável | Sim |
| Não-escopo explícito | Lista de itens fora do escopo com justificativa | Sim |
| Critérios mensuráveis | Cada cenário P0 tem critério de aceitação verificável | Sim |
| Stakeholder aprovou | Escopo e não-escopo validados formalmente | Sim |
| Sizing realista | Estimativa de tamanho coerente com restrições de prazo | Sim |

## Próxima Fase

→ [04-architecture.md](./04-architecture.md) — Design da solução técnica, alternativas e decisões arquiteturais
