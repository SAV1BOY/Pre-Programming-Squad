# Checklist: Auditoria Simplicidade vs Robustez

## Propósito
Verificar se o nível de robustez da solução é adequado ao contexto, sem sub-engenharia (solução frágil) nem over-engenharia (solução complexa demais para o problema).

## Quando Usar
- Ao avaliar propostas de arquitetura
- Quando há debate entre "fazer simples" e "fazer robusto"
- Quando a solução parece desproporcional ao problema

---

## Checklist

### Nível Adequado
- [ ] O nível de robustez está calibrado para o risco real (não o imaginário)
- [ ] Soluções para problemas de baixo impacto são simples
- [ ] Soluções para problemas de alto impacto são robustas
- [ ] O nível de engineering está proporcional à vida útil esperada da solução
- [ ] O nível de engineering está proporcional ao número de usuários/transações

### Evitando Over-Engineering
- [ ] Patterns complexos (CQRS, Event Sourcing, Saga) são usados apenas quando necessário
- [ ] Abstrações são criadas quando há necessidade real, não especulativa
- [ ] Configurabilidade é limitada ao que realmente varia (não "tudo é configurável")
- [ ] Generalização é feita quando há 3+ casos de uso, não com o primeiro
- [ ] Performance optimization é baseada em medição, não em intuição

### Evitando Sub-Engineering
- [ ] Funcionalidades críticas têm tratamento de erro adequado
- [ ] Dados críticos têm backup e recovery
- [ ] Segurança não foi sacrificada por simplicidade
- [ ] Monitoramento mínimo está presente para detectar problemas
- [ ] A solução não quebra catastroficamente sob carga moderada

### Calibração
- [ ] A criticidade do sistema está classificada (low/medium/high/critical)
- [ ] O SLA esperado está definido e a solução o suporta
- [ ] Custo de downtime está estimado para calibrar investimento em robustez
- [ ] Time-to-market foi balanceado com robustez adequada
- [ ] Dívida técnica aceita está documentada com plano de pagamento

### Decisão Consciente
- [ ] Trade-offs entre simplicidade e robustez estão documentados
- [ ] Stakeholders entendem o que está sendo sacrificado (e concordam)
- [ ] A decisão é revisável (pode-se adicionar robustez depois sem reescrever)
- [ ] O que é "bom o suficiente" para a v1 está definido
- [ ] Critérios para quando investir mais em robustez estão definidos

---

## Critérios de Aprovação
- **Mínimo**: Nível Adequado e Decisão Consciente completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Solução sub-engenheirada para sistema crítico ou over-engenheirada sem justificativa

## Sinais de Alerta (Red Flags)
- Kafka + Kubernetes + microsserviços para POC interna com 10 usuários
- Sistema financeiro sem tratamento de concorrência ou idempotência
- "Depois a gente refatora" como justificativa para código frágil em sistema crítico
- Três meses de arquitetura para projeto de duas semanas
- "Sempre usamos esse pattern" sem avaliar se é adequado ao caso

## Agente Responsável
**Agente de Solution Architecture** — responsável por calibrar o nível adequado de engineering.
