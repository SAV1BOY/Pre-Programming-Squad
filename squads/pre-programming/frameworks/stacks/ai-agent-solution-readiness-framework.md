# AI Agent Solution Readiness Framework

## Título e Propósito

O **AI Agent Solution Readiness Framework** é um checklist para avaliar se um projeto que envolve agentes de IA (LLMs, RAG, agentes autônomos) está pronto para implementação. O propósito é combater o hype cycle — garantindo que a equipe tenha clareza sobre onde IA agrega valor real, onde as limitações tornam a solução inadequada, e que aspectos como avaliação, segurança e custo estejam planejados.

## Quando Usar

- Antes de implementar qualquer solução baseada em LLMs ou agentes de IA
- Ao avaliar se um problema é melhor resolvido com IA ou com lógica tradicional
- Em projetos de RAG (Retrieval-Augmented Generation)
- Quando stakeholders pedem "usar IA" sem caso de uso claro
- Para avaliar riscos específicos de soluções baseadas em IA

## Conceitos-Chave

1. **IA vs. Regras**: Nem todo problema precisa de IA. Se as regras são claras e estáveis, lógica determinística é mais confiável e barata.
2. **Avaliação (Eval)**: Como medir se o agente está funcionando bem? Sem eval, é impossível iterar.
3. **Alucinação**: LLMs geram texto convincente que pode ser factualmente errado. O impacto de alucinação deve ser avaliado.
4. **Custo por Chamada**: LLMs têm custo por token. Em escala, o custo pode ser proibitivo se não planejado.
5. **Human-in-the-Loop**: Para decisões de alto risco, o agente sugere e o humano decide. Full autonomy é raramente adequado.
6. **Guardrails**: Limites que impedem o agente de tomar ações perigosas ou fora do escopo.

## Processo / Passos

### Passo 1 — Validar se IA é a Solução Certa
O problema requer raciocínio flexível, linguagem natural, ou classificação com muitas nuances? Se as regras são claras e estáveis, considere lógica tradicional.

### Passo 2 — Definir o Problema com Precisão
"Usar IA para melhorar o suporte" não é problema definido. "Classificar tickets de suporte nas 15 categorias existentes com >90% de acurácia" é.

### Passo 3 — Definir Métricas de Avaliação
Como medir se funciona? Acurácia, F1-score, taxa de alucinação, latência, custo por chamada, satisfação do usuário.

### Passo 4 — Avaliar Riscos de Alucinação
Se o agente alucinar, qual é o impacto? Informação errada para cliente? Decisão financeira errada? O risco determina o nível de guardrails.

### Passo 5 — Projetar Guardrails
Limites de ação, validação de output, escalação para humano, filtros de conteúdo, rate limiting, logging de todas as interações.

### Passo 6 — Estimar Custos
Custo por token × volume esperado × crescimento. Comparar com custo da solução atual (manual ou automatizada).

### Passo 7 — Definir Estratégia de Dados
Para RAG: qual a fonte de dados? Como é indexada? Como é atualizada? Para fine-tuning: há dados de treino suficientes e de qualidade?

## Perguntas de Ativação

- "Esse problema realmente precisa de IA ou regras claras resolveriam?"
- "Se o agente der uma resposta errada, qual é o impacto?"
- "Como vamos medir se o agente está funcionando bem?"
- "Qual é o custo por interação e é sustentável no volume esperado?"
- "Quem revisa as decisões do agente? Há human-in-the-loop?"
- "Os dados de contexto (para RAG) estão disponíveis, atualizados e de qualidade?"

## Output Esperado

Avaliação cobrindo: justificativa para IA vs. alternativas, métricas de eval, análise de risco de alucinação, guardrails projetados, estimativa de custo, estratégia de dados.

## Armadilhas Comuns

1. **IA como martelo**: Usar IA porque é tendência, não porque é a melhor solução para o problema.
2. **Sem eval**: Lançar agente sem métricas de qualidade. Sem eval, não se pode iterar nem detectar degradação.
3. **Ignorar alucinação**: "O modelo é bom" não é garantia de zero alucinações. Todo LLM alucina.
4. **Custo não projetado**: API de LLM que custa $0.01 por chamada × 1M chamadas/mês = $10k/mês. Surpresa?
5. **Dados ruins para RAG**: "Garbage in, garbage out" é ainda mais verdadeiro com IA. Dados desatualizados ou incorretos degradam output.
6. **Full autonomy prematura**: Deixar o agente tomar decisões sem revisão humana em domínios de alto risco.
