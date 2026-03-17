# Projeto de Agente IA — Fase 02: Discovery

## Objetivo da Fase

Explorar o domínio em profundidade, avaliar capacidades dos modelos disponíveis, definir métricas de avaliação (evals) e criar dataset de benchmark.

## Agentes Envolvidos

- **Agente de Requisitos** (líder da fase) — Mapeia cenários e expectativas de comportamento
- **Agente de Testes** — Começa a definir framework de evals

## Inputs

- Tipo de agente e requisitos de confiança (Fase 01)
- Dados disponíveis
- Exemplos de interações esperadas (inputs e outputs ideais)
- Domínio de conhecimento do agente

## Atividades

1. **Mapear cenários de uso** — Catalogar todos os tipos de input que o agente receberá: perguntas simples, complexas, ambíguas, fora do escopo, adversariais.
2. **Criar dataset de golden examples** — Conjunto curado de inputs com outputs esperados. Base para evals. Mínimo de 50 exemplos cobrindo variedade de cenários.
3. **Testar modelos candidatos** — Executar golden examples em modelos candidatos (GPT-4, Claude, modelos open-source). Comparar qualidade, latência e custo.
4. **Definir métricas de eval** — Para cada tipo de cenário: métrica de qualidade (accuracy, relevance, faithfulness), métrica de segurança (toxicity, PII leakage), métrica de performance (latência, custo por request).
5. **Mapear knowledge base** — Se o agente usa RAG: quais documentos? Como são indexados? Qual a qualidade do retrieval? Testar com perguntas que exigem retrieval.
6. **Identificar failure modes de IA** — Cenários onde o modelo falha: ambiguidade, domínio desconhecido, instruções conflitantes, context window excedido. Documentar e planejar tratamento.
7. **Avaliar custo operacional** — Custo por request estimado. Volume projetado. Custo mensal estimado. Compare com valor entregue.

## Outputs

- Catálogo de cenários de uso com exemplos
- Dataset de golden examples (50+ exemplos)
- Benchmark comparativo de modelos candidatos
- Framework de evals com métricas definidas
- Mapeamento de knowledge base (se RAG)
- Catálogo de failure modes de IA
- Estimativa de custo operacional

## Gates de Qualidade

| Gate | Critério | Obrigatório |
|------|----------|-------------|
| Golden examples | Dataset com 50+ exemplos curados | Sim |
| Modelos testados | Pelo menos 2 modelos comparados | Sim |
| Evals definidos | Métricas de qualidade e segurança explícitas | Sim |
| Failure modes | Cenários de falha de IA documentados | Sim |
| Custo estimado | Custo mensal projetado vs. valor entregue | Sim |

## Próxima Fase

→ [03-scope.md](./03-scope.md) — Definição de capacidades do agente, limites e guardrails
