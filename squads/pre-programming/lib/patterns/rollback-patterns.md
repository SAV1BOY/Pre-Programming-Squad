# Padrões de Rollback

## Nome do Padrão
Padrões para Planejamento de Estratégias de Rollback

## Problema que Resolve
Deploys falhos sem plano de rollback resultam em: downtime prolongado, perda de dados, decisões apressadas sob pressão e impacto descontrolado nos usuários. Planejar rollback desde a pré-programação reduz drasticamente o tempo de recuperação.

## Solução

### 1. Rollback Imutável (Immutable Rollback)
Manter versões anteriores do sistema prontas para reimplantação instantânea, sem necessidade de reverter código ou reconstruir artefatos.

**Aplicação prática:**
- Manter pelo menos 3 versões anteriores de containers/artefatos
- Usar blue-green deployment para troca instantânea
- Banco de dados compatível com versão N e N-1
- Testar rollback como parte do pipeline de CI/CD

### 2. Feature Flag como Rollback
Usar feature flags para desabilitar funcionalidades problemáticas sem necessidade de redeploy.

**Aplicação prática:**
- Toda feature nova atrás de flag
- Flags gerenciadas por sistema centralizado
- Killswitch com desabilitação em < 1 minuto
- Flags removidas após período de estabilização

### 3. Compensação Transacional (Saga Reversal)
Para operações distribuídas, planejar transações de compensação que desfazem os efeitos de operações já completadas.

**Aplicação prática:**
- Mapear cada operação e sua operação reversa
- Implementar compensação idempotente
- Registrar log de compensação para auditoria
- Definir timeout para compensação automática

### 4. Rollback de Dados com Snapshot
Manter snapshots do estado dos dados antes de mudanças críticas, permitindo restauração pontual.

**Aplicação prática:**
- Snapshot antes de migrações de schema
- Backup incremental antes de operações em lote
- Point-in-time recovery configurado e testado
- Validação de integridade pós-restauração

## Quando Usar

- Em todo deploy para produção
- Em migrações de dados e schema
- Em mudanças de infraestrutura
- Em integrações com sistemas críticos
- Em operações que afetam dados financeiros

## Quando NÃO Usar

- Em ambientes de desenvolvimento local
- Em deploys de documentação estática
- Quando o custo do rollback excede o custo de fix-forward
- Em sistemas com estado irrecuperável por design (ex: blockchain)

## Exemplos

### Exemplo 1: Plano de Rollback para Deploy de API
```
Critérios de ativação:
  - Taxa de erro > 5% por 3 minutos
  - Latência p99 > 5x da baseline
  - Funcionalidade crítica indisponível

Procedimento (tempo total: < 5 min):
  1. Ativar killswitch da feature (1 min)
  2. Se insuficiente: reverter para versão anterior (2 min)
  3. Se insuficiente: rollback de banco para snapshot (5 min)
  4. Notificar stakeholders via canal #incidents

Verificação pós-rollback:
  - Confirmar métricas normalizadas
  - Executar smoke tests automatizados
  - Verificar integridade de dados
```

### Exemplo 2: Compensação em Saga de Pedido
```
Fluxo normal:
  1. Reservar estoque      -> Compensação: liberar estoque
  2. Processar pagamento   -> Compensação: estornar pagamento
  3. Criar pedido          -> Compensação: cancelar pedido
  4. Notificar cliente     -> Compensação: notificar cancelamento

Se falhar no passo 3:
  - Executar compensação 2 (estornar pagamento)
  - Executar compensação 1 (liberar estoque)
  - Registrar motivo da falha
  - Notificar equipe de suporte
```

### Exemplo 3: Feature Flags como Mecanismo de Rollback
```
Feature: Novo algoritmo de recomendação

Flag: "recommendation_v2_enabled"
  Padrão: false (desabilitado)
  Rollout: 5% -> 25% -> 50% -> 100% (ao longo de 2 semanas)

Monitoramento:
  - CTR (Click Through Rate) das recomendações
  - Tempo de resposta do endpoint
  - Taxa de conversão

Critério de rollback: CTR cai > 10% vs. controle
Ação: Desabilitar flag (< 30 segundos, sem deploy)
```
