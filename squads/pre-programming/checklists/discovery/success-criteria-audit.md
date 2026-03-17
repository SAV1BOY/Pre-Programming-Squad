# Checklist: Auditoria de Critérios de Sucesso

## Propósito
Verificar se existe definição clara e mensurável de como saber que o projeto deu certo, evitando situações onde "sucesso" é subjetivo ou indefinido.

## Quando Usar
- Após definição do problema e antes de definir solução
- Quando não há consenso sobre o que é "pronto" ou "bom o suficiente"
- Em revisões de escopo e priorização

---

## Checklist

### Definição de Sucesso
- [ ] Critérios de sucesso estão escritos de forma mensurável e verificável
- [ ] Existe diferença clara entre sucesso mínimo e sucesso ideal
- [ ] Critérios de sucesso estão vinculados ao problema original (não a métricas aleatórias)
- [ ] Sucesso técnico está diferenciado de sucesso de negócio
- [ ] Critérios negativos estão definidos (o que NÃO pode acontecer para ser sucesso)

### Métricas
- [ ] Métricas quantitativas estão definidas com valores-alvo específicos
- [ ] Baseline atual de cada métrica está documentado (antes do projeto)
- [ ] Fonte de dados para cada métrica está identificada
- [ ] Frequência de medição está definida
- [ ] Responsável por coletar e reportar métricas está designado

### Verificação
- [ ] Método de verificação para cada critério está definido (teste, métrica, aprovação)
- [ ] Prazo para verificação está definido (quando medir após o deploy)
- [ ] Ambiente de verificação está definido (produção, staging, etc.)
- [ ] Quem valida o sucesso está definido (Product, Tech Lead, Stakeholder)
- [ ] Existe distinção entre verificação automática e manual

### Alinhamento
- [ ] Critérios de sucesso foram validados com o sponsor do projeto
- [ ] Critérios de sucesso foram validados com o time de implementação
- [ ] Não há conflito entre critérios de sucesso de diferentes stakeholders
- [ ] Critérios são atingíveis dentro das restrições do projeto
- [ ] Mudanças nos critérios de sucesso são versionadas e comunicadas

### Cenários de Insucesso
- [ ] Critérios de fracasso estão definidos (quando considerar que não deu certo)
- [ ] Plano de ação para caso de insucesso está delineado
- [ ] Ponto de decisão go/no-go pós-launch está planejado
- [ ] Custo de insucesso está estimado
- [ ] Aprendizados de insucesso serão capturados (post-mortem planejado)

---

## Critérios de Aprovação
- **Mínimo**: Definição de Sucesso e Métricas completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Nenhum critério de sucesso mensurável definido

## Sinais de Alerta (Red Flags)
- "Sucesso é quando o stakeholder gostar" (subjetivo)
- Métricas sem baseline (impossível medir melhoria)
- Critérios de sucesso que não se relacionam com o problema original
- Ninguém definido como responsável por medir o sucesso
- Critérios impossíveis de atingir nas restrições do projeto

## Agente Responsável
**Agente de Discovery & Framing** — responsável por definir e validar critérios de sucesso claros.
