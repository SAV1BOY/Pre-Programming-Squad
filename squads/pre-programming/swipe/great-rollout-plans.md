# Ótimos Planos de Rollout — Exemplos Anotados

## Introdução

Um plano de rollout excepcional transforma um deploy arriscado em um processo controlado e reversível. Ele define quem faz o quê, quando, em que ordem, como verificar sucesso e como reverter se algo der errado. Os melhores planos de rollout são testados em staging antes de serem executados em produção e tratam o deploy como uma operação crítica, não como "só dar push".

---

## Exemplo 1 — Rollout de Nova Arquitetura de Pagamentos

### O Plano

> **Estratégia**: Canary deployment com progressive rollout
>
> **Fases**:
> 1. **Canary (2%)**: 500 sellers selecionados (mix de volume alto/baixo). Duração: 48h. Critérios de avanço: taxa de erro < 0.1%, latência p99 < 500ms, zero transações perdidas.
> 2. **Early Adopters (10%)**: Sellers que optaram por beta. Duração: 1 semana. Mesmo critérios + feedback qualitativo.
> 3. **Rollout Gradual (25% -> 50% -> 75%)**: Incrementos a cada 48h com verificação automática de métricas.
> 4. **General Availability (100%)**: Feature flag removida. Código legado marcado para remoção em 30 dias.
>
> **Critérios de Rollback Automático**: Taxa de erro > 1%, latência p99 > 2s, alertas de perda de transação.
>
> **Runbook de Rollback**: (1) Desativar feature flag via dashboard — efeito imediato. (2) Se flag não funcionar: revert do deploy via pipeline — 5 minutos. (3) Se pipeline falhar: rollback manual de container image — 10 minutos.
>
> **Comunicação**: Slack #deploys para time técnico. E-mail pré-agendado para sellers afetados 24h antes. Status page atualizada durante rollout.
>
> **Janela**: Terça-feira, 10h-16h (horário de menor volume, equipe completa disponível). Nunca na sexta.

### Por que funciona

- **Progressão gradual com critérios claros**: Cada fase tem métricas de go/no-go
- **Rollback em camadas**: Feature flag, pipeline, manual — três níveis de segurança
- **Janela estratégica**: Menor volume, equipe presente, longe do final de semana
- **Comunicação planejada**: Cada audiência com canal e timing adequados

---

## Exemplo 2 — Rollout de Migração de Banco de Dados

### O Plano

> **Estratégia**: Blue-Green com dual-write
>
> **Pré-requisitos**: Backup validado, migration scripts testados 3x em staging, monitoring dashboards preparados, equipe de plantão confirmada.
>
> **Sequência**:
> 1. T-24h: Backup completo + validação de restore em ambiente isolado
> 2. T-4h: Ativar dual-write (MySQL primary + PostgreSQL secondary)
> 3. T-2h: Validar consistência entre bancos (script de reconciliação)
> 4. T-0: Switch de reads para PostgreSQL (via config, sem deploy)
> 5. T+1h: Validar métricas e erros. Se OK, desativar reads do MySQL
> 6. T+24h: Se estável, desativar writes para MySQL
> 7. T+7d: Descomissionar MySQL (manter backup por 90 dias)
>
> **Rollback em cada etapa**:
> - Até T+1h: Reverter config de reads para MySQL — 30 segundos
> - T+1h a T+24h: Reativar reads no MySQL, dados consistentes via dual-write
> - Após T+24h: Restore do MySQL a partir do último backup + replay de eventos

### Por que funciona

- **Timeline detalhada**: Cada passo com horário relativo — sem ambiguidade
- **Rollback por etapa**: Cada fase tem seu próprio caminho de volta
- **Período de coexistência**: 7 dias de MySQL ativo como segurança
- **Backup com validação**: Não basta ter backup — precisa validar o restore

---

## Lições Extraídas

1. **Nunca faça rollout big-bang**: Progressão gradual é obrigatória para mudanças significativas
2. **Feature flags são seu melhor amigo**: Permitem rollback instantâneo sem deploy
3. **Defina critérios de rollback antes de precisar deles**: Em modo de crise não é hora de decidir
4. **Teste o rollback, não apenas o deploy**: Se o rollback nunca foi testado, ele não funciona
5. **Escolha a janela com cuidado**: Menor tráfego, equipe completa, longe de feriados e sextas
6. **Comunique proativamente**: Stakeholders surpresos por downtime são stakeholders furiosos
7. **Automatize ao máximo**: Quanto menos passos manuais, menos erro humano
8. **Mantenha o caminho de volta aberto**: Não descomissione o sistema antigo até ter certeza
