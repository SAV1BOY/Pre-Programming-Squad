# Template: Plano de Rollback

## Título
Rollback Plan — Plano de Reversão em Caso de Falha

## Propósito
Definir procedimentos claros e testados para reverter uma implantação que cause problemas em produção, minimizando o tempo de indisponibilidade e o impacto nos usuários.

## Quando Usar
- Antes de qualquer deploy em produção (obrigatório).
- Quando há mudanças de banco de dados, infraestrutura ou integrações.
- Em releases de alto risco ou que afetam muitos usuários.

## Seções

### 1. Informações Gerais
| Campo | Valor |
|-------|-------|
| Projeto | `[nome do projeto]` |
| Release | `[versão]` |
| Data | `[YYYY-MM-DD]` |
| Responsável pelo Rollback | `[nome]` |
| Tempo Máximo de Rollback (RTO) | `[minutos]` |

### 2. Gatilhos de Rollback
| Gatilho | Threshold | Quem Decide | Tempo para Decisão |
|---------|-----------|------------|---------------------|
| `[error rate elevado]` | `[> 5% por 5 min]` | `[papel]` | `[X min]` |
| `[latência degradada]` | `[p99 > 3s por 10 min]` | `[papel]` | `[X min]` |
| `[funcionalidade quebrada]` | `[feature crítica indisponível]` | `[papel]` | `[imediato]` |
| `[perda de dados]` | `[qualquer ocorrência]` | `[papel]` | `[imediato]` |

### 3. Procedimento de Rollback

#### Passo 1: Confirmação
- [ ] Confirmar que o problema é causado pelo deploy (e não por fator externo)
- [ ] Notificar equipe de plantão no canal `[canal]`
- [ ] Decisor autoriza o rollback

#### Passo 2: Execução
- [ ] `[Comando/ação para reverter a aplicação]`
- [ ] `[Comando/ação para reverter migrations (se aplicável)]`
- [ ] `[Comando/ação para reverter feature flags]`
- [ ] `[Comando/ação para reverter configurações de infra]`

#### Passo 3: Verificação
- [ ] Confirmar que a versão anterior está rodando
- [ ] Verificar métricas de saúde (error rate, latência, disponibilidade)
- [ ] Testar funcionalidades críticas manualmente
- [ ] Confirmar integridade dos dados

#### Passo 4: Comunicação
- [ ] Notificar equipe técnica sobre o rollback
- [ ] Notificar stakeholders sobre o impacto
- [ ] Criar incidente no sistema de tracking

### 4. Rollback de Banco de Dados
| Migration | Script de Rollback | Testado? | Perda de Dados? | Tempo Estimado |
|-----------|-------------------|----------|----------------|----------------|
| `[migration]` | `[script]` | `[Sim/Não]` | `[Sim/Não — detalhe]` | `[minutos]` |

### 5. Rollback de Infraestrutura
| Componente | Estado Anterior | Procedimento | Tempo Estimado |
|------------|----------------|-------------|----------------|
| `[componente]` | `[configuração anterior]` | `[como reverter]` | `[minutos]` |

### 6. Cenários Onde Rollback NÃO é Possível
| Cenário | Motivo | Plano Alternativo |
|---------|--------|------------------|
| `[cenário]` | `[por que não pode reverter]` | `[o que fazer ao invés]` |

### 7. Contatos de Emergência
| Papel | Nome | Contato | Quando Acionar |
|-------|------|---------|----------------|
| `[papel]` | `[nome]` | `[telefone/Slack]` | `[em que situação]` |

## Exemplo de Preenchimento

### 3. Procedimento de Rollback — Passo 2
- [ ] Reverter deploy: `kubectl rollout undo deployment/api-service -n production`
- [ ] Reverter feature flag: Desativar flag `new-checkout-flow` no LaunchDarkly
- [ ] Reverter migration: `psql -f rollback_v2.3.sql` (testado em staging em 2026-03-15)
- [ ] Reverter config de CDN: Apontar para versão anterior do bundle no S3

### 6. Cenários Onde Rollback NÃO é Possível
| Cenário | Motivo | Plano Alternativo |
|---------|--------|------------------|
| Migration que remove coluna com dados | Dados perdidos não podem ser restaurados | Backup point-in-time + restore seletivo |
| Integração com parceiro já ativada | Parceiro não suporta reversão | Desativar feature flag e tratar dados em transição |

## Dicas de Qualidade
- **Teste o rollback:** Um plano não testado é um plano que não funciona.
- **Automatize quando possível:** Rollback manual sob pressão é propenso a erros.
- **Pense em dados:** Rollback de código é fácil. Rollback de dados é o problema real.
- **Defina quem decide:** Em uma crise, não pode haver dúvida sobre quem autoriza o rollback.
- **Pratique:** Faça simulações de rollback regularmente. A equipe deve conhecer o procedimento.
