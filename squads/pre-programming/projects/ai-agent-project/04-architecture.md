# Projeto de Agente IA — Fase 04: Arquitetura

## Objetivo da Fase

Definir arquitetura do agente incluindo: model provider, RAG pipeline, tool calling, memória, orquestração e guardrails técnicos.

## Agentes Envolvidos

- **Agente de Arquitetura** (líder da fase) — Desenha arquitetura do agente
- **Agente de Riscos** — Valida guardrails técnicos e segurança

## Inputs

- Modelo escolhido e benchmark (Fase 02)
- Capacidades, limites e guardrails (Fase 03)
- System prompt draft (Fase 03)
- Knowledge base mapeada (Fase 02)

## Atividades

1. **Definir arquitetura do agente** — Componentes: Model Provider (API), Prompt Manager, RAG Pipeline (se aplicável), Tool Executor, Memory Store, Guardrail Engine, Logger.
2. **Desenhar RAG pipeline** — Se o agente usa retrieval: indexação de documentos, chunking strategy, embedding model, vector store, retrieval strategy (similarity, hybrid, reranking).
3. **Definir tool calling** — Quais ferramentas o agente pode invocar? APIs, banco de dados, cálculos? Cada tool com: descrição, parâmetros, permissões, timeout, tratamento de erro.
4. **Planejar memória** — Tipo de memória: sem memória (stateless), memória de sessão (conversação), memória de longo prazo (perfil do usuário). Trade-off: custo de contexto vs. qualidade.
5. **Implementar guardrails técnicos** — Input validation (prompt injection detection), output filtering (PII, toxicity, off-topic), rate limiting, cost caps.
6. **Definir fallback strategy** — Se o model provider está indisponível: fallback para modelo alternativo? Mensagem de indisponibilidade? Cache de respostas frequentes?
7. **Planejar observabilidade** — Logs de cada interação: input, output, model, latência, tokens, custo. Dashboard de qualidade em tempo real.

## Outputs

- Diagrama de arquitetura do agente
- Design do RAG pipeline (se aplicável)
- Catálogo de tools com permissões e limites
- Design de memória e gestão de contexto
- Guardrails técnicos (input validation, output filtering)
- Fallback strategy para indisponibilidade do modelo
- Plano de observabilidade (logs, métricas, dashboard)

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Guardrails técnicos | Prompt injection e output filtering implementados | Sim |
| Tools seguros | Cada tool com permissões e timeout | Sim |
| Fallback definido | Comportamento em indisponibilidade do modelo | Sim |
| Observabilidade | Logs de interação e dashboard planejados | Sim |
| Cost cap | Limite de custo por request e mensal | Sim |

## Próxima Fase

→ [05-risks.md](./05-risks.md) — Riscos específicos de agentes de IA
