# Projeto de Agente IA — Fase 05: Riscos

## Objetivo da Fase

Identificar e mitigar riscos específicos de agentes de IA: alucinação, prompt injection, vazamento de dados, bias, dependência de modelo externo e degradação de qualidade ao longo do tempo.

## Agentes Envolvidos

- **Agente de Riscos** (líder da fase) — Identifica riscos de IA
- **Agente de Arquitetura** — Valida mitigações técnicas
- **Agente de Testes** — Prepara cenários adversariais

## Inputs

- Arquitetura do agente (Fase 04)
- Failure modes de IA (Fase 02)
- Guardrails definidos (Fases 03-04)
- Compliance checklist (Fase 01)

## Atividades

1. **Avaliar risco de alucinação** — Em quais cenários o modelo pode fabricar informações? Qual o impacto? Mitigação: grounding em knowledge base, citation obrigatório, confidence score.
2. **Avaliar risco de prompt injection** — Usuários podem manipular o agente via inputs maliciosos? Testar: jailbreak attempts, role hijacking, instruction override. Mitigação: input sanitization, system prompt robusto.
3. **Avaliar risco de vazamento de dados** — O modelo pode expor dados sensíveis do system prompt, knowledge base ou dados de outros usuários? Mitigação: output filtering, session isolation.
4. **Avaliar risco de bias** — O modelo tem vieses que afetam decisões (gênero, etnia, idade)? Testar com inputs que exponham viés. Mitigação: eval de fairness, auditoria periódica.
5. **Avaliar risco de dependência de provedor** — Se OpenAI/Anthropic mudar preço, API ou descontinuar modelo? Mitigação: abstração de model provider, fallback para modelo alternativo.
6. **Avaliar risco de degradação** — Qualidade do modelo pode mudar com atualizações do provedor. Evals automatizados detectam degradação? Mitigação: evals em CI/CD, alertas de degradação.
7. **Avaliar risco de custo descontrolado** — Volume inesperado ou prompts longos podem gerar custos altos. Mitigação: cost caps, rate limiting, monitoramento de custo em tempo real.

## Outputs

- Matriz de riscos de IA com severidade e probabilidade
- Red team playbook (cenários de prompt injection e jailbreak)
- Plano de mitigação de alucinação
- Avaliação de bias com plano de auditoria
- Plano de contingência para mudança de provedor
- Plano de monitoramento de degradação
- Budget cap e alertas de custo

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Red team testado | Cenários de prompt injection e jailbreak testados | Sim |
| Alucinação mitigada | Grounding e/ou confidence threshold definidos | Sim |
| Vazamento prevenido | Output filtering e session isolation testados | Sim |
| Cost cap definido | Limites de custo com alertas configurados | Sim |
| Degradação monitorável | Evals automatizados para detectar mudança de qualidade | Sim |

## Próxima Fase

→ [06-tests.md](./06-tests.md) — Framework de evals, testes adversariais e benchmarking
