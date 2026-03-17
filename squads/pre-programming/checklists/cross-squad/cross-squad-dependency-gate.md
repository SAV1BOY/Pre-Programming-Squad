# Cross-Squad Dependency Gate

## Propósito
Verificar se dependências cross-squad estão mapeadas e gerenciadas.

## Quando Usar
- Antes de avançar para a próxima fase do pipeline
- Em revisões de gate formais
- Quando há dúvida sobre prontidão para transição

---

## Como Verificar
Verificar contratos cross-squad, confirmar dependências rastreadas, validar aceite bilateral.

## Evidências Necessárias
Cross-squad handoff registry, SLA agreements, dependency board.

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
Dependência cross-squad não rastreada → bloqueio silencioso de 2 semanas → deadline perdido.

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
