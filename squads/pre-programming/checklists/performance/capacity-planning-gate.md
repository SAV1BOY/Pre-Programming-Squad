# Capacity Planning Gate

## Propósito
Verificar se planejamento de capacidade foi realizado.

## Quando Usar
- Antes de avançar para a próxima fase do pipeline
- Em revisões de gate formais
- Quando há dúvida sobre prontidão para transição

---

## Como Verificar
Verificar SLAs definidos, confirmar capacity planning, validar load test criteria.

## Evidências Necessárias
SLAs documentados (p50, p95, p99), capacity projection, load test plan.

## Critérios de Passagem

### Obrigatórios (todos devem ser atendidos)
- [ ] Todos os artefatos da fase estão completos e revisados
- [ ] Revisão por pelo menos um par foi realizada
- [ ] Nenhuma ambiguidade crítica permanece aberta
- [ ] Stakeholders relevantes foram informados
- [ ] Registro no decision log está atualizado

### Recomendados (80%+ para GOLD)
- [ ] Documentação está atualizada e acessível
- [ ] Métricas de qualidade da fase estão dentro do aceitável
- [ ] Feedback de revisão foi incorporado
- [ ] Próxima fase tem inputs suficientes para iniciar

---

## Exemplo de Falha Quando Gate é Ignorado
Sem SLA de performance → query N+1 descoberta em produção → latência p99 de 12s → churn de 8%.

## Processo de Aprovação
1. Responsável pela fase submete artefatos para revisão
2. Reviewer verifica critérios obrigatórios com evidências
3. Gate passa se todos os obrigatórios estão atendidos com evidência
4. Itens recomendados não atendidos → registrar como improvement no RalphLoop
5. Gate falha → lista de gaps específicos retorna para correção

## Escalação
- Se gate falha 2x consecutivas → escalar para Pre-Programming Chief
- Se bloqueio externo → registrar em risk register e comunicar stakeholders
- Se gate requer expertise não disponível → acionar DeepResearch Squad
