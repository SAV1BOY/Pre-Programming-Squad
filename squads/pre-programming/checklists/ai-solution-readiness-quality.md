# Checklist: Qualidade da Prontidão de Solução com IA

## Propósito
Garantir que soluções que envolvem IA/LLM têm prompts, avaliações, guardrails, fallbacks e observabilidade definidos antes da implementação.

## Quando Usar
- Quando a solução envolve modelos de IA, LLMs ou ML
- Ao planejar funcionalidades com geração de conteúdo, classificação ou predição
- Antes de implementar integrações com APIs de IA (OpenAI, Anthropic, etc.)

---

## Checklist

### Prompts e Instruções
- [ ] Prompts estão documentados com versão e propósito de cada um
- [ ] System prompts definem comportamento, tom e limitações do modelo
- [ ] Few-shot examples estão incluídos quando necessário
- [ ] Formato de output esperado está especificado (JSON, texto, etc.)
- [ ] Prompts foram testados com variações de input para validar robustez

### Avaliações (Evals)
- [ ] Dataset de avaliação está definido com inputs e outputs esperados
- [ ] Métricas de qualidade estão definidas (precisão, recall, relevância, etc.)
- [ ] Baseline de qualidade aceitável está estabelecido
- [ ] Processo de avaliação contínua está planejado (não apenas uma vez)
- [ ] Evals cobrem edge cases e inputs adversariais

### Guardrails
- [ ] Limites de input estão definidos (tamanho, formato, conteúdo)
- [ ] Filtros de output estão planejados (conteúdo inadequado, alucinações)
- [ ] Validação de output antes de apresentar ao usuário está definida
- [ ] Limites de custo/uso estão configurados (rate limiting, budget)
- [ ] Política de dados sensíveis enviados ao modelo está definida

### Fallback
- [ ] Comportamento quando o modelo falha está definido
- [ ] Comportamento quando o modelo retorna resposta inadequada está definido
- [ ] Fallback para abordagem não-IA existe (regras, busca, humano)
- [ ] Timeout e retry strategy para chamadas ao modelo estão definidos
- [ ] Degradação graceful está planejada (funcionalidade sem IA)

### Observabilidade de IA
- [ ] Logging de inputs e outputs do modelo está planejado (com privacidade)
- [ ] Métricas de uso, latência e custo do modelo estão definidas
- [ ] Monitoramento de qualidade das respostas em produção está planejado
- [ ] Alertas para degradação de qualidade estão definidos
- [ ] Feedback loop para melhoria contínua está desenhado

---

## Critérios de Aprovação
- **Mínimo**: Prompts, Guardrails e Fallback completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Nenhum eval definido ou sem fallback para falha do modelo

## Sinais de Alerta (Red Flags)
- "O modelo vai resolver" sem definir o que acontece quando não resolve
- Prompts criados ad-hoc sem versionamento ou teste
- Nenhum guardrail para conteúdo gerado pelo modelo
- Dados sensíveis (PII) enviados ao modelo sem política de tratamento
- Custo de API de IA não estimado ou sem limite

## Agente Responsável
**Agente de Solution Architecture** — em colaboração com especialistas de IA/ML quando disponível.
