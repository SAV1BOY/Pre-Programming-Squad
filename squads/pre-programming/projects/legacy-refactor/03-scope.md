# Refatoração de Legado — Fase 03: Escopo

## Objetivo da Fase

Definir as fronteiras exatas do refactoring, a estratégia de isolamento e o que será preservado sem alteração. Em legado, o escopo mais perigoso é o indefinido.

## Agentes Envolvidos

- **Agente de Escopo** (líder da fase) — Define fronteiras e estratégia de isolamento
- **Agente de Riscos** — Avalia risco de cada nível de escopo
- **Agente de Arquitetura** — Valida viabilidade técnica do isolamento

## Inputs

- Mapa de dependências (Fase 02)
- Testes de caracterização (Fase 02)
- Pontos de acoplamento identificados
- Motivação quantificada (Fase 01)

## Atividades

1. **Definir boundary do refactoring** — Traçar linha clara entre "dentro do refactoring" e "fora — não tocar". Boundary deve ser em ponto de interface natural (API, evento, tabela compartilhada).
2. **Escolher estratégia de isolamento:**
   - **Strangler Fig:** Construir novo ao lado do legado, migrar tráfego gradualmente
   - **Branch by Abstraction:** Criar interface, implementar novo atrás dela, trocar implementação
   - **Parallel Run:** Rodar legado e novo em paralelo, comparar resultados
   - **Big Bang:** Substituir de uma vez (alto risco, raramente recomendado)
3. **Priorizar áreas de refactoring** — Começar pela área com maior dor E menor risco. Mapa de calor: (frequência de bugs x facilidade de isolamento).
4. **Definir contratos de compatibilidade** — Interfaces que devem ser mantidas para que consumidores não sejam afetados durante o refactoring.
5. **Estabelecer critérios de equivalência** — Como provar que o código refatorado produz os mesmos resultados que o legado. Testes de caracterização são a base.
6. **Definir fases incrementais** — Refactoring de legado nunca deve ser big bang. Dividir em fases deployáveis e verificáveis independentemente.

## Outputs

- Boundary do refactoring com diagrama
- Estratégia de isolamento escolhida com justificativa
- Priorização de áreas (mapa de calor: dor x risco)
- Contratos de compatibilidade documentados
- Critérios de equivalência comportamental
- Plano de fases incrementais

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Boundary definido | Linha clara entre dentro e fora do refactoring | Sim |
| Estratégia escolhida | Isolamento com justificativa (não big bang por default) | Sim |
| Contratos de compatibilidade | Interfaces preservadas documentadas | Sim |
| Fases incrementais | Refactoring dividido em partes deployáveis | Sim |
| Critérios de equivalência | Como provar que refatorado = legado comportamentalmente | Sim |

## Próxima Fase

→ [04-architecture.md](./04-architecture.md) — Design da arquitetura-alvo e plano de transição
