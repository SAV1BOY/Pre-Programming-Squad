# Projeto de Automação — Fase 02: Discovery

## Objetivo da Fase

Mapear o processo completo em detalhes suficientes para automação: cada decisão, exceção, transformação de dados e interação entre sistemas.

## Agentes Envolvidos

- **Agente de Requisitos** (líder da fase) — Mapeia processo e regras
- **Agente de Arquitetura** — Identifica integrações e fluxo de dados

## Inputs

- Processo candidato validado (Fase 01)
- Acesso aos executores do processo para observação
- Documentação de processo existente
- Logs ou registros de execuções anteriores

## Atividades

1. **Mapear fluxo completo** — Diagrama BPMN ou flowchart com: início, fim, decisões, loops, exceções. Cada passo com input, transformação e output.
2. **Documentar regras de decisão** — Cada ponto de decisão no processo com regras explícitas. Converter "julgamento do operador" em regras automatizáveis ou identificar como necessidade de aprovação humana.
3. **Catalogar exceções** — Listar todos os cenários de exceção: dados incompletos, formato inesperado, sistema indisponível, regra não aplicável. Para cada exceção: como é tratada hoje?
4. **Mapear transformações de dados** — Cada transformação de dados entre sistemas: formato de entrada, formato de saída, regras de conversão, tratamento de valores nulos.
5. **Identificar pontos de aprovação humana** — Quais etapas DEVEM manter aprovação humana (regulatório, risco)? Human-in-the-loop vs. fully automated.
6. **Medir SLAs do processo atual** — Tempo de cada etapa, gargalos, tempo total end-to-end. Baseline para comparação pós-automação.

## Outputs

- Diagrama de fluxo do processo (BPMN ou flowchart)
- Catálogo de regras de decisão
- Lista de exceções com tratamento atual
- Mapeamento de transformações de dados
- Pontos de aprovação humana identificados
- SLAs e baseline do processo atual

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Fluxo completo | Todos os caminhos (incluindo exceções) mapeados | Sim |
| Regras explícitas | Cada decisão traduzida em regra automatizável | Sim |
| Exceções catalogadas | Tratamento para cada exceção definido | Sim |
| Human-in-the-loop | Pontos que requerem aprovação humana identificados | Sim |

## Próxima Fase

→ [03-scope.md](./03-scope.md) — Definição do que será automatizado em cada fase
