# Pipeline Orchestration Gate

## Propósito
Verificar se o pipeline está corretamente orquestrado entre fases.

## Quando Usar
- Antes de avançar para a próxima fase do pipeline
- Em revisões de gate formais
- Quando há dúvida sobre prontidão para transição

---

## Como Verificar
Revisar decision log, verificar que todos os agentes necessários foram acionados, confirmar que win condition está clara.

## Evidências Necessárias
Decision log atualizado, timeline documentado, stakeholder communication log.

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
Pipeline pulou fase de discovery por pressão de prazo → 40% de rework no coding.

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
