# Checklist: Qualidade da Readiness Review

## Propósito
Verificar se o projeto está pronto para avançar para implementação (Go/No-Go), consolidando o resultado de todas as análises anteriores.

## Quando Usar
- Como gate final antes de autorizar início da implementação
- Após todas as análises de pré-programação estarem concluídas
- Quando há dúvida se o time pode começar a codar

---

## Checklist

### Clareza do Problema
- [ ] Problema está definido e validado com stakeholders
- [ ] Causa raiz está identificada (não apenas sintoma)
- [ ] Critérios de sucesso estão quantificados
- [ ] Escopo está delimitado com MVP claro
- [ ] Premissas estão documentadas e validadas

### Solução Definida
- [ ] Solução escolhida tem justificativa documentada
- [ ] Arquitetura está desenhada com módulos e fronteiras claras
- [ ] Contratos de API estão definidos
- [ ] Modelo de domínio está validado
- [ ] Integrações estão mapeadas com planos de contingência

### Riscos Mapeados
- [ ] Modos de falha estão identificados com mitigações
- [ ] Riscos de segurança foram avaliados
- [ ] Performance e escalabilidade estão planejadas
- [ ] Compatibilidade com legado está resolvida
- [ ] Estratégia de rollback existe para deploy e dados

### Testes Planejados
- [ ] Estratégia de testes está definida por nível (unit, integration, e2e)
- [ ] Critérios de aceite estão claros
- [ ] Ambiente de testes está planejado
- [ ] Dados de teste estão identificados
- [ ] Definition of Done está estabelecida

### Time Preparado
- [ ] Time de implementação está alocado e disponível
- [ ] Competências necessárias estão no time (ou há plano de capacitação)
- [ ] Ferramentas e acessos necessários estão provisionados
- [ ] Ambientes de desenvolvimento estão configurados
- [ ] Dúvidas do time foram respondidas

---

## Critérios de Aprovação
- **Go**: Todos os itens marcados ou exceções justificadas e aceitas
- **No-Go condicional**: Até 3 itens pendentes com plano de resolução em 48h
- **No-Go**: Mais de 3 itens críticos pendentes ou bloqueantes não resolvidos

## Sinais de Alerta (Red Flags)
- Pressão para "Go" mesmo com itens críticos pendentes
- Time não participou da pré-programação e não entende a solução
- Decisões-chave foram adiadas para "durante a implementação"
- Nenhum risco identificado (análise insuficiente, não projeto perfeito)
- Stakeholders não revisaram ou aprovaram os artefatos

## Agente Responsável
**Agente de Final Review & Handoff** — responsável por conduzir a readiness review como gate keeper.
