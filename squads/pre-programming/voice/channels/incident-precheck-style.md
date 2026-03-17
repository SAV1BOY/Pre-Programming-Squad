# Estilo Pré-check de Incidente

## Formato

Checklist preventivo executado antes de deploys, migrações ou mudanças de alto risco. Estruturado como verificação sequencial com gates de aprovação. Cada item é binário (passa/não passa) com evidência obrigatória. O objetivo é capturar problemas antes que se tornem incidentes em produção.

## Estrutura

```
# Pré-check de Incidente — [Nome da Mudança]

## Metadata
- Mudança: [descrição concisa]
- Data planejada: [data e horário]
- Responsável: [pessoa executando a mudança]
- Aprovador: [pessoa que autoriza o go-ahead]
- Blast radius: [o que pode ser afetado se der errado]

## Gate 1: Prontidão Técnica
[Itens técnicos que devem estar OK antes de prosseguir]

## Gate 2: Prontidão Operacional
[Itens operacionais: monitoramento, rollback, comunicação]

## Gate 3: Prontidão Organizacional
[Pessoas disponíveis, stakeholders informados, horário adequado]

## Plano de Rollback
[Passos exatos para reverter se algo der errado]

## Critérios de Abort
[Condições que disparam rollback imediato]

## Veredicto
[GO / NO-GO com justificativa]
```

## Tom

- Disciplinado — cada item verificado com rigor
- Preventivo — mentalidade de "o que pode dar errado"
- Prático — foco em ação, não em teoria
- Sem pressão — o NO-GO é um resultado legítimo e protege a organização
- Baseado em evidência — "confie, mas verifique"

## Audiência

- Engenheiro responsável pela mudança
- SRE/DevOps que monitora durante a execução
- Tech lead que aprova o go-ahead
- On-call que pode ser acionado se houver incidente

## Exemplo

```
# Pré-check de Incidente — Migração de Banco do Serviço de Usuários

## Metadata
- Mudança: Migração de MongoDB 4.4 para PostgreSQL 16
  (serviço de usuários, ~2M registros)
- Data planejada: 15/mar/2025, sábado, 06:00 (janela de baixo tráfego)
- Responsável: Pedro Santos (@pedro)
- Aprovador: Ana Costa (Tech Lead)
- Blast radius: Serviço de usuários, login, cadastro,
  perfil — afeta 100% dos usuários se falhar
- Tempo estimado: 2 horas (06:00-08:00)
- Rollback estimado: 15 minutos

---

## Gate 1: Prontidão Técnica

| # | Item | Status | Evidência |
|---|---|---|---|
| 1.1 | Migração testada em staging com dados de produção | ✅ | Executada em 12/mar, 100% dos registros migrados, validação OK |
| 1.2 | Schema PostgreSQL revisado e aprovado | ✅ | Review do DBA @carlos em 11/mar, PR #487 |
| 1.3 | Dual-write ativo há 7+ dias sem erros | ✅ | Dashboard "dual-write-users": 7 dias, 0 erros, 0 divergências |
| 1.4 | Script de migração idempotente | ✅ | Testado 3x em staging, resultado idêntico |
| 1.5 | Queries do serviço otimizadas para PostgreSQL | ✅ | EXPLAIN ANALYZE em todas as queries críticas, PR #492 |
| 1.6 | Índices criados e validados | ✅ | 5 índices conforme spec, query plan OK |
| 1.7 | Connection pool dimensionado | ✅ | 30 conexões, load test sustentou 2x tráfego normal |
| 1.8 | Feature flag para switch de banco configurada | ✅ | LaunchDarkly flag "users-db-postgres", testada on/off em staging |

**Gate 1:** ✅ PASSA (8/8)

---

## Gate 2: Prontidão Operacional

| # | Item | Status | Evidência |
|---|---|---|---|
| 2.1 | Dashboard de monitoramento da migração criado | ✅ | Grafana "migration-users-mar15" com métricas de progresso |
| 2.2 | Alertas de erro rate configurados | ✅ | PagerDuty: alerta se error rate > 1% por 2 minutos |
| 2.3 | Alertas de latência configurados | ✅ | PagerDuty: alerta se p99 > 2s por 5 minutos |
| 2.4 | Runbook de migração escrito e revisado | ✅ | /docs/runbooks/migration-users-pg.md, revisado por @ana |
| 2.5 | Rollback testado em staging | ✅ | Feature flag off → revert para MongoDB em <30s |
| 2.6 | Backup do MongoDB pré-migração agendado | ✅ | mongodump agendado para 05:30, snapshot EBS às 05:45 |
| 2.7 | Comunicação para time de suporte preparada | ✅ | Mensagem no #suporte agendada para 05:50 |
| 2.8 | Página de status preparada | ✅ | statuspage.io atualizado com manutenção programada |

**Gate 2:** ✅ PASSA (8/8)

---

## Gate 3: Prontidão Organizacional

| # | Item | Status | Evidência |
|---|---|---|---|
| 3.1 | Engenheiro responsável disponível durante toda a janela | ✅ | @pedro confirmado 06:00-10:00 |
| 3.2 | Backup engineer disponível | ✅ | @julia como backup, confirmada |
| 3.3 | DBA disponível para emergência | ✅ | @carlos on-call, confirmado via Slack |
| 3.4 | Tech lead acessível para decisão de abort | ✅ | @ana acessível por telefone |
| 3.5 | Nenhum outro deploy concorrente na janela | ✅ | Deploy freeze confirmado das 00:00 de sex às 12:00 de sáb |
| 3.6 | Janela fora de pico de tráfego | ✅ | Sábado 06:00: ~5% do tráfego de pico |

**Gate 3:** ✅ PASSA (6/6)

---

## Plano de Rollback

1. Desligar feature flag "users-db-postgres" (switch para MongoDB)
   - Tempo: < 30 segundos
   - Executante: @pedro via LaunchDarkly
2. Verificar que 100% do tráfego voltou para MongoDB
   - Dashboard: "migration-users-mar15" → métricas MongoDB
3. Se dual-write divergiu: executar script de reconciliação
   - Script: /scripts/reconcile-users-db.sh
   - Tempo estimado: 10 minutos para 2M registros
4. Comunicar rollback no #suporte e statuspage

**RTO (Recovery Time Objective):** 15 minutos
**RPO (Recovery Point Objective):** 0 (dual-write garante ambos os bancos atualizados)

## Critérios de Abort

Abortar imediatamente se qualquer condição ocorrer:

- [ ] Error rate do serviço de usuários > 5% por mais de 1 minuto
- [ ] Latência p99 > 5s por mais de 2 minutos
- [ ] Divergência detectada entre MongoDB e PostgreSQL durante migração
- [ ] Qualquer erro de integridade de dados (constraint violation inesperada)
- [ ] Perda de conectividade com PostgreSQL por mais de 30 segundos
- [ ] Migração não concluída em 3 horas (150% do tempo estimado)

## Veredicto

### ✅ GO

Todos os 22 itens passaram. Equipe completa confirmada.
Janela de baixo risco. Rollback testado e rápido.

**Aprovado por:** Ana Costa (Tech Lead) — 14/mar/2025, 18:00
**Execução autorizada para:** 15/mar/2025, 06:00
```
