# Checklist: Qualidade da Compatibilidade com Legado

## Propósito
Garantir que backward compatibility, estratégia de migração e blast radius estão avaliados quando a solução interage com ou substitui sistemas legados.

## Quando Usar
- Quando a solução modifica, substitui ou integra com sistemas existentes
- Antes de iniciar migrações de dados ou de sistema
- Quando há risco de quebrar funcionalidades existentes

---

## Checklist

### Backward Compatibility
- [ ] APIs existentes que serão afetadas estão listadas
- [ ] Consumidores das APIs existentes estão identificados
- [ ] Mudanças são backward-compatible ou têm plano de migração
- [ ] Período de coexistência (versão antiga + nova) está definido
- [ ] Testes de compatibilidade com consumidores existentes estão planejados

### Migração
- [ ] Estratégia de migração está definida (big bang, gradual, strangler fig)
- [ ] Plano de migração de dados está documentado com etapas
- [ ] Validação de dados pós-migração está definida
- [ ] Rollback de migração é possível e está planejado
- [ ] Janela de migração está acordada com stakeholders

### Blast Radius
- [ ] Sistemas que podem ser afetados por falha na migração estão mapeados
- [ ] Impacto máximo de uma falha está quantificado (usuários, receita, operação)
- [ ] Estratégia de contenção de blast radius está definida (feature flag, canary)
- [ ] Monitoramento específico para período de migração está planejado
- [ ] Critérios de abort (quando parar a migração) estão definidos

### Coexistência
- [ ] Período de operação simultânea (legado + novo) está planejado
- [ ] Consistência de dados durante coexistência está garantida
- [ ] Roteamento entre versões está definido (como decidir quem usa o quê)
- [ ] Plano de descomissionamento do legado está definido com data
- [ ] Custo de manter duas versões simultaneamente está estimado

### Comunicação
- [ ] Times afetados foram notificados sobre as mudanças
- [ ] Cronograma de migração foi compartilhado com consumidores
- [ ] Documentação de migração para consumidores está planejada
- [ ] Canal de suporte durante migração está definido
- [ ] Critérios de sucesso da migração estão compartilhados

---

## Critérios de Aprovação
- **Mínimo**: Backward Compatibility e Blast Radius completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Migração sem rollback ou consumidores não mapeados

## Sinais de Alerta (Red Flags)
- "Vamos substituir tudo de uma vez" sem plano de rollback
- Consumidores do sistema legado não foram consultados
- Migração de dados sem validação pós-migração
- Nenhum período de coexistência planejado
- "O sistema legado vai ser desligado semana que vem" sem preparação

## Agente Responsável
**Agente de Risk & Failure Analysis** — em colaboração com o **Agente de Solution Architecture**.
