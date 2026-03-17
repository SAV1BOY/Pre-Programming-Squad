# Projeto de Agente IA — Fase 06: Testes

## Objetivo da Fase

Definir framework de evals abrangente: qualidade de respostas, segurança, performance e custo. Evals são para agentes de IA o que testes automatizados são para software tradicional.

## Agentes Envolvidos

- **Agente de Testes** (líder da fase) — Desenha framework de evals
- **Agente de Riscos** — Garante cobertura de cenários adversariais

## Inputs

- Golden examples dataset (Fase 02)
- Red team playbook (Fase 05)
- Guardrails e critérios de aceitação (Fase 03)
- Métricas de eval definidas (Fase 02)

## Atividades

1. **Implementar evals de qualidade** — Para cada categoria de cenário: accuracy (resposta correta), relevance (resposta útil), faithfulness (baseada em dados, não fabricada), coherence (resposta coerente e bem estruturada).
2. **Implementar evals de segurança** — Prompt injection resistance, PII detection em outputs, toxicity detection, off-topic detection, guardrail compliance.
3. **Implementar red team evals** — Executar playbook de red team automaticamente: tentativas de jailbreak, role hijacking, data exfiltration, instruction override. Score: % de ataques bloqueados.
4. **Implementar evals de RAG** — Se usa retrieval: retrieval accuracy (documentos corretos recuperados), answer grounding (resposta baseada no documento), context relevance.
5. **Definir evals em CI/CD** — Evals executam automaticamente em cada mudança de prompt, guardrail ou pipeline. Regressão de qualidade bloqueia deploy.
6. **Planejar human eval periódico** — Amostra de interações reais avaliadas por humanos mensalmente. Calibra evals automáticos e detecta problemas que automação não pega.
7. **Definir benchmark de custo e latência** — Custo médio por interação, latência p50 e p99, tokens médios por request. Alertas se excederem thresholds.

## Outputs

- Framework de evals com métricas por categoria
- Suite de evals de segurança (prompt injection, PII, toxicity)
- Red team evals automatizados
- Evals de RAG (se aplicável)
- Pipeline de evals em CI/CD
- Plano de human eval periódico
- Benchmark de custo e latência

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Evals de qualidade | Accuracy, relevance e faithfulness medidos | Sim |
| Evals de segurança | Prompt injection e PII detection implementados | Sim |
| Red team | >= 95% de ataques bloqueados | Sim |
| CI/CD integrado | Evals executam em cada mudança | Sim |
| Human eval planejado | Processo de avaliação humana periódica definido | Sim |

## Próxima Fase

→ [07-readiness.md](./07-readiness.md) — Avaliação de prontidão para lançamento do agente
