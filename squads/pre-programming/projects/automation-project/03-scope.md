# Projeto de Automação — Fase 03: Escopo

## Objetivo da Fase

Definir quais etapas do processo serão automatizadas, em que ordem, e qual o nível de automação (total, parcial com aprovação humana, ou assistida).

## Agentes Envolvidos

- **Agente de Escopo** (líder da fase) — Define fases de automação e prioridade
- **Agente de Riscos** — Avalia risco de cada nível de automação

## Inputs

- Diagrama de fluxo completo (Fase 02)
- Catálogo de regras e exceções
- ROI calculado (Fase 01)
- Pontos de aprovação humana

## Atividades

1. **Classificar nível de automação por etapa** — Total (sem intervenção), parcial (human-in-the-loop para aprovação), ou assistida (ferramenta sugere, humano decide).
2. **Priorizar fases de automação** — Começar pela etapa com maior ROI e menor risco. Entregar valor incremental.
3. **Definir tratamento de exceções** — Para cada exceção: automatizar tratamento, escalar para humano, ou rejeitar e logar?
4. **Estabelecer limites de automação** — Valores acima de X requerem aprovação humana. Operações irreversíveis precisam de confirmação. Anomalias detectadas param a automação.
5. **Definir métricas de automação** — Taxa de sucesso (straight-through processing), taxa de exceção, tempo médio de execução, volume processado.
6. **Planejar fallback manual** — Se a automação falhar, como retomar manualmente? Processo manual documentado e praticado.

## Outputs

- Classificação de nível de automação por etapa
- Roadmap de fases com priorização por ROI x risco
- Tratamento de exceções definido
- Limites e guardrails da automação
- Métricas de automação definidas
- Plano de fallback manual

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Fases priorizadas | Ordem de implementação com justificativa | Sim |
| Exceções tratadas | Cada exceção tem caminho definido | Sim |
| Guardrails definidos | Limites para operações de risco | Sim |
| Fallback manual | Processo manual documentado como backup | Sim |
| Métricas definidas | STP rate, exceção rate, tempo de execução | Sim |

## Próxima Fase

→ [04-architecture.md](./04-architecture.md) — Arquitetura da automação e orquestração
