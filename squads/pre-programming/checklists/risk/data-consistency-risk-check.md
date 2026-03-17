# Checklist: Verificação de Risco de Consistência de Dados

## Propósito
Avaliar riscos de integridade e concorrência de dados, garantindo que o sistema mantém dados corretos mesmo em cenários de falha, concorrência e distribuição.

## Quando Usar
- Quando a solução envolve múltiplas fontes de dados ou escritas
- Ao projetar fluxos com transações distribuídas
- Quando consistência de dados é crítica para o negócio

---

## Checklist

### Integridade de Dados
- [ ] Constraints de integridade referencial estão definidas (FK, unique, not null)
- [ ] Validações de dados estão definidas em cada camada (API, negócio, banco)
- [ ] Regras de negócio que protegem integridade estão implementadas nos lugares certos
- [ ] Dados derivados/calculados têm mecanismo de recálculo/reconciliação
- [ ] Migração de dados preserva integridade (validação pós-migração)

### Concorrência
- [ ] Cenários de acesso concorrente ao mesmo recurso estão identificados
- [ ] Estratégia de locking está definida (otimista, pessimista, nenhum)
- [ ] Race conditions conhecidas estão mapeadas com mitigação
- [ ] Operações críticas são idempotentes (re-execução não causa duplicação)
- [ ] Conflitos de escrita simultânea têm resolução definida (last-write-wins, merge, erro)

### Consistência Distribuída
- [ ] Modelo de consistência está definido (forte, eventual, causal)
- [ ] Impacto de consistência eventual nos fluxos de negócio está avaliado
- [ ] Janela de inconsistência aceitável está definida
- [ ] Mecanismos de reconciliação para inconsistências temporárias existem
- [ ] Transações distribuídas (se existirem) têm estratégia definida (saga, 2PC)

### Proteção contra Perda
- [ ] Estratégia de backup está definida (frequência, retenção, teste de restore)
- [ ] Write-ahead log ou equivalente protege contra crash
- [ ] Dados em trânsito (filas, eventos) têm garantia de entrega definida (at-least-once, exactly-once)
- [ ] Duplicação de dados (replicação, cache) tem mecanismo de sincronização
- [ ] Ponto de recuperação (RPO) e tempo de recuperação (RTO) estão definidos

### Monitoramento de Dados
- [ ] Anomalias de dados são detectáveis (volume inesperado, valores fora do range)
- [ ] Drift de dados entre sistemas é monitorado
- [ ] Auditoria de mudanças em dados sensíveis está planejada
- [ ] Alertas para inconsistências de dados estão definidos
- [ ] Dashboard de saúde de dados está planejado

---

## Critérios de Aprovação
- **Mínimo**: Integridade e Concorrência completos
- **Recomendado**: Todos os itens marcados
- **Bloqueante**: Cenários de concorrência não mapeados em sistema com escrita simultânea

## Sinais de Alerta (Red Flags)
- "Não vai ter concorrência" em sistema com múltiplos usuários
- Nenhuma constraint no banco de dados (tudo validado "no código")
- Consistência eventual sem reconciliação
- Dados financeiros sem idempotência nas transações
- Backup nunca testado com restore real

## Agente Responsável
**Agente de Risk & Failure Analysis** — responsável por avaliar riscos de integridade e consistência de dados.
