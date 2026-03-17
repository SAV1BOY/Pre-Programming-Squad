# Projeto de Agente IA — Fase 03: Escopo

## Objetivo da Fase

Definir capacidades e limites do agente, estabelecer guardrails de segurança e definir o que o agente NÃO deve fazer.

## Agentes Envolvidos

- **Agente de Escopo** (líder da fase) — Define capacidades e limites
- **Agente de Riscos** — Define guardrails e restrições de segurança

## Inputs

- Cenários de uso e failure modes (Fase 02)
- Requisitos de confiança (Fase 01)
- Benchmark de modelos (Fase 02)

## Atividades

1. **Definir capacidades do agente (can do)** — Lista explícita do que o agente pode fazer. Cada capacidade com exemplo e nível de confiança.
2. **Definir limites do agente (cannot do)** — Lista explícita do que o agente NÃO deve fazer. Tão importante quanto capacidades. Incluir: fora do domínio, ações perigosas, informações que não deve fornecer.
3. **Estabelecer guardrails** — Regras que o agente sempre segue:
   - Não executar ações irreversíveis sem confirmação humana
   - Não fornecer informações quando confiança é baixa (dizer "não sei")
   - Não reter PII em logs
   - Escalar para humano quando detectar frustração ou cenário complexo
4. **Definir system prompt** — Draft do system prompt com persona, instruções, limitações e formato de resposta. Iterar com base nos evals.
5. **Definir escalação** — Quando o agente deve parar e escalar para humano? Critérios explícitos: confiança abaixo de X, cenário fora do escopo, número de tentativas excedido.
6. **Estabelecer critérios de aceitação** — Score mínimo nos evals para lançamento. Score por categoria (accuracy, safety, relevance).

## Outputs

- Lista de capacidades (can do) com nível de confiança
- Lista de limitações (cannot do) com justificativa
- Guardrails documentados
- Draft do system prompt
- Critérios de escalação para humano
- Critérios de aceitação para lançamento (scores mínimos)

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Capacidades explícitas | Lista de "can do" com exemplos | Sim |
| Limitações explícitas | Lista de "cannot do" com justificativa | Sim |
| Guardrails definidos | Regras de segurança e comportamento | Sim |
| Escalação definida | Critérios para escalar a humano | Sim |
| Critérios de aceitação | Scores mínimos de evals para lançamento | Sim |

## Próxima Fase

→ [04-architecture.md](./04-architecture.md) — Arquitetura do agente, RAG, tools e orquestração
