# Checklist: Qualidade da Prontidão para Refatoração de Legado

## Propósito
Garantir que refatorações de sistemas legados têm boundaries claros, characterization tests, e estratégia de rollout segura antes de modificar código existente.

## Quando Usar
- Antes de iniciar refatoração de código ou sistema legado
- Quando a solução envolve modernização de componentes existentes
- Ao planejar migração incremental de legado

---

## Checklist

### Boundaries (Fronteiras)
- [ ] Fronteiras do código a ser refatorado estão claramente delimitadas
- [ ] Interfaces públicas do módulo legado estão documentadas
- [ ] Dependentes (quem consome o módulo) estão mapeados
- [ ] Dependências (do que o módulo depende) estão mapeadas
- [ ] Escopo da refatoração está limitado (não "reescrever tudo")

### Characterization Tests
- [ ] Comportamento atual do sistema está documentado com testes
- [ ] Testes de caracterização cobrem happy paths existentes
- [ ] Testes de caracterização cobrem edge cases conhecidos
- [ ] Comportamentos indesejados mas existentes estão documentados (bugs conhecidos)
- [ ] Testes podem ser executados automaticamente antes e depois da mudança

### Entendimento do Legado
- [ ] Razão de existência do código legado é compreendida
- [ ] Débitos técnicos conhecidos estão catalogados
- [ ] Regras de negócio embutidas no código estão extraídas e documentadas
- [ ] Dados e estados mantidos pelo sistema legado estão mapeados
- [ ] Histórico de incidentes relacionados ao legado está consultado

### Estratégia de Rollout
- [ ] Abordagem de rollout está definida (strangler fig, feature flag, canary)
- [ ] Critérios de rollout progressivo estão definidos (% de tráfego, por região, etc.)
- [ ] Período de coexistência legado + novo está planejado
- [ ] Monitoramento comparativo (legado vs novo) está definido
- [ ] Critérios de sucesso para cada fase do rollout estão definidos

### Segurança da Mudança
- [ ] Rollback é possível em cada fase do rollout
- [ ] Tempo de rollback está estimado
- [ ] Impacto em dados durante coexistência está avaliado
- [ ] Alertas específicos para a refatoração estão planejados
- [ ] Plano de comunicação para incidentes durante rollout existe

---

## Critérios de Aprovação
- **Mínimo**: Boundaries e Characterization Tests completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Sem characterization tests ou sem rollback planejado

## Sinais de Alerta (Red Flags)
- "Vamos reescrever do zero" sem entender o legado completamente
- Nenhum characterization test antes de modificar
- Refatoração com big bang deploy sem rollout gradual
- Regras de negócio no legado que ninguém entende
- "Vamos aproveitar e mudar tudo de uma vez"

## Agente Responsável
**Agente de Solution Architecture** — em colaboração com o **Agente de Risk & Failure Analysis**.
